"""MongoDB connection helpers."""

from __future__ import annotations

from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from config.settings import get_settings


@lru_cache(maxsize=1)
def _get_client() -> AsyncIOMotorClient:
    """Return a cached Motor client."""

    settings = get_settings()
    return AsyncIOMotorClient(settings.mongodb_uri)


def get_database() -> AsyncIOMotorDatabase:
    """Return the configured Mongo database instance."""

    settings = get_settings()
    client = _get_client()
    return client[settings.mongodb_database]
