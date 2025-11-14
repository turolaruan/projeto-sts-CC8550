"""Tests validating OOP characteristics such as inheritance and encapsulation."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from src.config.settings import Settings
from src.models.enums import CurrencyCode
from src.models.user import User, UserCreate
from src.repositories.base import Repository
from src.services.user_service import UserService


class IncompleteRepository(Repository[User, str]):
    """Repository missing delete implementation to trigger abstract enforcement."""

    async def create(self, entity: User) -> User:  # pragma: no cover - not executed
        return entity

    async def get(self, entity_id: str) -> Optional[User]:
        return None

    async def list(self, **filters: object) -> Iterable[User]:
        return []

    async def update(self, entity_id: str, data: dict[str, object]) -> Optional[User]:
        return None

    # delete intentionally omitted


class InMemoryUserRepository(Repository[User, str]):
    """Concrete repository implementing the abstract interface."""

    def __init__(self) -> None:
        self.storage: dict[str, User] = {}

    async def create(self, entity: User) -> User:
        self.storage[entity.id] = entity
        return entity

    async def get(self, entity_id: str) -> Optional[User]:
        return self.storage.get(entity_id)

    async def list(self, **filters: object) -> Iterable[User]:
        results = list(self.storage.values())
        for key, value in filters.items():
            results = [user for user in results if getattr(user, key) == value]
        return results

    async def update(self, entity_id: str, data: dict[str, object]) -> Optional[User]:
        user = self.storage.get(entity_id)
        if user is None:
            return None
        updated = user.model_copy(update=data)
        self.storage[entity_id] = updated
        return updated

    async def delete(self, entity_id: str) -> bool:
        return self.storage.pop(entity_id, None) is not None


def test_repository_inheritance_requires_all_abstract_methods() -> None:
    """Instantiating incomplete repositories should fail due to abstract contract."""
    with pytest.raises(TypeError):
        IncompleteRepository()


@pytest.mark.asyncio
async def test_user_service_polymorphism_with_custom_repository() -> None:
    """UserService should operate with any Repository implementation."""
    repository = InMemoryUserRepository()
    service = UserService(repository)
    payload = UserCreate(
        name="Usuario OO",
        email="oo@example.com",
        default_currency=CurrencyCode.USD,
    )
    created = await service.create_user(payload)
    fetched = await service.get_user(created.id)
    users = await service.list_users(email="oo@example.com")

    assert isinstance(repository, Repository)
    assert fetched.id == created.id
    assert users and users[0].email == "oo@example.com"


def test_settings_log_config_file_encapsulates_path_resolution(tmp_path, monkeypatch) -> None:
    """Settings should hide path resolution details behind property access."""
    monkeypatch.chdir(tmp_path)
    settings = Settings(LOG_CONFIG_PATH="custom/log.yaml")

    resolved = settings.log_config_file

    assert resolved == tmp_path / "custom" / "log.yaml"
