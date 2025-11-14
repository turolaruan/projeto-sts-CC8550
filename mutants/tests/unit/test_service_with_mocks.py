"""Unit tests using mocks/stubs to isolate service dependencies."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.models.enums import CurrencyCode
from src.models.user import UserCreate
from src.services.user_service import UserService
from src.utils.exceptions import EntityAlreadyExistsError, EntityNotFoundError
from tests.structural.helpers import build_user


@pytest.mark.asyncio
async def test_user_service_create_with_mocked_repository() -> None:
    """Ensure create_user uses repository mocks and isolates persistence."""
    repository = SimpleNamespace(
        list=AsyncMock(return_value=[]),
        create=AsyncMock(),
    )
    service = UserService(repository)  # type: ignore[arg-type]
    payload = UserCreate(
        name="Usuario Mock",
        email="mock@example.com",
        default_currency=CurrencyCode.EUR,
    )

    user = await service.create_user(payload)

    repository.list.assert_awaited_once_with(email="mock@example.com")
    repository.create.assert_awaited_once()
    created_user = repository.create.await_args.args[0]
    assert created_user.email == "mock@example.com"
    assert user.id == created_user.id


@pytest.mark.asyncio
async def test_user_service_prevents_duplicate_email_and_simulates_error() -> None:
    """Simulate error response when repository mock reports existing email."""
    existing = build_user(email="dup@example.com")
    repository = SimpleNamespace(
        list=AsyncMock(return_value=[existing]),
        create=AsyncMock(),
    )
    service = UserService(repository)  # type: ignore[arg-type]
    payload = UserCreate(
        name="Duplicado",
        email="dup@example.com",
        default_currency=CurrencyCode.BRL,
    )

    with pytest.raises(EntityAlreadyExistsError):
        await service.create_user(payload)

    repository.create.assert_not_called()


@pytest.mark.asyncio
async def test_user_service_get_user_handles_not_found_with_mock() -> None:
    """Ensure get_user raises correct exception using isolated mock repository."""
    repository = SimpleNamespace(
        get=AsyncMock(return_value=None),
    )
    service = UserService(repository)  # type: ignore[arg-type]

    with pytest.raises(EntityNotFoundError):
        await service.get_user("missing-id")

    repository.get.assert_awaited_once_with("missing-id")
