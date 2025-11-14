"""Tests for ReportService aggregation logic."""

from __future__ import annotations

from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.models.enums import CategoryType, TransactionType
from src.services.report_service import ReportService
from src.utils.exceptions import EntityNotFoundError
from tests.structural.helpers import build_budget, build_category

USER_ID = "64f6d1250a1b2c3d4e5f6789"
CATEGORY_ID = "66f6d1250a1b2c3d4e5f6789"


def _make_service():
    transaction_repository = SimpleNamespace(
        aggregate_monthly_summary=AsyncMock(return_value=[]),
    )
    category_repository = SimpleNamespace(get=AsyncMock())
    budget_repository = SimpleNamespace(list=AsyncMock(return_value=[]))
    service = ReportService(transaction_repository, category_repository, budget_repository)
    return service, transaction_repository, category_repository, budget_repository


@pytest.mark.asyncio
async def test_monthly_summary_raises_when_category_missing() -> None:
    service, transaction_repository, category_repository, _ = _make_service()
    transaction_repository.aggregate_monthly_summary.return_value = [
        {"category_id": CATEGORY_ID, "transaction_type": TransactionType.EXPENSE.value, "total": "100.00", "count": 1}
    ]
    category_repository.get.return_value = None

    with pytest.raises(EntityNotFoundError):
        await service.monthly_summary(USER_ID, 2024, 7)


@pytest.mark.asyncio
async def test_monthly_summary_calculates_budget_remaining() -> None:
    service, transaction_repository, category_repository, budget_repository = _make_service()
    category = build_category(id=CATEGORY_ID, user_id=USER_ID, name="Moradia", category_type=CategoryType.EXPENSE)
    category_repository.get.side_effect = lambda category_id: category if category_id == CATEGORY_ID else None
    transaction_repository.aggregate_monthly_summary.return_value = [
        {"category_id": CATEGORY_ID, "transaction_type": TransactionType.EXPENSE.value, "total": "150.00", "count": 2}
    ]
    budget = build_budget(user_id=USER_ID, category_id=CATEGORY_ID, amount=Decimal("300.00"), year=2024, month=7)
    budget_repository.list.return_value = [budget]

    summary = await service.monthly_summary(USER_ID, 2024, 7)

    assert summary.totals_by_type[TransactionType.EXPENSE] == Decimal("150.00")
    assert len(summary.categories) == 1
    item = summary.categories[0]
    assert item.category_id == CATEGORY_ID
    assert item.budget_amount == Decimal("300.00")
    assert item.budget_remaining == Decimal("150.00")
