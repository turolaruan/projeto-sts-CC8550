"""Transaction domain and API models."""

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
from src.models.enums import TransactionType
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


class TransactionBase(DocumentModel):
    """Shared transaction attributes."""

    user_id: ObjectIdStr
    account_id: ObjectIdStr
    category_id: ObjectIdStr
    amount: Decimal = Field(gt=Decimal("0"))
    transaction_type: TransactionType
    occurred_at: datetime = Field(default_factory=now_utc)
    description: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None, max_length=1000)
    counterparty: str | None = Field(default=None, max_length=120)
    transfer_account_id: ObjectIdStr | None = None

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal) -> Decimal:
        """Normalize monetary amount."""
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @field_validator("description")
    @classmethod
    def normalize_description(cls, value: str | None) -> str | None:
        """Strip description if provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "description")


class TransactionCreate(TransactionBase):
    """Payload for creating transactions."""

    model_config = {"extra": "forbid"}


class TransactionUpdate(DocumentModel):
    """Payload for updating transactions."""

    amount: Decimal | None = Field(default=None, gt=Decimal("0"))
    occurred_at: datetime | None = None
    description: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None, max_length=1000)
    counterparty: str | None = Field(default=None, max_length=120)

    model_config = {"extra": "forbid"}

    @field_validator("amount")
    @classmethod
    def normalize_amount(cls, value: Decimal | None) -> Decimal | None:
        """Normalize amount when provided."""
        if value is None:
            return value
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @field_validator("description")
    @classmethod
    def normalize_description(cls, value: str | None) -> str | None:
        """Normalize description when provided."""
        if value is None:
            return value
        return strip_and_validate_non_empty(value, "description")


class Transaction(TransactionBase):
    """Represents a stored transaction."""

    id: ObjectIdStr
    created_at: datetime
    updated_at: datetime

    model_config = {"extra": "ignore"}


def x_build_transaction__mutmut_orig(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_1(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = None
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_2(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = None
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_3(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(None, rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_4(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=None)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_5(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_6(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), )
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_7(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal(None), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_8(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("XX0.01XX"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_9(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=None,
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_10(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=None,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_11(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=None,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_12(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=None,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_13(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=None,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_14(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=None,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_15(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=None,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_16(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=None,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_17(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=None,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_18(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=None,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_19(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=None,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_20(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=None,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_21(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=None,
    )


def x_build_transaction__mutmut_22(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_23(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_24(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_25(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_26(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_27(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_28(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_29(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_30(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_31(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_32(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        created_at=timestamp,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_33(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        updated_at=timestamp,
    )


def x_build_transaction__mutmut_34(payload: TransactionCreate) -> Transaction:
    """Construct a transaction entity from payload."""
    timestamp = now_utc()
    normalized_amount = payload.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return Transaction(
        id=generate_object_id(),
        user_id=payload.user_id,
        account_id=payload.account_id,
        category_id=payload.category_id,
        amount=normalized_amount,
        transaction_type=payload.transaction_type,
        occurred_at=payload.occurred_at,
        description=payload.description,
        notes=payload.notes,
        counterparty=payload.counterparty,
        transfer_account_id=payload.transfer_account_id,
        created_at=timestamp,
        )

x_build_transaction__mutmut_mutants : ClassVar[MutantDict] = {
'x_build_transaction__mutmut_1': x_build_transaction__mutmut_1, 
    'x_build_transaction__mutmut_2': x_build_transaction__mutmut_2, 
    'x_build_transaction__mutmut_3': x_build_transaction__mutmut_3, 
    'x_build_transaction__mutmut_4': x_build_transaction__mutmut_4, 
    'x_build_transaction__mutmut_5': x_build_transaction__mutmut_5, 
    'x_build_transaction__mutmut_6': x_build_transaction__mutmut_6, 
    'x_build_transaction__mutmut_7': x_build_transaction__mutmut_7, 
    'x_build_transaction__mutmut_8': x_build_transaction__mutmut_8, 
    'x_build_transaction__mutmut_9': x_build_transaction__mutmut_9, 
    'x_build_transaction__mutmut_10': x_build_transaction__mutmut_10, 
    'x_build_transaction__mutmut_11': x_build_transaction__mutmut_11, 
    'x_build_transaction__mutmut_12': x_build_transaction__mutmut_12, 
    'x_build_transaction__mutmut_13': x_build_transaction__mutmut_13, 
    'x_build_transaction__mutmut_14': x_build_transaction__mutmut_14, 
    'x_build_transaction__mutmut_15': x_build_transaction__mutmut_15, 
    'x_build_transaction__mutmut_16': x_build_transaction__mutmut_16, 
    'x_build_transaction__mutmut_17': x_build_transaction__mutmut_17, 
    'x_build_transaction__mutmut_18': x_build_transaction__mutmut_18, 
    'x_build_transaction__mutmut_19': x_build_transaction__mutmut_19, 
    'x_build_transaction__mutmut_20': x_build_transaction__mutmut_20, 
    'x_build_transaction__mutmut_21': x_build_transaction__mutmut_21, 
    'x_build_transaction__mutmut_22': x_build_transaction__mutmut_22, 
    'x_build_transaction__mutmut_23': x_build_transaction__mutmut_23, 
    'x_build_transaction__mutmut_24': x_build_transaction__mutmut_24, 
    'x_build_transaction__mutmut_25': x_build_transaction__mutmut_25, 
    'x_build_transaction__mutmut_26': x_build_transaction__mutmut_26, 
    'x_build_transaction__mutmut_27': x_build_transaction__mutmut_27, 
    'x_build_transaction__mutmut_28': x_build_transaction__mutmut_28, 
    'x_build_transaction__mutmut_29': x_build_transaction__mutmut_29, 
    'x_build_transaction__mutmut_30': x_build_transaction__mutmut_30, 
    'x_build_transaction__mutmut_31': x_build_transaction__mutmut_31, 
    'x_build_transaction__mutmut_32': x_build_transaction__mutmut_32, 
    'x_build_transaction__mutmut_33': x_build_transaction__mutmut_33, 
    'x_build_transaction__mutmut_34': x_build_transaction__mutmut_34
}

def build_transaction(*args, **kwargs):
    result = _mutmut_trampoline(x_build_transaction__mutmut_orig, x_build_transaction__mutmut_mutants, args, kwargs)
    return result 

build_transaction.__signature__ = _mutmut_signature(x_build_transaction__mutmut_orig)
x_build_transaction__mutmut_orig.__name__ = 'x_build_transaction'
