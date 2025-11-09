"""Router registration for FastAPI application."""

from fastapi import APIRouter, FastAPI

from src.controllers.accounts import router as accounts_router
from src.controllers.budgets import router as budgets_router
from src.controllers.categories import router as categories_router
from src.controllers.health import router as health_router
from src.controllers.reports import router as reports_router
from src.controllers.transactions import router as transactions_router
from src.controllers.users import router as users_router


def register_controllers(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)
