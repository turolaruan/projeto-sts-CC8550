"""Budget focused business rules."""

from __future__ import annotations

from datetime import date
from typing import List

from src.models import BudgetCreate, BudgetModel, BudgetSummary, BudgetUpdate
from src.repositories import BudgetRepository

from .exceptions import BusinessRuleError, NotFoundError


class BudgetService:
    """Operations that manage category budgets."""

    def __init__(self, repository: BudgetRepository) -> None:
        self.repository = repository

    async def create_budget(self, payload: BudgetCreate) -> BudgetModel:
        """Create a budget making sure there are no overlapping periods."""

        self._validate_period(payload.period_start, payload.period_end)
        overlap = await self.repository.has_overlap(
            payload.user_id, payload.category, payload.period_start, payload.period_end
        )
        if overlap:
            raise BusinessRuleError("Budget period overlaps an existing one")
        return await self.repository.create(payload.model_dump())

    async def list_budgets(self, user_id: str) -> List[BudgetModel]:
        """List budgets filtered by user."""

        return await self.repository.list({"user_id": user_id})

    async def get_budget(self, budget_id: str) -> BudgetModel:
        """Return budget by id or raise."""

        budget = await self.repository.get_by_id(budget_id)
        if not budget:
            raise NotFoundError("Budget not found")
        return budget

    async def update_budget(self, budget_id: str, payload: BudgetUpdate) -> BudgetModel:
        """Update budget parameters."""

        data = payload.model_dump(exclude_none=True)
        updated = await self.repository.update(budget_id, data)
        if not updated:
            raise NotFoundError("Budget not found")
        return updated

    async def delete_budget(self, budget_id: str) -> bool:
        """Delete budget."""

        deleted = await self.repository.delete(budget_id)
        if not deleted:
            raise NotFoundError("Budget not found")
        return deleted

    async def summarize(self, user_id: str) -> List[BudgetSummary]:
        """Return summary for all budgets of the user."""

        return await self.repository.summary(user_id)

    async def get_budget_for(self, user_id: str, category: str, day: date) -> BudgetModel | None:
        """Fetch budget by category for provided day."""

        return await self.repository.get_for_category(user_id, day, category)

    async def apply_expense(self, budget: BudgetModel, amount: float) -> BudgetModel:
        """Register a new expense inside the provided budget."""

        if budget.amount_spent + amount > budget.limit_amount:
            raise BusinessRuleError(
                f"Budget {budget.category} exceeded by {budget.amount_spent + amount - budget.limit_amount:.2f}"
            )
        return await self.repository.increment_spent(budget.id, amount)

    def _validate_period(self, start: date, end: date) -> None:
        """Ensure the period boundaries make sense."""

        if start > end:
            raise BusinessRuleError("Budget period start must be <= end")
