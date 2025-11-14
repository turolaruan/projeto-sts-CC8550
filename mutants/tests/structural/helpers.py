"""Shared builders and fakes used across structural tests."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Any

from src.models.account import Account
from src.models.budget import Budget
from src.models.category import Category
from src.models.common import generate_object_id
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import Transaction
from src.models.user import User


UTC_NOW = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)


def build_user(**overrides: Any) -> User:
    data = {
        "id": generate_object_id(),
        "name": "Usuário Estrutural",
        "email": "estrutural@example.com",
        "default_currency": CurrencyCode.BRL,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return User(**data)


def build_account(**overrides: Any) -> Account:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "name": "Conta Estrutural",
        "account_type": AccountType.CHECKING,
        "currency": CurrencyCode.BRL,
        "description": "Conta para testes estruturais",
        "minimum_balance": Decimal("10.00"),
        "balance": Decimal("100.00"),
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Account(**data)


def build_category(**overrides: Any) -> Category:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "name": "Categoria Estrutural",
        "category_type": CategoryType.EXPENSE,
        "description": None,
        "parent_id": None,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Category(**data)


def build_budget(**overrides: Any) -> Budget:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "category_id": generate_object_id(),
        "year": 2024,
        "month": 6,
        "amount": Decimal("500.00"),
        "alert_percentage": 80,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Budget(**data)


def build_transaction(**overrides: Any) -> Transaction:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "account_id": generate_object_id(),
        "category_id": generate_object_id(),
        "amount": Decimal("150.00"),
        "transaction_type": TransactionType.EXPENSE,
        "occurred_at": UTC_NOW,
        "description": "Transação estrutural",
        "notes": None,
        "counterparty": None,
        "transfer_account_id": None,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Transaction(**data)


class FakeCollection:
    """Simple async-aware collection used to record index operations."""

    def __init__(self) -> None:
        self.index_calls: list[tuple[tuple[Any, ...], dict[str, Any]]] = []

    async def create_index(self, *args: Any, **kwargs: Any) -> None:
        self.index_calls.append((args, kwargs))


class FakeDatabase:
    """Minimal Motor-like database used for dependency wiring tests."""

    def __init__(self) -> None:
        self.collections: dict[str, FakeCollection] = {}

    def get_collection(self, name: str) -> FakeCollection:
        collection = self.collections.get(name)
        if collection is None:
            collection = FakeCollection()
            self.collections[name] = collection
        return collection


class FakeMotorClient:
    """Mimics AsyncIOMotorClient behaviour for structural tests."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.databases: dict[str, FakeDatabase] = {}
        self.closed = False

    def __getitem__(self, name: str) -> FakeDatabase:
        database = self.databases.get(name)
        if database is None:
            database = FakeDatabase()
            self.databases[name] = database
        return database

    def close(self) -> None:
        self.closed = True
