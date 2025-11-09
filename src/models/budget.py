"""Budget domain and API models."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from pydantic import Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
)


class BudgetBase(DocumentModel):
    """Shared attributes for budgets."""

    user_id: ObjectIdStr
    category_id: ObjectIdStr
    year: int = Field(ge=2000, le=2100)
    month: int = Field(ge=1, le=12)
    amount: Decimal = Field(gt=Decimal("0"))
    alert_percentage: int = Field(default=80, ge=1, le=100)

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal) -> Decimal:
        """Normalize amount to two decimals."""
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class BudgetCreate(BudgetBase):
    """Payload for creating budgets."""

    model_config = {"extra": "forbid"}


class BudgetUpdate(DocumentModel):
    """Payload for updating budgets."""

    amount: Decimal | None = Field(default=None, gt=Decimal("0"))
    alert_percentage: int | None = Field(default=None, ge=1, le=100)

    model_config = {"extra": "forbid"}

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal | None) -> Decimal | None:
        if value is None:
            return None
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class Budget(BudgetBase):
    """Represents a stored budget."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def build_budget(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )
