"""Account API endpoints."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from src.models.account import Account, AccountCreate, AccountUpdate
from src.models.enums import AccountType, CurrencyCode
from src.services.account_service import AccountService
from src.services.dependencies import get_account_service
from src.utils.exceptions import EntityNotFoundError, ValidationAppError


router = APIRouter(prefix="/accounts", tags=["accounts"])
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
    response_model=Account,
    status_code=status.HTTP_201_CREATED,
    summary="Create an account",
)
async def create_account(
    payload: AccountCreate,
    service: AccountService = Depends(get_account_service),
) -> Account:
    """Create a new account for a user."""
    try:
        return await service.create_account(payload)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)


@router.get(
    "/",
    response_model=List[Account],
    summary="List accounts",
)
async def list_accounts(
    user_id: str | None = Query(default=None, min_length=24, max_length=24),
    account_type: AccountType | None = Query(default=None),
    currency: CurrencyCode | None = Query(default=None),
    name: str | None = Query(default=None, min_length=1, max_length=120),
    service: AccountService = Depends(get_account_service),
) -> List[Account]:
    """Return accounts with optional filtering."""
    return await service.list_accounts(
        user_id=user_id,
        account_type=account_type.value if account_type else None,
        currency=currency.value if currency else None,
        name=name,
    )


@router.get(
    "/{account_id}",
    response_model=Account,
    summary="Get account by id",
)
async def get_account(
    account_id: str,
    service: AccountService = Depends(get_account_service),
) -> Account:
    """Retrieve account by identifier."""
    try:
        return await service.get_account(account_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.patch(
    "/{account_id}",
    response_model=Account,
    summary="Update account",
)
async def update_account(
    account_id: str,
    payload: AccountUpdate,
    service: AccountService = Depends(get_account_service),
) -> Account:
    """Update an existing account."""
    try:
        return await service.update_account(account_id, payload)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.delete(
    "/{account_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete account",
)
async def delete_account(
    account_id: str,
    service: AccountService = Depends(get_account_service),
) -> Response:
    """Delete an account."""
    try:
        await service.delete_account(account_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
