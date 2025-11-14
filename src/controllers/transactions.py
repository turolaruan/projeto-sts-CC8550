"""Transaction API endpoints."""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Response, status

from src.models import (
    TransactionCreate,
    TransactionFilter,
    TransactionModel,
    TransactionUpdate,
)
from src.services import TransactionService

from .dependencies import get_transaction_service

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("", response_model=TransactionModel, status_code=status.HTTP_201_CREATED)
async def create_transaction(
    payload: TransactionCreate,
    service: TransactionService = Depends(get_transaction_service),
) -> TransactionModel:
    """Create a new transaction."""

    return await service.create_transaction(payload)


@router.get("", response_model=list[TransactionModel])
async def list_transactions(
    user_id: str = Query(..., description="Filter by user"),
    service: TransactionService = Depends(get_transaction_service),
) -> list[TransactionModel]:
    """List transactions for a user."""

    return await service.list_transactions(user_id)


@router.get("/search", response_model=List[TransactionModel])
async def search_transactions(
    user_id: str = Query(...),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    category: Optional[str] = Query(None),
    min_amount: Optional[float] = Query(None, ge=0),
    max_amount: Optional[float] = Query(None, ge=0),
    tags: Optional[List[str]] = Query(None),
    sort_by: str = Query("event_date"),
    sort_order: int = Query(-1),
    service: TransactionService = Depends(get_transaction_service),
) -> List[TransactionModel]:
    """Search transactions with filters and ordering."""

    filters = TransactionFilter(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        category=category,
        min_amount=min_amount,
        max_amount=max_amount,
        tags=tags,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    return await service.search_transactions(filters)


@router.get("/{transaction_id}", response_model=TransactionModel)
async def get_transaction(
    transaction_id: str,
    service: TransactionService = Depends(get_transaction_service),
) -> TransactionModel:
    """Return transaction by id."""

    return await service.get_transaction(transaction_id)


@router.put("/{transaction_id}", response_model=TransactionModel)
async def update_transaction(
    transaction_id: str,
    payload: TransactionUpdate,
    service: TransactionService = Depends(get_transaction_service),
) -> TransactionModel:
    """Update transaction."""

    return await service.update_transaction(transaction_id, payload)


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_transaction(
    transaction_id: str,
    service: TransactionService = Depends(get_transaction_service),
) -> Response:
    """Delete transaction."""

    await service.delete_transaction(transaction_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
