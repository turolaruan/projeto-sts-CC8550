"""Business logic for managing budgets."""

from __future__ import annotations

from typing import List

from src.models.budget import Budget, BudgetCreate, BudgetUpdate, build_budget
from src.models.enums import CategoryType
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)


class BudgetService:
    """Encapsulates budget workflows and validations."""

    def __init__(
        self,
        repository: BudgetRepository,
        user_repository: UserRepository,
        category_repository: CategoryRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._category_repository = category_repository
        self._transaction_repository = transaction_repository

    async def create_budget(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def list_budgets(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def get_budget(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def update_budget(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def delete_budget(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def _ensure_user_exists(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def _get_category(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    def _ensure_same_user(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def _ensure_category_is_expense(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                context={"category_type": category_type},
            )
