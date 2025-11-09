"""Reporting API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from src.models.report import MonthlySummary
from src.services.dependencies import get_report_service
from src.services.report_service import ReportService
from src.utils.exceptions import EntityNotFoundError


router = APIRouter(prefix="/reports", tags=["reports"])


@router.get(
    "/monthly-summary",
    response_model=MonthlySummary,
    summary="Monthly summary report",
)
async def get_monthly_summary(
    user_id: str = Query(min_length=24, max_length=24),
    year: int = Query(ge=2000, le=2100),
    month: int = Query(ge=1, le=12),
    service: ReportService = Depends(get_report_service),
) -> MonthlySummary:
    """Return aggregated totals by category and transaction type for the month."""
    try:
        return await service.monthly_summary(user_id, year, month)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
