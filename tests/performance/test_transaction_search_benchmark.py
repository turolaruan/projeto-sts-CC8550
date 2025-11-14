"""Performance benchmark for transaction search functionality."""

import asyncio

from src.models import TransactionFilter
from tests.fixtures.factories import make_transaction_model


def test_transaction_search_benchmark(transaction_service, transaction_repository, benchmark):
    user_id = "perf-user"

    async def populate() -> None:
        for idx in range(200):
            transaction = make_transaction_model(user_id=user_id, amount=idx + 1)
            transaction_repository.storage[transaction.id] = transaction.model_dump()

    asyncio.run(populate())
    filters = TransactionFilter(user_id=user_id)

    async def run_search():
        await transaction_service.search_transactions(filters)

    benchmark(lambda: asyncio.run(run_search()))
