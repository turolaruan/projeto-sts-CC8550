"""User API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Response, status

from src.models import UserCreate, UserModel, UserUpdate
from src.services import UserService

from .dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreate,
    service: UserService = Depends(get_user_service),
) -> UserModel:
    """Register a new user."""

    return await service.create_user(payload)


@router.get("", response_model=list[UserModel])
async def list_users(service: UserService = Depends(get_user_service)) -> list[UserModel]:
    """Return all users."""

    return await service.list_users()


@router.get("/{user_id}", response_model=UserModel)
async def get_user(user_id: str, service: UserService = Depends(get_user_service)) -> UserModel:
    """Return a user by id."""

    return await service.get_user(user_id)


@router.put("/{user_id}", response_model=UserModel)
async def update_user(
    user_id: str,
    payload: UserUpdate,
    service: UserService = Depends(get_user_service),
) -> UserModel:
    """Update a user."""

    return await service.update_user(user_id, payload)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user(user_id: str, service: UserService = Depends(get_user_service)) -> Response:
    """Delete a user."""

    await service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
