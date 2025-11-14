"""Focused tests for AccountService validations to improve mutation coverage."""

from __future__ import annotations

from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from src.models.account import AccountCreate, AccountUpdate
from src.models.enums import AccountType, CurrencyCode
from src.services.account_service import AccountService
from src.utils.exceptions import EntityNotFoundError, ValidationAppError
from tests.structural.helpers import build_account

USER_ID = "64f6d1250a1b2c3d4e5f6789"


def _make_service():
    account_repository = SimpleNamespace(
        create=AsyncMock(),
        list=AsyncMock(),
        get=AsyncMock(),
        update=AsyncMock(),
        delete=AsyncMock(),
    )
    user_repository = SimpleNamespace(get=AsyncMock(return_value={"id": USER_ID}))
    transaction_repository = SimpleNamespace(exists_for_account=AsyncMock(return_value=False))
    service = AccountService(account_repository, user_repository, transaction_repository)
    return service, account_repository, user_repository, transaction_repository


def _sample_payload(**overrides: object) -> AccountCreate:
    data = {
        "user_id": USER_ID,
        "name": "Conta Teste",
        "account_type": AccountType.CHECKING,
        "currency": CurrencyCode.BRL,
        "starting_balance": Decimal("100.00"),
        "minimum_balance": Decimal("10.00"),
    }
    data.update(overrides)
    return AccountCreate(**data)


@pytest.mark.asyncio
async def test_create_account_requires_existing_user() -> None:
    service, account_repo, user_repo, _ = _make_service()
    user_repo.get.return_value = None

    with pytest.raises(EntityNotFoundError):
        await service.create_account(_sample_payload())

    account_repo.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_create_account_rejects_starting_balance_below_minimum() -> None:
    service, account_repo, _, __ = _make_service()
    payload = _sample_payload(starting_balance=Decimal("5.00"), minimum_balance=Decimal("10.00"))

    with pytest.raises(ValidationAppError):
        await service.create_account(payload)

    account_repo.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_update_account_rejects_empty_payload() -> None:
    service, _, __, ___ = _make_service()

    with pytest.raises(ValidationAppError):
        await service.update_account("acc", AccountUpdate())


@pytest.mark.asyncio
async def test_update_account_rejects_minimum_above_balance() -> None:
    service, account_repo, _, __ = _make_service()
    account = build_account(balance=Decimal("100.00"), minimum_balance=Decimal("10.00"))
    account_repo.get.return_value = account

    with pytest.raises(ValidationAppError):
        await service.update_account(account.id, AccountUpdate(minimum_balance=Decimal("150.00")))

    account_repo.update.assert_not_awaited()


@pytest.mark.asyncio
async def test_update_account_raises_when_repository_returns_none() -> None:
    service, account_repo, _, __ = _make_service()
    account = build_account()
    account_repo.get.return_value = account
    account_repo.update.return_value = None

    with pytest.raises(EntityNotFoundError):
        await service.update_account(account.id, AccountUpdate(name="Nova Conta"))


@pytest.mark.asyncio
async def test_delete_account_blocks_when_transactions_exist() -> None:
    service, account_repo, _, transaction_repo = _make_service()
    transaction_repo.exists_for_account.return_value = True

    with pytest.raises(ValidationAppError):
        await service.delete_account("account-id")

    account_repo.delete.assert_not_awaited()


@pytest.mark.asyncio
async def test_delete_account_raises_when_repository_reports_missing() -> None:
    service, account_repo, _, transaction_repo = _make_service()
    transaction_repo.exists_for_account.return_value = False
    account_repo.delete.return_value = False

    with pytest.raises(EntityNotFoundError):
        await service.delete_account("account-id")


@pytest.mark.asyncio
async def test_adjust_balance_rejects_drop_below_minimum() -> None:
    service, account_repo, _, __ = _make_service()
    account = build_account(balance=Decimal("50.00"), minimum_balance=Decimal("20.00"))
    account_repo.get.return_value = account

    with pytest.raises(ValidationAppError):
        await service.adjust_balance(account.id, Decimal("-40.00"))

    account_repo.update.assert_not_awaited()


@pytest.mark.asyncio
async def test_adjust_balance_updates_repository_on_success() -> None:
    service, account_repo, _, __ = _make_service()
    account = build_account(balance=Decimal("100.00"), minimum_balance=Decimal("10.00"))
    updated_account = account.model_copy(update={"balance": Decimal("90.00")})
    account_repo.get.return_value = account
    account_repo.update.return_value = updated_account

    result = await service.adjust_balance(account.id, Decimal("-10.00"))

    account_repo.update.assert_awaited_once()
    assert result.balance == Decimal("90.00")


@pytest.mark.asyncio
async def test_set_balance_rejects_value_below_minimum() -> None:
    service, account_repo, _, __ = _make_service()
    account = build_account(balance=Decimal("50.00"), minimum_balance=Decimal("25.00"))
    account_repo.get.return_value = account

    with pytest.raises(ValidationAppError):
        await service.set_balance(account.id, Decimal("20.00"))

