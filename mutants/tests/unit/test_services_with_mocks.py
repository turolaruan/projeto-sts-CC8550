"""Tests leveraging mocks/stubs to isolate dependencies."""

import unittest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

from src.models import ReportPayload
from src.services import BusinessRuleError, ReportService, TransactionService
from tests.fixtures.factories import make_transaction_create


class TestServicesWithMocks(unittest.IsolatedAsyncioTestCase):
    async def test_report_service_uses_file_manager(self):
        repo = MagicMock()
        repo.list = AsyncMock(return_value=[])
        file_manager = MagicMock()
        file_manager.export_transactions.return_value = ReportPayload(
            generated_at=datetime.utcnow(),
            file_path="/tmp/report.csv",
            total_transactions=0,
            total_expenses=0,
            total_income=0,
        )

        service = ReportService(repo, file_manager)
        result = await service.export_transactions("user-1")

        repo.list.assert_awaited_once_with({"user_id": "user-1"})
        file_manager.export_transactions.assert_called_once()
        self.assertTrue(result.file_path.endswith("report.csv"))

    async def test_transaction_service_handles_repository_errors_with_mock(self):
        repo = MagicMock()
        repo.create = AsyncMock(side_effect=RuntimeError("db unavailable"))
        account_repo = MagicMock()
        account_repo.get_by_id = AsyncMock(return_value=MagicMock(user_id="user-1", balance=100, goal_locked_amount=0))
        account_repo.adjust_balance = AsyncMock()
        user_repo = MagicMock()
        user_repo.get_by_id = AsyncMock(return_value=MagicMock())
        budget_service = MagicMock()
        budget_service.get_budget_for = AsyncMock(return_value=None)
        budget_service.apply_expense = AsyncMock()
        goal_service = MagicMock()
        goal_service.apply_contribution = AsyncMock()

        service = TransactionService(repo, account_repo, user_repo, budget_service, goal_service)
        payload = make_transaction_create(user_id="user-1", account_id="acc-1")

        with self.assertRaises(RuntimeError):
            await service.create_transaction(payload)

        repo.create.assert_awaited_once()

    async def test_transaction_service_propagates_goal_service_errors(self):
        repo = MagicMock()
        repo.create = AsyncMock()
        account_repo = MagicMock()
        account_repo.get_by_id = AsyncMock(return_value=MagicMock(user_id="user-1", balance=500, goal_locked_amount=0))
        account_repo.adjust_balance = AsyncMock()
        user_repo = MagicMock()
        user_repo.get_by_id = AsyncMock(return_value=MagicMock())
        budget_service = MagicMock()
        budget_service.get_budget_for = AsyncMock(return_value=None)
        budget_service.apply_expense = AsyncMock()
        goal_service = MagicMock()
        goal_service.apply_contribution = AsyncMock(side_effect=BusinessRuleError("goal failure"))

        service = TransactionService(repo, account_repo, user_repo, budget_service, goal_service)
        payload = make_transaction_create(user_id="user-1", account_id="acc-1", goal_id="goal-1")

        with self.assertRaises(BusinessRuleError):
            await service.create_transaction(payload)

        goal_service.apply_contribution.assert_awaited_once()

    async def test_report_service_handles_file_manager_failure(self):
        repo = MagicMock()
        repo.list = AsyncMock(return_value=[])
        file_manager = MagicMock()
        file_manager.export_transactions.side_effect = RuntimeError("io error")
        service = ReportService(repo, file_manager)

        with self.assertRaises(RuntimeError):
            await service.export_transactions("user-1")

        repo.list.assert_awaited_once()
        file_manager.export_transactions.assert_called_once()
