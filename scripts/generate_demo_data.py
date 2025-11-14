"""Populate MongoDB with demo data for the Finance Manager API."""

from __future__ import annotations

import argparse
import asyncio
import random
import sys
from pathlib import Path
from typing import Iterable

from motor.motor_asyncio import AsyncIOMotorClient

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from config.settings import get_settings  # noqa: E402
from tests.fixtures.factories import (  # noqa: E402
    make_account_model,
    make_budget_model,
    make_goal_model,
    make_transaction_model,
    make_user_model,
)


def _model_to_document(model) -> dict:
    data = model.model_dump()
    data["_id"] = data.pop("id")
    for key, value in list(data.items()):
        if hasattr(value, "isoformat"):
            data[key] = value.isoformat()
    return data


async def seed_demo_data(
    *,
    users: int,
    accounts_per_user: int,
    budgets_per_user: int,
    goals_per_user: int,
    transactions_per_account: int,
    mongodb_uri: str | None,
    mongodb_database: str | None,
    drop_existing: bool,
) -> None:
    settings = get_settings()
    uri = mongodb_uri or settings.mongodb_uri
    database_name = mongodb_database or settings.mongodb_database

    client = AsyncIOMotorClient(uri)
    db = client[database_name]

    if drop_existing:
        for collection_name in ("users", "accounts", "budgets", "goals", "transactions"):
            await db[collection_name].delete_many({})

    user_models = [
        make_user_model(name=f"Demo User {idx+1}", email=f"user{idx+1}@demo.example.com")
        for idx in range(users)
    ]
    account_models = []
    budget_models = []
    goal_models = []
    transaction_models = []

    for user in user_models:
        for account_idx in range(accounts_per_user):
            account_models.append(
                make_account_model(
                    user_id=user.id,
                    name=f"{user.name.split()[0]}'s Account {account_idx+1}",
                    balance=random.choice([1000, 2500, 4200]),
                )
            )
        for budget_idx in range(budgets_per_user):
            budget_models.append(
                make_budget_model(
                    user_id=user.id,
                    category=random.choice(["groceries", "rent", "transport", "entertainment"]),
                    limit_amount=random.choice([300, 500, 800]),
                    amount_spent=random.choice([0, 50, 150]),
                )
            )

    for account in account_models:
        for goal_idx in range(goals_per_user):
            goal_models.append(
                make_goal_model(
                    user_id=account.user_id,
                    account_id=account.id,
                    name=f"Goal {goal_idx+1} for {account.name}",
                    target_amount=random.choice([500, 1200, 2000]),
                    current_amount=random.choice([0, 150, 300]),
                )
            )
        for tx_idx in range(transactions_per_account):
            transaction_models.append(
                make_transaction_model(
                    user_id=account.user_id,
                    account_id=account.id,
                    amount=random.choice([20, 45, 75, 110]),
                    description=f"Auto TX {tx_idx+1} - {account.name}",
                )
            )

    await db.users.insert_many([_model_to_document(u) for u in user_models])
    await db.accounts.insert_many([_model_to_document(a) for a in account_models])
    await db.budgets.insert_many([_model_to_document(b) for b in budget_models])
    if goal_models:
        await db.goals.insert_many([_model_to_document(g) for g in goal_models])
    if transaction_models:
        await db.transactions.insert_many([_model_to_document(t) for t in transaction_models])

    print(
        f"Inserted {len(user_models)} users, "
        f"{len(account_models)} accounts, "
        f"{len(budget_models)} budgets, "
        f"{len(goal_models)} goals, "
        f"{len(transaction_models)} transactions into '{database_name}'."
    )


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Seed MongoDB with demo data.")
    parser.add_argument("--users", type=int, default=3, help="Number of users to create.")
    parser.add_argument("--accounts-per-user", type=int, default=2, help="Accounts per user.")
    parser.add_argument("--budgets-per-user", type=int, default=2, help="Budgets per user.")
    parser.add_argument("--goals-per-user", type=int, default=1, help="Goals per account.")
    parser.add_argument("--transactions-per-account", type=int, default=5, help="Transactions per account.")
    parser.add_argument("--mongodb-uri", type=str, help="Override MongoDB URI.")
    parser.add_argument("--mongodb-database", type=str, help="Override database name.")
    parser.add_argument("--drop-existing", action="store_true", help="Delete existing documents first.")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    asyncio.run(
        seed_demo_data(
            users=args.users,
            accounts_per_user=args.accounts_per_user,
            budgets_per_user=args.budgets_per_user,
            goals_per_user=args.goals_per_user,
            transactions_per_account=args.transactions_per_account,
            mongodb_uri=args.mongodb_uri,
            mongodb_database=args.mongodb_database,
            drop_existing=args.drop_existing,
        )
    )


if __name__ == "__main__":
    main()
