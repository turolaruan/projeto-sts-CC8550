"""User related business logic."""

from __future__ import annotations

from typing import List

from src.models import UserCreate, UserModel, UserUpdate
from src.repositories import UserRepository

from .exceptions import BusinessRuleError, NotFoundError


class UserService:
    """Encapsulates high-level operations for users."""

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, payload: UserCreate) -> UserModel:
        """Register a new user ensuring e-mail uniqueness."""

        existing = await self.repository.find_by_email(payload.email)
        if existing:
            raise BusinessRuleError("E-mail already registered")
        return await self.repository.create(payload.model_dump())

    async def list_users(self) -> List[UserModel]:
        """Return all users."""

        return await self.repository.list()

    async def get_user(self, user_id: str) -> UserModel:
        """Fetch a user by id or raise."""

        user = await self.repository.get_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")
        return user

    async def update_user(self, user_id: str, payload: UserUpdate) -> UserModel:
        """Update user properties."""

        data = {k: v for k, v in payload.model_dump(exclude_none=True).items()}
        updated = await self.repository.update(user_id, data)
        if not updated:
            raise NotFoundError("User not found")
        return updated

    async def delete_user(self, user_id: str) -> bool:
        """Remove a user."""

        deleted = await self.repository.delete(user_id)
        if not deleted:
            raise NotFoundError("User not found")
        return deleted
