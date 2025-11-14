"""Business logic for managing categories."""

from __future__ import annotations

from typing import List

from src.models.category import Category, CategoryCreate, CategoryUpdate, build_category
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.utils.exceptions import EntityNotFoundError, ValidationAppError
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


class CategoryService:
    """Encapsulates category workflows and validations."""

    def xǁCategoryServiceǁ__init____mutmut_orig(
        self,
        repository: CategoryRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository
        self._budget_repository = budget_repository

    def xǁCategoryServiceǁ__init____mutmut_1(
        self,
        repository: CategoryRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = None
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository
        self._budget_repository = budget_repository

    def xǁCategoryServiceǁ__init____mutmut_2(
        self,
        repository: CategoryRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = None
        self._transaction_repository = transaction_repository
        self._budget_repository = budget_repository

    def xǁCategoryServiceǁ__init____mutmut_3(
        self,
        repository: CategoryRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = None
        self._budget_repository = budget_repository

    def xǁCategoryServiceǁ__init____mutmut_4(
        self,
        repository: CategoryRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository
        self._budget_repository = None
    
    xǁCategoryServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁ__init____mutmut_1': xǁCategoryServiceǁ__init____mutmut_1, 
        'xǁCategoryServiceǁ__init____mutmut_2': xǁCategoryServiceǁ__init____mutmut_2, 
        'xǁCategoryServiceǁ__init____mutmut_3': xǁCategoryServiceǁ__init____mutmut_3, 
        'xǁCategoryServiceǁ__init____mutmut_4': xǁCategoryServiceǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCategoryServiceǁ__init____mutmut_orig)
    xǁCategoryServiceǁ__init____mutmut_orig.__name__ = 'xǁCategoryServiceǁ__init__'

    async def xǁCategoryServiceǁcreate_category__mutmut_orig(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, payload.user_id)
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_1(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(None)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, payload.user_id)
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_2(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(None, payload.user_id)
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_3(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, None)
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_4(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.user_id)
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_5(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, )
        category = build_category(payload)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_6(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, payload.user_id)
        category = None
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_7(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, payload.user_id)
        category = build_category(None)
        await self._repository.create(category)
        return category

    async def xǁCategoryServiceǁcreate_category__mutmut_8(self, payload: CategoryCreate) -> Category:
        """Create a new category ensuring user and parent validity."""
        await self._ensure_user_exists(payload.user_id)
        if payload.parent_id:
            await self._validate_parent(payload.parent_id, payload.user_id)
        category = build_category(payload)
        await self._repository.create(None)
        return category
    
    xǁCategoryServiceǁcreate_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁcreate_category__mutmut_1': xǁCategoryServiceǁcreate_category__mutmut_1, 
        'xǁCategoryServiceǁcreate_category__mutmut_2': xǁCategoryServiceǁcreate_category__mutmut_2, 
        'xǁCategoryServiceǁcreate_category__mutmut_3': xǁCategoryServiceǁcreate_category__mutmut_3, 
        'xǁCategoryServiceǁcreate_category__mutmut_4': xǁCategoryServiceǁcreate_category__mutmut_4, 
        'xǁCategoryServiceǁcreate_category__mutmut_5': xǁCategoryServiceǁcreate_category__mutmut_5, 
        'xǁCategoryServiceǁcreate_category__mutmut_6': xǁCategoryServiceǁcreate_category__mutmut_6, 
        'xǁCategoryServiceǁcreate_category__mutmut_7': xǁCategoryServiceǁcreate_category__mutmut_7, 
        'xǁCategoryServiceǁcreate_category__mutmut_8': xǁCategoryServiceǁcreate_category__mutmut_8
    }
    
    def create_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁcreate_category__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁcreate_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_category.__signature__ = _mutmut_signature(xǁCategoryServiceǁcreate_category__mutmut_orig)
    xǁCategoryServiceǁcreate_category__mutmut_orig.__name__ = 'xǁCategoryServiceǁcreate_category'

    async def xǁCategoryServiceǁlist_categories__mutmut_orig(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_1(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = None
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_2(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = None
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_3(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["XXuser_idXX"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_4(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["USER_ID"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_5(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = None
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_6(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["XXcategory_typeXX"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_7(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["CATEGORY_TYPE"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_8(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_9(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = None
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_10(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["XXparent_idXX"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_11(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["PARENT_ID"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_12(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = None
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_13(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["XXnameXX"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_14(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["NAME"] = name
        categories = await self._repository.list(**filters)
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_15(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = None
        return list(categories)

    async def xǁCategoryServiceǁlist_categories__mutmut_16(
        self,
        *,
        user_id: str | None = None,
        category_type: str | None = None,
        parent_id: str | None = None,
        name: str | None = None,
    ) -> List[Category]:
        """Return categories with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if category_type:
            filters["category_type"] = category_type
        if parent_id is not None:
            filters["parent_id"] = parent_id
        if name:
            filters["name"] = name
        categories = await self._repository.list(**filters)
        return list(None)
    
    xǁCategoryServiceǁlist_categories__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁlist_categories__mutmut_1': xǁCategoryServiceǁlist_categories__mutmut_1, 
        'xǁCategoryServiceǁlist_categories__mutmut_2': xǁCategoryServiceǁlist_categories__mutmut_2, 
        'xǁCategoryServiceǁlist_categories__mutmut_3': xǁCategoryServiceǁlist_categories__mutmut_3, 
        'xǁCategoryServiceǁlist_categories__mutmut_4': xǁCategoryServiceǁlist_categories__mutmut_4, 
        'xǁCategoryServiceǁlist_categories__mutmut_5': xǁCategoryServiceǁlist_categories__mutmut_5, 
        'xǁCategoryServiceǁlist_categories__mutmut_6': xǁCategoryServiceǁlist_categories__mutmut_6, 
        'xǁCategoryServiceǁlist_categories__mutmut_7': xǁCategoryServiceǁlist_categories__mutmut_7, 
        'xǁCategoryServiceǁlist_categories__mutmut_8': xǁCategoryServiceǁlist_categories__mutmut_8, 
        'xǁCategoryServiceǁlist_categories__mutmut_9': xǁCategoryServiceǁlist_categories__mutmut_9, 
        'xǁCategoryServiceǁlist_categories__mutmut_10': xǁCategoryServiceǁlist_categories__mutmut_10, 
        'xǁCategoryServiceǁlist_categories__mutmut_11': xǁCategoryServiceǁlist_categories__mutmut_11, 
        'xǁCategoryServiceǁlist_categories__mutmut_12': xǁCategoryServiceǁlist_categories__mutmut_12, 
        'xǁCategoryServiceǁlist_categories__mutmut_13': xǁCategoryServiceǁlist_categories__mutmut_13, 
        'xǁCategoryServiceǁlist_categories__mutmut_14': xǁCategoryServiceǁlist_categories__mutmut_14, 
        'xǁCategoryServiceǁlist_categories__mutmut_15': xǁCategoryServiceǁlist_categories__mutmut_15, 
        'xǁCategoryServiceǁlist_categories__mutmut_16': xǁCategoryServiceǁlist_categories__mutmut_16
    }
    
    def list_categories(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁlist_categories__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁlist_categories__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_categories.__signature__ = _mutmut_signature(xǁCategoryServiceǁlist_categories__mutmut_orig)
    xǁCategoryServiceǁlist_categories__mutmut_orig.__name__ = 'xǁCategoryServiceǁlist_categories'

    async def xǁCategoryServiceǁget_category__mutmut_orig(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_1(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = None
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_2(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(None)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_3(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is not None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_4(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError(None, context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_5(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context=None)
        return category

    async def xǁCategoryServiceǁget_category__mutmut_6(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError(context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_7(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", )
        return category

    async def xǁCategoryServiceǁget_category__mutmut_8(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("XXCategory not foundXX", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_9(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_10(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("CATEGORY NOT FOUND", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_11(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"XXidXX": category_id})
        return category

    async def xǁCategoryServiceǁget_category__mutmut_12(self, category_id: str) -> Category:
        """Retrieve category by identifier."""
        category = await self._repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"ID": category_id})
        return category
    
    xǁCategoryServiceǁget_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁget_category__mutmut_1': xǁCategoryServiceǁget_category__mutmut_1, 
        'xǁCategoryServiceǁget_category__mutmut_2': xǁCategoryServiceǁget_category__mutmut_2, 
        'xǁCategoryServiceǁget_category__mutmut_3': xǁCategoryServiceǁget_category__mutmut_3, 
        'xǁCategoryServiceǁget_category__mutmut_4': xǁCategoryServiceǁget_category__mutmut_4, 
        'xǁCategoryServiceǁget_category__mutmut_5': xǁCategoryServiceǁget_category__mutmut_5, 
        'xǁCategoryServiceǁget_category__mutmut_6': xǁCategoryServiceǁget_category__mutmut_6, 
        'xǁCategoryServiceǁget_category__mutmut_7': xǁCategoryServiceǁget_category__mutmut_7, 
        'xǁCategoryServiceǁget_category__mutmut_8': xǁCategoryServiceǁget_category__mutmut_8, 
        'xǁCategoryServiceǁget_category__mutmut_9': xǁCategoryServiceǁget_category__mutmut_9, 
        'xǁCategoryServiceǁget_category__mutmut_10': xǁCategoryServiceǁget_category__mutmut_10, 
        'xǁCategoryServiceǁget_category__mutmut_11': xǁCategoryServiceǁget_category__mutmut_11, 
        'xǁCategoryServiceǁget_category__mutmut_12': xǁCategoryServiceǁget_category__mutmut_12
    }
    
    def get_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁget_category__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁget_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_category.__signature__ = _mutmut_signature(xǁCategoryServiceǁget_category__mutmut_orig)
    xǁCategoryServiceǁget_category__mutmut_orig.__name__ = 'xǁCategoryServiceǁget_category'

    async def xǁCategoryServiceǁupdate_category__mutmut_orig(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_1(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = None
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_2(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(None)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_3(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = None
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_4(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=None, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_5(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=None)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_6(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_7(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, )
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_8(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=False, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_9(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=False)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_10(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_11(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                None,
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_12(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context=None,
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_13(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_14(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_15(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "XXNo data provided to update categoryXX",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_16(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "no data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_17(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "NO DATA PROVIDED TO UPDATE CATEGORY",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_18(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"XXidXX": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_19(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"ID": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_20(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates or updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_21(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "XXparent_idXX" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_22(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "PARENT_ID" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_23(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" not in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_24(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["XXparent_idXX"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_25(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["PARENT_ID"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_26(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                None,
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_27(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                None,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_28(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=None,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_29(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_30(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_31(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_32(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["XXparent_idXX"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_33(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["PARENT_ID"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_34(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = None
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_35(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(None, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_36(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, None)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_37(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_38(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, )
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_39(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is not None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_40(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError(None, context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_41(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context=None)
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_42(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError(context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_43(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", )
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_44(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("XXCategory not foundXX", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_45(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("category not found", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_46(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("CATEGORY NOT FOUND", context={"id": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_47(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"XXidXX": category_id})
        return category

    async def xǁCategoryServiceǁupdate_category__mutmut_48(self, category_id: str, payload: CategoryUpdate) -> Category:
        """Update category metadata."""
        existing = await self.get_category(category_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update category",
                context={"id": category_id},
            )
        if "parent_id" in updates and updates["parent_id"]:
            await self._validate_parent(
                updates["parent_id"],
                existing.user_id,
                category_id=category_id,
            )
        category = await self._repository.update(category_id, updates)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"ID": category_id})
        return category
    
    xǁCategoryServiceǁupdate_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁupdate_category__mutmut_1': xǁCategoryServiceǁupdate_category__mutmut_1, 
        'xǁCategoryServiceǁupdate_category__mutmut_2': xǁCategoryServiceǁupdate_category__mutmut_2, 
        'xǁCategoryServiceǁupdate_category__mutmut_3': xǁCategoryServiceǁupdate_category__mutmut_3, 
        'xǁCategoryServiceǁupdate_category__mutmut_4': xǁCategoryServiceǁupdate_category__mutmut_4, 
        'xǁCategoryServiceǁupdate_category__mutmut_5': xǁCategoryServiceǁupdate_category__mutmut_5, 
        'xǁCategoryServiceǁupdate_category__mutmut_6': xǁCategoryServiceǁupdate_category__mutmut_6, 
        'xǁCategoryServiceǁupdate_category__mutmut_7': xǁCategoryServiceǁupdate_category__mutmut_7, 
        'xǁCategoryServiceǁupdate_category__mutmut_8': xǁCategoryServiceǁupdate_category__mutmut_8, 
        'xǁCategoryServiceǁupdate_category__mutmut_9': xǁCategoryServiceǁupdate_category__mutmut_9, 
        'xǁCategoryServiceǁupdate_category__mutmut_10': xǁCategoryServiceǁupdate_category__mutmut_10, 
        'xǁCategoryServiceǁupdate_category__mutmut_11': xǁCategoryServiceǁupdate_category__mutmut_11, 
        'xǁCategoryServiceǁupdate_category__mutmut_12': xǁCategoryServiceǁupdate_category__mutmut_12, 
        'xǁCategoryServiceǁupdate_category__mutmut_13': xǁCategoryServiceǁupdate_category__mutmut_13, 
        'xǁCategoryServiceǁupdate_category__mutmut_14': xǁCategoryServiceǁupdate_category__mutmut_14, 
        'xǁCategoryServiceǁupdate_category__mutmut_15': xǁCategoryServiceǁupdate_category__mutmut_15, 
        'xǁCategoryServiceǁupdate_category__mutmut_16': xǁCategoryServiceǁupdate_category__mutmut_16, 
        'xǁCategoryServiceǁupdate_category__mutmut_17': xǁCategoryServiceǁupdate_category__mutmut_17, 
        'xǁCategoryServiceǁupdate_category__mutmut_18': xǁCategoryServiceǁupdate_category__mutmut_18, 
        'xǁCategoryServiceǁupdate_category__mutmut_19': xǁCategoryServiceǁupdate_category__mutmut_19, 
        'xǁCategoryServiceǁupdate_category__mutmut_20': xǁCategoryServiceǁupdate_category__mutmut_20, 
        'xǁCategoryServiceǁupdate_category__mutmut_21': xǁCategoryServiceǁupdate_category__mutmut_21, 
        'xǁCategoryServiceǁupdate_category__mutmut_22': xǁCategoryServiceǁupdate_category__mutmut_22, 
        'xǁCategoryServiceǁupdate_category__mutmut_23': xǁCategoryServiceǁupdate_category__mutmut_23, 
        'xǁCategoryServiceǁupdate_category__mutmut_24': xǁCategoryServiceǁupdate_category__mutmut_24, 
        'xǁCategoryServiceǁupdate_category__mutmut_25': xǁCategoryServiceǁupdate_category__mutmut_25, 
        'xǁCategoryServiceǁupdate_category__mutmut_26': xǁCategoryServiceǁupdate_category__mutmut_26, 
        'xǁCategoryServiceǁupdate_category__mutmut_27': xǁCategoryServiceǁupdate_category__mutmut_27, 
        'xǁCategoryServiceǁupdate_category__mutmut_28': xǁCategoryServiceǁupdate_category__mutmut_28, 
        'xǁCategoryServiceǁupdate_category__mutmut_29': xǁCategoryServiceǁupdate_category__mutmut_29, 
        'xǁCategoryServiceǁupdate_category__mutmut_30': xǁCategoryServiceǁupdate_category__mutmut_30, 
        'xǁCategoryServiceǁupdate_category__mutmut_31': xǁCategoryServiceǁupdate_category__mutmut_31, 
        'xǁCategoryServiceǁupdate_category__mutmut_32': xǁCategoryServiceǁupdate_category__mutmut_32, 
        'xǁCategoryServiceǁupdate_category__mutmut_33': xǁCategoryServiceǁupdate_category__mutmut_33, 
        'xǁCategoryServiceǁupdate_category__mutmut_34': xǁCategoryServiceǁupdate_category__mutmut_34, 
        'xǁCategoryServiceǁupdate_category__mutmut_35': xǁCategoryServiceǁupdate_category__mutmut_35, 
        'xǁCategoryServiceǁupdate_category__mutmut_36': xǁCategoryServiceǁupdate_category__mutmut_36, 
        'xǁCategoryServiceǁupdate_category__mutmut_37': xǁCategoryServiceǁupdate_category__mutmut_37, 
        'xǁCategoryServiceǁupdate_category__mutmut_38': xǁCategoryServiceǁupdate_category__mutmut_38, 
        'xǁCategoryServiceǁupdate_category__mutmut_39': xǁCategoryServiceǁupdate_category__mutmut_39, 
        'xǁCategoryServiceǁupdate_category__mutmut_40': xǁCategoryServiceǁupdate_category__mutmut_40, 
        'xǁCategoryServiceǁupdate_category__mutmut_41': xǁCategoryServiceǁupdate_category__mutmut_41, 
        'xǁCategoryServiceǁupdate_category__mutmut_42': xǁCategoryServiceǁupdate_category__mutmut_42, 
        'xǁCategoryServiceǁupdate_category__mutmut_43': xǁCategoryServiceǁupdate_category__mutmut_43, 
        'xǁCategoryServiceǁupdate_category__mutmut_44': xǁCategoryServiceǁupdate_category__mutmut_44, 
        'xǁCategoryServiceǁupdate_category__mutmut_45': xǁCategoryServiceǁupdate_category__mutmut_45, 
        'xǁCategoryServiceǁupdate_category__mutmut_46': xǁCategoryServiceǁupdate_category__mutmut_46, 
        'xǁCategoryServiceǁupdate_category__mutmut_47': xǁCategoryServiceǁupdate_category__mutmut_47, 
        'xǁCategoryServiceǁupdate_category__mutmut_48': xǁCategoryServiceǁupdate_category__mutmut_48
    }
    
    def update_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁupdate_category__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁupdate_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_category.__signature__ = _mutmut_signature(xǁCategoryServiceǁupdate_category__mutmut_orig)
    xǁCategoryServiceǁupdate_category__mutmut_orig.__name__ = 'xǁCategoryServiceǁupdate_category'

    async def xǁCategoryServiceǁdelete_category__mutmut_orig(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_1(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = None
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_2(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(None)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_3(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                None,
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_4(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context=None,
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_5(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_6(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_7(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "XXCategory has related transactions and cannot be deletedXX",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_8(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_9(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "CATEGORY HAS RELATED TRANSACTIONS AND CANNOT BE DELETED",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_10(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"XXidXX": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_11(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"ID": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_12(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = None
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_13(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=None)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_14(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                None,
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_15(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context=None,
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_16(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_17(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_18(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "XXCategory has budgets assigned and cannot be deletedXX",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_19(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_20(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "CATEGORY HAS BUDGETS ASSIGNED AND CANNOT BE DELETED",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_21(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"XXidXX": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_22(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"ID": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_23(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = None
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_24(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(None)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_25(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if deleted:
            raise EntityNotFoundError("Category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_26(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError(None, context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_27(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context=None)

    async def xǁCategoryServiceǁdelete_category__mutmut_28(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError(context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_29(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", )

    async def xǁCategoryServiceǁdelete_category__mutmut_30(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("XXCategory not foundXX", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_31(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("category not found", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_32(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("CATEGORY NOT FOUND", context={"id": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_33(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"XXidXX": category_id})

    async def xǁCategoryServiceǁdelete_category__mutmut_34(self, category_id: str) -> None:
        """Delete category ensuring existence."""
        has_transactions = await self._transaction_repository.exists_for_category(category_id)
        if has_transactions:
            raise ValidationAppError(
                "Category has related transactions and cannot be deleted",
                context={"id": category_id},
            )

        budgets = await self._budget_repository.list(category_id=category_id)
        if budgets:
            raise ValidationAppError(
                "Category has budgets assigned and cannot be deleted",
                context={"id": category_id},
            )

        deleted = await self._repository.delete(category_id)
        if not deleted:
            raise EntityNotFoundError("Category not found", context={"ID": category_id})
    
    xǁCategoryServiceǁdelete_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁdelete_category__mutmut_1': xǁCategoryServiceǁdelete_category__mutmut_1, 
        'xǁCategoryServiceǁdelete_category__mutmut_2': xǁCategoryServiceǁdelete_category__mutmut_2, 
        'xǁCategoryServiceǁdelete_category__mutmut_3': xǁCategoryServiceǁdelete_category__mutmut_3, 
        'xǁCategoryServiceǁdelete_category__mutmut_4': xǁCategoryServiceǁdelete_category__mutmut_4, 
        'xǁCategoryServiceǁdelete_category__mutmut_5': xǁCategoryServiceǁdelete_category__mutmut_5, 
        'xǁCategoryServiceǁdelete_category__mutmut_6': xǁCategoryServiceǁdelete_category__mutmut_6, 
        'xǁCategoryServiceǁdelete_category__mutmut_7': xǁCategoryServiceǁdelete_category__mutmut_7, 
        'xǁCategoryServiceǁdelete_category__mutmut_8': xǁCategoryServiceǁdelete_category__mutmut_8, 
        'xǁCategoryServiceǁdelete_category__mutmut_9': xǁCategoryServiceǁdelete_category__mutmut_9, 
        'xǁCategoryServiceǁdelete_category__mutmut_10': xǁCategoryServiceǁdelete_category__mutmut_10, 
        'xǁCategoryServiceǁdelete_category__mutmut_11': xǁCategoryServiceǁdelete_category__mutmut_11, 
        'xǁCategoryServiceǁdelete_category__mutmut_12': xǁCategoryServiceǁdelete_category__mutmut_12, 
        'xǁCategoryServiceǁdelete_category__mutmut_13': xǁCategoryServiceǁdelete_category__mutmut_13, 
        'xǁCategoryServiceǁdelete_category__mutmut_14': xǁCategoryServiceǁdelete_category__mutmut_14, 
        'xǁCategoryServiceǁdelete_category__mutmut_15': xǁCategoryServiceǁdelete_category__mutmut_15, 
        'xǁCategoryServiceǁdelete_category__mutmut_16': xǁCategoryServiceǁdelete_category__mutmut_16, 
        'xǁCategoryServiceǁdelete_category__mutmut_17': xǁCategoryServiceǁdelete_category__mutmut_17, 
        'xǁCategoryServiceǁdelete_category__mutmut_18': xǁCategoryServiceǁdelete_category__mutmut_18, 
        'xǁCategoryServiceǁdelete_category__mutmut_19': xǁCategoryServiceǁdelete_category__mutmut_19, 
        'xǁCategoryServiceǁdelete_category__mutmut_20': xǁCategoryServiceǁdelete_category__mutmut_20, 
        'xǁCategoryServiceǁdelete_category__mutmut_21': xǁCategoryServiceǁdelete_category__mutmut_21, 
        'xǁCategoryServiceǁdelete_category__mutmut_22': xǁCategoryServiceǁdelete_category__mutmut_22, 
        'xǁCategoryServiceǁdelete_category__mutmut_23': xǁCategoryServiceǁdelete_category__mutmut_23, 
        'xǁCategoryServiceǁdelete_category__mutmut_24': xǁCategoryServiceǁdelete_category__mutmut_24, 
        'xǁCategoryServiceǁdelete_category__mutmut_25': xǁCategoryServiceǁdelete_category__mutmut_25, 
        'xǁCategoryServiceǁdelete_category__mutmut_26': xǁCategoryServiceǁdelete_category__mutmut_26, 
        'xǁCategoryServiceǁdelete_category__mutmut_27': xǁCategoryServiceǁdelete_category__mutmut_27, 
        'xǁCategoryServiceǁdelete_category__mutmut_28': xǁCategoryServiceǁdelete_category__mutmut_28, 
        'xǁCategoryServiceǁdelete_category__mutmut_29': xǁCategoryServiceǁdelete_category__mutmut_29, 
        'xǁCategoryServiceǁdelete_category__mutmut_30': xǁCategoryServiceǁdelete_category__mutmut_30, 
        'xǁCategoryServiceǁdelete_category__mutmut_31': xǁCategoryServiceǁdelete_category__mutmut_31, 
        'xǁCategoryServiceǁdelete_category__mutmut_32': xǁCategoryServiceǁdelete_category__mutmut_32, 
        'xǁCategoryServiceǁdelete_category__mutmut_33': xǁCategoryServiceǁdelete_category__mutmut_33, 
        'xǁCategoryServiceǁdelete_category__mutmut_34': xǁCategoryServiceǁdelete_category__mutmut_34
    }
    
    def delete_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁdelete_category__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁdelete_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete_category.__signature__ = _mutmut_signature(xǁCategoryServiceǁdelete_category__mutmut_orig)
    xǁCategoryServiceǁdelete_category__mutmut_orig.__name__ = 'xǁCategoryServiceǁdelete_category'

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_orig(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_1(self, user_id: str) -> None:
        user = None
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_2(self, user_id: str) -> None:
        user = await self._user_repository.get(None)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_3(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is not None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_4(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(None, context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_5(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context=None)

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_6(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_7(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", )

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_8(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_9(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("user not found", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_10(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_11(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})

    async def xǁCategoryServiceǁ_ensure_user_exists__mutmut_12(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
    
    xǁCategoryServiceǁ_ensure_user_exists__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁ_ensure_user_exists__mutmut_1': xǁCategoryServiceǁ_ensure_user_exists__mutmut_1, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_2': xǁCategoryServiceǁ_ensure_user_exists__mutmut_2, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_3': xǁCategoryServiceǁ_ensure_user_exists__mutmut_3, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_4': xǁCategoryServiceǁ_ensure_user_exists__mutmut_4, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_5': xǁCategoryServiceǁ_ensure_user_exists__mutmut_5, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_6': xǁCategoryServiceǁ_ensure_user_exists__mutmut_6, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_7': xǁCategoryServiceǁ_ensure_user_exists__mutmut_7, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_8': xǁCategoryServiceǁ_ensure_user_exists__mutmut_8, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_9': xǁCategoryServiceǁ_ensure_user_exists__mutmut_9, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_10': xǁCategoryServiceǁ_ensure_user_exists__mutmut_10, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_11': xǁCategoryServiceǁ_ensure_user_exists__mutmut_11, 
        'xǁCategoryServiceǁ_ensure_user_exists__mutmut_12': xǁCategoryServiceǁ_ensure_user_exists__mutmut_12
    }
    
    def _ensure_user_exists(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁ_ensure_user_exists__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁ_ensure_user_exists__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_user_exists.__signature__ = _mutmut_signature(xǁCategoryServiceǁ_ensure_user_exists__mutmut_orig)
    xǁCategoryServiceǁ_ensure_user_exists__mutmut_orig.__name__ = 'xǁCategoryServiceǁ_ensure_user_exists'

    async def xǁCategoryServiceǁ_validate_parent__mutmut_orig(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_1(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = None
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_2(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(None)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_3(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is not None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_4(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError(None, context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_5(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context=None)
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_6(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError(context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_7(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", )
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_8(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("XXParent category not foundXX", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_9(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_10(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("PARENT CATEGORY NOT FOUND", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_11(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"XXidXX": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_12(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"ID": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_13(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id or parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_14(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id != category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_15(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                None,
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_16(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context=None,
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_17(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_18(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_19(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "XXCategory cannot reference itself as parentXX",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_20(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_21(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "CATEGORY CANNOT REFERENCE ITSELF AS PARENT",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_22(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"XXidXX": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_23(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"ID": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_24(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id or parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_25(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id == user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_26(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                None,
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_27(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context=None,
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_28(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_29(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_30(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "XXParent category belongs to a different userXX",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_31(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "parent category belongs to a different user",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_32(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "PARENT CATEGORY BELONGS TO A DIFFERENT USER",
                context={"parent_id": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_33(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"XXparent_idXX": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_34(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"PARENT_ID": parent_id, "user_id": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_35(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "XXuser_idXX": user_id},
            )

    async def xǁCategoryServiceǁ_validate_parent__mutmut_36(
        self,
        parent_id: str,
        user_id: str | None,
        *,
        category_id: str | None = None,
    ) -> None:
        parent = await self._repository.get(parent_id)
        if parent is None:
            raise EntityNotFoundError("Parent category not found", context={"id": parent_id})
        if category_id and parent.id == category_id:
            raise ValidationAppError(
                "Category cannot reference itself as parent",
                context={"id": category_id},
            )
        if user_id and parent.user_id != user_id:
            raise ValidationAppError(
                "Parent category belongs to a different user",
                context={"parent_id": parent_id, "USER_ID": user_id},
            )
    
    xǁCategoryServiceǁ_validate_parent__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryServiceǁ_validate_parent__mutmut_1': xǁCategoryServiceǁ_validate_parent__mutmut_1, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_2': xǁCategoryServiceǁ_validate_parent__mutmut_2, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_3': xǁCategoryServiceǁ_validate_parent__mutmut_3, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_4': xǁCategoryServiceǁ_validate_parent__mutmut_4, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_5': xǁCategoryServiceǁ_validate_parent__mutmut_5, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_6': xǁCategoryServiceǁ_validate_parent__mutmut_6, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_7': xǁCategoryServiceǁ_validate_parent__mutmut_7, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_8': xǁCategoryServiceǁ_validate_parent__mutmut_8, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_9': xǁCategoryServiceǁ_validate_parent__mutmut_9, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_10': xǁCategoryServiceǁ_validate_parent__mutmut_10, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_11': xǁCategoryServiceǁ_validate_parent__mutmut_11, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_12': xǁCategoryServiceǁ_validate_parent__mutmut_12, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_13': xǁCategoryServiceǁ_validate_parent__mutmut_13, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_14': xǁCategoryServiceǁ_validate_parent__mutmut_14, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_15': xǁCategoryServiceǁ_validate_parent__mutmut_15, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_16': xǁCategoryServiceǁ_validate_parent__mutmut_16, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_17': xǁCategoryServiceǁ_validate_parent__mutmut_17, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_18': xǁCategoryServiceǁ_validate_parent__mutmut_18, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_19': xǁCategoryServiceǁ_validate_parent__mutmut_19, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_20': xǁCategoryServiceǁ_validate_parent__mutmut_20, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_21': xǁCategoryServiceǁ_validate_parent__mutmut_21, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_22': xǁCategoryServiceǁ_validate_parent__mutmut_22, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_23': xǁCategoryServiceǁ_validate_parent__mutmut_23, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_24': xǁCategoryServiceǁ_validate_parent__mutmut_24, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_25': xǁCategoryServiceǁ_validate_parent__mutmut_25, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_26': xǁCategoryServiceǁ_validate_parent__mutmut_26, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_27': xǁCategoryServiceǁ_validate_parent__mutmut_27, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_28': xǁCategoryServiceǁ_validate_parent__mutmut_28, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_29': xǁCategoryServiceǁ_validate_parent__mutmut_29, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_30': xǁCategoryServiceǁ_validate_parent__mutmut_30, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_31': xǁCategoryServiceǁ_validate_parent__mutmut_31, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_32': xǁCategoryServiceǁ_validate_parent__mutmut_32, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_33': xǁCategoryServiceǁ_validate_parent__mutmut_33, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_34': xǁCategoryServiceǁ_validate_parent__mutmut_34, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_35': xǁCategoryServiceǁ_validate_parent__mutmut_35, 
        'xǁCategoryServiceǁ_validate_parent__mutmut_36': xǁCategoryServiceǁ_validate_parent__mutmut_36
    }
    
    def _validate_parent(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryServiceǁ_validate_parent__mutmut_orig"), object.__getattribute__(self, "xǁCategoryServiceǁ_validate_parent__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _validate_parent.__signature__ = _mutmut_signature(xǁCategoryServiceǁ_validate_parent__mutmut_orig)
    xǁCategoryServiceǁ_validate_parent__mutmut_orig.__name__ = 'xǁCategoryServiceǁ_validate_parent'
