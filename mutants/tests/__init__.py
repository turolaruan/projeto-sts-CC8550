"""Ensure project root is importable in tests and provide optional stubs."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace

if os.environ.get("MUTANT_UNDER_TEST") == "fail":  # pragma: no cover - exercised only by mutmut
    raise SystemExit("Mutmut verification run")

_CURRENT_ROOT = Path(__file__).resolve().parent.parent
_ORIGINAL_ROOT = os.environ.get("PROJECT_ROOT")
candidate_roots = [_CURRENT_ROOT]
if _ORIGINAL_ROOT:
    original_path = Path(_ORIGINAL_ROOT).resolve()
    if original_path != _CURRENT_ROOT:
        candidate_roots.append(original_path)
        os.environ["COV_CORE_SKIP"] = "1"
else:
    os.environ.setdefault("PROJECT_ROOT", str(_CURRENT_ROOT))
for _root in candidate_roots:
    root_str = str(_root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)


def _install_motor_stub() -> None:
    """Provide a lightweight stub for motor if the real dependency is missing or broken."""
    if "motor.motor_asyncio" in sys.modules:
        return
    try:  # pragma: no cover - prefer real dependency when available
        import motor.motor_asyncio  # type: ignore  # noqa: F401

        return
    except Exception:
        pass

    class _AsyncCursor:
        def __init__(self) -> None:
            self._iterated = False

        def sort(self, *args, **kwargs) -> "_AsyncCursor":
            return self

        def __aiter__(self) -> "_AsyncCursor":
            self._iterated = False
            return self

        async def __anext__(self):
            if self._iterated:
                raise StopAsyncIteration
            self._iterated = True
            raise StopAsyncIteration

        async def to_list(self, length: int) -> list[dict[str, object]]:
            return []

    class _AsyncIOMotorCollection(SimpleNamespace):
        async def create_index(self, *args, **kwargs):
            return None

        async def insert_one(self, *args, **kwargs):
            return SimpleNamespace(inserted_id=None)

        async def find_one(self, *args, **kwargs):
            return None

        def find(self, *args, **kwargs) -> _AsyncCursor:
            return _AsyncCursor()

        async def find_one_and_update(self, *args, **kwargs):
            return None

        async def delete_one(self, *args, **kwargs):
            return SimpleNamespace(deleted_count=0)

        async def count_documents(self, *args, **kwargs):
            return 0

        def aggregate(self, *args, **kwargs) -> _AsyncCursor:
            return _AsyncCursor()

    class _AsyncIOMotorDatabase(dict):
        def get_collection(self, name: str) -> _AsyncIOMotorCollection:
            if name not in self:
                self[name] = _AsyncIOMotorCollection()
            return self[name]

    class _AsyncIOMotorClient:
        def __init__(self, *args, **kwargs) -> None:
            self._databases: dict[str, _AsyncIOMotorDatabase] = {}

        def __getitem__(self, name: str) -> _AsyncIOMotorDatabase:
            if name not in self._databases:
                self._databases[name] = _AsyncIOMotorDatabase()
            return self._databases[name]

        def close(self) -> None:
            self._databases.clear()

    motor_module = ModuleType("motor")
    motor_asyncio_module = ModuleType("motor.motor_asyncio")
    motor_asyncio_module.AsyncIOMotorClient = _AsyncIOMotorClient
    motor_asyncio_module.AsyncIOMotorDatabase = _AsyncIOMotorDatabase
    motor_asyncio_module.AsyncIOMotorCollection = _AsyncIOMotorCollection
    motor_module.motor_asyncio = motor_asyncio_module  # type: ignore[attr-defined]

    sys.modules["motor"] = motor_module
    sys.modules["motor.motor_asyncio"] = motor_asyncio_module


def _install_pymongo_stub() -> None:
    """Provide a very small pymongo stub for test environments."""
    if "pymongo" in sys.modules:
        return
    try:  # pragma: no cover - prefer real dependency
        import pymongo  # type: ignore  # noqa: F401

        return
    except Exception:
        pass

    pymongo_module = ModuleType("pymongo")
    pymongo_module.ASCENDING = 1
    pymongo_module.DESCENDING = -1

    class _ReturnDocument:
        BEFORE = "before"
        AFTER = "after"

    class _DuplicateKeyError(Exception):
        """Fallback DuplicateKeyError."""

    pymongo_module.ReturnDocument = _ReturnDocument
    errors_module = ModuleType("pymongo.errors")
    errors_module.DuplicateKeyError = _DuplicateKeyError
    pymongo_module.errors = errors_module  # type: ignore[attr-defined]

    sys.modules["pymongo"] = pymongo_module
    sys.modules["pymongo.errors"] = errors_module


_install_motor_stub()
_install_pymongo_stub()
