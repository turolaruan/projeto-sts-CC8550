"""MongoDB connection management using Motor."""

from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config import Settings, get_settings
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


class MongoManager:
    """Manage lifecycle of the MongoDB client."""

    def xǁMongoManagerǁ__init____mutmut_orig(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()
        self._client: AsyncIOMotorClient | None = None

    def xǁMongoManagerǁ__init____mutmut_1(self, settings: Settings | None = None) -> None:
        self._settings = None
        self._client: AsyncIOMotorClient | None = None

    def xǁMongoManagerǁ__init____mutmut_2(self, settings: Settings | None = None) -> None:
        self._settings = settings and get_settings()
        self._client: AsyncIOMotorClient | None = None

    def xǁMongoManagerǁ__init____mutmut_3(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()
        self._client: AsyncIOMotorClient | None = ""
    
    xǁMongoManagerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMongoManagerǁ__init____mutmut_1': xǁMongoManagerǁ__init____mutmut_1, 
        'xǁMongoManagerǁ__init____mutmut_2': xǁMongoManagerǁ__init____mutmut_2, 
        'xǁMongoManagerǁ__init____mutmut_3': xǁMongoManagerǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMongoManagerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁMongoManagerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁMongoManagerǁ__init____mutmut_orig)
    xǁMongoManagerǁ__init____mutmut_orig.__name__ = 'xǁMongoManagerǁ__init__'

    async def xǁMongoManagerǁconnect__mutmut_orig(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="standard",
            )

    async def xǁMongoManagerǁconnect__mutmut_1(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is not None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="standard",
            )

    async def xǁMongoManagerǁconnect__mutmut_2(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = None

    async def xǁMongoManagerǁconnect__mutmut_3(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                None,
                uuidRepresentation="standard",
            )

    async def xǁMongoManagerǁconnect__mutmut_4(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation=None,
            )

    async def xǁMongoManagerǁconnect__mutmut_5(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                uuidRepresentation="standard",
            )

    async def xǁMongoManagerǁconnect__mutmut_6(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                )

    async def xǁMongoManagerǁconnect__mutmut_7(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="XXstandardXX",
            )

    async def xǁMongoManagerǁconnect__mutmut_8(self) -> None:
        """Establish connection with MongoDB if not already connected."""
        if self._client is None:
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="STANDARD",
            )
    
    xǁMongoManagerǁconnect__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMongoManagerǁconnect__mutmut_1': xǁMongoManagerǁconnect__mutmut_1, 
        'xǁMongoManagerǁconnect__mutmut_2': xǁMongoManagerǁconnect__mutmut_2, 
        'xǁMongoManagerǁconnect__mutmut_3': xǁMongoManagerǁconnect__mutmut_3, 
        'xǁMongoManagerǁconnect__mutmut_4': xǁMongoManagerǁconnect__mutmut_4, 
        'xǁMongoManagerǁconnect__mutmut_5': xǁMongoManagerǁconnect__mutmut_5, 
        'xǁMongoManagerǁconnect__mutmut_6': xǁMongoManagerǁconnect__mutmut_6, 
        'xǁMongoManagerǁconnect__mutmut_7': xǁMongoManagerǁconnect__mutmut_7, 
        'xǁMongoManagerǁconnect__mutmut_8': xǁMongoManagerǁconnect__mutmut_8
    }
    
    def connect(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMongoManagerǁconnect__mutmut_orig"), object.__getattribute__(self, "xǁMongoManagerǁconnect__mutmut_mutants"), args, kwargs, self)
        return result 
    
    connect.__signature__ = _mutmut_signature(xǁMongoManagerǁconnect__mutmut_orig)
    xǁMongoManagerǁconnect__mutmut_orig.__name__ = 'xǁMongoManagerǁconnect'

    async def xǁMongoManagerǁclose__mutmut_orig(self) -> None:
        """Gracefully close MongoDB connection."""
        if self._client is not None:
            self._client.close()
            self._client = None

    async def xǁMongoManagerǁclose__mutmut_1(self) -> None:
        """Gracefully close MongoDB connection."""
        if self._client is None:
            self._client.close()
            self._client = None

    async def xǁMongoManagerǁclose__mutmut_2(self) -> None:
        """Gracefully close MongoDB connection."""
        if self._client is not None:
            self._client.close()
            self._client = ""
    
    xǁMongoManagerǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMongoManagerǁclose__mutmut_1': xǁMongoManagerǁclose__mutmut_1, 
        'xǁMongoManagerǁclose__mutmut_2': xǁMongoManagerǁclose__mutmut_2
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMongoManagerǁclose__mutmut_orig"), object.__getattribute__(self, "xǁMongoManagerǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁMongoManagerǁclose__mutmut_orig)
    xǁMongoManagerǁclose__mutmut_orig.__name__ = 'xǁMongoManagerǁclose'

    @property
    def client(self) -> AsyncIOMotorClient:
        """Return the underlying Motor client, connecting if needed."""
        if self._client is None:
            # Ensure connection is established synchronously when needed.
            self._client = AsyncIOMotorClient(
                self._settings.mongodb_uri,
                uuidRepresentation="standard",
            )
        return self._client

    @property
    def database(self) -> AsyncIOMotorDatabase:
        """Return the configured database instance."""
        return self.client[self._settings.mongodb_db]


mongo_manager = MongoManager()
