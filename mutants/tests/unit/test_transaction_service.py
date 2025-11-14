"""TransactionService tests covering complex validation and budget logic."""

from __future__ import annotations

from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import AsyncMock, call

import pytest

from src.models.enums import CategoryType, TransactionType
from src.models.transaction import TransactionCreate, TransactionUpdate
from src.services.transaction_service import TransactionService
from src.utils.exceptions import EntityNotFoundError, ValidationAppError
from tests.structural.helpers import (
    UTC_NOW,
    build_account,
    build_budget,
    build_category,
    build_transaction,
    build_user,
)

USER_ID = "64f6d1250a1b2c3d4e5f6789"
ACCOUNT_ID = "65f6d1250a1b2c3d4e5f6789"
CATEGORY_ID = "66f6d1250a1b2c3d4e5f6789"
OTHER_USER_ID = "71f6d1250a1b2c3d4e5f6789"
TRANSFER_ACCOUNT_ID = "77f6d1250a1b2c3d4e5f6789"
TRANSACTION_ID = "67f6d1250a1b2c3d4e5f6789"


def _make_service(
    *,
    account=None,
    transfer_account=None,
    category=None,
    user=None,
    transaction=None,
):
    account = account or build_account(id=ACCOUNT_ID, user_id=USER_ID)
    transfer_account = transfer_account or build_account(id=TRANSFER_ACCOUNT_ID, user_id=USER_ID)
    category = category or build_category(id=CATEGORY_ID, user_id=USER_ID, category_type=CategoryType.EXPENSE)
    user = user or build_user(id=USER_ID)
    transaction = transaction or build_transaction(id=TRANSACTION_ID, user_id=USER_ID, account_id=ACCOUNT_ID, category_id=CATEGORY_ID)

    async def account_get(account_id: str):
        if account_id == account.id:
            return account
        if account_id == transfer_account.id:
            return transfer_account
        return None

    repository = SimpleNamespace(
        create=AsyncMock(),
        list=AsyncMock(return_value=[transaction]),
        get=AsyncMock(return_value=transaction),
        update=AsyncMock(return_value=transaction),
        delete=AsyncMock(return_value=True),
        sum_for_category_period=AsyncMock(return_value=Decimal("0")),
    )
    account_service = SimpleNamespace(adjust_balance=AsyncMock())
    account_repository = SimpleNamespace(get=AsyncMock(side_effect=account_get))
    category_repository = SimpleNamespace(get=AsyncMock(return_value=category))
    user_repository = SimpleNamespace(get=AsyncMock(return_value=user))
    budget_repository = SimpleNamespace(list=AsyncMock(return_value=[]))

    service = TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )
    return SimpleNamespace(
        service=service,
        repository=repository,
        account_service=account_service,
        account_repository=account_repository,
        category_repository=category_repository,
        user_repository=user_repository,
        budget_repository=budget_repository,
        default_account=account,
        transfer_account=transfer_account,
        default_category=category,
        default_transaction=transaction,
    )


def _transfer_payload(**overrides: object) -> TransactionCreate:
    data = {
        "user_id": USER_ID,
        "account_id": ACCOUNT_ID,
        "category_id": CATEGORY_ID,
        "amount": Decimal("100.00"),
        "transaction_type": TransactionType.TRANSFER,
        "occurred_at": UTC_NOW,
        "transfer_account_id": TRANSFER_ACCOUNT_ID,
    }
    data.update(overrides)
    return TransactionCreate(**data)


def _expense_payload(**overrides: object) -> TransactionCreate:
    data = {
        "user_id": USER_ID,
        "account_id": ACCOUNT_ID,
        "category_id": CATEGORY_ID,
        "amount": Decimal("50.00"),
        "transaction_type": TransactionType.EXPENSE,
        "occurred_at": UTC_NOW,
    }
    data.update(overrides)
    return TransactionCreate(**data)


@pytest.mark.asyncio
async def test_create_transaction_requires_transfer_destination() -> None:
    ctx = _make_service()
    payload = _transfer_payload(transfer_account_id=None)

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(payload)

    ctx.repository.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_create_transaction_rejects_same_transfer_account() -> None:
    ctx = _make_service()
    payload = _transfer_payload(transfer_account_id=ACCOUNT_ID)

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(payload)


@pytest.mark.asyncio
async def test_create_transaction_respects_budget_limit() -> None:
    ctx = _make_service()
    budget = build_budget(user_id=USER_ID, category_id=CATEGORY_ID, year=UTC_NOW.year, month=UTC_NOW.month, amount=Decimal("80.00"))
    ctx.budget_repository.list.return_value = [budget]
    ctx.repository.sum_for_category_period.return_value = Decimal("70.00")
    payload = _expense_payload(amount=Decimal("20.00"))

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(payload)

    ctx.account_service.adjust_balance.assert_not_called()


@pytest.mark.asyncio
async def test_create_transaction_validates_category_user_mismatch() -> None:
    ctx = _make_service()
    ctx.category_repository.get.return_value = build_category(
        id=CATEGORY_ID, user_id=OTHER_USER_ID, category_type=CategoryType.EXPENSE
    )

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(_expense_payload())


@pytest.mark.asyncio
async def test_create_transaction_requires_existing_user() -> None:
    ctx = _make_service()
    ctx.user_repository.get.return_value = None

    with pytest.raises(EntityNotFoundError):
        await ctx.service.create_transaction(_expense_payload())


