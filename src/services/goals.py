"""Business logic for savings goals."""

from __future__ import annotations

from typing import List

from src.models import GoalCreate, GoalModel, GoalStatus, GoalUpdate
from src.repositories import AccountRepository, GoalRepository

from .exceptions import BusinessRuleError, NotFoundError


class GoalService:
    """Service coordinating goal operations with accounts."""

    def __init__(self, repository: GoalRepository, account_repository: AccountRepository) -> None:
        self.repository = repository
        self.account_repository = account_repository

    async def create_goal(self, payload: GoalCreate) -> GoalModel:
        """Create a new goal ensuring the account exists."""

        account = await self.account_repository.get_by_id(payload.account_id)
        if not account:
            raise NotFoundError("Account not found for goal")
        if account.user_id != payload.user_id:
            raise BusinessRuleError("Goal account mismatch")
        return await self.repository.create(payload.model_dump())

    async def list_goals(self, user_id: str) -> List[GoalModel]:
        """Return all goals for a user."""

        return await self.repository.list({"user_id": user_id})

    async def get_goal(self, goal_id: str) -> GoalModel:
        """Fetch goal or raise."""

        goal = await self.repository.get_by_id(goal_id)
        if not goal:
            raise NotFoundError("Goal not found")
        return goal

    async def update_goal(self, goal_id: str, payload: GoalUpdate) -> GoalModel:
        """Update goal fields."""

        data = payload.model_dump(exclude_none=True)
        updated = await self.repository.update(goal_id, data)
        if not updated:
            raise NotFoundError("Goal not found")
        return updated

    async def delete_goal(self, goal_id: str) -> bool:
        """Delete goal and release locked amounts."""

        goal = await self.repository.get_by_id(goal_id)
        if not goal:
            raise NotFoundError("Goal not found")
        deleted = await self.repository.delete(goal_id)
        if deleted and goal.lock_funds and goal.reserved_amount:
            await self.account_repository.update_goal_lock(goal.account_id, -goal.reserved_amount)
        return deleted

    async def apply_contribution(self, goal_id: str, amount: float) -> GoalModel:
        """Add a contribution to the goal and optionally lock funds."""

        goal = await self.get_goal(goal_id)
        account = await self.account_repository.get_by_id(goal.account_id)
        if not account:
            raise NotFoundError("Account not found for goal contribution")
        available_balance = account.balance - account.goal_locked_amount
        if goal.lock_funds and available_balance < amount:
            raise BusinessRuleError("Insufficient free balance for locked goal contribution")
        if goal.lock_funds:
            await self.account_repository.update_goal_lock(goal.account_id, amount)
            await self.repository.adjust_reserved(goal_id, amount)
        updated_goal = await self.repository.increment_amount(goal_id, amount)
        if updated_goal and updated_goal.current_amount >= updated_goal.target_amount:
            await self.repository.update(goal_id, {"status": GoalStatus.COMPLETED.value})
            if updated_goal.lock_funds:
                release_amount = updated_goal.reserved_amount
                await self.repository.adjust_reserved(goal_id, -release_amount)
                await self.account_repository.update_goal_lock(goal.account_id, -release_amount)
        return await self.get_goal(goal_id)
