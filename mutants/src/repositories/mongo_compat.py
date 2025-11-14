"""Compatibility helpers for optional motor/pymongo dependencies."""

from __future__ import annotations

from typing import Any, Optional

try:  # pragma: no cover - exercised indirectly by runtime imports
    from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
    from pymongo import ASCENDING, DESCENDING, ReturnDocument
    from pymongo.errors import DuplicateKeyError

    _IMPORT_ERROR: Optional[Exception] = None
except Exception as exc:  # pragma: no cover - triggered when deps missing
    AsyncIOMotorCollection = AsyncIOMotorDatabase = Any  # type: ignore[misc, assignment]
    ASCENDING = 1  # type: ignore[assignment]
    DESCENDING = -1  # type: ignore[assignment]

    class _FallbackReturnDocument:
        BEFORE = "before"
        AFTER = "after"

    ReturnDocument = _FallbackReturnDocument()  # type: ignore[assignment]

    class DuplicateKeyError(Exception):
        """Placeholder for pymongo.errors.DuplicateKeyError."""

    _IMPORT_ERROR = exc
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


def x_ensure_motor_dependencies__mutmut_orig() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "motor/pymongo are required for MongoDB repositories but could not be imported. "
        "Install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_1() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is not None:
        return
    raise RuntimeError(
        "motor/pymongo are required for MongoDB repositories but could not be imported. "
        "Install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_2() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        None
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_3() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "XXmotor/pymongo are required for MongoDB repositories but could not be imported. XX"
        "Install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_4() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "motor/pymongo are required for mongodb repositories but could not be imported. "
        "Install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_5() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "MOTOR/PYMONGO ARE REQUIRED FOR MONGODB REPOSITORIES BUT COULD NOT BE IMPORTED. "
        "Install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_6() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "motor/pymongo are required for MongoDB repositories but could not be imported. "
        "XXInstall compatible versions or switch to the in-memory repositories for tests.XX"
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_7() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "motor/pymongo are required for MongoDB repositories but could not be imported. "
        "install compatible versions or switch to the in-memory repositories for tests."
    ) from _IMPORT_ERROR


def x_ensure_motor_dependencies__mutmut_8() -> None:
    """Raise a clear error if motor/pymongo failed to import."""
    if _IMPORT_ERROR is None:
        return
    raise RuntimeError(
        "motor/pymongo are required for MongoDB repositories but could not be imported. "
        "INSTALL COMPATIBLE VERSIONS OR SWITCH TO THE IN-MEMORY REPOSITORIES FOR TESTS."
    ) from _IMPORT_ERROR

x_ensure_motor_dependencies__mutmut_mutants : ClassVar[MutantDict] = {
'x_ensure_motor_dependencies__mutmut_1': x_ensure_motor_dependencies__mutmut_1, 
    'x_ensure_motor_dependencies__mutmut_2': x_ensure_motor_dependencies__mutmut_2, 
    'x_ensure_motor_dependencies__mutmut_3': x_ensure_motor_dependencies__mutmut_3, 
    'x_ensure_motor_dependencies__mutmut_4': x_ensure_motor_dependencies__mutmut_4, 
    'x_ensure_motor_dependencies__mutmut_5': x_ensure_motor_dependencies__mutmut_5, 
    'x_ensure_motor_dependencies__mutmut_6': x_ensure_motor_dependencies__mutmut_6, 
    'x_ensure_motor_dependencies__mutmut_7': x_ensure_motor_dependencies__mutmut_7, 
    'x_ensure_motor_dependencies__mutmut_8': x_ensure_motor_dependencies__mutmut_8
}

def ensure_motor_dependencies(*args, **kwargs):
    result = _mutmut_trampoline(x_ensure_motor_dependencies__mutmut_orig, x_ensure_motor_dependencies__mutmut_mutants, args, kwargs)
    return result 

ensure_motor_dependencies.__signature__ = _mutmut_signature(x_ensure_motor_dependencies__mutmut_orig)
x_ensure_motor_dependencies__mutmut_orig.__name__ = 'x_ensure_motor_dependencies'


__all__ = [
    "ASCENDING",
    "DESCENDING",
    "AsyncIOMotorCollection",
    "AsyncIOMotorDatabase",
    "DuplicateKeyError",
    "ReturnDocument",
    "ensure_motor_dependencies",
]
