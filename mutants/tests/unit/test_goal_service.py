"""Unit tests for GoalService."""

import unittest

from src.models import GoalUpdate
from src.services import BusinessRuleError, GoalService, NotFoundError
from tests.fixtures.factories import make_account_model, make_goal_create, make_goal_model
from tests.fixtures.memory_repositories import MemoryAccountRepository, MemoryGoalRepository


class TestGoalService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.account_repository = MemoryAccountRepository()
        self.goal_repository = MemoryGoalRepository()
        self.service = GoalService(repository=self.goal_repository, account_repository=self.account_repository)

    async def test_create_goal_requires_existing_account(self):
        account = make_account_model()
        self.account_repository.storage[account.id] = account.model_dump()
        payload = make_goal_create(user_id=account.user_id, account_id=account.id)

        goal = await self.service.create_goal(payload)

        self.assertEqual(goal.account_id, account.id)

    async def test_create_goal_without_account_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.create_goal(make_goal_create())

    async def test_create_goal_with_mismatched_user_raises(self):
        account = make_account_model()
        self.account_repository.storage[account.id] = account.model_dump()
        payload = make_goal_create(user_id="other-user", account_id=account.id)

        with self.assertRaises(BusinessRuleError):
            await self.service.create_goal(payload)

    async def test_apply_contribution_respects_locked_amount(self):
        account = make_account_model(goal_locked_amount=100, balance=150)
        self.account_repository.storage[account.id] = account.model_dump()
        goal = make_goal_model(account_id=account.id, user_id=account.user_id, lock_funds=True)
        self.goal_repository.storage[goal.id] = goal.model_dump()

        with self.assertRaises(BusinessRuleError):
            await self.service.apply_contribution(goal.id, amount=100)

    async def test_delete_goal_releases_locked_amount(self):
        account = make_account_model(goal_locked_amount=200)
        goal = make_goal_model(account_id=account.id, user_id=account.user_id, lock_funds=True, reserved_amount=200)
        self.account_repository.storage[account.id] = account.model_dump()
        self.goal_repository.storage[goal.id] = goal.model_dump()

        await self.service.delete_goal(goal.id)

        self.assertEqual(self.account_repository.storage[account.id]["goal_locked_amount"], 0)
        self.assertNotIn(goal.id, self.goal_repository.storage)

    async def test_list_goals_returns_user_entries(self):
        goal_a = make_goal_model(user_id="user-1")
        goal_b = make_goal_model(user_id="user-2")
        self.goal_repository.storage[goal_a.id] = goal_a.model_dump()
        self.goal_repository.storage[goal_b.id] = goal_b.model_dump()

        results = await self.service.list_goals("user-1")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].user_id, "user-1")

    async def test_apply_contribution_completes_goal(self):
        account = make_account_model(balance=1000)
        goal = make_goal_model(
            account_id=account.id,
            user_id=account.user_id,
            current_amount=900,
            target_amount=1000,
            lock_funds=False,
        )
        self.account_repository.storage[account.id] = account.model_dump()
        self.goal_repository.storage[goal.id] = goal.model_dump()

        updated = await self.service.apply_contribution(goal.id, amount=150)

        self.assertEqual(updated.status.value, "completed")

    async def test_apply_contribution_with_lock_releases_funds(self):
        account = make_account_model(balance=500, goal_locked_amount=0)
        goal = make_goal_model(
            account_id=account.id,
            user_id=account.user_id,
            current_amount=90,
            target_amount=100,
            lock_funds=True,
            reserved_amount=0,
        )
        self.account_repository.storage[account.id] = account.model_dump()
        self.goal_repository.storage[goal.id] = goal.model_dump()

        updated = await self.service.apply_contribution(goal.id, amount=20)

        self.assertEqual(updated.status.value, "completed")
        self.assertEqual(self.account_repository.storage[account.id]["goal_locked_amount"], 0)

    async def test_update_goal_changes_name(self):
        goal = make_goal_model(name="Trip")
        self.goal_repository.storage[goal.id] = goal.model_dump()

        updated = await self.service.update_goal(goal.id, GoalUpdate(name="Updated"))

        self.assertEqual(updated.name, "Updated")

    async def test_get_goal_missing_raises(self):
        for missing_id in ("missing", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.get_goal(missing_id)

    async def test_update_goal_missing_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.update_goal("missing", GoalUpdate(name="Ghost"))

    async def test_delete_goal_missing_raises(self):
        for missing_id in ("missing", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.delete_goal(missing_id)

    async def test_apply_contribution_missing_account(self):
        goal = make_goal_model()
        self.goal_repository.storage[goal.id] = goal.model_dump()

        with self.assertRaises(NotFoundError):
            await self.service.apply_contribution(goal.id, 10)
