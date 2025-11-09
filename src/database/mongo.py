"""MongoDB connection management using Motor."""

from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import Settings, get_settings


class MongoManager:
    """Manage lifecycle of the MongoDB client."""

    def __init__(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()
        self._client: AsyncIOMotorClient | None = None

    async def connect(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="standard",
            )

    async def close(self) -> None:
        """Gracefully close MongoDB connection."""
        if self._client is not None:
            self._client.close()
            self._client = None

    @property
    def client(self) -> AsyncIOMotorClient:
        """Return the underlying Motor client, connecting if needed."""
        if self._client is None:
            # Ensure connection is established synchronously when needed.
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="standard",
            )
        return self._client

    @property
    def database(self) -> AsyncIOMotorDatabase:
        """Return the configured database instance."""
        return self.client[self._settings.mongodb_db]


mongo_manager = MongoManager()
