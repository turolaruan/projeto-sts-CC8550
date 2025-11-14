"""Business logic around financial accounts."""

from __future__ import annotations

from typing import List

from src.models import AccountCreate, AccountModel, AccountUpdate
from src.repositories import AccountRepository, UserRepository

from .exceptions import NotFoundError


class AccountService:
    """Operations for managing accounts."""

    def __init__(self, repository: AccountRepository, user_repository: UserRepository) -> None:
        self.repository = repository
        self.user_repository = user_repository

    async def create_account(self, payload: AccountCreate) -> AccountModel:
        """Create a new account ensuring the user exists."""

        user = await self.user_repository.get_by_id(payload.user_id)
        if not user:
            raise NotFoundError("User not found for account creation")
        return await self.repository.create(payload.model_dump())

    async def list_accounts(self, user_id: str) -> List[AccountModel]:
        """Return all accounts for a user."""

        return await self.repository.find_by_user(user_id)

    async def get_account(self, account_id: str) -> AccountModel:
        """Return account by id or raise."""

        account = await self.repository.get_by_id(account_id)
        if not account:
            raise NotFoundError("Account not found")
        return account

    async def update_account(self, account_id: str, payload: AccountUpdate) -> AccountModel:
        """Update account fields."""

        data = payload.model_dump(exclude_none=True)
        updated = await self.repository.update(account_id, data)
        if not updated:
            raise NotFoundError("Account not found")
        return updated

    async def delete_account(self, account_id: str) -> bool:
        """Delete an account."""

        deleted = await self.repository.delete(account_id)
        if not deleted:
            raise NotFoundError("Account not found")
        return deleted
