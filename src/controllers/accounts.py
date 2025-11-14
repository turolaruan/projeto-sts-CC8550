"""Account API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query, Response, status

from src.models import AccountCreate, AccountModel, AccountUpdate
from src.services import AccountService

from .dependencies import get_account_service

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("", response_model=AccountModel, status_code=status.HTTP_201_CREATED)
async def create_account(
    payload: AccountCreate,
    service: AccountService = Depends(get_account_service),
) -> AccountModel:
    """Create a new account."""

    return await service.create_account(payload)


@router.get("", response_model=list[AccountModel])
async def list_accounts(
    user_id: str = Query(..., description="Filter accounts by owner"),
    service: AccountService = Depends(get_account_service),
) -> list[AccountModel]:
    """List accounts for a given user."""

    return await service.list_accounts(user_id)


@router.get("/{account_id}", response_model=AccountModel)
async def get_account(
    account_id: str,
    service: AccountService = Depends(get_account_service),
) -> AccountModel:
    """Return account details."""

    return await service.get_account(account_id)


@router.put("/{account_id}", response_model=AccountModel)
async def update_account(
    account_id: str,
    payload: AccountUpdate,
    service: AccountService = Depends(get_account_service),
) -> AccountModel:
    """Update account."""

    return await service.update_account(account_id, payload)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_account(account_id: str, service: AccountService = Depends(get_account_service)) -> Response:
    """Delete account."""

    await service.delete_account(account_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
