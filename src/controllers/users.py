"""User API endpoints."""

from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from pydantic import EmailStr

from src.models.enums import CurrencyCode
from src.models.user import User, UserCreate, UserUpdate
from src.services.dependencies import get_user_service
from src.services.user_service import UserService
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
)
async def create_user(
    payload: UserCreate,
    service: UserService = Depends(get_user_service),
) -> User:
    """Create a new user."""
    try:
        return await service.create_user(payload)
    except EntityAlreadyExistsError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.message)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)


@router.get(
    "/",
    response_model=List[User],
    summary="List users",
)
async def list_users(
    name: str | None = Query(default=None, min_length=1, max_length=100),
    email: EmailStr | None = Query(default=None),
    default_currency: CurrencyCode | None = Query(default=None),
    service: UserService = Depends(get_user_service),
) -> List[User]:
    """Return users applying optional filters."""
    return await service.list_users(
        name=name,
        email=str(email) if email else None,
        default_currency=default_currency.value if default_currency else None,
    )


@router.get(
    "/{user_id}",
    response_model=User,
    summary="Get user by id",
)
async def get_user(
    user_id: str,
    service: UserService = Depends(get_user_service),
) -> User:
    """Retrieve a user by identifier."""
    try:
        return await service.get_user(user_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.patch(
    "/{user_id}",
    response_model=User,
    summary="Update user",
)
async def update_user(
    user_id: str,
    payload: UserUpdate,
    service: UserService = Depends(get_user_service),
) -> User:
    """Update fields of an existing user."""
    try:
        return await service.update_user(user_id, payload)
    except ValidationAppError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
)
async def delete_user(
    user_id: str,
    service: UserService = Depends(get_user_service),
) -> Response:
    """Delete a user."""
    try:
        await service.delete_user(user_id)
    except EntityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
