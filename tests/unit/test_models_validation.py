"""Additional model validation tests to strengthen mutation coverage."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from src.models.account import AccountCreate, AccountUpdate, build_account
from src.models.budget import BudgetCreate, BudgetUpdate, build_budget
from src.models.category import CategoryCreate, CategoryUpdate, build_category
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import TransactionCreate, TransactionUpdate, build_transaction
from src.models.user import UserCreate, UserUpdate, build_user

USER_ID = "64f6d1250a1b2c3d4e5f6789"
ACCOUNT_ID = "65f6d1250a1b2c3d4e5f6789"
CATEGORY_ID = "66f6d1250a1b2c3d4e5f6789"


def test_account_create_normalizes_defaults_and_forbids_extra_fields() -> None:
    payload = AccountCreate(
        user_id=USER_ID,
        name="   Conta Mutação   ",
        account_type=AccountType.CASH,
        starting_balance=Decimal("10.125"),
        minimum_balance=Decimal("5.554"),
    )
    assert payload.name == "Conta Mutação"
    assert payload.currency == CurrencyCode.BRL
    assert payload.starting_balance == Decimal("10.13")
    assert payload.minimum_balance == Decimal("5.55")

    with pytest.raises(ValidationError):
        AccountCreate(
            user_id=USER_ID,
            name="Conta X",
            account_type=AccountType.CHECKING,
            starting_balance=Decimal("0"),
            invalid_field="boom",  # type: ignore[arg-type]
        )


def test_account_update_trims_name_and_normalizes_minimum() -> None:
    update = AccountUpdate(name="  Nova Conta  ", minimum_balance=Decimal("12.345"))
    assert update.name == "Nova Conta"
    assert update.minimum_balance == Decimal("12.35")


def test_build_account_generates_consistent_fields(monkeypatch) -> None:
    timestamp = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)
    monkeypatch.setattr("src.models.account.generate_object_id", lambda: ACCOUNT_ID)
    monkeypatch.setattr("src.models.account.now_utc", lambda: timestamp)
    payload = AccountCreate(
        user_id=USER_ID,
        name="Conta Build",
        account_type=AccountType.CHECKING,
        starting_balance=Decimal("42.005"),
    )

    account = build_account(payload)

    assert account.id == ACCOUNT_ID
    assert account.balance == Decimal("42.01")
    assert account.created_at == timestamp


def test_budget_models_normalize_amount_and_block_extra_fields() -> None:
    payload = BudgetCreate(
        user_id=USER_ID,
        category_id=CATEGORY_ID,
        year=2024,
        month=5,
        amount=Decimal("123.456"),
        alert_percentage=90,
    )
    assert payload.amount == Decimal("123.46")

    update = BudgetUpdate(amount=Decimal("200.009"))
    assert update.amount == Decimal("200.01")

    with pytest.raises(ValidationError):
        BudgetCreate(
            user_id=USER_ID,
            category_id=CATEGORY_ID,
            year=2024,
            month=5,
            amount=Decimal("10"),
            extra="boom",  # type: ignore[arg-type]
        )


def test_build_budget_uses_timestamp(monkeypatch) -> None:
    timestamp = datetime(2024, 6, 1, 8, 0, tzinfo=timezone.utc)
    monkeypatch.setattr("src.models.budget.generate_object_id", lambda: "70f6d1250a1b2c3d4e5f6789")
    monkeypatch.setattr("src.models.budget.now_utc", lambda: timestamp)
    budget = build_budget(
        BudgetCreate(
            user_id=USER_ID,
            category_id=CATEGORY_ID,
            year=2024,
            month=6,
            amount=Decimal("310.00"),
        )
    )
    assert budget.created_at == timestamp
    assert budget.updated_at == timestamp


def test_category_models_validate_names_and_extras() -> None:
    payload = CategoryCreate(
        user_id=USER_ID,
        name="  Categoria   ",
        category_type=CategoryType.EXPENSE,
    )
    assert payload.name == "Categoria"

    with pytest.raises(ValidationError):
        CategoryUpdate(name="   ")


def test_transaction_models_normalize_amounts_and_descriptions() -> None:
    payload = TransactionCreate(
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        amount=Decimal("50.159"),
        transaction_type=TransactionType.EXPENSE,
        description="  compra mercado  ",
    )
    assert payload.amount == Decimal("50.16")
    assert payload.description == "compra mercado"

    update = TransactionUpdate(amount=Decimal("10.335"), description="  lanche ")
    assert update.amount == Decimal("10.34")
    assert update.description == "lanche"


def test_build_transaction_preserves_optional_fields(monkeypatch) -> None:
    timestamp = datetime(2024, 2, 1, 10, 30, tzinfo=timezone.utc)
    monkeypatch.setattr("src.models.transaction.generate_object_id", lambda: "71f6d1250a1b2c3d4e5f6789")
    monkeypatch.setattr("src.models.transaction.now_utc", lambda: timestamp)
    payload = TransactionCreate(
        user_id=USER_ID,
        account_id=ACCOUNT_ID,
        category_id=CATEGORY_ID,
        amount=Decimal("75.15"),
        transaction_type=TransactionType.INCOME,
        description="Salário",
        notes=None,
        counterparty="Empresa",
    )
    transaction = build_transaction(payload)
    assert transaction.id == "71f6d1250a1b2c3d4e5f6789"
    assert transaction.updated_at == timestamp


def test_user_models_normalize_inputs() -> None:
    payload = UserCreate(
        name="  Usuário  ",
        email="USER@EXAMPLE.COM",
        default_currency=CurrencyCode.USD,
    )
    assert payload.name == "Usuário"
    assert payload.email == "user@example.com"

    update = UserUpdate(name="  Outro  ")
    assert update.name == "Outro"

    with pytest.raises(ValidationError):
        UserCreate(name="  ", email="invalid@example.com", default_currency=CurrencyCode.BRL)


def test_build_user_uses_generated_fields(monkeypatch) -> None:
    timestamp = datetime(2024, 3, 2, 9, 0, tzinfo=timezone.utc)
    monkeypatch.setattr("src.models.user.generate_object_id", lambda: USER_ID)
    monkeypatch.setattr("src.models.user.now_utc", lambda: timestamp)
    user = build_user(
        UserCreate(
            name="Novo",
            email="novo@example.com",
            default_currency=CurrencyCode.BRL,
        )
    )
    assert user.id == USER_ID
    assert user.created_at == timestamp
