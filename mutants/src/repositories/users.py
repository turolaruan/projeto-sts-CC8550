"""User repository implementation."""

from __future__ import annotations

from typing import Optional

from src.models import UserModel
from src.utils import serialize_document

from .base import AbstractRepository


class UserRepository(AbstractRepository[UserModel]):
    """Manages persistence for users."""

    collection_name = "users"
    model = UserModel

    async def find_by_email(self, email: str) -> Optional[UserModel]:
        """Return a user matching the provided e-mail."""

        document = await self.collection.find_one({"email": email})
        return UserModel(**serialize_document(document)) if document else None
