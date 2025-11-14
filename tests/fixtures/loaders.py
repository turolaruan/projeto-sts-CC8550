"""Utility helpers to read fixture data from JSON files."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Type, TypeVar

from pydantic import BaseModel

FIXTURE_DIR = Path(__file__).resolve().parent
T = TypeVar("T", bound=BaseModel)


def get_fixture_path(name: str) -> Path:
    """Return the path to a fixture JSON file by name."""
    path = FIXTURE_DIR / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(f"Fixture '{name}' not found at {path}")
    return path


@lru_cache(maxsize=None)
def load_fixture(name: str) -> Any:
    """Load the raw JSON content for a fixture file."""
    path = get_fixture_path(name)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_models(name: str, model_cls: Type[T]) -> Iterable[T]:
    """Instantiate Pydantic models from a fixture file."""
    records = load_fixture(name)
    if not isinstance(records, list):
        raise ValueError(f"Fixture '{name}' must contain a JSON array of objects.")
    return [model_cls(**record) for record in records]
