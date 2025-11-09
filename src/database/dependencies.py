"""Database dependency providers for FastAPI."""

from motor.motor_asyncio import AsyncIOMotorDatabase

from src.database.mongo import mongo_manager


async def get_database() -> AsyncIOMotorDatabase:
    """FastAPI dependency to access the MongoDB database."""
    return mongo_manager.database
