"""Category repository implementations."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.models.category import Category
from src.models.common import ensure_object_id
from src.repositories.base import Repository
from src.repositories.mongo_compat import (
    ASCENDING,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
    ReturnDocument,
    ensure_motor_dependencies,
)


class CategoryRepository(Repository[Category, str]):
    """Mongo-backed repository for categories."""

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("categories")
        self._indexes_ready = False

    async def create(self, entity: Category) -> Category:
        await self._ensure_indexes()
        await self._collection.insert_one(_category_to_document(entity))
        return entity

    async def get(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_category(document)

    async def list(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def delete(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def _ensure_indexes(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True


class InMemoryCategoryRepository(Repository[Category, str]):
    """In-memory repository for categories."""

    def __init__(self) -> None:
        self._storage: Dict[str, Category] = {}

    async def create(self, entity: Category) -> Category:
        self._storage[entity.id] = entity
        return entity

    async def get(self, entity_id: str) -> Optional[Category]:
        return self._storage.get(entity_id)

    async def list(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def delete(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None


def _category_to_document(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def _document_to_category(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def _prepare_category_update(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data
