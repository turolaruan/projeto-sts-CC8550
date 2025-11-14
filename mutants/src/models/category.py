"""Category domain and API models."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import CategoryType
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


class CategoryBase(DocumentModel):
    """Shared category attributes."""

    user_id: ObjectIdStr
    name: str = Field(min_length=2, max_length=100)
    category_type: CategoryType
    description: str | None = Field(default=None, max_length=255)
    parent_id: ObjectIdStr | None = Field(default=None)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not blank and normalize."""
        return strip_and_validate_non_empty(value, "name")


class CategoryCreate(CategoryBase):
    """Payload for creating categories."""

    model_config = {"extra": "forbid"}


class CategoryUpdate(DocumentModel):
    """Payload for updating categories."""

    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    parent_id: ObjectIdStr | None = Field(default=None)

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Ensure updated name is valid if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "name")


class Category(CategoryBase):
    """Represents a stored category."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def x_build_category__mutmut_orig(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_1(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = None
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_2(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=None,
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_3(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=None,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_4(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=None,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_5(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=None,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_6(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=None,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_7(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=None,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_8(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=None,
        updated_at=timestamp,
    )


def x_build_category__mutmut_9(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=None,
    )


def x_build_category__mutmut_10(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_11(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_12(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_13(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_14(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        parent_id=payload.parent_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_15(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_category__mutmut_16(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        updated_at=timestamp,
    )


def x_build_category__mutmut_17(payload: CategoryCreate) -> Category:
    """Construct a category entity from payload."""
    timestamp = now_utc()
    return Category(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        category_type=payload.category_type,
        description=payload.description,
        parent_id=payload.parent_id,
        created_at=timestamp,
        )

x_build_category__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_category__mutmut_1': x_build_category__mutmut_1, 
    'x_build_category__mutmut_2': x_build_category__mutmut_2, 
    'x_build_category__mutmut_3': x_build_category__mutmut_3, 
    'x_build_category__mutmut_4': x_build_category__mutmut_4, 
    'x_build_category__mutmut_5': x_build_category__mutmut_5, 
    'x_build_category__mutmut_6': x_build_category__mutmut_6, 
    'x_build_category__mutmut_7': x_build_category__mutmut_7, 
    'x_build_category__mutmut_8': x_build_category__mutmut_8, 
    'x_build_category__mutmut_9': x_build_category__mutmut_9, 
    'x_build_category__mutmut_10': x_build_category__mutmut_10, 
    'x_build_category__mutmut_11': x_build_category__mutmut_11, 
    'x_build_category__mutmut_12': x_build_category__mutmut_12, 
    'x_build_category__mutmut_13': x_build_category__mutmut_13, 
    'x_build_category__mutmut_14': x_build_category__mutmut_14, 
    'x_build_category__mutmut_15': x_build_category__mutmut_15, 
    'x_build_category__mutmut_16': x_build_category__mutmut_16, 
    'x_build_category__mutmut_17': x_build_category__mutmut_17
}

def build_category(*args, **kwargs):
    result = _mutmut_trampoline(x_build_category__mutmut_orig, x_build_category__mutmut_mutants, args, kwargs)
    return result 

build_category.__signature__ = _mutmut_signature(x_build_category__mutmut_orig)
x_build_category__mutmut_orig.__name__ = 'x_build_category'
