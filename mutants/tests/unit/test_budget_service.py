"""Targeted tests for BudgetService to harden validation branches."""

from __future__ import annotations

from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.models.budget import BudgetCreate, BudgetUpdate
from src.models.enums import CategoryType
from src.services.budget_service import BudgetService
from src.utils.exceptions import EntityAlreadyExistsError, EntityNotFoundError, ValidationAppError
from tests.structural.helpers import build_budget, build_category

USER_ID = "64f6d1250a1b2c3d4e5f6789"
CATEGORY_ID = "66f6d1250a1b2c3d4e5f6789"
BUDGET_ID = "68f6d1250a1b2c3d4e5f6789"
OTHER_USER_ID = "70f6d1250a1b2c3d4e5f6789"


def _make_service():
    repository = SimpleNamespace(
        create=AsyncMock(),
        list=AsyncMock(return_value=[]),
        get=AsyncMock(),
        update=AsyncMock(),
        delete=AsyncMock(),
        find_by_period=AsyncMock(return_value=None),
    )
    user_repository = SimpleNamespace(get=AsyncMock(return_value={"id": USER_ID}))
    category_repository = SimpleNamespace(
        get=AsyncMock(return_value=build_category(id=CATEGORY_ID, user_id=USER_ID, category_type=CategoryType.EXPENSE))
    )
    transaction_repository = SimpleNamespace(
        exists_for_category=AsyncMock(return_value=False),
    )
    service = BudgetService(repository, user_repository, category_repository, transaction_repository)
    return service, repository, user_repository, category_repository, transaction_repository


def _payload(**overrides: object) -> BudgetCreate:
    data = {
        "user_id": USER_ID,
        "category_id": CATEGORY_ID,
        "year": 2024,
        "month": 6,
        "amount": Decimal("500.00"),
        "alert_percentage": 70,
    }
    data.update(overrides)
    return BudgetCreate(**data)


@pytest.mark.asyncio
async def test_create_budget_rejects_category_from_other_user() -> None:
    service, repository, _, category_repo, _ = _make_service()
    category_repo.get.return_value = build_category(id=CATEGORY_ID, user_id=OTHER_USER_ID, category_type=CategoryType.EXPENSE)

    with pytest.raises(ValidationAppError):
        await service.create_budget(_payload())

    repository.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_create_budget_rejects_non_expense_category() -> None:
    service, repository, _, category_repo, _ = _make_service()
    category_repo.get.return_value = build_category(id=CATEGORY_ID, user_id=USER_ID, category_type=CategoryType.INCOME)

    with pytest.raises(ValidationAppError):
        await service.create_budget(_payload())

    repository.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_create_budget_detects_duplicate_period() -> None:
    service, repository, _, __, ___ = _make_service()
    repository.find_by_period.return_value = build_budget()

    with pytest.raises(EntityAlreadyExistsError):
        await service.create_budget(_payload())


@pytest.mark.asyncio
async def test_update_budget_rejects_empty_payload() -> None:
    service, _, __, ___, ____ = _make_service()

    with pytest.raises(ValidationAppError):
        await service.update_budget("budget-id", BudgetUpdate())


@pytest.mark.asyncio
async def test_delete_budget_prevents_when_transactions_exist() -> None:
    service, repository, __, ___, transaction_repo = _make_service()
    budget = build_budget(id=BUDGET_ID, user_id=USER_ID, category_id=CATEGORY_ID, year=2024, month=6)
    repository.get.return_value = budget
    transaction_repo.exists_for_category.return_value = True

    with pytest.raises(ValidationAppError):
        await service.delete_budget(budget.id)

    repository.delete.assert_not_awaited()


@pytest.mark.asyncio
async def test_delete_budget_raises_when_repository_reports_missing() -> None:
    service, repository, __, ___, transaction_repo = _make_service()
    budget = build_budget(id=BUDGET_ID, user_id=USER_ID, category_id=CATEGORY_ID, year=2024, month=6)
    repository.get.return_value = budget
    transaction_repo.exists_for_category.return_value = False
    repository.delete.return_value = False

    with pytest.raises(EntityNotFoundError):
        await service.delete_budget(budget.id)
