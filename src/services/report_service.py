"""Reporting services for financial summaries."""

from __future__ import annotations

from collections import defaultdict
from decimal import Decimal
from typing import Dict, List

from src.models.enums import TransactionType
from src.models.report import MonthlyCategorySummary, MonthlySummary
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.utils.exceptions import EntityNotFoundError


class ReportService:
    """Generate high-level financial reports."""

    def __init__(
        self,
        transaction_repository: TransactionRepository,
        category_repository: CategoryRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._transaction_repository = transaction_repository
        self._category_repository = category_repository
        self._budget_repository = budget_repository

    async def monthly_summary(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def _fetch_categories(self, category_ids: set[str]):
        result: Dict[str, object] = {}
        for category_id in category_ids:
            category = await self._category_repository.get(category_id)
            if category:
                result[category_id] = category
        return result

    async def _fetch_budgets(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result
