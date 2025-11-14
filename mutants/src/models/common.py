"""Common utilities and base classes for models."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field

ObjectIdStr = Annotated[
    str,
    Field(min_length=24, max_length=24, pattern=r"^[0-9a-fA-F]{24}$"),
]
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


class DocumentModel(BaseModel):
    """Base model configuring Pydantic for Mongo compatibility."""

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={
            ObjectId: lambda oid: str(oid),
            Decimal: lambda value: str(value),
        },
        use_enum_values=True,
    )


def x_generate_object_id__mutmut_orig() -> str:
    """Return a new ObjectId as hexadecimal string."""
    return str(ObjectId())


def x_generate_object_id__mutmut_1() -> str:
    """Return a new ObjectId as hexadecimal string."""
    return str(None)

x_generate_object_id__mutmut_mutants : ClassVar[MutantDict] = {
'x_generate_object_id__mutmut_1': x_generate_object_id__mutmut_1
}

def generate_object_id(*args, **kwargs):
    result = _mutmut_trampoline(x_generate_object_id__mutmut_orig, x_generate_object_id__mutmut_mutants, args, kwargs)
    return result 

generate_object_id.__signature__ = _mutmut_signature(x_generate_object_id__mutmut_orig)
x_generate_object_id__mutmut_orig.__name__ = 'x_generate_object_id'


def x_ensure_object_id__mutmut_orig(value: str) -> ObjectId:
    """Convert hex string to ObjectId or raise ValueError."""
    if not ObjectId.is_valid(value):
        raise ValueError(f"Invalid ObjectId: {value}")
    return ObjectId(value)


def x_ensure_object_id__mutmut_1(value: str) -> ObjectId:
    """Convert hex string to ObjectId or raise ValueError."""
    if ObjectId.is_valid(value):
        raise ValueError(f"Invalid ObjectId: {value}")
    return ObjectId(value)


def x_ensure_object_id__mutmut_2(value: str) -> ObjectId:
    """Convert hex string to ObjectId or raise ValueError."""
    if not ObjectId.is_valid(None):
        raise ValueError(f"Invalid ObjectId: {value}")
    return ObjectId(value)


def x_ensure_object_id__mutmut_3(value: str) -> ObjectId:
    """Convert hex string to ObjectId or raise ValueError."""
    if not ObjectId.is_valid(value):
        raise ValueError(None)
    return ObjectId(value)


def x_ensure_object_id__mutmut_4(value: str) -> ObjectId:
    """Convert hex string to ObjectId or raise ValueError."""
    if not ObjectId.is_valid(value):
        raise ValueError(f"Invalid ObjectId: {value}")
    return ObjectId(None)

x_ensure_object_id__mutmut_mutants : ClassVar[MutantDict] = {
'x_ensure_object_id__mutmut_1': x_ensure_object_id__mutmut_1, 
    'x_ensure_object_id__mutmut_2': x_ensure_object_id__mutmut_2, 
    'x_ensure_object_id__mutmut_3': x_ensure_object_id__mutmut_3, 
    'x_ensure_object_id__mutmut_4': x_ensure_object_id__mutmut_4
}

def ensure_object_id(*args, **kwargs):
    result = _mutmut_trampoline(x_ensure_object_id__mutmut_orig, x_ensure_object_id__mutmut_mutants, args, kwargs)
    return result 

ensure_object_id.__signature__ = _mutmut_signature(x_ensure_object_id__mutmut_orig)
x_ensure_object_id__mutmut_orig.__name__ = 'x_ensure_object_id'


def x_now_utc__mutmut_orig() -> datetime:
    """Return an aware datetime in UTC."""
    return datetime.now(tz=timezone.utc)


def x_now_utc__mutmut_1() -> datetime:
    """Return an aware datetime in UTC."""
    return datetime.now(tz=None)

x_now_utc__mutmut_mutants : ClassVar[MutantDict] = {
'x_now_utc__mutmut_1': x_now_utc__mutmut_1
}

def now_utc(*args, **kwargs):
    result = _mutmut_trampoline(x_now_utc__mutmut_orig, x_now_utc__mutmut_mutants, args, kwargs)
    return result 

now_utc.__signature__ = _mutmut_signature(x_now_utc__mutmut_orig)
x_now_utc__mutmut_orig.__name__ = 'x_now_utc'


def x_strip_and_validate_non_empty__mutmut_orig(value: str, field_name: str) -> str:
    """Strip whitespace and ensure value is not empty."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} must not be empty")
    return cleaned


def x_strip_and_validate_non_empty__mutmut_1(value: str, field_name: str) -> str:
    """Strip whitespace and ensure value is not empty."""
    cleaned = None
    if not cleaned:
        raise ValueError(f"{field_name} must not be empty")
    return cleaned


def x_strip_and_validate_non_empty__mutmut_2(value: str, field_name: str) -> str:
    """Strip whitespace and ensure value is not empty."""
    cleaned = value.strip()
    if cleaned:
        raise ValueError(f"{field_name} must not be empty")
    return cleaned


def x_strip_and_validate_non_empty__mutmut_3(value: str, field_name: str) -> str:
    """Strip whitespace and ensure value is not empty."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(None)
    return cleaned

x_strip_and_validate_non_empty__mutmut_mutants : ClassVar[MutantDict] = {
'x_strip_and_validate_non_empty__mutmut_1': x_strip_and_validate_non_empty__mutmut_1, 
    'x_strip_and_validate_non_empty__mutmut_2': x_strip_and_validate_non_empty__mutmut_2, 
    'x_strip_and_validate_non_empty__mutmut_3': x_strip_and_validate_non_empty__mutmut_3
}

def strip_and_validate_non_empty(*args, **kwargs):
    result = _mutmut_trampoline(x_strip_and_validate_non_empty__mutmut_orig, x_strip_and_validate_non_empty__mutmut_mutants, args, kwargs)
    return result 

strip_and_validate_non_empty.__signature__ = _mutmut_signature(x_strip_and_validate_non_empty__mutmut_orig)
x_strip_and_validate_non_empty__mutmut_orig.__name__ = 'x_strip_and_validate_non_empty'
