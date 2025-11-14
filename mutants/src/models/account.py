"""Account domain and API models."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from pydantic import Field, field_validator

from src.models.common import (
    DocumentModel,
    ObjectIdStr,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import AccountType, CurrencyCode
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


class AccountBase(DocumentModel):
    """Shared account attributes."""

    user_id: ObjectIdStr
    name: str = Field(min_length=3, max_length=120)
    account_type: AccountType
    currency: CurrencyCode = Field(default=CurrencyCode.BRL)
    description: str | None = Field(default=None, max_length=255)
    minimum_balance: Decimal = Field(default=Decimal("0"))

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Ensure name is not blank and normalize whitespace."""
        return strip_and_validate_non_empty(value, "name")

    @field_validator("minimum_balance")
    @classmethod
    def normalize_minimum_balance(cls, value: Decimal) -> Decimal:
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class AccountCreate(AccountBase):
    """Payload for creating accounts."""

    starting_balance: Decimal = Field(default=Decimal("0"))

    model_config = {"extra": "forbid"}

    @field_validator("starting_balance")
    @classmethod
    def validate_balance(cls, value: Decimal) -> Decimal:
        """Normalize decimal to two fraction digits."""
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class AccountUpdate(DocumentModel):
    """Payload for updating accounts."""

    name: str | None = Field(default=None, min_length=3, max_length=120)
    description: str | None = Field(default=None, max_length=255)
    account_type: AccountType | None = None
    currency: CurrencyCode | None = None
    minimum_balance: Decimal | None = None

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Ensure updated name is valid if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "name")

    @field_validator("minimum_balance")
    @classmethod
    def normalize_minimum_balance(cls, value: Decimal | None) -> Decimal | None:
        if value is None:
            return None
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class Account(AccountBase):
    """Represents a stored account."""

    id: ObjectIdStr
    balance: Decimal = Field(default=Decimal("0"))
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def x_build_account__mutmut_orig(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_1(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = None
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_2(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=None,
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_3(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=None,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_4(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=None,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_5(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=None,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_6(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=None,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_7(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=None,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_8(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=None,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_9(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=None,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_10(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=None,
        updated_at=timestamp,
    )


def x_build_account__mutmut_11(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=None,
    )


def x_build_account__mutmut_12(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_13(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_14(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_15(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_16(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_17(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_18(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_19(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_20(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        updated_at=timestamp,
    )


def x_build_account__mutmut_21(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        )


def x_build_account__mutmut_22(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(None, rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_23(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), rounding=None),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_24(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_25(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("0.01"), ),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_26(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal(None), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_account__mutmut_27(payload: AccountCreate) -> Account:
    """Construct an account entity from payload."""
    timestamp = now_utc()
    return Account(
        id=generate_object_id(),
        user_id=payload.user_id,
        name=payload.name,
        account_type=payload.account_type,
        currency=payload.currency,
        description=payload.description,
        minimum_balance=payload.minimum_balance,
        balance=payload.starting_balance.quantize(Decimal("XX0.01XX"), rounding=ROUND_HALF_UP),
        created_at=timestamp,
        updated_at=timestamp,
    )

x_build_account__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_account__mutmut_1': x_build_account__mutmut_1, 
    'x_build_account__mutmut_2': x_build_account__mutmut_2, 
    'x_build_account__mutmut_3': x_build_account__mutmut_3, 
    'x_build_account__mutmut_4': x_build_account__mutmut_4, 
    'x_build_account__mutmut_5': x_build_account__mutmut_5, 
    'x_build_account__mutmut_6': x_build_account__mutmut_6, 
    'x_build_account__mutmut_7': x_build_account__mutmut_7, 
    'x_build_account__mutmut_8': x_build_account__mutmut_8, 
    'x_build_account__mutmut_9': x_build_account__mutmut_9, 
    'x_build_account__mutmut_10': x_build_account__mutmut_10, 
    'x_build_account__mutmut_11': x_build_account__mutmut_11, 
    'x_build_account__mutmut_12': x_build_account__mutmut_12, 
    'x_build_account__mutmut_13': x_build_account__mutmut_13, 
    'x_build_account__mutmut_14': x_build_account__mutmut_14, 
    'x_build_account__mutmut_15': x_build_account__mutmut_15, 
    'x_build_account__mutmut_16': x_build_account__mutmut_16, 
    'x_build_account__mutmut_17': x_build_account__mutmut_17, 
    'x_build_account__mutmut_18': x_build_account__mutmut_18, 
    'x_build_account__mutmut_19': x_build_account__mutmut_19, 
    'x_build_account__mutmut_20': x_build_account__mutmut_20, 
    'x_build_account__mutmut_21': x_build_account__mutmut_21, 
    'x_build_account__mutmut_22': x_build_account__mutmut_22, 
    'x_build_account__mutmut_23': x_build_account__mutmut_23, 
    'x_build_account__mutmut_24': x_build_account__mutmut_24, 
    'x_build_account__mutmut_25': x_build_account__mutmut_25, 
    'x_build_account__mutmut_26': x_build_account__mutmut_26, 
    'x_build_account__mutmut_27': x_build_account__mutmut_27
}

def build_account(*args, **kwargs):
    result = _mutmut_trampoline(x_build_account__mutmut_orig, x_build_account__mutmut_mutants, args, kwargs)
    return result 

build_account.__signature__ = _mutmut_signature(x_build_account__mutmut_orig)
x_build_account__mutmut_orig.__name__ = 'x_build_account'
