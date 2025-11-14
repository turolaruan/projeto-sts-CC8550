"""FastAPI dependency providers for services and repositories."""

from __future__ import annotations

from fastapi import Depends

from src.repositories import (
    AccountRepository,
    BudgetRepository,
    GoalRepository,
    TransactionRepository,
    UserRepository,
)
from src.services import (
    AccountService,
    BudgetService,
    GoalService,
    ReportService,
    TransactionService,
    UserService,
)
from src.utils import FileManager, get_database


def get_user_repository():
    """Provide a user repository bound to the DB dependency."""

    database = get_database()
    return UserRepository(database)


def get_account_repository():
    """Provide account repository instance."""

    database = get_database()
    return AccountRepository(database)


def get_transaction_repository():
    """Provide transaction repository instance."""

    database = get_database()
    return TransactionRepository(database)


def get_budget_repository():
    """Provide budget repository instance."""

    database = get_database()
    return BudgetRepository(database)


def get_goal_repository():
    """Provide goal repository instance."""

    database = get_database()
    return GoalRepository(database)


def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    """Provide user service."""

    return UserService(repository=repo)


def get_account_service(
    repo: AccountRepository = Depends(get_account_repository),
    user_repo: UserRepository = Depends(get_user_repository),
) -> AccountService:
    """Provide account service."""

    return AccountService(repository=repo, user_repository=user_repo)


def get_budget_service(repo: BudgetRepository = Depends(get_budget_repository)) -> BudgetService:
    """Provide budget service."""

    return BudgetService(repository=repo)


def get_goal_service(
    repo: GoalRepository = Depends(get_goal_repository),
    account_repo: AccountRepository = Depends(get_account_repository),
) -> GoalService:
    """Provide goal service."""

    return GoalService(repository=repo, account_repository=account_repo)


def get_transaction_service(
    repo: TransactionRepository = Depends(get_transaction_repository),
    account_repo: AccountRepository = Depends(get_account_repository),
    user_repo: UserRepository = Depends(get_user_repository),
    budget_service: BudgetService = Depends(get_budget_service),
    goal_service: GoalService = Depends(get_goal_service),
) -> TransactionService:
    """Provide transaction service."""

    return TransactionService(
        repository=repo,
        account_repository=account_repo,
        user_repository=user_repo,
        budget_service=budget_service,
        goal_service=goal_service,
    )


def get_report_service(
    repo: TransactionRepository = Depends(get_transaction_repository),
) -> ReportService:
    """Provide report service."""

    return ReportService(repository=repo, file_manager=FileManager())
