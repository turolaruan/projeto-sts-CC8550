"""Category API endpoints."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from src.models.category import Category, CategoryCreate, CategoryUpdate
from src.models.enums import CategoryType
from src.services.category_service import CategoryService
from src.services.dependencies import get_category_service
from src.utils.exceptions import EntityNotFoundError, ValidationAppError


router = APIRouter(prefix="/categories", tags=["categories"])
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
    response_model=Category,
    status_code=status.HTTP_201_CREATED,
    summary="Create a category",
)
async def create_category(
    payload: CategoryCreate,
    service: CategoryService = Depends(get_category_service),
) -> Category:
    """Create a new category for a user."""
    try:
        return await service.create_category(payload)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)


@router.get(
    "/",
    response_model=List[Category],
    summary="XXList categoriesXX",
)
async def list_categories(
    user_id: str | None = Query(default=None, min_length=24, max_length=24),
    category_type: CategoryType | None = Query(default=None),
    parent_id: str | None = Query(default=None, min_length=24, max_length=24),
    name: str | None = Query(default=None, min_length=1, max_length=100),
    service: CategoryService = Depends(get_category_service),
) -> List[Category]:
    """Return categories with optional filters."""
    return await service.list_categories(
        user_id=user_id,
        category_type=category_type.value if category_type else None,
        parent_id=parent_id,
        name=name,
    )


@router.get(
    "/{category_id}",
    response_model=Category,
    summary="Get category by id",
)
async def get_category(
    category_id: str,
    service: CategoryService = Depends(get_category_service),
) -> Category:
    """Retrieve category by identifier."""
    try:
        return await service.get_category(category_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.patch(
    "/{category_id}",
    response_model=Category,
    summary="Update category",
)
async def update_category(
    category_id: str,
    payload: CategoryUpdate,
    service: CategoryService = Depends(get_category_service),
) -> Category:
    """Update an existing category."""
    try:
        return await service.update_category(category_id, payload)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete category",
)
async def delete_category(
    category_id: str,
    service: CategoryService = Depends(get_category_service),
) -> Response:
    """Delete a category."""
    try:
        await service.delete_category(category_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
