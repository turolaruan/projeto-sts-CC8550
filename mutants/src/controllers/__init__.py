"""Routes for the FastAPI application."""

from fastapi import APIRouter

from . import accounts, budgets, goals, reports, transactions, users

router = APIRouter()
router.include_router(users.router)
router.include_router(accounts.router)
router.include_router(transactions.router)
router.include_router(budgets.router)
router.include_router(goals.router)
router.include_router(reports.router)

__all__ = ["router"]
