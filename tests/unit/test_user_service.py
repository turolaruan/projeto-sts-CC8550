"""Tests for UserService covering validation-heavy paths."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.models.enums import CurrencyCode
from src.models.user import UserCreate, UserUpdate
from src.services.user_service import UserService
from src.utils.exceptions import EntityAlreadyExistsError, EntityNotFoundError, ValidationAppError
from tests.structural.helpers import build_user


def _make_service():
    repository = SimpleNamespace(
        create=AsyncMock(),
        list=AsyncMock(return_value=[]),
        get=AsyncMock(),
        update=AsyncMock(),
        delete=AsyncMock(return_value=True),
    )
    service = UserService(repository)
    return service, repository


def _payload(**overrides: object) -> UserCreate:
    data = {
        "name": "Usuário Serviço",
        "email": "user@example.com",
        "default_currency": CurrencyCode.BRL,
    }
    data.update(overrides)
    return UserCreate(**data)


@pytest.mark.asyncio
async def test_create_user_rejects_duplicate_email() -> None:
    service, repository = _make_service()
    repository.list.return_value = [build_user()]

    with pytest.raises(EntityAlreadyExistsError):
        await service.create_user(_payload())

    repository.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_list_users_forwards_filters() -> None:
    service, repository = _make_service()
    await service.list_users(name="Ana", email="ana@example.com", default_currency=CurrencyCode.BRL)
    repository.list.assert_awaited_once_with(name="Ana", email="ana@example.com", default_currency=CurrencyCode.BRL)


@pytest.mark.asyncio
async def test_update_user_rejects_empty_payload() -> None:
    service, _ = _make_service()

    with pytest.raises(ValidationAppError):
        await service.update_user("user-id", UserUpdate())


@pytest.mark.asyncio
async def test_update_user_raises_when_repository_returns_none() -> None:
    service, repository = _make_service()
    repository.update.return_value = None

    with pytest.raises(EntityNotFoundError):
        await service.update_user("user-id", UserUpdate(name="Novo"))


@pytest.mark.asyncio
async def test_delete_user_raises_when_repository_reports_missing() -> None:
    service, repository = _make_service()
    repository.delete.return_value = False

    with pytest.raises(EntityNotFoundError):
        await service.delete_user("user-id")
