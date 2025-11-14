"""Integration tests hitting FastAPI endpoints."""

from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from httpx import ASGITransport, AsyncClient

from src.controllers.dependencies import (
    get_account_service,
    get_budget_service,
    get_goal_service,
    get_report_service,
    get_transaction_service,
    get_user_service,
)
from src.main import create_app
from src.models import AccountCreate, AccountType
from src.services import AccountService, BudgetService, GoalService, ReportService, TransactionService, UserService
from src.utils import FileManager
from tests.fixtures.factories import make_budget_create, make_transaction_create, make_user_create
from tests.fixtures.memory_repositories import (
    MemoryAccountRepository,
    MemoryBudgetRepository,
    MemoryGoalRepository,
    MemoryTransactionRepository,
    MemoryUserRepository,
)


class TestIntegrationFlows(unittest.IsolatedAsyncioTestCase):
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
        self.temp_dir = TemporaryDirectory()
        self.report_service = ReportService(
            repository=self.transaction_repository,
            file_manager=FileManager(base_dir=Path(self.temp_dir.name)),
        )
        self.transaction_service = TransactionService(
            repository=self.transaction_repository,
            account_repository=self.account_repository,
            user_repository=self.user_repository,
            budget_service=self.budget_service,
            goal_service=self.goal_service,
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

    async def test_user_and_account_flow(self):
        user_payload = make_user_create().model_dump()
        response = await self.client.post("/api/v1/users", json=user_payload)
        self.assertEqual(response.status_code, 201)
        user_id = response.json()["id"]

        account_payload = {
            "user_id": user_id,
            "name": "My Wallet",
            "institution": "Bank",
            "type": "checking",
            "balance": 250.0,
        }
        account_response = await self.client.post("/api/v1/accounts", json=account_payload)
        self.assertEqual(account_response.status_code, 201)

        accounts = await self.client.get("/api/v1/accounts", params={"user_id": user_id})
        self.assertEqual(accounts.status_code, 200)
        self.assertEqual(len(accounts.json()), 1)

    async def test_budget_summary_endpoint(self):
        user = await self.user_service.create_user(make_user_create())
        budget_payload = {
            "user_id": user.id,
            "category": "groceries",
            "limit_amount": 300,
            "period_start": "2024-01-01",
            "period_end": "2024-01-31",
            "alerts_enabled": True,
        }

        response = await self.client.post("/api/v1/budgets", json=budget_payload)
        self.assertEqual(response.status_code, 201)

        summary = await self.client.get(f"/api/v1/budgets/summary/{user.id}")
        self.assertEqual(summary.status_code, 200)
        self.assertEqual(summary.json()[0]["category"], "groceries")

    async def test_transaction_search_returns_inserted_items(self):
        user = await self.user_service.create_user(make_user_create())
        account = await self.account_service.create_account(
            AccountCreate(user_id=user.id, name="Wallet", institution="Bank", type=AccountType.CHECKING, balance=400)
        )
        await self.budget_service.create_budget(
            make_budget_create(user_id=user.id, category="groceries", period_start=date(2024, 1, 1), period_end=date(2024, 1, 31))
        )

        tx_payload = {
            "user_id": user.id,
            "account_id": account.id,
            "type": "expense",
            "category": "groceries",
            "description": "Dinner",
            "amount": 60.0,
        }
        await self.client.post("/api/v1/transactions", json=tx_payload)

        response = await self.client.get(
            "/api/v1/transactions/search",
            params={"user_id": user.id, "category": "groceries"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    async def test_goal_contribution_flow(self):
        user = await self.client.post("/api/v1/users", json=make_user_create().model_dump())
        user_id = user.json()["id"]
        account_payload = {
            "user_id": user_id,
            "name": "Savings",
            "institution": "Bank",
            "type": "checking",
            "balance": 500,
        }
        account = await self.client.post("/api/v1/accounts", json=account_payload)
        account_id = account.json()["id"]
        goal_payload = {
            "user_id": user_id,
            "account_id": account_id,
            "name": "Trip",
            "target_amount": 100,
            "target_date": "2024-12-31",
            "lock_funds": False,
        }
        goal = await self.client.post("/api/v1/goals", json=goal_payload)
        goal_id = goal.json()["id"]

        tx_payload = {
            "user_id": user_id,
            "account_id": account_id,
            "goal_id": goal_id,
            "type": "expense",
            "category": "goals",
            "description": "Deposit",
            "amount": 120,
        }
        tx_response = await self.client.post("/api/v1/transactions", json=tx_payload)
        self.assertEqual(tx_response.status_code, 201)

        goal_response = await self.client.get(f"/api/v1/goals/{goal_id}")
        self.assertGreaterEqual(goal_response.json()["current_amount"], 120)

    async def test_report_endpoint_generates_payload(self):
        user = await self.user_service.create_user(make_user_create())
        account = await self.account_service.create_account(
            AccountCreate(user_id=user.id, name="Report", institution="Bank", type=AccountType.CHECKING, balance=100)
        )
        await self.transaction_service.create_transaction(
            make_transaction_create(user_id=user.id, account_id=account.id, amount=20, description="Lunch")
        )
        await self.transaction_service.create_transaction(
            make_transaction_create(
                user_id=user.id,
                account_id=account.id,
                type="income",
                amount=200,
                description="Bonus",
            )
        )

        response = await self.client.get(f"/api/v1/reports/transactions/{user.id}")

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json()["total_transactions"], 1)

    async def test_budget_creation_overlap_returns_conflict(self):
        user = await self.user_service.create_user(make_user_create())
        payload = {
            "user_id": user.id,
            "category": "travel",
            "limit_amount": 200,
            "period_start": "2024-02-01",
            "period_end": "2024-02-28",
        }
        first = await self.client.post("/api/v1/budgets", json=payload)
        self.assertEqual(first.status_code, 201)
        conflict = await self.client.post("/api/v1/budgets", json=payload)
        self.assertEqual(conflict.status_code, 409)

    async def test_user_update_endpoint(self):
        create = await self.client.post("/api/v1/users", json=make_user_create().model_dump())
        user_id = create.json()["id"]
        update_payload = {"name": "Updated", "monthly_income": 8000}
        response = await self.client.put(f"/api/v1/users/{user_id}", json=update_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Updated")

    async def test_account_delete_endpoint_removes_account(self):
        user = await self.client.post("/api/v1/users", json=make_user_create().model_dump())
        user_id = user.json()["id"]
        account_payload = {
            "user_id": user_id,
            "name": "Temp",
            "institution": "Bank",
            "type": "checking",
            "balance": 100,
        }
        account = await self.client.post("/api/v1/accounts", json=account_payload)
        account_id = account.json()["id"]
        delete_resp = await self.client.delete(f"/api/v1/accounts/{account_id}")
        self.assertEqual(delete_resp.status_code, 204)
        list_resp = await self.client.get("/api/v1/accounts", params={"user_id": user_id})
        self.assertEqual(list_resp.json(), [])

    async def test_goal_delete_releases_locked_amount(self):
        user_resp = await self.client.post("/api/v1/users", json=make_user_create().model_dump())
        user_id = user_resp.json()["id"]
        account_payload = {
            "user_id": user_id,
            "name": "Lock",
            "institution": "Bank",
            "type": "checking",
            "balance": 500,
        }
        account_resp = await self.client.post("/api/v1/accounts", json=account_payload)
        account_id = account_resp.json()["id"]
        goal_payload = {
            "user_id": user_id,
            "account_id": account_id,
            "name": "Reserve",
            "target_amount": 300,
            "target_date": "2024-12-01",
            "lock_funds": True,
        }
        goal_resp = await self.client.post("/api/v1/goals", json=goal_payload)
        goal_id = goal_resp.json()["id"]
        tx_payload = {
            "user_id": user_id,
            "account_id": account_id,
            "goal_id": goal_id,
            "type": "expense",
            "category": "goal",
            "description": "Lock",
            "amount": 100,
        }
        await self.client.post("/api/v1/transactions", json=tx_payload)
        delete_resp = await self.client.delete(f"/api/v1/goals/{goal_id}")
        self.assertEqual(delete_resp.status_code, 204)
        account_after = await self.client.get(f"/api/v1/accounts/{account_id}")
        self.assertEqual(account_after.json()["goal_locked_amount"], 0)

    async def test_transaction_with_goal_wrong_type_returns_conflict(self):
        user_resp = await self.client.post("/api/v1/users", json=make_user_create().model_dump())
        user_id = user_resp.json()["id"]
        account_payload = {
            "user_id": user_id,
            "name": "Goal",
            "institution": "Bank",
            "type": "checking",
            "balance": 400,
        }
        account_resp = await self.client.post("/api/v1/accounts", json=account_payload)
        account_id = account_resp.json()["id"]
        goal_payload = {
            "user_id": user_id,
            "account_id": account_id,
            "name": "Trip",
            "target_amount": 500,
            "target_date": "2024-11-30",
            "lock_funds": False,
        }
        goal_resp = await self.client.post("/api/v1/goals", json=goal_payload)
        tx_payload = {
            "user_id": user_id,
            "account_id": account_id,
            "goal_id": goal_resp.json()["id"],
            "type": "income",
            "category": "goal",
            "description": "Invalid",
            "amount": 50,
        }
        response = await self.client.post("/api/v1/transactions", json=tx_payload)
        self.assertEqual(response.status_code, 409)

    async def test_get_missing_user_returns_404_with_json(self):
        response = await self.client.get("/api/v1/users/ghost-user")

        self.assertEqual(response.status_code, 404)
        body = response.json()
        self.assertIn("detail", body)
        self.assertTrue(body["detail"])

    async def test_update_nonexistent_account_returns_404(self):
        payload = {
            "name": "Updated",
            "institution": "Bank",
            "type": "checking",
            "balance": 100,
        }

        response = await self.client.put("/api/v1/accounts/invalid-id", json=payload)

        self.assertEqual(response.status_code, 404)
        self.assertIn("account", response.json()["detail"].lower())
