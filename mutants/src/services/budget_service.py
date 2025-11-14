"""Business logic for managing budgets."""

from __future__ import annotations

from typing import List

from src.models.budget import Budget, BudgetCreate, BudgetUpdate, build_budget
from src.models.enums import CategoryType
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
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


class BudgetService:
    """Encapsulates budget workflows and validations."""

    def xǁBudgetServiceǁ__init____mutmut_orig(
        self,
        repository: BudgetRepository,
        user_repository: UserRepository,
        category_repository: CategoryRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._category_repository = category_repository
        self._transaction_repository = transaction_repository

    def xǁBudgetServiceǁ__init____mutmut_1(
        self,
        repository: BudgetRepository,
        user_repository: UserRepository,
        category_repository: CategoryRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = None
        self._user_repository = user_repository
        self._category_repository = category_repository
        self._transaction_repository = transaction_repository

    def xǁBudgetServiceǁ__init____mutmut_2(
        self,
        repository: BudgetRepository,
        user_repository: UserRepository,
        category_repository: CategoryRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = None
        self._category_repository = category_repository
        self._transaction_repository = transaction_repository

    def xǁBudgetServiceǁ__init____mutmut_3(
        self,
        repository: BudgetRepository,
        user_repository: UserRepository,
        category_repository: CategoryRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._category_repository = None
        self._transaction_repository = transaction_repository

    def xǁBudgetServiceǁ__init____mutmut_4(
        self,
        repository: BudgetRepository,
        user_repository: UserRepository,
        category_repository: CategoryRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._category_repository = category_repository
        self._transaction_repository = None
    
    xǁBudgetServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁ__init____mutmut_1': xǁBudgetServiceǁ__init____mutmut_1, 
        'xǁBudgetServiceǁ__init____mutmut_2': xǁBudgetServiceǁ__init____mutmut_2, 
        'xǁBudgetServiceǁ__init____mutmut_3': xǁBudgetServiceǁ__init____mutmut_3, 
        'xǁBudgetServiceǁ__init____mutmut_4': xǁBudgetServiceǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBudgetServiceǁ__init____mutmut_orig)
    xǁBudgetServiceǁ__init____mutmut_orig.__name__ = 'xǁBudgetServiceǁ__init__'

    async def xǁBudgetServiceǁcreate_budget__mutmut_orig(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_1(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(None)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_2(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = None
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_3(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(None)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_4(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(None, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_5(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, None, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_6(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, None)
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_7(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_8(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_9(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, )
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_10(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "XXcategoryXX")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_11(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "CATEGORY")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_12(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(None)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_13(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = None
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_14(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=None,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_15(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=None,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_16(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=None,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_17(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=None,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_18(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_19(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_20(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_21(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_22(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                None,
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_23(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context=None,
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_24(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_25(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_26(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "XXBudget already defined for this category and periodXX",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_27(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_28(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "BUDGET ALREADY DEFINED FOR THIS CATEGORY AND PERIOD",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_29(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "XXcategory_idXX": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_30(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "CATEGORY_ID": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_31(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "XXyearXX": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_32(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "YEAR": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_33(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "XXmonthXX": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_34(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "MONTH": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_35(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = None
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_36(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(None)
        await self._repository.create(budget)
        return budget

    async def xǁBudgetServiceǁcreate_budget__mutmut_37(self, payload: BudgetCreate) -> Budget:
        """Create a budget ensuring uniqueness and category rules."""
        await self._ensure_user_exists(payload.user_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._ensure_category_is_expense(category.category_type)

        existing = await self._repository.find_by_period(
            user_id=payload.user_id,
            category_id=payload.category_id,
            year=payload.year,
            month=payload.month,
        )
        if existing:
            raise EntityAlreadyExistsError(
                "Budget already defined for this category and period",
                context={
                    "category_id": payload.category_id,
                    "year": payload.year,
                    "month": payload.month,
                },
            )

        budget = build_budget(payload)
        await self._repository.create(None)
        return budget
    
    xǁBudgetServiceǁcreate_budget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁcreate_budget__mutmut_1': xǁBudgetServiceǁcreate_budget__mutmut_1, 
        'xǁBudgetServiceǁcreate_budget__mutmut_2': xǁBudgetServiceǁcreate_budget__mutmut_2, 
        'xǁBudgetServiceǁcreate_budget__mutmut_3': xǁBudgetServiceǁcreate_budget__mutmut_3, 
        'xǁBudgetServiceǁcreate_budget__mutmut_4': xǁBudgetServiceǁcreate_budget__mutmut_4, 
        'xǁBudgetServiceǁcreate_budget__mutmut_5': xǁBudgetServiceǁcreate_budget__mutmut_5, 
        'xǁBudgetServiceǁcreate_budget__mutmut_6': xǁBudgetServiceǁcreate_budget__mutmut_6, 
        'xǁBudgetServiceǁcreate_budget__mutmut_7': xǁBudgetServiceǁcreate_budget__mutmut_7, 
        'xǁBudgetServiceǁcreate_budget__mutmut_8': xǁBudgetServiceǁcreate_budget__mutmut_8, 
        'xǁBudgetServiceǁcreate_budget__mutmut_9': xǁBudgetServiceǁcreate_budget__mutmut_9, 
        'xǁBudgetServiceǁcreate_budget__mutmut_10': xǁBudgetServiceǁcreate_budget__mutmut_10, 
        'xǁBudgetServiceǁcreate_budget__mutmut_11': xǁBudgetServiceǁcreate_budget__mutmut_11, 
        'xǁBudgetServiceǁcreate_budget__mutmut_12': xǁBudgetServiceǁcreate_budget__mutmut_12, 
        'xǁBudgetServiceǁcreate_budget__mutmut_13': xǁBudgetServiceǁcreate_budget__mutmut_13, 
        'xǁBudgetServiceǁcreate_budget__mutmut_14': xǁBudgetServiceǁcreate_budget__mutmut_14, 
        'xǁBudgetServiceǁcreate_budget__mutmut_15': xǁBudgetServiceǁcreate_budget__mutmut_15, 
        'xǁBudgetServiceǁcreate_budget__mutmut_16': xǁBudgetServiceǁcreate_budget__mutmut_16, 
        'xǁBudgetServiceǁcreate_budget__mutmut_17': xǁBudgetServiceǁcreate_budget__mutmut_17, 
        'xǁBudgetServiceǁcreate_budget__mutmut_18': xǁBudgetServiceǁcreate_budget__mutmut_18, 
        'xǁBudgetServiceǁcreate_budget__mutmut_19': xǁBudgetServiceǁcreate_budget__mutmut_19, 
        'xǁBudgetServiceǁcreate_budget__mutmut_20': xǁBudgetServiceǁcreate_budget__mutmut_20, 
        'xǁBudgetServiceǁcreate_budget__mutmut_21': xǁBudgetServiceǁcreate_budget__mutmut_21, 
        'xǁBudgetServiceǁcreate_budget__mutmut_22': xǁBudgetServiceǁcreate_budget__mutmut_22, 
        'xǁBudgetServiceǁcreate_budget__mutmut_23': xǁBudgetServiceǁcreate_budget__mutmut_23, 
        'xǁBudgetServiceǁcreate_budget__mutmut_24': xǁBudgetServiceǁcreate_budget__mutmut_24, 
        'xǁBudgetServiceǁcreate_budget__mutmut_25': xǁBudgetServiceǁcreate_budget__mutmut_25, 
        'xǁBudgetServiceǁcreate_budget__mutmut_26': xǁBudgetServiceǁcreate_budget__mutmut_26, 
        'xǁBudgetServiceǁcreate_budget__mutmut_27': xǁBudgetServiceǁcreate_budget__mutmut_27, 
        'xǁBudgetServiceǁcreate_budget__mutmut_28': xǁBudgetServiceǁcreate_budget__mutmut_28, 
        'xǁBudgetServiceǁcreate_budget__mutmut_29': xǁBudgetServiceǁcreate_budget__mutmut_29, 
        'xǁBudgetServiceǁcreate_budget__mutmut_30': xǁBudgetServiceǁcreate_budget__mutmut_30, 
        'xǁBudgetServiceǁcreate_budget__mutmut_31': xǁBudgetServiceǁcreate_budget__mutmut_31, 
        'xǁBudgetServiceǁcreate_budget__mutmut_32': xǁBudgetServiceǁcreate_budget__mutmut_32, 
        'xǁBudgetServiceǁcreate_budget__mutmut_33': xǁBudgetServiceǁcreate_budget__mutmut_33, 
        'xǁBudgetServiceǁcreate_budget__mutmut_34': xǁBudgetServiceǁcreate_budget__mutmut_34, 
        'xǁBudgetServiceǁcreate_budget__mutmut_35': xǁBudgetServiceǁcreate_budget__mutmut_35, 
        'xǁBudgetServiceǁcreate_budget__mutmut_36': xǁBudgetServiceǁcreate_budget__mutmut_36, 
        'xǁBudgetServiceǁcreate_budget__mutmut_37': xǁBudgetServiceǁcreate_budget__mutmut_37
    }
    
    def create_budget(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁcreate_budget__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁcreate_budget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_budget.__signature__ = _mutmut_signature(xǁBudgetServiceǁcreate_budget__mutmut_orig)
    xǁBudgetServiceǁcreate_budget__mutmut_orig.__name__ = 'xǁBudgetServiceǁcreate_budget'

    async def xǁBudgetServiceǁlist_budgets__mutmut_orig(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_1(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = None
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_2(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = None
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_3(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["XXuser_idXX"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_4(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["USER_ID"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_5(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = None
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_6(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["XXcategory_idXX"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_7(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["CATEGORY_ID"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_8(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_9(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = None
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_10(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["XXyearXX"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_11(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["YEAR"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_12(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_13(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = None
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_14(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["XXmonthXX"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_15(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["MONTH"] = month
        budgets = await self._repository.list(**filters)
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_16(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = None
        return list(budgets)

    async def xǁBudgetServiceǁlist_budgets__mutmut_17(
        self,
        *,
        user_id: str | None = None,
        category_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> List[Budget]:
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_id:
            filters["category_id"] = category_id
        if year is not None:
            filters["year"] = year
        if month is not None:
            filters["month"] = month
        budgets = await self._repository.list(**filters)
        return list(None)
    
    xǁBudgetServiceǁlist_budgets__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁlist_budgets__mutmut_1': xǁBudgetServiceǁlist_budgets__mutmut_1, 
        'xǁBudgetServiceǁlist_budgets__mutmut_2': xǁBudgetServiceǁlist_budgets__mutmut_2, 
        'xǁBudgetServiceǁlist_budgets__mutmut_3': xǁBudgetServiceǁlist_budgets__mutmut_3, 
        'xǁBudgetServiceǁlist_budgets__mutmut_4': xǁBudgetServiceǁlist_budgets__mutmut_4, 
        'xǁBudgetServiceǁlist_budgets__mutmut_5': xǁBudgetServiceǁlist_budgets__mutmut_5, 
        'xǁBudgetServiceǁlist_budgets__mutmut_6': xǁBudgetServiceǁlist_budgets__mutmut_6, 
        'xǁBudgetServiceǁlist_budgets__mutmut_7': xǁBudgetServiceǁlist_budgets__mutmut_7, 
        'xǁBudgetServiceǁlist_budgets__mutmut_8': xǁBudgetServiceǁlist_budgets__mutmut_8, 
        'xǁBudgetServiceǁlist_budgets__mutmut_9': xǁBudgetServiceǁlist_budgets__mutmut_9, 
        'xǁBudgetServiceǁlist_budgets__mutmut_10': xǁBudgetServiceǁlist_budgets__mutmut_10, 
        'xǁBudgetServiceǁlist_budgets__mutmut_11': xǁBudgetServiceǁlist_budgets__mutmut_11, 
        'xǁBudgetServiceǁlist_budgets__mutmut_12': xǁBudgetServiceǁlist_budgets__mutmut_12, 
        'xǁBudgetServiceǁlist_budgets__mutmut_13': xǁBudgetServiceǁlist_budgets__mutmut_13, 
        'xǁBudgetServiceǁlist_budgets__mutmut_14': xǁBudgetServiceǁlist_budgets__mutmut_14, 
        'xǁBudgetServiceǁlist_budgets__mutmut_15': xǁBudgetServiceǁlist_budgets__mutmut_15, 
        'xǁBudgetServiceǁlist_budgets__mutmut_16': xǁBudgetServiceǁlist_budgets__mutmut_16, 
        'xǁBudgetServiceǁlist_budgets__mutmut_17': xǁBudgetServiceǁlist_budgets__mutmut_17
    }
    
    def list_budgets(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁlist_budgets__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁlist_budgets__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_budgets.__signature__ = _mutmut_signature(xǁBudgetServiceǁlist_budgets__mutmut_orig)
    xǁBudgetServiceǁlist_budgets__mutmut_orig.__name__ = 'xǁBudgetServiceǁlist_budgets'

    async def xǁBudgetServiceǁget_budget__mutmut_orig(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_1(self, budget_id: str) -> Budget:
        budget = None
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_2(self, budget_id: str) -> Budget:
        budget = await self._repository.get(None)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_3(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is not None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_4(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError(None, context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_5(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context=None)
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_6(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError(context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_7(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("Budget not found", )
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_8(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("XXBudget not foundXX", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_9(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_10(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("BUDGET NOT FOUND", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_11(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"XXidXX": budget_id})
        return budget

    async def xǁBudgetServiceǁget_budget__mutmut_12(self, budget_id: str) -> Budget:
        budget = await self._repository.get(budget_id)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"ID": budget_id})
        return budget
    
    xǁBudgetServiceǁget_budget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁget_budget__mutmut_1': xǁBudgetServiceǁget_budget__mutmut_1, 
        'xǁBudgetServiceǁget_budget__mutmut_2': xǁBudgetServiceǁget_budget__mutmut_2, 
        'xǁBudgetServiceǁget_budget__mutmut_3': xǁBudgetServiceǁget_budget__mutmut_3, 
        'xǁBudgetServiceǁget_budget__mutmut_4': xǁBudgetServiceǁget_budget__mutmut_4, 
        'xǁBudgetServiceǁget_budget__mutmut_5': xǁBudgetServiceǁget_budget__mutmut_5, 
        'xǁBudgetServiceǁget_budget__mutmut_6': xǁBudgetServiceǁget_budget__mutmut_6, 
        'xǁBudgetServiceǁget_budget__mutmut_7': xǁBudgetServiceǁget_budget__mutmut_7, 
        'xǁBudgetServiceǁget_budget__mutmut_8': xǁBudgetServiceǁget_budget__mutmut_8, 
        'xǁBudgetServiceǁget_budget__mutmut_9': xǁBudgetServiceǁget_budget__mutmut_9, 
        'xǁBudgetServiceǁget_budget__mutmut_10': xǁBudgetServiceǁget_budget__mutmut_10, 
        'xǁBudgetServiceǁget_budget__mutmut_11': xǁBudgetServiceǁget_budget__mutmut_11, 
        'xǁBudgetServiceǁget_budget__mutmut_12': xǁBudgetServiceǁget_budget__mutmut_12
    }
    
    def get_budget(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁget_budget__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁget_budget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_budget.__signature__ = _mutmut_signature(xǁBudgetServiceǁget_budget__mutmut_orig)
    xǁBudgetServiceǁget_budget__mutmut_orig.__name__ = 'xǁBudgetServiceǁget_budget'

    async def xǁBudgetServiceǁupdate_budget__mutmut_orig(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_1(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = None
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_2(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=None, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_3(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=None)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_4(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_5(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, )
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_6(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=False, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_7(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=False)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_8(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_9(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                None,
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_10(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context=None,
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_11(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_12(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_13(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "XXNo data provided to update budgetXX",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_14(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "no data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_15(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "NO DATA PROVIDED TO UPDATE BUDGET",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_16(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"XXidXX": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_17(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"ID": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_18(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = None
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_19(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(None, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_20(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, None)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_21(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_22(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, )
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_23(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is not None:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_24(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError(None, context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_25(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context=None)
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_26(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError(context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_27(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", )
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_28(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("XXBudget not foundXX", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_29(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("budget not found", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_30(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("BUDGET NOT FOUND", context={"id": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_31(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"XXidXX": budget_id})
        return budget

    async def xǁBudgetServiceǁupdate_budget__mutmut_32(self, budget_id: str, payload: BudgetUpdate) -> Budget:
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update budget",
                context={"id": budget_id},
            )
        budget = await self._repository.update(budget_id, updates)
        if budget is None:
            raise EntityNotFoundError("Budget not found", context={"ID": budget_id})
        return budget
    
    xǁBudgetServiceǁupdate_budget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁupdate_budget__mutmut_1': xǁBudgetServiceǁupdate_budget__mutmut_1, 
        'xǁBudgetServiceǁupdate_budget__mutmut_2': xǁBudgetServiceǁupdate_budget__mutmut_2, 
        'xǁBudgetServiceǁupdate_budget__mutmut_3': xǁBudgetServiceǁupdate_budget__mutmut_3, 
        'xǁBudgetServiceǁupdate_budget__mutmut_4': xǁBudgetServiceǁupdate_budget__mutmut_4, 
        'xǁBudgetServiceǁupdate_budget__mutmut_5': xǁBudgetServiceǁupdate_budget__mutmut_5, 
        'xǁBudgetServiceǁupdate_budget__mutmut_6': xǁBudgetServiceǁupdate_budget__mutmut_6, 
        'xǁBudgetServiceǁupdate_budget__mutmut_7': xǁBudgetServiceǁupdate_budget__mutmut_7, 
        'xǁBudgetServiceǁupdate_budget__mutmut_8': xǁBudgetServiceǁupdate_budget__mutmut_8, 
        'xǁBudgetServiceǁupdate_budget__mutmut_9': xǁBudgetServiceǁupdate_budget__mutmut_9, 
        'xǁBudgetServiceǁupdate_budget__mutmut_10': xǁBudgetServiceǁupdate_budget__mutmut_10, 
        'xǁBudgetServiceǁupdate_budget__mutmut_11': xǁBudgetServiceǁupdate_budget__mutmut_11, 
        'xǁBudgetServiceǁupdate_budget__mutmut_12': xǁBudgetServiceǁupdate_budget__mutmut_12, 
        'xǁBudgetServiceǁupdate_budget__mutmut_13': xǁBudgetServiceǁupdate_budget__mutmut_13, 
        'xǁBudgetServiceǁupdate_budget__mutmut_14': xǁBudgetServiceǁupdate_budget__mutmut_14, 
        'xǁBudgetServiceǁupdate_budget__mutmut_15': xǁBudgetServiceǁupdate_budget__mutmut_15, 
        'xǁBudgetServiceǁupdate_budget__mutmut_16': xǁBudgetServiceǁupdate_budget__mutmut_16, 
        'xǁBudgetServiceǁupdate_budget__mutmut_17': xǁBudgetServiceǁupdate_budget__mutmut_17, 
        'xǁBudgetServiceǁupdate_budget__mutmut_18': xǁBudgetServiceǁupdate_budget__mutmut_18, 
        'xǁBudgetServiceǁupdate_budget__mutmut_19': xǁBudgetServiceǁupdate_budget__mutmut_19, 
        'xǁBudgetServiceǁupdate_budget__mutmut_20': xǁBudgetServiceǁupdate_budget__mutmut_20, 
        'xǁBudgetServiceǁupdate_budget__mutmut_21': xǁBudgetServiceǁupdate_budget__mutmut_21, 
        'xǁBudgetServiceǁupdate_budget__mutmut_22': xǁBudgetServiceǁupdate_budget__mutmut_22, 
        'xǁBudgetServiceǁupdate_budget__mutmut_23': xǁBudgetServiceǁupdate_budget__mutmut_23, 
        'xǁBudgetServiceǁupdate_budget__mutmut_24': xǁBudgetServiceǁupdate_budget__mutmut_24, 
        'xǁBudgetServiceǁupdate_budget__mutmut_25': xǁBudgetServiceǁupdate_budget__mutmut_25, 
        'xǁBudgetServiceǁupdate_budget__mutmut_26': xǁBudgetServiceǁupdate_budget__mutmut_26, 
        'xǁBudgetServiceǁupdate_budget__mutmut_27': xǁBudgetServiceǁupdate_budget__mutmut_27, 
        'xǁBudgetServiceǁupdate_budget__mutmut_28': xǁBudgetServiceǁupdate_budget__mutmut_28, 
        'xǁBudgetServiceǁupdate_budget__mutmut_29': xǁBudgetServiceǁupdate_budget__mutmut_29, 
        'xǁBudgetServiceǁupdate_budget__mutmut_30': xǁBudgetServiceǁupdate_budget__mutmut_30, 
        'xǁBudgetServiceǁupdate_budget__mutmut_31': xǁBudgetServiceǁupdate_budget__mutmut_31, 
        'xǁBudgetServiceǁupdate_budget__mutmut_32': xǁBudgetServiceǁupdate_budget__mutmut_32
    }
    
    def update_budget(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁupdate_budget__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁupdate_budget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_budget.__signature__ = _mutmut_signature(xǁBudgetServiceǁupdate_budget__mutmut_orig)
    xǁBudgetServiceǁupdate_budget__mutmut_orig.__name__ = 'xǁBudgetServiceǁupdate_budget'

    async def xǁBudgetServiceǁdelete_budget__mutmut_orig(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_1(self, budget_id: str) -> None:
        budget = None
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_2(self, budget_id: str) -> None:
        budget = await self.get_budget(None)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_3(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = None
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_4(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            None,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_5(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=None,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_6(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=None,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_7(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=None,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_8(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_9(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_10(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_11(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_12(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                None,
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_13(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context=None,
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_14(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_15(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_16(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "XXCannot delete budget with transactions in the same periodXX",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_17(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_18(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "CANNOT DELETE BUDGET WITH TRANSACTIONS IN THE SAME PERIOD",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_19(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "XXcategory_idXX": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_20(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "CATEGORY_ID": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_21(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "XXyearXX": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_22(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "YEAR": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_23(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "XXmonthXX": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_24(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "MONTH": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_25(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = None
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_26(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(None)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_27(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if deleted:
            raise EntityNotFoundError("Budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_28(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError(None, context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_29(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context=None)

    async def xǁBudgetServiceǁdelete_budget__mutmut_30(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError(context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_31(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", )

    async def xǁBudgetServiceǁdelete_budget__mutmut_32(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("XXBudget not foundXX", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_33(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("budget not found", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_34(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("BUDGET NOT FOUND", context={"id": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_35(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"XXidXX": budget_id})

    async def xǁBudgetServiceǁdelete_budget__mutmut_36(self, budget_id: str) -> None:
        budget = await self.get_budget(budget_id)
        has_transactions = await self._transaction_repository.exists_for_category(
            budget.category_id,
            user_id=budget.user_id,
            year=budget.year,
            month=budget.month,
        )
        if has_transactions:
            raise ValidationAppError(
                "Cannot delete budget with transactions in the same period",
                context={
                    "category_id": budget.category_id,
                    "year": budget.year,
                    "month": budget.month,
                },
            )

        deleted = await self._repository.delete(budget_id)
        if not deleted:
            raise EntityNotFoundError("Budget not found", context={"ID": budget_id})
    
    xǁBudgetServiceǁdelete_budget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁdelete_budget__mutmut_1': xǁBudgetServiceǁdelete_budget__mutmut_1, 
        'xǁBudgetServiceǁdelete_budget__mutmut_2': xǁBudgetServiceǁdelete_budget__mutmut_2, 
        'xǁBudgetServiceǁdelete_budget__mutmut_3': xǁBudgetServiceǁdelete_budget__mutmut_3, 
        'xǁBudgetServiceǁdelete_budget__mutmut_4': xǁBudgetServiceǁdelete_budget__mutmut_4, 
        'xǁBudgetServiceǁdelete_budget__mutmut_5': xǁBudgetServiceǁdelete_budget__mutmut_5, 
        'xǁBudgetServiceǁdelete_budget__mutmut_6': xǁBudgetServiceǁdelete_budget__mutmut_6, 
        'xǁBudgetServiceǁdelete_budget__mutmut_7': xǁBudgetServiceǁdelete_budget__mutmut_7, 
        'xǁBudgetServiceǁdelete_budget__mutmut_8': xǁBudgetServiceǁdelete_budget__mutmut_8, 
        'xǁBudgetServiceǁdelete_budget__mutmut_9': xǁBudgetServiceǁdelete_budget__mutmut_9, 
        'xǁBudgetServiceǁdelete_budget__mutmut_10': xǁBudgetServiceǁdelete_budget__mutmut_10, 
        'xǁBudgetServiceǁdelete_budget__mutmut_11': xǁBudgetServiceǁdelete_budget__mutmut_11, 
        'xǁBudgetServiceǁdelete_budget__mutmut_12': xǁBudgetServiceǁdelete_budget__mutmut_12, 
        'xǁBudgetServiceǁdelete_budget__mutmut_13': xǁBudgetServiceǁdelete_budget__mutmut_13, 
        'xǁBudgetServiceǁdelete_budget__mutmut_14': xǁBudgetServiceǁdelete_budget__mutmut_14, 
        'xǁBudgetServiceǁdelete_budget__mutmut_15': xǁBudgetServiceǁdelete_budget__mutmut_15, 
        'xǁBudgetServiceǁdelete_budget__mutmut_16': xǁBudgetServiceǁdelete_budget__mutmut_16, 
        'xǁBudgetServiceǁdelete_budget__mutmut_17': xǁBudgetServiceǁdelete_budget__mutmut_17, 
        'xǁBudgetServiceǁdelete_budget__mutmut_18': xǁBudgetServiceǁdelete_budget__mutmut_18, 
        'xǁBudgetServiceǁdelete_budget__mutmut_19': xǁBudgetServiceǁdelete_budget__mutmut_19, 
        'xǁBudgetServiceǁdelete_budget__mutmut_20': xǁBudgetServiceǁdelete_budget__mutmut_20, 
        'xǁBudgetServiceǁdelete_budget__mutmut_21': xǁBudgetServiceǁdelete_budget__mutmut_21, 
        'xǁBudgetServiceǁdelete_budget__mutmut_22': xǁBudgetServiceǁdelete_budget__mutmut_22, 
        'xǁBudgetServiceǁdelete_budget__mutmut_23': xǁBudgetServiceǁdelete_budget__mutmut_23, 
        'xǁBudgetServiceǁdelete_budget__mutmut_24': xǁBudgetServiceǁdelete_budget__mutmut_24, 
        'xǁBudgetServiceǁdelete_budget__mutmut_25': xǁBudgetServiceǁdelete_budget__mutmut_25, 
        'xǁBudgetServiceǁdelete_budget__mutmut_26': xǁBudgetServiceǁdelete_budget__mutmut_26, 
        'xǁBudgetServiceǁdelete_budget__mutmut_27': xǁBudgetServiceǁdelete_budget__mutmut_27, 
        'xǁBudgetServiceǁdelete_budget__mutmut_28': xǁBudgetServiceǁdelete_budget__mutmut_28, 
        'xǁBudgetServiceǁdelete_budget__mutmut_29': xǁBudgetServiceǁdelete_budget__mutmut_29, 
        'xǁBudgetServiceǁdelete_budget__mutmut_30': xǁBudgetServiceǁdelete_budget__mutmut_30, 
        'xǁBudgetServiceǁdelete_budget__mutmut_31': xǁBudgetServiceǁdelete_budget__mutmut_31, 
        'xǁBudgetServiceǁdelete_budget__mutmut_32': xǁBudgetServiceǁdelete_budget__mutmut_32, 
        'xǁBudgetServiceǁdelete_budget__mutmut_33': xǁBudgetServiceǁdelete_budget__mutmut_33, 
        'xǁBudgetServiceǁdelete_budget__mutmut_34': xǁBudgetServiceǁdelete_budget__mutmut_34, 
        'xǁBudgetServiceǁdelete_budget__mutmut_35': xǁBudgetServiceǁdelete_budget__mutmut_35, 
        'xǁBudgetServiceǁdelete_budget__mutmut_36': xǁBudgetServiceǁdelete_budget__mutmut_36
    }
    
    def delete_budget(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁdelete_budget__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁdelete_budget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete_budget.__signature__ = _mutmut_signature(xǁBudgetServiceǁdelete_budget__mutmut_orig)
    xǁBudgetServiceǁdelete_budget__mutmut_orig.__name__ = 'xǁBudgetServiceǁdelete_budget'

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_orig(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_1(self, user_id: str) -> None:
        user = None
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_2(self, user_id: str) -> None:
        user = await self._user_repository.get(None)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_3(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is not None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_4(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(None, context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_5(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context=None)

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_6(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_7(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", )

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_8(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_9(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("user not found", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_10(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_11(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})

    async def xǁBudgetServiceǁ_ensure_user_exists__mutmut_12(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
    
    xǁBudgetServiceǁ_ensure_user_exists__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁ_ensure_user_exists__mutmut_1': xǁBudgetServiceǁ_ensure_user_exists__mutmut_1, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_2': xǁBudgetServiceǁ_ensure_user_exists__mutmut_2, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_3': xǁBudgetServiceǁ_ensure_user_exists__mutmut_3, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_4': xǁBudgetServiceǁ_ensure_user_exists__mutmut_4, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_5': xǁBudgetServiceǁ_ensure_user_exists__mutmut_5, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_6': xǁBudgetServiceǁ_ensure_user_exists__mutmut_6, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_7': xǁBudgetServiceǁ_ensure_user_exists__mutmut_7, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_8': xǁBudgetServiceǁ_ensure_user_exists__mutmut_8, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_9': xǁBudgetServiceǁ_ensure_user_exists__mutmut_9, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_10': xǁBudgetServiceǁ_ensure_user_exists__mutmut_10, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_11': xǁBudgetServiceǁ_ensure_user_exists__mutmut_11, 
        'xǁBudgetServiceǁ_ensure_user_exists__mutmut_12': xǁBudgetServiceǁ_ensure_user_exists__mutmut_12
    }
    
    def _ensure_user_exists(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁ_ensure_user_exists__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁ_ensure_user_exists__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_user_exists.__signature__ = _mutmut_signature(xǁBudgetServiceǁ_ensure_user_exists__mutmut_orig)
    xǁBudgetServiceǁ_ensure_user_exists__mutmut_orig.__name__ = 'xǁBudgetServiceǁ_ensure_user_exists'

    async def xǁBudgetServiceǁ_get_category__mutmut_orig(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_1(self, category_id: str):
        category = None
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_2(self, category_id: str):
        category = await self._category_repository.get(None)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_3(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is not None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_4(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError(None, context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_5(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context=None)
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_6(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError(context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_7(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", )
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_8(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("XXCategory not foundXX", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_9(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("category not found", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_10(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("CATEGORY NOT FOUND", context={"id": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_11(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"XXidXX": category_id})
        return category

    async def xǁBudgetServiceǁ_get_category__mutmut_12(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"ID": category_id})
        return category
    
    xǁBudgetServiceǁ_get_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁ_get_category__mutmut_1': xǁBudgetServiceǁ_get_category__mutmut_1, 
        'xǁBudgetServiceǁ_get_category__mutmut_2': xǁBudgetServiceǁ_get_category__mutmut_2, 
        'xǁBudgetServiceǁ_get_category__mutmut_3': xǁBudgetServiceǁ_get_category__mutmut_3, 
        'xǁBudgetServiceǁ_get_category__mutmut_4': xǁBudgetServiceǁ_get_category__mutmut_4, 
        'xǁBudgetServiceǁ_get_category__mutmut_5': xǁBudgetServiceǁ_get_category__mutmut_5, 
        'xǁBudgetServiceǁ_get_category__mutmut_6': xǁBudgetServiceǁ_get_category__mutmut_6, 
        'xǁBudgetServiceǁ_get_category__mutmut_7': xǁBudgetServiceǁ_get_category__mutmut_7, 
        'xǁBudgetServiceǁ_get_category__mutmut_8': xǁBudgetServiceǁ_get_category__mutmut_8, 
        'xǁBudgetServiceǁ_get_category__mutmut_9': xǁBudgetServiceǁ_get_category__mutmut_9, 
        'xǁBudgetServiceǁ_get_category__mutmut_10': xǁBudgetServiceǁ_get_category__mutmut_10, 
        'xǁBudgetServiceǁ_get_category__mutmut_11': xǁBudgetServiceǁ_get_category__mutmut_11, 
        'xǁBudgetServiceǁ_get_category__mutmut_12': xǁBudgetServiceǁ_get_category__mutmut_12
    }
    
    def _get_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁ_get_category__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁ_get_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_category.__signature__ = _mutmut_signature(xǁBudgetServiceǁ_get_category__mutmut_orig)
    xǁBudgetServiceǁ_get_category__mutmut_orig.__name__ = 'xǁBudgetServiceǁ_get_category'

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_orig(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_1(self, expected: str, actual: str, label: str) -> None:
        if expected == actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_2(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                None,
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_3(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context=None,
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_4(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_5(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_6(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"XXexpected_user_idXX": expected, "actual_user_id": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_7(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"EXPECTED_USER_ID": expected, "actual_user_id": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_8(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "XXactual_user_idXX": actual},
            )

    def xǁBudgetServiceǁ_ensure_same_user__mutmut_9(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "ACTUAL_USER_ID": actual},
            )
    
    xǁBudgetServiceǁ_ensure_same_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁ_ensure_same_user__mutmut_1': xǁBudgetServiceǁ_ensure_same_user__mutmut_1, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_2': xǁBudgetServiceǁ_ensure_same_user__mutmut_2, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_3': xǁBudgetServiceǁ_ensure_same_user__mutmut_3, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_4': xǁBudgetServiceǁ_ensure_same_user__mutmut_4, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_5': xǁBudgetServiceǁ_ensure_same_user__mutmut_5, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_6': xǁBudgetServiceǁ_ensure_same_user__mutmut_6, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_7': xǁBudgetServiceǁ_ensure_same_user__mutmut_7, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_8': xǁBudgetServiceǁ_ensure_same_user__mutmut_8, 
        'xǁBudgetServiceǁ_ensure_same_user__mutmut_9': xǁBudgetServiceǁ_ensure_same_user__mutmut_9
    }
    
    def _ensure_same_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁ_ensure_same_user__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁ_ensure_same_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_same_user.__signature__ = _mutmut_signature(xǁBudgetServiceǁ_ensure_same_user__mutmut_orig)
    xǁBudgetServiceǁ_ensure_same_user__mutmut_orig.__name__ = 'xǁBudgetServiceǁ_ensure_same_user'

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_orig(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_1(self, category_type: CategoryType) -> None:
        if category_type == CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_2(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                None,
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_3(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                context=None,
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_4(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_5(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_6(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "XXBudgets can only be defined for expense categoriesXX",
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_7(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "budgets can only be defined for expense categories",
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_8(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "BUDGETS CAN ONLY BE DEFINED FOR EXPENSE CATEGORIES",
                context={"category_type": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_9(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                context={"XXcategory_typeXX": category_type},
            )

    def xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_10(self, category_type: CategoryType) -> None:
        if category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Budgets can only be defined for expense categories",
                context={"CATEGORY_TYPE": category_type},
            )
    
    xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_1': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_1, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_2': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_2, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_3': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_3, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_4': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_4, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_5': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_5, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_6': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_6, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_7': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_7, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_8': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_8, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_9': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_9, 
        'xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_10': xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_10
    }
    
    def _ensure_category_is_expense(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_orig"), object.__getattribute__(self, "xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_category_is_expense.__signature__ = _mutmut_signature(xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_orig)
    xǁBudgetServiceǁ_ensure_category_is_expense__mutmut_orig.__name__ = 'xǁBudgetServiceǁ_ensure_category_is_expense'
