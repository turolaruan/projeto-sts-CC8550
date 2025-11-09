"""Application settings definitions."""

from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Holds configuration loaded from environment variables and files."""

    app_name: str = Field(
        default="Personal Finance Manager API",
        validation_alias="APP_NAME",
    )
    environment: str = Field(default="development", validation_alias="ENVIRONMENT")
    debug: bool = Field(default=True, validation_alias="DEBUG")
    mongodb_uri: str = Field(
        default="mongodb://localhost:27017",
        validation_alias="MONGODB_URI",
    )
    mongodb_db: str = Field(
        default="personal_finance_db",
        validation_alias="MONGODB_DB",
    )
    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")
    log_config_path: str = Field(
        default="config/logging.yaml",
        validation_alias="LOG_CONFIG_PATH",
    )

    model_config = SettingsConfigDict(
        env_file=(".env",),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def is_production(self) -> bool:
        """Return True when running in production environment."""
        return self.environment.lower() == "production"

    @property
    def log_config_file(self) -> Path:
        """Return resolved path to logging configuration file."""
        path = Path(self.log_config_path)
        return path if path.is_absolute() else Path.cwd() / path

    def model_dump_public(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "mongodb_db": self.mongodb_db,
        }


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings instance."""
    return Settings()
