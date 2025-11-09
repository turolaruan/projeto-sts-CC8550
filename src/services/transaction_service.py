"""Business logic for managing transactions."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import List

from src.models.enums import CategoryType, TransactionType
from src.models.transaction import (
    Transaction,
    TransactionCreate,
    TransactionUpdate,
    build_transaction,
)
from src.repositories.account_repository import AccountRepository
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.services.account_service import AccountService
from src.models.common import now_utc
from src.utils.exceptions import EntityNotFoundError, ValidationAppError


class TransactionService:
    """Encapsulates transaction workflows and financial adjustments."""

    def __init__(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = account_service
        self._account_repository = account_repository
        self._category_repository = category_repository
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    async def create_transaction(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def list_transactions(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def get_transaction(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        return transaction

    async def update_transaction(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def delete_transaction(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def _apply_balance_delta(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def _ensure_budget_allows(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def _get_account(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def _get_category(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def _ensure_user_exists(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    def _ensure_same_user(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def _validate_category_for_transaction(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
