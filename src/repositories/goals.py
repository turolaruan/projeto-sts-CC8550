"""Goal repository implementation."""

from __future__ import annotations

from datetime import date
from typing import Optional

from src.models import GoalModel, GoalStatus
from src.utils import serialize_document

from .base import AbstractRepository


class GoalRepository(AbstractRepository[GoalModel]):
    """Persistence operations for goals."""

    collection_name = "goals"
    model = GoalModel

    async def increment_amount(self, goal_id: str, delta: float) -> Optional[GoalModel]:
        """Increment current amount and return the updated goal."""

        await self.collection.update_one(
            {"_id": self._to_object_id(goal_id)},
            {"$inc": {"current_amount": delta}},
        )
        document = await self.collection.find_one({"_id": self._to_object_id(goal_id)})
        return GoalModel(**serialize_document(document)) if document else None

    async def adjust_reserved(self, goal_id: str, delta: float) -> Optional[GoalModel]:
        """Increment reserved amount and return goal."""

        await self.collection.update_one(
            {"_id": self._to_object_id(goal_id)},
            {"$inc": {"reserved_amount": delta}},
        )
        document = await self.collection.find_one({"_id": self._to_object_id(goal_id)})
        return GoalModel(**serialize_document(document)) if document else None

    async def list_active(self, user_id: str):
        """Return active goals for the user."""

        cursor = self.collection.find({"user_id": user_id, "status": GoalStatus.ACTIVE.value})
        return [GoalModel(**serialize_document(doc)) async for doc in cursor]

    async def get_due_goals(self, target_date: date):
        """Return goals that should be completed by the provided date."""

        cursor = self.collection.find({"target_date": {"$lte": target_date}})
        return [GoalModel(**serialize_document(doc)) async for doc in cursor]
