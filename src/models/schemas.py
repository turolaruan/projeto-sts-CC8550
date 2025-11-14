"""API schemas derived from the domain entities."""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, PositiveFloat

from .enums import AccountType, GoalStatus, TransactionType


class UserCreate(BaseModel):
    """Payload used to register new users."""

    name: str
    email: EmailStr
    monthly_income: PositiveFloat


class UserUpdate(BaseModel):
    """Payload used to partially update users."""

    name: Optional[str] = None
    monthly_income: Optional[PositiveFloat] = None


class AccountCreate(BaseModel):
    """Payload used to create new accounts."""

    user_id: str
    name: str
    institution: str
    type: AccountType
    balance: float = Field(default=0, ge=0)
    currency: str = Field(default="BRL", min_length=3, max_length=3)


class AccountUpdate(BaseModel):
    """Payload used to update existing accounts."""

    name: Optional[str] = None
    institution: Optional[str] = None
    type: Optional[AccountType] = None
    balance: Optional[float] = Field(default=None, ge=0)


class TransactionCreate(BaseModel):
    """Payload for registering transactions."""

    user_id: str
    account_id: str
    budget_id: Optional[str] = None
    goal_id: Optional[str] = None
    type: TransactionType
    category: str
    description: str
    amount: PositiveFloat
    event_date: datetime = Field(default_factory=datetime.utcnow)


class TransactionUpdate(BaseModel):
    """Payload for editing transactions."""

    description: Optional[str] = None
    amount: Optional[PositiveFloat] = None
    category: Optional[str] = None
    event_date: Optional[datetime] = None


class BudgetCreate(BaseModel):
    """Payload used to create budgets."""

    user_id: str
    category: str
    limit_amount: PositiveFloat
    period_start: date
    period_end: date
    alerts_enabled: bool = True


class BudgetUpdate(BaseModel):
    """Payload used to update budgets."""

    limit_amount: Optional[PositiveFloat] = None
    alerts_enabled: Optional[bool] = None


class GoalCreate(BaseModel):
    """Payload used to create savings goals."""

    user_id: str
    account_id: str
    name: str
    description: Optional[str] = None
    target_amount: PositiveFloat
    target_date: date
    lock_funds: bool = False


class GoalUpdate(BaseModel):
    """Payload used to update existing goals."""

    name: Optional[str] = None
    description: Optional[str] = None
    target_amount: Optional[PositiveFloat] = None
    target_date: Optional[date] = None
    status: Optional[GoalStatus] = None
    lock_funds: Optional[bool] = None
