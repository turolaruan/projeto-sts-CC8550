"""Base classes for repository implementations."""

from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import Any, ClassVar, Generic, Optional, TypeVar

from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase

from src.models import MongoBaseModel
from src.utils import serialize_document

ModelType = TypeVar("ModelType", bound=MongoBaseModel)


class AbstractRepository(Generic[ModelType], ABC):
    """Generic repository implementing CRUD helpers."""

    collection_name: ClassVar[str]
    model: ClassVar[type[ModelType]]

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        self.database = database
        self.collection: AsyncIOMotorCollection = database[self.collection_name]

    async def create(self, payload: dict[str, Any]) -> ModelType:
        """Insert a new document and return the corresponding model."""

        sanitized = {k: v for k, v in payload.items() if k != "id"}
        sanitized.setdefault("created_at", datetime.utcnow())
        result = await self.collection.insert_one(sanitized)
        persisted = await self.collection.find_one({"_id": result.inserted_id})
        return self.model(**serialize_document(persisted))

    async def get_by_id(self, entity_id: str) -> Optional[ModelType]:
        """Fetch a document by identifier."""

        document = await self.collection.find_one({"_id": self._to_object_id(entity_id)})
        return self.model(**serialize_document(document)) if document else None

    async def list(self, filters: Optional[dict[str, Any]] = None) -> list[ModelType]:
        """Return all documents matching the provided filters."""

        cursor = self.collection.find(filters or {})
        documents = [self.model(**serialize_document(doc)) async for doc in cursor]
        return documents

    async def update(self, entity_id: str, payload: dict[str, Any]) -> Optional[ModelType]:
        """Update a document partially."""

        sanitized = {k: v for k, v in payload.items() if k != "id"}
        sanitized["updated_at"] = datetime.utcnow()
        await self.collection.update_one(
            {"_id": self._to_object_id(entity_id)},
            {"$set": sanitized},
        )
        document = await self.collection.find_one({"_id": self._to_object_id(entity_id)})
        return self.model(**serialize_document(document)) if document else None

    async def delete(self, entity_id: str) -> bool:
        """Remove a document by identifier."""

        result = await self.collection.delete_one({"_id": self._to_object_id(entity_id)})
        return result.deleted_count == 1

    @staticmethod
    def _to_object_id(entity_id: str):
        """Convert string ids to ObjectId when possible."""

        from bson import ObjectId

        return ObjectId(entity_id)

    async def exists(self, filters: dict[str, Any]) -> bool:
        """Return whether the filter matches any document."""

        document = await self.collection.find_one(filters, projection={"_id": 1})
        return document is not None
