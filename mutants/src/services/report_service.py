"""Reporting services for financial summaries."""

from __future__ import annotations

from collections import defaultdict
from decimal import Decimal
from typing import Dict, List

from src.models.enums import TransactionType
from src.models.report import MonthlyCategorySummary, MonthlySummary
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.utils.exceptions import EntityNotFoundError
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


class ReportService:
    """Generate high-level financial reports."""

    def xǁReportServiceǁ__init____mutmut_orig(
        self,
        transaction_repository: TransactionRepository,
        category_repository: CategoryRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._transaction_repository = transaction_repository
        self._category_repository = category_repository
        self._budget_repository = budget_repository

    def xǁReportServiceǁ__init____mutmut_1(
        self,
        transaction_repository: TransactionRepository,
        category_repository: CategoryRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._transaction_repository = None
        self._category_repository = category_repository
        self._budget_repository = budget_repository

    def xǁReportServiceǁ__init____mutmut_2(
        self,
        transaction_repository: TransactionRepository,
        category_repository: CategoryRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._transaction_repository = transaction_repository
        self._category_repository = None
        self._budget_repository = budget_repository

    def xǁReportServiceǁ__init____mutmut_3(
        self,
        transaction_repository: TransactionRepository,
        category_repository: CategoryRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._transaction_repository = transaction_repository
        self._category_repository = category_repository
        self._budget_repository = None
    
    xǁReportServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁReportServiceǁ__init____mutmut_1': xǁReportServiceǁ__init____mutmut_1, 
        'xǁReportServiceǁ__init____mutmut_2': xǁReportServiceǁ__init____mutmut_2, 
        'xǁReportServiceǁ__init____mutmut_3': xǁReportServiceǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁReportServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁReportServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁReportServiceǁ__init____mutmut_orig)
    xǁReportServiceǁ__init____mutmut_orig.__name__ = 'xǁReportServiceǁ__init__'

    async def xǁReportServiceǁmonthly_summary__mutmut_orig(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_1(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = None

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_2(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            None,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_3(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=None,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_4(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=None,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_5(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_6(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_7(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_8(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = None
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_9(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(None) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_10(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["XXcategory_idXX"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_11(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["CATEGORY_ID"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_12(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = None
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_13(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(None)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_14(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = None

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_15(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(None, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_16(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, None, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_17(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, None, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_18(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, None)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_19(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_20(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_21(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_22(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, )

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_23(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = None
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_24(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(None)
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_25(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: None)
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_26(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal(None))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_27(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("XX0XX"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_28(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = None

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_29(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = None
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_30(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(None)
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_31(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["XXcategory_idXX"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_32(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["CATEGORY_ID"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_33(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = None
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_34(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(None)
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_35(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["XXtransaction_typeXX"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_36(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["TRANSACTION_TYPE"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_37(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = None
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_38(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(None)
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_39(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(None))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_40(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["XXtotalXX"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_41(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["TOTAL"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_42(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = None

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_43(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(None)

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_44(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get(None, 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_45(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", None))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_46(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get(0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_47(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", ))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_48(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("XXcountXX", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_49(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("COUNT", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_50(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 1))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_51(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = None
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_52(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(None)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_53(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is not None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_54(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    None,
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_55(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context=None,
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_56(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_57(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_58(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "XXCategory not found while building reportXX",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_59(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_60(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "CATEGORY NOT FOUND WHILE BUILDING REPORT",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_61(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"XXcategory_idXX": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_62(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"CATEGORY_ID": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_63(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = None
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_64(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(None)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_65(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_66(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = ""
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_67(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_68(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = None

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_69(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount + total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_70(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                None
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_71(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=None,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_72(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=None,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_73(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=None,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_74(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=None,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_75(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=None,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_76(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=None,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_77(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=None,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_78(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_79(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_80(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_81(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_82(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_83(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_84(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_85(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] = total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_86(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] -= total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_87(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=None,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_88(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=None,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_89(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=None,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_90(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=None,
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_91(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=None,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_92(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_93(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            month=month,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_94(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            totals_by_type=dict(totals_by_type),
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_95(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            categories=category_summaries,
        )

    async def xǁReportServiceǁmonthly_summary__mutmut_96(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(totals_by_type),
            )

    async def xǁReportServiceǁmonthly_summary__mutmut_97(self, user_id: str, year: int, month: int) -> MonthlySummary:
        """Return aggregated totals grouped by category and transaction type."""
        raw_summary = await self._transaction_repository.aggregate_monthly_summary(
            user_id,
            year=year,
            month=month,
        )

        category_ids = {str(item["category_id"]) for item in raw_summary}
        categories = await self._fetch_categories(category_ids)
        budgets = await self._fetch_budgets(user_id, category_ids, year, month)

        totals_by_type: Dict[TransactionType, Decimal] = defaultdict(lambda: Decimal("0"))
        category_summaries: List[MonthlyCategorySummary] = []

        for item in raw_summary:
            category_id = str(item["category_id"])
            transaction_type = TransactionType(item["transaction_type"])
            total = Decimal(str(item["total"]))
            count = int(item.get("count", 0))

            category = categories.get(category_id)
            if category is None:
                raise EntityNotFoundError(
                    "Category not found while building report",
                    context={"category_id": category_id},
                )

            budget = budgets.get(category_id)
            budget_amount = budget.amount if budget else None
            budget_remaining = None
            if budget_amount is not None:
                budget_remaining = budget_amount - total

            category_summaries.append(
                MonthlyCategorySummary(
                    category_id=category_id,
                    name=category.name,
                    transaction_type=transaction_type,
                    total=total,
                    count=count,
                    budget_amount=budget_amount,
                    budget_remaining=budget_remaining,
                )
            )

            totals_by_type[transaction_type] += total

        return MonthlySummary(
            user_id=user_id,
            year=year,
            month=month,
            totals_by_type=dict(None),
            categories=category_summaries,
        )
    
    xǁReportServiceǁmonthly_summary__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁReportServiceǁmonthly_summary__mutmut_1': xǁReportServiceǁmonthly_summary__mutmut_1, 
        'xǁReportServiceǁmonthly_summary__mutmut_2': xǁReportServiceǁmonthly_summary__mutmut_2, 
        'xǁReportServiceǁmonthly_summary__mutmut_3': xǁReportServiceǁmonthly_summary__mutmut_3, 
        'xǁReportServiceǁmonthly_summary__mutmut_4': xǁReportServiceǁmonthly_summary__mutmut_4, 
        'xǁReportServiceǁmonthly_summary__mutmut_5': xǁReportServiceǁmonthly_summary__mutmut_5, 
        'xǁReportServiceǁmonthly_summary__mutmut_6': xǁReportServiceǁmonthly_summary__mutmut_6, 
        'xǁReportServiceǁmonthly_summary__mutmut_7': xǁReportServiceǁmonthly_summary__mutmut_7, 
        'xǁReportServiceǁmonthly_summary__mutmut_8': xǁReportServiceǁmonthly_summary__mutmut_8, 
        'xǁReportServiceǁmonthly_summary__mutmut_9': xǁReportServiceǁmonthly_summary__mutmut_9, 
        'xǁReportServiceǁmonthly_summary__mutmut_10': xǁReportServiceǁmonthly_summary__mutmut_10, 
        'xǁReportServiceǁmonthly_summary__mutmut_11': xǁReportServiceǁmonthly_summary__mutmut_11, 
        'xǁReportServiceǁmonthly_summary__mutmut_12': xǁReportServiceǁmonthly_summary__mutmut_12, 
        'xǁReportServiceǁmonthly_summary__mutmut_13': xǁReportServiceǁmonthly_summary__mutmut_13, 
        'xǁReportServiceǁmonthly_summary__mutmut_14': xǁReportServiceǁmonthly_summary__mutmut_14, 
        'xǁReportServiceǁmonthly_summary__mutmut_15': xǁReportServiceǁmonthly_summary__mutmut_15, 
        'xǁReportServiceǁmonthly_summary__mutmut_16': xǁReportServiceǁmonthly_summary__mutmut_16, 
        'xǁReportServiceǁmonthly_summary__mutmut_17': xǁReportServiceǁmonthly_summary__mutmut_17, 
        'xǁReportServiceǁmonthly_summary__mutmut_18': xǁReportServiceǁmonthly_summary__mutmut_18, 
        'xǁReportServiceǁmonthly_summary__mutmut_19': xǁReportServiceǁmonthly_summary__mutmut_19, 
        'xǁReportServiceǁmonthly_summary__mutmut_20': xǁReportServiceǁmonthly_summary__mutmut_20, 
        'xǁReportServiceǁmonthly_summary__mutmut_21': xǁReportServiceǁmonthly_summary__mutmut_21, 
        'xǁReportServiceǁmonthly_summary__mutmut_22': xǁReportServiceǁmonthly_summary__mutmut_22, 
        'xǁReportServiceǁmonthly_summary__mutmut_23': xǁReportServiceǁmonthly_summary__mutmut_23, 
        'xǁReportServiceǁmonthly_summary__mutmut_24': xǁReportServiceǁmonthly_summary__mutmut_24, 
        'xǁReportServiceǁmonthly_summary__mutmut_25': xǁReportServiceǁmonthly_summary__mutmut_25, 
        'xǁReportServiceǁmonthly_summary__mutmut_26': xǁReportServiceǁmonthly_summary__mutmut_26, 
        'xǁReportServiceǁmonthly_summary__mutmut_27': xǁReportServiceǁmonthly_summary__mutmut_27, 
        'xǁReportServiceǁmonthly_summary__mutmut_28': xǁReportServiceǁmonthly_summary__mutmut_28, 
        'xǁReportServiceǁmonthly_summary__mutmut_29': xǁReportServiceǁmonthly_summary__mutmut_29, 
        'xǁReportServiceǁmonthly_summary__mutmut_30': xǁReportServiceǁmonthly_summary__mutmut_30, 
        'xǁReportServiceǁmonthly_summary__mutmut_31': xǁReportServiceǁmonthly_summary__mutmut_31, 
        'xǁReportServiceǁmonthly_summary__mutmut_32': xǁReportServiceǁmonthly_summary__mutmut_32, 
        'xǁReportServiceǁmonthly_summary__mutmut_33': xǁReportServiceǁmonthly_summary__mutmut_33, 
        'xǁReportServiceǁmonthly_summary__mutmut_34': xǁReportServiceǁmonthly_summary__mutmut_34, 
        'xǁReportServiceǁmonthly_summary__mutmut_35': xǁReportServiceǁmonthly_summary__mutmut_35, 
        'xǁReportServiceǁmonthly_summary__mutmut_36': xǁReportServiceǁmonthly_summary__mutmut_36, 
        'xǁReportServiceǁmonthly_summary__mutmut_37': xǁReportServiceǁmonthly_summary__mutmut_37, 
        'xǁReportServiceǁmonthly_summary__mutmut_38': xǁReportServiceǁmonthly_summary__mutmut_38, 
        'xǁReportServiceǁmonthly_summary__mutmut_39': xǁReportServiceǁmonthly_summary__mutmut_39, 
        'xǁReportServiceǁmonthly_summary__mutmut_40': xǁReportServiceǁmonthly_summary__mutmut_40, 
        'xǁReportServiceǁmonthly_summary__mutmut_41': xǁReportServiceǁmonthly_summary__mutmut_41, 
        'xǁReportServiceǁmonthly_summary__mutmut_42': xǁReportServiceǁmonthly_summary__mutmut_42, 
        'xǁReportServiceǁmonthly_summary__mutmut_43': xǁReportServiceǁmonthly_summary__mutmut_43, 
        'xǁReportServiceǁmonthly_summary__mutmut_44': xǁReportServiceǁmonthly_summary__mutmut_44, 
        'xǁReportServiceǁmonthly_summary__mutmut_45': xǁReportServiceǁmonthly_summary__mutmut_45, 
        'xǁReportServiceǁmonthly_summary__mutmut_46': xǁReportServiceǁmonthly_summary__mutmut_46, 
        'xǁReportServiceǁmonthly_summary__mutmut_47': xǁReportServiceǁmonthly_summary__mutmut_47, 
        'xǁReportServiceǁmonthly_summary__mutmut_48': xǁReportServiceǁmonthly_summary__mutmut_48, 
        'xǁReportServiceǁmonthly_summary__mutmut_49': xǁReportServiceǁmonthly_summary__mutmut_49, 
        'xǁReportServiceǁmonthly_summary__mutmut_50': xǁReportServiceǁmonthly_summary__mutmut_50, 
        'xǁReportServiceǁmonthly_summary__mutmut_51': xǁReportServiceǁmonthly_summary__mutmut_51, 
        'xǁReportServiceǁmonthly_summary__mutmut_52': xǁReportServiceǁmonthly_summary__mutmut_52, 
        'xǁReportServiceǁmonthly_summary__mutmut_53': xǁReportServiceǁmonthly_summary__mutmut_53, 
        'xǁReportServiceǁmonthly_summary__mutmut_54': xǁReportServiceǁmonthly_summary__mutmut_54, 
        'xǁReportServiceǁmonthly_summary__mutmut_55': xǁReportServiceǁmonthly_summary__mutmut_55, 
        'xǁReportServiceǁmonthly_summary__mutmut_56': xǁReportServiceǁmonthly_summary__mutmut_56, 
        'xǁReportServiceǁmonthly_summary__mutmut_57': xǁReportServiceǁmonthly_summary__mutmut_57, 
        'xǁReportServiceǁmonthly_summary__mutmut_58': xǁReportServiceǁmonthly_summary__mutmut_58, 
        'xǁReportServiceǁmonthly_summary__mutmut_59': xǁReportServiceǁmonthly_summary__mutmut_59, 
        'xǁReportServiceǁmonthly_summary__mutmut_60': xǁReportServiceǁmonthly_summary__mutmut_60, 
        'xǁReportServiceǁmonthly_summary__mutmut_61': xǁReportServiceǁmonthly_summary__mutmut_61, 
        'xǁReportServiceǁmonthly_summary__mutmut_62': xǁReportServiceǁmonthly_summary__mutmut_62, 
        'xǁReportServiceǁmonthly_summary__mutmut_63': xǁReportServiceǁmonthly_summary__mutmut_63, 
        'xǁReportServiceǁmonthly_summary__mutmut_64': xǁReportServiceǁmonthly_summary__mutmut_64, 
        'xǁReportServiceǁmonthly_summary__mutmut_65': xǁReportServiceǁmonthly_summary__mutmut_65, 
        'xǁReportServiceǁmonthly_summary__mutmut_66': xǁReportServiceǁmonthly_summary__mutmut_66, 
        'xǁReportServiceǁmonthly_summary__mutmut_67': xǁReportServiceǁmonthly_summary__mutmut_67, 
        'xǁReportServiceǁmonthly_summary__mutmut_68': xǁReportServiceǁmonthly_summary__mutmut_68, 
        'xǁReportServiceǁmonthly_summary__mutmut_69': xǁReportServiceǁmonthly_summary__mutmut_69, 
        'xǁReportServiceǁmonthly_summary__mutmut_70': xǁReportServiceǁmonthly_summary__mutmut_70, 
        'xǁReportServiceǁmonthly_summary__mutmut_71': xǁReportServiceǁmonthly_summary__mutmut_71, 
        'xǁReportServiceǁmonthly_summary__mutmut_72': xǁReportServiceǁmonthly_summary__mutmut_72, 
        'xǁReportServiceǁmonthly_summary__mutmut_73': xǁReportServiceǁmonthly_summary__mutmut_73, 
        'xǁReportServiceǁmonthly_summary__mutmut_74': xǁReportServiceǁmonthly_summary__mutmut_74, 
        'xǁReportServiceǁmonthly_summary__mutmut_75': xǁReportServiceǁmonthly_summary__mutmut_75, 
        'xǁReportServiceǁmonthly_summary__mutmut_76': xǁReportServiceǁmonthly_summary__mutmut_76, 
        'xǁReportServiceǁmonthly_summary__mutmut_77': xǁReportServiceǁmonthly_summary__mutmut_77, 
        'xǁReportServiceǁmonthly_summary__mutmut_78': xǁReportServiceǁmonthly_summary__mutmut_78, 
        'xǁReportServiceǁmonthly_summary__mutmut_79': xǁReportServiceǁmonthly_summary__mutmut_79, 
        'xǁReportServiceǁmonthly_summary__mutmut_80': xǁReportServiceǁmonthly_summary__mutmut_80, 
        'xǁReportServiceǁmonthly_summary__mutmut_81': xǁReportServiceǁmonthly_summary__mutmut_81, 
        'xǁReportServiceǁmonthly_summary__mutmut_82': xǁReportServiceǁmonthly_summary__mutmut_82, 
        'xǁReportServiceǁmonthly_summary__mutmut_83': xǁReportServiceǁmonthly_summary__mutmut_83, 
        'xǁReportServiceǁmonthly_summary__mutmut_84': xǁReportServiceǁmonthly_summary__mutmut_84, 
        'xǁReportServiceǁmonthly_summary__mutmut_85': xǁReportServiceǁmonthly_summary__mutmut_85, 
        'xǁReportServiceǁmonthly_summary__mutmut_86': xǁReportServiceǁmonthly_summary__mutmut_86, 
        'xǁReportServiceǁmonthly_summary__mutmut_87': xǁReportServiceǁmonthly_summary__mutmut_87, 
        'xǁReportServiceǁmonthly_summary__mutmut_88': xǁReportServiceǁmonthly_summary__mutmut_88, 
        'xǁReportServiceǁmonthly_summary__mutmut_89': xǁReportServiceǁmonthly_summary__mutmut_89, 
        'xǁReportServiceǁmonthly_summary__mutmut_90': xǁReportServiceǁmonthly_summary__mutmut_90, 
        'xǁReportServiceǁmonthly_summary__mutmut_91': xǁReportServiceǁmonthly_summary__mutmut_91, 
        'xǁReportServiceǁmonthly_summary__mutmut_92': xǁReportServiceǁmonthly_summary__mutmut_92, 
        'xǁReportServiceǁmonthly_summary__mutmut_93': xǁReportServiceǁmonthly_summary__mutmut_93, 
        'xǁReportServiceǁmonthly_summary__mutmut_94': xǁReportServiceǁmonthly_summary__mutmut_94, 
        'xǁReportServiceǁmonthly_summary__mutmut_95': xǁReportServiceǁmonthly_summary__mutmut_95, 
        'xǁReportServiceǁmonthly_summary__mutmut_96': xǁReportServiceǁmonthly_summary__mutmut_96, 
        'xǁReportServiceǁmonthly_summary__mutmut_97': xǁReportServiceǁmonthly_summary__mutmut_97
    }
    
    def monthly_summary(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁReportServiceǁmonthly_summary__mutmut_orig"), object.__getattribute__(self, "xǁReportServiceǁmonthly_summary__mutmut_mutants"), args, kwargs, self)
        return result 
    
    monthly_summary.__signature__ = _mutmut_signature(xǁReportServiceǁmonthly_summary__mutmut_orig)
    xǁReportServiceǁmonthly_summary__mutmut_orig.__name__ = 'xǁReportServiceǁmonthly_summary'

    async def xǁReportServiceǁ_fetch_categories__mutmut_orig(self, category_ids: set[str]):
        result: Dict[str, object] = {}
        for category_id in category_ids:
            category = await self._category_repository.get(category_id)
            if category:
                result[category_id] = category
        return result

    async def xǁReportServiceǁ_fetch_categories__mutmut_1(self, category_ids: set[str]):
        result: Dict[str, object] = None
        for category_id in category_ids:
            category = await self._category_repository.get(category_id)
            if category:
                result[category_id] = category
        return result

    async def xǁReportServiceǁ_fetch_categories__mutmut_2(self, category_ids: set[str]):
        result: Dict[str, object] = {}
        for category_id in category_ids:
            category = None
            if category:
                result[category_id] = category
        return result

    async def xǁReportServiceǁ_fetch_categories__mutmut_3(self, category_ids: set[str]):
        result: Dict[str, object] = {}
        for category_id in category_ids:
            category = await self._category_repository.get(None)
            if category:
                result[category_id] = category
        return result

    async def xǁReportServiceǁ_fetch_categories__mutmut_4(self, category_ids: set[str]):
        result: Dict[str, object] = {}
        for category_id in category_ids:
            category = await self._category_repository.get(category_id)
            if category:
                result[category_id] = None
        return result
    
    xǁReportServiceǁ_fetch_categories__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁReportServiceǁ_fetch_categories__mutmut_1': xǁReportServiceǁ_fetch_categories__mutmut_1, 
        'xǁReportServiceǁ_fetch_categories__mutmut_2': xǁReportServiceǁ_fetch_categories__mutmut_2, 
        'xǁReportServiceǁ_fetch_categories__mutmut_3': xǁReportServiceǁ_fetch_categories__mutmut_3, 
        'xǁReportServiceǁ_fetch_categories__mutmut_4': xǁReportServiceǁ_fetch_categories__mutmut_4
    }
    
    def _fetch_categories(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁReportServiceǁ_fetch_categories__mutmut_orig"), object.__getattribute__(self, "xǁReportServiceǁ_fetch_categories__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _fetch_categories.__signature__ = _mutmut_signature(xǁReportServiceǁ_fetch_categories__mutmut_orig)
    xǁReportServiceǁ_fetch_categories__mutmut_orig.__name__ = 'xǁReportServiceǁ_fetch_categories'

    async def xǁReportServiceǁ_fetch_budgets__mutmut_orig(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_1(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = None
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_2(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=None,
            year=year,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_3(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=None,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_4(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            month=None,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_5(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            year=year,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_6(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_7(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_8(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            month=month,
        )
        result: Dict[str, object] = None
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_9(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id not in category_ids:
                result[budget.category_id] = budget
        return result

    async def xǁReportServiceǁ_fetch_budgets__mutmut_10(
        self,
        user_id: str,
        category_ids: set[str],
        year: int,
        month: int,
    ) -> Dict[str, object]:
        budgets = await self._budget_repository.list(
            user_id=user_id,
            year=year,
            month=month,
        )
        result: Dict[str, object] = {}
        for budget in budgets:
            if budget.category_id in category_ids:
                result[budget.category_id] = None
        return result
    
    xǁReportServiceǁ_fetch_budgets__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁReportServiceǁ_fetch_budgets__mutmut_1': xǁReportServiceǁ_fetch_budgets__mutmut_1, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_2': xǁReportServiceǁ_fetch_budgets__mutmut_2, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_3': xǁReportServiceǁ_fetch_budgets__mutmut_3, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_4': xǁReportServiceǁ_fetch_budgets__mutmut_4, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_5': xǁReportServiceǁ_fetch_budgets__mutmut_5, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_6': xǁReportServiceǁ_fetch_budgets__mutmut_6, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_7': xǁReportServiceǁ_fetch_budgets__mutmut_7, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_8': xǁReportServiceǁ_fetch_budgets__mutmut_8, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_9': xǁReportServiceǁ_fetch_budgets__mutmut_9, 
        'xǁReportServiceǁ_fetch_budgets__mutmut_10': xǁReportServiceǁ_fetch_budgets__mutmut_10
    }
    
    def _fetch_budgets(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁReportServiceǁ_fetch_budgets__mutmut_orig"), object.__getattribute__(self, "xǁReportServiceǁ_fetch_budgets__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _fetch_budgets.__signature__ = _mutmut_signature(xǁReportServiceǁ_fetch_budgets__mutmut_orig)
    xǁReportServiceǁ_fetch_budgets__mutmut_orig.__name__ = 'xǁReportServiceǁ_fetch_budgets'
