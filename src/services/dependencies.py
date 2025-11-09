"""Service dependencies for FastAPI routes."""

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.database.dependencies import get_database
from src.repositories.account_repository import AccountRepository
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.services.account_service import AccountService
from src.services.budget_service import BudgetService
from src.services.category_service import CategoryService
from src.services.report_service import ReportService
from src.services.transaction_service import TransactionService
from src.services.user_service import UserService


def get_user_repository(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> UserRepository:
    """FastAPI dependency returning the user repository instance."""
    return UserRepository(db)


def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    """FastAPI dependency returning the user service."""
    return UserService(repository)


def get_account_repository(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> AccountRepository:
    """Return account repository."""
    return AccountRepository(db)


def get_transaction_repository(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> TransactionRepository:
    """Return transaction repository."""
    return TransactionRepository(db)


def get_account_service(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(repository, user_repository, transaction_repository)


def get_category_repository(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> CategoryRepository:
    """Return category repository."""
    return CategoryRepository(db)


def get_budget_repository(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> BudgetRepository:
    """Return budget repository."""
    return BudgetRepository(db)


def get_category_service(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        user_repository,
        transaction_repository,
        budget_repository,
    )


def get_budget_service(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        user_repository,
        category_repository,
        transaction_repository,
    )


def get_transaction_service(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )


def get_report_service(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(transaction_repository, category_repository, budget_repository)
