"""MongoDB initialization utilities and CLI."""

from __future__ import annotations

import asyncio
import logging
from contextlib import asynccontextmanager

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo import ASCENDING, DESCENDING

from src.config import Settings, get_settings


logger = logging.getLogger(__name__)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


async def x_ensure_indexes__mutmut_orig(database: AsyncIOMotorDatabase) -> None:
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


async def x_ensure_indexes__mutmut_1(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info(None)
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


async def x_ensure_indexes__mutmut_2(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("XXCreating indexes for collection 'users'XX")
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


async def x_ensure_indexes__mutmut_3(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("creating indexes for collection 'users'")
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


async def x_ensure_indexes__mutmut_4(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("CREATING INDEXES FOR COLLECTION 'USERS'")
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


async def x_ensure_indexes__mutmut_5(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = None
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


async def x_ensure_indexes__mutmut_6(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection(None)
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


async def x_ensure_indexes__mutmut_7(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("XXusersXX")
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


async def x_ensure_indexes__mutmut_8(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("USERS")
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


async def x_ensure_indexes__mutmut_9(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index(None, unique=True)
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


async def x_ensure_indexes__mutmut_10(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=None)
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


async def x_ensure_indexes__mutmut_11(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index(unique=True)
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


async def x_ensure_indexes__mutmut_12(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", )
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


async def x_ensure_indexes__mutmut_13(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("XXemailXX", unique=True)
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


async def x_ensure_indexes__mutmut_14(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("EMAIL", unique=True)
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


async def x_ensure_indexes__mutmut_15(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=False)
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


async def x_ensure_indexes__mutmut_16(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index(None)
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


async def x_ensure_indexes__mutmut_17(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("XXnameXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_18(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("NAME", ASCENDING)])
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


async def x_ensure_indexes__mutmut_19(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index(None)

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


async def x_ensure_indexes__mutmut_20(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("XXcreated_atXX", ASCENDING)])

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


async def x_ensure_indexes__mutmut_21(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("CREATED_AT", ASCENDING)])

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


async def x_ensure_indexes__mutmut_22(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info(None)
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


async def x_ensure_indexes__mutmut_23(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("XXCreating indexes for collection 'accounts'XX")
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


async def x_ensure_indexes__mutmut_24(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("creating indexes for collection 'accounts'")
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


async def x_ensure_indexes__mutmut_25(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("CREATING INDEXES FOR COLLECTION 'ACCOUNTS'")
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


async def x_ensure_indexes__mutmut_26(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = None
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


async def x_ensure_indexes__mutmut_27(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection(None)
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


async def x_ensure_indexes__mutmut_28(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("XXaccountsXX")
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


async def x_ensure_indexes__mutmut_29(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("ACCOUNTS")
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


async def x_ensure_indexes__mutmut_30(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index(None)
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


async def x_ensure_indexes__mutmut_31(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index([("XXuser_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_32(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index([("USER_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_33(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index([("user_id", ASCENDING)])
    await accounts.create_index(None)
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


async def x_ensure_indexes__mutmut_34(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index([("user_id", ASCENDING)])
    await accounts.create_index([("XXaccount_typeXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_35(database: AsyncIOMotorDatabase) -> None:
    """Create collections and indexes required by the application."""

    logger.info("Creating indexes for collection 'users'")
    users = database.get_collection("users")
    await users.create_index("email", unique=True)
    await users.create_index([("name", ASCENDING)])
    await users.create_index([("created_at", ASCENDING)])

    logger.info("Creating indexes for collection 'accounts'")
    accounts = database.get_collection("accounts")
    await accounts.create_index([("user_id", ASCENDING)])
    await accounts.create_index([("ACCOUNT_TYPE", ASCENDING)])
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


async def x_ensure_indexes__mutmut_36(database: AsyncIOMotorDatabase) -> None:
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
    await accounts.create_index(None)
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


async def x_ensure_indexes__mutmut_37(database: AsyncIOMotorDatabase) -> None:
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
    await accounts.create_index([("XXcurrencyXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_38(database: AsyncIOMotorDatabase) -> None:
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
    await accounts.create_index([("CURRENCY", ASCENDING)])
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


async def x_ensure_indexes__mutmut_39(database: AsyncIOMotorDatabase) -> None:
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
    await accounts.create_index(None)

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


async def x_ensure_indexes__mutmut_40(database: AsyncIOMotorDatabase) -> None:
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
    await accounts.create_index([("XXnameXX", ASCENDING)])

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


async def x_ensure_indexes__mutmut_41(database: AsyncIOMotorDatabase) -> None:
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
    await accounts.create_index([("NAME", ASCENDING)])

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


async def x_ensure_indexes__mutmut_42(database: AsyncIOMotorDatabase) -> None:
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

    logger.info(None)
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


async def x_ensure_indexes__mutmut_43(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("XXCreating indexes for collection 'categories'XX")
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


async def x_ensure_indexes__mutmut_44(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("creating indexes for collection 'categories'")
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


async def x_ensure_indexes__mutmut_45(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("CREATING INDEXES FOR COLLECTION 'CATEGORIES'")
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


async def x_ensure_indexes__mutmut_46(database: AsyncIOMotorDatabase) -> None:
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
    categories = None
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


async def x_ensure_indexes__mutmut_47(database: AsyncIOMotorDatabase) -> None:
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
    categories = database.get_collection(None)
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


async def x_ensure_indexes__mutmut_48(database: AsyncIOMotorDatabase) -> None:
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
    categories = database.get_collection("XXcategoriesXX")
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


async def x_ensure_indexes__mutmut_49(database: AsyncIOMotorDatabase) -> None:
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
    categories = database.get_collection("CATEGORIES")
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


async def x_ensure_indexes__mutmut_50(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index(None)
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


async def x_ensure_indexes__mutmut_51(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("XXuser_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_52(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("USER_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_53(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index(None)
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


async def x_ensure_indexes__mutmut_54(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("XXcategory_typeXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_55(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("CATEGORY_TYPE", ASCENDING)])
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


async def x_ensure_indexes__mutmut_56(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index(None)
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


async def x_ensure_indexes__mutmut_57(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("XXparent_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_58(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("PARENT_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_59(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index(None)

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


async def x_ensure_indexes__mutmut_60(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("XXnameXX", ASCENDING)])

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


async def x_ensure_indexes__mutmut_61(database: AsyncIOMotorDatabase) -> None:
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
    await categories.create_index([("NAME", ASCENDING)])

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


async def x_ensure_indexes__mutmut_62(database: AsyncIOMotorDatabase) -> None:
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

    logger.info(None)
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


async def x_ensure_indexes__mutmut_63(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("XXCreating indexes for collection 'transactions'XX")
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


async def x_ensure_indexes__mutmut_64(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("creating indexes for collection 'transactions'")
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


async def x_ensure_indexes__mutmut_65(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("CREATING INDEXES FOR COLLECTION 'TRANSACTIONS'")
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


async def x_ensure_indexes__mutmut_66(database: AsyncIOMotorDatabase) -> None:
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
    transactions = None
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


async def x_ensure_indexes__mutmut_67(database: AsyncIOMotorDatabase) -> None:
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
    transactions = database.get_collection(None)
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


async def x_ensure_indexes__mutmut_68(database: AsyncIOMotorDatabase) -> None:
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
    transactions = database.get_collection("XXtransactionsXX")
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


async def x_ensure_indexes__mutmut_69(database: AsyncIOMotorDatabase) -> None:
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
    transactions = database.get_collection("TRANSACTIONS")
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


async def x_ensure_indexes__mutmut_70(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index(None)
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


async def x_ensure_indexes__mutmut_71(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("XXuser_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_72(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("USER_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_73(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index(None)
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


async def x_ensure_indexes__mutmut_74(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("XXaccount_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_75(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("ACCOUNT_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_76(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index(None)
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


async def x_ensure_indexes__mutmut_77(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("XXcategory_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_78(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("CATEGORY_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_79(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index(None)
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


async def x_ensure_indexes__mutmut_80(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("XXtransfer_account_idXX", ASCENDING)])
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


async def x_ensure_indexes__mutmut_81(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("TRANSFER_ACCOUNT_ID", ASCENDING)])
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


async def x_ensure_indexes__mutmut_82(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index(None)

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


async def x_ensure_indexes__mutmut_83(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("XXoccurred_atXX", DESCENDING)])

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


async def x_ensure_indexes__mutmut_84(database: AsyncIOMotorDatabase) -> None:
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
    await transactions.create_index([("OCCURRED_AT", DESCENDING)])

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


async def x_ensure_indexes__mutmut_85(database: AsyncIOMotorDatabase) -> None:
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

    logger.info(None)
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


async def x_ensure_indexes__mutmut_86(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("XXCreating indexes for collection 'budgets'XX")
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


async def x_ensure_indexes__mutmut_87(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("creating indexes for collection 'budgets'")
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


async def x_ensure_indexes__mutmut_88(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("CREATING INDEXES FOR COLLECTION 'BUDGETS'")
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


async def x_ensure_indexes__mutmut_89(database: AsyncIOMotorDatabase) -> None:
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
    budgets = None
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


async def x_ensure_indexes__mutmut_90(database: AsyncIOMotorDatabase) -> None:
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
    budgets = database.get_collection(None)
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


async def x_ensure_indexes__mutmut_91(database: AsyncIOMotorDatabase) -> None:
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
    budgets = database.get_collection("XXbudgetsXX")
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


async def x_ensure_indexes__mutmut_92(database: AsyncIOMotorDatabase) -> None:
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
    budgets = database.get_collection("BUDGETS")
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


async def x_ensure_indexes__mutmut_93(database: AsyncIOMotorDatabase) -> None:
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
        None,
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_94(database: AsyncIOMotorDatabase) -> None:
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
        unique=None,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_95(database: AsyncIOMotorDatabase) -> None:
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
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_96(database: AsyncIOMotorDatabase) -> None:
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
        )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_97(database: AsyncIOMotorDatabase) -> None:
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
            ("XXuser_idXX", ASCENDING),
            ("category_id", ASCENDING),
            ("year", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_98(database: AsyncIOMotorDatabase) -> None:
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
            ("USER_ID", ASCENDING),
            ("category_id", ASCENDING),
            ("year", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_99(database: AsyncIOMotorDatabase) -> None:
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
            ("XXcategory_idXX", ASCENDING),
            ("year", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_100(database: AsyncIOMotorDatabase) -> None:
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
            ("CATEGORY_ID", ASCENDING),
            ("year", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_101(database: AsyncIOMotorDatabase) -> None:
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
            ("XXyearXX", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_102(database: AsyncIOMotorDatabase) -> None:
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
            ("YEAR", ASCENDING),
            ("month", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_103(database: AsyncIOMotorDatabase) -> None:
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
            ("XXmonthXX", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_104(database: AsyncIOMotorDatabase) -> None:
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
            ("MONTH", ASCENDING),
        ],
        unique=True,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_105(database: AsyncIOMotorDatabase) -> None:
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
        unique=False,
    )

    logger.info("MongoDB indexes ensured successfully")


async def x_ensure_indexes__mutmut_106(database: AsyncIOMotorDatabase) -> None:
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

    logger.info(None)


async def x_ensure_indexes__mutmut_107(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("XXMongoDB indexes ensured successfullyXX")


async def x_ensure_indexes__mutmut_108(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("mongodb indexes ensured successfully")


async def x_ensure_indexes__mutmut_109(database: AsyncIOMotorDatabase) -> None:
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

    logger.info("MONGODB INDEXES ENSURED SUCCESSFULLY")

x_ensure_indexes__mutmut_mutants : ClassVar[MutantDict] = {
'x_ensure_indexes__mutmut_1': x_ensure_indexes__mutmut_1, 
    'x_ensure_indexes__mutmut_2': x_ensure_indexes__mutmut_2, 
    'x_ensure_indexes__mutmut_3': x_ensure_indexes__mutmut_3, 
    'x_ensure_indexes__mutmut_4': x_ensure_indexes__mutmut_4, 
    'x_ensure_indexes__mutmut_5': x_ensure_indexes__mutmut_5, 
    'x_ensure_indexes__mutmut_6': x_ensure_indexes__mutmut_6, 
    'x_ensure_indexes__mutmut_7': x_ensure_indexes__mutmut_7, 
    'x_ensure_indexes__mutmut_8': x_ensure_indexes__mutmut_8, 
    'x_ensure_indexes__mutmut_9': x_ensure_indexes__mutmut_9, 
    'x_ensure_indexes__mutmut_10': x_ensure_indexes__mutmut_10, 
    'x_ensure_indexes__mutmut_11': x_ensure_indexes__mutmut_11, 
    'x_ensure_indexes__mutmut_12': x_ensure_indexes__mutmut_12, 
    'x_ensure_indexes__mutmut_13': x_ensure_indexes__mutmut_13, 
    'x_ensure_indexes__mutmut_14': x_ensure_indexes__mutmut_14, 
    'x_ensure_indexes__mutmut_15': x_ensure_indexes__mutmut_15, 
    'x_ensure_indexes__mutmut_16': x_ensure_indexes__mutmut_16, 
    'x_ensure_indexes__mutmut_17': x_ensure_indexes__mutmut_17, 
    'x_ensure_indexes__mutmut_18': x_ensure_indexes__mutmut_18, 
    'x_ensure_indexes__mutmut_19': x_ensure_indexes__mutmut_19, 
    'x_ensure_indexes__mutmut_20': x_ensure_indexes__mutmut_20, 
    'x_ensure_indexes__mutmut_21': x_ensure_indexes__mutmut_21, 
    'x_ensure_indexes__mutmut_22': x_ensure_indexes__mutmut_22, 
    'x_ensure_indexes__mutmut_23': x_ensure_indexes__mutmut_23, 
    'x_ensure_indexes__mutmut_24': x_ensure_indexes__mutmut_24, 
    'x_ensure_indexes__mutmut_25': x_ensure_indexes__mutmut_25, 
    'x_ensure_indexes__mutmut_26': x_ensure_indexes__mutmut_26, 
    'x_ensure_indexes__mutmut_27': x_ensure_indexes__mutmut_27, 
    'x_ensure_indexes__mutmut_28': x_ensure_indexes__mutmut_28, 
    'x_ensure_indexes__mutmut_29': x_ensure_indexes__mutmut_29, 
    'x_ensure_indexes__mutmut_30': x_ensure_indexes__mutmut_30, 
    'x_ensure_indexes__mutmut_31': x_ensure_indexes__mutmut_31, 
    'x_ensure_indexes__mutmut_32': x_ensure_indexes__mutmut_32, 
    'x_ensure_indexes__mutmut_33': x_ensure_indexes__mutmut_33, 
    'x_ensure_indexes__mutmut_34': x_ensure_indexes__mutmut_34, 
    'x_ensure_indexes__mutmut_35': x_ensure_indexes__mutmut_35, 
    'x_ensure_indexes__mutmut_36': x_ensure_indexes__mutmut_36, 
    'x_ensure_indexes__mutmut_37': x_ensure_indexes__mutmut_37, 
    'x_ensure_indexes__mutmut_38': x_ensure_indexes__mutmut_38, 
    'x_ensure_indexes__mutmut_39': x_ensure_indexes__mutmut_39, 
    'x_ensure_indexes__mutmut_40': x_ensure_indexes__mutmut_40, 
    'x_ensure_indexes__mutmut_41': x_ensure_indexes__mutmut_41, 
    'x_ensure_indexes__mutmut_42': x_ensure_indexes__mutmut_42, 
    'x_ensure_indexes__mutmut_43': x_ensure_indexes__mutmut_43, 
    'x_ensure_indexes__mutmut_44': x_ensure_indexes__mutmut_44, 
    'x_ensure_indexes__mutmut_45': x_ensure_indexes__mutmut_45, 
    'x_ensure_indexes__mutmut_46': x_ensure_indexes__mutmut_46, 
    'x_ensure_indexes__mutmut_47': x_ensure_indexes__mutmut_47, 
    'x_ensure_indexes__mutmut_48': x_ensure_indexes__mutmut_48, 
    'x_ensure_indexes__mutmut_49': x_ensure_indexes__mutmut_49, 
    'x_ensure_indexes__mutmut_50': x_ensure_indexes__mutmut_50, 
    'x_ensure_indexes__mutmut_51': x_ensure_indexes__mutmut_51, 
    'x_ensure_indexes__mutmut_52': x_ensure_indexes__mutmut_52, 
    'x_ensure_indexes__mutmut_53': x_ensure_indexes__mutmut_53, 
    'x_ensure_indexes__mutmut_54': x_ensure_indexes__mutmut_54, 
    'x_ensure_indexes__mutmut_55': x_ensure_indexes__mutmut_55, 
    'x_ensure_indexes__mutmut_56': x_ensure_indexes__mutmut_56, 
    'x_ensure_indexes__mutmut_57': x_ensure_indexes__mutmut_57, 
    'x_ensure_indexes__mutmut_58': x_ensure_indexes__mutmut_58, 
    'x_ensure_indexes__mutmut_59': x_ensure_indexes__mutmut_59, 
    'x_ensure_indexes__mutmut_60': x_ensure_indexes__mutmut_60, 
    'x_ensure_indexes__mutmut_61': x_ensure_indexes__mutmut_61, 
    'x_ensure_indexes__mutmut_62': x_ensure_indexes__mutmut_62, 
    'x_ensure_indexes__mutmut_63': x_ensure_indexes__mutmut_63, 
    'x_ensure_indexes__mutmut_64': x_ensure_indexes__mutmut_64, 
    'x_ensure_indexes__mutmut_65': x_ensure_indexes__mutmut_65, 
    'x_ensure_indexes__mutmut_66': x_ensure_indexes__mutmut_66, 
    'x_ensure_indexes__mutmut_67': x_ensure_indexes__mutmut_67, 
    'x_ensure_indexes__mutmut_68': x_ensure_indexes__mutmut_68, 
    'x_ensure_indexes__mutmut_69': x_ensure_indexes__mutmut_69, 
    'x_ensure_indexes__mutmut_70': x_ensure_indexes__mutmut_70, 
    'x_ensure_indexes__mutmut_71': x_ensure_indexes__mutmut_71, 
    'x_ensure_indexes__mutmut_72': x_ensure_indexes__mutmut_72, 
    'x_ensure_indexes__mutmut_73': x_ensure_indexes__mutmut_73, 
    'x_ensure_indexes__mutmut_74': x_ensure_indexes__mutmut_74, 
    'x_ensure_indexes__mutmut_75': x_ensure_indexes__mutmut_75, 
    'x_ensure_indexes__mutmut_76': x_ensure_indexes__mutmut_76, 
    'x_ensure_indexes__mutmut_77': x_ensure_indexes__mutmut_77, 
    'x_ensure_indexes__mutmut_78': x_ensure_indexes__mutmut_78, 
    'x_ensure_indexes__mutmut_79': x_ensure_indexes__mutmut_79, 
    'x_ensure_indexes__mutmut_80': x_ensure_indexes__mutmut_80, 
    'x_ensure_indexes__mutmut_81': x_ensure_indexes__mutmut_81, 
    'x_ensure_indexes__mutmut_82': x_ensure_indexes__mutmut_82, 
    'x_ensure_indexes__mutmut_83': x_ensure_indexes__mutmut_83, 
    'x_ensure_indexes__mutmut_84': x_ensure_indexes__mutmut_84, 
    'x_ensure_indexes__mutmut_85': x_ensure_indexes__mutmut_85, 
    'x_ensure_indexes__mutmut_86': x_ensure_indexes__mutmut_86, 
    'x_ensure_indexes__mutmut_87': x_ensure_indexes__mutmut_87, 
    'x_ensure_indexes__mutmut_88': x_ensure_indexes__mutmut_88, 
    'x_ensure_indexes__mutmut_89': x_ensure_indexes__mutmut_89, 
    'x_ensure_indexes__mutmut_90': x_ensure_indexes__mutmut_90, 
    'x_ensure_indexes__mutmut_91': x_ensure_indexes__mutmut_91, 
    'x_ensure_indexes__mutmut_92': x_ensure_indexes__mutmut_92, 
    'x_ensure_indexes__mutmut_93': x_ensure_indexes__mutmut_93, 
    'x_ensure_indexes__mutmut_94': x_ensure_indexes__mutmut_94, 
    'x_ensure_indexes__mutmut_95': x_ensure_indexes__mutmut_95, 
    'x_ensure_indexes__mutmut_96': x_ensure_indexes__mutmut_96, 
    'x_ensure_indexes__mutmut_97': x_ensure_indexes__mutmut_97, 
    'x_ensure_indexes__mutmut_98': x_ensure_indexes__mutmut_98, 
    'x_ensure_indexes__mutmut_99': x_ensure_indexes__mutmut_99, 
    'x_ensure_indexes__mutmut_100': x_ensure_indexes__mutmut_100, 
    'x_ensure_indexes__mutmut_101': x_ensure_indexes__mutmut_101, 
    'x_ensure_indexes__mutmut_102': x_ensure_indexes__mutmut_102, 
    'x_ensure_indexes__mutmut_103': x_ensure_indexes__mutmut_103, 
    'x_ensure_indexes__mutmut_104': x_ensure_indexes__mutmut_104, 
    'x_ensure_indexes__mutmut_105': x_ensure_indexes__mutmut_105, 
    'x_ensure_indexes__mutmut_106': x_ensure_indexes__mutmut_106, 
    'x_ensure_indexes__mutmut_107': x_ensure_indexes__mutmut_107, 
    'x_ensure_indexes__mutmut_108': x_ensure_indexes__mutmut_108, 
    'x_ensure_indexes__mutmut_109': x_ensure_indexes__mutmut_109
}

def ensure_indexes(*args, **kwargs):
    result = _mutmut_trampoline(x_ensure_indexes__mutmut_orig, x_ensure_indexes__mutmut_mutants, args, kwargs)
    return result 

ensure_indexes.__signature__ = _mutmut_signature(x_ensure_indexes__mutmut_orig)
x_ensure_indexes__mutmut_orig.__name__ = 'x_ensure_indexes'


@asynccontextmanager
async def _get_client(settings: Settings) -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(settings.mongodb_uri, uuidRepresentation="standard")
    try:
        yield client
    finally:
        client.close()


async def x_initialize_database__mutmut_orig(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = settings or get_settings()
    async with _get_client(app_settings) as client:
        database = client[app_settings.mongodb_db]
        await ensure_indexes(database)


async def x_initialize_database__mutmut_1(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = None
    async with _get_client(app_settings) as client:
        database = client[app_settings.mongodb_db]
        await ensure_indexes(database)


async def x_initialize_database__mutmut_2(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = settings and get_settings()
    async with _get_client(app_settings) as client:
        database = client[app_settings.mongodb_db]
        await ensure_indexes(database)


async def x_initialize_database__mutmut_3(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = settings or get_settings()
    async with _get_client(None) as client:
        database = client[app_settings.mongodb_db]
        await ensure_indexes(database)


async def x_initialize_database__mutmut_4(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = settings or get_settings()
    async with _get_client(app_settings) as client:
        database = None
        await ensure_indexes(database)


async def x_initialize_database__mutmut_5(settings: Settings | None = None) -> None:
    """Ensure database indexes exist using provided settings."""

    app_settings = settings or get_settings()
    async with _get_client(app_settings) as client:
        database = client[app_settings.mongodb_db]
        await ensure_indexes(None)

x_initialize_database__mutmut_mutants : ClassVar[MutantDict] = {
'x_initialize_database__mutmut_1': x_initialize_database__mutmut_1, 
    'x_initialize_database__mutmut_2': x_initialize_database__mutmut_2, 
    'x_initialize_database__mutmut_3': x_initialize_database__mutmut_3, 
    'x_initialize_database__mutmut_4': x_initialize_database__mutmut_4, 
    'x_initialize_database__mutmut_5': x_initialize_database__mutmut_5
}

def initialize_database(*args, **kwargs):
    result = _mutmut_trampoline(x_initialize_database__mutmut_orig, x_initialize_database__mutmut_mutants, args, kwargs)
    return result 

initialize_database.__signature__ = _mutmut_signature(x_initialize_database__mutmut_orig)
x_initialize_database__mutmut_orig.__name__ = 'x_initialize_database'


def x_main__mutmut_orig() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_1() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=None)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_2() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = None

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_3() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        None,
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_4() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        None,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_5() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        None,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_6() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_7() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_8() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_9() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "XXEnsuring MongoDB schema on %s/%sXX",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_10() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "ensuring mongodb schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_11() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "ENSURING MONGODB SCHEMA ON %S/%S",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(settings))


def x_main__mutmut_12() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(None)


def x_main__mutmut_13() -> None:
    """CLI entry-point to initialize the MongoDB schema."""

    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    logger.info(
        "Ensuring MongoDB schema on %s/%s",
        settings.mongodb_uri,
        settings.mongodb_db,
    )
    asyncio.run(initialize_database(None))

x_main__mutmut_mutants : ClassVar[MutantDict] = {
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'


if __name__ == "__main__":
    main()
