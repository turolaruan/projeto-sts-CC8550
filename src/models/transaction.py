"""Transaction domain and API models."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from pydantic import Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import TransactionType


class TransactionBase(DocumentModel):
    """Shared transaction attributes."""

    user_id: ObjectIdStr
    account_id: ObjectIdStr
    category_id: ObjectIdStr
    amount: Decimal = Field(gt=Decimal("0"))
    transaction_type: TransactionType
    occurred_at: datetime = Field(default_factory=now_utc)
    description: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None, max_length=1000)
    counterparty: str | None = Field(default=None, max_length=120)
    transfer_account_id: ObjectIdStr | None = None

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal) -> Decimal:
        """Normalize monetary amount."""
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @field_validator("description")
    @classmethod
    def normalize_description(cls, value: str | None) -> str | None:
        """Strip description if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "description")


class TransactionCreate(TransactionBase):
    """Payload for creating transactions."""

    model_config = {"extra": "forbid"}


class TransactionUpdate(DocumentModel):
    """Payload for updating transactions."""

    amount: Decimal | None = Field(default=None, gt=Decimal("0"))
    occurred_at: datetime | None = None
    description: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None, max_length=1000)
    counterparty: str | None = Field(default=None, max_length=120)

    model_config = {"extra": "forbid"}

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal | None) -> Decimal | None:
        """Normalize amount when provided."""
        if value is None:
            return value
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @field_validator("description")
    @classmethod
    def normalize_description(cls, value: str | None) -> str | None:
        """Normalize description when provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "description")


class Transaction(TransactionBase):
    """Represents a stored transaction."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def build_transaction(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )
