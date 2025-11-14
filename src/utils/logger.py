"""Logging helpers built on top of loguru."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from loguru import logger

from config.settings import get_settings

_CONFIGURED = False


def _configure_logger() -> None:
    """Configure loguru sinks only once."""

    global _CONFIGURED
    if _CONFIGURED:
        return
    settings = get_settings()
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.remove()
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level=settings.log_level,
        backtrace=False,
        diagnose=False,
    )
    logger.add(
        log_dir / "app.log",
        rotation="10 MB",
        retention="10 days",
        level=settings.log_level,
        serialize=False,
    )
    _CONFIGURED = True


def get_logger(name: Optional[str] = None):
    """Return a configured logger bound to the provided name."""

    _configure_logger()
    return logger if name is None else logger.bind(component=name)
