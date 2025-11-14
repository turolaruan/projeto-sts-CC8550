"""Account repository implementations."""

from __future__ import annotations

from decimal import Decimal
from typing import Dict, Iterable, List, Optional

from bson.decimal128 import Decimal128

from src.models.account import Account
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


class AccountRepository(Repository[Account, str]):
    """Mongo-backed repository for accounts."""

    def xǁAccountRepositoryǁ__init____mutmut_orig(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("accounts")
        self._indexes_ready = False

    def xǁAccountRepositoryǁ__init____mutmut_1(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = None
        self._indexes_ready = False

    def xǁAccountRepositoryǁ__init____mutmut_2(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection(None)
        self._indexes_ready = False

    def xǁAccountRepositoryǁ__init____mutmut_3(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("XXaccountsXX")
        self._indexes_ready = False

    def xǁAccountRepositoryǁ__init____mutmut_4(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("ACCOUNTS")
        self._indexes_ready = False

    def xǁAccountRepositoryǁ__init____mutmut_5(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("accounts")
        self._indexes_ready = None

    def xǁAccountRepositoryǁ__init____mutmut_6(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("accounts")
        self._indexes_ready = True
    
    xǁAccountRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁ__init____mutmut_1': xǁAccountRepositoryǁ__init____mutmut_1, 
        'xǁAccountRepositoryǁ__init____mutmut_2': xǁAccountRepositoryǁ__init____mutmut_2, 
        'xǁAccountRepositoryǁ__init____mutmut_3': xǁAccountRepositoryǁ__init____mutmut_3, 
        'xǁAccountRepositoryǁ__init____mutmut_4': xǁAccountRepositoryǁ__init____mutmut_4, 
        'xǁAccountRepositoryǁ__init____mutmut_5': xǁAccountRepositoryǁ__init____mutmut_5, 
        'xǁAccountRepositoryǁ__init____mutmut_6': xǁAccountRepositoryǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁAccountRepositoryǁ__init____mutmut_orig)
    xǁAccountRepositoryǁ__init____mutmut_orig.__name__ = 'xǁAccountRepositoryǁ__init__'

    async def xǁAccountRepositoryǁcreate__mutmut_orig(self, entity: Account) -> Account:
        await self._ensure_indexes()
        await self._collection.insert_one(_account_to_document(entity))
        return entity

    async def xǁAccountRepositoryǁcreate__mutmut_1(self, entity: Account) -> Account:
        await self._ensure_indexes()
        await self._collection.insert_one(None)
        return entity

    async def xǁAccountRepositoryǁcreate__mutmut_2(self, entity: Account) -> Account:
        await self._ensure_indexes()
        await self._collection.insert_one(_account_to_document(None))
        return entity
    
    xǁAccountRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁcreate__mutmut_1': xǁAccountRepositoryǁcreate__mutmut_1, 
        'xǁAccountRepositoryǁcreate__mutmut_2': xǁAccountRepositoryǁcreate__mutmut_2
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁAccountRepositoryǁcreate__mutmut_orig)
    xǁAccountRepositoryǁcreate__mutmut_orig.__name__ = 'xǁAccountRepositoryǁcreate'

    async def xǁAccountRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Account]:
        document = None
        if not document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_2(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one(None)
        if not document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_3(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"XX_idXX": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_4(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"_ID": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_5(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"_id": ensure_object_id(None)})
        if not document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_6(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if document:
            return None
        return _document_to_account(document)

    async def xǁAccountRepositoryǁget__mutmut_7(self, entity_id: str) -> Optional[Account]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_account(None)
    
    xǁAccountRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁget__mutmut_1': xǁAccountRepositoryǁget__mutmut_1, 
        'xǁAccountRepositoryǁget__mutmut_2': xǁAccountRepositoryǁget__mutmut_2, 
        'xǁAccountRepositoryǁget__mutmut_3': xǁAccountRepositoryǁget__mutmut_3, 
        'xǁAccountRepositoryǁget__mutmut_4': xǁAccountRepositoryǁget__mutmut_4, 
        'xǁAccountRepositoryǁget__mutmut_5': xǁAccountRepositoryǁget__mutmut_5, 
        'xǁAccountRepositoryǁget__mutmut_6': xǁAccountRepositoryǁget__mutmut_6, 
        'xǁAccountRepositoryǁget__mutmut_7': xǁAccountRepositoryǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁAccountRepositoryǁget__mutmut_orig)
    xǁAccountRepositoryǁget__mutmut_orig.__name__ = 'xǁAccountRepositoryǁget'

    async def xǁAccountRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = None

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = None
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get(None)
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = None

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["XXuser_idXX"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["USER_ID"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(None)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = None
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get(None)
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("XXaccount_typeXX")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("ACCOUNT_TYPE")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = None

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["XXaccount_typeXX"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["ACCOUNT_TYPE"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = None
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get(None)
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("XXcurrencyXX")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("CURRENCY")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = None

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["XXcurrencyXX"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["CURRENCY"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = None
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get(None)
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("XXnameXX")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("NAME")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = None

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["XXnameXX"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["NAME"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"XX$regexXX": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$REGEX": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "XX$optionsXX": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$OPTIONS": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "XXiXX"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "I"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_37(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = None
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_38(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort(None, ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_39(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", None)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_40(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort(ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_41(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", )
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_42(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(None).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_43(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.rfind(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_44(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("XXcreated_atXX", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_45(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("CREATED_AT", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_46(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = None
        async for document in cursor:
            results.append(_document_to_account(document))
        return results

    async def xǁAccountRepositoryǁlist__mutmut_47(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(None)
        return results

    async def xǁAccountRepositoryǁlist__mutmut_48(self, **filters: object) -> Iterable[Account]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            query["account_type"] = account_type

        currency = filters.get("currency")
        if isinstance(currency, str):
            query["currency"] = currency

        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[Account] = []
        async for document in cursor:
            results.append(_document_to_account(None))
        return results
    
    xǁAccountRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁlist__mutmut_1': xǁAccountRepositoryǁlist__mutmut_1, 
        'xǁAccountRepositoryǁlist__mutmut_2': xǁAccountRepositoryǁlist__mutmut_2, 
        'xǁAccountRepositoryǁlist__mutmut_3': xǁAccountRepositoryǁlist__mutmut_3, 
        'xǁAccountRepositoryǁlist__mutmut_4': xǁAccountRepositoryǁlist__mutmut_4, 
        'xǁAccountRepositoryǁlist__mutmut_5': xǁAccountRepositoryǁlist__mutmut_5, 
        'xǁAccountRepositoryǁlist__mutmut_6': xǁAccountRepositoryǁlist__mutmut_6, 
        'xǁAccountRepositoryǁlist__mutmut_7': xǁAccountRepositoryǁlist__mutmut_7, 
        'xǁAccountRepositoryǁlist__mutmut_8': xǁAccountRepositoryǁlist__mutmut_8, 
        'xǁAccountRepositoryǁlist__mutmut_9': xǁAccountRepositoryǁlist__mutmut_9, 
        'xǁAccountRepositoryǁlist__mutmut_10': xǁAccountRepositoryǁlist__mutmut_10, 
        'xǁAccountRepositoryǁlist__mutmut_11': xǁAccountRepositoryǁlist__mutmut_11, 
        'xǁAccountRepositoryǁlist__mutmut_12': xǁAccountRepositoryǁlist__mutmut_12, 
        'xǁAccountRepositoryǁlist__mutmut_13': xǁAccountRepositoryǁlist__mutmut_13, 
        'xǁAccountRepositoryǁlist__mutmut_14': xǁAccountRepositoryǁlist__mutmut_14, 
        'xǁAccountRepositoryǁlist__mutmut_15': xǁAccountRepositoryǁlist__mutmut_15, 
        'xǁAccountRepositoryǁlist__mutmut_16': xǁAccountRepositoryǁlist__mutmut_16, 
        'xǁAccountRepositoryǁlist__mutmut_17': xǁAccountRepositoryǁlist__mutmut_17, 
        'xǁAccountRepositoryǁlist__mutmut_18': xǁAccountRepositoryǁlist__mutmut_18, 
        'xǁAccountRepositoryǁlist__mutmut_19': xǁAccountRepositoryǁlist__mutmut_19, 
        'xǁAccountRepositoryǁlist__mutmut_20': xǁAccountRepositoryǁlist__mutmut_20, 
        'xǁAccountRepositoryǁlist__mutmut_21': xǁAccountRepositoryǁlist__mutmut_21, 
        'xǁAccountRepositoryǁlist__mutmut_22': xǁAccountRepositoryǁlist__mutmut_22, 
        'xǁAccountRepositoryǁlist__mutmut_23': xǁAccountRepositoryǁlist__mutmut_23, 
        'xǁAccountRepositoryǁlist__mutmut_24': xǁAccountRepositoryǁlist__mutmut_24, 
        'xǁAccountRepositoryǁlist__mutmut_25': xǁAccountRepositoryǁlist__mutmut_25, 
        'xǁAccountRepositoryǁlist__mutmut_26': xǁAccountRepositoryǁlist__mutmut_26, 
        'xǁAccountRepositoryǁlist__mutmut_27': xǁAccountRepositoryǁlist__mutmut_27, 
        'xǁAccountRepositoryǁlist__mutmut_28': xǁAccountRepositoryǁlist__mutmut_28, 
        'xǁAccountRepositoryǁlist__mutmut_29': xǁAccountRepositoryǁlist__mutmut_29, 
        'xǁAccountRepositoryǁlist__mutmut_30': xǁAccountRepositoryǁlist__mutmut_30, 
        'xǁAccountRepositoryǁlist__mutmut_31': xǁAccountRepositoryǁlist__mutmut_31, 
        'xǁAccountRepositoryǁlist__mutmut_32': xǁAccountRepositoryǁlist__mutmut_32, 
        'xǁAccountRepositoryǁlist__mutmut_33': xǁAccountRepositoryǁlist__mutmut_33, 
        'xǁAccountRepositoryǁlist__mutmut_34': xǁAccountRepositoryǁlist__mutmut_34, 
        'xǁAccountRepositoryǁlist__mutmut_35': xǁAccountRepositoryǁlist__mutmut_35, 
        'xǁAccountRepositoryǁlist__mutmut_36': xǁAccountRepositoryǁlist__mutmut_36, 
        'xǁAccountRepositoryǁlist__mutmut_37': xǁAccountRepositoryǁlist__mutmut_37, 
        'xǁAccountRepositoryǁlist__mutmut_38': xǁAccountRepositoryǁlist__mutmut_38, 
        'xǁAccountRepositoryǁlist__mutmut_39': xǁAccountRepositoryǁlist__mutmut_39, 
        'xǁAccountRepositoryǁlist__mutmut_40': xǁAccountRepositoryǁlist__mutmut_40, 
        'xǁAccountRepositoryǁlist__mutmut_41': xǁAccountRepositoryǁlist__mutmut_41, 
        'xǁAccountRepositoryǁlist__mutmut_42': xǁAccountRepositoryǁlist__mutmut_42, 
        'xǁAccountRepositoryǁlist__mutmut_43': xǁAccountRepositoryǁlist__mutmut_43, 
        'xǁAccountRepositoryǁlist__mutmut_44': xǁAccountRepositoryǁlist__mutmut_44, 
        'xǁAccountRepositoryǁlist__mutmut_45': xǁAccountRepositoryǁlist__mutmut_45, 
        'xǁAccountRepositoryǁlist__mutmut_46': xǁAccountRepositoryǁlist__mutmut_46, 
        'xǁAccountRepositoryǁlist__mutmut_47': xǁAccountRepositoryǁlist__mutmut_47, 
        'xǁAccountRepositoryǁlist__mutmut_48': xǁAccountRepositoryǁlist__mutmut_48
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁAccountRepositoryǁlist__mutmut_orig)
    xǁAccountRepositoryǁlist__mutmut_orig.__name__ = 'xǁAccountRepositoryǁlist'

    async def xǁAccountRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(None)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
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
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(None)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = None
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            None,
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            None,
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_8(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=None,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_9(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_10(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_11(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_12(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"XX_idXX": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_13(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_ID": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_14(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(None)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_15(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"XX$setXX": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_16(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$SET": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_17(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return None
        return _document_to_account(result)

    async def xǁAccountRepositoryǁupdate__mutmut_18(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_account_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_account(None)
    
    xǁAccountRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁupdate__mutmut_1': xǁAccountRepositoryǁupdate__mutmut_1, 
        'xǁAccountRepositoryǁupdate__mutmut_2': xǁAccountRepositoryǁupdate__mutmut_2, 
        'xǁAccountRepositoryǁupdate__mutmut_3': xǁAccountRepositoryǁupdate__mutmut_3, 
        'xǁAccountRepositoryǁupdate__mutmut_4': xǁAccountRepositoryǁupdate__mutmut_4, 
        'xǁAccountRepositoryǁupdate__mutmut_5': xǁAccountRepositoryǁupdate__mutmut_5, 
        'xǁAccountRepositoryǁupdate__mutmut_6': xǁAccountRepositoryǁupdate__mutmut_6, 
        'xǁAccountRepositoryǁupdate__mutmut_7': xǁAccountRepositoryǁupdate__mutmut_7, 
        'xǁAccountRepositoryǁupdate__mutmut_8': xǁAccountRepositoryǁupdate__mutmut_8, 
        'xǁAccountRepositoryǁupdate__mutmut_9': xǁAccountRepositoryǁupdate__mutmut_9, 
        'xǁAccountRepositoryǁupdate__mutmut_10': xǁAccountRepositoryǁupdate__mutmut_10, 
        'xǁAccountRepositoryǁupdate__mutmut_11': xǁAccountRepositoryǁupdate__mutmut_11, 
        'xǁAccountRepositoryǁupdate__mutmut_12': xǁAccountRepositoryǁupdate__mutmut_12, 
        'xǁAccountRepositoryǁupdate__mutmut_13': xǁAccountRepositoryǁupdate__mutmut_13, 
        'xǁAccountRepositoryǁupdate__mutmut_14': xǁAccountRepositoryǁupdate__mutmut_14, 
        'xǁAccountRepositoryǁupdate__mutmut_15': xǁAccountRepositoryǁupdate__mutmut_15, 
        'xǁAccountRepositoryǁupdate__mutmut_16': xǁAccountRepositoryǁupdate__mutmut_16, 
        'xǁAccountRepositoryǁupdate__mutmut_17': xǁAccountRepositoryǁupdate__mutmut_17, 
        'xǁAccountRepositoryǁupdate__mutmut_18': xǁAccountRepositoryǁupdate__mutmut_18
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁAccountRepositoryǁupdate__mutmut_orig)
    xǁAccountRepositoryǁupdate__mutmut_orig.__name__ = 'xǁAccountRepositoryǁupdate'

    async def xǁAccountRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁAccountRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        outcome = None
        return outcome.deleted_count > 0

    async def xǁAccountRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one(None)
        return outcome.deleted_count > 0

    async def xǁAccountRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"XX_idXX": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁAccountRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_ID": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁAccountRepositoryǁdelete__mutmut_5(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(None)})
        return outcome.deleted_count > 0

    async def xǁAccountRepositoryǁdelete__mutmut_6(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count >= 0

    async def xǁAccountRepositoryǁdelete__mutmut_7(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 1
    
    xǁAccountRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁdelete__mutmut_1': xǁAccountRepositoryǁdelete__mutmut_1, 
        'xǁAccountRepositoryǁdelete__mutmut_2': xǁAccountRepositoryǁdelete__mutmut_2, 
        'xǁAccountRepositoryǁdelete__mutmut_3': xǁAccountRepositoryǁdelete__mutmut_3, 
        'xǁAccountRepositoryǁdelete__mutmut_4': xǁAccountRepositoryǁdelete__mutmut_4, 
        'xǁAccountRepositoryǁdelete__mutmut_5': xǁAccountRepositoryǁdelete__mutmut_5, 
        'xǁAccountRepositoryǁdelete__mutmut_6': xǁAccountRepositoryǁdelete__mutmut_6, 
        'xǁAccountRepositoryǁdelete__mutmut_7': xǁAccountRepositoryǁdelete__mutmut_7
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁAccountRepositoryǁdelete__mutmut_orig)
    xǁAccountRepositoryǁdelete__mutmut_orig.__name__ = 'xǁAccountRepositoryǁdelete'

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_orig(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_1(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(None)
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_2(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("XXuser_idXX", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_3(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("USER_ID", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_4(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index(None)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_5(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("XXaccount_typeXX", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_6(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("ACCOUNT_TYPE", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_7(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index(None)
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_8(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("XXnameXX", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_9(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("NAME", ASCENDING)])
        self._indexes_ready = True

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_10(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = None

    async def xǁAccountRepositoryǁ_ensure_indexes__mutmut_11(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_type", ASCENDING)])
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = False
    
    xǁAccountRepositoryǁ_ensure_indexes__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountRepositoryǁ_ensure_indexes__mutmut_1': xǁAccountRepositoryǁ_ensure_indexes__mutmut_1, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_2': xǁAccountRepositoryǁ_ensure_indexes__mutmut_2, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_3': xǁAccountRepositoryǁ_ensure_indexes__mutmut_3, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_4': xǁAccountRepositoryǁ_ensure_indexes__mutmut_4, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_5': xǁAccountRepositoryǁ_ensure_indexes__mutmut_5, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_6': xǁAccountRepositoryǁ_ensure_indexes__mutmut_6, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_7': xǁAccountRepositoryǁ_ensure_indexes__mutmut_7, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_8': xǁAccountRepositoryǁ_ensure_indexes__mutmut_8, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_9': xǁAccountRepositoryǁ_ensure_indexes__mutmut_9, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_10': xǁAccountRepositoryǁ_ensure_indexes__mutmut_10, 
        'xǁAccountRepositoryǁ_ensure_indexes__mutmut_11': xǁAccountRepositoryǁ_ensure_indexes__mutmut_11
    }
    
    def _ensure_indexes(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountRepositoryǁ_ensure_indexes__mutmut_orig"), object.__getattribute__(self, "xǁAccountRepositoryǁ_ensure_indexes__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_indexes.__signature__ = _mutmut_signature(xǁAccountRepositoryǁ_ensure_indexes__mutmut_orig)
    xǁAccountRepositoryǁ_ensure_indexes__mutmut_orig.__name__ = 'xǁAccountRepositoryǁ_ensure_indexes'


class InMemoryAccountRepository(Repository[Account, str]):
    """In-memory repository for accounts (useful in tests)."""

    def xǁInMemoryAccountRepositoryǁ__init____mutmut_orig(self) -> None:
        self._storage: Dict[str, Account] = {}

    def xǁInMemoryAccountRepositoryǁ__init____mutmut_1(self) -> None:
        self._storage: Dict[str, Account] = None
    
    xǁInMemoryAccountRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryAccountRepositoryǁ__init____mutmut_1': xǁInMemoryAccountRepositoryǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁInMemoryAccountRepositoryǁ__init____mutmut_orig)
    xǁInMemoryAccountRepositoryǁ__init____mutmut_orig.__name__ = 'xǁInMemoryAccountRepositoryǁ__init__'

    async def xǁInMemoryAccountRepositoryǁcreate__mutmut_orig(self, entity: Account) -> Account:
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryAccountRepositoryǁcreate__mutmut_1(self, entity: Account) -> Account:
        self._storage[entity.id] = None
        return entity
    
    xǁInMemoryAccountRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryAccountRepositoryǁcreate__mutmut_1': xǁInMemoryAccountRepositoryǁcreate__mutmut_1
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁInMemoryAccountRepositoryǁcreate__mutmut_orig)
    xǁInMemoryAccountRepositoryǁcreate__mutmut_orig.__name__ = 'xǁInMemoryAccountRepositoryǁcreate'

    async def xǁInMemoryAccountRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Account]:
        return self._storage.get(entity_id)

    async def xǁInMemoryAccountRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Account]:
        return self._storage.get(None)
    
    xǁInMemoryAccountRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryAccountRepositoryǁget__mutmut_1': xǁInMemoryAccountRepositoryǁget__mutmut_1
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁInMemoryAccountRepositoryǁget__mutmut_orig)
    xǁInMemoryAccountRepositoryǁget__mutmut_orig.__name__ = 'xǁInMemoryAccountRepositoryǁget'

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Account]:
        accounts = None
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Account]:
        accounts = list(None)
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = None
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get(None)
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = None

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id != user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = None
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get(None)
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("XXaccount_typeXX")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("ACCOUNT_TYPE")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = None

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type != account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = None
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get(None)
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("XXcurrencyXX")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("CURRENCY")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = None

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency != currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = None
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get(None)
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("XXnameXX")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("NAME")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = None
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.upper()
            accounts = [acct for acct in accounts if term in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = None

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term not in acct.name.lower()]

        return accounts

    async def xǁInMemoryAccountRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Account]:
        accounts = list(self._storage.values())
        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            accounts = [acct for acct in accounts if acct.user_id == user_id]

        account_type = filters.get("account_type")
        if isinstance(account_type, str):
            accounts = [acct for acct in accounts if acct.account_type == account_type]

        currency = filters.get("currency")
        if isinstance(currency, str):
            accounts = [acct for acct in accounts if acct.currency == currency]

        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            accounts = [acct for acct in accounts if term in acct.name.upper()]

        return accounts
    
    xǁInMemoryAccountRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryAccountRepositoryǁlist__mutmut_1': xǁInMemoryAccountRepositoryǁlist__mutmut_1, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_2': xǁInMemoryAccountRepositoryǁlist__mutmut_2, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_3': xǁInMemoryAccountRepositoryǁlist__mutmut_3, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_4': xǁInMemoryAccountRepositoryǁlist__mutmut_4, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_5': xǁInMemoryAccountRepositoryǁlist__mutmut_5, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_6': xǁInMemoryAccountRepositoryǁlist__mutmut_6, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_7': xǁInMemoryAccountRepositoryǁlist__mutmut_7, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_8': xǁInMemoryAccountRepositoryǁlist__mutmut_8, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_9': xǁInMemoryAccountRepositoryǁlist__mutmut_9, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_10': xǁInMemoryAccountRepositoryǁlist__mutmut_10, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_11': xǁInMemoryAccountRepositoryǁlist__mutmut_11, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_12': xǁInMemoryAccountRepositoryǁlist__mutmut_12, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_13': xǁInMemoryAccountRepositoryǁlist__mutmut_13, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_14': xǁInMemoryAccountRepositoryǁlist__mutmut_14, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_15': xǁInMemoryAccountRepositoryǁlist__mutmut_15, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_16': xǁInMemoryAccountRepositoryǁlist__mutmut_16, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_17': xǁInMemoryAccountRepositoryǁlist__mutmut_17, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_18': xǁInMemoryAccountRepositoryǁlist__mutmut_18, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_19': xǁInMemoryAccountRepositoryǁlist__mutmut_19, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_20': xǁInMemoryAccountRepositoryǁlist__mutmut_20, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_21': xǁInMemoryAccountRepositoryǁlist__mutmut_21, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_22': xǁInMemoryAccountRepositoryǁlist__mutmut_22, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_23': xǁInMemoryAccountRepositoryǁlist__mutmut_23, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_24': xǁInMemoryAccountRepositoryǁlist__mutmut_24, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_25': xǁInMemoryAccountRepositoryǁlist__mutmut_25, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_26': xǁInMemoryAccountRepositoryǁlist__mutmut_26, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_27': xǁInMemoryAccountRepositoryǁlist__mutmut_27, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_28': xǁInMemoryAccountRepositoryǁlist__mutmut_28, 
        'xǁInMemoryAccountRepositoryǁlist__mutmut_29': xǁInMemoryAccountRepositoryǁlist__mutmut_29
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁInMemoryAccountRepositoryǁlist__mutmut_orig)
    xǁInMemoryAccountRepositoryǁlist__mutmut_orig.__name__ = 'xǁInMemoryAccountRepositoryǁlist'

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = None
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(None)
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if not account:
            return None
        updated_data = None
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(None)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = None
        self._storage[entity_id] = updated_account
        return updated_account

    async def xǁInMemoryAccountRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Account]:
        account = await self.get(entity_id)
        if not account:
            return None
        updated_data = account.model_dump()
        updated_data.update(data)
        updated_account = Account(**updated_data)
        self._storage[entity_id] = None
        return updated_account
    
    xǁInMemoryAccountRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryAccountRepositoryǁupdate__mutmut_1': xǁInMemoryAccountRepositoryǁupdate__mutmut_1, 
        'xǁInMemoryAccountRepositoryǁupdate__mutmut_2': xǁInMemoryAccountRepositoryǁupdate__mutmut_2, 
        'xǁInMemoryAccountRepositoryǁupdate__mutmut_3': xǁInMemoryAccountRepositoryǁupdate__mutmut_3, 
        'xǁInMemoryAccountRepositoryǁupdate__mutmut_4': xǁInMemoryAccountRepositoryǁupdate__mutmut_4, 
        'xǁInMemoryAccountRepositoryǁupdate__mutmut_5': xǁInMemoryAccountRepositoryǁupdate__mutmut_5, 
        'xǁInMemoryAccountRepositoryǁupdate__mutmut_6': xǁInMemoryAccountRepositoryǁupdate__mutmut_6, 
        'xǁInMemoryAccountRepositoryǁupdate__mutmut_7': xǁInMemoryAccountRepositoryǁupdate__mutmut_7
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁInMemoryAccountRepositoryǁupdate__mutmut_orig)
    xǁInMemoryAccountRepositoryǁupdate__mutmut_orig.__name__ = 'xǁInMemoryAccountRepositoryǁupdate'

    async def xǁInMemoryAccountRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def xǁInMemoryAccountRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        return self._storage.pop(None, None) is not None

    async def xǁInMemoryAccountRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        return self._storage.pop(None) is not None

    async def xǁInMemoryAccountRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, ) is not None

    async def xǁInMemoryAccountRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is None
    
    xǁInMemoryAccountRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryAccountRepositoryǁdelete__mutmut_1': xǁInMemoryAccountRepositoryǁdelete__mutmut_1, 
        'xǁInMemoryAccountRepositoryǁdelete__mutmut_2': xǁInMemoryAccountRepositoryǁdelete__mutmut_2, 
        'xǁInMemoryAccountRepositoryǁdelete__mutmut_3': xǁInMemoryAccountRepositoryǁdelete__mutmut_3, 
        'xǁInMemoryAccountRepositoryǁdelete__mutmut_4': xǁInMemoryAccountRepositoryǁdelete__mutmut_4
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryAccountRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁInMemoryAccountRepositoryǁdelete__mutmut_orig)
    xǁInMemoryAccountRepositoryǁdelete__mutmut_orig.__name__ = 'xǁInMemoryAccountRepositoryǁdelete'


def x__account_to_document__mutmut_orig(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_1(account: Account) -> Dict[str, object]:
    data = None
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_2(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = None
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_3(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["XX_idXX"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_4(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_ID"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_5(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(None)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_6(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = None
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_7(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["XXuser_idXX"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_8(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["USER_ID"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_9(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(None)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_10(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = None
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_11(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["XXbalanceXX"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_12(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["BALANCE"] = Decimal128(str(account.balance))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_13(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(None)
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_14(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(None))
    data.pop("id", None)
    return data


def x__account_to_document__mutmut_15(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop(None, None)
    return data


def x__account_to_document__mutmut_16(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop(None)
    return data


def x__account_to_document__mutmut_17(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("id", )
    return data


def x__account_to_document__mutmut_18(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("XXidXX", None)
    return data


def x__account_to_document__mutmut_19(account: Account) -> Dict[str, object]:
    data = account.model_dump()
    data["_id"] = ensure_object_id(account.id)
    data["user_id"] = ensure_object_id(account.user_id)
    data["balance"] = Decimal128(str(account.balance))
    data.pop("ID", None)
    return data

x__account_to_document__mutmut_mutants : ClassVar[MutantDict] = {
'x__account_to_document__mutmut_1': x__account_to_document__mutmut_1, 
    'x__account_to_document__mutmut_2': x__account_to_document__mutmut_2, 
    'x__account_to_document__mutmut_3': x__account_to_document__mutmut_3, 
    'x__account_to_document__mutmut_4': x__account_to_document__mutmut_4, 
    'x__account_to_document__mutmut_5': x__account_to_document__mutmut_5, 
    'x__account_to_document__mutmut_6': x__account_to_document__mutmut_6, 
    'x__account_to_document__mutmut_7': x__account_to_document__mutmut_7, 
    'x__account_to_document__mutmut_8': x__account_to_document__mutmut_8, 
    'x__account_to_document__mutmut_9': x__account_to_document__mutmut_9, 
    'x__account_to_document__mutmut_10': x__account_to_document__mutmut_10, 
    'x__account_to_document__mutmut_11': x__account_to_document__mutmut_11, 
    'x__account_to_document__mutmut_12': x__account_to_document__mutmut_12, 
    'x__account_to_document__mutmut_13': x__account_to_document__mutmut_13, 
    'x__account_to_document__mutmut_14': x__account_to_document__mutmut_14, 
    'x__account_to_document__mutmut_15': x__account_to_document__mutmut_15, 
    'x__account_to_document__mutmut_16': x__account_to_document__mutmut_16, 
    'x__account_to_document__mutmut_17': x__account_to_document__mutmut_17, 
    'x__account_to_document__mutmut_18': x__account_to_document__mutmut_18, 
    'x__account_to_document__mutmut_19': x__account_to_document__mutmut_19
}

def _account_to_document(*args, **kwargs):
    result = _mutmut_trampoline(x__account_to_document__mutmut_orig, x__account_to_document__mutmut_mutants, args, kwargs)
    return result 

_account_to_document.__signature__ = _mutmut_signature(x__account_to_document__mutmut_orig)
x__account_to_document__mutmut_orig.__name__ = 'x__account_to_document'


def x__document_to_account__mutmut_orig(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_1(document: Dict[str, object]) -> Account:
    document = None
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_2(document: Dict[str, object]) -> Account:
    document = dict(None)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_3(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = None
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_4(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["XXidXX"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_5(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["ID"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_6(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(None)
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_7(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop(None))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_8(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("XX_idXX"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_9(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_ID"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_10(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = None
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_11(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["XXuser_idXX"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_12(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["USER_ID"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_13(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(None)
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_14(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["XXuser_idXX"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_15(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["USER_ID"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_16(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = None
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_17(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get(None, Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_18(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", None)
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_19(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get(Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_20(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", )
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_21(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("XXbalanceXX", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_22(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("BALANCE", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_23(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal(None))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_24(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("XX0XX"))
    if isinstance(balance, Decimal128):
        document["balance"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_25(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["balance"] = None
    return Account(**document)


def x__document_to_account__mutmut_26(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["XXbalanceXX"] = balance.to_decimal()
    return Account(**document)


def x__document_to_account__mutmut_27(document: Dict[str, object]) -> Account:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    balance = document.get("balance", Decimal("0"))
    if isinstance(balance, Decimal128):
        document["BALANCE"] = balance.to_decimal()
    return Account(**document)

x__document_to_account__mutmut_mutants : ClassVar[MutantDict] = {
'x__document_to_account__mutmut_1': x__document_to_account__mutmut_1, 
    'x__document_to_account__mutmut_2': x__document_to_account__mutmut_2, 
    'x__document_to_account__mutmut_3': x__document_to_account__mutmut_3, 
    'x__document_to_account__mutmut_4': x__document_to_account__mutmut_4, 
    'x__document_to_account__mutmut_5': x__document_to_account__mutmut_5, 
    'x__document_to_account__mutmut_6': x__document_to_account__mutmut_6, 
    'x__document_to_account__mutmut_7': x__document_to_account__mutmut_7, 
    'x__document_to_account__mutmut_8': x__document_to_account__mutmut_8, 
    'x__document_to_account__mutmut_9': x__document_to_account__mutmut_9, 
    'x__document_to_account__mutmut_10': x__document_to_account__mutmut_10, 
    'x__document_to_account__mutmut_11': x__document_to_account__mutmut_11, 
    'x__document_to_account__mutmut_12': x__document_to_account__mutmut_12, 
    'x__document_to_account__mutmut_13': x__document_to_account__mutmut_13, 
    'x__document_to_account__mutmut_14': x__document_to_account__mutmut_14, 
    'x__document_to_account__mutmut_15': x__document_to_account__mutmut_15, 
    'x__document_to_account__mutmut_16': x__document_to_account__mutmut_16, 
    'x__document_to_account__mutmut_17': x__document_to_account__mutmut_17, 
    'x__document_to_account__mutmut_18': x__document_to_account__mutmut_18, 
    'x__document_to_account__mutmut_19': x__document_to_account__mutmut_19, 
    'x__document_to_account__mutmut_20': x__document_to_account__mutmut_20, 
    'x__document_to_account__mutmut_21': x__document_to_account__mutmut_21, 
    'x__document_to_account__mutmut_22': x__document_to_account__mutmut_22, 
    'x__document_to_account__mutmut_23': x__document_to_account__mutmut_23, 
    'x__document_to_account__mutmut_24': x__document_to_account__mutmut_24, 
    'x__document_to_account__mutmut_25': x__document_to_account__mutmut_25, 
    'x__document_to_account__mutmut_26': x__document_to_account__mutmut_26, 
    'x__document_to_account__mutmut_27': x__document_to_account__mutmut_27
}

def _document_to_account(*args, **kwargs):
    result = _mutmut_trampoline(x__document_to_account__mutmut_orig, x__document_to_account__mutmut_mutants, args, kwargs)
    return result 

_document_to_account.__signature__ = _mutmut_signature(x__document_to_account__mutmut_orig)
x__document_to_account__mutmut_orig.__name__ = 'x__document_to_account'


def x__prepare_account_update__mutmut_orig(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_1(data: Dict[str, object]) -> Dict[str, object]:
    update_data = None
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_2(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(None)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_3(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "XXuser_idXX" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_4(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "USER_ID" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_5(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" not in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_6(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = None
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_7(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["XXuser_idXX"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_8(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["USER_ID"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_9(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(None)
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_10(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(None))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_11(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["XXuser_idXX"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_12(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["USER_ID"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_13(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data or update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_14(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "XXbalanceXX" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_15(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "BALANCE" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_16(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" not in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_17(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["XXbalanceXX"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_18(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["BALANCE"] is not None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_19(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is None:
        update_data["balance"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_20(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = None
    return update_data


def x__prepare_account_update__mutmut_21(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["XXbalanceXX"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_22(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["BALANCE"] = Decimal128(str(update_data["balance"]))
    return update_data


def x__prepare_account_update__mutmut_23(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(None)
    return update_data


def x__prepare_account_update__mutmut_24(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(None))
    return update_data


def x__prepare_account_update__mutmut_25(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["XXbalanceXX"]))
    return update_data


def x__prepare_account_update__mutmut_26(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "balance" in update_data and update_data["balance"] is not None:
        update_data["balance"] = Decimal128(str(update_data["BALANCE"]))
    return update_data

x__prepare_account_update__mutmut_mutants : ClassVar[MutantDict] = {
'x__prepare_account_update__mutmut_1': x__prepare_account_update__mutmut_1, 
    'x__prepare_account_update__mutmut_2': x__prepare_account_update__mutmut_2, 
    'x__prepare_account_update__mutmut_3': x__prepare_account_update__mutmut_3, 
    'x__prepare_account_update__mutmut_4': x__prepare_account_update__mutmut_4, 
    'x__prepare_account_update__mutmut_5': x__prepare_account_update__mutmut_5, 
    'x__prepare_account_update__mutmut_6': x__prepare_account_update__mutmut_6, 
    'x__prepare_account_update__mutmut_7': x__prepare_account_update__mutmut_7, 
    'x__prepare_account_update__mutmut_8': x__prepare_account_update__mutmut_8, 
    'x__prepare_account_update__mutmut_9': x__prepare_account_update__mutmut_9, 
    'x__prepare_account_update__mutmut_10': x__prepare_account_update__mutmut_10, 
    'x__prepare_account_update__mutmut_11': x__prepare_account_update__mutmut_11, 
    'x__prepare_account_update__mutmut_12': x__prepare_account_update__mutmut_12, 
    'x__prepare_account_update__mutmut_13': x__prepare_account_update__mutmut_13, 
    'x__prepare_account_update__mutmut_14': x__prepare_account_update__mutmut_14, 
    'x__prepare_account_update__mutmut_15': x__prepare_account_update__mutmut_15, 
    'x__prepare_account_update__mutmut_16': x__prepare_account_update__mutmut_16, 
    'x__prepare_account_update__mutmut_17': x__prepare_account_update__mutmut_17, 
    'x__prepare_account_update__mutmut_18': x__prepare_account_update__mutmut_18, 
    'x__prepare_account_update__mutmut_19': x__prepare_account_update__mutmut_19, 
    'x__prepare_account_update__mutmut_20': x__prepare_account_update__mutmut_20, 
    'x__prepare_account_update__mutmut_21': x__prepare_account_update__mutmut_21, 
    'x__prepare_account_update__mutmut_22': x__prepare_account_update__mutmut_22, 
    'x__prepare_account_update__mutmut_23': x__prepare_account_update__mutmut_23, 
    'x__prepare_account_update__mutmut_24': x__prepare_account_update__mutmut_24, 
    'x__prepare_account_update__mutmut_25': x__prepare_account_update__mutmut_25, 
    'x__prepare_account_update__mutmut_26': x__prepare_account_update__mutmut_26
}

def _prepare_account_update(*args, **kwargs):
    result = _mutmut_trampoline(x__prepare_account_update__mutmut_orig, x__prepare_account_update__mutmut_mutants, args, kwargs)
    return result 

_prepare_account_update.__signature__ = _mutmut_signature(x__prepare_account_update__mutmut_orig)
x__prepare_account_update__mutmut_orig.__name__ = 'x__prepare_account_update'
