"""Account repository implementation."""

from __future__ import annotations

from typing import Optional

from src.models import AccountModel
from src.utils import serialize_document

from .base import AbstractRepository


class AccountRepository(AbstractRepository[AccountModel]):
    """Persistence operations for financial accounts."""

    collection_name = "accounts"
    model = AccountModel

    async def find_by_user(self, user_id: str) -> list[AccountModel]:
        """Return all accounts for a user."""

        return await self.list({"user_id": user_id})

    async def adjust_balance(self, account_id: str, delta: float) -> Optional[AccountModel]:
        """Increment balance atomically and return the updated account."""

        await self.collection.update_one(
            {"_id": self._to_object_id(account_id)},
            {"$inc": {"balance": delta}},
        )
        document = await self.collection.find_one({"_id": self._to_object_id(account_id)})
        return AccountModel(**serialize_document(document)) if document else None

    async def update_goal_lock(self, account_id: str, delta: float) -> Optional[AccountModel]:
        """Increment the reserved goal amount."""

        await self.collection.update_one(
            {"_id": self._to_object_id(account_id)},
            {"$inc": {"goal_locked_amount": delta}},
        )
        document = await self.collection.find_one({"_id": self._to_object_id(account_id)})
        return AccountModel(**serialize_document(document)) if document else None
