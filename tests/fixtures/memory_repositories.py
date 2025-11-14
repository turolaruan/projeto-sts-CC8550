"""In-memory repositories used for integration tests."""

from __future__ import annotations

from collections.abc import AsyncIterator
from typing import Any, Dict, Iterable, List, Optional
from uuid import uuid4

from src.models import (
    AccountModel,
    BudgetModel,
    BudgetSummary,
    GoalModel,
    TransactionModel,
    UserModel,
)


class BaseMemoryRepository:
    """Simple asynchronous helpers for CRUD operations."""

    model_cls = dict

    def __init__(self) -> None:
        self.storage: Dict[str, dict[str, Any]] = {}

    def _to_model(self, data: Optional[dict[str, Any]]):
        if data is None:
            return None
        if self.model_cls is dict:
            return data
        return self.model_cls(**data)

    async def create(self, payload: dict[str, Any]):
        entity_id = payload.get("id", str(uuid4()))
        payload = {**payload, "id": entity_id}
        model = self._to_model(payload)
        if hasattr(model, "model_dump"):
            self.storage[entity_id] = model.model_dump()
        else:
            self.storage[entity_id] = payload
        return model

    async def get_by_id(self, entity_id: str):
        return self._to_model(self.storage.get(entity_id))

    async def list(self, filters: Optional[dict[str, Any]] = None) -> List[Any]:
        if not filters:
            items = list(self.storage.values())
        else:
            items = [item for item in self.storage.values() if all(item.get(k) == v for k, v in filters.items())]
        return [self._to_model(item) for item in items]

    async def update(self, entity_id: str, payload: dict[str, Any]):
        if entity_id not in self.storage:
            return None
        self.storage[entity_id].update(payload)
        return self._to_model(self.storage[entity_id])

    async def delete(self, entity_id: str) -> bool:
        return self.storage.pop(entity_id, None) is not None

    async def exists(self, filters: dict[str, Any]) -> bool:
        return any(all(item.get(k) == v for k, v in filters.items()) for item in self.storage.values())


class MemoryUserRepository(BaseMemoryRepository):
    model_cls = UserModel

    async def find_by_email(self, email: str) -> Optional[UserModel]:
        for item in self.storage.values():
            if item["email"] == email:
                return UserModel(**item)
        return None


class MemoryAccountRepository(BaseMemoryRepository):
    model_cls = AccountModel

    async def find_by_user(self, user_id: str) -> List[AccountModel]:
        items = [item for item in self.storage.values() if item["user_id"] == user_id]
        return [AccountModel(**item) for item in items]

    async def adjust_balance(self, account_id: str, delta: float) -> Optional[AccountModel]:
        if account_id not in self.storage:
            return None
        self.storage[account_id]["balance"] += delta
        return AccountModel(**self.storage[account_id])

    async def update_goal_lock(self, account_id: str, delta: float) -> Optional[AccountModel]:
        if account_id not in self.storage:
            return None
        self.storage[account_id]["goal_locked_amount"] = self.storage[account_id].get("goal_locked_amount", 0) + delta
        return AccountModel(**self.storage[account_id])


class MemoryBudgetRepository(BaseMemoryRepository):
    model_cls = BudgetModel

    async def get_for_category(self, user_id: str, day, category: str):
        for item in self.storage.values():
            if (
                item["user_id"] == user_id
                and item["category"] == category
                and item["period_start"] <= day <= item["period_end"]
            ):
                return BudgetModel(**item)
        return None

    async def increment_spent(self, budget_id: str, amount: float) -> Optional[BudgetModel]:
        if budget_id not in self.storage:
            return None
        self.storage[budget_id]["amount_spent"] += amount
        return BudgetModel(**self.storage[budget_id])

    async def summary(self, user_id: str) -> List[BudgetModel]:
        summaries = []
        for item in self.storage.values():
            if item["user_id"] != user_id:
                continue
            budget = BudgetModel(**item)
            summaries.append(
                BudgetSummary(
                    category=budget.category,
                    limit_amount=budget.limit_amount,
                    amount_spent=budget.amount_spent,
                    status=budget.status,
                    remaining=max(budget.limit_amount - budget.amount_spent, 0),
                )
            )
        return summaries

    async def has_overlap(self, user_id: str, category: str, start, end) -> bool:
        for item in self.storage.values():
            if item["user_id"] != user_id or item["category"] != category:
                continue
            if item["period_start"] <= start <= item["period_end"]:
                return True
            if item["period_start"] <= end <= item["period_end"]:
                return True
        return False


class MemoryGoalRepository(BaseMemoryRepository):
    model_cls = GoalModel

    async def increment_amount(self, goal_id: str, delta: float) -> Optional[GoalModel]:
        if goal_id not in self.storage:
            return None
        self.storage[goal_id]["current_amount"] += delta
        return GoalModel(**self.storage[goal_id])

    async def adjust_reserved(self, goal_id: str, delta: float) -> Optional[GoalModel]:
        if goal_id not in self.storage:
            return None
        self.storage[goal_id]["reserved_amount"] = self.storage[goal_id].get("reserved_amount", 0) + delta
        return GoalModel(**self.storage[goal_id])

    async def list_active(self, user_id: str) -> List[GoalModel]:
        return [
            GoalModel(**item)
            for item in self.storage.values()
            if item["user_id"] == user_id and item["status"] == "active"
        ]


class MemoryTransactionRepository(BaseMemoryRepository):
    model_cls = TransactionModel

    async def search(self, filters) -> List[TransactionModel]:
        results = []
        for item in self.storage.values():
            if item["user_id"] != filters.user_id:
                continue
            if filters.category and item["category"] != filters.category:
                continue
            if filters.min_amount is not None and item["amount"] < filters.min_amount:
                continue
            if filters.max_amount is not None and item["amount"] > filters.max_amount:
                continue
            results.append(TransactionModel(**item))
        return results

    async def total_by_type(self, user_id: str) -> dict[str, float]:
        totals = {"income": 0.0, "expense": 0.0}
        for item in self.storage.values():
            if item["user_id"] != user_id:
                continue
            totals[item["type"].value] += item["amount"]
        return totals
