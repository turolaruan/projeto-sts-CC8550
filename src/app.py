"""Application factory for the FastAPI service."""

from fastapi import FastAPI

from src.config import Settings, get_settings
from src.controllers import register_controllers
from src.database.mongo import mongo_manager
from src.utils.logging_config import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app
