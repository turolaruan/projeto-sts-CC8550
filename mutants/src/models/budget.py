"""Budget domain and API models."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from pydantic import Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
)
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


class BudgetBase(DocumentModel):
    """Shared attributes for budgets."""

    user_id: ObjectIdStr
    category_id: ObjectIdStr
    year: int = Field(ge=2000, le=2100)
    month: int = Field(ge=1, le=12)
    amount: Decimal = Field(gt=Decimal("0"))
    alert_percentage: int = Field(default=80, ge=1, le=100)

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal) -> Decimal:
        """Normalize amount to two decimals."""
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class BudgetCreate(BudgetBase):
    """Payload for creating budgets."""

    model_config = {"extra": "forbid"}


class BudgetUpdate(DocumentModel):
    """Payload for updating budgets."""

    amount: Decimal | None = Field(default=None, gt=Decimal("0"))
    alert_percentage: int | None = Field(default=None, ge=1, le=100)

    model_config = {"extra": "forbid"}

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal | None) -> Decimal | None:
        if value is None:
            return None
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class Budget(BudgetBase):
    """Represents a stored budget."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def x_build_budget__mutmut_orig(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_1(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = None
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_2(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=None,
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_3(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=None,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_4(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=None,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_5(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=None,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_6(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=None,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_7(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=None,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_8(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=None,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_9(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=None,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_10(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=None,
    )


def x_build_budget__mutmut_11(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_12(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_13(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_14(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_15(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_16(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_17(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_18(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        updated_at=timestamp,
    )


def x_build_budget__mutmut_19(payload: BudgetCreate) -> Budget:
    """Construct budget entity from payload."""
    timestamp = now_utc()
    return Budget(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        year=payload.year,
        month=payload.month,
        amount=payload.amount,
        alert_percentage=payload.alert_percentage,
        created_at=timestamp,
        )

x_build_budget__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_budget__mutmut_1': x_build_budget__mutmut_1, 
    'x_build_budget__mutmut_2': x_build_budget__mutmut_2, 
    'x_build_budget__mutmut_3': x_build_budget__mutmut_3, 
    'x_build_budget__mutmut_4': x_build_budget__mutmut_4, 
    'x_build_budget__mutmut_5': x_build_budget__mutmut_5, 
    'x_build_budget__mutmut_6': x_build_budget__mutmut_6, 
    'x_build_budget__mutmut_7': x_build_budget__mutmut_7, 
    'x_build_budget__mutmut_8': x_build_budget__mutmut_8, 
    'x_build_budget__mutmut_9': x_build_budget__mutmut_9, 
    'x_build_budget__mutmut_10': x_build_budget__mutmut_10, 
    'x_build_budget__mutmut_11': x_build_budget__mutmut_11, 
    'x_build_budget__mutmut_12': x_build_budget__mutmut_12, 
    'x_build_budget__mutmut_13': x_build_budget__mutmut_13, 
    'x_build_budget__mutmut_14': x_build_budget__mutmut_14, 
    'x_build_budget__mutmut_15': x_build_budget__mutmut_15, 
    'x_build_budget__mutmut_16': x_build_budget__mutmut_16, 
    'x_build_budget__mutmut_17': x_build_budget__mutmut_17, 
    'x_build_budget__mutmut_18': x_build_budget__mutmut_18, 
    'x_build_budget__mutmut_19': x_build_budget__mutmut_19
}

def build_budget(*args, **kwargs):
    result = _mutmut_trampoline(x_build_budget__mutmut_orig, x_build_budget__mutmut_mutants, args, kwargs)
    return result 

build_budget.__signature__ = _mutmut_signature(x_build_budget__mutmut_orig)
x_build_budget__mutmut_orig.__name__ = 'x_build_budget'
