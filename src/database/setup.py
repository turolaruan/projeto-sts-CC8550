"""MongoDB initialization utilities and CLI."""

from __future__ import annotations

import asyncio
import logging
from contextlib import asynccontextmanager

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo import ASCENDING, DESCENDING

from src.config import Settings, get_settings


logger = logging.getLogger(__name__)


async def ensure_indexes(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index([("user_id", ASCENDING)])
    await accounts.create_index([("account_type", ASCENDING)])
    await accounts.create_index([("currency", ASCENDING)])
    await accounts.create_index([("name", ASCENDING)])

    logger.info("Creating indexes for collection 'categories'")
    categories = database.get_collection("categories")
    await categories.create_index([("user_id", ASCENDING)])
    await categories.create_index([("category_type", ASCENDING)])
    await categories.create_index([("parent_id", ASCENDING)])
    await categories.create_index([("name", ASCENDING)])

    logger.info("Creating indexes for collection 'transactions'")
    transactions = database.get_collection("transactions")
    await transactions.create_index([("user_id", ASCENDING)])
    await transactions.create_index([("account_id", ASCENDING)])
    await transactions.create_index([("category_id", ASCENDING)])
    await transactions.create_index([("transfer_account_id", ASCENDING)])
    await transactions.create_index([("occurred_at", DESCENDING)])

    logger.info("Creating indexes for collection 'budgets'")
    budgets = database.get_collection("budgets")
    await budgets.create_index(
        [
            ("user_id", ASCENDING),
            ("category_id", ASCENDING),
            ("year", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


@asynccontextmanager
async def _get_client(settings: Settings) -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(settings.mongodb_uri, uuidRepresentation="standard")
    try:
        yield client
    finally:
        client.close()


async def initialize_database(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = settings or get_settings()
    async with _get_client(app_settings) as client:
        database = client[app_settings.mongodb_db]
        await ensure_indexes(database)


def main() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


if __name__ == "__main__":
    main()
