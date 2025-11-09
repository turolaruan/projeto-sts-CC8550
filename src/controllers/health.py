"""Health check endpoints."""

from fastapi import APIRouter, status

from src.config import get_settings

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="API health check",
)
async def health_check() -> dict[str, object]:
    """Return basic application information."""
    settings = get_settings()
    return {
        "status": "ok",
        "application": settings.app_name,
        "environment": settings.environment,
    }