@pytest.mark.asyncio
async def test_create_transaction_rejects_account_user_mismatch() -> None:
    foreign_account = build_account(id=ACCOUNT_ID, user_id=OTHER_USER_ID)
    ctx = _make_service(account=foreign_account)

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(_expense_payload())


@pytest.mark.asyncio
async def test_create_transaction_validates_category_type_for_income() -> None:
    ctx = _make_service()

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(_expense_payload(transaction_type=TransactionType.INCOME))


@pytest.mark.asyncio
async def test_create_transaction_requires_transfer_account_same_user() -> None:
    foreign_transfer = build_account(id=TRANSFER_ACCOUNT_ID, user_id=OTHER_USER_ID)
    ctx = _make_service(transfer_account=foreign_transfer)

    with pytest.raises(ValidationAppError):
        await ctx.service.create_transaction(_transfer_payload())


@pytest.mark.asyncio
async def test_list_transactions_forward_filters_to_repository() -> None:
    ctx = _make_service()

    transactions = await ctx.service.list_transactions(
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.EXPENSE,
        transfer_account_id=TRANSFER_ACCOUNT_ID,
        date_from=UTC_NOW,
        date_to=UTC_NOW,
    )

    ctx.repository.list.assert_awaited_once_with(
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.EXPENSE,
        transfer_account_id=TRANSFER_ACCOUNT_ID,
        date_from=UTC_NOW,
        date_to=UTC_NOW,
    )
    assert transactions


@pytest.mark.asyncio
async def test_get_transaction_missing_raises() -> None:
    ctx = _make_service()
    ctx.repository.get.return_value = None

    with pytest.raises(EntityNotFoundError):
        await ctx.service.get_transaction("missing")


@pytest.mark.asyncio
async def test_update_transaction_rejects_empty_payload() -> None:
    ctx = _make_service()

    with pytest.raises(ValidationAppError):
        await ctx.service.update_transaction(TRANSACTION_ID, TransactionUpdate())


@pytest.mark.asyncio
async def test_update_transaction_adjusts_balance_when_amount_changes() -> None:
    ctx = _make_service()
    transaction = build_transaction(
        id=TRANSACTION_ID,
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.EXPENSE,
        amount=Decimal("20.00"),
    )
    ctx.repository.get.return_value = transaction
    ctx.repository.update.return_value = transaction

    await ctx.service.update_transaction(TRANSACTION_ID, TransactionUpdate(amount=Decimal("35.00")))

    ctx.account_service.adjust_balance.assert_called_once_with(ACCOUNT_ID, Decimal("-15.00"))


@pytest.mark.asyncio
async def test_update_transaction_raises_when_repository_returns_none() -> None:
    ctx = _make_service()
    ctx.repository.update.return_value = None

    with pytest.raises(EntityNotFoundError):
        await ctx.service.update_transaction(TRANSACTION_ID, TransactionUpdate(description="desc"))


@pytest.mark.asyncio
async def test_delete_transaction_reverts_balance_effect() -> None:
    ctx = _make_service()
    transaction = build_transaction(
        id=TRANSACTION_ID,
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.EXPENSE,
        amount=Decimal("25.00"),
    )
    ctx.repository.get.return_value = transaction
    ctx.repository.delete.return_value = True

    await ctx.service.delete_transaction(TRANSACTION_ID)

    ctx.account_service.adjust_balance.assert_called_once_with(ACCOUNT_ID, Decimal("25.00"))


@pytest.mark.asyncio
async def test_delete_transaction_raises_when_repository_returns_false() -> None:
    ctx = _make_service()
    ctx.repository.delete.return_value = False

    with pytest.raises(EntityNotFoundError):
        await ctx.service.delete_transaction(TRANSACTION_ID)


@pytest.mark.asyncio
async def test_apply_balance_delta_income_adjusts_positive_delta() -> None:
    ctx = _make_service()
    transaction = build_transaction(
        id=TRANSACTION_ID,
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.INCOME,
    )
    ctx.account_service.adjust_balance.reset_mock()

    await ctx.service._apply_balance_delta(transaction, Decimal("15.005"))

    ctx.account_service.adjust_balance.assert_awaited_once_with(ACCOUNT_ID, Decimal("15.01"))


@pytest.mark.asyncio
async def test_apply_balance_delta_transfer_requires_destination_account() -> None:
    ctx = _make_service()
    transaction = build_transaction(
        id=TRANSACTION_ID,
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.TRANSFER,
        transfer_account_id=None,
    )

    with pytest.raises(ValidationAppError):
        await ctx.service._apply_balance_delta(transaction, Decimal("10.00"))


@pytest.mark.asyncio
async def test_apply_balance_delta_transfer_updates_both_accounts() -> None:
    ctx = _make_service()
    transaction = build_transaction(
        id=TRANSACTION_ID,
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        transaction_type=TransactionType.TRANSFER,
        transfer_account_id=TRANSFER_ACCOUNT_ID,
    )
    ctx.account_service.adjust_balance.reset_mock()

    await ctx.service._apply_balance_delta(transaction, Decimal("25.00"))

    ctx.account_service.adjust_balance.assert_has_awaits(
        [
            call(ACCOUNT_ID, Decimal("-25.00")),
            call(TRANSFER_ACCOUNT_ID, Decimal("25.00")),
        ]
    )
