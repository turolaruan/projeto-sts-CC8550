"""Structural tests verifying FastAPI dependency factories."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from src.repositories.account_repository import AccountRepository
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.services import dependencies as deps
from src.services.account_service import AccountService
from src.services.budget_service import BudgetService
from src.services.category_service import CategoryService
from src.services.report_service import ReportService
from src.services.transaction_service import TransactionService
from src.services.user_service import UserService
from tests.structural.helpers import FakeDatabase


def test_repository_dependencies_return_instances() -> None:
    db = FakeDatabase()
    assert isinstance(deps.get_user_repository(db=db), UserRepository)
    assert isinstance(deps.get_account_repository(db=db), AccountRepository)
    assert isinstance(deps.get_category_repository(db=db), CategoryRepository)
    assert isinstance(deps.get_budget_repository(db=db), BudgetRepository)
    assert isinstance(deps.get_transaction_repository(db=db), TransactionRepository)


def test_service_dependencies_wire_nested_components() -> None:
    user_repo = SimpleNamespace()
    account_repo = SimpleNamespace()
    transaction_repo = SimpleNamespace()
    category_repo = SimpleNamespace()
    budget_repo = SimpleNamespace()

    account_service = deps.get_account_service(
        repository=account_repo,
        user_repository=user_repo,
        transaction_repository=transaction_repo,
    )
    assert isinstance(account_service, AccountService)

    category_service = deps.get_category_service(
        repository=category_repo,
        user_repository=user_repo,
        transaction_repository=transaction_repo,
        budget_repository=budget_repo,
    )
    assert isinstance(category_service, CategoryService)

    budget_service = deps.get_budget_service(
        repository=budget_repo,
        user_repository=user_repo,
        category_repository=category_repo,
        transaction_repository=transaction_repo,
    )
    assert isinstance(budget_service, BudgetService)

    transaction_service = deps.get_transaction_service(
        repository=transaction_repo,
        account_service=account_service,
        account_repository=account_repo,
        category_repository=category_repo,
        user_repository=user_repo,
        budget_repository=budget_repo,
    )
    assert isinstance(transaction_service, TransactionService)

    report_service = deps.get_report_service(
        transaction_repository=transaction_repo,
        category_repository=category_repo,
        budget_repository=budget_repo,
    )
    assert isinstance(report_service, ReportService)


def test_user_service_dependency_returns_valid_instance() -> None:
    repo = SimpleNamespace()
    service = deps.get_user_service(repository=repo)
    assert isinstance(service, UserService)
