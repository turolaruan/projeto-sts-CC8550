"""Custom exception hierarchy for the application."""

from __future__ import annotations

from typing import Any


class AppException(Exception):
    """Base application exception carrying optional context."""

    def __init__(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = context or {}


class EntityNotFoundError(AppException):
    """Raised when an entity is not found in the persistence layer."""


class EntityAlreadyExistsError(AppException):
    """Raised when attempting to create an entity that already exists."""


class ValidationAppError(AppException):
    """Raised for custom validation failures in services."""
