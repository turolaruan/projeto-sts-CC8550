"""Business logic for managing users."""

from __future__ import annotations

from typing import List

from src.models.common import now_utc
from src.models.user import User, UserCreate, UserUpdate, build_user
from src.repositories.base import Repository
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)


class UserService:
    """Encapsulates user-related operations and business rules."""

    def __init__(self, repository: Repository[User, str]) -> None:
        self._repository = repository

    async def create_user(self, payload: UserCreate) -> User:
        """Create a new user ensuring email uniqueness."""
        await self._ensure_unique_email(payload.email)
        user = build_user(payload)
        await self._repository.create(user)
        return user

    async def list_users(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def get_user(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return user

    async def update_user(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def delete_user(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def _ensure_unique_email(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"email": email},
            )
