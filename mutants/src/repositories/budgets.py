"""Budget repository implementation."""

from __future__ import annotations

from datetime import date

from src.models import BudgetModel, BudgetSummary
from src.utils import serialize_document

from .base import AbstractRepository


class BudgetRepository(AbstractRepository[BudgetModel]):
    """Persistence operations for budgets."""

    collection_name = "budgets"
    model = BudgetModel

    async def get_for_category(self, user_id: str, period: date, category: str):
        """Return budget for category and period date."""

        document = await self.collection.find_one(
            {
                "user_id": user_id,
                "category": category,
                "period_start": {"$lte": period},
                "period_end": {"$gte": period},
            }
        )
        return BudgetModel(**serialize_document(document)) if document else None

    async def increment_spent(self, budget_id: str, amount: float) -> BudgetModel | None:
        """Increase the spent value and return the updated budget."""

        await self.collection.update_one(
            {"_id": self._to_object_id(budget_id)},
            {"$inc": {"amount_spent": amount}},
        )
        document = await self.collection.find_one({"_id": self._to_object_id(budget_id)})
        return BudgetModel(**serialize_document(document)) if document else None

    async def summary(self, user_id: str) -> list[BudgetSummary]:
        """Aggregate budgets with derived state."""

        cursor = self.collection.find({"user_id": user_id})
        budgets = [BudgetModel(**serialize_document(doc)) async for doc in cursor]
        return [
            BudgetSummary(
                category=budget.category,
                limit_amount=budget.limit_amount,
                amount_spent=budget.amount_spent,
                status=budget.status,
                remaining=max(budget.limit_amount - budget.amount_spent, 0),
            )
            for budget in budgets
        ]

    async def has_overlap(self, user_id: str, category: str, start: date, end: date) -> bool:
        """Return whether a budget exists overlapping the period."""

        clash = await self.collection.find_one(
            {
                "user_id": user_id,
                "category": category,
                "$or": [
                    {
                        "period_start": {"$lte": start},
                        "period_end": {"$gte": start},
                    },
                    {
                        "period_start": {"$lte": end},
                        "period_end": {"$gte": end},
                    },
                ],
            },
            projection={"_id": 1},
        )
        return clash is not None
