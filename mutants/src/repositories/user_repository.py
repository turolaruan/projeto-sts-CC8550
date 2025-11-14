"""User repository implementations."""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.models.common import ensure_object_id
from src.models.user import User
from src.repositories.base import Repository
from src.repositories.mongo_compat import (
    ASCENDING,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
    DuplicateKeyError,
    ReturnDocument,
    ensure_motor_dependencies,
)
from src.utils.exceptions import EntityAlreadyExistsError
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


class UserRepository(Repository[User, str]):
    """Mongo-backed repository for users."""

    def xǁUserRepositoryǁ__init____mutmut_orig(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("users")
        self._indexes_ready: bool = False

    def xǁUserRepositoryǁ__init____mutmut_1(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = None
        self._indexes_ready: bool = False

    def xǁUserRepositoryǁ__init____mutmut_2(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection(None)
        self._indexes_ready: bool = False

    def xǁUserRepositoryǁ__init____mutmut_3(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("XXusersXX")
        self._indexes_ready: bool = False

    def xǁUserRepositoryǁ__init____mutmut_4(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("USERS")
        self._indexes_ready: bool = False

    def xǁUserRepositoryǁ__init____mutmut_5(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("users")
        self._indexes_ready: bool = None

    def xǁUserRepositoryǁ__init____mutmut_6(self, database: AsyncIOMotorDatabase) -> None:
        ensure_motor_dependencies()
        self._collection: AsyncIOMotorCollection = database.get_collection("users")
        self._indexes_ready: bool = True
    
    xǁUserRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁ__init____mutmut_1': xǁUserRepositoryǁ__init____mutmut_1, 
        'xǁUserRepositoryǁ__init____mutmut_2': xǁUserRepositoryǁ__init____mutmut_2, 
        'xǁUserRepositoryǁ__init____mutmut_3': xǁUserRepositoryǁ__init____mutmut_3, 
        'xǁUserRepositoryǁ__init____mutmut_4': xǁUserRepositoryǁ__init____mutmut_4, 
        'xǁUserRepositoryǁ__init____mutmut_5': xǁUserRepositoryǁ__init____mutmut_5, 
        'xǁUserRepositoryǁ__init____mutmut_6': xǁUserRepositoryǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUserRepositoryǁ__init____mutmut_orig)
    xǁUserRepositoryǁ__init____mutmut_orig.__name__ = 'xǁUserRepositoryǁ__init__'

    async def xǁUserRepositoryǁcreate__mutmut_orig(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_1(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = None
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_2(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(None)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_3(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(None)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_4(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                None,
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_5(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context=None,
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_6(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_7(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_8(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "XXUser with this email already existsXX",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_9(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "user with this email already exists",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_10(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "USER WITH THIS EMAIL ALREADY EXISTS",
                context={"email": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_11(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"XXemailXX": entity.email},
            ) from exc
        return entity

    async def xǁUserRepositoryǁcreate__mutmut_12(self, entity: User) -> User:
        """Persist a new user document."""
        await self._ensure_indexes()
        document = _user_to_document(entity)
        try:
            await self._collection.insert_one(document)
        except DuplicateKeyError as exc:  # pragma: no cover - depends on DB state
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"EMAIL": entity.email},
            ) from exc
        return entity
    
    xǁUserRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁcreate__mutmut_1': xǁUserRepositoryǁcreate__mutmut_1, 
        'xǁUserRepositoryǁcreate__mutmut_2': xǁUserRepositoryǁcreate__mutmut_2, 
        'xǁUserRepositoryǁcreate__mutmut_3': xǁUserRepositoryǁcreate__mutmut_3, 
        'xǁUserRepositoryǁcreate__mutmut_4': xǁUserRepositoryǁcreate__mutmut_4, 
        'xǁUserRepositoryǁcreate__mutmut_5': xǁUserRepositoryǁcreate__mutmut_5, 
        'xǁUserRepositoryǁcreate__mutmut_6': xǁUserRepositoryǁcreate__mutmut_6, 
        'xǁUserRepositoryǁcreate__mutmut_7': xǁUserRepositoryǁcreate__mutmut_7, 
        'xǁUserRepositoryǁcreate__mutmut_8': xǁUserRepositoryǁcreate__mutmut_8, 
        'xǁUserRepositoryǁcreate__mutmut_9': xǁUserRepositoryǁcreate__mutmut_9, 
        'xǁUserRepositoryǁcreate__mutmut_10': xǁUserRepositoryǁcreate__mutmut_10, 
        'xǁUserRepositoryǁcreate__mutmut_11': xǁUserRepositoryǁcreate__mutmut_11, 
        'xǁUserRepositoryǁcreate__mutmut_12': xǁUserRepositoryǁcreate__mutmut_12
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁUserRepositoryǁcreate__mutmut_orig)
    xǁUserRepositoryǁcreate__mutmut_orig.__name__ = 'xǁUserRepositoryǁcreate'

    async def xǁUserRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = None
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_2(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one(None)
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_3(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"XX_idXX": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_4(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"_ID": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_5(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"_id": ensure_object_id(None)})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_6(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget__mutmut_7(self, entity_id: str) -> Optional[User]:
        """Fetch a user by identifier."""
        document = await self._collection.find_one({"_id": ensure_object_id(entity_id)})
        if not document:
            return None
        return _document_to_user(None)
    
    xǁUserRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁget__mutmut_1': xǁUserRepositoryǁget__mutmut_1, 
        'xǁUserRepositoryǁget__mutmut_2': xǁUserRepositoryǁget__mutmut_2, 
        'xǁUserRepositoryǁget__mutmut_3': xǁUserRepositoryǁget__mutmut_3, 
        'xǁUserRepositoryǁget__mutmut_4': xǁUserRepositoryǁget__mutmut_4, 
        'xǁUserRepositoryǁget__mutmut_5': xǁUserRepositoryǁget__mutmut_5, 
        'xǁUserRepositoryǁget__mutmut_6': xǁUserRepositoryǁget__mutmut_6, 
        'xǁUserRepositoryǁget__mutmut_7': xǁUserRepositoryǁget__mutmut_7
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁUserRepositoryǁget__mutmut_orig)
    xǁUserRepositoryǁget__mutmut_orig.__name__ = 'xǁUserRepositoryǁget'

    async def xǁUserRepositoryǁget_by_email__mutmut_orig(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"email": email.lower()})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_1(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = None
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_2(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one(None)
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_3(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"XXemailXX": email.lower()})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_4(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"EMAIL": email.lower()})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_5(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"email": email.upper()})
        if not document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_6(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"email": email.lower()})
        if document:
            return None
        return _document_to_user(document)

    async def xǁUserRepositoryǁget_by_email__mutmut_7(self, email: str) -> Optional[User]:
        """Fetch a user by email if it exists."""
        document = await self._collection.find_one({"email": email.lower()})
        if not document:
            return None
        return _document_to_user(None)
    
    xǁUserRepositoryǁget_by_email__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁget_by_email__mutmut_1': xǁUserRepositoryǁget_by_email__mutmut_1, 
        'xǁUserRepositoryǁget_by_email__mutmut_2': xǁUserRepositoryǁget_by_email__mutmut_2, 
        'xǁUserRepositoryǁget_by_email__mutmut_3': xǁUserRepositoryǁget_by_email__mutmut_3, 
        'xǁUserRepositoryǁget_by_email__mutmut_4': xǁUserRepositoryǁget_by_email__mutmut_4, 
        'xǁUserRepositoryǁget_by_email__mutmut_5': xǁUserRepositoryǁget_by_email__mutmut_5, 
        'xǁUserRepositoryǁget_by_email__mutmut_6': xǁUserRepositoryǁget_by_email__mutmut_6, 
        'xǁUserRepositoryǁget_by_email__mutmut_7': xǁUserRepositoryǁget_by_email__mutmut_7
    }
    
    def get_by_email(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁget_by_email__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁget_by_email__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_by_email.__signature__ = _mutmut_signature(xǁUserRepositoryǁget_by_email__mutmut_orig)
    xǁUserRepositoryǁget_by_email__mutmut_orig.__name__ = 'xǁUserRepositoryǁget_by_email'

    async def xǁUserRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = None
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = None
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get(None)
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("XXemailXX")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("EMAIL")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = None
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["XXemailXX"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["EMAIL"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.upper()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = None
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get(None)
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("XXdefault_currencyXX")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("DEFAULT_CURRENCY")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = None
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["XXdefault_currencyXX"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["DEFAULT_CURRENCY"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = None
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get(None)
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("XXnameXX")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("NAME")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = None

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["XXnameXX"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["NAME"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"XX$regexXX": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$REGEX": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_26(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "XX$optionsXX": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_27(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$OPTIONS": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_28(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "XXiXX"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_29(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "I"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_30(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = None
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_31(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort(None, ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_32(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", None)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_33(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort(ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_34(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", )
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_35(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(None).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_36(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.rfind(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_37(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("XXcreated_atXX", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_38(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("CREATED_AT", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_39(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = None
        async for document in cursor:
            results.append(_document_to_user(document))
        return results

    async def xǁUserRepositoryǁlist__mutmut_40(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(None)
        return results

    async def xǁUserRepositoryǁlist__mutmut_41(self, **filters: object) -> Iterable[User]:
        """Return users applying optional filters."""
        await self._ensure_indexes()
        query: Dict[str, object] = {}
        email = filters.get("email")
        if isinstance(email, str):
            query["email"] = email.lower()
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            query["default_currency"] = currency
        name = filters.get("name")
        if isinstance(name, str):
            query["name"] = {"$regex": name, "$options": "i"}

        cursor = self._collection.find(query).sort("created_at", ASCENDING)
        results: List[User] = []
        async for document in cursor:
            results.append(_document_to_user(None))
        return results
    
    xǁUserRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁlist__mutmut_1': xǁUserRepositoryǁlist__mutmut_1, 
        'xǁUserRepositoryǁlist__mutmut_2': xǁUserRepositoryǁlist__mutmut_2, 
        'xǁUserRepositoryǁlist__mutmut_3': xǁUserRepositoryǁlist__mutmut_3, 
        'xǁUserRepositoryǁlist__mutmut_4': xǁUserRepositoryǁlist__mutmut_4, 
        'xǁUserRepositoryǁlist__mutmut_5': xǁUserRepositoryǁlist__mutmut_5, 
        'xǁUserRepositoryǁlist__mutmut_6': xǁUserRepositoryǁlist__mutmut_6, 
        'xǁUserRepositoryǁlist__mutmut_7': xǁUserRepositoryǁlist__mutmut_7, 
        'xǁUserRepositoryǁlist__mutmut_8': xǁUserRepositoryǁlist__mutmut_8, 
        'xǁUserRepositoryǁlist__mutmut_9': xǁUserRepositoryǁlist__mutmut_9, 
        'xǁUserRepositoryǁlist__mutmut_10': xǁUserRepositoryǁlist__mutmut_10, 
        'xǁUserRepositoryǁlist__mutmut_11': xǁUserRepositoryǁlist__mutmut_11, 
        'xǁUserRepositoryǁlist__mutmut_12': xǁUserRepositoryǁlist__mutmut_12, 
        'xǁUserRepositoryǁlist__mutmut_13': xǁUserRepositoryǁlist__mutmut_13, 
        'xǁUserRepositoryǁlist__mutmut_14': xǁUserRepositoryǁlist__mutmut_14, 
        'xǁUserRepositoryǁlist__mutmut_15': xǁUserRepositoryǁlist__mutmut_15, 
        'xǁUserRepositoryǁlist__mutmut_16': xǁUserRepositoryǁlist__mutmut_16, 
        'xǁUserRepositoryǁlist__mutmut_17': xǁUserRepositoryǁlist__mutmut_17, 
        'xǁUserRepositoryǁlist__mutmut_18': xǁUserRepositoryǁlist__mutmut_18, 
        'xǁUserRepositoryǁlist__mutmut_19': xǁUserRepositoryǁlist__mutmut_19, 
        'xǁUserRepositoryǁlist__mutmut_20': xǁUserRepositoryǁlist__mutmut_20, 
        'xǁUserRepositoryǁlist__mutmut_21': xǁUserRepositoryǁlist__mutmut_21, 
        'xǁUserRepositoryǁlist__mutmut_22': xǁUserRepositoryǁlist__mutmut_22, 
        'xǁUserRepositoryǁlist__mutmut_23': xǁUserRepositoryǁlist__mutmut_23, 
        'xǁUserRepositoryǁlist__mutmut_24': xǁUserRepositoryǁlist__mutmut_24, 
        'xǁUserRepositoryǁlist__mutmut_25': xǁUserRepositoryǁlist__mutmut_25, 
        'xǁUserRepositoryǁlist__mutmut_26': xǁUserRepositoryǁlist__mutmut_26, 
        'xǁUserRepositoryǁlist__mutmut_27': xǁUserRepositoryǁlist__mutmut_27, 
        'xǁUserRepositoryǁlist__mutmut_28': xǁUserRepositoryǁlist__mutmut_28, 
        'xǁUserRepositoryǁlist__mutmut_29': xǁUserRepositoryǁlist__mutmut_29, 
        'xǁUserRepositoryǁlist__mutmut_30': xǁUserRepositoryǁlist__mutmut_30, 
        'xǁUserRepositoryǁlist__mutmut_31': xǁUserRepositoryǁlist__mutmut_31, 
        'xǁUserRepositoryǁlist__mutmut_32': xǁUserRepositoryǁlist__mutmut_32, 
        'xǁUserRepositoryǁlist__mutmut_33': xǁUserRepositoryǁlist__mutmut_33, 
        'xǁUserRepositoryǁlist__mutmut_34': xǁUserRepositoryǁlist__mutmut_34, 
        'xǁUserRepositoryǁlist__mutmut_35': xǁUserRepositoryǁlist__mutmut_35, 
        'xǁUserRepositoryǁlist__mutmut_36': xǁUserRepositoryǁlist__mutmut_36, 
        'xǁUserRepositoryǁlist__mutmut_37': xǁUserRepositoryǁlist__mutmut_37, 
        'xǁUserRepositoryǁlist__mutmut_38': xǁUserRepositoryǁlist__mutmut_38, 
        'xǁUserRepositoryǁlist__mutmut_39': xǁUserRepositoryǁlist__mutmut_39, 
        'xǁUserRepositoryǁlist__mutmut_40': xǁUserRepositoryǁlist__mutmut_40, 
        'xǁUserRepositoryǁlist__mutmut_41': xǁUserRepositoryǁlist__mutmut_41
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁUserRepositoryǁlist__mutmut_orig)
    xǁUserRepositoryǁlist__mutmut_orig.__name__ = 'xǁUserRepositoryǁlist'

    async def xǁUserRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(None)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = None
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            None,
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            None,
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=None,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_8(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_9(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_10(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"XX_idXX": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_11(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_ID": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_12(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(None)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_13(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"XX$setXX": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_14(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$SET": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_15(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return None
        return _document_to_user(result)

    async def xǁUserRepositoryǁupdate__mutmut_16(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        """Update user fields and return the updated instance."""
        if not data:
            return await self.get(entity_id)

        result = await self._collection.find_one_and_update(
            {"_id": ensure_object_id(entity_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        if not result:
            return None
        return _document_to_user(None)
    
    xǁUserRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁupdate__mutmut_1': xǁUserRepositoryǁupdate__mutmut_1, 
        'xǁUserRepositoryǁupdate__mutmut_2': xǁUserRepositoryǁupdate__mutmut_2, 
        'xǁUserRepositoryǁupdate__mutmut_3': xǁUserRepositoryǁupdate__mutmut_3, 
        'xǁUserRepositoryǁupdate__mutmut_4': xǁUserRepositoryǁupdate__mutmut_4, 
        'xǁUserRepositoryǁupdate__mutmut_5': xǁUserRepositoryǁupdate__mutmut_5, 
        'xǁUserRepositoryǁupdate__mutmut_6': xǁUserRepositoryǁupdate__mutmut_6, 
        'xǁUserRepositoryǁupdate__mutmut_7': xǁUserRepositoryǁupdate__mutmut_7, 
        'xǁUserRepositoryǁupdate__mutmut_8': xǁUserRepositoryǁupdate__mutmut_8, 
        'xǁUserRepositoryǁupdate__mutmut_9': xǁUserRepositoryǁupdate__mutmut_9, 
        'xǁUserRepositoryǁupdate__mutmut_10': xǁUserRepositoryǁupdate__mutmut_10, 
        'xǁUserRepositoryǁupdate__mutmut_11': xǁUserRepositoryǁupdate__mutmut_11, 
        'xǁUserRepositoryǁupdate__mutmut_12': xǁUserRepositoryǁupdate__mutmut_12, 
        'xǁUserRepositoryǁupdate__mutmut_13': xǁUserRepositoryǁupdate__mutmut_13, 
        'xǁUserRepositoryǁupdate__mutmut_14': xǁUserRepositoryǁupdate__mutmut_14, 
        'xǁUserRepositoryǁupdate__mutmut_15': xǁUserRepositoryǁupdate__mutmut_15, 
        'xǁUserRepositoryǁupdate__mutmut_16': xǁUserRepositoryǁupdate__mutmut_16
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁUserRepositoryǁupdate__mutmut_orig)
    xǁUserRepositoryǁupdate__mutmut_orig.__name__ = 'xǁUserRepositoryǁupdate'

    async def xǁUserRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁUserRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = None
        return outcome.deleted_count > 0

    async def xǁUserRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one(None)
        return outcome.deleted_count > 0

    async def xǁUserRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"XX_idXX": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁUserRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"_ID": ensure_object_id(entity_id)})
        return outcome.deleted_count > 0

    async def xǁUserRepositoryǁdelete__mutmut_5(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"_id": ensure_object_id(None)})
        return outcome.deleted_count > 0

    async def xǁUserRepositoryǁdelete__mutmut_6(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count >= 0

    async def xǁUserRepositoryǁdelete__mutmut_7(self, entity_id: str) -> bool:
        """Delete user by identifier."""
        outcome = await self._collection.delete_one({"_id": ensure_object_id(entity_id)})
        return outcome.deleted_count > 1
    
    xǁUserRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁdelete__mutmut_1': xǁUserRepositoryǁdelete__mutmut_1, 
        'xǁUserRepositoryǁdelete__mutmut_2': xǁUserRepositoryǁdelete__mutmut_2, 
        'xǁUserRepositoryǁdelete__mutmut_3': xǁUserRepositoryǁdelete__mutmut_3, 
        'xǁUserRepositoryǁdelete__mutmut_4': xǁUserRepositoryǁdelete__mutmut_4, 
        'xǁUserRepositoryǁdelete__mutmut_5': xǁUserRepositoryǁdelete__mutmut_5, 
        'xǁUserRepositoryǁdelete__mutmut_6': xǁUserRepositoryǁdelete__mutmut_6, 
        'xǁUserRepositoryǁdelete__mutmut_7': xǁUserRepositoryǁdelete__mutmut_7
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁUserRepositoryǁdelete__mutmut_orig)
    xǁUserRepositoryǁdelete__mutmut_orig.__name__ = 'xǁUserRepositoryǁdelete'

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_orig(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_1(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index(None, unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_2(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=None)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_3(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index(unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_4(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", )
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_5(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("XXemailXX", unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_6(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("EMAIL", unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_7(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=False)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_8(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index(None)
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_9(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index([("XXnameXX", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_10(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index([("NAME", ASCENDING)])
        self._indexes_ready = True

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_11(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = None

    async def xǁUserRepositoryǁ_ensure_indexes__mutmut_12(self) -> None:
        """Create indexes lazily (idempotent)."""
        if self._indexes_ready:
            return
        await self._collection.create_index("email", unique=True)
        await self._collection.create_index([("name", ASCENDING)])
        self._indexes_ready = False
    
    xǁUserRepositoryǁ_ensure_indexes__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserRepositoryǁ_ensure_indexes__mutmut_1': xǁUserRepositoryǁ_ensure_indexes__mutmut_1, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_2': xǁUserRepositoryǁ_ensure_indexes__mutmut_2, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_3': xǁUserRepositoryǁ_ensure_indexes__mutmut_3, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_4': xǁUserRepositoryǁ_ensure_indexes__mutmut_4, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_5': xǁUserRepositoryǁ_ensure_indexes__mutmut_5, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_6': xǁUserRepositoryǁ_ensure_indexes__mutmut_6, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_7': xǁUserRepositoryǁ_ensure_indexes__mutmut_7, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_8': xǁUserRepositoryǁ_ensure_indexes__mutmut_8, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_9': xǁUserRepositoryǁ_ensure_indexes__mutmut_9, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_10': xǁUserRepositoryǁ_ensure_indexes__mutmut_10, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_11': xǁUserRepositoryǁ_ensure_indexes__mutmut_11, 
        'xǁUserRepositoryǁ_ensure_indexes__mutmut_12': xǁUserRepositoryǁ_ensure_indexes__mutmut_12
    }
    
    def _ensure_indexes(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserRepositoryǁ_ensure_indexes__mutmut_orig"), object.__getattribute__(self, "xǁUserRepositoryǁ_ensure_indexes__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_indexes.__signature__ = _mutmut_signature(xǁUserRepositoryǁ_ensure_indexes__mutmut_orig)
    xǁUserRepositoryǁ_ensure_indexes__mutmut_orig.__name__ = 'xǁUserRepositoryǁ_ensure_indexes'


class InMemoryUserRepository(Repository[User, str]):
    """In-memory repository for testing purposes."""

    def xǁInMemoryUserRepositoryǁ__init____mutmut_orig(self) -> None:
        self._storage: Dict[str, User] = {}

    def xǁInMemoryUserRepositoryǁ__init____mutmut_1(self) -> None:
        self._storage: Dict[str, User] = None
    
    xǁInMemoryUserRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryUserRepositoryǁ__init____mutmut_1': xǁInMemoryUserRepositoryǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryUserRepositoryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁInMemoryUserRepositoryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁInMemoryUserRepositoryǁ__init____mutmut_orig)
    xǁInMemoryUserRepositoryǁ__init____mutmut_orig.__name__ = 'xǁInMemoryUserRepositoryǁ__init__'

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_orig(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_1(self, entity: User) -> User:
        if entity.id not in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_2(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                None,
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_3(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context=None,
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_4(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_5(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_6(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "XXUser with this id already existsXX",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_7(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "user with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_8(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "USER WITH THIS ID ALREADY EXISTS",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_9(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"XXidXX": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_10(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"ID": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_11(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(None):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_12(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email != entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_13(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                None,
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_14(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context=None,
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_15(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_16(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_17(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "XXUser with this email already existsXX",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_18(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "user with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_19(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "USER WITH THIS EMAIL ALREADY EXISTS",
                context={"email": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_20(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"XXemailXX": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_21(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"EMAIL": entity.email},
            )
        self._storage[entity.id] = entity
        return entity

    async def xǁInMemoryUserRepositoryǁcreate__mutmut_22(self, entity: User) -> User:
        if entity.id in self._storage:
            raise EntityAlreadyExistsError(
                "User with this id already exists",
                context={"id": entity.id},
            )
        if any(user.email == entity.email for user in self._storage.values()):
            raise EntityAlreadyExistsError(
                "User with this email already exists",
                context={"email": entity.email},
            )
        self._storage[entity.id] = None
        return entity
    
    xǁInMemoryUserRepositoryǁcreate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryUserRepositoryǁcreate__mutmut_1': xǁInMemoryUserRepositoryǁcreate__mutmut_1, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_2': xǁInMemoryUserRepositoryǁcreate__mutmut_2, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_3': xǁInMemoryUserRepositoryǁcreate__mutmut_3, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_4': xǁInMemoryUserRepositoryǁcreate__mutmut_4, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_5': xǁInMemoryUserRepositoryǁcreate__mutmut_5, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_6': xǁInMemoryUserRepositoryǁcreate__mutmut_6, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_7': xǁInMemoryUserRepositoryǁcreate__mutmut_7, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_8': xǁInMemoryUserRepositoryǁcreate__mutmut_8, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_9': xǁInMemoryUserRepositoryǁcreate__mutmut_9, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_10': xǁInMemoryUserRepositoryǁcreate__mutmut_10, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_11': xǁInMemoryUserRepositoryǁcreate__mutmut_11, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_12': xǁInMemoryUserRepositoryǁcreate__mutmut_12, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_13': xǁInMemoryUserRepositoryǁcreate__mutmut_13, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_14': xǁInMemoryUserRepositoryǁcreate__mutmut_14, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_15': xǁInMemoryUserRepositoryǁcreate__mutmut_15, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_16': xǁInMemoryUserRepositoryǁcreate__mutmut_16, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_17': xǁInMemoryUserRepositoryǁcreate__mutmut_17, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_18': xǁInMemoryUserRepositoryǁcreate__mutmut_18, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_19': xǁInMemoryUserRepositoryǁcreate__mutmut_19, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_20': xǁInMemoryUserRepositoryǁcreate__mutmut_20, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_21': xǁInMemoryUserRepositoryǁcreate__mutmut_21, 
        'xǁInMemoryUserRepositoryǁcreate__mutmut_22': xǁInMemoryUserRepositoryǁcreate__mutmut_22
    }
    
    def create(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryUserRepositoryǁcreate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryUserRepositoryǁcreate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create.__signature__ = _mutmut_signature(xǁInMemoryUserRepositoryǁcreate__mutmut_orig)
    xǁInMemoryUserRepositoryǁcreate__mutmut_orig.__name__ = 'xǁInMemoryUserRepositoryǁcreate'

    async def xǁInMemoryUserRepositoryǁget__mutmut_orig(self, entity_id: str) -> Optional[User]:
        return self._storage.get(entity_id)

    async def xǁInMemoryUserRepositoryǁget__mutmut_1(self, entity_id: str) -> Optional[User]:
        return self._storage.get(None)
    
    xǁInMemoryUserRepositoryǁget__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryUserRepositoryǁget__mutmut_1': xǁInMemoryUserRepositoryǁget__mutmut_1
    }
    
    def get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryUserRepositoryǁget__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryUserRepositoryǁget__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get.__signature__ = _mutmut_signature(xǁInMemoryUserRepositoryǁget__mutmut_orig)
    xǁInMemoryUserRepositoryǁget__mutmut_orig.__name__ = 'xǁInMemoryUserRepositoryǁget'

    async def xǁInMemoryUserRepositoryǁlist__mutmut_orig(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_1(self, **filters: object) -> Iterable[User]:
        users = None
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_2(self, **filters: object) -> Iterable[User]:
        users = list(None)
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_3(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = None
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_4(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get(None)
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_5(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("XXemailXX")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_6(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("EMAIL")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_7(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = None
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_8(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email != email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_9(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.upper()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_10(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = None
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_11(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get(None)
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_12(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("XXdefault_currencyXX")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_13(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("DEFAULT_CURRENCY")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_14(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = None
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_15(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency != currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_16(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = None
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_17(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get(None)
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_18(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("XXnameXX")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_19(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("NAME")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_20(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = None
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_21(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.upper()
            users = [user for user in users if term in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_22(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = None
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_23(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term not in user.name.lower()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_24(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.upper()]
        return list(users)

    async def xǁInMemoryUserRepositoryǁlist__mutmut_25(self, **filters: object) -> Iterable[User]:
        users = list(self._storage.values())
        email = filters.get("email")
        if isinstance(email, str):
            users = [user for user in users if user.email == email.lower()]
        currency = filters.get("default_currency")
        if isinstance(currency, str):
            users = [user for user in users if user.default_currency == currency]
        name = filters.get("name")
        if isinstance(name, str):
            term = name.lower()
            users = [user for user in users if term in user.name.lower()]
        return list(None)
    
    xǁInMemoryUserRepositoryǁlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryUserRepositoryǁlist__mutmut_1': xǁInMemoryUserRepositoryǁlist__mutmut_1, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_2': xǁInMemoryUserRepositoryǁlist__mutmut_2, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_3': xǁInMemoryUserRepositoryǁlist__mutmut_3, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_4': xǁInMemoryUserRepositoryǁlist__mutmut_4, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_5': xǁInMemoryUserRepositoryǁlist__mutmut_5, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_6': xǁInMemoryUserRepositoryǁlist__mutmut_6, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_7': xǁInMemoryUserRepositoryǁlist__mutmut_7, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_8': xǁInMemoryUserRepositoryǁlist__mutmut_8, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_9': xǁInMemoryUserRepositoryǁlist__mutmut_9, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_10': xǁInMemoryUserRepositoryǁlist__mutmut_10, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_11': xǁInMemoryUserRepositoryǁlist__mutmut_11, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_12': xǁInMemoryUserRepositoryǁlist__mutmut_12, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_13': xǁInMemoryUserRepositoryǁlist__mutmut_13, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_14': xǁInMemoryUserRepositoryǁlist__mutmut_14, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_15': xǁInMemoryUserRepositoryǁlist__mutmut_15, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_16': xǁInMemoryUserRepositoryǁlist__mutmut_16, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_17': xǁInMemoryUserRepositoryǁlist__mutmut_17, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_18': xǁInMemoryUserRepositoryǁlist__mutmut_18, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_19': xǁInMemoryUserRepositoryǁlist__mutmut_19, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_20': xǁInMemoryUserRepositoryǁlist__mutmut_20, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_21': xǁInMemoryUserRepositoryǁlist__mutmut_21, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_22': xǁInMemoryUserRepositoryǁlist__mutmut_22, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_23': xǁInMemoryUserRepositoryǁlist__mutmut_23, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_24': xǁInMemoryUserRepositoryǁlist__mutmut_24, 
        'xǁInMemoryUserRepositoryǁlist__mutmut_25': xǁInMemoryUserRepositoryǁlist__mutmut_25
    }
    
    def list(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryUserRepositoryǁlist__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryUserRepositoryǁlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list.__signature__ = _mutmut_signature(xǁInMemoryUserRepositoryǁlist__mutmut_orig)
    xǁInMemoryUserRepositoryǁlist__mutmut_orig.__name__ = 'xǁInMemoryUserRepositoryǁlist'

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_orig(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_1(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = None
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_2(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(None)
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_3(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_4(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if not user:
            return None
        updated_data = None
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_5(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(None)
        updated_user = User(**updated_data)
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_6(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = None
        self._storage[entity_id] = updated_user
        return updated_user

    async def xǁInMemoryUserRepositoryǁupdate__mutmut_7(self, entity_id: str, data: Dict[str, object]) -> Optional[User]:
        user = await self.get(entity_id)
        if not user:
            return None
        updated_data = user.model_dump()
        updated_data.update(data)
        updated_user = User(**updated_data)
        self._storage[entity_id] = None
        return updated_user
    
    xǁInMemoryUserRepositoryǁupdate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryUserRepositoryǁupdate__mutmut_1': xǁInMemoryUserRepositoryǁupdate__mutmut_1, 
        'xǁInMemoryUserRepositoryǁupdate__mutmut_2': xǁInMemoryUserRepositoryǁupdate__mutmut_2, 
        'xǁInMemoryUserRepositoryǁupdate__mutmut_3': xǁInMemoryUserRepositoryǁupdate__mutmut_3, 
        'xǁInMemoryUserRepositoryǁupdate__mutmut_4': xǁInMemoryUserRepositoryǁupdate__mutmut_4, 
        'xǁInMemoryUserRepositoryǁupdate__mutmut_5': xǁInMemoryUserRepositoryǁupdate__mutmut_5, 
        'xǁInMemoryUserRepositoryǁupdate__mutmut_6': xǁInMemoryUserRepositoryǁupdate__mutmut_6, 
        'xǁInMemoryUserRepositoryǁupdate__mutmut_7': xǁInMemoryUserRepositoryǁupdate__mutmut_7
    }
    
    def update(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryUserRepositoryǁupdate__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryUserRepositoryǁupdate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update.__signature__ = _mutmut_signature(xǁInMemoryUserRepositoryǁupdate__mutmut_orig)
    xǁInMemoryUserRepositoryǁupdate__mutmut_orig.__name__ = 'xǁInMemoryUserRepositoryǁupdate'

    async def xǁInMemoryUserRepositoryǁdelete__mutmut_orig(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is not None

    async def xǁInMemoryUserRepositoryǁdelete__mutmut_1(self, entity_id: str) -> bool:
        return self._storage.pop(None, None) is not None

    async def xǁInMemoryUserRepositoryǁdelete__mutmut_2(self, entity_id: str) -> bool:
        return self._storage.pop(None) is not None

    async def xǁInMemoryUserRepositoryǁdelete__mutmut_3(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, ) is not None

    async def xǁInMemoryUserRepositoryǁdelete__mutmut_4(self, entity_id: str) -> bool:
        return self._storage.pop(entity_id, None) is None
    
    xǁInMemoryUserRepositoryǁdelete__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁInMemoryUserRepositoryǁdelete__mutmut_1': xǁInMemoryUserRepositoryǁdelete__mutmut_1, 
        'xǁInMemoryUserRepositoryǁdelete__mutmut_2': xǁInMemoryUserRepositoryǁdelete__mutmut_2, 
        'xǁInMemoryUserRepositoryǁdelete__mutmut_3': xǁInMemoryUserRepositoryǁdelete__mutmut_3, 
        'xǁInMemoryUserRepositoryǁdelete__mutmut_4': xǁInMemoryUserRepositoryǁdelete__mutmut_4
    }
    
    def delete(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁInMemoryUserRepositoryǁdelete__mutmut_orig"), object.__getattribute__(self, "xǁInMemoryUserRepositoryǁdelete__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete.__signature__ = _mutmut_signature(xǁInMemoryUserRepositoryǁdelete__mutmut_orig)
    xǁInMemoryUserRepositoryǁdelete__mutmut_orig.__name__ = 'xǁInMemoryUserRepositoryǁdelete'


def x__user_to_document__mutmut_orig(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop("id", None)
    return data


def x__user_to_document__mutmut_1(user: User) -> Dict[str, object]:
    data = None
    data["_id"] = ensure_object_id(user.id)
    data.pop("id", None)
    return data


def x__user_to_document__mutmut_2(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = None
    data.pop("id", None)
    return data


def x__user_to_document__mutmut_3(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["XX_idXX"] = ensure_object_id(user.id)
    data.pop("id", None)
    return data


def x__user_to_document__mutmut_4(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_ID"] = ensure_object_id(user.id)
    data.pop("id", None)
    return data


def x__user_to_document__mutmut_5(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(None)
    data.pop("id", None)
    return data


def x__user_to_document__mutmut_6(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop(None, None)
    return data


def x__user_to_document__mutmut_7(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop(None)
    return data


def x__user_to_document__mutmut_8(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop("id", )
    return data


def x__user_to_document__mutmut_9(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop("XXidXX", None)
    return data


def x__user_to_document__mutmut_10(user: User) -> Dict[str, object]:
    data = user.model_dump()
    data["_id"] = ensure_object_id(user.id)
    data.pop("ID", None)
    return data

x__user_to_document__mutmut_mutants : ClassVar[MutantDict] = {
'x__user_to_document__mutmut_1': x__user_to_document__mutmut_1, 
    'x__user_to_document__mutmut_2': x__user_to_document__mutmut_2, 
    'x__user_to_document__mutmut_3': x__user_to_document__mutmut_3, 
    'x__user_to_document__mutmut_4': x__user_to_document__mutmut_4, 
    'x__user_to_document__mutmut_5': x__user_to_document__mutmut_5, 
    'x__user_to_document__mutmut_6': x__user_to_document__mutmut_6, 
    'x__user_to_document__mutmut_7': x__user_to_document__mutmut_7, 
    'x__user_to_document__mutmut_8': x__user_to_document__mutmut_8, 
    'x__user_to_document__mutmut_9': x__user_to_document__mutmut_9, 
    'x__user_to_document__mutmut_10': x__user_to_document__mutmut_10
}

def _user_to_document(*args, **kwargs):
    result = _mutmut_trampoline(x__user_to_document__mutmut_orig, x__user_to_document__mutmut_mutants, args, kwargs)
    return result 

_user_to_document.__signature__ = _mutmut_signature(x__user_to_document__mutmut_orig)
x__user_to_document__mutmut_orig.__name__ = 'x__user_to_document'


def x__document_to_user__mutmut_orig(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = str(document.pop("_id"))
    return User(**document)


def x__document_to_user__mutmut_1(document: Dict[str, object]) -> User:
    document = None
    document["id"] = str(document.pop("_id"))
    return User(**document)


def x__document_to_user__mutmut_2(document: Dict[str, object]) -> User:
    document = dict(None)
    document["id"] = str(document.pop("_id"))
    return User(**document)


def x__document_to_user__mutmut_3(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = None
    return User(**document)


def x__document_to_user__mutmut_4(document: Dict[str, object]) -> User:
    document = dict(document)
    document["XXidXX"] = str(document.pop("_id"))
    return User(**document)


def x__document_to_user__mutmut_5(document: Dict[str, object]) -> User:
    document = dict(document)
    document["ID"] = str(document.pop("_id"))
    return User(**document)


def x__document_to_user__mutmut_6(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = str(None)
    return User(**document)


def x__document_to_user__mutmut_7(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = str(document.pop(None))
    return User(**document)


def x__document_to_user__mutmut_8(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = str(document.pop("XX_idXX"))
    return User(**document)


def x__document_to_user__mutmut_9(document: Dict[str, object]) -> User:
    document = dict(document)
    document["id"] = str(document.pop("_ID"))
    return User(**document)

x__document_to_user__mutmut_mutants : ClassVar[MutantDict] = {
'x__document_to_user__mutmut_1': x__document_to_user__mutmut_1, 
    'x__document_to_user__mutmut_2': x__document_to_user__mutmut_2, 
    'x__document_to_user__mutmut_3': x__document_to_user__mutmut_3, 
    'x__document_to_user__mutmut_4': x__document_to_user__mutmut_4, 
    'x__document_to_user__mutmut_5': x__document_to_user__mutmut_5, 
    'x__document_to_user__mutmut_6': x__document_to_user__mutmut_6, 
    'x__document_to_user__mutmut_7': x__document_to_user__mutmut_7, 
    'x__document_to_user__mutmut_8': x__document_to_user__mutmut_8, 
    'x__document_to_user__mutmut_9': x__document_to_user__mutmut_9
}

def _document_to_user(*args, **kwargs):
    result = _mutmut_trampoline(x__document_to_user__mutmut_orig, x__document_to_user__mutmut_mutants, args, kwargs)
    return result 

_document_to_user.__signature__ = _mutmut_signature(x__document_to_user__mutmut_orig)
x__document_to_user__mutmut_orig.__name__ = 'x__document_to_user'
