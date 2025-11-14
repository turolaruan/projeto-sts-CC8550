"""Domain and API models for the finance management system."""

from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, PositiveFloat, conlist

from .enums import AccountType, BudgetStatus, GoalStatus, TransactionType


class MongoBaseModel(BaseModel):
    """Base model with common Mongo-oriented settings."""

    id: Optional[str] = Field(default=None, alias="id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    model_config = {
        "populate_by_name": True,
        "from_attributes": True,
    }


class UserModel(MongoBaseModel):
    """Represents an application user owning accounts and goals."""

    name: str
    email: EmailStr
    monthly_income: PositiveFloat


class AccountModel(MongoBaseModel):
    """Financial account belonging to a user."""

    user_id: str
    name: str
    institution: str
    type: AccountType
    balance: float = Field(ge=0)
    currency: str = Field(default="BRL", min_length=3, max_length=3)
    goal_locked_amount: float = Field(default=0, ge=0)


class TransactionModel(MongoBaseModel):
    """Represents a debit/credit entry for an account."""

    user_id: str
    account_id: str
    budget_id: Optional[str] = None
    goal_id: Optional[str] = None
    type: TransactionType
    category: str
    description: str
    amount: PositiveFloat
    event_date: datetime = Field(default_factory=datetime.utcnow)
    tags: List[str] = Field(default_factory=list)


class BudgetModel(MongoBaseModel):
    """Budget configured per category and date interval."""

    user_id: str
    category: str
    limit_amount: PositiveFloat
    amount_spent: float = Field(default=0, ge=0)
    period_start: date
    period_end: date
    alerts_enabled: bool = True

    @property
    def status(self) -> BudgetStatus:
        """Compute the budget usage status dynamically."""

        usage = self.amount_spent / self.limit_amount
        if usage < 0.8:
            return BudgetStatus.HEALTHY
        if usage < 1.0:
            return BudgetStatus.WARNING
        return BudgetStatus.EXCEEDED


class GoalModel(MongoBaseModel):
    """Savings goal with optional locked funds."""

    user_id: str
    account_id: str
    name: str
    description: Optional[str] = None
    target_amount: PositiveFloat
    current_amount: float = Field(default=0, ge=0)
    reserved_amount: float = Field(default=0, ge=0)
    target_date: date
    status: GoalStatus = GoalStatus.ACTIVE
    lock_funds: bool = False


class TransactionFilter(BaseModel):
    """Filtering options for transaction search endpoints."""

    user_id: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    category: Optional[str] = None
    min_amount: Optional[float] = Field(default=None, ge=0)
    max_amount: Optional[float] = Field(default=None, ge=0)
    tags: Optional[conlist(str, min_length=1)] = None
    sort_by: str = "event_date"
    sort_order: int = Field(default=-1, description="Mongo sort order")


class BudgetSummary(BaseModel):
    """Aggregated data returned by the budget summary endpoint."""

    category: str
    limit_amount: float
    amount_spent: float
    status: BudgetStatus
    remaining: float


class ReportPayload(BaseModel):
    """Payload describing data exported to files."""

    generated_at: datetime
    file_path: str
    total_transactions: int
    total_expenses: float
    total_income: float
