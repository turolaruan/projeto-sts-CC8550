"""Account domain and API models."""

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
from src.models.enums import AccountType, CurrencyCode


class AccountBase(DocumentModel):
    """Shared account attributes."""

    user_id: ObjectIdStr
    name: str = Field(min_length=3, max_length=120)
    account_type: AccountType
    currency: CurrencyCode = Field(default=CurrencyCode.BRL)
    description: str | None = Field(default=None, max_length=255)
    minimum_balance: Decimal = Field(default=Decimal("0"))

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not blank and normalize whitespace."""
        return strip_and_validate_non_empty(value, "name")

    @field_validator("minimum_balance")
    @classmethod
    def normalize_minimum_balance(cls, value: Decimal) -> Decimal:
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class AccountCreate(AccountBase):
    """Payload for creating accounts."""

    starting_balance: Decimal = Field(default=Decimal("0"))

    model_config = {"extra": "forbid"}

    @field_validator("starting_balance")
    @classmethod
    def validate_balance(cls, value: Decimal) -> Decimal:
        """Normalize decimal to two fraction digits."""
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class AccountUpdate(DocumentModel):
    """Payload for updating accounts."""

    name: str | None = Field(default=None, min_length=3, max_length=120)
    description: str | None = Field(default=None, max_length=255)
    account_type: AccountType | None = None
    currency: CurrencyCode | None = None
    minimum_balance: Decimal | None = None

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Ensure updated name is valid if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "name")

    @field_validator("minimum_balance")
    @classmethod
    def normalize_minimum_balance(cls, value: Decimal | None) -> Decimal | None:
        if value is None:
            return None
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class Account(AccountBase):
    """Represents a stored account."""

    id: ObjectIdStr
    balance: Decimal = Field(default=Decimal("0"))
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def build_account(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )
