"""Structural tests covering repository infrastructure and transaction-specific logic."""

from __future__ import annotations

import unittest
from datetime import datetime
from types import SimpleNamespace
from typing import Any, Dict, List

from src.models import MongoBaseModel, TransactionFilter
from src.repositories import TransactionRepository
from src.repositories.base import AbstractRepository


class DummyModel(MongoBaseModel):
    value: str


class FakeCursor:
    def __init__(self, documents: List[dict[str, Any]]):
        self._docs = [doc.copy() for doc in documents]
        self._iter = iter(self._docs)

    def sort(self, field: str, direction: int):
        reverse = direction < 0
        self._docs.sort(key=lambda doc: doc.get(field), reverse=reverse)
        self._iter = iter(self._docs)
        return self

    def __aiter__(self):
        self._iter = iter(self._docs)
        return self

    async def __anext__(self):
        try:
            return next(self._iter)
        except StopIteration as exc:
            raise StopAsyncIteration from exc


class FakeAggregation:
    def __init__(self, rows: List[dict[str, Any]]):
        self._rows = rows

    async def to_list(self, length=None):
        return self._rows


class FakeCollection:
    def __init__(self):
        self.documents: Dict[str, dict[str, Any]] = {}

    @staticmethod
    def _match(doc: dict[str, Any], filters: dict[str, Any]) -> bool:
        if not filters:
            return True
        for key, value in filters.items():
            if isinstance(value, dict):
                if "$all" in value:
                    target = doc.get(key, [])
                    if not set(value["$all"]).issubset(set(target)):
                        return False
                else:
                    lower = value.get("$gte")
                    upper = value.get("$lte")
                    candidate = doc.get(key)
                    if lower is not None and candidate < lower:
                        return False
                    if upper is not None and candidate > upper:
                        return False
            else:
                if doc.get(key) != value:
                    return False
        return True

    async def insert_one(self, payload: dict[str, Any]):
        document = payload.copy()
        doc_id = str(document.pop("_id", f"doc-{len(self.documents) + 1}"))
        document["_id"] = doc_id
        self.documents[doc_id] = document
        return SimpleNamespace(inserted_id=doc_id)

    async def find_one(self, filters: dict[str, Any], projection: dict[str, int] | None = None):
        for doc in self.documents.values():
            if self._match(doc, filters):
                return doc.copy()
        return None

    def find(self, filters: dict[str, Any] | None = None):
        matched = [
            doc.copy()
            for doc in self.documents.values()
            if self._match(doc, filters or {})
        ]
        return FakeCursor(matched)

    async def update_one(self, query: dict[str, Any], payload: dict[str, Any]):
        document = await self.find_one(query)
        if not document:
            return
        document.update(payload.get("$set", {}))
        self.documents[str(document["_id"])] = document

    async def delete_one(self, query: dict[str, Any]):
        key = str(query.get("_id"))
        removed = self.documents.pop(key, None)
        return SimpleNamespace(deleted_count=1 if removed else 0)

    def aggregate(self, pipeline: list[dict[str, Any]]):
        match_stage = pipeline[0].get("$match", {})
        grouped: Dict[str, float] = {}
        for doc in self.documents.values():
            if not self._match(doc, match_stage):
                continue
            type_key = doc.get("type", "").upper()
            grouped[type_key] = grouped.get(type_key, 0.0) + float(doc.get("amount", 0.0))
        rows = [{"_id": key, "total": total} for key, total in grouped.items()]
        return FakeAggregation(rows)


class FakeDatabase(dict):
    def __getitem__(self, name: str) -> FakeCollection:
        if name not in self:
            super().__setitem__(name, FakeCollection())
        return super().__getitem__(name)


class DummyRepository(AbstractRepository[DummyModel]):
    collection_name = "dummy"
    model = DummyModel

    @staticmethod
    def _to_object_id(entity_id: str):
        return entity_id


class TestAbstractRepository(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.database = FakeDatabase()
        self.repository = DummyRepository(self.database)

    async def test_create_and_get_by_id(self):
        created = await self.repository.create({"id": "ignored", "value": "alpha"})
        self.assertEqual(created.value, "alpha")
        fetched = await self.repository.get_by_id(created.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, created.id)

    async def test_list_filters_and_exists(self):
        await self.repository.create({"value": "keep"})
        await self.repository.create({"value": "other"})

        filtered = await self.repository.list({"value": "keep"})
        self.assertEqual(len(filtered), 1)
        self.assertTrue(await self.repository.exists({"value": "keep"}))

    async def test_update_and_delete(self):
        created = await self.repository.create({"value": "initial"})
        updated = await self.repository.update(created.id, {"value": "updated"})
        self.assertIsNotNone(updated)
        self.assertEqual(updated.value, "updated")
        self.assertIsNotNone(updated.updated_at)

        deleted = await self.repository.delete(created.id)
        self.assertTrue(deleted)
        missing_delete = await self.repository.delete("missing")
        self.assertFalse(missing_delete)


class TestTransactionRepository(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.database = FakeDatabase()
        self.repository = TransactionRepository(self.database)
        original_converter = TransactionRepository._to_object_id
        TransactionRepository._to_object_id = staticmethod(lambda value: value)
        self.addCleanup(lambda: setattr(TransactionRepository, "_to_object_id", original_converter))

    async def _insert_transaction(self, **overrides):
        document = {
            "_id": overrides.get("_id", f"tx-{len(self.repository.collection.documents) + 1}"),
            "user_id": overrides.get("user_id", "user-1"),
            "account_id": overrides.get("account_id", "account-1"),
            "type": overrides.get("type", "expense"),
            "category": overrides.get("category", "groceries"),
            "description": overrides.get("description", "desc"),
            "amount": overrides.get("amount", 100.0),
            "event_date": overrides.get("event_date", datetime(2024, 1, 1)),
            "tags": overrides.get("tags", ["food"]),
        }
        await self.repository.collection.insert_one(document)
        return document

    async def test_search_applies_filters_and_sorting(self):
        await self._insert_transaction(amount=90, event_date=datetime(2024, 1, 15), tags=["food"])
        await self._insert_transaction(amount=180, event_date=datetime(2024, 1, 20), tags=["food", "family"])
        await self._insert_transaction(amount=25, category="rent", tags=["home"])

        filters = TransactionFilter(
            user_id="user-1",
            start_date=datetime(2024, 1, 10),
            end_date=datetime(2024, 1, 31),
            category="groceries",
            min_amount=50,
            max_amount=200,
            tags=["food"],
            sort_by="amount",
            sort_order=-1,
        )

        results = await self.repository.search(filters)

        self.assertEqual(len(results), 2)
        self.assertGreaterEqual(results[0].amount, results[1].amount)
        self.assertTrue(all(r.category == "groceries" for r in results))

    async def test_total_by_type_aggregates_values(self):
        await self._insert_transaction(type="expense", amount=50)
        await self._insert_transaction(type="income", amount=120)
        await self._insert_transaction(type="expense", amount=30, user_id="user-2")

        totals = await self.repository.total_by_type("user-1")

        self.assertEqual(totals["income"], 120)
        self.assertEqual(totals["expense"], 50)
