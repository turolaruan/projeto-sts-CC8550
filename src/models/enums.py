"""Enumerations used across domain models."""

from enum import Enum


class AccountType(str, Enum):
    """Supported types of financial accounts."""

    CHECKING = "checking"
    SAVINGS = "savings"
    INVESTMENT = "investment"
    CASH = "cash"


class TransactionType(str, Enum):
    """Supported transaction types in the system."""

    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"


class GoalStatus(str, Enum):
    """Life-cycle states for savings goals."""

    ACTIVE = "active"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"


class BudgetStatus(str, Enum):
    """Possible evaluation states for a budget."""

    HEALTHY = "healthy"
    WARNING = "warning"
    EXCEEDED = "exceeded"
