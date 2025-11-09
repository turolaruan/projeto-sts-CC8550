"""Transaction repository implementations."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Dict, Iterable, List, Optional

from bson.decimal128 import Decimal128
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from pymongo import ASCENDING, DESCENDING, ReturnDocument

from src.models.common import ensure_object_id
from src.models.transaction import Transaction
from src.repositories.base import Repository


class TransactionRepository(Repository[Transaction, str]):
    """Mongo-backed repository for transactions."""

    def __init__(self, database: AsyncIOMotorDatabase) -> None:
        self._collection: AsyncIOMotorCollection = database.get_collection("transactions")
        self._indexes_ready = False

    async def create(self, entity: Transaction) -> Transaction:
        await self._ensure_indexes()
        await self._collection.insert_one(_transaction_to_document(entity))
        return entity

    async def get(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_transaction(document)

    async def list(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def delete(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def exists_for_account(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=1) > 0

    async def exists_for_category(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def aggregate_monthly_summary(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def sum_for_category_period(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def _ensure_indexes(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True


class InMemoryTransactionRepository(Repository[Transaction, str]):
    """In-memory repository for transactions."""

    def __init__(self) -> None:
        self._storage: Dict[str, Transaction] = {}

    async def create(self, entity: Transaction) -> Transaction:
        self._storage[entity.id] = entity
        return entity

    async def get(self, entity_id: str) -> Optional[Transaction]:
        return self._storage.get(entity_id)

    async def list(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def update(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def delete(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def exists_for_account(self, account_id: str) -> bool:
        return any(txn.account_id == account_id for txn in self._storage.values())

    async def exists_for_category(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def aggregate_monthly_summary(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
        summary[key]["count"] += 1
        return list(summary.values())

    async def sum_for_category_period(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total


def _transaction_to_document(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def _document_to_transaction(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def _prepare_transaction_update(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data
