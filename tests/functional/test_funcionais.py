"""Functional (black-box) scenarios validating complete flows."""

from __future__ import annotations

import unittest
from datetime import date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from httpx import ASGITransport, AsyncClient, Response

from src.controllers.dependencies import (
    get_account_service,
    get_budget_service,
    get_goal_service,
    get_report_service,
    get_transaction_service,
    get_user_service,
)
from src.main import create_app
from src.services import AccountService, BudgetService, GoalService, ReportService, TransactionService, UserService
from src.utils import FileManager
from tests.fixtures.factories import make_budget_create, make_user_create
from tests.fixtures.memory_repositories import (
    MemoryAccountRepository,
    MemoryBudgetRepository,
    MemoryGoalRepository,
    MemoryTransactionRepository,
    MemoryUserRepository,
)


class TestFunctionalScenarios(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.user_repository = MemoryUserRepository()
        self.account_repository = MemoryAccountRepository()
        self.budget_repository = MemoryBudgetRepository()
        self.goal_repository = MemoryGoalRepository()
        self.transaction_repository = MemoryTransactionRepository()
        self.user_service = UserService(repository=self.user_repository)
        self.account_service = AccountService(repository=self.account_repository, user_repository=self.user_repository)
        self.budget_service = BudgetService(repository=self.budget_repository)
        self.goal_service = GoalService(repository=self.goal_repository, account_repository=self.account_repository)
        self.transaction_service = TransactionService(
            repository=self.transaction_repository,
            account_repository=self.account_repository,
            user_repository=self.user_repository,
            budget_service=self.budget_service,
            goal_service=self.goal_service,
        )
        self.temp_dir = TemporaryDirectory()
        self.report_service = ReportService(
            repository=self.transaction_repository,
            file_manager=FileManager(base_dir=Path(self.temp_dir.name)),
        )
        self.app = create_app()
        self.app.dependency_overrides[get_user_service] = lambda: self.user_service
        self.app.dependency_overrides[get_account_service] = lambda: self.account_service
        self.app.dependency_overrides[get_budget_service] = lambda: self.budget_service
        self.app.dependency_overrides[get_goal_service] = lambda: self.goal_service
        self.app.dependency_overrides[get_transaction_service] = lambda: self.transaction_service
        self.app.dependency_overrides[get_report_service] = lambda: self.report_service
        transport = ASGITransport(app=self.app)
        self.client = AsyncClient(transport=transport, base_url="http://testserver")

    async def asyncTearDown(self):
        await self.client.aclose()
        self.temp_dir.cleanup()

    async def _create_user(self) -> str:
        response = await self.client.post("/api/v1/users", json=make_user_create().model_dump())
        self.assertEqual(response.status_code, 201)
        return response.json()["id"]

    async def _create_account(self, user_id: str, *, name: str = "Wallet", balance: float = 500.0) -> str:
        payload = {
            "user_id": user_id,
            "name": name,
            "institution": "Bank",
            "type": "checking",
            "balance": balance,
        }
        response = await self.client.post("/api/v1/accounts", json=payload)
        self.assertEqual(response.status_code, 201)
        return response.json()["id"]

    async def _create_budget(self, **overrides) -> str:
        payload = make_budget_create(**overrides).model_dump()
        payload["period_start"] = payload["period_start"].isoformat()
        payload["period_end"] = payload["period_end"].isoformat()
        response = await self.client.post("/api/v1/budgets", json=payload)
        self.assertEqual(response.status_code, 201)
        return response.json()["id"]

    async def _create_goal(self, user_id: str, account_id: str, **overrides) -> str:
        payload = {
            "user_id": user_id,
            "account_id": account_id,
            "name": overrides.get("name", "Goal"),
            "target_amount": overrides.get("target_amount", 500),
            "target_date": overrides.get("target_date", "2024-12-31"),
            "lock_funds": overrides.get("lock_funds", False),
        }
        response = await self.client.post("/api/v1/goals", json=payload)
        self.assertEqual(response.status_code, 201)
        return response.json()["id"]

    async def _post_transaction(self, payload: dict) -> Response:
        return await self.client.post("/api/v1/transactions", json=payload)

    async def test_user_cannot_exceed_budget(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, balance=500)
        await self._create_budget(
            user_id=user_id,
            category="travel",
            limit_amount=100,
            period_start=date(2024, 1, 1),
            period_end=date(2024, 1, 31),
        )

        payload = {
            "user_id": user_id,
            "account_id": account_id,
            "type": "expense",
            "category": "travel",
            "description": "Tickets",
            "amount": 80.0,
            "event_date": "2024-01-10T00:00:00",
        }
        ok_response = await self._post_transaction(payload)
        self.assertEqual(ok_response.status_code, 201)

        payload["amount"] = 50.0
        error_response = await self._post_transaction(payload)
        self.assertEqual(error_response.status_code, 409)
        self.assertIn("Budget", error_response.json()["detail"])

    async def test_report_generation_returns_file(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, name="Main", balance=100)
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "expense",
                "category": "food",
                "description": "Lunch",
                "amount": 20,
            }
        )
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "income",
                "category": "salary",
                "description": "Bonus",
                "amount": 200,
            }
        )

        response = await self.client.get(f"/api/v1/reports/transactions/{user_id}")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["total_transactions"], 2)
        self.assertTrue(payload["file_path"].endswith(".csv"))

    async def test_transaction_search_with_amount_filters(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, name="Daily", balance=300)
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "expense",
                "category": "food",
                "description": "Lunch",
                "amount": 40,
            }
        )
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "expense",
                "category": "food",
                "description": "Grocery",
                "amount": 150,
            }
        )

        response = await self.client.get(
            "/api/v1/transactions/search",
            params={"user_id": user_id, "min_amount": 100, "max_amount": 200},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    async def test_account_creation_with_invalid_user_returns_404(self):
        payload = {
            "user_id": "non-existent",
            "name": "Ghost",
            "institution": "Nowhere",
            "type": "checking",
            "balance": 10,
        }

        response = await self.client.post("/api/v1/accounts", json=payload)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "User not found for account creation")

    async def test_goal_completion_flow(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, name="Goals", balance=1000)
        goal_id = await self._create_goal(user_id, account_id, name="Laptop", target_amount=500)

        for amount in (300, 250):
            await self._post_transaction(
                {
                    "user_id": user_id,
                    "account_id": account_id,
                    "goal_id": goal_id,
                    "type": "expense",
                    "category": "goal",
                    "description": f"Contribution {amount}",
                    "amount": amount,
                }
            )

        goal = await self.client.get(f"/api/v1/goals/{goal_id}")
        self.assertEqual(goal.json()["status"], "completed")

    async def test_transaction_negative_amount_validation(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, name="Daily", balance=100)

        payload = {
            "user_id": user_id,
            "account_id": account_id,
            "type": "expense",
            "category": "food",
            "description": "Invalid",
            "amount": -10,
        }
        response = await self.client.post("/api/v1/transactions", json=payload)
        self.assertEqual(response.status_code, 422)

    async def test_budget_status_reaches_warning(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, name="Budget", balance=500)
        await self._create_budget(
            user_id=user_id,
            category="food",
            limit_amount=100,
            period_start=date(2024, 1, 1),
            period_end=date(2024, 1, 31),
        )
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "expense",
                "category": "food",
                "description": "Groceries",
                "amount": 90,
                "event_date": datetime(2024, 1, 10).isoformat(),
            }
        )
        summary = await self.client.get(f"/api/v1/budgets/summary/{user_id}")
        self.assertEqual(summary.status_code, 200)
        self.assertIn(summary.json()[0]["status"], {"warning", "exceeded"})

    async def test_report_totals_match_transactions(self):
        user_id = await self._create_user()
        account_id = await self._create_account(user_id, name="Statements", balance=200)
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "expense",
                "category": "food",
                "description": "Lunch",
                "amount": 50,
            }
        )
        await self._post_transaction(
            {
                "user_id": user_id,
                "account_id": account_id,
                "type": "income",
                "category": "bonus",
                "description": "Bonus",
                "amount": 120,
            }
        )
        response = await self.client.get(f"/api/v1/reports/transactions/{user_id}")
        data = response.json()
        self.assertEqual(data["total_expenses"], 50)
        self.assertEqual(data["total_income"], 120)
