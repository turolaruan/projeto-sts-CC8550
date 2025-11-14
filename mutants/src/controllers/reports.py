"""Reporting API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status

from src.models.report import MonthlySummary
from src.services.dependencies import get_report_service
from src.services.report_service import ReportService
from src.utils.exceptions import EntityNotFoundError


router = APIRouter(prefix="/reports", tags=["reports"])
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


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
