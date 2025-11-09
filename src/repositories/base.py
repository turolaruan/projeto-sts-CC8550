"""Repository base interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")


class Repository(Generic[T, ID], ABC):
    """Abstract base class for repositories."""

    @abstractmethod
    async def create(self, entity: T) -> T:
        """Persist a new entity."""

    @abstractmethod
    async def get(self, entity_id: ID) -> Optional[T]:
        """Retrieve entity by identifier."""

    @abstractmethod
    async def list(self, **filters: object) -> Iterable[T]:
        """Return iterable of entities matching filters."""

    @abstractmethod
    async def update(self, entity_id: ID, data: dict[str, object]) -> Optional[T]:
        """Update existing entity with provided data."""

    @abstractmethod
    async def delete(self, entity_id: ID) -> bool:
        """Delete entity by identifier and return success flag."""
