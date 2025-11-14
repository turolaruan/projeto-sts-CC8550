"""Shared factories for building domain objects in tests."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any
from uuid import uuid4

from src.models import (
    AccountCreate,
    AccountModel,
    AccountType,
    BudgetCreate,
    BudgetModel,
    GoalCreate,
    GoalModel,
    GoalStatus,
    TransactionCreate,
    TransactionModel,
    TransactionType,
    UserCreate,
    UserModel,
)


def make_user_model(**overrides: Any) -> UserModel:
    """Return a populated user model."""

    payload = {
        "id": overrides.get("id", str(uuid4())),
        "name": "Test User",
        "email": "user@example.com",
        "monthly_income": 10000.0,
    }
    payload.update(overrides)
    return UserModel(**payload)


def make_user_create(**overrides: Any) -> UserCreate:
    """Return payload for creating a user."""

    payload = {
        "name": "New User",
        "email": overrides.get("email", f"{uuid4().hex[:6]}@example.com"),
        "monthly_income": 5000.0,
    }
    payload.update(overrides)
    return UserCreate(**payload)


def make_account_model(**overrides: Any) -> AccountModel:
    """Return sample account model."""

    payload = {
        "id": overrides.get("id", str(uuid4())),
        "user_id": overrides.get("user_id", str(uuid4())),
        "name": "Main Account",
        "institution": "Bank",
        "type": AccountType.CHECKING,
        "balance": 2000.0,
        "goal_locked_amount": overrides.get("goal_locked_amount", 0.0),
    }
    payload.update(overrides)
    return AccountModel(**payload)


def make_account_create(**overrides: Any) -> AccountCreate:
    """Return payload for account creation."""

    payload = {
        "user_id": overrides.get("user_id", str(uuid4())),
        "name": "Wallet",
        "institution": "Bank",
        "type": AccountType.CHECKING,
        "balance": overrides.get("balance", 0.0),
    }
    payload.update(overrides)
    return AccountCreate(**payload)


def make_budget_model(**overrides: Any) -> BudgetModel:
    """Return a budget model spanning the current month."""

    today = date.today()
    start = today.replace(day=1)
    end = (start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    payload = {
        "id": overrides.get("id", str(uuid4())),
        "user_id": overrides.get("user_id", str(uuid4())),
        "category": "groceries",
        "limit_amount": 500.0,
        "amount_spent": overrides.get("amount_spent", 0.0),
        "period_start": start,
        "period_end": end,
        "alerts_enabled": True,
    }
    payload.update(overrides)
    return BudgetModel(**payload)


def make_budget_create(**overrides: Any) -> BudgetCreate:
    """Return payload for creating budgets."""

    today = date.today()
    start = today.replace(day=1)
    end = (start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    payload = {
        "user_id": overrides.get("user_id", str(uuid4())),
        "category": overrides.get("category", "groceries"),
        "limit_amount": overrides.get("limit_amount", 500.0),
        "period_start": overrides.get("period_start", start),
        "period_end": overrides.get("period_end", end),
        "alerts_enabled": overrides.get("alerts_enabled", True),
    }
    payload.update(overrides)
    return BudgetCreate(**payload)


def make_goal_model(**overrides: Any) -> GoalModel:
    """Return sample goal model."""

    payload = {
        "id": overrides.get("id", str(uuid4())),
        "user_id": overrides.get("user_id", str(uuid4())),
        "account_id": overrides.get("account_id", str(uuid4())),
        "name": "Trip",
        "target_amount": 1000.0,
        "current_amount": overrides.get("current_amount", 0.0),
        "target_date": date.today() + timedelta(days=90),
        "status": overrides.get("status", GoalStatus.ACTIVE),
        "lock_funds": overrides.get("lock_funds", False),
        "reserved_amount": overrides.get("reserved_amount", 0.0),
    }
    payload.update(overrides)
    return GoalModel(**payload)


def make_goal_create(**overrides: Any) -> GoalCreate:
    """Return payload for creating goals."""

    payload = {
        "user_id": overrides.get("user_id", str(uuid4())),
        "account_id": overrides.get("account_id", str(uuid4())),
        "name": "Emergency fund",
        "target_amount": overrides.get("target_amount", 2000.0),
        "target_date": overrides.get("target_date", date.today() + timedelta(days=180)),
        "lock_funds": overrides.get("lock_funds", True),
    }
    payload.update(overrides)
    return GoalCreate(**payload)


def make_transaction_model(**overrides: Any) -> TransactionModel:
    """Return transaction model."""

    payload = {
        "id": overrides.get("id", str(uuid4())),
        "user_id": overrides.get("user_id", str(uuid4())),
        "account_id": overrides.get("account_id", str(uuid4())),
        "type": overrides.get("type", TransactionType.EXPENSE),
        "category": overrides.get("category", "groceries"),
        "description": overrides.get("description", "Weekly groceries"),
        "amount": overrides.get("amount", 150.0),
        "event_date": overrides.get("event_date", datetime.utcnow()),
        "tags": overrides.get("tags", ["food"]),
    }
    payload.update(overrides)
    return TransactionModel(**payload)


def make_transaction_create(**overrides: Any) -> TransactionCreate:
    """Return payload for transaction creation."""

    payload = {
        "user_id": overrides.get("user_id", str(uuid4())),
        "account_id": overrides.get("account_id", str(uuid4())),
        "type": overrides.get("type", TransactionType.EXPENSE),
        "category": overrides.get("category", "groceries"),
        "description": overrides.get("description", "Dinner"),
        "amount": overrides.get("amount", 75.0),
        "event_date": overrides.get("event_date", datetime.utcnow()),
    }
    payload.update(overrides)
    return TransactionCreate(**payload)
