"""Transaction repository implementation."""

from __future__ import annotations

from typing import Any

from pymongo import ASCENDING, DESCENDING

from src.models import TransactionFilter, TransactionModel
from src.utils import serialize_document

from .base import AbstractRepository


class TransactionRepository(AbstractRepository[TransactionModel]):
    """Persistence operations for transactions."""

    collection_name = "transactions"
    model = TransactionModel

    async def search(self, filters: TransactionFilter) -> list[TransactionModel]:
        """Return transactions applying filters and ordering."""

        query: dict[str, Any] = {"user_id": filters.user_id}
        if filters.start_date or filters.end_date:
            query["event_date"] = {}
            if filters.start_date:
                query["event_date"]["$gte"] = filters.start_date
            if filters.end_date:
                query["event_date"]["$lte"] = filters.end_date
        if filters.category:
            query["category"] = filters.category
        if filters.min_amount is not None or filters.max_amount is not None:
            query["amount"] = {}
            if filters.min_amount is not None:
                query["amount"]["$gte"] = filters.min_amount
            if filters.max_amount is not None:
                query["amount"]["$lte"] = filters.max_amount
        if filters.tags:
            query["tags"] = {"$all": filters.tags}
        sort_direction = DESCENDING if filters.sort_order < 0 else ASCENDING
        cursor = (
            self.collection.find(query).sort(filters.sort_by, sort_direction)
        )
        documents = [self.model(**serialize_document(doc)) async for doc in cursor]
        return documents

    async def total_by_type(self, user_id: str) -> dict[str, float]:
        """Aggregate totals of income vs expenses for a user."""

        pipeline = [
            {"$match": {"user_id": user_id}},
            {
                "$group": {
                    "_id": "$type",
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        results = await self.collection.aggregate(pipeline).to_list(length=None)
        response = {"income": 0.0, "expense": 0.0}
        for row in results:
            key = row["_id"].lower()
            response[key] = row["total"]
        return response
