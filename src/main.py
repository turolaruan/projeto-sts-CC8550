"""FastAPI application entry point."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from config.settings import get_settings
from src.controllers import router as api_router
from src.services.exceptions import BusinessRuleError, NotFoundError, ServiceError, ValidationError
from src.utils import get_logger


def create_app() -> FastAPI:
    """Instantiate the FastAPI application."""

    settings = get_settings()

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        logger = get_logger("startup")
        logger.info("Starting Finance Manager API in {env}", env=settings.environment)
        yield

    app = FastAPI(title=settings.app_name, version="1.0.0", lifespan=lifespan)
    app.include_router(api_router, prefix=settings.api_prefix)
    register_exception_handlers(app)
    return app


def register_exception_handlers(app: FastAPI) -> None:
    """Register service-layer exception handlers."""

    @app.exception_handler(NotFoundError)
    async def _not_found_handler(request: Request, exc: NotFoundError) -> JSONResponse:  # type: ignore[override]
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(BusinessRuleError)
    async def _business_handler(request: Request, exc: BusinessRuleError) -> JSONResponse:  # type: ignore[override]
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(ValidationError)
    async def _validation_handler(request: Request, exc: ValidationError) -> JSONResponse:  # type: ignore[override]
        return JSONResponse(status_code=422, content={"detail": str(exc)})

    @app.exception_handler(ServiceError)
    async def _service_handler(request: Request, exc: ServiceError) -> JSONResponse:  # type: ignore[override]
        return JSONResponse(status_code=500, content={"detail": str(exc)})


app = create_app()
