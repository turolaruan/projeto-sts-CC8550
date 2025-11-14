"""Report response models."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, List

from pydantic import Field

from src.models.common import DocumentModel, ObjectIdStr
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


class MonthlyCategorySummary(DocumentModel):
    """Aggregated summary for a category in a month."""

    category_id: ObjectIdStr
    name: str
    transaction_type: TransactionType
    total: Decimal = Field(default=Decimal("0"))
    count: int = Field(default=0, ge=0)
    budget_amount: Decimal | None = None
    budget_remaining: Decimal | None = None


class MonthlySummary(DocumentModel):
    """Monthly summary report for a user."""

    user_id: ObjectIdStr
    year: int
    month: int
    totals_by_type: Dict[TransactionType, Decimal]
    categories: List[MonthlyCategorySummary]
