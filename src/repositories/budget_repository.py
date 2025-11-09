"""Budget repository implementations."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, Iterable, List, Optional

from bson.decimal128 import Decimal128
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from pymongo import ASCENDING, ReturnDocument

from src.models.budget import Budget
from src.models.common import ensure_object_id
from src.repositories.base import Repository


class BudgetRepository(Repository[Budget, str]):
    """Mongo-backed repository for budgets."""

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        self._collection: AsyncIOMotorCollection = database.get_collection("budgets")
        self._indexes_ready = False

    async def create(self, entity: Budget) -> Budget:
        await self._ensure_indexes()
        await self._collection.insert_one(_budget_to_document(entity))
        return entity

    async def get(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_budget(document)

    async def list(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def delete(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def find_by_period(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def _ensure_indexes(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True


class InMemoryBudgetRepository(Repository[Budget, str]):
    """In-memory repository for budgets."""

    def __init__(self) -> None:
        self._storage: Dict[str, Budget] = {}

    async def create(self, entity: Budget) -> Budget:
        self._storage[entity.id] = entity
        return entity

    async def get(self, entity_id: str) -> Optional[Budget]:
        return self._storage.get(entity_id)

    async def list(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def delete(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def find_by_period(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id == category_id
                and budget.year == year
                and budget.month == month
            ):
                return budget
        return None


def _budget_to_document(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def _document_to_budget(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def _prepare_budget_update(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data
