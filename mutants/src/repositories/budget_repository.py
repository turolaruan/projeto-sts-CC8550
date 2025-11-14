"""Budget repository implementations."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, Iterable, List, Optional

from bson.decimal128 import Decimal128

from src.models.budget import Budget
from src.models.common import ensure_object_id
from src.repositories.base import Repository
from src.repositories.mongo_compat import (
    ASCENDING,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
    ReturnDocument,
    ensure_motor_dependencies,
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


class BudgetRepository(Repository[Budget, str]):
    """Mongo-backed repository for budgets."""

    def xǁBudgetRepositoryǁ__init____mutmut_orig(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("budgets")
        self._indexes_ready = False

    def xǁBudgetRepositoryǁ__init____mutmut_1(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = None
        self._indexes_ready = False

    def xǁBudgetRepositoryǁ__init____mutmut_2(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection(None)
        self._indexes_ready = False

    def xǁBudgetRepositoryǁ__init____mutmut_3(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("XXbudgetsXX")
        self._indexes_ready = False

    def xǁBudgetRepositoryǁ__init____mutmut_4(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("BUDGETS")
        self._indexes_ready = False

    def xǁBudgetRepositoryǁ__init____mutmut_5(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("budgets")
        self._indexes_ready = None

    def xǁBudgetRepositoryǁ__init____mutmut_6(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("budgets")
        self._indexes_ready = True
    
    xǁBudgetRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁ__init____mutmut_1': xǁBudgetRepositoryǁ__init____mutmut_1, 
        'xǁBudgetRepositoryǁ__init____mutmut_2': xǁBudgetRepositoryǁ__init____mutmut_2, 
        'xǁBudgetRepositoryǁ__init____mutmut_3': xǁBudgetRepositoryǁ__init____mutmut_3, 
        'xǁBudgetRepositoryǁ__init____mutmut_4': xǁBudgetRepositoryǁ__init____mutmut_4, 
        'xǁBudgetRepositoryǁ__init____mutmut_5': xǁBudgetRepositoryǁ__init____mutmut_5, 
        'xǁBudgetRepositoryǁ__init____mutmut_6': xǁBudgetRepositoryǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁ__init____mutmut_orig)
    xǁBudgetRepositoryǁ__init____mutmut_orig.__name__ = 'xǁBudgetRepositoryǁ__init__'

    async def xǁBudgetRepositoryǁcreate__mutmut_orig(self, entity: Budget) -> Budget:
        await self._ensure_indexes()
        await self._collection.insert_one(_budget_to_document(entity))
        return entity

    async def xǁBudgetRepositoryǁcreate__mutmut_1(self, entity: Budget) -> Budget:
        await self._ensure_indexes()
        await self._collection.insert_one(None)
        return entity

    async def xǁBudgetRepositoryǁcreate__mutmut_2(self, entity: Budget) -> Budget:
        await self._ensure_indexes()
        await self._collection.insert_one(_budget_to_document(None))
        return entity
    
    xǁBudgetRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁcreate__mutmut_1': xǁBudgetRepositoryǁcreate__mutmut_1, 
        'xǁBudgetRepositoryǁcreate__mutmut_2': xǁBudgetRepositoryǁcreate__mutmut_2
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁcreate__mutmut_orig)
    xǁBudgetRepositoryǁcreate__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁcreate'

    async def xǁBudgetRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Budget]:
        document = None
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_2(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one(None)
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_3(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"XX_idXX": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_4(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"_ID": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_5(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"_id": ensure_object_id(None)})
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_6(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁget__mutmut_7(self, entity_id: str) -> Optional[Budget]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_budget(None)
    
    xǁBudgetRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁget__mutmut_1': xǁBudgetRepositoryǁget__mutmut_1, 
        'xǁBudgetRepositoryǁget__mutmut_2': xǁBudgetRepositoryǁget__mutmut_2, 
        'xǁBudgetRepositoryǁget__mutmut_3': xǁBudgetRepositoryǁget__mutmut_3, 
        'xǁBudgetRepositoryǁget__mutmut_4': xǁBudgetRepositoryǁget__mutmut_4, 
        'xǁBudgetRepositoryǁget__mutmut_5': xǁBudgetRepositoryǁget__mutmut_5, 
        'xǁBudgetRepositoryǁget__mutmut_6': xǁBudgetRepositoryǁget__mutmut_6, 
        'xǁBudgetRepositoryǁget__mutmut_7': xǁBudgetRepositoryǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁget__mutmut_orig)
    xǁBudgetRepositoryǁget__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁget'

    async def xǁBudgetRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = None

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = None
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get(None)
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = None

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["XXuser_idXX"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["USER_ID"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(None)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = None
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get(None)
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("XXcategory_idXX")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("CATEGORY_ID")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = None

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["XXcategory_idXX"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["CATEGORY_ID"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(None)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = None
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get(None)
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("XXyearXX")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("YEAR")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = None

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["XXyearXX"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["YEAR"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = None
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get(None)
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("XXmonthXX")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("MONTH")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = None

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["XXmonthXX"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["MONTH"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = None
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort(None)
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(None).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.rfind(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("XXyearXX", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_37(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("YEAR", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_38(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("XXmonthXX", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_39(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("MONTH", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_40(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = None
        async for document in cursor:
            results.append(_document_to_budget(document))
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_41(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(None)
        return results

    async def xǁBudgetRepositoryǁlist__mutmut_42(self, **filters: object) -> Iterable[Budget]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        year = filters.get("year")
        if isinstance(year, int):
            query["year"] = year

        month = filters.get("month")
        if isinstance(month, int):
            query["month"] = month

        cursor = self._collection.find(query).sort([("year", ASCENDING), ("month", ASCENDING)])
        results: List[Budget] = []
        async for document in cursor:
            results.append(_document_to_budget(None))
        return results
    
    xǁBudgetRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁlist__mutmut_1': xǁBudgetRepositoryǁlist__mutmut_1, 
        'xǁBudgetRepositoryǁlist__mutmut_2': xǁBudgetRepositoryǁlist__mutmut_2, 
        'xǁBudgetRepositoryǁlist__mutmut_3': xǁBudgetRepositoryǁlist__mutmut_3, 
        'xǁBudgetRepositoryǁlist__mutmut_4': xǁBudgetRepositoryǁlist__mutmut_4, 
        'xǁBudgetRepositoryǁlist__mutmut_5': xǁBudgetRepositoryǁlist__mutmut_5, 
        'xǁBudgetRepositoryǁlist__mutmut_6': xǁBudgetRepositoryǁlist__mutmut_6, 
        'xǁBudgetRepositoryǁlist__mutmut_7': xǁBudgetRepositoryǁlist__mutmut_7, 
        'xǁBudgetRepositoryǁlist__mutmut_8': xǁBudgetRepositoryǁlist__mutmut_8, 
        'xǁBudgetRepositoryǁlist__mutmut_9': xǁBudgetRepositoryǁlist__mutmut_9, 
        'xǁBudgetRepositoryǁlist__mutmut_10': xǁBudgetRepositoryǁlist__mutmut_10, 
        'xǁBudgetRepositoryǁlist__mutmut_11': xǁBudgetRepositoryǁlist__mutmut_11, 
        'xǁBudgetRepositoryǁlist__mutmut_12': xǁBudgetRepositoryǁlist__mutmut_12, 
        'xǁBudgetRepositoryǁlist__mutmut_13': xǁBudgetRepositoryǁlist__mutmut_13, 
        'xǁBudgetRepositoryǁlist__mutmut_14': xǁBudgetRepositoryǁlist__mutmut_14, 
        'xǁBudgetRepositoryǁlist__mutmut_15': xǁBudgetRepositoryǁlist__mutmut_15, 
        'xǁBudgetRepositoryǁlist__mutmut_16': xǁBudgetRepositoryǁlist__mutmut_16, 
        'xǁBudgetRepositoryǁlist__mutmut_17': xǁBudgetRepositoryǁlist__mutmut_17, 
        'xǁBudgetRepositoryǁlist__mutmut_18': xǁBudgetRepositoryǁlist__mutmut_18, 
        'xǁBudgetRepositoryǁlist__mutmut_19': xǁBudgetRepositoryǁlist__mutmut_19, 
        'xǁBudgetRepositoryǁlist__mutmut_20': xǁBudgetRepositoryǁlist__mutmut_20, 
        'xǁBudgetRepositoryǁlist__mutmut_21': xǁBudgetRepositoryǁlist__mutmut_21, 
        'xǁBudgetRepositoryǁlist__mutmut_22': xǁBudgetRepositoryǁlist__mutmut_22, 
        'xǁBudgetRepositoryǁlist__mutmut_23': xǁBudgetRepositoryǁlist__mutmut_23, 
        'xǁBudgetRepositoryǁlist__mutmut_24': xǁBudgetRepositoryǁlist__mutmut_24, 
        'xǁBudgetRepositoryǁlist__mutmut_25': xǁBudgetRepositoryǁlist__mutmut_25, 
        'xǁBudgetRepositoryǁlist__mutmut_26': xǁBudgetRepositoryǁlist__mutmut_26, 
        'xǁBudgetRepositoryǁlist__mutmut_27': xǁBudgetRepositoryǁlist__mutmut_27, 
        'xǁBudgetRepositoryǁlist__mutmut_28': xǁBudgetRepositoryǁlist__mutmut_28, 
        'xǁBudgetRepositoryǁlist__mutmut_29': xǁBudgetRepositoryǁlist__mutmut_29, 
        'xǁBudgetRepositoryǁlist__mutmut_30': xǁBudgetRepositoryǁlist__mutmut_30, 
        'xǁBudgetRepositoryǁlist__mutmut_31': xǁBudgetRepositoryǁlist__mutmut_31, 
        'xǁBudgetRepositoryǁlist__mutmut_32': xǁBudgetRepositoryǁlist__mutmut_32, 
        'xǁBudgetRepositoryǁlist__mutmut_33': xǁBudgetRepositoryǁlist__mutmut_33, 
        'xǁBudgetRepositoryǁlist__mutmut_34': xǁBudgetRepositoryǁlist__mutmut_34, 
        'xǁBudgetRepositoryǁlist__mutmut_35': xǁBudgetRepositoryǁlist__mutmut_35, 
        'xǁBudgetRepositoryǁlist__mutmut_36': xǁBudgetRepositoryǁlist__mutmut_36, 
        'xǁBudgetRepositoryǁlist__mutmut_37': xǁBudgetRepositoryǁlist__mutmut_37, 
        'xǁBudgetRepositoryǁlist__mutmut_38': xǁBudgetRepositoryǁlist__mutmut_38, 
        'xǁBudgetRepositoryǁlist__mutmut_39': xǁBudgetRepositoryǁlist__mutmut_39, 
        'xǁBudgetRepositoryǁlist__mutmut_40': xǁBudgetRepositoryǁlist__mutmut_40, 
        'xǁBudgetRepositoryǁlist__mutmut_41': xǁBudgetRepositoryǁlist__mutmut_41, 
        'xǁBudgetRepositoryǁlist__mutmut_42': xǁBudgetRepositoryǁlist__mutmut_42
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁlist__mutmut_orig)
    xǁBudgetRepositoryǁlist__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁlist'

    async def xǁBudgetRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(None)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = None
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(None)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = None
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            None,
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            None,
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_8(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=None,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_9(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_10(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_11(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_12(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"XX_idXX": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_13(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_ID": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_14(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(None)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_15(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"XX$setXX": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_16(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$SET": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_17(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return None
        return _document_to_budget(result)

    async def xǁBudgetRepositoryǁupdate__mutmut_18(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_budget_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_budget(None)
    
    xǁBudgetRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁupdate__mutmut_1': xǁBudgetRepositoryǁupdate__mutmut_1, 
        'xǁBudgetRepositoryǁupdate__mutmut_2': xǁBudgetRepositoryǁupdate__mutmut_2, 
        'xǁBudgetRepositoryǁupdate__mutmut_3': xǁBudgetRepositoryǁupdate__mutmut_3, 
        'xǁBudgetRepositoryǁupdate__mutmut_4': xǁBudgetRepositoryǁupdate__mutmut_4, 
        'xǁBudgetRepositoryǁupdate__mutmut_5': xǁBudgetRepositoryǁupdate__mutmut_5, 
        'xǁBudgetRepositoryǁupdate__mutmut_6': xǁBudgetRepositoryǁupdate__mutmut_6, 
        'xǁBudgetRepositoryǁupdate__mutmut_7': xǁBudgetRepositoryǁupdate__mutmut_7, 
        'xǁBudgetRepositoryǁupdate__mutmut_8': xǁBudgetRepositoryǁupdate__mutmut_8, 
        'xǁBudgetRepositoryǁupdate__mutmut_9': xǁBudgetRepositoryǁupdate__mutmut_9, 
        'xǁBudgetRepositoryǁupdate__mutmut_10': xǁBudgetRepositoryǁupdate__mutmut_10, 
        'xǁBudgetRepositoryǁupdate__mutmut_11': xǁBudgetRepositoryǁupdate__mutmut_11, 
        'xǁBudgetRepositoryǁupdate__mutmut_12': xǁBudgetRepositoryǁupdate__mutmut_12, 
        'xǁBudgetRepositoryǁupdate__mutmut_13': xǁBudgetRepositoryǁupdate__mutmut_13, 
        'xǁBudgetRepositoryǁupdate__mutmut_14': xǁBudgetRepositoryǁupdate__mutmut_14, 
        'xǁBudgetRepositoryǁupdate__mutmut_15': xǁBudgetRepositoryǁupdate__mutmut_15, 
        'xǁBudgetRepositoryǁupdate__mutmut_16': xǁBudgetRepositoryǁupdate__mutmut_16, 
        'xǁBudgetRepositoryǁupdate__mutmut_17': xǁBudgetRepositoryǁupdate__mutmut_17, 
        'xǁBudgetRepositoryǁupdate__mutmut_18': xǁBudgetRepositoryǁupdate__mutmut_18
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁupdate__mutmut_orig)
    xǁBudgetRepositoryǁupdate__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁupdate'

    async def xǁBudgetRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁBudgetRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        outcome = None
        return outcome.deleted_count > 0

    async def xǁBudgetRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one(None)
        return outcome.deleted_count > 0

    async def xǁBudgetRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"XX_idXX": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁBudgetRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_ID": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁBudgetRepositoryǁdelete__mutmut_5(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(None)})
        return outcome.deleted_count > 0

    async def xǁBudgetRepositoryǁdelete__mutmut_6(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count >= 0

    async def xǁBudgetRepositoryǁdelete__mutmut_7(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 1
    
    xǁBudgetRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁdelete__mutmut_1': xǁBudgetRepositoryǁdelete__mutmut_1, 
        'xǁBudgetRepositoryǁdelete__mutmut_2': xǁBudgetRepositoryǁdelete__mutmut_2, 
        'xǁBudgetRepositoryǁdelete__mutmut_3': xǁBudgetRepositoryǁdelete__mutmut_3, 
        'xǁBudgetRepositoryǁdelete__mutmut_4': xǁBudgetRepositoryǁdelete__mutmut_4, 
        'xǁBudgetRepositoryǁdelete__mutmut_5': xǁBudgetRepositoryǁdelete__mutmut_5, 
        'xǁBudgetRepositoryǁdelete__mutmut_6': xǁBudgetRepositoryǁdelete__mutmut_6, 
        'xǁBudgetRepositoryǁdelete__mutmut_7': xǁBudgetRepositoryǁdelete__mutmut_7
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁdelete__mutmut_orig)
    xǁBudgetRepositoryǁdelete__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁdelete'

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_orig(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_1(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = None
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_2(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            None
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_3(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "XXuser_idXX": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_4(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "USER_ID": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_5(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(None),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_6(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "XXcategory_idXX": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_7(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "CATEGORY_ID": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_8(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(None),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_9(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "XXyearXX": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_10(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "YEAR": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_11(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "XXmonthXX": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_12(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "MONTH": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_13(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if document:
            return None
        return _document_to_budget(document)

    async def xǁBudgetRepositoryǁfind_by_period__mutmut_14(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        document = await self._collection.find_one(
            {
                "user_id": ensure_object_id(user_id),
                "category_id": ensure_object_id(category_id),
                "year": year,
                "month": month,
            }
        )
        if not document:
            return None
        return _document_to_budget(None)
    
    xǁBudgetRepositoryǁfind_by_period__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁfind_by_period__mutmut_1': xǁBudgetRepositoryǁfind_by_period__mutmut_1, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_2': xǁBudgetRepositoryǁfind_by_period__mutmut_2, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_3': xǁBudgetRepositoryǁfind_by_period__mutmut_3, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_4': xǁBudgetRepositoryǁfind_by_period__mutmut_4, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_5': xǁBudgetRepositoryǁfind_by_period__mutmut_5, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_6': xǁBudgetRepositoryǁfind_by_period__mutmut_6, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_7': xǁBudgetRepositoryǁfind_by_period__mutmut_7, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_8': xǁBudgetRepositoryǁfind_by_period__mutmut_8, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_9': xǁBudgetRepositoryǁfind_by_period__mutmut_9, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_10': xǁBudgetRepositoryǁfind_by_period__mutmut_10, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_11': xǁBudgetRepositoryǁfind_by_period__mutmut_11, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_12': xǁBudgetRepositoryǁfind_by_period__mutmut_12, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_13': xǁBudgetRepositoryǁfind_by_period__mutmut_13, 
        'xǁBudgetRepositoryǁfind_by_period__mutmut_14': xǁBudgetRepositoryǁfind_by_period__mutmut_14
    }
    
    def find_by_period(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁfind_by_period__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁfind_by_period__mutmut_mutants"), args, kwargs, self)
        return result 
    
    find_by_period.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁfind_by_period__mutmut_orig)
    xǁBudgetRepositoryǁfind_by_period__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁfind_by_period'

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_orig(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_1(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            None,
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_2(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=None,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_3(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_4(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_5(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("XXuser_idXX", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_6(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("USER_ID", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_7(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("XXcategory_idXX", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_8(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("CATEGORY_ID", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_9(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("XXyearXX", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_10(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("YEAR", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_11(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("XXmonthXX", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_12(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("MONTH", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_13(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=False,
        )
        self._indexes_ready = True

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_14(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = None

    async def xǁBudgetRepositoryǁ_ensure_indexes__mutmut_15(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(
            [
                ("user_id", ASCENDING),
                ("category_id", ASCENDING),
                ("year", ASCENDING),
                ("month", ASCENDING),
            ],
            unique=True,
        )
        self._indexes_ready = False
    
    xǁBudgetRepositoryǁ_ensure_indexes__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_1': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_1, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_2': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_2, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_3': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_3, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_4': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_4, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_5': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_5, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_6': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_6, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_7': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_7, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_8': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_8, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_9': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_9, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_10': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_10, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_11': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_11, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_12': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_12, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_13': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_13, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_14': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_14, 
        'xǁBudgetRepositoryǁ_ensure_indexes__mutmut_15': xǁBudgetRepositoryǁ_ensure_indexes__mutmut_15
    }
    
    def _ensure_indexes(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBudgetRepositoryǁ_ensure_indexes__mutmut_orig"), object.__getattribute__(self, "xǁBudgetRepositoryǁ_ensure_indexes__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_indexes.__signature__ = _mutmut_signature(xǁBudgetRepositoryǁ_ensure_indexes__mutmut_orig)
    xǁBudgetRepositoryǁ_ensure_indexes__mutmut_orig.__name__ = 'xǁBudgetRepositoryǁ_ensure_indexes'


class InMemoryBudgetRepository(Repository[Budget, str]):
    """In-memory repository for budgets."""

    def xǁInMemoryBudgetRepositoryǁ__init____mutmut_orig(self) -> None:
        self._storage: Dict[str, Budget] = {}

    def xǁInMemoryBudgetRepositoryǁ__init____mutmut_1(self) -> None:
        self._storage: Dict[str, Budget] = None
    
    xǁInMemoryBudgetRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁ__init____mutmut_1': xǁInMemoryBudgetRepositoryǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁ__init____mutmut_orig)
    xǁInMemoryBudgetRepositoryǁ__init____mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁ__init__'

    async def xǁInMemoryBudgetRepositoryǁcreate__mutmut_orig(self, entity: Budget) -> Budget:
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryBudgetRepositoryǁcreate__mutmut_1(self, entity: Budget) -> Budget:
        self._storage[entity.id] = None
        return entity
    
    xǁInMemoryBudgetRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁcreate__mutmut_1': xǁInMemoryBudgetRepositoryǁcreate__mutmut_1
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁcreate__mutmut_orig)
    xǁInMemoryBudgetRepositoryǁcreate__mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁcreate'

    async def xǁInMemoryBudgetRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Budget]:
        return self._storage.get(entity_id)

    async def xǁInMemoryBudgetRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Budget]:
        return self._storage.get(None)
    
    xǁInMemoryBudgetRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁget__mutmut_1': xǁInMemoryBudgetRepositoryǁget__mutmut_1
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁget__mutmut_orig)
    xǁInMemoryBudgetRepositoryǁget__mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁget'

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Budget]:
        budgets = None
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Budget]:
        budgets = list(None)
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = None
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get(None)
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = None

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id != user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = None
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get(None)
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("XXcategory_idXX")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("CATEGORY_ID")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = None

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id != category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = None
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get(None)
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("XXyearXX")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("YEAR")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = None

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year != year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = None
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get(None)
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("XXmonthXX")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("MONTH")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = None

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month != month]

        budgets.sort(key=lambda item: (item.year, item.month))
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=None)
        return budgets

    async def xǁInMemoryBudgetRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Budget]:
        budgets = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            budgets = [budget for budget in budgets if budget.user_id == user_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            budgets = [budget for budget in budgets if budget.category_id == category_id]

        year = filters.get("year")
        if isinstance(year, int):
            budgets = [budget for budget in budgets if budget.year == year]

        month = filters.get("month")
        if isinstance(month, int):
            budgets = [budget for budget in budgets if budget.month == month]

        budgets.sort(key=lambda item: None)
        return budgets
    
    xǁInMemoryBudgetRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁlist__mutmut_1': xǁInMemoryBudgetRepositoryǁlist__mutmut_1, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_2': xǁInMemoryBudgetRepositoryǁlist__mutmut_2, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_3': xǁInMemoryBudgetRepositoryǁlist__mutmut_3, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_4': xǁInMemoryBudgetRepositoryǁlist__mutmut_4, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_5': xǁInMemoryBudgetRepositoryǁlist__mutmut_5, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_6': xǁInMemoryBudgetRepositoryǁlist__mutmut_6, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_7': xǁInMemoryBudgetRepositoryǁlist__mutmut_7, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_8': xǁInMemoryBudgetRepositoryǁlist__mutmut_8, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_9': xǁInMemoryBudgetRepositoryǁlist__mutmut_9, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_10': xǁInMemoryBudgetRepositoryǁlist__mutmut_10, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_11': xǁInMemoryBudgetRepositoryǁlist__mutmut_11, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_12': xǁInMemoryBudgetRepositoryǁlist__mutmut_12, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_13': xǁInMemoryBudgetRepositoryǁlist__mutmut_13, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_14': xǁInMemoryBudgetRepositoryǁlist__mutmut_14, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_15': xǁInMemoryBudgetRepositoryǁlist__mutmut_15, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_16': xǁInMemoryBudgetRepositoryǁlist__mutmut_16, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_17': xǁInMemoryBudgetRepositoryǁlist__mutmut_17, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_18': xǁInMemoryBudgetRepositoryǁlist__mutmut_18, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_19': xǁInMemoryBudgetRepositoryǁlist__mutmut_19, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_20': xǁInMemoryBudgetRepositoryǁlist__mutmut_20, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_21': xǁInMemoryBudgetRepositoryǁlist__mutmut_21, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_22': xǁInMemoryBudgetRepositoryǁlist__mutmut_22, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_23': xǁInMemoryBudgetRepositoryǁlist__mutmut_23, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_24': xǁInMemoryBudgetRepositoryǁlist__mutmut_24, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_25': xǁInMemoryBudgetRepositoryǁlist__mutmut_25, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_26': xǁInMemoryBudgetRepositoryǁlist__mutmut_26, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_27': xǁInMemoryBudgetRepositoryǁlist__mutmut_27, 
        'xǁInMemoryBudgetRepositoryǁlist__mutmut_28': xǁInMemoryBudgetRepositoryǁlist__mutmut_28
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁlist__mutmut_orig)
    xǁInMemoryBudgetRepositoryǁlist__mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁlist'

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = None
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(None)
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if not budget:
            return None
        updated_data = None
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(None)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = None
        self._storage[entity_id] = updated_budget
        return updated_budget

    async def xǁInMemoryBudgetRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Budget]:
        budget = await self.get(entity_id)
        if not budget:
            return None
        updated_data = budget.model_dump()
        updated_data.update(data)
        updated_budget = Budget(**updated_data)
        self._storage[entity_id] = None
        return updated_budget
    
    xǁInMemoryBudgetRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁupdate__mutmut_1': xǁInMemoryBudgetRepositoryǁupdate__mutmut_1, 
        'xǁInMemoryBudgetRepositoryǁupdate__mutmut_2': xǁInMemoryBudgetRepositoryǁupdate__mutmut_2, 
        'xǁInMemoryBudgetRepositoryǁupdate__mutmut_3': xǁInMemoryBudgetRepositoryǁupdate__mutmut_3, 
        'xǁInMemoryBudgetRepositoryǁupdate__mutmut_4': xǁInMemoryBudgetRepositoryǁupdate__mutmut_4, 
        'xǁInMemoryBudgetRepositoryǁupdate__mutmut_5': xǁInMemoryBudgetRepositoryǁupdate__mutmut_5, 
        'xǁInMemoryBudgetRepositoryǁupdate__mutmut_6': xǁInMemoryBudgetRepositoryǁupdate__mutmut_6, 
        'xǁInMemoryBudgetRepositoryǁupdate__mutmut_7': xǁInMemoryBudgetRepositoryǁupdate__mutmut_7
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁupdate__mutmut_orig)
    xǁInMemoryBudgetRepositoryǁupdate__mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁupdate'

    async def xǁInMemoryBudgetRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def xǁInMemoryBudgetRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        return self._storage.pop(None, None) is not None

    async def xǁInMemoryBudgetRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        return self._storage.pop(None) is not None

    async def xǁInMemoryBudgetRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, ) is not None

    async def xǁInMemoryBudgetRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is None
    
    xǁInMemoryBudgetRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁdelete__mutmut_1': xǁInMemoryBudgetRepositoryǁdelete__mutmut_1, 
        'xǁInMemoryBudgetRepositoryǁdelete__mutmut_2': xǁInMemoryBudgetRepositoryǁdelete__mutmut_2, 
        'xǁInMemoryBudgetRepositoryǁdelete__mutmut_3': xǁInMemoryBudgetRepositoryǁdelete__mutmut_3, 
        'xǁInMemoryBudgetRepositoryǁdelete__mutmut_4': xǁInMemoryBudgetRepositoryǁdelete__mutmut_4
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁdelete__mutmut_orig)
    xǁInMemoryBudgetRepositoryǁdelete__mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁdelete'

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_orig(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id == category_id
                and budget.year == year
                and budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_1(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id == category_id
                and budget.year == year or budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_2(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id == category_id or budget.year == year
                and budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_3(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id or budget.category_id == category_id
                and budget.year == year
                and budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_4(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id != user_id
                and budget.category_id == category_id
                and budget.year == year
                and budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_5(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id != category_id
                and budget.year == year
                and budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_6(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id == category_id
                and budget.year != year
                and budget.month == month
            ):
                return budget
        return None

    async def xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_7(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Optional[Budget]:
        for budget in self._storage.values():
            if (
                budget.user_id == user_id
                and budget.category_id == category_id
                and budget.year == year
                and budget.month != month
            ):
                return budget
        return None
    
    xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_1': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_1, 
        'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_2': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_2, 
        'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_3': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_3, 
        'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_4': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_4, 
        'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_5': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_5, 
        'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_6': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_6, 
        'xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_7': xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_7
    }
    
    def find_by_period(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_mutants"), args, kwargs, self)
        return result 
    
    find_by_period.__signature__ = _mutmut_signature(xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_orig)
    xǁInMemoryBudgetRepositoryǁfind_by_period__mutmut_orig.__name__ = 'xǁInMemoryBudgetRepositoryǁfind_by_period'


def x__budget_to_document__mutmut_orig(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_1(budget: Budget) -> Dict[str, object]:
    data = None
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_2(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = None
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_3(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["XX_idXX"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_4(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_ID"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_5(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(None)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_6(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = None
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_7(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["XXuser_idXX"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_8(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["USER_ID"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_9(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(None)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_10(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = None
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_11(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["XXcategory_idXX"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_12(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["CATEGORY_ID"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_13(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(None)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_14(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = None
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_15(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["XXamountXX"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_16(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["AMOUNT"] = Decimal128(str(budget.amount))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_17(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(None)
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_18(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(None))
    data.pop("id", None)
    return data


def x__budget_to_document__mutmut_19(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop(None, None)
    return data


def x__budget_to_document__mutmut_20(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop(None)
    return data


def x__budget_to_document__mutmut_21(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("id", )
    return data


def x__budget_to_document__mutmut_22(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("XXidXX", None)
    return data


def x__budget_to_document__mutmut_23(budget: Budget) -> Dict[str, object]:
    data = budget.model_dump()
    data["_id"] = ensure_object_id(budget.id)
    data["user_id"] = ensure_object_id(budget.user_id)
    data["category_id"] = ensure_object_id(budget.category_id)
    data["amount"] = Decimal128(str(budget.amount))
    data.pop("ID", None)
    return data

x__budget_to_document__mutmut_mutants : ClassVar[MutantDict] = {
'x__budget_to_document__mutmut_1': x__budget_to_document__mutmut_1, 
    'x__budget_to_document__mutmut_2': x__budget_to_document__mutmut_2, 
    'x__budget_to_document__mutmut_3': x__budget_to_document__mutmut_3, 
    'x__budget_to_document__mutmut_4': x__budget_to_document__mutmut_4, 
    'x__budget_to_document__mutmut_5': x__budget_to_document__mutmut_5, 
    'x__budget_to_document__mutmut_6': x__budget_to_document__mutmut_6, 
    'x__budget_to_document__mutmut_7': x__budget_to_document__mutmut_7, 
    'x__budget_to_document__mutmut_8': x__budget_to_document__mutmut_8, 
    'x__budget_to_document__mutmut_9': x__budget_to_document__mutmut_9, 
    'x__budget_to_document__mutmut_10': x__budget_to_document__mutmut_10, 
    'x__budget_to_document__mutmut_11': x__budget_to_document__mutmut_11, 
    'x__budget_to_document__mutmut_12': x__budget_to_document__mutmut_12, 
    'x__budget_to_document__mutmut_13': x__budget_to_document__mutmut_13, 
    'x__budget_to_document__mutmut_14': x__budget_to_document__mutmut_14, 
    'x__budget_to_document__mutmut_15': x__budget_to_document__mutmut_15, 
    'x__budget_to_document__mutmut_16': x__budget_to_document__mutmut_16, 
    'x__budget_to_document__mutmut_17': x__budget_to_document__mutmut_17, 
    'x__budget_to_document__mutmut_18': x__budget_to_document__mutmut_18, 
    'x__budget_to_document__mutmut_19': x__budget_to_document__mutmut_19, 
    'x__budget_to_document__mutmut_20': x__budget_to_document__mutmut_20, 
    'x__budget_to_document__mutmut_21': x__budget_to_document__mutmut_21, 
    'x__budget_to_document__mutmut_22': x__budget_to_document__mutmut_22, 
    'x__budget_to_document__mutmut_23': x__budget_to_document__mutmut_23
}

def _budget_to_document(*args, **kwargs):
    result = _mutmut_trampoline(x__budget_to_document__mutmut_orig, x__budget_to_document__mutmut_mutants, args, kwargs)
    return result 

_budget_to_document.__signature__ = _mutmut_signature(x__budget_to_document__mutmut_orig)
x__budget_to_document__mutmut_orig.__name__ = 'x__budget_to_document'


def x__document_to_budget__mutmut_orig(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_1(document: Dict[str, object]) -> Budget:
    document = None
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_2(document: Dict[str, object]) -> Budget:
    document = dict(None)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_3(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = None
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_4(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["XXidXX"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_5(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["ID"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_6(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(None)
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_7(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop(None))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_8(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("XX_idXX"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_9(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_ID"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_10(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = None
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_11(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["XXuser_idXX"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_12(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["USER_ID"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_13(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(None)
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_14(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["XXuser_idXX"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_15(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["USER_ID"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_16(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = None
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_17(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["XXcategory_idXX"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_18(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["CATEGORY_ID"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_19(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(None)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_20(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["XXcategory_idXX"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_21(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["CATEGORY_ID"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_22(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = None
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_23(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get(None, Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_24(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", None)
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_25(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get(Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_26(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", )
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_27(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("XXamountXX", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_28(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("AMOUNT", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_29(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal(None))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_30(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("XX0XX"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_31(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = None
    return Budget(**document)


def x__document_to_budget__mutmut_32(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["XXamountXX"] = amount.to_decimal()
    return Budget(**document)


def x__document_to_budget__mutmut_33(document: Dict[str, object]) -> Budget:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["category_id"] = str(document["category_id"])
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["AMOUNT"] = amount.to_decimal()
    return Budget(**document)

x__document_to_budget__mutmut_mutants : ClassVar[MutantDict] = {
'x__document_to_budget__mutmut_1': x__document_to_budget__mutmut_1, 
    'x__document_to_budget__mutmut_2': x__document_to_budget__mutmut_2, 
    'x__document_to_budget__mutmut_3': x__document_to_budget__mutmut_3, 
    'x__document_to_budget__mutmut_4': x__document_to_budget__mutmut_4, 
    'x__document_to_budget__mutmut_5': x__document_to_budget__mutmut_5, 
    'x__document_to_budget__mutmut_6': x__document_to_budget__mutmut_6, 
    'x__document_to_budget__mutmut_7': x__document_to_budget__mutmut_7, 
    'x__document_to_budget__mutmut_8': x__document_to_budget__mutmut_8, 
    'x__document_to_budget__mutmut_9': x__document_to_budget__mutmut_9, 
    'x__document_to_budget__mutmut_10': x__document_to_budget__mutmut_10, 
    'x__document_to_budget__mutmut_11': x__document_to_budget__mutmut_11, 
    'x__document_to_budget__mutmut_12': x__document_to_budget__mutmut_12, 
    'x__document_to_budget__mutmut_13': x__document_to_budget__mutmut_13, 
    'x__document_to_budget__mutmut_14': x__document_to_budget__mutmut_14, 
    'x__document_to_budget__mutmut_15': x__document_to_budget__mutmut_15, 
    'x__document_to_budget__mutmut_16': x__document_to_budget__mutmut_16, 
    'x__document_to_budget__mutmut_17': x__document_to_budget__mutmut_17, 
    'x__document_to_budget__mutmut_18': x__document_to_budget__mutmut_18, 
    'x__document_to_budget__mutmut_19': x__document_to_budget__mutmut_19, 
    'x__document_to_budget__mutmut_20': x__document_to_budget__mutmut_20, 
    'x__document_to_budget__mutmut_21': x__document_to_budget__mutmut_21, 
    'x__document_to_budget__mutmut_22': x__document_to_budget__mutmut_22, 
    'x__document_to_budget__mutmut_23': x__document_to_budget__mutmut_23, 
    'x__document_to_budget__mutmut_24': x__document_to_budget__mutmut_24, 
    'x__document_to_budget__mutmut_25': x__document_to_budget__mutmut_25, 
    'x__document_to_budget__mutmut_26': x__document_to_budget__mutmut_26, 
    'x__document_to_budget__mutmut_27': x__document_to_budget__mutmut_27, 
    'x__document_to_budget__mutmut_28': x__document_to_budget__mutmut_28, 
    'x__document_to_budget__mutmut_29': x__document_to_budget__mutmut_29, 
    'x__document_to_budget__mutmut_30': x__document_to_budget__mutmut_30, 
    'x__document_to_budget__mutmut_31': x__document_to_budget__mutmut_31, 
    'x__document_to_budget__mutmut_32': x__document_to_budget__mutmut_32, 
    'x__document_to_budget__mutmut_33': x__document_to_budget__mutmut_33
}

def _document_to_budget(*args, **kwargs):
    result = _mutmut_trampoline(x__document_to_budget__mutmut_orig, x__document_to_budget__mutmut_mutants, args, kwargs)
    return result 

_document_to_budget.__signature__ = _mutmut_signature(x__document_to_budget__mutmut_orig)
x__document_to_budget__mutmut_orig.__name__ = 'x__document_to_budget'


def x__prepare_budget_update__mutmut_orig(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_1(data: Dict[str, object]) -> Dict[str, object]:
    update_data = None
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_2(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(None)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_3(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "XXuser_idXX" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_4(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "USER_ID" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_5(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" not in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_6(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = None
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_7(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["XXuser_idXX"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_8(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["USER_ID"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_9(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(None)
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_10(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(None))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_11(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["XXuser_idXX"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_12(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["USER_ID"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_13(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "XXcategory_idXX" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_14(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "CATEGORY_ID" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_15(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" not in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_16(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = None
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_17(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["XXcategory_idXX"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_18(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["CATEGORY_ID"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_19(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(None)
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_20(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(None))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_21(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["XXcategory_idXX"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_22(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["CATEGORY_ID"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_23(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data or update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_24(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "XXamountXX" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_25(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "AMOUNT" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_26(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" not in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_27(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["XXamountXX"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_28(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["AMOUNT"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_29(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_30(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = None
    return update_data


def x__prepare_budget_update__mutmut_31(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["XXamountXX"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_32(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["AMOUNT"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_budget_update__mutmut_33(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(None)
    return update_data


def x__prepare_budget_update__mutmut_34(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(None))
    return update_data


def x__prepare_budget_update__mutmut_35(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["XXamountXX"]))
    return update_data


def x__prepare_budget_update__mutmut_36(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["AMOUNT"]))
    return update_data

x__prepare_budget_update__mutmut_mutants : ClassVar[MutantDict] = {
'x__prepare_budget_update__mutmut_1': x__prepare_budget_update__mutmut_1, 
    'x__prepare_budget_update__mutmut_2': x__prepare_budget_update__mutmut_2, 
    'x__prepare_budget_update__mutmut_3': x__prepare_budget_update__mutmut_3, 
    'x__prepare_budget_update__mutmut_4': x__prepare_budget_update__mutmut_4, 
    'x__prepare_budget_update__mutmut_5': x__prepare_budget_update__mutmut_5, 
    'x__prepare_budget_update__mutmut_6': x__prepare_budget_update__mutmut_6, 
    'x__prepare_budget_update__mutmut_7': x__prepare_budget_update__mutmut_7, 
    'x__prepare_budget_update__mutmut_8': x__prepare_budget_update__mutmut_8, 
    'x__prepare_budget_update__mutmut_9': x__prepare_budget_update__mutmut_9, 
    'x__prepare_budget_update__mutmut_10': x__prepare_budget_update__mutmut_10, 
    'x__prepare_budget_update__mutmut_11': x__prepare_budget_update__mutmut_11, 
    'x__prepare_budget_update__mutmut_12': x__prepare_budget_update__mutmut_12, 
    'x__prepare_budget_update__mutmut_13': x__prepare_budget_update__mutmut_13, 
    'x__prepare_budget_update__mutmut_14': x__prepare_budget_update__mutmut_14, 
    'x__prepare_budget_update__mutmut_15': x__prepare_budget_update__mutmut_15, 
    'x__prepare_budget_update__mutmut_16': x__prepare_budget_update__mutmut_16, 
    'x__prepare_budget_update__mutmut_17': x__prepare_budget_update__mutmut_17, 
    'x__prepare_budget_update__mutmut_18': x__prepare_budget_update__mutmut_18, 
    'x__prepare_budget_update__mutmut_19': x__prepare_budget_update__mutmut_19, 
    'x__prepare_budget_update__mutmut_20': x__prepare_budget_update__mutmut_20, 
    'x__prepare_budget_update__mutmut_21': x__prepare_budget_update__mutmut_21, 
    'x__prepare_budget_update__mutmut_22': x__prepare_budget_update__mutmut_22, 
    'x__prepare_budget_update__mutmut_23': x__prepare_budget_update__mutmut_23, 
    'x__prepare_budget_update__mutmut_24': x__prepare_budget_update__mutmut_24, 
    'x__prepare_budget_update__mutmut_25': x__prepare_budget_update__mutmut_25, 
    'x__prepare_budget_update__mutmut_26': x__prepare_budget_update__mutmut_26, 
    'x__prepare_budget_update__mutmut_27': x__prepare_budget_update__mutmut_27, 
    'x__prepare_budget_update__mutmut_28': x__prepare_budget_update__mutmut_28, 
    'x__prepare_budget_update__mutmut_29': x__prepare_budget_update__mutmut_29, 
    'x__prepare_budget_update__mutmut_30': x__prepare_budget_update__mutmut_30, 
    'x__prepare_budget_update__mutmut_31': x__prepare_budget_update__mutmut_31, 
    'x__prepare_budget_update__mutmut_32': x__prepare_budget_update__mutmut_32, 
    'x__prepare_budget_update__mutmut_33': x__prepare_budget_update__mutmut_33, 
    'x__prepare_budget_update__mutmut_34': x__prepare_budget_update__mutmut_34, 
    'x__prepare_budget_update__mutmut_35': x__prepare_budget_update__mutmut_35, 
    'x__prepare_budget_update__mutmut_36': x__prepare_budget_update__mutmut_36
}

def _prepare_budget_update(*args, **kwargs):
    result = _mutmut_trampoline(x__prepare_budget_update__mutmut_orig, x__prepare_budget_update__mutmut_mutants, args, kwargs)
    return result 

_prepare_budget_update.__signature__ = _mutmut_signature(x__prepare_budget_update__mutmut_orig)
x__prepare_budget_update__mutmut_orig.__name__ = 'x__prepare_budget_update'
