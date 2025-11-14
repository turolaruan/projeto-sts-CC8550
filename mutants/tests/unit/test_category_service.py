"""Focused tests for CategoryService validation branches."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.models.category import CategoryCreate, CategoryUpdate
from src.models.enums import CategoryType
from src.services.category_service import CategoryService
from src.utils.exceptions import EntityNotFoundError, ValidationAppError
from tests.structural.helpers import build_category

USER_ID = "64f6d1250a1b2c3d4e5f6789"
CATEGORY_ID = "66f6d1250a1b2c3d4e5f6789"
PARENT_ID = "77f6d1250a1b2c3d4e5f6789"
OTHER_USER_ID = "70f6d1250a1b2c3d4e5f6789"


def _make_service():
    repository = SimpleNamespace(
        create=AsyncMock(),
        list=AsyncMock(return_value=[]),
        get=AsyncMock(return_value=build_category(id=CATEGORY_ID, user_id=USER_ID)),
        update=AsyncMock(),
        delete=AsyncMock(return_value=True),
    )
    user_repository = SimpleNamespace(get=AsyncMock(return_value={"id": USER_ID}))
    transaction_repository = SimpleNamespace(exists_for_category=AsyncMock(return_value=False))
    budget_repository = SimpleNamespace(list=AsyncMock(return_value=[]))
    service = CategoryService(repository, user_repository, transaction_repository, budget_repository)
    return service, repository, user_repository, transaction_repository, budget_repository


def _payload(**overrides: object) -> CategoryCreate:
    data = {
        "user_id": USER_ID,
        "name": "Categoria",
        "category_type": CategoryType.EXPENSE,
        "description": None,
        "parent_id": None,
    }
    data.update(overrides)
    return CategoryCreate(**data)


@pytest.mark.asyncio
async def test_create_category_requires_existing_user() -> None:
    service, _, user_repository, __, ___ = _make_service()
    user_repository.get.return_value = None

    with pytest.raises(EntityNotFoundError):
        await service.create_category(_payload())


@pytest.mark.asyncio
async def test_create_category_validates_parent_presence() -> None:
    service, repository, _, __, ___ = _make_service()
    repository.get.return_value = None

    with pytest.raises(EntityNotFoundError):
        await service.create_category(_payload(parent_id=PARENT_ID))


@pytest.mark.asyncio
async def test_update_category_rejects_empty_payload() -> None:
    service, _, __, ___, ____ = _make_service()

    with pytest.raises(ValidationAppError):
        await service.update_category(CATEGORY_ID, CategoryUpdate())


@pytest.mark.asyncio
async def test_update_category_validates_parent_user_and_self_reference() -> None:
    service, repository, _, __, ____ = _make_service()
    category = build_category(id=CATEGORY_ID, user_id=USER_ID, category_type=CategoryType.EXPENSE)
    parent = build_category(id=PARENT_ID, user_id=OTHER_USER_ID, category_type=CategoryType.EXPENSE)
    repository.get.side_effect = [category, parent]

    with pytest.raises(ValidationAppError):
        await service.update_category(
            CATEGORY_ID,
            CategoryUpdate(parent_id=PARENT_ID),
        )


@pytest.mark.asyncio
async def test_delete_category_blocks_when_transactions_exist() -> None:
    service, repository, __, transaction_repository, ___ = _make_service()
    transaction_repository.exists_for_category.return_value = True

    with pytest.raises(ValidationAppError):
        await service.delete_category(CATEGORY_ID)

    repository.delete.assert_not_awaited()


@pytest.mark.asyncio
async def test_delete_category_blocks_when_budget_exists() -> None:
    service, repository, __, transaction_repository, budget_repository = _make_service()
    transaction_repository.exists_for_category.return_value = False
    budget_repository.list.return_value = [object()]

    with pytest.raises(ValidationAppError):
        await service.delete_category(CATEGORY_ID)

    repository.delete.assert_not_awaited()


@pytest.mark.asyncio
async def test_delete_category_raises_when_repository_reports_missing() -> None:
    service, repository, __, transaction_repository, budget_repository = _make_service()
    transaction_repository.exists_for_category.return_value = False
    budget_repository.list.return_value = []
    repository.delete.return_value = False

    with pytest.raises(EntityNotFoundError):
        await service.delete_category(CATEGORY_ID)
