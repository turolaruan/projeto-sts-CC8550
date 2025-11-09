"""Account repository implementations."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, Iterable, List, Optional

from bson.decimal128 import Decimal128
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from pymongo import ASCENDING, ReturnDocument

from src.models.account import Account
from src.models.common import ensure_object_id
from src.repositories.base import Repository


class AccountRepository(Repository[Account, str]):
    """Mongo-backed repository for accounts."""

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        self._collection: AsyncIOMotorCollection = database.get_collection("accounts")
        self._indexes_ready = False

    async def create(self, entity: Account) -> Account:
        await self._ensure_indexes()
        await self._collection.insert_one(_account_to_document(entity))
        return entity

    async def get(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_account(document)

    async def list(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def delete(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def _ensure_indexes(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True


class InMemoryAccountRepository(Repository[Account, str]):
    """In-memory repository for accounts (useful in tests)."""

    def __init__(self) -> None:
        self._storage: Dict[str, Account] = {}

    async def create(self, entity: Account) -> Account:
        self._storage[entity.id] = entity
        return entity

    async def get(self, entity_id: str) -> Optional[Account]:
        return self._storage.get(entity_id)

    async def list(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def delete(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None


def _account_to_document(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def _document_to_account(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def _prepare_account_update(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data
