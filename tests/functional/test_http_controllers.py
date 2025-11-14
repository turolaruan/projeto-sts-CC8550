"""HTTP-level controller tests to exercise FastAPI wiring and error handling."""

from __future__ import annotations

from datetime import timedelta
from types import SimpleNamespace
from unittest.mock import AsyncMock
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.controllers import accounts as accounts_ctrl
from src.controllers import transactions as transactions_ctrl
from src.models.enums import AccountType, CurrencyCode, TransactionType
from src.utils.exceptions import EntityNotFoundError, ValidationAppError
from tests.structural.helpers import UTC_NOW, build_account, build_transaction


def _accounts_client():
    account = build_account()
    service = SimpleNamespace(
        create_account=AsyncMock(return_value=account),
        list_accounts=AsyncMock(return_value=[account]),
        get_account=AsyncMock(return_value=account),
        update_account=AsyncMock(return_value=account),
        delete_account=AsyncMock(return_value=None),
    )
    app = FastAPI()
    app.include_router(accounts_ctrl.router)
    app.dependency_overrides[accounts_ctrl.get_account_service] = lambda: service
    return TestClient(app), service, account


def _transactions_client():
    transaction = build_transaction(transfer_account_id="7" * 24)
    service = SimpleNamespace(
        create_transaction=AsyncMock(return_value=transaction),
        list_transactions=AsyncMock(return_value=[transaction]),
        get_transaction=AsyncMock(return_value=transaction),
        update_transaction=AsyncMock(return_value=transaction),
        delete_transaction=AsyncMock(return_value=None),
    )
    app = FastAPI()
    app.include_router(transactions_ctrl.router)
    app.dependency_overrides[transactions_ctrl.get_transaction_service] = lambda: service
    return TestClient(app), service, transaction


def test_accounts_create_http_success() -> None:
    client, service, account = _accounts_client()
    payload = {
        "user_id": account.user_id,
        "name": "Conta API",
        "account_type": AccountType.CHECKING.value,
        "currency": CurrencyCode.BRL.value,
        "starting_balance": "120.50",
    }
    response = client.post("/accounts/", json=payload)
    assert response.status_code == 201
    assert response.json()["id"] == account.id
    service.create_account.assert_awaited_once()


def test_accounts_create_http_validation_error() -> None:
    client, service, account = _accounts_client()
    service.create_account.side_effect = ValidationAppError("invalid")
    payload = {
        "user_id": account.user_id,
        "name": "Conta API",
        "account_type": AccountType.CHECKING.value,
        "currency": CurrencyCode.BRL.value,
        "starting_balance": "0",
    }
    response = client.post("/accounts/", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "invalid"


def test_accounts_get_http_not_found() -> None:
    client, service, account = _accounts_client()
    service.get_account.side_effect = EntityNotFoundError("missing")
    response = client.get(f"/accounts/{account.id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "missing"


def test_transactions_list_http_applies_filters() -> None:
    client, service, transaction = _transactions_client()
    params = {
        "user_id": transaction.user_id,
        "account_id": transaction.account_id,
        "category_id": transaction.category_id,
        "transaction_type": TransactionType.EXPENSE.value,
        "transfer_account_id": transaction.transfer_account_id,
        "date_from": UTC_NOW.isoformat(),
        "date_to": (UTC_NOW + timedelta(days=1)).isoformat(),
    }
    response = client.get("/transactions/", params=params)
    assert response.status_code == 200
    call = service.list_transactions.await_args_list[0]
    assert call.kwargs["transaction_type"] == TransactionType.EXPENSE.value
    assert call.kwargs["transfer_account_id"] == transaction.transfer_account_id
    assert call.kwargs["date_from"] is not None
    assert response.json()[0]["id"] == transaction.id


def test_transactions_delete_http_not_found() -> None:
    client, service, transaction = _transactions_client()
    service.delete_transaction.side_effect = EntityNotFoundError("missing")
    response = client.delete(f"/transactions/{transaction.id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "missing"
