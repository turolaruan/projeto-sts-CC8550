"""Structural tests ensuring dependency providers wire repositories/services correctly."""

from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from src.controllers import dependencies


class TestDependencyProviders(unittest.TestCase):
    def test_repository_providers_use_database_dependency(self):
        repo_paths = {
            "get_user_repository": "UserRepository",
            "get_account_repository": "AccountRepository",
            "get_transaction_repository": "TransactionRepository",
            "get_budget_repository": "BudgetRepository",
            "get_goal_repository": "GoalRepository",
        }
        for provider_name, repo_attr in repo_paths.items():
            with self.subTest(provider=provider_name):
                fake_db = SimpleNamespace()
                with patch.object(dependencies, "get_database", return_value=fake_db) as mock_get_db, patch.object(
                    dependencies, repo_attr
                ) as mock_repo:
                    instance = getattr(dependencies, provider_name)()
                mock_get_db.assert_called_once()
                mock_repo.assert_called_once_with(fake_db)
                self.assertIs(instance, mock_repo.return_value)

    def test_service_providers_bind_dependencies(self):
        with patch.object(dependencies, "UserService") as mock_user_service:
            fake_repo = object()
            service = dependencies.get_user_service(repo=fake_repo)
            mock_user_service.assert_called_once_with(repository=fake_repo)
            self.assertIs(service, mock_user_service.return_value)

        with patch.object(dependencies, "AccountService") as mock_account_service:
            fake_repo = object()
            fake_user_repo = object()
            service = dependencies.get_account_service(repo=fake_repo, user_repo=fake_user_repo)
            mock_account_service.assert_called_once_with(
                repository=fake_repo,
                user_repository=fake_user_repo,
            )
            self.assertIs(service, mock_account_service.return_value)

        with patch.object(dependencies, "BudgetService") as mock_budget_service:
            fake_repo = object()
            service = dependencies.get_budget_service(repo=fake_repo)
            mock_budget_service.assert_called_once_with(repository=fake_repo)
            self.assertIs(service, mock_budget_service.return_value)

        with patch.object(dependencies, "GoalService") as mock_goal_service:
            fake_repo = object()
            fake_account_repo = object()
            service = dependencies.get_goal_service(repo=fake_repo, account_repo=fake_account_repo)
            mock_goal_service.assert_called_once_with(
                repository=fake_repo,
                account_repository=fake_account_repo,
            )
            self.assertIs(service, mock_goal_service.return_value)

        with patch.object(dependencies, "TransactionService") as mock_transaction_service:
            kwargs = {
                "repo": object(),
                "account_repo": object(),
                "user_repo": object(),
                "budget_service": object(),
                "goal_service": object(),
            }
            service = dependencies.get_transaction_service(**kwargs)
            mock_transaction_service.assert_called_once_with(
                repository=kwargs["repo"],
                account_repository=kwargs["account_repo"],
                user_repository=kwargs["user_repo"],
                budget_service=kwargs["budget_service"],
                goal_service=kwargs["goal_service"],
            )
            self.assertIs(service, mock_transaction_service.return_value)

    def test_report_service_builds_file_manager(self):
        fake_repo = MagicMock()
        with patch.object(dependencies, "FileManager") as mock_file_manager, patch.object(
            dependencies, "ReportService"
        ) as mock_report_service:
            result = dependencies.get_report_service(repo=fake_repo)

        mock_file_manager.assert_called_once()
        mock_report_service.assert_called_once_with(repository=fake_repo, file_manager=mock_file_manager.return_value)
        self.assertIs(result, mock_report_service.return_value)
