"""Performance and load-oriented tests using pytest-benchmark."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.services.user_service import UserService
from tests.structural.helpers import build_user


class LargeDatasetRepository:
    """Stub repository returning a pre-built large dataset."""

    def __init__(self, dataset):
        self.dataset = dataset

    async def list(self, **filters):
        if filters:
            return [user for user in self.dataset if all(getattr(user, key) == value for key, value in filters.items())]
        return list(self.dataset)

    async def create(self, entity):
        raise NotImplementedError

    async def get(self, entity_id):
        raise NotImplementedError

    async def update(self, entity_id, data):
        raise NotImplementedError

    async def delete(self, entity_id):
        raise NotImplementedError


@pytest.mark.benchmark
def test_list_users_performance_with_large_volume(benchmark) -> None:
    """Benchmark list_users with a large dataset to detect regressions."""
    dataset = [
        build_user(name=f"Usuario {idx}", email=f"user{idx}@example.com")
        for idx in range(5000)
    ]
    repository = LargeDatasetRepository(dataset)
    service = UserService(repository)  # type: ignore[arg-type]

    def run_list_users():
        return asyncio.run(service.list_users())

    result = benchmark(run_list_users)
    assert len(result) == len(dataset)
