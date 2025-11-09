"""User domain and API models."""

from __future__ import annotations

from datetime import datetime
from pydantic import EmailStr, Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import CurrencyCode


class UserBase(DocumentModel):
    """Shared attributes for user representations."""

    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    default_currency: CurrencyCode = Field(default=CurrencyCode.BRL)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not blank and normalize whitespace."""
        return strip_and_validate_non_empty(value, "name")

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        """Ensure email is lower-case for uniqueness."""
        return value.lower()


class UserCreate(UserBase):
    """Payload for creating users."""

    model_config = {"extra": "forbid"}


class UserUpdate(DocumentModel):
    """Payload for updating users."""

    name: str | None = Field(default=None, min_length=3, max_length=100)
    default_currency: CurrencyCode | None = None

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Ensure updated name is valid if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "name")


class User(UserBase):
    """Represents a user in the system."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


class UserInDB(User):
    """Alias for clarity when dealing with persisted entities."""


def build_user(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )
