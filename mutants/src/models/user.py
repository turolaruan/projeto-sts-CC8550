"""User domain and API models."""

from __future__ import annotations

from datetime import datetime
from pydantic import EmailStr, Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import CurrencyCode
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


class UserBase(DocumentModel):
    """Shared attributes for user representations."""

    name: str = Field(min_length=3, max_length=100)
    email: EmailStr
    default_currency: CurrencyCode = Field(default=CurrencyCode.BRL)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not blank and normalize whitespace."""
        return strip_and_validate_non_empty(value, "name")

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        """Ensure email is lower-case for uniqueness."""
        return value.lower()


class UserCreate(UserBase):
    """Payload for creating users."""

    model_config = {"extra": "forbid"}


class UserUpdate(DocumentModel):
    """Payload for updating users."""

    name: str | None = Field(default=None, min_length=3, max_length=100)
    default_currency: CurrencyCode | None = None

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Ensure updated name is valid if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "name")


class User(UserBase):
    """Represents a user in the system."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


class UserInDB(User):
    """Alias for clarity when dealing with persisted entities."""


def x_build_user__mutmut_orig(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_1(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = None
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_2(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=None,
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_3(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=None,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_4(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=None,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_5(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=None,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_6(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=None,
        updated_at=timestamp,
    )


def x_build_user__mutmut_7(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=None,
    )


def x_build_user__mutmut_8(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_9(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_10(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        default_currency=payload.default_currency,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_11(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_user__mutmut_12(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        updated_at=timestamp,
    )


def x_build_user__mutmut_13(payload: UserCreate) -> User:
    """Construct a new user entity from creation payload."""
    timestamp = now_utc()
    return User(
        id=generate_object_id(),
        name=payload.name,
        email=payload.email,
        default_currency=payload.default_currency,
        created_at=timestamp,
        )

x_build_user__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_user__mutmut_1': x_build_user__mutmut_1, 
    'x_build_user__mutmut_2': x_build_user__mutmut_2, 
    'x_build_user__mutmut_3': x_build_user__mutmut_3, 
    'x_build_user__mutmut_4': x_build_user__mutmut_4, 
    'x_build_user__mutmut_5': x_build_user__mutmut_5, 
    'x_build_user__mutmut_6': x_build_user__mutmut_6, 
    'x_build_user__mutmut_7': x_build_user__mutmut_7, 
    'x_build_user__mutmut_8': x_build_user__mutmut_8, 
    'x_build_user__mutmut_9': x_build_user__mutmut_9, 
    'x_build_user__mutmut_10': x_build_user__mutmut_10, 
    'x_build_user__mutmut_11': x_build_user__mutmut_11, 
    'x_build_user__mutmut_12': x_build_user__mutmut_12, 
    'x_build_user__mutmut_13': x_build_user__mutmut_13
}

def build_user(*args, **kwargs):
    result = _mutmut_trampoline(x_build_user__mutmut_orig, x_build_user__mutmut_mutants, args, kwargs)
    return result 

build_user.__signature__ = _mutmut_signature(x_build_user__mutmut_orig)
x_build_user__mutmut_orig.__name__ = 'x_build_user'
