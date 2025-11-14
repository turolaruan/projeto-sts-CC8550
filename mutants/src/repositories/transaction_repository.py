"""Transaction repository implementations."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Dict, Iterable, List, Optional

from bson.decimal128 import Decimal128

from src.models.common import ensure_object_id
from src.models.transaction import Transaction
from src.repositories.base import Repository
from src.repositories.mongo_compat import (
    ASCENDING,
    DESCENDING,
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


class TransactionRepository(Repository[Transaction, str]):
    """Mongo-backed repository for transactions."""

    def xǁTransactionRepositoryǁ__init____mutmut_orig(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("transactions")
        self._indexes_ready = False

    def xǁTransactionRepositoryǁ__init____mutmut_1(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = None
        self._indexes_ready = False

    def xǁTransactionRepositoryǁ__init____mutmut_2(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection(None)
        self._indexes_ready = False

    def xǁTransactionRepositoryǁ__init____mutmut_3(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("XXtransactionsXX")
        self._indexes_ready = False

    def xǁTransactionRepositoryǁ__init____mutmut_4(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("TRANSACTIONS")
        self._indexes_ready = False

    def xǁTransactionRepositoryǁ__init____mutmut_5(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("transactions")
        self._indexes_ready = None

    def xǁTransactionRepositoryǁ__init____mutmut_6(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("transactions")
        self._indexes_ready = True
    
    xǁTransactionRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁ__init____mutmut_1': xǁTransactionRepositoryǁ__init____mutmut_1, 
        'xǁTransactionRepositoryǁ__init____mutmut_2': xǁTransactionRepositoryǁ__init____mutmut_2, 
        'xǁTransactionRepositoryǁ__init____mutmut_3': xǁTransactionRepositoryǁ__init____mutmut_3, 
        'xǁTransactionRepositoryǁ__init____mutmut_4': xǁTransactionRepositoryǁ__init____mutmut_4, 
        'xǁTransactionRepositoryǁ__init____mutmut_5': xǁTransactionRepositoryǁ__init____mutmut_5, 
        'xǁTransactionRepositoryǁ__init____mutmut_6': xǁTransactionRepositoryǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁ__init____mutmut_orig)
    xǁTransactionRepositoryǁ__init____mutmut_orig.__name__ = 'xǁTransactionRepositoryǁ__init__'

    async def xǁTransactionRepositoryǁcreate__mutmut_orig(self, entity: Transaction) -> Transaction:
        await self._ensure_indexes()
        await self._collection.insert_one(_transaction_to_document(entity))
        return entity

    async def xǁTransactionRepositoryǁcreate__mutmut_1(self, entity: Transaction) -> Transaction:
        await self._ensure_indexes()
        await self._collection.insert_one(None)
        return entity

    async def xǁTransactionRepositoryǁcreate__mutmut_2(self, entity: Transaction) -> Transaction:
        await self._ensure_indexes()
        await self._collection.insert_one(_transaction_to_document(None))
        return entity
    
    xǁTransactionRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁcreate__mutmut_1': xǁTransactionRepositoryǁcreate__mutmut_1, 
        'xǁTransactionRepositoryǁcreate__mutmut_2': xǁTransactionRepositoryǁcreate__mutmut_2
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁcreate__mutmut_orig)
    xǁTransactionRepositoryǁcreate__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁcreate'

    async def xǁTransactionRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Transaction]:
        document = None
        if not document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_2(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one(None)
        if not document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_3(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"XX_idXX": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_4(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"_ID": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_5(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"_id": ensure_object_id(None)})
        if not document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_6(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if document:
            return None
        return _document_to_transaction(document)

    async def xǁTransactionRepositoryǁget__mutmut_7(self, entity_id: str) -> Optional[Transaction]:
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_transaction(None)
    
    xǁTransactionRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁget__mutmut_1': xǁTransactionRepositoryǁget__mutmut_1, 
        'xǁTransactionRepositoryǁget__mutmut_2': xǁTransactionRepositoryǁget__mutmut_2, 
        'xǁTransactionRepositoryǁget__mutmut_3': xǁTransactionRepositoryǁget__mutmut_3, 
        'xǁTransactionRepositoryǁget__mutmut_4': xǁTransactionRepositoryǁget__mutmut_4, 
        'xǁTransactionRepositoryǁget__mutmut_5': xǁTransactionRepositoryǁget__mutmut_5, 
        'xǁTransactionRepositoryǁget__mutmut_6': xǁTransactionRepositoryǁget__mutmut_6, 
        'xǁTransactionRepositoryǁget__mutmut_7': xǁTransactionRepositoryǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁget__mutmut_orig)
    xǁTransactionRepositoryǁget__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁget'

    async def xǁTransactionRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = None

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = None
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get(None)
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = None

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["XXuser_idXX"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["USER_ID"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(None)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = None
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get(None)
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("XXaccount_idXX")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("ACCOUNT_ID")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = None

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["XXaccount_idXX"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["ACCOUNT_ID"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(None)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = None
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get(None)
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("XXcategory_idXX")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("CATEGORY_ID")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = None

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["XXcategory_idXX"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["CATEGORY_ID"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(None)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = None
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get(None)
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("XXtransaction_typeXX")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("TRANSACTION_TYPE")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = None

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["XXtransaction_typeXX"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["TRANSACTION_TYPE"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = None
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get(None)
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("XXtransfer_account_idXX")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("TRANSFER_ACCOUNT_ID")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_37(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = None

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_38(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["XXtransfer_account_idXX"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_39(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["TRANSFER_ACCOUNT_ID"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_40(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(None)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_41(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = None
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_42(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = None
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_43(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get(None)
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_44(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("XXdate_fromXX")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_45(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("DATE_FROM")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_46(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = None
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_47(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["XX$gteXX"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_48(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$GTE"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_49(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = None
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_50(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get(None)
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_51(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("XXdate_toXX")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_52(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("DATE_TO")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_53(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = None
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_54(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["XX$lteXX"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_55(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$LTE"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_56(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = None

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_57(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["XXoccurred_atXX"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_58(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["OCCURRED_AT"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_59(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = None
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_60(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort(None, DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_61(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", None)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_62(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort(DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_63(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", )
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_64(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(None).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_65(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.rfind(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_66(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("XXoccurred_atXX", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_67(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("OCCURRED_AT", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_68(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = None
        async for document in cursor:
            results.append(_document_to_transaction(document))
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_69(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(None)
        return results

    async def xǁTransactionRepositoryǁlist__mutmut_70(self, **filters: object) -> Iterable[Transaction]:
        await self._ensure_indexes()
        query: Dict[str, object] = {}

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            query["user_id"] = ensure_object_id(user_id)

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            query["account_id"] = ensure_object_id(account_id)

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            query["category_id"] = ensure_object_id(category_id)

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            query["transaction_type"] = transaction_type

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            query["transfer_account_id"] = ensure_object_id(transfer_account_id)

        date_filters: Dict[str, object] = {}
        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            date_filters["$gte"] = date_from
        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            date_filters["$lte"] = date_to
        if date_filters:
            query["occurred_at"] = date_filters

        cursor = self._collection.find(query).sort("occurred_at", DESCENDING)
        results: List[Transaction] = []
        async for document in cursor:
            results.append(_document_to_transaction(None))
        return results
    
    xǁTransactionRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁlist__mutmut_1': xǁTransactionRepositoryǁlist__mutmut_1, 
        'xǁTransactionRepositoryǁlist__mutmut_2': xǁTransactionRepositoryǁlist__mutmut_2, 
        'xǁTransactionRepositoryǁlist__mutmut_3': xǁTransactionRepositoryǁlist__mutmut_3, 
        'xǁTransactionRepositoryǁlist__mutmut_4': xǁTransactionRepositoryǁlist__mutmut_4, 
        'xǁTransactionRepositoryǁlist__mutmut_5': xǁTransactionRepositoryǁlist__mutmut_5, 
        'xǁTransactionRepositoryǁlist__mutmut_6': xǁTransactionRepositoryǁlist__mutmut_6, 
        'xǁTransactionRepositoryǁlist__mutmut_7': xǁTransactionRepositoryǁlist__mutmut_7, 
        'xǁTransactionRepositoryǁlist__mutmut_8': xǁTransactionRepositoryǁlist__mutmut_8, 
        'xǁTransactionRepositoryǁlist__mutmut_9': xǁTransactionRepositoryǁlist__mutmut_9, 
        'xǁTransactionRepositoryǁlist__mutmut_10': xǁTransactionRepositoryǁlist__mutmut_10, 
        'xǁTransactionRepositoryǁlist__mutmut_11': xǁTransactionRepositoryǁlist__mutmut_11, 
        'xǁTransactionRepositoryǁlist__mutmut_12': xǁTransactionRepositoryǁlist__mutmut_12, 
        'xǁTransactionRepositoryǁlist__mutmut_13': xǁTransactionRepositoryǁlist__mutmut_13, 
        'xǁTransactionRepositoryǁlist__mutmut_14': xǁTransactionRepositoryǁlist__mutmut_14, 
        'xǁTransactionRepositoryǁlist__mutmut_15': xǁTransactionRepositoryǁlist__mutmut_15, 
        'xǁTransactionRepositoryǁlist__mutmut_16': xǁTransactionRepositoryǁlist__mutmut_16, 
        'xǁTransactionRepositoryǁlist__mutmut_17': xǁTransactionRepositoryǁlist__mutmut_17, 
        'xǁTransactionRepositoryǁlist__mutmut_18': xǁTransactionRepositoryǁlist__mutmut_18, 
        'xǁTransactionRepositoryǁlist__mutmut_19': xǁTransactionRepositoryǁlist__mutmut_19, 
        'xǁTransactionRepositoryǁlist__mutmut_20': xǁTransactionRepositoryǁlist__mutmut_20, 
        'xǁTransactionRepositoryǁlist__mutmut_21': xǁTransactionRepositoryǁlist__mutmut_21, 
        'xǁTransactionRepositoryǁlist__mutmut_22': xǁTransactionRepositoryǁlist__mutmut_22, 
        'xǁTransactionRepositoryǁlist__mutmut_23': xǁTransactionRepositoryǁlist__mutmut_23, 
        'xǁTransactionRepositoryǁlist__mutmut_24': xǁTransactionRepositoryǁlist__mutmut_24, 
        'xǁTransactionRepositoryǁlist__mutmut_25': xǁTransactionRepositoryǁlist__mutmut_25, 
        'xǁTransactionRepositoryǁlist__mutmut_26': xǁTransactionRepositoryǁlist__mutmut_26, 
        'xǁTransactionRepositoryǁlist__mutmut_27': xǁTransactionRepositoryǁlist__mutmut_27, 
        'xǁTransactionRepositoryǁlist__mutmut_28': xǁTransactionRepositoryǁlist__mutmut_28, 
        'xǁTransactionRepositoryǁlist__mutmut_29': xǁTransactionRepositoryǁlist__mutmut_29, 
        'xǁTransactionRepositoryǁlist__mutmut_30': xǁTransactionRepositoryǁlist__mutmut_30, 
        'xǁTransactionRepositoryǁlist__mutmut_31': xǁTransactionRepositoryǁlist__mutmut_31, 
        'xǁTransactionRepositoryǁlist__mutmut_32': xǁTransactionRepositoryǁlist__mutmut_32, 
        'xǁTransactionRepositoryǁlist__mutmut_33': xǁTransactionRepositoryǁlist__mutmut_33, 
        'xǁTransactionRepositoryǁlist__mutmut_34': xǁTransactionRepositoryǁlist__mutmut_34, 
        'xǁTransactionRepositoryǁlist__mutmut_35': xǁTransactionRepositoryǁlist__mutmut_35, 
        'xǁTransactionRepositoryǁlist__mutmut_36': xǁTransactionRepositoryǁlist__mutmut_36, 
        'xǁTransactionRepositoryǁlist__mutmut_37': xǁTransactionRepositoryǁlist__mutmut_37, 
        'xǁTransactionRepositoryǁlist__mutmut_38': xǁTransactionRepositoryǁlist__mutmut_38, 
        'xǁTransactionRepositoryǁlist__mutmut_39': xǁTransactionRepositoryǁlist__mutmut_39, 
        'xǁTransactionRepositoryǁlist__mutmut_40': xǁTransactionRepositoryǁlist__mutmut_40, 
        'xǁTransactionRepositoryǁlist__mutmut_41': xǁTransactionRepositoryǁlist__mutmut_41, 
        'xǁTransactionRepositoryǁlist__mutmut_42': xǁTransactionRepositoryǁlist__mutmut_42, 
        'xǁTransactionRepositoryǁlist__mutmut_43': xǁTransactionRepositoryǁlist__mutmut_43, 
        'xǁTransactionRepositoryǁlist__mutmut_44': xǁTransactionRepositoryǁlist__mutmut_44, 
        'xǁTransactionRepositoryǁlist__mutmut_45': xǁTransactionRepositoryǁlist__mutmut_45, 
        'xǁTransactionRepositoryǁlist__mutmut_46': xǁTransactionRepositoryǁlist__mutmut_46, 
        'xǁTransactionRepositoryǁlist__mutmut_47': xǁTransactionRepositoryǁlist__mutmut_47, 
        'xǁTransactionRepositoryǁlist__mutmut_48': xǁTransactionRepositoryǁlist__mutmut_48, 
        'xǁTransactionRepositoryǁlist__mutmut_49': xǁTransactionRepositoryǁlist__mutmut_49, 
        'xǁTransactionRepositoryǁlist__mutmut_50': xǁTransactionRepositoryǁlist__mutmut_50, 
        'xǁTransactionRepositoryǁlist__mutmut_51': xǁTransactionRepositoryǁlist__mutmut_51, 
        'xǁTransactionRepositoryǁlist__mutmut_52': xǁTransactionRepositoryǁlist__mutmut_52, 
        'xǁTransactionRepositoryǁlist__mutmut_53': xǁTransactionRepositoryǁlist__mutmut_53, 
        'xǁTransactionRepositoryǁlist__mutmut_54': xǁTransactionRepositoryǁlist__mutmut_54, 
        'xǁTransactionRepositoryǁlist__mutmut_55': xǁTransactionRepositoryǁlist__mutmut_55, 
        'xǁTransactionRepositoryǁlist__mutmut_56': xǁTransactionRepositoryǁlist__mutmut_56, 
        'xǁTransactionRepositoryǁlist__mutmut_57': xǁTransactionRepositoryǁlist__mutmut_57, 
        'xǁTransactionRepositoryǁlist__mutmut_58': xǁTransactionRepositoryǁlist__mutmut_58, 
        'xǁTransactionRepositoryǁlist__mutmut_59': xǁTransactionRepositoryǁlist__mutmut_59, 
        'xǁTransactionRepositoryǁlist__mutmut_60': xǁTransactionRepositoryǁlist__mutmut_60, 
        'xǁTransactionRepositoryǁlist__mutmut_61': xǁTransactionRepositoryǁlist__mutmut_61, 
        'xǁTransactionRepositoryǁlist__mutmut_62': xǁTransactionRepositoryǁlist__mutmut_62, 
        'xǁTransactionRepositoryǁlist__mutmut_63': xǁTransactionRepositoryǁlist__mutmut_63, 
        'xǁTransactionRepositoryǁlist__mutmut_64': xǁTransactionRepositoryǁlist__mutmut_64, 
        'xǁTransactionRepositoryǁlist__mutmut_65': xǁTransactionRepositoryǁlist__mutmut_65, 
        'xǁTransactionRepositoryǁlist__mutmut_66': xǁTransactionRepositoryǁlist__mutmut_66, 
        'xǁTransactionRepositoryǁlist__mutmut_67': xǁTransactionRepositoryǁlist__mutmut_67, 
        'xǁTransactionRepositoryǁlist__mutmut_68': xǁTransactionRepositoryǁlist__mutmut_68, 
        'xǁTransactionRepositoryǁlist__mutmut_69': xǁTransactionRepositoryǁlist__mutmut_69, 
        'xǁTransactionRepositoryǁlist__mutmut_70': xǁTransactionRepositoryǁlist__mutmut_70
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁlist__mutmut_orig)
    xǁTransactionRepositoryǁlist__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁlist'

    async def xǁTransactionRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(None)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
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
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(None)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = None
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            None,
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            None,
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_8(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=None,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_9(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_10(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_11(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_12(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"XX_idXX": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_13(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_ID": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_14(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(None)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_15(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"XX$setXX": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_16(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$SET": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_17(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return None
        return _document_to_transaction(result)

    async def xǁTransactionRepositoryǁupdate__mutmut_18(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        if not data:
            return await self.get(entity_id)

        update_payload = _prepare_transaction_update(data)
        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": update_payload},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_transaction(None)
    
    xǁTransactionRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁupdate__mutmut_1': xǁTransactionRepositoryǁupdate__mutmut_1, 
        'xǁTransactionRepositoryǁupdate__mutmut_2': xǁTransactionRepositoryǁupdate__mutmut_2, 
        'xǁTransactionRepositoryǁupdate__mutmut_3': xǁTransactionRepositoryǁupdate__mutmut_3, 
        'xǁTransactionRepositoryǁupdate__mutmut_4': xǁTransactionRepositoryǁupdate__mutmut_4, 
        'xǁTransactionRepositoryǁupdate__mutmut_5': xǁTransactionRepositoryǁupdate__mutmut_5, 
        'xǁTransactionRepositoryǁupdate__mutmut_6': xǁTransactionRepositoryǁupdate__mutmut_6, 
        'xǁTransactionRepositoryǁupdate__mutmut_7': xǁTransactionRepositoryǁupdate__mutmut_7, 
        'xǁTransactionRepositoryǁupdate__mutmut_8': xǁTransactionRepositoryǁupdate__mutmut_8, 
        'xǁTransactionRepositoryǁupdate__mutmut_9': xǁTransactionRepositoryǁupdate__mutmut_9, 
        'xǁTransactionRepositoryǁupdate__mutmut_10': xǁTransactionRepositoryǁupdate__mutmut_10, 
        'xǁTransactionRepositoryǁupdate__mutmut_11': xǁTransactionRepositoryǁupdate__mutmut_11, 
        'xǁTransactionRepositoryǁupdate__mutmut_12': xǁTransactionRepositoryǁupdate__mutmut_12, 
        'xǁTransactionRepositoryǁupdate__mutmut_13': xǁTransactionRepositoryǁupdate__mutmut_13, 
        'xǁTransactionRepositoryǁupdate__mutmut_14': xǁTransactionRepositoryǁupdate__mutmut_14, 
        'xǁTransactionRepositoryǁupdate__mutmut_15': xǁTransactionRepositoryǁupdate__mutmut_15, 
        'xǁTransactionRepositoryǁupdate__mutmut_16': xǁTransactionRepositoryǁupdate__mutmut_16, 
        'xǁTransactionRepositoryǁupdate__mutmut_17': xǁTransactionRepositoryǁupdate__mutmut_17, 
        'xǁTransactionRepositoryǁupdate__mutmut_18': xǁTransactionRepositoryǁupdate__mutmut_18
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁupdate__mutmut_orig)
    xǁTransactionRepositoryǁupdate__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁupdate'

    async def xǁTransactionRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁTransactionRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        outcome = None
        return outcome.deleted_count > 0

    async def xǁTransactionRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one(None)
        return outcome.deleted_count > 0

    async def xǁTransactionRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"XX_idXX": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁTransactionRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_ID": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁTransactionRepositoryǁdelete__mutmut_5(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(None)})
        return outcome.deleted_count > 0

    async def xǁTransactionRepositoryǁdelete__mutmut_6(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count >= 0

    async def xǁTransactionRepositoryǁdelete__mutmut_7(self, entity_id: str) -> bool:
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 1
    
    xǁTransactionRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁdelete__mutmut_1': xǁTransactionRepositoryǁdelete__mutmut_1, 
        'xǁTransactionRepositoryǁdelete__mutmut_2': xǁTransactionRepositoryǁdelete__mutmut_2, 
        'xǁTransactionRepositoryǁdelete__mutmut_3': xǁTransactionRepositoryǁdelete__mutmut_3, 
        'xǁTransactionRepositoryǁdelete__mutmut_4': xǁTransactionRepositoryǁdelete__mutmut_4, 
        'xǁTransactionRepositoryǁdelete__mutmut_5': xǁTransactionRepositoryǁdelete__mutmut_5, 
        'xǁTransactionRepositoryǁdelete__mutmut_6': xǁTransactionRepositoryǁdelete__mutmut_6, 
        'xǁTransactionRepositoryǁdelete__mutmut_7': xǁTransactionRepositoryǁdelete__mutmut_7
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁdelete__mutmut_orig)
    xǁTransactionRepositoryǁdelete__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁdelete'

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_orig(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_1(self, account_id: str) -> bool:
        query = None
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_2(self, account_id: str) -> bool:
        query = {"XXaccount_idXX": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_3(self, account_id: str) -> bool:
        query = {"ACCOUNT_ID": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_4(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(None)}
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_5(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(None, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_6(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=None) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_7(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_8(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, ) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_9(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=2) > 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_10(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=1) >= 0

    async def xǁTransactionRepositoryǁexists_for_account__mutmut_11(self, account_id: str) -> bool:
        query = {"account_id": ensure_object_id(account_id)}
        return await self._collection.count_documents(query, limit=1) > 1
    
    xǁTransactionRepositoryǁexists_for_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁexists_for_account__mutmut_1': xǁTransactionRepositoryǁexists_for_account__mutmut_1, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_2': xǁTransactionRepositoryǁexists_for_account__mutmut_2, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_3': xǁTransactionRepositoryǁexists_for_account__mutmut_3, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_4': xǁTransactionRepositoryǁexists_for_account__mutmut_4, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_5': xǁTransactionRepositoryǁexists_for_account__mutmut_5, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_6': xǁTransactionRepositoryǁexists_for_account__mutmut_6, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_7': xǁTransactionRepositoryǁexists_for_account__mutmut_7, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_8': xǁTransactionRepositoryǁexists_for_account__mutmut_8, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_9': xǁTransactionRepositoryǁexists_for_account__mutmut_9, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_10': xǁTransactionRepositoryǁexists_for_account__mutmut_10, 
        'xǁTransactionRepositoryǁexists_for_account__mutmut_11': xǁTransactionRepositoryǁexists_for_account__mutmut_11
    }
    
    def exists_for_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁexists_for_account__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁexists_for_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    exists_for_account.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁexists_for_account__mutmut_orig)
    xǁTransactionRepositoryǁexists_for_account__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁexists_for_account'

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_orig(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_1(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = None
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_2(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"XXcategory_idXX": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_3(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"CATEGORY_ID": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_4(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(None)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_5(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = None
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_6(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["XXuser_idXX"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_7(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["USER_ID"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_8(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(None)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_9(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None and month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_10(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_11(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_12(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = None
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_13(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_14(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = None
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_15(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(None, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_16(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, None, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_17(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, None)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_18(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_19(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_20(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, )
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_21(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 2, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_22(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 2)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_23(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = None
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_24(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["XX$gteXX"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_25(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$GTE"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_26(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_27(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month != 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_28(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 13:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_29(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = None
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_30(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(None, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_31(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, None, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_32(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, None)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_33(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_34(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_35(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, )
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_36(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year - 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_37(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 2, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_38(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 2, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_39(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 2)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_40(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = None
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_41(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(None, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_42(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, None, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_43(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, None)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_44(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_45(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_46(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, )
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_47(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month - 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_48(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 2, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_49(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 2)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_50(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = None
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_51(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["XX$ltXX"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_52(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$LT"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_53(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = None
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_54(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["XXoccurred_atXX"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_55(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["OCCURRED_AT"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_56(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(None, limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_57(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=None) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_58(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(limit=1) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_59(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, ) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_60(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=2) > 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_61(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) >= 0

    async def xǁTransactionRepositoryǁexists_for_category__mutmut_62(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        query: Dict[str, object] = {"category_id": ensure_object_id(category_id)}
        if user_id:
            query["user_id"] = ensure_object_id(user_id)
        if year is not None or month is not None:
            date_filter: Dict[str, object] = {}
            if year is not None:
                from datetime import datetime

                start = datetime(year, month if month else 1, 1)
                date_filter["$gte"] = start
                if month is not None:
                    if month == 12:
                        end = datetime(year + 1, 1, 1)
                    else:
                        end = datetime(year, month + 1, 1)
                    date_filter["$lt"] = end
            if date_filter:
                query["occurred_at"] = date_filter
        return await self._collection.count_documents(query, limit=1) > 1
    
    xǁTransactionRepositoryǁexists_for_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁexists_for_category__mutmut_1': xǁTransactionRepositoryǁexists_for_category__mutmut_1, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_2': xǁTransactionRepositoryǁexists_for_category__mutmut_2, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_3': xǁTransactionRepositoryǁexists_for_category__mutmut_3, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_4': xǁTransactionRepositoryǁexists_for_category__mutmut_4, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_5': xǁTransactionRepositoryǁexists_for_category__mutmut_5, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_6': xǁTransactionRepositoryǁexists_for_category__mutmut_6, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_7': xǁTransactionRepositoryǁexists_for_category__mutmut_7, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_8': xǁTransactionRepositoryǁexists_for_category__mutmut_8, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_9': xǁTransactionRepositoryǁexists_for_category__mutmut_9, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_10': xǁTransactionRepositoryǁexists_for_category__mutmut_10, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_11': xǁTransactionRepositoryǁexists_for_category__mutmut_11, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_12': xǁTransactionRepositoryǁexists_for_category__mutmut_12, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_13': xǁTransactionRepositoryǁexists_for_category__mutmut_13, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_14': xǁTransactionRepositoryǁexists_for_category__mutmut_14, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_15': xǁTransactionRepositoryǁexists_for_category__mutmut_15, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_16': xǁTransactionRepositoryǁexists_for_category__mutmut_16, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_17': xǁTransactionRepositoryǁexists_for_category__mutmut_17, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_18': xǁTransactionRepositoryǁexists_for_category__mutmut_18, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_19': xǁTransactionRepositoryǁexists_for_category__mutmut_19, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_20': xǁTransactionRepositoryǁexists_for_category__mutmut_20, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_21': xǁTransactionRepositoryǁexists_for_category__mutmut_21, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_22': xǁTransactionRepositoryǁexists_for_category__mutmut_22, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_23': xǁTransactionRepositoryǁexists_for_category__mutmut_23, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_24': xǁTransactionRepositoryǁexists_for_category__mutmut_24, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_25': xǁTransactionRepositoryǁexists_for_category__mutmut_25, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_26': xǁTransactionRepositoryǁexists_for_category__mutmut_26, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_27': xǁTransactionRepositoryǁexists_for_category__mutmut_27, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_28': xǁTransactionRepositoryǁexists_for_category__mutmut_28, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_29': xǁTransactionRepositoryǁexists_for_category__mutmut_29, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_30': xǁTransactionRepositoryǁexists_for_category__mutmut_30, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_31': xǁTransactionRepositoryǁexists_for_category__mutmut_31, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_32': xǁTransactionRepositoryǁexists_for_category__mutmut_32, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_33': xǁTransactionRepositoryǁexists_for_category__mutmut_33, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_34': xǁTransactionRepositoryǁexists_for_category__mutmut_34, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_35': xǁTransactionRepositoryǁexists_for_category__mutmut_35, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_36': xǁTransactionRepositoryǁexists_for_category__mutmut_36, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_37': xǁTransactionRepositoryǁexists_for_category__mutmut_37, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_38': xǁTransactionRepositoryǁexists_for_category__mutmut_38, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_39': xǁTransactionRepositoryǁexists_for_category__mutmut_39, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_40': xǁTransactionRepositoryǁexists_for_category__mutmut_40, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_41': xǁTransactionRepositoryǁexists_for_category__mutmut_41, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_42': xǁTransactionRepositoryǁexists_for_category__mutmut_42, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_43': xǁTransactionRepositoryǁexists_for_category__mutmut_43, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_44': xǁTransactionRepositoryǁexists_for_category__mutmut_44, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_45': xǁTransactionRepositoryǁexists_for_category__mutmut_45, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_46': xǁTransactionRepositoryǁexists_for_category__mutmut_46, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_47': xǁTransactionRepositoryǁexists_for_category__mutmut_47, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_48': xǁTransactionRepositoryǁexists_for_category__mutmut_48, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_49': xǁTransactionRepositoryǁexists_for_category__mutmut_49, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_50': xǁTransactionRepositoryǁexists_for_category__mutmut_50, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_51': xǁTransactionRepositoryǁexists_for_category__mutmut_51, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_52': xǁTransactionRepositoryǁexists_for_category__mutmut_52, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_53': xǁTransactionRepositoryǁexists_for_category__mutmut_53, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_54': xǁTransactionRepositoryǁexists_for_category__mutmut_54, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_55': xǁTransactionRepositoryǁexists_for_category__mutmut_55, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_56': xǁTransactionRepositoryǁexists_for_category__mutmut_56, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_57': xǁTransactionRepositoryǁexists_for_category__mutmut_57, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_58': xǁTransactionRepositoryǁexists_for_category__mutmut_58, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_59': xǁTransactionRepositoryǁexists_for_category__mutmut_59, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_60': xǁTransactionRepositoryǁexists_for_category__mutmut_60, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_61': xǁTransactionRepositoryǁexists_for_category__mutmut_61, 
        'xǁTransactionRepositoryǁexists_for_category__mutmut_62': xǁTransactionRepositoryǁexists_for_category__mutmut_62
    }
    
    def exists_for_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁexists_for_category__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁexists_for_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    exists_for_category.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁexists_for_category__mutmut_orig)
    xǁTransactionRepositoryǁexists_for_category__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁexists_for_category'

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_1(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = None
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_2(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "XX$matchXX": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_3(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$MATCH": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_4(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "XXuser_idXX": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_5(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "USER_ID": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_6(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(None),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_7(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "XX$exprXX": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_8(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$EXPR": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_9(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "XX$andXX": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_10(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$AND": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_11(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"XX$eqXX": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_12(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$EQ": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_13(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"XX$yearXX": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_14(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$YEAR": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_15(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "XX$occurred_atXX"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_16(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$OCCURRED_AT"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_17(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"XX$eqXX": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_18(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$EQ": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_19(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"XX$monthXX": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_20(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$MONTH": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_21(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "XX$occurred_atXX"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_22(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$OCCURRED_AT"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_23(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "XX$groupXX": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_24(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$GROUP": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_25(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "XX_idXX": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_26(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_ID": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_27(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "XXcategory_idXX": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_28(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "CATEGORY_ID": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_29(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "XX$category_idXX",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_30(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$CATEGORY_ID",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_31(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "XXtransaction_typeXX": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_32(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "TRANSACTION_TYPE": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_33(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "XX$transaction_typeXX",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_34(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$TRANSACTION_TYPE",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_35(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "XXtotalXX": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_36(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "TOTAL": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_37(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"XX$sumXX": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_38(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$SUM": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_39(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "XX$amountXX"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_40(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$AMOUNT"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_41(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "XXcountXX": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_42(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "COUNT": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_43(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"XX$sumXX": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_44(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$SUM": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_45(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 2},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_46(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "XX$projectXX": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_47(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$PROJECT": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_48(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "XXcategory_idXX": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_49(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "CATEGORY_ID": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_50(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "XX$_id.category_idXX",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_51(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_ID.CATEGORY_ID",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_52(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "XXtransaction_typeXX": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_53(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "TRANSACTION_TYPE": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_54(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "XX$_id.transaction_typeXX",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_55(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_ID.TRANSACTION_TYPE",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_56(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "XXtotalXX": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_57(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "TOTAL": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_58(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 2,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_59(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "XXcountXX": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_60(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "COUNT": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_61(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 2,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_62(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "XX_idXX": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_63(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_ID": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_64(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 1,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_65(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = None
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_66(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(None)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_67(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = None
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_68(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = None
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_69(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get(None)
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_70(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("XXtotalXX")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_71(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("TOTAL")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_72(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = None
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_73(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["XXtotalXX"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_74(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["TOTAL"] = total.to_decimal()
            results.append(item)
        return results

    async def xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_75(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "category_id": "$category_id",
                        "transaction_type": "$transaction_type",
                    },
                    "total": {"$sum": "$amount"},
                    "count": {"$sum": 1},
                }
            },
            {
                "$project": {
                    "category_id": "$_id.category_id",
                    "transaction_type": "$_id.transaction_type",
                    "total": 1,
                    "count": 1,
                    "_id": 0,
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        results: list[dict[str, object]] = []
        async for item in cursor:
            total = item.get("total")
            if isinstance(total, Decimal128):
                item["total"] = total.to_decimal()
            results.append(None)
        return results
    
    xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_1': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_1, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_2': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_2, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_3': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_3, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_4': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_4, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_5': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_5, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_6': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_6, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_7': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_7, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_8': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_8, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_9': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_9, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_10': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_10, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_11': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_11, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_12': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_12, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_13': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_13, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_14': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_14, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_15': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_15, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_16': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_16, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_17': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_17, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_18': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_18, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_19': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_19, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_20': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_20, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_21': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_21, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_22': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_22, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_23': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_23, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_24': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_24, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_25': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_25, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_26': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_26, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_27': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_27, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_28': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_28, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_29': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_29, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_30': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_30, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_31': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_31, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_32': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_32, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_33': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_33, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_34': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_34, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_35': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_35, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_36': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_36, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_37': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_37, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_38': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_38, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_39': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_39, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_40': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_40, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_41': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_41, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_42': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_42, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_43': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_43, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_44': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_44, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_45': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_45, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_46': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_46, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_47': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_47, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_48': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_48, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_49': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_49, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_50': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_50, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_51': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_51, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_52': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_52, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_53': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_53, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_54': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_54, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_55': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_55, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_56': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_56, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_57': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_57, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_58': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_58, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_59': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_59, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_60': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_60, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_61': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_61, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_62': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_62, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_63': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_63, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_64': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_64, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_65': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_65, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_66': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_66, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_67': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_67, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_68': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_68, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_69': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_69, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_70': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_70, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_71': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_71, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_72': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_72, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_73': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_73, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_74': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_74, 
        'xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_75': xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_75
    }
    
    def aggregate_monthly_summary(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_mutants"), args, kwargs, self)
        return result 
    
    aggregate_monthly_summary.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig)
    xǁTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁaggregate_monthly_summary'

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_orig(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_1(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = None
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_2(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "XX$matchXX": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_3(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$MATCH": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_4(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "XXuser_idXX": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_5(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "USER_ID": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_6(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(None),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_7(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "XXcategory_idXX": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_8(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "CATEGORY_ID": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_9(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(None),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_10(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "XX$exprXX": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_11(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$EXPR": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_12(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "XX$andXX": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_13(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$AND": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_14(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"XX$eqXX": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_15(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$EQ": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_16(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"XX$yearXX": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_17(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$YEAR": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_18(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "XX$occurred_atXX"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_19(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$OCCURRED_AT"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_20(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"XX$eqXX": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_21(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$EQ": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_22(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"XX$monthXX": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_23(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$MONTH": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_24(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "XX$occurred_atXX"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_25(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$OCCURRED_AT"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_26(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "XX$groupXX": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_27(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$GROUP": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_28(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "XX_idXX": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_29(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_ID": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_30(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "XXtotalXX": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_31(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "TOTAL": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_32(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"XX$sumXX": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_33(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$SUM": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_34(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "XX$amountXX"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_35(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$AMOUNT"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_36(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = None
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_37(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(None)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_38(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = None
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_39(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=None)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_40(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=2)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_41(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_42(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal(None)
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_43(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("XX0XX")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_44(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = None
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_45(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get(None, Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_46(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", None)
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_47(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get(Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_48(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", )
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_49(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[1].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_50(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("XXtotalXX", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_51(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("TOTAL", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_52(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal(None))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_53(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("XX0XX"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(total))

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_54(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(None)

    async def xǁTransactionRepositoryǁsum_for_category_period__mutmut_55(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        pipeline = [
            {
                "$match": {
                    "user_id": ensure_object_id(user_id),
                    "category_id": ensure_object_id(category_id),
                    "$expr": {
                        "$and": [
                            {"$eq": [{"$year": "$occurred_at"}, year]},
                            {"$eq": [{"$month": "$occurred_at"}, month]},
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"},
                }
            },
        ]
        cursor = self._collection.aggregate(pipeline)
        result = await cursor.to_list(length=1)
        if not result:
            return Decimal("0")
        total = result[0].get("total", Decimal("0"))
        if isinstance(total, Decimal128):
            return total.to_decimal()
        return Decimal(str(None))
    
    xǁTransactionRepositoryǁsum_for_category_period__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁsum_for_category_period__mutmut_1': xǁTransactionRepositoryǁsum_for_category_period__mutmut_1, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_2': xǁTransactionRepositoryǁsum_for_category_period__mutmut_2, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_3': xǁTransactionRepositoryǁsum_for_category_period__mutmut_3, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_4': xǁTransactionRepositoryǁsum_for_category_period__mutmut_4, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_5': xǁTransactionRepositoryǁsum_for_category_period__mutmut_5, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_6': xǁTransactionRepositoryǁsum_for_category_period__mutmut_6, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_7': xǁTransactionRepositoryǁsum_for_category_period__mutmut_7, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_8': xǁTransactionRepositoryǁsum_for_category_period__mutmut_8, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_9': xǁTransactionRepositoryǁsum_for_category_period__mutmut_9, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_10': xǁTransactionRepositoryǁsum_for_category_period__mutmut_10, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_11': xǁTransactionRepositoryǁsum_for_category_period__mutmut_11, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_12': xǁTransactionRepositoryǁsum_for_category_period__mutmut_12, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_13': xǁTransactionRepositoryǁsum_for_category_period__mutmut_13, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_14': xǁTransactionRepositoryǁsum_for_category_period__mutmut_14, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_15': xǁTransactionRepositoryǁsum_for_category_period__mutmut_15, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_16': xǁTransactionRepositoryǁsum_for_category_period__mutmut_16, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_17': xǁTransactionRepositoryǁsum_for_category_period__mutmut_17, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_18': xǁTransactionRepositoryǁsum_for_category_period__mutmut_18, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_19': xǁTransactionRepositoryǁsum_for_category_period__mutmut_19, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_20': xǁTransactionRepositoryǁsum_for_category_period__mutmut_20, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_21': xǁTransactionRepositoryǁsum_for_category_period__mutmut_21, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_22': xǁTransactionRepositoryǁsum_for_category_period__mutmut_22, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_23': xǁTransactionRepositoryǁsum_for_category_period__mutmut_23, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_24': xǁTransactionRepositoryǁsum_for_category_period__mutmut_24, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_25': xǁTransactionRepositoryǁsum_for_category_period__mutmut_25, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_26': xǁTransactionRepositoryǁsum_for_category_period__mutmut_26, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_27': xǁTransactionRepositoryǁsum_for_category_period__mutmut_27, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_28': xǁTransactionRepositoryǁsum_for_category_period__mutmut_28, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_29': xǁTransactionRepositoryǁsum_for_category_period__mutmut_29, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_30': xǁTransactionRepositoryǁsum_for_category_period__mutmut_30, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_31': xǁTransactionRepositoryǁsum_for_category_period__mutmut_31, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_32': xǁTransactionRepositoryǁsum_for_category_period__mutmut_32, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_33': xǁTransactionRepositoryǁsum_for_category_period__mutmut_33, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_34': xǁTransactionRepositoryǁsum_for_category_period__mutmut_34, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_35': xǁTransactionRepositoryǁsum_for_category_period__mutmut_35, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_36': xǁTransactionRepositoryǁsum_for_category_period__mutmut_36, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_37': xǁTransactionRepositoryǁsum_for_category_period__mutmut_37, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_38': xǁTransactionRepositoryǁsum_for_category_period__mutmut_38, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_39': xǁTransactionRepositoryǁsum_for_category_period__mutmut_39, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_40': xǁTransactionRepositoryǁsum_for_category_period__mutmut_40, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_41': xǁTransactionRepositoryǁsum_for_category_period__mutmut_41, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_42': xǁTransactionRepositoryǁsum_for_category_period__mutmut_42, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_43': xǁTransactionRepositoryǁsum_for_category_period__mutmut_43, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_44': xǁTransactionRepositoryǁsum_for_category_period__mutmut_44, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_45': xǁTransactionRepositoryǁsum_for_category_period__mutmut_45, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_46': xǁTransactionRepositoryǁsum_for_category_period__mutmut_46, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_47': xǁTransactionRepositoryǁsum_for_category_period__mutmut_47, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_48': xǁTransactionRepositoryǁsum_for_category_period__mutmut_48, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_49': xǁTransactionRepositoryǁsum_for_category_period__mutmut_49, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_50': xǁTransactionRepositoryǁsum_for_category_period__mutmut_50, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_51': xǁTransactionRepositoryǁsum_for_category_period__mutmut_51, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_52': xǁTransactionRepositoryǁsum_for_category_period__mutmut_52, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_53': xǁTransactionRepositoryǁsum_for_category_period__mutmut_53, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_54': xǁTransactionRepositoryǁsum_for_category_period__mutmut_54, 
        'xǁTransactionRepositoryǁsum_for_category_period__mutmut_55': xǁTransactionRepositoryǁsum_for_category_period__mutmut_55
    }
    
    def sum_for_category_period(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁsum_for_category_period__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁsum_for_category_period__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sum_for_category_period.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁsum_for_category_period__mutmut_orig)
    xǁTransactionRepositoryǁsum_for_category_period__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁsum_for_category_period'

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_orig(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_1(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index(None)
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_2(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("XXuser_idXX", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_3(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("USER_ID", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_4(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index(None)
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_5(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("XXaccount_idXX", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_6(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("ACCOUNT_ID", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_7(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index(None)
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_8(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("XXcategory_idXX", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_9(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("CATEGORY_ID", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_10(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index(None)
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_11(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("XXoccurred_atXX", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_12(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("OCCURRED_AT", DESCENDING)])
        self._indexes_ready = True

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_13(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = None

    async def xǁTransactionRepositoryǁ_ensure_indexes__mutmut_14(self) -> None:
        if self._indexes_ready:
            return
        await self._collection.create_index([("user_id", ASCENDING)])
        await self._collection.create_index([("account_id", ASCENDING)])
        await self._collection.create_index([("category_id", ASCENDING)])
        await self._collection.create_index([("occurred_at", DESCENDING)])
        self._indexes_ready = False
    
    xǁTransactionRepositoryǁ_ensure_indexes__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_1': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_1, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_2': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_2, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_3': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_3, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_4': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_4, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_5': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_5, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_6': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_6, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_7': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_7, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_8': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_8, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_9': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_9, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_10': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_10, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_11': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_11, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_12': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_12, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_13': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_13, 
        'xǁTransactionRepositoryǁ_ensure_indexes__mutmut_14': xǁTransactionRepositoryǁ_ensure_indexes__mutmut_14
    }
    
    def _ensure_indexes(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionRepositoryǁ_ensure_indexes__mutmut_orig"), object.__getattribute__(self, "xǁTransactionRepositoryǁ_ensure_indexes__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_indexes.__signature__ = _mutmut_signature(xǁTransactionRepositoryǁ_ensure_indexes__mutmut_orig)
    xǁTransactionRepositoryǁ_ensure_indexes__mutmut_orig.__name__ = 'xǁTransactionRepositoryǁ_ensure_indexes'


class InMemoryTransactionRepository(Repository[Transaction, str]):
    """In-memory repository for transactions."""

    def xǁInMemoryTransactionRepositoryǁ__init____mutmut_orig(self) -> None:
        self._storage: Dict[str, Transaction] = {}

    def xǁInMemoryTransactionRepositoryǁ__init____mutmut_1(self) -> None:
        self._storage: Dict[str, Transaction] = None
    
    xǁInMemoryTransactionRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁ__init____mutmut_1': xǁInMemoryTransactionRepositoryǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁ__init____mutmut_orig)
    xǁInMemoryTransactionRepositoryǁ__init____mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁ__init__'

    async def xǁInMemoryTransactionRepositoryǁcreate__mutmut_orig(self, entity: Transaction) -> Transaction:
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryTransactionRepositoryǁcreate__mutmut_1(self, entity: Transaction) -> Transaction:
        self._storage[entity.id] = None
        return entity
    
    xǁInMemoryTransactionRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁcreate__mutmut_1': xǁInMemoryTransactionRepositoryǁcreate__mutmut_1
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁcreate__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁcreate__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁcreate'

    async def xǁInMemoryTransactionRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[Transaction]:
        return self._storage.get(entity_id)

    async def xǁInMemoryTransactionRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[Transaction]:
        return self._storage.get(None)
    
    xǁInMemoryTransactionRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁget__mutmut_1': xǁInMemoryTransactionRepositoryǁget__mutmut_1
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁget__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁget__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁget'

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[Transaction]:
        transactions = None

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(None)

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = None
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get(None)
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("XXuser_idXX")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("USER_ID")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = None

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id != user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = None
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get(None)
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("XXaccount_idXX")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("ACCOUNT_ID")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = None

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id != account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = None
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get(None)
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("XXcategory_idXX")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("CATEGORY_ID")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = None

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id != category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = None
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get(None)
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("XXtransaction_typeXX")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("TRANSACTION_TYPE")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = None

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type != transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = None
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get(None)
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("XXtransfer_account_idXX")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("TRANSFER_ACCOUNT_ID")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = None

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id != transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = None
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get(None)
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("XXdate_fromXX")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("DATE_FROM")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_37(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = None

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_38(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at > date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_39(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = None
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_40(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get(None)
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_41(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("XXdate_toXX")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_42(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("DATE_TO")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_43(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = None

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_44(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at < date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_45(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=None, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_46(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=None)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_47(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_48(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, )
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_49(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: None, reverse=True)
        return transactions

    async def xǁInMemoryTransactionRepositoryǁlist__mutmut_50(self, **filters: object) -> Iterable[Transaction]:
        transactions = list(self._storage.values())

        user_id = filters.get("user_id")
        if isinstance(user_id, str):
            transactions = [txn for txn in transactions if txn.user_id == user_id]

        account_id = filters.get("account_id")
        if isinstance(account_id, str):
            transactions = [txn for txn in transactions if txn.account_id == account_id]

        category_id = filters.get("category_id")
        if isinstance(category_id, str):
            transactions = [txn for txn in transactions if txn.category_id == category_id]

        transaction_type = filters.get("transaction_type")
        if isinstance(transaction_type, str):
            transactions = [txn for txn in transactions if txn.transaction_type == transaction_type]

        transfer_account_id = filters.get("transfer_account_id")
        if isinstance(transfer_account_id, str):
            transactions = [
                txn for txn in transactions if txn.transfer_account_id == transfer_account_id
            ]

        date_from = filters.get("date_from")
        if isinstance(date_from, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at >= date_from]

        date_to = filters.get("date_to")
        if isinstance(date_to, datetime):
            transactions = [txn for txn in transactions if txn.occurred_at <= date_to]

        transactions.sort(key=lambda txn: txn.occurred_at, reverse=False)
        return transactions
    
    xǁInMemoryTransactionRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁlist__mutmut_1': xǁInMemoryTransactionRepositoryǁlist__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_2': xǁInMemoryTransactionRepositoryǁlist__mutmut_2, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_3': xǁInMemoryTransactionRepositoryǁlist__mutmut_3, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_4': xǁInMemoryTransactionRepositoryǁlist__mutmut_4, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_5': xǁInMemoryTransactionRepositoryǁlist__mutmut_5, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_6': xǁInMemoryTransactionRepositoryǁlist__mutmut_6, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_7': xǁInMemoryTransactionRepositoryǁlist__mutmut_7, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_8': xǁInMemoryTransactionRepositoryǁlist__mutmut_8, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_9': xǁInMemoryTransactionRepositoryǁlist__mutmut_9, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_10': xǁInMemoryTransactionRepositoryǁlist__mutmut_10, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_11': xǁInMemoryTransactionRepositoryǁlist__mutmut_11, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_12': xǁInMemoryTransactionRepositoryǁlist__mutmut_12, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_13': xǁInMemoryTransactionRepositoryǁlist__mutmut_13, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_14': xǁInMemoryTransactionRepositoryǁlist__mutmut_14, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_15': xǁInMemoryTransactionRepositoryǁlist__mutmut_15, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_16': xǁInMemoryTransactionRepositoryǁlist__mutmut_16, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_17': xǁInMemoryTransactionRepositoryǁlist__mutmut_17, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_18': xǁInMemoryTransactionRepositoryǁlist__mutmut_18, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_19': xǁInMemoryTransactionRepositoryǁlist__mutmut_19, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_20': xǁInMemoryTransactionRepositoryǁlist__mutmut_20, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_21': xǁInMemoryTransactionRepositoryǁlist__mutmut_21, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_22': xǁInMemoryTransactionRepositoryǁlist__mutmut_22, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_23': xǁInMemoryTransactionRepositoryǁlist__mutmut_23, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_24': xǁInMemoryTransactionRepositoryǁlist__mutmut_24, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_25': xǁInMemoryTransactionRepositoryǁlist__mutmut_25, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_26': xǁInMemoryTransactionRepositoryǁlist__mutmut_26, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_27': xǁInMemoryTransactionRepositoryǁlist__mutmut_27, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_28': xǁInMemoryTransactionRepositoryǁlist__mutmut_28, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_29': xǁInMemoryTransactionRepositoryǁlist__mutmut_29, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_30': xǁInMemoryTransactionRepositoryǁlist__mutmut_30, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_31': xǁInMemoryTransactionRepositoryǁlist__mutmut_31, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_32': xǁInMemoryTransactionRepositoryǁlist__mutmut_32, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_33': xǁInMemoryTransactionRepositoryǁlist__mutmut_33, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_34': xǁInMemoryTransactionRepositoryǁlist__mutmut_34, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_35': xǁInMemoryTransactionRepositoryǁlist__mutmut_35, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_36': xǁInMemoryTransactionRepositoryǁlist__mutmut_36, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_37': xǁInMemoryTransactionRepositoryǁlist__mutmut_37, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_38': xǁInMemoryTransactionRepositoryǁlist__mutmut_38, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_39': xǁInMemoryTransactionRepositoryǁlist__mutmut_39, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_40': xǁInMemoryTransactionRepositoryǁlist__mutmut_40, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_41': xǁInMemoryTransactionRepositoryǁlist__mutmut_41, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_42': xǁInMemoryTransactionRepositoryǁlist__mutmut_42, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_43': xǁInMemoryTransactionRepositoryǁlist__mutmut_43, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_44': xǁInMemoryTransactionRepositoryǁlist__mutmut_44, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_45': xǁInMemoryTransactionRepositoryǁlist__mutmut_45, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_46': xǁInMemoryTransactionRepositoryǁlist__mutmut_46, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_47': xǁInMemoryTransactionRepositoryǁlist__mutmut_47, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_48': xǁInMemoryTransactionRepositoryǁlist__mutmut_48, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_49': xǁInMemoryTransactionRepositoryǁlist__mutmut_49, 
        'xǁInMemoryTransactionRepositoryǁlist__mutmut_50': xǁInMemoryTransactionRepositoryǁlist__mutmut_50
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁlist__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁlist__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁlist'

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = None
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(None)
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if not transaction:
            return None
        updated_data = None
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(None)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = None
        self._storage[entity_id] = updated_transaction
        return updated_transaction

    async def xǁInMemoryTransactionRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[Transaction]:
        transaction = await self.get(entity_id)
        if not transaction:
            return None
        updated_data = transaction.model_dump()
        updated_data.update(data)
        updated_transaction = Transaction(**updated_data)
        self._storage[entity_id] = None
        return updated_transaction
    
    xǁInMemoryTransactionRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁupdate__mutmut_1': xǁInMemoryTransactionRepositoryǁupdate__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁupdate__mutmut_2': xǁInMemoryTransactionRepositoryǁupdate__mutmut_2, 
        'xǁInMemoryTransactionRepositoryǁupdate__mutmut_3': xǁInMemoryTransactionRepositoryǁupdate__mutmut_3, 
        'xǁInMemoryTransactionRepositoryǁupdate__mutmut_4': xǁInMemoryTransactionRepositoryǁupdate__mutmut_4, 
        'xǁInMemoryTransactionRepositoryǁupdate__mutmut_5': xǁInMemoryTransactionRepositoryǁupdate__mutmut_5, 
        'xǁInMemoryTransactionRepositoryǁupdate__mutmut_6': xǁInMemoryTransactionRepositoryǁupdate__mutmut_6, 
        'xǁInMemoryTransactionRepositoryǁupdate__mutmut_7': xǁInMemoryTransactionRepositoryǁupdate__mutmut_7
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁupdate__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁupdate__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁupdate'

    async def xǁInMemoryTransactionRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def xǁInMemoryTransactionRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        return self._storage.pop(None, None) is not None

    async def xǁInMemoryTransactionRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        return self._storage.pop(None) is not None

    async def xǁInMemoryTransactionRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, ) is not None

    async def xǁInMemoryTransactionRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is None
    
    xǁInMemoryTransactionRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁdelete__mutmut_1': xǁInMemoryTransactionRepositoryǁdelete__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁdelete__mutmut_2': xǁInMemoryTransactionRepositoryǁdelete__mutmut_2, 
        'xǁInMemoryTransactionRepositoryǁdelete__mutmut_3': xǁInMemoryTransactionRepositoryǁdelete__mutmut_3, 
        'xǁInMemoryTransactionRepositoryǁdelete__mutmut_4': xǁInMemoryTransactionRepositoryǁdelete__mutmut_4
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁdelete__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁdelete__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁdelete'

    async def xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_orig(self, account_id: str) -> bool:
        return any(txn.account_id == account_id for txn in self._storage.values())

    async def xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_1(self, account_id: str) -> bool:
        return any(None)

    async def xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_2(self, account_id: str) -> bool:
        return any(txn.account_id != account_id for txn in self._storage.values())
    
    xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_1': xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_2': xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_2
    }
    
    def exists_for_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    exists_for_account.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁexists_for_account__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁexists_for_account'

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_orig(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_1(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id == category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_2(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                break
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_3(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id or txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_4(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id == user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_5(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                break
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_6(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None or txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_7(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_8(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year == year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_9(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                break
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_10(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None or txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_11(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is None and txn.occurred_at.month != month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_12(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month == month:
                continue
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_13(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                break
            return True
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_14(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return False
        return False

    async def xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_15(
        self,
        category_id: str,
        *,
        user_id: str | None = None,
        year: int | None = None,
        month: int | None = None,
    ) -> bool:
        for txn in self._storage.values():
            if txn.category_id != category_id:
                continue
            if user_id and txn.user_id != user_id:
                continue
            if year is not None and txn.occurred_at.year != year:
                continue
            if month is not None and txn.occurred_at.month != month:
                continue
            return True
        return True
    
    xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_1': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_2': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_2, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_3': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_3, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_4': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_4, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_5': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_5, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_6': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_6, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_7': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_7, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_8': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_8, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_9': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_9, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_10': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_10, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_11': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_11, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_12': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_12, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_13': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_13, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_14': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_14, 
        'xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_15': xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_15
    }
    
    def exists_for_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    exists_for_category.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁexists_for_category__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁexists_for_category'

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_1(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = None
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_2(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id == user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_3(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                break
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_4(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year and txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_5(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year == year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_6(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month == month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_7(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                break
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_8(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = None
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_9(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_10(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = None
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_11(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "XXcategory_idXX": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_12(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "CATEGORY_ID": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_13(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "XXtransaction_typeXX": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_14(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "TRANSACTION_TYPE": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_15(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "XXtotalXX": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_16(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "TOTAL": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_17(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal(None),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_18(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("XX0XX"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_19(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "XXcountXX": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_20(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "COUNT": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_21(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 1,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_22(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] = txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_23(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] -= txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_24(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["XXtotalXX"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_25(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["TOTAL"] += txn.amount
            summary[key]["count"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_26(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] = 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_27(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] -= 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_28(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["XXcountXX"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_29(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["COUNT"] += 1
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_30(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 2
        return list(summary.values())

    async def xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_31(
        self,
        user_id: str,
        *,
        year: int,
        month: int,
    ) -> list[dict[str, object]]:
        summary: dict[tuple[str, str], dict[str, object]] = {}
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            key = (txn.category_id, txn.transaction_type)
            if key not in summary:
                summary[key] = {
                    "category_id": txn.category_id,
                    "transaction_type": txn.transaction_type,
                    "total": Decimal("0"),
                    "count": 0,
                }
            summary[key]["total"] += txn.amount
            summary[key]["count"] += 1
        return list(None)
    
    xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_1': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_2': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_2, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_3': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_3, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_4': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_4, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_5': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_5, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_6': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_6, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_7': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_7, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_8': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_8, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_9': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_9, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_10': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_10, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_11': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_11, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_12': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_12, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_13': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_13, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_14': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_14, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_15': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_15, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_16': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_16, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_17': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_17, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_18': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_18, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_19': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_19, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_20': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_20, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_21': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_21, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_22': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_22, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_23': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_23, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_24': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_24, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_25': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_25, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_26': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_26, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_27': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_27, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_28': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_28, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_29': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_29, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_30': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_30, 
        'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_31': xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_31
    }
    
    def aggregate_monthly_summary(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_mutants"), args, kwargs, self)
        return result 
    
    aggregate_monthly_summary.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁaggregate_monthly_summary'

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_orig(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_1(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = None
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_2(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal(None)
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_3(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("XX0XX")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_4(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id == user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_5(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                break
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_6(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id == category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_7(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                break
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_8(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year and txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_9(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year == year or txn.occurred_at.month != month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_10(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month == month:
                continue
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_11(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                break
            total += txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_12(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total = txn.amount
        return total

    async def xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_13(
        self,
        *,
        user_id: str,
        category_id: str,
        year: int,
        month: int,
    ) -> Decimal:
        total = Decimal("0")
        for txn in self._storage.values():
            if txn.user_id != user_id:
                continue
            if txn.category_id != category_id:
                continue
            if txn.occurred_at.year != year or txn.occurred_at.month != month:
                continue
            total -= txn.amount
        return total
    
    xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_1': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_1, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_2': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_2, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_3': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_3, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_4': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_4, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_5': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_5, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_6': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_6, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_7': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_7, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_8': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_8, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_9': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_9, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_10': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_10, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_11': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_11, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_12': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_12, 
        'xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_13': xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_13
    }
    
    def sum_for_category_period(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sum_for_category_period.__signature__ = _mutmut_signature(xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_orig)
    xǁInMemoryTransactionRepositoryǁsum_for_category_period__mutmut_orig.__name__ = 'xǁInMemoryTransactionRepositoryǁsum_for_category_period'


def x__transaction_to_document__mutmut_orig(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_1(transaction: Transaction) -> Dict[str, object]:
    data = None
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_2(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = None
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_3(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["XX_idXX"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_4(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_ID"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_5(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(None)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_6(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = None
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_7(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["XXuser_idXX"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_8(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["USER_ID"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_9(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(None)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_10(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = None
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_11(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["XXaccount_idXX"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_12(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["ACCOUNT_ID"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_13(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(None)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_14(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = None
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_15(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["XXcategory_idXX"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_16(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["CATEGORY_ID"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_17(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(None)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_18(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = None
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_19(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["XXtransfer_account_idXX"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_20(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["TRANSFER_ACCOUNT_ID"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_21(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(None)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_22(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = ""
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_23(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["XXtransfer_account_idXX"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_24(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["TRANSFER_ACCOUNT_ID"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_25(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = None
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_26(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["XXamountXX"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_27(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["AMOUNT"] = Decimal128(str(transaction.amount))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_28(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(None)
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_29(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(None))
    data.pop("id", None)
    return data


def x__transaction_to_document__mutmut_30(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop(None, None)
    return data


def x__transaction_to_document__mutmut_31(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop(None)
    return data


def x__transaction_to_document__mutmut_32(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("id", )
    return data


def x__transaction_to_document__mutmut_33(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("XXidXX", None)
    return data


def x__transaction_to_document__mutmut_34(transaction: Transaction) -> Dict[str, object]:
    data = transaction.model_dump()
    data["_id"] = ensure_object_id(transaction.id)
    data["user_id"] = ensure_object_id(transaction.user_id)
    data["account_id"] = ensure_object_id(transaction.account_id)
    data["category_id"] = ensure_object_id(transaction.category_id)
    if transaction.transfer_account_id:
        data["transfer_account_id"] = ensure_object_id(transaction.transfer_account_id)
    else:
        data["transfer_account_id"] = None
    data["amount"] = Decimal128(str(transaction.amount))
    data.pop("ID", None)
    return data

x__transaction_to_document__mutmut_mutants : ClassVar[MutantDict] = {
'x__transaction_to_document__mutmut_1': x__transaction_to_document__mutmut_1, 
    'x__transaction_to_document__mutmut_2': x__transaction_to_document__mutmut_2, 
    'x__transaction_to_document__mutmut_3': x__transaction_to_document__mutmut_3, 
    'x__transaction_to_document__mutmut_4': x__transaction_to_document__mutmut_4, 
    'x__transaction_to_document__mutmut_5': x__transaction_to_document__mutmut_5, 
    'x__transaction_to_document__mutmut_6': x__transaction_to_document__mutmut_6, 
    'x__transaction_to_document__mutmut_7': x__transaction_to_document__mutmut_7, 
    'x__transaction_to_document__mutmut_8': x__transaction_to_document__mutmut_8, 
    'x__transaction_to_document__mutmut_9': x__transaction_to_document__mutmut_9, 
    'x__transaction_to_document__mutmut_10': x__transaction_to_document__mutmut_10, 
    'x__transaction_to_document__mutmut_11': x__transaction_to_document__mutmut_11, 
    'x__transaction_to_document__mutmut_12': x__transaction_to_document__mutmut_12, 
    'x__transaction_to_document__mutmut_13': x__transaction_to_document__mutmut_13, 
    'x__transaction_to_document__mutmut_14': x__transaction_to_document__mutmut_14, 
    'x__transaction_to_document__mutmut_15': x__transaction_to_document__mutmut_15, 
    'x__transaction_to_document__mutmut_16': x__transaction_to_document__mutmut_16, 
    'x__transaction_to_document__mutmut_17': x__transaction_to_document__mutmut_17, 
    'x__transaction_to_document__mutmut_18': x__transaction_to_document__mutmut_18, 
    'x__transaction_to_document__mutmut_19': x__transaction_to_document__mutmut_19, 
    'x__transaction_to_document__mutmut_20': x__transaction_to_document__mutmut_20, 
    'x__transaction_to_document__mutmut_21': x__transaction_to_document__mutmut_21, 
    'x__transaction_to_document__mutmut_22': x__transaction_to_document__mutmut_22, 
    'x__transaction_to_document__mutmut_23': x__transaction_to_document__mutmut_23, 
    'x__transaction_to_document__mutmut_24': x__transaction_to_document__mutmut_24, 
    'x__transaction_to_document__mutmut_25': x__transaction_to_document__mutmut_25, 
    'x__transaction_to_document__mutmut_26': x__transaction_to_document__mutmut_26, 
    'x__transaction_to_document__mutmut_27': x__transaction_to_document__mutmut_27, 
    'x__transaction_to_document__mutmut_28': x__transaction_to_document__mutmut_28, 
    'x__transaction_to_document__mutmut_29': x__transaction_to_document__mutmut_29, 
    'x__transaction_to_document__mutmut_30': x__transaction_to_document__mutmut_30, 
    'x__transaction_to_document__mutmut_31': x__transaction_to_document__mutmut_31, 
    'x__transaction_to_document__mutmut_32': x__transaction_to_document__mutmut_32, 
    'x__transaction_to_document__mutmut_33': x__transaction_to_document__mutmut_33, 
    'x__transaction_to_document__mutmut_34': x__transaction_to_document__mutmut_34
}

def _transaction_to_document(*args, **kwargs):
    result = _mutmut_trampoline(x__transaction_to_document__mutmut_orig, x__transaction_to_document__mutmut_mutants, args, kwargs)
    return result 

_transaction_to_document.__signature__ = _mutmut_signature(x__transaction_to_document__mutmut_orig)
x__transaction_to_document__mutmut_orig.__name__ = 'x__transaction_to_document'


def x__document_to_transaction__mutmut_orig(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_1(document: Dict[str, object]) -> Transaction:
    document = None
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_2(document: Dict[str, object]) -> Transaction:
    document = dict(None)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_3(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = None
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_4(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["XXidXX"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_5(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["ID"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_6(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(None)
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_7(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop(None))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_8(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("XX_idXX"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_9(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_ID"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_10(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = None
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_11(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["XXuser_idXX"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_12(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["USER_ID"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_13(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(None)
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_14(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["XXuser_idXX"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_15(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["USER_ID"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_16(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = None
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_17(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["XXaccount_idXX"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_18(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["ACCOUNT_ID"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_19(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(None)
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_20(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["XXaccount_idXX"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_21(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["ACCOUNT_ID"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_22(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = None
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_23(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["XXcategory_idXX"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_24(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["CATEGORY_ID"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_25(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(None)
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_26(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["XXcategory_idXX"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_27(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["CATEGORY_ID"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_28(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = None
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_29(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get(None)
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_30(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("XXtransfer_account_idXX")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_31(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("TRANSFER_ACCOUNT_ID")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_32(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = None
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_33(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["XXtransfer_account_idXX"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_34(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["TRANSFER_ACCOUNT_ID"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_35(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(None)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_36(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = None
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_37(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get(None, Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_38(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", None)
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_39(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get(Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_40(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", )
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_41(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("XXamountXX", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_42(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("AMOUNT", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_43(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal(None))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_44(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("XX0XX"))
    if isinstance(amount, Decimal128):
        document["amount"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_45(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["amount"] = None
    return Transaction(**document)


def x__document_to_transaction__mutmut_46(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["XXamountXX"] = amount.to_decimal()
    return Transaction(**document)


def x__document_to_transaction__mutmut_47(document: Dict[str, object]) -> Transaction:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    document["user_id"] = str(document["user_id"])
    document["account_id"] = str(document["account_id"])
    document["category_id"] = str(document["category_id"])
    transfer_account_id = document.get("transfer_account_id")
    if transfer_account_id:
        document["transfer_account_id"] = str(transfer_account_id)
    amount = document.get("amount", Decimal("0"))
    if isinstance(amount, Decimal128):
        document["AMOUNT"] = amount.to_decimal()
    return Transaction(**document)

x__document_to_transaction__mutmut_mutants : ClassVar[MutantDict] = {
'x__document_to_transaction__mutmut_1': x__document_to_transaction__mutmut_1, 
    'x__document_to_transaction__mutmut_2': x__document_to_transaction__mutmut_2, 
    'x__document_to_transaction__mutmut_3': x__document_to_transaction__mutmut_3, 
    'x__document_to_transaction__mutmut_4': x__document_to_transaction__mutmut_4, 
    'x__document_to_transaction__mutmut_5': x__document_to_transaction__mutmut_5, 
    'x__document_to_transaction__mutmut_6': x__document_to_transaction__mutmut_6, 
    'x__document_to_transaction__mutmut_7': x__document_to_transaction__mutmut_7, 
    'x__document_to_transaction__mutmut_8': x__document_to_transaction__mutmut_8, 
    'x__document_to_transaction__mutmut_9': x__document_to_transaction__mutmut_9, 
    'x__document_to_transaction__mutmut_10': x__document_to_transaction__mutmut_10, 
    'x__document_to_transaction__mutmut_11': x__document_to_transaction__mutmut_11, 
    'x__document_to_transaction__mutmut_12': x__document_to_transaction__mutmut_12, 
    'x__document_to_transaction__mutmut_13': x__document_to_transaction__mutmut_13, 
    'x__document_to_transaction__mutmut_14': x__document_to_transaction__mutmut_14, 
    'x__document_to_transaction__mutmut_15': x__document_to_transaction__mutmut_15, 
    'x__document_to_transaction__mutmut_16': x__document_to_transaction__mutmut_16, 
    'x__document_to_transaction__mutmut_17': x__document_to_transaction__mutmut_17, 
    'x__document_to_transaction__mutmut_18': x__document_to_transaction__mutmut_18, 
    'x__document_to_transaction__mutmut_19': x__document_to_transaction__mutmut_19, 
    'x__document_to_transaction__mutmut_20': x__document_to_transaction__mutmut_20, 
    'x__document_to_transaction__mutmut_21': x__document_to_transaction__mutmut_21, 
    'x__document_to_transaction__mutmut_22': x__document_to_transaction__mutmut_22, 
    'x__document_to_transaction__mutmut_23': x__document_to_transaction__mutmut_23, 
    'x__document_to_transaction__mutmut_24': x__document_to_transaction__mutmut_24, 
    'x__document_to_transaction__mutmut_25': x__document_to_transaction__mutmut_25, 
    'x__document_to_transaction__mutmut_26': x__document_to_transaction__mutmut_26, 
    'x__document_to_transaction__mutmut_27': x__document_to_transaction__mutmut_27, 
    'x__document_to_transaction__mutmut_28': x__document_to_transaction__mutmut_28, 
    'x__document_to_transaction__mutmut_29': x__document_to_transaction__mutmut_29, 
    'x__document_to_transaction__mutmut_30': x__document_to_transaction__mutmut_30, 
    'x__document_to_transaction__mutmut_31': x__document_to_transaction__mutmut_31, 
    'x__document_to_transaction__mutmut_32': x__document_to_transaction__mutmut_32, 
    'x__document_to_transaction__mutmut_33': x__document_to_transaction__mutmut_33, 
    'x__document_to_transaction__mutmut_34': x__document_to_transaction__mutmut_34, 
    'x__document_to_transaction__mutmut_35': x__document_to_transaction__mutmut_35, 
    'x__document_to_transaction__mutmut_36': x__document_to_transaction__mutmut_36, 
    'x__document_to_transaction__mutmut_37': x__document_to_transaction__mutmut_37, 
    'x__document_to_transaction__mutmut_38': x__document_to_transaction__mutmut_38, 
    'x__document_to_transaction__mutmut_39': x__document_to_transaction__mutmut_39, 
    'x__document_to_transaction__mutmut_40': x__document_to_transaction__mutmut_40, 
    'x__document_to_transaction__mutmut_41': x__document_to_transaction__mutmut_41, 
    'x__document_to_transaction__mutmut_42': x__document_to_transaction__mutmut_42, 
    'x__document_to_transaction__mutmut_43': x__document_to_transaction__mutmut_43, 
    'x__document_to_transaction__mutmut_44': x__document_to_transaction__mutmut_44, 
    'x__document_to_transaction__mutmut_45': x__document_to_transaction__mutmut_45, 
    'x__document_to_transaction__mutmut_46': x__document_to_transaction__mutmut_46, 
    'x__document_to_transaction__mutmut_47': x__document_to_transaction__mutmut_47
}

def _document_to_transaction(*args, **kwargs):
    result = _mutmut_trampoline(x__document_to_transaction__mutmut_orig, x__document_to_transaction__mutmut_mutants, args, kwargs)
    return result 

_document_to_transaction.__signature__ = _mutmut_signature(x__document_to_transaction__mutmut_orig)
x__document_to_transaction__mutmut_orig.__name__ = 'x__document_to_transaction'


def x__prepare_transaction_update__mutmut_orig(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_1(data: Dict[str, object]) -> Dict[str, object]:
    update_data = None
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_2(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(None)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_3(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "XXuser_idXX" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_4(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "USER_ID" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_5(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" not in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_6(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = None
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_7(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["XXuser_idXX"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_8(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["USER_ID"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_9(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(None)
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_10(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(None))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_11(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["XXuser_idXX"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_12(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["USER_ID"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_13(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "XXaccount_idXX" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_14(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "ACCOUNT_ID" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_15(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" not in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_16(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = None
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_17(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["XXaccount_idXX"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_18(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["ACCOUNT_ID"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_19(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(None)
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_20(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(None))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_21(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["XXaccount_idXX"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_22(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["ACCOUNT_ID"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_23(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "XXcategory_idXX" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_24(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "CATEGORY_ID" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_25(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" not in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_26(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = None
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_27(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["XXcategory_idXX"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_28(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["CATEGORY_ID"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_29(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(None)
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_30(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(None))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_31(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["XXcategory_idXX"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_32(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["CATEGORY_ID"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_33(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "XXtransfer_account_idXX" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_34(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "TRANSFER_ACCOUNT_ID" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_35(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" not in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_36(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = None
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_37(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["XXtransfer_account_idXX"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_38(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["TRANSFER_ACCOUNT_ID"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_39(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = None
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_40(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["XXtransfer_account_idXX"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_41(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["TRANSFER_ACCOUNT_ID"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_42(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(None) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_43(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(None)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_44(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data or update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_45(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "XXamountXX" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_46(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "AMOUNT" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_47(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" not in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_48(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["XXamountXX"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_49(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["AMOUNT"] is not None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_50(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is None:
        update_data["amount"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_51(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = None
    return update_data


def x__prepare_transaction_update__mutmut_52(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["XXamountXX"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_53(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["AMOUNT"] = Decimal128(str(update_data["amount"]))
    return update_data


def x__prepare_transaction_update__mutmut_54(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(None)
    return update_data


def x__prepare_transaction_update__mutmut_55(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(None))
    return update_data


def x__prepare_transaction_update__mutmut_56(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["XXamountXX"]))
    return update_data


def x__prepare_transaction_update__mutmut_57(data: Dict[str, object]) -> Dict[str, object]:
    update_data = dict(data)
    if "user_id" in update_data:
        update_data["user_id"] = ensure_object_id(str(update_data["user_id"]))
    if "account_id" in update_data:
        update_data["account_id"] = ensure_object_id(str(update_data["account_id"]))
    if "category_id" in update_data:
        update_data["category_id"] = ensure_object_id(str(update_data["category_id"]))
    if "transfer_account_id" in update_data:
        transfer_value = update_data["transfer_account_id"]
        update_data["transfer_account_id"] = (
            ensure_object_id(str(transfer_value)) if transfer_value else None
        )
    if "amount" in update_data and update_data["amount"] is not None:
        update_data["amount"] = Decimal128(str(update_data["AMOUNT"]))
    return update_data

x__prepare_transaction_update__mutmut_mutants : ClassVar[MutantDict] = {
'x__prepare_transaction_update__mutmut_1': x__prepare_transaction_update__mutmut_1, 
    'x__prepare_transaction_update__mutmut_2': x__prepare_transaction_update__mutmut_2, 
    'x__prepare_transaction_update__mutmut_3': x__prepare_transaction_update__mutmut_3, 
    'x__prepare_transaction_update__mutmut_4': x__prepare_transaction_update__mutmut_4, 
    'x__prepare_transaction_update__mutmut_5': x__prepare_transaction_update__mutmut_5, 
    'x__prepare_transaction_update__mutmut_6': x__prepare_transaction_update__mutmut_6, 
    'x__prepare_transaction_update__mutmut_7': x__prepare_transaction_update__mutmut_7, 
    'x__prepare_transaction_update__mutmut_8': x__prepare_transaction_update__mutmut_8, 
    'x__prepare_transaction_update__mutmut_9': x__prepare_transaction_update__mutmut_9, 
    'x__prepare_transaction_update__mutmut_10': x__prepare_transaction_update__mutmut_10, 
    'x__prepare_transaction_update__mutmut_11': x__prepare_transaction_update__mutmut_11, 
    'x__prepare_transaction_update__mutmut_12': x__prepare_transaction_update__mutmut_12, 
    'x__prepare_transaction_update__mutmut_13': x__prepare_transaction_update__mutmut_13, 
    'x__prepare_transaction_update__mutmut_14': x__prepare_transaction_update__mutmut_14, 
    'x__prepare_transaction_update__mutmut_15': x__prepare_transaction_update__mutmut_15, 
    'x__prepare_transaction_update__mutmut_16': x__prepare_transaction_update__mutmut_16, 
    'x__prepare_transaction_update__mutmut_17': x__prepare_transaction_update__mutmut_17, 
    'x__prepare_transaction_update__mutmut_18': x__prepare_transaction_update__mutmut_18, 
    'x__prepare_transaction_update__mutmut_19': x__prepare_transaction_update__mutmut_19, 
    'x__prepare_transaction_update__mutmut_20': x__prepare_transaction_update__mutmut_20, 
    'x__prepare_transaction_update__mutmut_21': x__prepare_transaction_update__mutmut_21, 
    'x__prepare_transaction_update__mutmut_22': x__prepare_transaction_update__mutmut_22, 
    'x__prepare_transaction_update__mutmut_23': x__prepare_transaction_update__mutmut_23, 
    'x__prepare_transaction_update__mutmut_24': x__prepare_transaction_update__mutmut_24, 
    'x__prepare_transaction_update__mutmut_25': x__prepare_transaction_update__mutmut_25, 
    'x__prepare_transaction_update__mutmut_26': x__prepare_transaction_update__mutmut_26, 
    'x__prepare_transaction_update__mutmut_27': x__prepare_transaction_update__mutmut_27, 
    'x__prepare_transaction_update__mutmut_28': x__prepare_transaction_update__mutmut_28, 
    'x__prepare_transaction_update__mutmut_29': x__prepare_transaction_update__mutmut_29, 
    'x__prepare_transaction_update__mutmut_30': x__prepare_transaction_update__mutmut_30, 
    'x__prepare_transaction_update__mutmut_31': x__prepare_transaction_update__mutmut_31, 
    'x__prepare_transaction_update__mutmut_32': x__prepare_transaction_update__mutmut_32, 
    'x__prepare_transaction_update__mutmut_33': x__prepare_transaction_update__mutmut_33, 
    'x__prepare_transaction_update__mutmut_34': x__prepare_transaction_update__mutmut_34, 
    'x__prepare_transaction_update__mutmut_35': x__prepare_transaction_update__mutmut_35, 
    'x__prepare_transaction_update__mutmut_36': x__prepare_transaction_update__mutmut_36, 
    'x__prepare_transaction_update__mutmut_37': x__prepare_transaction_update__mutmut_37, 
    'x__prepare_transaction_update__mutmut_38': x__prepare_transaction_update__mutmut_38, 
    'x__prepare_transaction_update__mutmut_39': x__prepare_transaction_update__mutmut_39, 
    'x__prepare_transaction_update__mutmut_40': x__prepare_transaction_update__mutmut_40, 
    'x__prepare_transaction_update__mutmut_41': x__prepare_transaction_update__mutmut_41, 
    'x__prepare_transaction_update__mutmut_42': x__prepare_transaction_update__mutmut_42, 
    'x__prepare_transaction_update__mutmut_43': x__prepare_transaction_update__mutmut_43, 
    'x__prepare_transaction_update__mutmut_44': x__prepare_transaction_update__mutmut_44, 
    'x__prepare_transaction_update__mutmut_45': x__prepare_transaction_update__mutmut_45, 
    'x__prepare_transaction_update__mutmut_46': x__prepare_transaction_update__mutmut_46, 
    'x__prepare_transaction_update__mutmut_47': x__prepare_transaction_update__mutmut_47, 
    'x__prepare_transaction_update__mutmut_48': x__prepare_transaction_update__mutmut_48, 
    'x__prepare_transaction_update__mutmut_49': x__prepare_transaction_update__mutmut_49, 
    'x__prepare_transaction_update__mutmut_50': x__prepare_transaction_update__mutmut_50, 
    'x__prepare_transaction_update__mutmut_51': x__prepare_transaction_update__mutmut_51, 
    'x__prepare_transaction_update__mutmut_52': x__prepare_transaction_update__mutmut_52, 
    'x__prepare_transaction_update__mutmut_53': x__prepare_transaction_update__mutmut_53, 
    'x__prepare_transaction_update__mutmut_54': x__prepare_transaction_update__mutmut_54, 
    'x__prepare_transaction_update__mutmut_55': x__prepare_transaction_update__mutmut_55, 
    'x__prepare_transaction_update__mutmut_56': x__prepare_transaction_update__mutmut_56, 
    'x__prepare_transaction_update__mutmut_57': x__prepare_transaction_update__mutmut_57
}

def _prepare_transaction_update(*args, **kwargs):
    result = _mutmut_trampoline(x__prepare_transaction_update__mutmut_orig, x__prepare_transaction_update__mutmut_mutants, args, kwargs)
    return result 

_prepare_transaction_update.__signature__ = _mutmut_signature(x__prepare_transaction_update__mutmut_orig)
x__prepare_transaction_update__mutmut_orig.__name__ = 'x__prepare_transaction_update'
