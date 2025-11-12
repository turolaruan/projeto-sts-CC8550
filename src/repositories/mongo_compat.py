"""Compatibility helpers for optional motor/pymongo dependencies."""

from __future__ import annotations

from typing import Any, Optional

try:  # pragma: no cover - exercised indirectly by runtime imports
    from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
    from pymongo import ASCENDING, DESCENDING, ReturnDocument
    from pymongo.errors import DuplicateKeyError

    _IMPORT_ERROR: Optional[Exception] = None
except Exception as exc:  # pragma: no cover - triggered when deps missing
    AsyncIOMotorCollection = AsyncIOMotorDatabase = Any  # type: ignore[misc, assignment]
    ASCENDING = 1  # type: ignore[assignment]
    DESCENDING = -1  # type: ignore[assignment]

    class _FallbackReturnDocument:
        BEFORE = "before"
        AFTER = "after"

    ReturnDocument = _FallbackReturnDocument()  # type: ignore[assignment]

    class DuplicateKeyError(Exception):
        """Placeholder for pymongo.errors.DuplicateKeyError."""

    _IMPORT_ERROR = exc


def ensure_motor_dependencies() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "motor/pymongo are required for MongoDB repositories but could not be imported. "
        "Install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


__all__ = [
    "ASCENDING",
    "DESCENDING",
    "AsyncIOMotorCollection",
    "AsyncIOMotorDatabase",
    "DuplicateKeyError",
    "ReturnDocument",
    "ensure_motor_dependencies",
]
