"""Structural tests for database helpers and Mongo lifecycle."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from src.config.settings import Settings
from src.database import dependencies
from src.database.mongo import MongoManager
from src.database import setup as db_setup
from tests.structural.helpers import FakeDatabase, FakeMotorClient


@pytest.mark.asyncio
async def test_mongo_manager_connect_close_and_client_property(monkeypatch) -> None:
    """Ensure MongoManager manages the Motor client lifecycle correctly."""

    fake_client = FakeMotorClient()
    monkeypatch.setattr("src.database.mongo.AsyncIOMotorClient", lambda *_, **__: fake_client)

    manager = MongoManager(Settings())

    # Connect should instantiate the client only once.
    await manager.connect()
    assert manager.client is fake_client

    # Accessing .client again should reuse cached instance.
    assert manager.client is fake_client

    await manager.close()
    assert fake_client.closed

    # After closing, accessing .client lazily recreates the client.
    new_client = FakeMotorClient()
    monkeypatch.setattr("src.database.mongo.AsyncIOMotorClient", lambda *_, **__: new_client)
    assert manager.client is new_client


@pytest.mark.asyncio
async def test_get_client_context_manager_closes_client(monkeypatch) -> None:
    fake_client = FakeMotorClient()
    monkeypatch.setattr("src.database.setup.AsyncIOMotorClient", lambda *_, **__: fake_client)
    settings = Settings()

    async with db_setup._get_client(settings) as client:
        assert client is fake_client
    assert fake_client.closed


@pytest.mark.asyncio
async def test_ensure_indexes_creates_expected_entries() -> None:
    database = FakeDatabase()
    await db_setup.ensure_indexes(database)

    assert len(database.collections["users"].index_calls) == 3
    assert len(database.collections["accounts"].index_calls) == 4
    assert len(database.collections["categories"].index_calls) == 4
    assert len(database.collections["transactions"].index_calls) == 5
    assert len(database.collections["budgets"].index_calls) == 1


@pytest.mark.asyncio
async def test_initialize_database_uses_context_manager(monkeypatch) -> None:
    fake_client = FakeMotorClient()
    settings = Settings()

    @asynccontextmanager
    async def fake_context(_settings: Settings):
        assert _settings is settings
        yield fake_client

    called = {}

    async def fake_ensure_indexes(database) -> None:
        called["database"] = database

    monkeypatch.setattr(db_setup, "_get_client", fake_context)
    monkeypatch.setattr(db_setup, "ensure_indexes", fake_ensure_indexes)

    await db_setup.initialize_database(settings)
    assert called["database"] is fake_client[settings.mongodb_db]


def test_setup_main_invokes_initializer(monkeypatch) -> None:
    called = {}

    async def fake_initialize(settings: Settings) -> None:
        called["settings"] = settings

    settings = Settings()
    monkeypatch.setattr(db_setup, "initialize_database", fake_initialize)
    monkeypatch.setattr(db_setup, "get_settings", lambda: settings)

    db_setup.main()
    assert called["settings"] is settings


@pytest.mark.asyncio
async def test_database_dependency_returns_manager_database(monkeypatch) -> None:
    class DummyManager:
        def __init__(self) -> None:
            self.database = object()

    dummy_manager = DummyManager()
    monkeypatch.setattr(dependencies, "mongo_manager", dummy_manager)

    result = await dependencies.get_database()
    assert result is dummy_manager.database
