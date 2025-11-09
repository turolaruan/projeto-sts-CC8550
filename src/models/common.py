"""Common utilities and base classes for models."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field

ObjectIdStr = Annotated[
    str,
    Field(min_length=24, max_length=24, pattern=r"^[0-9a-fA-F]{24}$"),
]


class DocumentModel(BaseModel):
    """Base model configuring Pydantic for Mongo compatibility."""

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={
            ObjectId: lambda oid: str(oid),
            Decimal: lambda value: str(value),
        },
        use_enum_values=True,
    )


def generate_object_id() -> str:
    """Return a new ObjectId as hexadecimal string."""
    return str(ObjectId())


def ensure_object_id(value: str) -> ObjectId:
    """Convert hex string to ObjectId or raise ValueError."""
    if not ObjectId.is_valid(value):
        raise ValueError(f"Invalid ObjectId: {value}")
    return ObjectId(value)


def now_utc() -> datetime:
    """Return an aware datetime in UTC."""
    return datetime.now(tz=timezone.utc)


def strip_and_validate_non_empty(value: str, field_name: str) -> str:
    """Strip whitespace and ensure value is not empty."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} must not be empty")
    return cleaned
