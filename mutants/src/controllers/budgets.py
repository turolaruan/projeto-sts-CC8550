"""Budget API endpoints."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from src.models.budget import Budget, BudgetCreate, BudgetUpdate
from src.services.budget_service import BudgetService
from src.services.dependencies import get_budget_service
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)


router = APIRouter(prefix="/budgets", tags=["budgets"])
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


@router.post(
    "/",
    response_model=Budget,
    status_code=status.HTTP_201_CREATED,
    summary="Create budget",
)
async def create_budget(
    payload: BudgetCreate,
    service: BudgetService = Depends(get_budget_service),
) -> Budget:
    """Create budget for category and period."""
    try:
        return await service.create_budget(payload)
    except EntityAlreadyExistsError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.message)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)


@router.get(
    "/",
    response_model=List[Budget],
    summary="List budgets",
)
async def list_budgets(
    user_id: str | None = Query(default=None, min_length=24, max_length=24),
    category_id: str | None = Query(default=None, min_length=24, max_length=24),
    year: int | None = Query(default=None, ge=2000, le=2100),
    month: int | None = Query(default=None, ge=1, le=12),
    service: BudgetService = Depends(get_budget_service),
) -> List[Budget]:
    """Return budgets filtered by optional parameters."""
    return await service.list_budgets(
        user_id=user_id,
        category_id=category_id,
        year=year,
        month=month,
    )


@router.get(
    "/{budget_id}",
    response_model=Budget,
    summary="Get budget by id",
)
async def get_budget(
    budget_id: str,
    service: BudgetService = Depends(get_budget_service),
) -> Budget:
    """Retrieve budget by identifier."""
    try:
        return await service.get_budget(budget_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.patch(
    "/{budget_id}",
    response_model=Budget,
    summary="Update budget",
)
async def update_budget(
    budget_id: str,
    payload: BudgetUpdate,
    service: BudgetService = Depends(get_budget_service),
) -> Budget:
    """Update budget details."""
    try:
        return await service.update_budget(budget_id, payload)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)


@router.delete(
    "/{budget_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete budget",
)
async def delete_budget(
    budget_id: str,
    service: BudgetService = Depends(get_budget_service),
) -> Response:
    """Delete budget if there are no conflicting transactions."""
    try:
        await service.delete_budget(budget_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
