"""Unit tests for TransactionService."""

import unittest

from src.models import TransactionFilter, TransactionType, TransactionUpdate
from src.services import (
    BudgetService,
    BusinessRuleError,
    GoalService,
    NotFoundError,
    TransactionService,
)
from tests.fixtures.factories import (
    make_account_model,
    make_budget_model,
    make_transaction_create,
    make_user_model,
)
from tests.fixtures.memory_repositories import (
    MemoryAccountRepository,
    MemoryBudgetRepository,
    MemoryGoalRepository,
    MemoryTransactionRepository,
    MemoryUserRepository,
)


class TestTransactionService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.transaction_repository = MemoryTransactionRepository()
        self.user_repository = MemoryUserRepository()
        self.account_repository = MemoryAccountRepository()
        self.budget_repository = MemoryBudgetRepository()
        self.goal_repository = MemoryGoalRepository()
        self.budget_service = BudgetService(repository=self.budget_repository)
        self.goal_service = GoalService(repository=self.goal_repository, account_repository=self.account_repository)
        self.service = TransactionService(
            repository=self.transaction_repository,
            account_repository=self.account_repository,
            user_repository=self.user_repository,
            budget_service=self.budget_service,
            goal_service=self.goal_service,
        )

    async def test_create_transaction_updates_balance_and_budget(self):
        user = make_user_model()
        account = make_account_model(user_id=user.id, balance=400)
        budget = make_budget_model(user_id=user.id, category="groceries", limit_amount=300)
        self.user_repository.storage[user.id] = user.model_dump()
        self.account_repository.storage[account.id] = account.model_dump()
        self.budget_repository.storage[budget.id] = budget.model_dump()

        payload = make_transaction_create(user_id=user.id, account_id=account.id, category="groceries", amount=50)

        transaction = await self.service.create_transaction(payload)

        self.assertEqual(transaction.amount, 50)
        self.assertEqual(self.account_repository.storage[account.id]["balance"], 350)
        self.assertEqual(self.budget_repository.storage[budget.id]["amount_spent"], 50)

    async def test_create_expense_with_locked_funds_raises(self):
        user = make_user_model()
        account = make_account_model(user_id=user.id, balance=100, goal_locked_amount=80)
        self.user_repository.storage[user.id] = user.model_dump()
        self.account_repository.storage[account.id] = account.model_dump()
        payload = make_transaction_create(user_id=user.id, account_id=account.id, amount=50)

        with self.assertRaises(BusinessRuleError):
            await self.service.create_transaction(payload)

    async def test_income_transaction_increases_balance(self):
        user = make_user_model()
        account = make_account_model(user_id=user.id, balance=100)
        self.user_repository.storage[user.id] = user.model_dump()
        self.account_repository.storage[account.id] = account.model_dump()
        payload = make_transaction_create(
            user_id=user.id,
            account_id=account.id,
            type=TransactionType.INCOME,
            amount=200,
        )

        await self.service.create_transaction(payload)

        self.assertEqual(self.account_repository.storage[account.id]["balance"], 300)

    async def test_search_transactions_filters_by_category(self):
        tx_a = await self.transaction_repository.create(make_transaction_create(category="groceries").model_dump())
        await self.transaction_repository.create(make_transaction_create(category="rent", user_id=tx_a.user_id).model_dump())

        filters = TransactionFilter(user_id=tx_a.user_id, category="groceries")
        results = await self.service.search_transactions(filters)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].category, "groceries")

    async def test_update_transaction_changes_description(self):
        tx = await self.transaction_repository.create(make_transaction_create(description="Lunch").model_dump())

        updated = await self.service.update_transaction(tx.id, TransactionUpdate(description="Dinner"))

        self.assertEqual(updated.description, "Dinner")

    async def test_update_transaction_missing_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.update_transaction("missing", make_transaction_create())

    async def test_delete_transaction_removes_entry(self):
        tx = await self.transaction_repository.create(make_transaction_create().model_dump())

        result = await self.service.delete_transaction(tx.id)

        self.assertTrue(result)
        self.assertNotIn(tx.id, self.transaction_repository.storage)

    async def test_delete_transaction_missing_raises(self):
        for missing_id in ("missing", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.delete_transaction(missing_id)

    async def test_create_transaction_missing_user_raises(self):
        payload = make_transaction_create()

        with self.assertRaises(NotFoundError):
            await self.service.create_transaction(payload)

    async def test_get_transaction_returns_entry(self):
        tx = await self.transaction_repository.create(make_transaction_create(description="Coffee").model_dump())

        fetched = await self.service.get_transaction(tx.id)

        self.assertEqual(fetched.description, "Coffee")

    async def test_get_transaction_missing_raises(self):
        for missing_id in ("unknown", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.get_transaction(missing_id)

    async def test_get_budget_helper_skips_when_requested(self):
        payload = make_transaction_create()

        result = await self.service._get_budget(payload, skip_budget=True)

        self.assertIsNone(result)

    async def test_get_budget_helper_returns_none_for_income(self):
        payload = make_transaction_create(type=TransactionType.INCOME)

        result = await self.service._get_budget(payload, skip_budget=False)

        self.assertIsNone(result)

    async def test_list_transactions_returns_entries(self):
        tx = await self.transaction_repository.create(make_transaction_create().model_dump())

        results = await self.service.list_transactions(tx.user_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, tx.id)
