"""Category repository implementations."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.models.category import Category
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


class CategoryRepository(Repository[Category, str]):
    """Mongo-backed repository for categories."""

    def xǁCategoryRepositoryǁ__init____mutmut_orig(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("categories")
        self._indexes_ready = False

    def xǁCategoryRepositoryǁ__init____mutmut_1(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = None
        self._indexes_ready = False

    def xǁCategoryRepositoryǁ__init____mutmut_2(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection(None)
        self._indexes_ready = False

    def xǁCategoryRepositoryǁ__init____mutmut_3(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("XXcategoriesXX")
        self._indexes_ready = False

    def xǁCategoryRepositoryǁ__init____mutmut_4(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("CATEGORIES")
        self._indexes_ready = False

    def xǁCategoryRepositoryǁ__init____mutmut_5(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("categories")
        self._indexes_ready = None

    def xǁCategoryRepositoryǁ__init____mutmut_6(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("categories")
        self._indexes_ready = True
    
    xǁCategoryRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁ__init____mutmut_1': xǁCategoryRepositoryǁ__init____mutmut_1, 
        'xǁCategoryRepositoryǁ__init____mutmut_2': xǁCategoryRepositoryǁ__init____mutmut_2, 
        'xǁCategoryRepositoryǁ__init____mutmut_3': xǁCategoryRepositoryǁ__init____mutmut_3, 
        'xǁCategoryRepositoryǁ__init____mutmut_4': xǁCategoryRepositoryǁ__init____mutmut_4, 
        'xǁCategoryRepositoryǁ__init____mutmut_5': xǁCategoryRepositoryǁ__init____mutmut_5, 
        'xǁCategoryRepositoryǁ__init____mutmut_6': xǁCategoryRepositoryǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁ__init____mutmut_orig)
    xǁCategoryRepositoryǁ__init____mutmut_orig.__name__ = 'xǁCategoryRepositoryǁ__init__'

    async def xǁCategoryRepositoryǁcreate__mutmut_orig(self, entity: Category) -> Category:
        await self._ensure_indexes()
        await self._collection.insert_one(_category_to_document(entity))
        return entity

    async def xǁCategoryRepositoryǁcreate__mutmut_1(self, entity: Category) -> Category:
        await self._ensure_indexes()
        await self._collection.insert_one(None)
        return entity

    async def xǁCategoryRepositoryǁcreate__mutmut_2(self, entity: Category) -> Category:
        await self._ensure_indexes()
        await self._collection.insert_one(_category_to_document(None))
        return entity
    
    xǁCategoryRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁcreate__mutmut_1': xǁCategoryRepositoryǁcreate__mutmut_1, 
        'xǁCategoryRepositoryǁcreate__mutmut_2': xǁCategoryRepositoryǁcreate__mutmut_2
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁcreate__mutmut_orig)
    xǁCategoryRepositoryǁcreate__mutmut_orig.__name__ = 'xǁCategoryRepositoryǁcreate'

    async def xǁCategoryRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Category]:
        document = None
        if not document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_2(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one(None)
        if not document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_3(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"XX_idXX": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_4(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"_ID": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_5(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"_id": ensure_object_id(None)})
        if not document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_6(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if document:
            return None
        return _document_to_category(document)

    async def xǁCategoryRepositoryǁget__mutmut_7(self, entity_id: str) -> Optional[Category]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_category(None)
    
    xǁCategoryRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁget__mutmut_1': xǁCategoryRepositoryǁget__mutmut_1, 
        'xǁCategoryRepositoryǁget__mutmut_2': xǁCategoryRepositoryǁget__mutmut_2, 
        'xǁCategoryRepositoryǁget__mutmut_3': xǁCategoryRepositoryǁget__mutmut_3, 
        'xǁCategoryRepositoryǁget__mutmut_4': xǁCategoryRepositoryǁget__mutmut_4, 
        'xǁCategoryRepositoryǁget__mutmut_5': xǁCategoryRepositoryǁget__mutmut_5, 
        'xǁCategoryRepositoryǁget__mutmut_6': xǁCategoryRepositoryǁget__mutmut_6, 
        'xǁCategoryRepositoryǁget__mutmut_7': xǁCategoryRepositoryǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁget__mutmut_orig)
    xǁCategoryRepositoryǁget__mutmut_orig.__name__ = 'xǁCategoryRepositoryǁget'

    async def xǁCategoryRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = None

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = None
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get(None)
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = None

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["XXuser_idXX"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["USER_ID"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(None)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = None
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get(None)
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("XXcategory_typeXX")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("CATEGORY_TYPE")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = None

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["XXcategory_typeXX"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["CATEGORY_TYPE"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = None
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get(None)
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("XXparent_idXX")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("PARENT_ID")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = None
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["XXparent_idXX"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["PARENT_ID"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(None)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None or "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is not None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "XXparent_idXX" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "PARENT_ID" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" not in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = ""

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["XXparent_idXX"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["PARENT_ID"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = None
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get(None)
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("XXnameXX")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("NAME")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_37(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = None

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_38(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["XXnameXX"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_39(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["NAME"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_40(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"XX$regexXX": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_41(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$REGEX": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_42(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "XX$optionsXX": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_43(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$OPTIONS": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_44(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "XXiXX"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_45(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "I"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_46(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = None
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_47(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort(None, ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_48(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", None)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_49(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort(ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_50(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", )
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_51(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(None).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_52(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.rfind(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_53(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("XXnameXX", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_54(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("NAME", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_55(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = None
        async for document in cursor:
            results.append(_document_to_category(document))
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_56(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(None)
        return results

    async def xǁCategoryRepositoryǁlist__mutmut_57(self, **filters: object) -> Iterable[Category]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            query["category_type"] = category_type

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            query["parent_id"] = ensure_object_id(parent_id)
        elif parent_id is None and "parent_id" in filters:
            query["parent_id"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("name", ASCENDING)
        results: List[Category] = []
        async for document in cursor:
            results.append(_document_to_category(None))
        return results
    
    xǁCategoryRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁlist__mutmut_1': xǁCategoryRepositoryǁlist__mutmut_1, 
        'xǁCategoryRepositoryǁlist__mutmut_2': xǁCategoryRepositoryǁlist__mutmut_2, 
        'xǁCategoryRepositoryǁlist__mutmut_3': xǁCategoryRepositoryǁlist__mutmut_3, 
        'xǁCategoryRepositoryǁlist__mutmut_4': xǁCategoryRepositoryǁlist__mutmut_4, 
        'xǁCategoryRepositoryǁlist__mutmut_5': xǁCategoryRepositoryǁlist__mutmut_5, 
        'xǁCategoryRepositoryǁlist__mutmut_6': xǁCategoryRepositoryǁlist__mutmut_6, 
        'xǁCategoryRepositoryǁlist__mutmut_7': xǁCategoryRepositoryǁlist__mutmut_7, 
        'xǁCategoryRepositoryǁlist__mutmut_8': xǁCategoryRepositoryǁlist__mutmut_8, 
        'xǁCategoryRepositoryǁlist__mutmut_9': xǁCategoryRepositoryǁlist__mutmut_9, 
        'xǁCategoryRepositoryǁlist__mutmut_10': xǁCategoryRepositoryǁlist__mutmut_10, 
        'xǁCategoryRepositoryǁlist__mutmut_11': xǁCategoryRepositoryǁlist__mutmut_11, 
        'xǁCategoryRepositoryǁlist__mutmut_12': xǁCategoryRepositoryǁlist__mutmut_12, 
        'xǁCategoryRepositoryǁlist__mutmut_13': xǁCategoryRepositoryǁlist__mutmut_13, 
        'xǁCategoryRepositoryǁlist__mutmut_14': xǁCategoryRepositoryǁlist__mutmut_14, 
        'xǁCategoryRepositoryǁlist__mutmut_15': xǁCategoryRepositoryǁlist__mutmut_15, 
        'xǁCategoryRepositoryǁlist__mutmut_16': xǁCategoryRepositoryǁlist__mutmut_16, 
        'xǁCategoryRepositoryǁlist__mutmut_17': xǁCategoryRepositoryǁlist__mutmut_17, 
        'xǁCategoryRepositoryǁlist__mutmut_18': xǁCategoryRepositoryǁlist__mutmut_18, 
        'xǁCategoryRepositoryǁlist__mutmut_19': xǁCategoryRepositoryǁlist__mutmut_19, 
        'xǁCategoryRepositoryǁlist__mutmut_20': xǁCategoryRepositoryǁlist__mutmut_20, 
        'xǁCategoryRepositoryǁlist__mutmut_21': xǁCategoryRepositoryǁlist__mutmut_21, 
        'xǁCategoryRepositoryǁlist__mutmut_22': xǁCategoryRepositoryǁlist__mutmut_22, 
        'xǁCategoryRepositoryǁlist__mutmut_23': xǁCategoryRepositoryǁlist__mutmut_23, 
        'xǁCategoryRepositoryǁlist__mutmut_24': xǁCategoryRepositoryǁlist__mutmut_24, 
        'xǁCategoryRepositoryǁlist__mutmut_25': xǁCategoryRepositoryǁlist__mutmut_25, 
        'xǁCategoryRepositoryǁlist__mutmut_26': xǁCategoryRepositoryǁlist__mutmut_26, 
        'xǁCategoryRepositoryǁlist__mutmut_27': xǁCategoryRepositoryǁlist__mutmut_27, 
        'xǁCategoryRepositoryǁlist__mutmut_28': xǁCategoryRepositoryǁlist__mutmut_28, 
        'xǁCategoryRepositoryǁlist__mutmut_29': xǁCategoryRepositoryǁlist__mutmut_29, 
        'xǁCategoryRepositoryǁlist__mutmut_30': xǁCategoryRepositoryǁlist__mutmut_30, 
        'xǁCategoryRepositoryǁlist__mutmut_31': xǁCategoryRepositoryǁlist__mutmut_31, 
        'xǁCategoryRepositoryǁlist__mutmut_32': xǁCategoryRepositoryǁlist__mutmut_32, 
        'xǁCategoryRepositoryǁlist__mutmut_33': xǁCategoryRepositoryǁlist__mutmut_33, 
        'xǁCategoryRepositoryǁlist__mutmut_34': xǁCategoryRepositoryǁlist__mutmut_34, 
        'xǁCategoryRepositoryǁlist__mutmut_35': xǁCategoryRepositoryǁlist__mutmut_35, 
        'xǁCategoryRepositoryǁlist__mutmut_36': xǁCategoryRepositoryǁlist__mutmut_36, 
        'xǁCategoryRepositoryǁlist__mutmut_37': xǁCategoryRepositoryǁlist__mutmut_37, 
        'xǁCategoryRepositoryǁlist__mutmut_38': xǁCategoryRepositoryǁlist__mutmut_38, 
        'xǁCategoryRepositoryǁlist__mutmut_39': xǁCategoryRepositoryǁlist__mutmut_39, 
        'xǁCategoryRepositoryǁlist__mutmut_40': xǁCategoryRepositoryǁlist__mutmut_40, 
        'xǁCategoryRepositoryǁlist__mutmut_41': xǁCategoryRepositoryǁlist__mutmut_41, 
        'xǁCategoryRepositoryǁlist__mutmut_42': xǁCategoryRepositoryǁlist__mutmut_42, 
        'xǁCategoryRepositoryǁlist__mutmut_43': xǁCategoryRepositoryǁlist__mutmut_43, 
        'xǁCategoryRepositoryǁlist__mutmut_44': xǁCategoryRepositoryǁlist__mutmut_44, 
        'xǁCategoryRepositoryǁlist__mutmut_45': xǁCategoryRepositoryǁlist__mutmut_45, 
        'xǁCategoryRepositoryǁlist__mutmut_46': xǁCategoryRepositoryǁlist__mutmut_46, 
        'xǁCategoryRepositoryǁlist__mutmut_47': xǁCategoryRepositoryǁlist__mutmut_47, 
        'xǁCategoryRepositoryǁlist__mutmut_48': xǁCategoryRepositoryǁlist__mutmut_48, 
        'xǁCategoryRepositoryǁlist__mutmut_49': xǁCategoryRepositoryǁlist__mutmut_49, 
        'xǁCategoryRepositoryǁlist__mutmut_50': xǁCategoryRepositoryǁlist__mutmut_50, 
        'xǁCategoryRepositoryǁlist__mutmut_51': xǁCategoryRepositoryǁlist__mutmut_51, 
        'xǁCategoryRepositoryǁlist__mutmut_52': xǁCategoryRepositoryǁlist__mutmut_52, 
        'xǁCategoryRepositoryǁlist__mutmut_53': xǁCategoryRepositoryǁlist__mutmut_53, 
        'xǁCategoryRepositoryǁlist__mutmut_54': xǁCategoryRepositoryǁlist__mutmut_54, 
        'xǁCategoryRepositoryǁlist__mutmut_55': xǁCategoryRepositoryǁlist__mutmut_55, 
        'xǁCategoryRepositoryǁlist__mutmut_56': xǁCategoryRepositoryǁlist__mutmut_56, 
        'xǁCategoryRepositoryǁlist__mutmut_57': xǁCategoryRepositoryǁlist__mutmut_57
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁlist__mutmut_orig)
    xǁCategoryRepositoryǁlist__mutmut_orig.__name__ = 'xǁCategoryRepositoryǁlist'

    async def xǁCategoryRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(None)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
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
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(None)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = None
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            None,
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            None,
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_8(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=None,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_9(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_10(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_11(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_12(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"XX_idXX": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_13(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_ID": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_14(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(None)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_15(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"XX$setXX": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_16(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$SET": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_17(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return None
        return _document_to_category(result)

    async def xǁCategoryRepositoryǁupdate__mutmut_18(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_category_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_category(None)
    
    xǁCategoryRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁupdate__mutmut_1': xǁCategoryRepositoryǁupdate__mutmut_1, 
        'xǁCategoryRepositoryǁupdate__mutmut_2': xǁCategoryRepositoryǁupdate__mutmut_2, 
        'xǁCategoryRepositoryǁupdate__mutmut_3': xǁCategoryRepositoryǁupdate__mutmut_3, 
        'xǁCategoryRepositoryǁupdate__mutmut_4': xǁCategoryRepositoryǁupdate__mutmut_4, 
        'xǁCategoryRepositoryǁupdate__mutmut_5': xǁCategoryRepositoryǁupdate__mutmut_5, 
        'xǁCategoryRepositoryǁupdate__mutmut_6': xǁCategoryRepositoryǁupdate__mutmut_6, 
        'xǁCategoryRepositoryǁupdate__mutmut_7': xǁCategoryRepositoryǁupdate__mutmut_7, 
        'xǁCategoryRepositoryǁupdate__mutmut_8': xǁCategoryRepositoryǁupdate__mutmut_8, 
        'xǁCategoryRepositoryǁupdate__mutmut_9': xǁCategoryRepositoryǁupdate__mutmut_9, 
        'xǁCategoryRepositoryǁupdate__mutmut_10': xǁCategoryRepositoryǁupdate__mutmut_10, 
        'xǁCategoryRepositoryǁupdate__mutmut_11': xǁCategoryRepositoryǁupdate__mutmut_11, 
        'xǁCategoryRepositoryǁupdate__mutmut_12': xǁCategoryRepositoryǁupdate__mutmut_12, 
        'xǁCategoryRepositoryǁupdate__mutmut_13': xǁCategoryRepositoryǁupdate__mutmut_13, 
        'xǁCategoryRepositoryǁupdate__mutmut_14': xǁCategoryRepositoryǁupdate__mutmut_14, 
        'xǁCategoryRepositoryǁupdate__mutmut_15': xǁCategoryRepositoryǁupdate__mutmut_15, 
        'xǁCategoryRepositoryǁupdate__mutmut_16': xǁCategoryRepositoryǁupdate__mutmut_16, 
        'xǁCategoryRepositoryǁupdate__mutmut_17': xǁCategoryRepositoryǁupdate__mutmut_17, 
        'xǁCategoryRepositoryǁupdate__mutmut_18': xǁCategoryRepositoryǁupdate__mutmut_18
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁupdate__mutmut_orig)
    xǁCategoryRepositoryǁupdate__mutmut_orig.__name__ = 'xǁCategoryRepositoryǁupdate'

    async def xǁCategoryRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁCategoryRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        outcome = None
        return outcome.deleted_count > 0

    async def xǁCategoryRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one(None)
        return outcome.deleted_count > 0

    async def xǁCategoryRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"XX_idXX": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁCategoryRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_ID": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁCategoryRepositoryǁdelete__mutmut_5(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(None)})
        return outcome.deleted_count > 0

    async def xǁCategoryRepositoryǁdelete__mutmut_6(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count >= 0

    async def xǁCategoryRepositoryǁdelete__mutmut_7(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 1
    
    xǁCategoryRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁdelete__mutmut_1': xǁCategoryRepositoryǁdelete__mutmut_1, 
        'xǁCategoryRepositoryǁdelete__mutmut_2': xǁCategoryRepositoryǁdelete__mutmut_2, 
        'xǁCategoryRepositoryǁdelete__mutmut_3': xǁCategoryRepositoryǁdelete__mutmut_3, 
        'xǁCategoryRepositoryǁdelete__mutmut_4': xǁCategoryRepositoryǁdelete__mutmut_4, 
        'xǁCategoryRepositoryǁdelete__mutmut_5': xǁCategoryRepositoryǁdelete__mutmut_5, 
        'xǁCategoryRepositoryǁdelete__mutmut_6': xǁCategoryRepositoryǁdelete__mutmut_6, 
        'xǁCategoryRepositoryǁdelete__mutmut_7': xǁCategoryRepositoryǁdelete__mutmut_7
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁdelete__mutmut_orig)
    xǁCategoryRepositoryǁdelete__mutmut_orig.__name__ = 'xǁCategoryRepositoryǁdelete'

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_orig(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_1(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(None)
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_2(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("XXuser_idXX", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_3(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("USER_ID", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_4(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index(None)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_5(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("XXcategory_typeXX", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_6(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("CATEGORY_TYPE", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_7(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index(None)
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_8(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("XXnameXX", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_9(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("NAME", ASCENDING)])
        self._indexes_ready = True

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_10(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = None

    async def xǁCategoryRepositoryǁ_ensure_indexes__mutmut_11(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("category_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = False
    
    xǁCategoryRepositoryǁ_ensure_indexes__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_1': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_1, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_2': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_2, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_3': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_3, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_4': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_4, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_5': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_5, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_6': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_6, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_7': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_7, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_8': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_8, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_9': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_9, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_10': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_10, 
        'xǁCategoryRepositoryǁ_ensure_indexes__mutmut_11': xǁCategoryRepositoryǁ_ensure_indexes__mutmut_11
    }
    
    def _ensure_indexes(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCategoryRepositoryǁ_ensure_indexes__mutmut_orig"), object.__getattribute__(self, "xǁCategoryRepositoryǁ_ensure_indexes__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_indexes.__signature__ = _mutmut_signature(xǁCategoryRepositoryǁ_ensure_indexes__mutmut_orig)
    xǁCategoryRepositoryǁ_ensure_indexes__mutmut_orig.__name__ = 'xǁCategoryRepositoryǁ_ensure_indexes'


class InMemoryCategoryRepository(Repository[Category, str]):
    """In-memory repository for categories."""

    def xǁInMemoryCategoryRepositoryǁ__init____mutmut_orig(self) -> None:
        self._storage: Dict[str, Category] = {}

    def xǁInMemoryCategoryRepositoryǁ__init____mutmut_1(self) -> None:
        self._storage: Dict[str, Category] = None
    
    xǁInMemoryCategoryRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryCategoryRepositoryǁ__init____mutmut_1': xǁInMemoryCategoryRepositoryǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁInMemoryCategoryRepositoryǁ__init____mutmut_orig)
    xǁInMemoryCategoryRepositoryǁ__init____mutmut_orig.__name__ = 'xǁInMemoryCategoryRepositoryǁ__init__'

    async def xǁInMemoryCategoryRepositoryǁcreate__mutmut_orig(self, entity: Category) -> Category:
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryCategoryRepositoryǁcreate__mutmut_1(self, entity: Category) -> Category:
        self._storage[entity.id] = None
        return entity
    
    xǁInMemoryCategoryRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryCategoryRepositoryǁcreate__mutmut_1': xǁInMemoryCategoryRepositoryǁcreate__mutmut_1
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁInMemoryCategoryRepositoryǁcreate__mutmut_orig)
    xǁInMemoryCategoryRepositoryǁcreate__mutmut_orig.__name__ = 'xǁInMemoryCategoryRepositoryǁcreate'

    async def xǁInMemoryCategoryRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Category]:
        return self._storage.get(entity_id)

    async def xǁInMemoryCategoryRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Category]:
        return self._storage.get(None)
    
    xǁInMemoryCategoryRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryCategoryRepositoryǁget__mutmut_1': xǁInMemoryCategoryRepositoryǁget__mutmut_1
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁInMemoryCategoryRepositoryǁget__mutmut_orig)
    xǁInMemoryCategoryRepositoryǁget__mutmut_orig.__name__ = 'xǁInMemoryCategoryRepositoryǁget'

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Category]:
        categories = None
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Category]:
        categories = list(None)
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = None
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get(None)
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = None

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id != user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = None
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get(None)
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("XXcategory_typeXX")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("CATEGORY_TYPE")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = None

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type != category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = None
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get(None)
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("XXparent_idXX")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("PARENT_ID")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = None
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id != parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None or "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is not None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "XXparent_idXX" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "PARENT_ID" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" not in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = None

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is not None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = None
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get(None)
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("XXnameXX")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("NAME")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = None
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.upper()
            categories = [cat for cat in categories if term in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = None

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term not in cat.name.lower()]

        return categories

    async def xǁInMemoryCategoryRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[Category]:
        categories = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            categories = [cat for cat in categories if cat.user_id == user_id]

        category_type = filters.get("category_type")
        if isinstance(category_type, str):
            categories = [cat for cat in categories if cat.category_type == category_type]

        parent_id = filters.get("parent_id")
        if isinstance(parent_id, str):
            categories = [cat for cat in categories if cat.parent_id == parent_id]
        elif parent_id is None and "parent_id" in filters:
            categories = [cat for cat in categories if cat.parent_id is None]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            categories = [cat for cat in categories if term in cat.name.upper()]

        return categories
    
    xǁInMemoryCategoryRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryCategoryRepositoryǁlist__mutmut_1': xǁInMemoryCategoryRepositoryǁlist__mutmut_1, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_2': xǁInMemoryCategoryRepositoryǁlist__mutmut_2, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_3': xǁInMemoryCategoryRepositoryǁlist__mutmut_3, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_4': xǁInMemoryCategoryRepositoryǁlist__mutmut_4, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_5': xǁInMemoryCategoryRepositoryǁlist__mutmut_5, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_6': xǁInMemoryCategoryRepositoryǁlist__mutmut_6, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_7': xǁInMemoryCategoryRepositoryǁlist__mutmut_7, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_8': xǁInMemoryCategoryRepositoryǁlist__mutmut_8, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_9': xǁInMemoryCategoryRepositoryǁlist__mutmut_9, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_10': xǁInMemoryCategoryRepositoryǁlist__mutmut_10, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_11': xǁInMemoryCategoryRepositoryǁlist__mutmut_11, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_12': xǁInMemoryCategoryRepositoryǁlist__mutmut_12, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_13': xǁInMemoryCategoryRepositoryǁlist__mutmut_13, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_14': xǁInMemoryCategoryRepositoryǁlist__mutmut_14, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_15': xǁInMemoryCategoryRepositoryǁlist__mutmut_15, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_16': xǁInMemoryCategoryRepositoryǁlist__mutmut_16, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_17': xǁInMemoryCategoryRepositoryǁlist__mutmut_17, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_18': xǁInMemoryCategoryRepositoryǁlist__mutmut_18, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_19': xǁInMemoryCategoryRepositoryǁlist__mutmut_19, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_20': xǁInMemoryCategoryRepositoryǁlist__mutmut_20, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_21': xǁInMemoryCategoryRepositoryǁlist__mutmut_21, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_22': xǁInMemoryCategoryRepositoryǁlist__mutmut_22, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_23': xǁInMemoryCategoryRepositoryǁlist__mutmut_23, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_24': xǁInMemoryCategoryRepositoryǁlist__mutmut_24, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_25': xǁInMemoryCategoryRepositoryǁlist__mutmut_25, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_26': xǁInMemoryCategoryRepositoryǁlist__mutmut_26, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_27': xǁInMemoryCategoryRepositoryǁlist__mutmut_27, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_28': xǁInMemoryCategoryRepositoryǁlist__mutmut_28, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_29': xǁInMemoryCategoryRepositoryǁlist__mutmut_29, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_30': xǁInMemoryCategoryRepositoryǁlist__mutmut_30, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_31': xǁInMemoryCategoryRepositoryǁlist__mutmut_31, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_32': xǁInMemoryCategoryRepositoryǁlist__mutmut_32, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_33': xǁInMemoryCategoryRepositoryǁlist__mutmut_33, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_34': xǁInMemoryCategoryRepositoryǁlist__mutmut_34, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_35': xǁInMemoryCategoryRepositoryǁlist__mutmut_35, 
        'xǁInMemoryCategoryRepositoryǁlist__mutmut_36': xǁInMemoryCategoryRepositoryǁlist__mutmut_36
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁInMemoryCategoryRepositoryǁlist__mutmut_orig)
    xǁInMemoryCategoryRepositoryǁlist__mutmut_orig.__name__ = 'xǁInMemoryCategoryRepositoryǁlist'

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = None
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(None)
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if not category:
            return None
        updated_data = None
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(None)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = None
        self._storage[entity_id] = updated_category
        return updated_category

    async def xǁInMemoryCategoryRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Category]:
        category = await self.get(entity_id)
        if not category:
            return None
        updated_data = category.model_dump()
        updated_data.update(data)
        updated_category = Category(**updated_data)
        self._storage[entity_id] = None
        return updated_category
    
    xǁInMemoryCategoryRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryCategoryRepositoryǁupdate__mutmut_1': xǁInMemoryCategoryRepositoryǁupdate__mutmut_1, 
        'xǁInMemoryCategoryRepositoryǁupdate__mutmut_2': xǁInMemoryCategoryRepositoryǁupdate__mutmut_2, 
        'xǁInMemoryCategoryRepositoryǁupdate__mutmut_3': xǁInMemoryCategoryRepositoryǁupdate__mutmut_3, 
        'xǁInMemoryCategoryRepositoryǁupdate__mutmut_4': xǁInMemoryCategoryRepositoryǁupdate__mutmut_4, 
        'xǁInMemoryCategoryRepositoryǁupdate__mutmut_5': xǁInMemoryCategoryRepositoryǁupdate__mutmut_5, 
        'xǁInMemoryCategoryRepositoryǁupdate__mutmut_6': xǁInMemoryCategoryRepositoryǁupdate__mutmut_6, 
        'xǁInMemoryCategoryRepositoryǁupdate__mutmut_7': xǁInMemoryCategoryRepositoryǁupdate__mutmut_7
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁInMemoryCategoryRepositoryǁupdate__mutmut_orig)
    xǁInMemoryCategoryRepositoryǁupdate__mutmut_orig.__name__ = 'xǁInMemoryCategoryRepositoryǁupdate'

    async def xǁInMemoryCategoryRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def xǁInMemoryCategoryRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        return self._storage.pop(None, None) is not None

    async def xǁInMemoryCategoryRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        return self._storage.pop(None) is not None

    async def xǁInMemoryCategoryRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, ) is not None

    async def xǁInMemoryCategoryRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is None
    
    xǁInMemoryCategoryRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryCategoryRepositoryǁdelete__mutmut_1': xǁInMemoryCategoryRepositoryǁdelete__mutmut_1, 
        'xǁInMemoryCategoryRepositoryǁdelete__mutmut_2': xǁInMemoryCategoryRepositoryǁdelete__mutmut_2, 
        'xǁInMemoryCategoryRepositoryǁdelete__mutmut_3': xǁInMemoryCategoryRepositoryǁdelete__mutmut_3, 
        'xǁInMemoryCategoryRepositoryǁdelete__mutmut_4': xǁInMemoryCategoryRepositoryǁdelete__mutmut_4
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryCategoryRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁInMemoryCategoryRepositoryǁdelete__mutmut_orig)
    xǁInMemoryCategoryRepositoryǁdelete__mutmut_orig.__name__ = 'xǁInMemoryCategoryRepositoryǁdelete'


def x__category_to_document__mutmut_orig(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_1(category: Category) -> Dict[str, object]:
    data = None
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_2(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = None
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_3(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["XX_idXX"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_4(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_ID"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_5(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(None)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_6(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = None
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_7(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["XXuser_idXX"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_8(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["USER_ID"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_9(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(None)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_10(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = None
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_11(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["XXparent_idXX"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_12(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["PARENT_ID"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_13(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(None)
    else:
        data["parent_id"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_14(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = ""
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_15(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["XXparent_idXX"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_16(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["PARENT_ID"] = None
    data.pop("id", None)
    return data


def x__category_to_document__mutmut_17(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop(None, None)
    return data


def x__category_to_document__mutmut_18(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop(None)
    return data


def x__category_to_document__mutmut_19(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("id", )
    return data


def x__category_to_document__mutmut_20(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("XXidXX", None)
    return data


def x__category_to_document__mutmut_21(category: Category) -> Dict[str, object]:
    data = category.model_dump()
    data["_id"] = ensure_object_id(category.id)
    data["user_id"] = ensure_object_id(category.user_id)
    if category.parent_id:
        data["parent_id"] = ensure_object_id(category.parent_id)
    else:
        data["parent_id"] = None
    data.pop("ID", None)
    return data

x__category_to_document__mutmut_mutants : ClassVar[MutantDict] = {
'x__category_to_document__mutmut_1': x__category_to_document__mutmut_1, 
    'x__category_to_document__mutmut_2': x__category_to_document__mutmut_2, 
    'x__category_to_document__mutmut_3': x__category_to_document__mutmut_3, 
    'x__category_to_document__mutmut_4': x__category_to_document__mutmut_4, 
    'x__category_to_document__mutmut_5': x__category_to_document__mutmut_5, 
    'x__category_to_document__mutmut_6': x__category_to_document__mutmut_6, 
    'x__category_to_document__mutmut_7': x__category_to_document__mutmut_7, 
    'x__category_to_document__mutmut_8': x__category_to_document__mutmut_8, 
    'x__category_to_document__mutmut_9': x__category_to_document__mutmut_9, 
    'x__category_to_document__mutmut_10': x__category_to_document__mutmut_10, 
    'x__category_to_document__mutmut_11': x__category_to_document__mutmut_11, 
    'x__category_to_document__mutmut_12': x__category_to_document__mutmut_12, 
    'x__category_to_document__mutmut_13': x__category_to_document__mutmut_13, 
    'x__category_to_document__mutmut_14': x__category_to_document__mutmut_14, 
    'x__category_to_document__mutmut_15': x__category_to_document__mutmut_15, 
    'x__category_to_document__mutmut_16': x__category_to_document__mutmut_16, 
    'x__category_to_document__mutmut_17': x__category_to_document__mutmut_17, 
    'x__category_to_document__mutmut_18': x__category_to_document__mutmut_18, 
    'x__category_to_document__mutmut_19': x__category_to_document__mutmut_19, 
    'x__category_to_document__mutmut_20': x__category_to_document__mutmut_20, 
    'x__category_to_document__mutmut_21': x__category_to_document__mutmut_21
}

def _category_to_document(*args, **kwargs):
    result = _mutmut_trampoline(x__category_to_document__mutmut_orig, x__category_to_document__mutmut_mutants, args, kwargs)
    return result 

_category_to_document.__signature__ = _mutmut_signature(x__category_to_document__mutmut_orig)
x__category_to_document__mutmut_orig.__name__ = 'x__category_to_document'


def x__document_to_category__mutmut_orig(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_1(document: Dict[str, object]) -> Category:
    document = None
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_2(document: Dict[str, object]) -> Category:
    document = dict(None)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_3(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = None
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_4(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["XXidXX"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_5(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["ID"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_6(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(None)
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_7(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop(None))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_8(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("XX_idXX"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_9(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_ID"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_10(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = None
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_11(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["XXuser_idXX"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_12(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["USER_ID"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_13(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(None)
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_14(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["XXuser_idXX"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_15(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["USER_ID"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_16(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = None
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_17(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get(None)
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_18(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("XXparent_idXX")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_19(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("PARENT_ID")
    if parent_id:
        document["parent_id"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_20(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = None
    return Category(**document)


def x__document_to_category__mutmut_21(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["XXparent_idXX"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_22(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["PARENT_ID"] = str(parent_id)
    return Category(**document)


def x__document_to_category__mutmut_23(document: Dict[str, object]) -> Category:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    parent_id = document.get("parent_id")
    if parent_id:
        document["parent_id"] = str(None)
    return Category(**document)

x__document_to_category__mutmut_mutants : ClassVar[MutantDict] = {
'x__document_to_category__mutmut_1': x__document_to_category__mutmut_1, 
    'x__document_to_category__mutmut_2': x__document_to_category__mutmut_2, 
    'x__document_to_category__mutmut_3': x__document_to_category__mutmut_3, 
    'x__document_to_category__mutmut_4': x__document_to_category__mutmut_4, 
    'x__document_to_category__mutmut_5': x__document_to_category__mutmut_5, 
    'x__document_to_category__mutmut_6': x__document_to_category__mutmut_6, 
    'x__document_to_category__mutmut_7': x__document_to_category__mutmut_7, 
    'x__document_to_category__mutmut_8': x__document_to_category__mutmut_8, 
    'x__document_to_category__mutmut_9': x__document_to_category__mutmut_9, 
    'x__document_to_category__mutmut_10': x__document_to_category__mutmut_10, 
    'x__document_to_category__mutmut_11': x__document_to_category__mutmut_11, 
    'x__document_to_category__mutmut_12': x__document_to_category__mutmut_12, 
    'x__document_to_category__mutmut_13': x__document_to_category__mutmut_13, 
    'x__document_to_category__mutmut_14': x__document_to_category__mutmut_14, 
    'x__document_to_category__mutmut_15': x__document_to_category__mutmut_15, 
    'x__document_to_category__mutmut_16': x__document_to_category__mutmut_16, 
    'x__document_to_category__mutmut_17': x__document_to_category__mutmut_17, 
    'x__document_to_category__mutmut_18': x__document_to_category__mutmut_18, 
    'x__document_to_category__mutmut_19': x__document_to_category__mutmut_19, 
    'x__document_to_category__mutmut_20': x__document_to_category__mutmut_20, 
    'x__document_to_category__mutmut_21': x__document_to_category__mutmut_21, 
    'x__document_to_category__mutmut_22': x__document_to_category__mutmut_22, 
    'x__document_to_category__mutmut_23': x__document_to_category__mutmut_23
}

def _document_to_category(*args, **kwargs):
    result = _mutmut_trampoline(x__document_to_category__mutmut_orig, x__document_to_category__mutmut_mutants, args, kwargs)
    return result 

_document_to_category.__signature__ = _mutmut_signature(x__document_to_category__mutmut_orig)
x__document_to_category__mutmut_orig.__name__ = 'x__document_to_category'


def x__prepare_category_update__mutmut_orig(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_1(data: Dict[str, object]) -> Dict[str, object]:
    update_data = None
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_2(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(None)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_3(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "XXuser_idXX" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_4(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "USER_ID" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_5(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" not in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_6(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = None
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_7(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["XXuser_idXX"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_8(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["USER_ID"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_9(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(None)
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_10(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(None))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_11(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["XXuser_idXX"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_12(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["USER_ID"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_13(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "XXparent_idXX" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_14(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "PARENT_ID" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_15(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" not in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_16(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = None
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_17(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["XXparent_idXX"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_18(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["PARENT_ID"]
        update_data["parent_id"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_19(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = None
    return update_data


def x__prepare_category_update__mutmut_20(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["XXparent_idXX"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_21(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["PARENT_ID"] = (
            ensure_object_id(str(parent_value)) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_22(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(None) if parent_value else None
        )
    return update_data


def x__prepare_category_update__mutmut_23(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "parent_id" in update_data:
        parent_value = update_data["parent_id"]
        update_data["parent_id"] = (
            ensure_object_id(str(None)) if parent_value else None
        )
    return update_data

x__prepare_category_update__mutmut_mutants : ClassVar[MutantDict] = {
'x__prepare_category_update__mutmut_1': x__prepare_category_update__mutmut_1, 
    'x__prepare_category_update__mutmut_2': x__prepare_category_update__mutmut_2, 
    'x__prepare_category_update__mutmut_3': x__prepare_category_update__mutmut_3, 
    'x__prepare_category_update__mutmut_4': x__prepare_category_update__mutmut_4, 
    'x__prepare_category_update__mutmut_5': x__prepare_category_update__mutmut_5, 
    'x__prepare_category_update__mutmut_6': x__prepare_category_update__mutmut_6, 
    'x__prepare_category_update__mutmut_7': x__prepare_category_update__mutmut_7, 
    'x__prepare_category_update__mutmut_8': x__prepare_category_update__mutmut_8, 
    'x__prepare_category_update__mutmut_9': x__prepare_category_update__mutmut_9, 
    'x__prepare_category_update__mutmut_10': x__prepare_category_update__mutmut_10, 
    'x__prepare_category_update__mutmut_11': x__prepare_category_update__mutmut_11, 
    'x__prepare_category_update__mutmut_12': x__prepare_category_update__mutmut_12, 
    'x__prepare_category_update__mutmut_13': x__prepare_category_update__mutmut_13, 
    'x__prepare_category_update__mutmut_14': x__prepare_category_update__mutmut_14, 
    'x__prepare_category_update__mutmut_15': x__prepare_category_update__mutmut_15, 
    'x__prepare_category_update__mutmut_16': x__prepare_category_update__mutmut_16, 
    'x__prepare_category_update__mutmut_17': x__prepare_category_update__mutmut_17, 
    'x__prepare_category_update__mutmut_18': x__prepare_category_update__mutmut_18, 
    'x__prepare_category_update__mutmut_19': x__prepare_category_update__mutmut_19, 
    'x__prepare_category_update__mutmut_20': x__prepare_category_update__mutmut_20, 
    'x__prepare_category_update__mutmut_21': x__prepare_category_update__mutmut_21, 
    'x__prepare_category_update__mutmut_22': x__prepare_category_update__mutmut_22, 
    'x__prepare_category_update__mutmut_23': x__prepare_category_update__mutmut_23
}

def _prepare_category_update(*args, **kwargs):
    result = _mutmut_trampoline(x__prepare_category_update__mutmut_orig, x__prepare_category_update__mutmut_mutants, args, kwargs)
    return result 

_prepare_category_update.__signature__ = _mutmut_signature(x__prepare_category_update__mutmut_orig)
x__prepare_category_update__mutmut_orig.__name__ = 'x__prepare_category_update'
