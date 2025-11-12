"""Structural tests ensuring FastAPI controllers handle success/error paths."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from fastapi import HTTPException
from src.controllers import (
    accounts as accounts_ctrl,
    budgets as budgets_ctrl,
    categories as categories_ctrl,
    health as health_ctrl,
    reports as reports_ctrl,
    transactions as transactions_ctrl,
    users as users_ctrl,
)
from src.config.settings import Settings
from src.models.account import AccountCreate, AccountUpdate
from src.models.budget import BudgetCreate, BudgetUpdate
from src.models.category import CategoryCreate, CategoryUpdate
from src.models.common import generate_object_id
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import TransactionCreate, TransactionUpdate
from src.models.user import UserCreate, UserUpdate
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)
from tests.structural.helpers import (
    UTC_NOW,
    build_account,
    build_budget,
    build_category,
    build_transaction,
    build_user,
)


# ---------------------------------------------------------------------------
# Users controller
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_users_controller_success_flows() -> None:
    user = build_user()
    updated_user = user.model_copy(update={"name": "Atualizado"})
    service = SimpleNamespace(
        create_user=AsyncMock(return_value=user),
        list_users=AsyncMock(return_value=[user]),
        get_user=AsyncMock(return_value=user),
        update_user=AsyncMock(return_value=updated_user),
        delete_user=AsyncMock(return_value=None),
    )
    payload = UserCreate(name="Teste", email="teste@example.com", default_currency=CurrencyCode.USD)

    created = await users_ctrl.create_user(payload, service=service)
    users = await users_ctrl.list_users(
        name=None,
        email=None,
        default_currency=None,
        service=service,
    )
    fetched = await users_ctrl.get_user(created.id, service=service)
    updated = await users_ctrl.update_user(created.id, UserUpdate(name="Outro"), service=service)
    response = await users_ctrl.delete_user(created.id, service=service)

    assert created.email.endswith("@example.com")
    assert len(users) == 1
    assert fetched.id == created.id
    assert updated.name == "Atualizado"
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_users_controller_error_branches() -> None:
    payload = UserCreate(name="Dup", email="dup@example.com", default_currency=CurrencyCode.BRL)
    service = SimpleNamespace(
        create_user=AsyncMock(side_effect=EntityAlreadyExistsError("exists")),
        update_user=AsyncMock(side_effect=ValidationAppError("invalid")),
        delete_user=AsyncMock(side_effect=EntityNotFoundError("missing")),
        get_user=AsyncMock(side_effect=EntityNotFoundError("missing")),
    )

    with pytest.raises(HTTPException) as excinfo:
        await users_ctrl.create_user(payload, service=service)
    assert excinfo.value.status_code == 409

    with pytest.raises(HTTPException) as excinfo:
        await users_ctrl.update_user("user", UserUpdate(), service=service)
    assert excinfo.value.status_code == 400

    with pytest.raises(HTTPException) as excinfo:
        await users_ctrl.delete_user("user", service=service)
    assert excinfo.value.status_code == 404

    with pytest.raises(HTTPException):
        await users_ctrl.get_user("user", service=service)


# ---------------------------------------------------------------------------
# Accounts controller
# ---------------------------------------------------------------------------


def _account_payload(user_id: str | None = None) -> AccountCreate:
    user_id = user_id or generate_object_id()
    return AccountCreate(
        user_id=user_id,
        name="Conta",
        account_type=AccountType.CHECKING,
        currency=CurrencyCode.BRL,
        starting_balance=Decimal("100.00"),
    )


@pytest.mark.asyncio
async def test_accounts_controller_success_paths() -> None:
    account = build_account()
    user_id = account.user_id
    service = SimpleNamespace(
        create_account=AsyncMock(return_value=account),
        list_accounts=AsyncMock(return_value=[account]),
        get_account=AsyncMock(return_value=account),
        update_account=AsyncMock(return_value=account),
        delete_account=AsyncMock(return_value=None),
    )

    created = await accounts_ctrl.create_account(_account_payload(user_id), service=service)
    accounts = await accounts_ctrl.list_accounts(
        user_id=None,
        account_type=None,
        currency=None,
        name=None,
        service=service,
    )
    fetched = await accounts_ctrl.get_account(account.id, service=service)
    updated = await accounts_ctrl.update_account(account.id, AccountUpdate(name="Nova"), service=service)
    response = await accounts_ctrl.delete_account(account.id, service=service)

    assert created.id == account.id
    assert len(accounts) == 1
    assert fetched.id == account.id
    assert updated.id == account.id
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_accounts_controller_error_paths() -> None:
    service = SimpleNamespace(
        create_account=AsyncMock(side_effect=EntityNotFoundError("user missing")),
    )
    payload = _account_payload(generate_object_id())
    with pytest.raises(HTTPException) as excinfo:
        await accounts_ctrl.create_account(payload, service=service)
    assert excinfo.value.status_code == 404

    service.create_account.side_effect = ValidationAppError("invalid")
    with pytest.raises(HTTPException) as excinfo:
        await accounts_ctrl.create_account(payload, service=service)
    assert excinfo.value.status_code == 400

    service.get_account = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await accounts_ctrl.get_account("acc", service=service)

    service.update_account = AsyncMock(side_effect=ValidationAppError("invalid"))
    with pytest.raises(HTTPException) as excinfo:
        await accounts_ctrl.update_account("acc", AccountUpdate(), service=service)
    assert excinfo.value.status_code == 400

    service.update_account.side_effect = EntityNotFoundError("missing")
    with pytest.raises(HTTPException) as excinfo:
        await accounts_ctrl.update_account("acc", AccountUpdate(name="Conta X"), service=service)
    assert excinfo.value.status_code == 404

    service.delete_account = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await accounts_ctrl.delete_account("acc", service=service)


# ---------------------------------------------------------------------------
# Budgets controller
# ---------------------------------------------------------------------------


def _budget_payload(user_id: str, category_id: str) -> BudgetCreate:
    return BudgetCreate(
        user_id=user_id,
        category_id=category_id,
        year=2024,
        month=6,
        amount=Decimal("500.00"),
        alert_percentage=80,
    )


@pytest.mark.asyncio
async def test_budgets_controller_success_paths() -> None:
    budget = build_budget()
    updated_budget = budget.model_copy(update={"amount": Decimal("600.00")})
    service = SimpleNamespace(
        create_budget=AsyncMock(return_value=budget),
        list_budgets=AsyncMock(return_value=[budget]),
        get_budget=AsyncMock(return_value=budget),
        update_budget=AsyncMock(return_value=updated_budget),
        delete_budget=AsyncMock(return_value=None),
    )

    created = await budgets_ctrl.create_budget(
        _budget_payload(budget.user_id, budget.category_id),
        service=service,
    )
    budgets = await budgets_ctrl.list_budgets(
        user_id=None,
        category_id=None,
        year=None,
        month=None,
        service=service,
    )
    fetched = await budgets_ctrl.get_budget(budget.id, service=service)
    updated = await budgets_ctrl.update_budget(budget.id, BudgetUpdate(amount=Decimal("600.00")), service=service)
    response = await budgets_ctrl.delete_budget(budget.id, service=service)

    assert created.id == budget.id
    assert len(budgets) == 1
    assert fetched.id == budget.id
    assert updated.amount == Decimal("600.00")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_budgets_controller_error_paths() -> None:
    budget = build_budget()
    payload = _budget_payload(budget.user_id, budget.category_id)
    service = SimpleNamespace(
        create_budget=AsyncMock(side_effect=EntityAlreadyExistsError("dup")),
    )

    with pytest.raises(HTTPException) as excinfo:
        await budgets_ctrl.create_budget(payload, service=service)
    assert excinfo.value.status_code == 409

    service.create_budget.side_effect = EntityNotFoundError("missing")
    with pytest.raises(HTTPException) as excinfo:
        await budgets_ctrl.create_budget(payload, service=service)
    assert excinfo.value.status_code == 404

    service.create_budget.side_effect = ValidationAppError("invalid")
    with pytest.raises(HTTPException) as excinfo:
        await budgets_ctrl.create_budget(payload, service=service)
    assert excinfo.value.status_code == 400

    service.update_budget = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await budgets_ctrl.update_budget(budget.id, BudgetUpdate(amount=Decimal("1")), service=service)

    service.update_budget = AsyncMock(side_effect=ValidationAppError("invalid"))
    with pytest.raises(HTTPException) as excinfo:
        await budgets_ctrl.update_budget(budget.id, BudgetUpdate(), service=service)
    assert excinfo.value.status_code == 400

    service.delete_budget = AsyncMock(side_effect=ValidationAppError("invalid"))
    with pytest.raises(HTTPException):
        await budgets_ctrl.delete_budget(budget.id, service=service)

    service.delete_budget = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await budgets_ctrl.delete_budget(budget.id, service=service)


# ---------------------------------------------------------------------------
# Categories controller
# ---------------------------------------------------------------------------


def _category_payload(user_id: str | None = None) -> CategoryCreate:
    user_id = user_id or generate_object_id()
    return CategoryCreate(
        user_id=user_id,
        name="Categoria",
        category_type=CategoryType.EXPENSE,
    )


@pytest.mark.asyncio
async def test_categories_controller_success_paths() -> None:
    category = build_category()
    service = SimpleNamespace(
        create_category=AsyncMock(return_value=category),
        list_categories=AsyncMock(return_value=[category]),
        get_category=AsyncMock(return_value=category),
        update_category=AsyncMock(return_value=category),
        delete_category=AsyncMock(return_value=None),
    )

    created = await categories_ctrl.create_category(_category_payload(category.user_id), service=service)
    categories = await categories_ctrl.list_categories(
        user_id=None,
        category_type=None,
        parent_id=None,
        name=None,
        service=service,
    )
    fetched = await categories_ctrl.get_category(category.id, service=service)
    updated = await categories_ctrl.update_category(
        category.id,
        CategoryUpdate(name="Nova"),
        service=service,
    )
    response = await categories_ctrl.delete_category(category.id, service=service)

    assert created.id == category.id
    assert len(categories) == 1
    assert fetched.id == category.id
    assert updated.name == category.name
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_categories_controller_error_paths() -> None:
    service = SimpleNamespace(
        create_category=AsyncMock(side_effect=EntityNotFoundError("missing")),
    )
    payload = _category_payload(generate_object_id())
    with pytest.raises(HTTPException):
        await categories_ctrl.create_category(payload, service=service)

    service.create_category.side_effect = ValidationAppError("invalid")
    with pytest.raises(HTTPException) as excinfo:
        await categories_ctrl.create_category(payload, service=service)
    assert excinfo.value.status_code == 400

    service.get_category = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await categories_ctrl.get_category("cat", service=service)

    service.update_category = AsyncMock(side_effect=ValidationAppError("invalid"))
    with pytest.raises(HTTPException):
        await categories_ctrl.update_category("cat", CategoryUpdate(name="Categoria X"), service=service)

    service.update_category = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await categories_ctrl.update_category("cat", CategoryUpdate(name="Categoria Y"), service=service)

    service.delete_category = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await categories_ctrl.delete_category("cat", service=service)


# ---------------------------------------------------------------------------
# Transactions controller
# ---------------------------------------------------------------------------


def _transaction_payload(
    user_id: str | None = None,
    account_id: str | None = None,
    category_id: str | None = None,
) -> TransactionCreate:
    user_id = user_id or generate_object_id()
    account_id = account_id or generate_object_id()
    category_id = category_id or generate_object_id()
    return TransactionCreate(
        user_id=user_id,
        account_id=account_id,
        category_id=category_id,
        amount=Decimal("90.00"),
        transaction_type=TransactionType.EXPENSE,
        occurred_at=UTC_NOW,
        description="Despesa",
    )


@pytest.mark.asyncio
async def test_transactions_controller_success_paths() -> None:
    transaction = build_transaction()
    service = SimpleNamespace(
        create_transaction=AsyncMock(return_value=transaction),
        list_transactions=AsyncMock(return_value=[transaction]),
        get_transaction=AsyncMock(return_value=transaction),
        update_transaction=AsyncMock(return_value=transaction),
        delete_transaction=AsyncMock(return_value=None),
    )

    created = await transactions_ctrl.create_transaction(
        _transaction_payload(transaction.user_id, transaction.account_id, transaction.category_id),
        service=service,
    )
    txns = await transactions_ctrl.list_transactions(
        user_id=None,
        account_id=None,
        category_id=None,
        transaction_type=None,
        transfer_account_id=None,
        date_from=None,
        date_to=None,
        service=service,
    )
    fetched = await transactions_ctrl.get_transaction(transaction.id, service=service)
    updated = await transactions_ctrl.update_transaction(
        transaction.id,
        TransactionUpdate(amount=Decimal("150.00")),
        service=service,
    )
    response = await transactions_ctrl.delete_transaction(transaction.id, service=service)

    assert created.id == transaction.id
    assert len(txns) == 1
    assert fetched.id == transaction.id
    assert updated.amount == Decimal("150.00")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_transactions_controller_error_paths() -> None:
    payload = _transaction_payload()
    service = SimpleNamespace(
        create_transaction=AsyncMock(side_effect=EntityNotFoundError("missing")),
    )

    with pytest.raises(HTTPException):
        await transactions_ctrl.create_transaction(payload, service=service)

    service.create_transaction.side_effect = ValidationAppError("invalid")
    with pytest.raises(HTTPException) as excinfo:
        await transactions_ctrl.create_transaction(payload, service=service)
    assert excinfo.value.status_code == 400

    service.get_transaction = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await transactions_ctrl.get_transaction("txn", service=service)

    service.update_transaction = AsyncMock(side_effect=ValidationAppError("invalid"))
    with pytest.raises(HTTPException):
        await transactions_ctrl.update_transaction("txn", TransactionUpdate(amount=Decimal("1")), service=service)

    service.update_transaction = AsyncMock(side_effect=EntityNotFoundError("missing"))
    with pytest.raises(HTTPException):
        await transactions_ctrl.update_transaction("txn", TransactionUpdate(amount=Decimal("2")), service=service)


# ---------------------------------------------------------------------------
# Reports & Health controllers
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_reports_controller_success_and_error() -> None:
    summary = SimpleNamespace(
        user_id="user",
        year=2024,
        month=7,
        totals_by_type={},
        categories=[],
    )
    service = SimpleNamespace(monthly_summary=AsyncMock(return_value=summary))
    result = await reports_ctrl.get_monthly_summary("user", 2024, 7, service=service)
    assert result.user_id == "user"

    service.monthly_summary.side_effect = EntityNotFoundError("missing")
    with pytest.raises(HTTPException):
        await reports_ctrl.get_monthly_summary("user", 2024, 7, service=service)


@pytest.mark.asyncio
async def test_health_controller_uses_settings(monkeypatch) -> None:
    settings = Settings(APP_NAME="Health API", ENVIRONMENT="test")
    monkeypatch.setattr("src.controllers.health.get_settings", lambda: settings)
    response = await health_ctrl.health_check()
    assert response["application"] == "Health API"
    assert response["environment"] == "test"
