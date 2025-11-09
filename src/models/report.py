"""Report response models."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, List

from pydantic import Field

from src.models.common import DocumentModel, ObjectIdStr
from src.models.enums import TransactionType


class MonthlyCategorySummary(DocumentModel):
    """Aggregated summary for a category in a month."""

    category_id: ObjectIdStr
    name: str
    transaction_type: TransactionType
    total: Decimal = Field(default=Decimal("0"))
    count: int = Field(default=0, ge=0)
    budget_amount: Decimal | None = None
    budget_remaining: Decimal | None = None


class MonthlySummary(DocumentModel):
    """Monthly summary report for a user."""

    user_id: ObjectIdStr
    year: int
    month: int
    totals_by_type: Dict[TransactionType, Decimal]
    categories: List[MonthlyCategorySummary]
