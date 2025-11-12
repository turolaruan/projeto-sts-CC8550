"""User repository implementations."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.models.common import ensure_object_id
from src.models.user import User
from src.repositories.base import Repository
from src.repositories.mongo_compat import (
    ASCENDING,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
    DuplicateKeyError,
    ReturnDocument,
    ensure_motor_dependencies,
)
from src.utils.exceptions import EntityAlreadyExistsError


class UserRepository(Repository[User, str]):
    """Mongo-backed repository for users."""

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("users")
        self._indexes_ready: bool = False

    async def create(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            ) from exc
        return entity

    async def get(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_user(document)

    async def get_by_email(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"email": email.lower()})
        if not document:
            return None
        return _document_to_user(document)

    async def list(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def delete(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def _ensure_indexes(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True


class InMemoryUserRepository(Repository[User, str]):
    """In-memory repository for testing purposes."""

    def __init__(self) -> None:
        self._storage: Dict[str, User] = {}

    async def create(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def get(self, entity_id: str) -> Optional[User]:
        return self._storage.get(entity_id)

    async def list(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def delete(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None


def _user_to_document(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop("id", None)
    return data


def _document_to_user(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    return User(**document)
