"""Business logic for managing categories."""

from __future__ import annotations

from typing import List

from src.models.category import Category, CategoryCreate, CategoryUpdate, build_category
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.utils.exceptions import EntityNotFoundError, ValidationAppError


class CategoryService:
    """Encapsulates category workflows and validations."""

    def __init__(
        self,
        repository: CategoryRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository
        self._budget_repository = budget_repository

    async def create_category(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, payload.user_id)
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def list_categories(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def get_category(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def update_category(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def delete_category(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def _ensure_user_exists(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def _validate_parent(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )
