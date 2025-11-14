"""Transaction API endpoints."""

from __future__ import annotations

from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from src.models.enums import TransactionType
from src.models.transaction import Transaction, TransactionCreate, TransactionUpdate
from src.services.dependencies import get_transaction_service
from src.services.transaction_service import TransactionService
from src.utils.exceptions import EntityNotFoundError, ValidationAppError


router = APIRouter(prefix="/transactions", tags=["transactions"])
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
    response_model=Transaction,
    status_code=status.HTTP_201_CREATED,
    summary="Create a transaction",
)
async def create_transaction(
    payload: TransactionCreate,
    service: TransactionService = Depends(get_transaction_service),
) -> Transaction:
    """Create a transaction and update affected balances."""
    try:
        return await service.create_transaction(payload)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)


@router.get(
    "/",
    response_model=List[Transaction],
    summary="List transactions",
)
async def list_transactions(
    user_id: str | None = Query(default=None, min_length=24, max_length=24),
    account_id: str | None = Query(default=None, min_length=24, max_length=24),
    category_id: str | None = Query(default=None, min_length=24, max_length=24),
    transaction_type: TransactionType | None = Query(default=None),
    transfer_account_id: str | None = Query(default=None, min_length=24, max_length=24),
    date_from: datetime | None = Query(default=None),
    date_to: datetime | None = Query(default=None),
    service: TransactionService = Depends(get_transaction_service),
) -> List[Transaction]:
    """Return transactions with optional filtering."""
    return await service.list_transactions(
        user_id=user_id,
        account_id=account_id,
        category_id=category_id,
        transaction_type=transaction_type.value if transaction_type else None,
        transfer_account_id=transfer_account_id,
        date_from=date_from,
        date_to=date_to,
    )


@router.get(
    "/{transaction_id}",
    response_model=Transaction,
    summary="Get transaction by id",
)
async def get_transaction(
    transaction_id: str,
    service: TransactionService = Depends(get_transaction_service),
) -> Transaction:
    """Retrieve a transaction by identifier."""
    try:
        return await service.get_transaction(transaction_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.patch(
    "/{transaction_id}",
    response_model=Transaction,
    summary="Update transaction",
)
async def update_transaction(
    transaction_id: str,
    payload: TransactionUpdate,
    service: TransactionService = Depends(get_transaction_service),
) -> Transaction:
    """Update transaction details."""
    try:
        return await service.update_transaction(transaction_id, payload)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.delete(
    "/{transaction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete transaction",
)
async def delete_transaction(
    transaction_id: str,
    service: TransactionService = Depends(get_transaction_service),
) -> Response:
    """Delete a transaction and revert balance effects."""
    try:
        await service.delete_transaction(transaction_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
