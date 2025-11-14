"""Goal API endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query, Response, status

from src.models import GoalCreate, GoalModel, GoalUpdate
from src.services import GoalService

from .dependencies import get_goal_service

router = APIRouter(prefix="/goals", tags=["Goals"])


@router.post("", response_model=GoalModel, status_code=status.HTTP_201_CREATED)
async def create_goal(
    payload: GoalCreate,
    service: GoalService = Depends(get_goal_service),
) -> GoalModel:
    """Create goal."""

    return await service.create_goal(payload)


@router.get("", response_model=list[GoalModel])
async def list_goals(
    user_id: str = Query(...),
    service: GoalService = Depends(get_goal_service),
) -> list[GoalModel]:
    """List goals for user."""

    return await service.list_goals(user_id)


@router.get("/{goal_id}", response_model=GoalModel)
async def get_goal(goal_id: str, service: GoalService = Depends(get_goal_service)) -> GoalModel:
    """Get goal by id."""

    return await service.get_goal(goal_id)


@router.put("/{goal_id}", response_model=GoalModel)
async def update_goal(
    goal_id: str,
    payload: GoalUpdate,
    service: GoalService = Depends(get_goal_service),
) -> GoalModel:
    """Update goal."""

    return await service.update_goal(goal_id, payload)


@router.delete("/{goal_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_goal(goal_id: str, service: GoalService = Depends(get_goal_service)) -> Response:
    """Delete goal."""

    await service.delete_goal(goal_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
