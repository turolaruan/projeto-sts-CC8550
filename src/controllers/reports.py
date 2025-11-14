"""Report related endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from src.models import ReportPayload
from src.services import ReportService

from .dependencies import get_report_service

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/transactions/{user_id}", response_model=ReportPayload)
async def export_transactions(
    user_id: str,
    service: ReportService = Depends(get_report_service),
) -> ReportPayload:
    """Generate a CSV export for transactions."""

    return await service.export_transactions(user_id)
