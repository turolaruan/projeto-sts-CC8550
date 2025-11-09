"""Logging configuration utilities."""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path
from typing import Any

import yaml

from src.config import Settings


def configure_logging(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def _ensure_log_directories(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
