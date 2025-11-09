"""Category domain and API models."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import CategoryType


class CategoryBase(DocumentModel):
    """Shared category attributes."""

    user_id: ObjectIdStr
    name: str = Field(min_length=2, max_length=100)
    category_type: CategoryType
    description: str | None = Field(default=None, max_length=255)
    parent_id: ObjectIdStr | None = Field(default=None)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not blank and normalize."""
        return strip_and_validate_non_empty(value, "name")


class CategoryCreate(CategoryBase):
    """Payload for creating categories."""

    model_config = {"extra": "forbid"}


class CategoryUpdate(DocumentModel):
    """Payload for updating categories."""

    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    parent_id: ObjectIdStr | None = Field(default=None)

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Ensure updated name is valid if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "name")


class Category(CategoryBase):
    """Represents a stored category."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def build_category(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )
