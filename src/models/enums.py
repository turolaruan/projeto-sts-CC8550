"""Enumerations used across domain models."""

from __future__ import annotations

from enum import Enum


class CurrencyCode(str, Enum):
    """Supported currency codes for financial entities."""

    BRL = "BRL"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"

    @classmethod
    def choices(cls) -> list[str]:
        """Return list of available currency codes."""
        return [member.value for member in cls]


class AccountType(str, Enum):
    """Different kinds of financial accounts."""

    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT_CARD = "credit_card"
    CASH = "cash"
    INVESTMENT = "investment"


class CategoryType(str, Enum):
    """Category grouping for transactions."""

    INCOME = "income"
    EXPENSE = "expense"


class TransactionType(str, Enum):
    """Supported transaction types."""

    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"
