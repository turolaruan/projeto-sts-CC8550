"""Budget API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query, Response, status

from src.models import BudgetCreate, BudgetModel, BudgetSummary, BudgetUpdate
from src.services import BudgetService

from .dependencies import get_budget_service

router = APIRouter(prefix="/budgets", tags=["Budgets"])


@router.post("", response_model=BudgetModel, status_code=status.HTTP_201_CREATED)
async def create_budget(
    payload: BudgetCreate,
    service: BudgetService = Depends(get_budget_service),
) -> BudgetModel:
    """Create new budget."""

    return await service.create_budget(payload)


@router.get("", response_model=list[BudgetModel])
async def list_budgets(
    user_id: str = Query(...),
    service: BudgetService = Depends(get_budget_service),
) -> list[BudgetModel]:
    """List budgets for user."""

    return await service.list_budgets(user_id)


@router.get("/{budget_id}", response_model=BudgetModel)
async def get_budget(budget_id: str, service: BudgetService = Depends(get_budget_service)) -> BudgetModel:
    """Get budget by id."""

    return await service.get_budget(budget_id)


@router.put("/{budget_id}", response_model=BudgetModel)
async def update_budget(
    budget_id: str,
    payload: BudgetUpdate,
    service: BudgetService = Depends(get_budget_service),
) -> BudgetModel:
    """Update budget."""

    return await service.update_budget(budget_id, payload)


@router.delete("/{budget_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_budget(
    budget_id: str,
    service: BudgetService = Depends(get_budget_service),
) -> Response:
    """Delete budget."""

    await service.delete_budget(budget_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/summary/{user_id}", response_model=list[BudgetSummary])
async def summarize_budgets(
    user_id: str,
    service: BudgetService = Depends(get_budget_service),
) -> list[BudgetSummary]:
    """Return aggregated summary for budgets."""

    return await service.summarize(user_id)
