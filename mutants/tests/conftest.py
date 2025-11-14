"""Global pytest fixtures for the project."""

from __future__ import annotations

import os

from pathlib import Path

import pytest
import pytest_asyncio
from httpx import AsyncClient



from src.controllers.dependencies import (
    get_account_service,
    get_budget_service,
    get_goal_service,
    get_report_service,
    get_transaction_service,
    get_user_service,
)
from src.main import create_app
from src.models import TransactionType
from src.services import AccountService, BudgetService, GoalService, ReportService, TransactionService, UserService
from src.utils import FileManager
from tests.fixtures.memory_repositories import (
    MemoryAccountRepository,
    MemoryBudgetRepository,
    MemoryGoalRepository,
    MemoryTransactionRepository,
    MemoryUserRepository,
)




@pytest.fixture()
def user_repository() -> MemoryUserRepository:
    return MemoryUserRepository()


@pytest.fixture()
def account_repository() -> MemoryAccountRepository:
    return MemoryAccountRepository()


@pytest.fixture()
def budget_repository() -> MemoryBudgetRepository:
    return MemoryBudgetRepository()


@pytest.fixture()
def goal_repository() -> MemoryGoalRepository:
    return MemoryGoalRepository()


@pytest.fixture()
def transaction_repository() -> MemoryTransactionRepository:
    return MemoryTransactionRepository()


@pytest.fixture()
def user_service(user_repository: MemoryUserRepository) -> UserService:
    return UserService(repository=user_repository)


@pytest.fixture()
def account_service(
    account_repository: MemoryAccountRepository,
    user_repository: MemoryUserRepository,
) -> AccountService:
    return AccountService(repository=account_repository, user_repository=user_repository)


@pytest.fixture()
def budget_service(budget_repository: MemoryBudgetRepository) -> BudgetService:
    return BudgetService(repository=budget_repository)


@pytest.fixture()
def goal_service(
    goal_repository: MemoryGoalRepository,
    account_repository: MemoryAccountRepository,
) -> GoalService:
    return GoalService(repository=goal_repository, account_repository=account_repository)


@pytest.fixture()
def transaction_service(
    transaction_repository: MemoryTransactionRepository,
    account_repository: MemoryAccountRepository,
    user_repository: MemoryUserRepository,
    budget_service: BudgetService,
    goal_service: GoalService,
) -> TransactionService:
    return TransactionService(
        repository=transaction_repository,
        account_repository=account_repository,
        user_repository=user_repository,
        budget_service=budget_service,
        goal_service=goal_service,
    )


@pytest.fixture()
def report_service(transaction_repository: MemoryTransactionRepository, tmp_path: Path) -> ReportService:
    file_manager = FileManager(base_dir=tmp_path)
    return ReportService(repository=transaction_repository, file_manager=file_manager)


@pytest.fixture()
def api_app(
    user_service: UserService,
    account_service: AccountService,
    budget_service: BudgetService,
    goal_service: GoalService,
    transaction_service: TransactionService,
    report_service: ReportService,
):
    app = create_app()
    app.dependency_overrides[get_user_service] = lambda: user_service
    app.dependency_overrides[get_account_service] = lambda: account_service
    app.dependency_overrides[get_budget_service] = lambda: budget_service
    app.dependency_overrides[get_goal_service] = lambda: goal_service
    app.dependency_overrides[get_transaction_service] = lambda: transaction_service
    app.dependency_overrides[get_report_service] = lambda: report_service
    return app


@pytest_asyncio.fixture()
async def api_client(api_app):
    async with AsyncClient(app=api_app, base_url="http://testserver") as client:
        yield client
