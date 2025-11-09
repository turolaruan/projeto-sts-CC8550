"""Business logic for managing accounts."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import List

from src.models.account import Account, AccountCreate, AccountUpdate, build_account
from src.models.common import now_utc
from src.repositories.account_repository import AccountRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.utils.exceptions import EntityNotFoundError, ValidationAppError


class AccountService:
    """Encapsulates account-related workflows."""

    def __init__(
        self,
        repository: AccountRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository

    async def create_account(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def list_accounts(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def get_account(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def update_account(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def delete_account(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def adjust_balance(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def set_balance(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def _ensure_user_exists(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
