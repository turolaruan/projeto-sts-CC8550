"""Application settings loaded from the environment."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Centralized strongly-typed configuration."""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Finance Manager API"
    environment: Literal["local", "test", "production"] = "local"
    api_prefix: str = "/api/v1"
    mongodb_uri: str = "mongodb://mongo:27017"
    mongodb_database: str = "finance_manager"
    log_level: str = "INFO"
    export_dir: str = "reports"
    benchmark_threshold_ms: int = 500
    enable_demo_data: bool = False


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()
