"""Business logic coordinating transactions."""

from __future__ import annotations

from typing import List

from src.models import (
    BudgetModel,
    TransactionCreate,
    TransactionFilter,
    TransactionModel,
    TransactionType,
    TransactionUpdate,
)
from src.repositories import AccountRepository, TransactionRepository, UserRepository

from .exceptions import BusinessRuleError, NotFoundError
from .goals import GoalService
from .budgets import BudgetService


class TransactionService:
    """Coordinates validation and persistence of transactions."""

    def __init__(
        self,
        repository: TransactionRepository,
        account_repository: AccountRepository,
        user_repository: UserRepository,
        budget_service: BudgetService,
        goal_service: GoalService,
    ) -> None:
        self.repository = repository
        self.account_repository = account_repository
        self.user_repository = user_repository
        self.budget_service = budget_service
        self.goal_service = goal_service

    async def create_transaction(self, payload: TransactionCreate) -> TransactionModel:
        """Validate and persist a new transaction."""

        user = await self.user_repository.get_by_id(payload.user_id)
        if not user:
            raise NotFoundError("User not found")
        account = await self.account_repository.get_by_id(payload.account_id)
        if not account:
            raise NotFoundError("Account not found")
        if account.user_id != payload.user_id:
            raise BusinessRuleError("Account does not belong to user")

        is_expense = payload.type in {TransactionType.EXPENSE, TransactionType.TRANSFER}
        is_goal_contribution = payload.goal_id is not None
        if is_expense:
            available_balance = account.balance - account.goal_locked_amount
            if available_balance < payload.amount:
                raise BusinessRuleError("Insufficient balance considering locked funds")
        budget = await self._get_budget(payload, skip_budget=is_goal_contribution)

        if payload.type == TransactionType.INCOME:
            await self.account_repository.adjust_balance(payload.account_id, payload.amount)
        elif is_expense and not is_goal_contribution:
            await self.account_repository.adjust_balance(payload.account_id, -payload.amount)

        if budget:
            await self.budget_service.apply_expense(budget, payload.amount)

        if payload.goal_id:
            if payload.type != TransactionType.EXPENSE:
                raise BusinessRuleError("Goal contributions must be expense transactions")
            await self.goal_service.apply_contribution(payload.goal_id, payload.amount)

        transaction = await self.repository.create(payload.model_dump())
        return transaction

    async def _get_budget(self, payload: TransactionCreate, skip_budget: bool) -> BudgetModel | None:
        """Return active budget for expense transactions when needed."""

        if skip_budget:
            return None
        if payload.type != TransactionType.EXPENSE or not payload.category:
            return None
        return await self.budget_service.get_budget_for(
            payload.user_id,
            payload.category,
            payload.event_date.date(),
        )

    async def list_transactions(self, user_id: str) -> List[TransactionModel]:
        """Return all transactions for a user."""

        return await self.repository.list({"user_id": user_id})

    async def get_transaction(self, transaction_id: str) -> TransactionModel:
        """Fetch transaction by id or raise."""

        transaction = await self.repository.get_by_id(transaction_id)
        if not transaction:
            raise NotFoundError("Transaction not found")
        return transaction

    async def update_transaction(self, transaction_id: str, payload: TransactionUpdate) -> TransactionModel:
        """Update mutable fields of a transaction."""

        data = payload.model_dump(exclude_none=True)
        updated = await self.repository.update(transaction_id, data)
        if not updated:
            raise NotFoundError("Transaction not found")
        return updated

    async def delete_transaction(self, transaction_id: str) -> bool:
        """Delete a transaction by id."""

        deleted = await self.repository.delete(transaction_id)
        if not deleted:
            raise NotFoundError("Transaction not found")
        return deleted

    async def search_transactions(self, filters: TransactionFilter) -> List[TransactionModel]:
        """Perform filtered search with ordering."""

        return await self.repository.search(filters)
