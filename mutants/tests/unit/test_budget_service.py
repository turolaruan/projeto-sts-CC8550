"""Unit tests for BudgetService."""

import unittest
from datetime import date, timedelta

from src.models import BudgetUpdate
from src.services import BudgetService, BusinessRuleError, NotFoundError
from tests.fixtures.factories import make_budget_create, make_budget_model
from tests.fixtures.memory_repositories import MemoryBudgetRepository


class TestBudgetService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.repository = MemoryBudgetRepository()
        self.service = BudgetService(repository=self.repository)

    async def test_create_budget_rejects_overlapping_periods(self):
        existing = make_budget_model(category="food")
        self.repository.storage[existing.id] = existing.model_dump()
        payload = make_budget_create(
            user_id=existing.user_id,
            category="food",
            period_start=existing.period_start + timedelta(days=1),
            period_end=existing.period_end,
        )

        with self.assertRaises(BusinessRuleError):
            await self.service.create_budget(payload)

    async def test_apply_expense_beyond_limit_raises(self):
        budget = make_budget_model(limit_amount=100, amount_spent=90)
        self.repository.storage[budget.id] = budget.model_dump()

        with self.assertRaises(BusinessRuleError):
            await self.service.apply_expense(budget, amount=20)

    async def test_apply_expense_within_limit_updates_spent(self):
        budget = make_budget_model(limit_amount=200, amount_spent=50)
        self.repository.storage[budget.id] = budget.model_dump()

        updated = await self.service.apply_expense(budget, amount=75)

        self.assertEqual(updated.amount_spent, 125)

    async def test_get_missing_budget_raises(self):
        for missing_id in ("unknown", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.get_budget(missing_id)

    async def test_create_budget_invalid_period_raises(self):
        invalid_ranges = (
            (date(2024, 2, 1), date(2024, 1, 1)),
            (date(2024, 3, 10), date(2024, 3, 10) - timedelta(days=1)),
        )
        for start, end in invalid_ranges:
            with self.subTest(period=(start, end)):
                payload = make_budget_create(period_start=start, period_end=end)
                with self.assertRaises(BusinessRuleError):
                    await self.service.create_budget(payload)

    async def test_list_budgets_returns_all_for_user(self):
        user_a = make_budget_model(user_id="user-1")
        user_b = make_budget_model(user_id="user-2")
        self.repository.storage[user_a.id] = user_a.model_dump()
        self.repository.storage[user_b.id] = user_b.model_dump()

        results = await self.service.list_budgets("user-1")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].user_id, "user-1")

    async def test_summarize_returns_budget_status(self):
        budget = make_budget_model(user_id="user-1", amount_spent=50, limit_amount=100)
        self.repository.storage[budget.id] = budget.model_dump()

        summary = await self.service.summarize("user-1")

        self.assertEqual(summary[0].remaining, 50)
        self.assertEqual(summary[0].status, budget.status)

    async def test_get_budget_for_returns_matching_period(self):
        budget = make_budget_model(category="rent")
        self.repository.storage[budget.id] = budget.model_dump()

        found = await self.service.get_budget_for(budget.user_id, "rent", budget.period_start)

        self.assertIsNotNone(found)
        self.assertEqual(found.category, "rent")

    async def test_get_budget_returns_entry(self):
        budget = make_budget_model()
        self.repository.storage[budget.id] = budget.model_dump()

        result = await self.service.get_budget(budget.id)

        self.assertEqual(result.id, budget.id)

    async def test_update_budget_changes_limit(self):
        budget = make_budget_model(limit_amount=100)
        self.repository.storage[budget.id] = budget.model_dump()

        updated = await self.service.update_budget(budget.id, BudgetUpdate(limit_amount=250))

        self.assertEqual(updated.limit_amount, 250)

    async def test_delete_budget_returns_true(self):
        budget = make_budget_model()
        self.repository.storage[budget.id] = budget.model_dump()

        self.assertTrue(await self.service.delete_budget(budget.id))

    async def test_update_budget_missing_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.update_budget("missing", BudgetUpdate(limit_amount=10))

    async def test_delete_budget_missing_raises(self):
        for missing_id in ("missing", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.delete_budget(missing_id)

    async def test_summarize_returns_budget_summary(self):
        budget = make_budget_model(user_id="owner", category="entertainment", amount_spent=40, limit_amount=100)
        self.repository.storage[budget.id] = budget.model_dump()

        summaries = await self.service.summarize("owner")

        self.assertEqual(summaries[0].category, "entertainment")
