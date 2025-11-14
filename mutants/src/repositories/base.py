"""Repository base interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")
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


class Repository(Generic[T, ID], ABC):
    """Abstract base class for repositories."""

    @abstractmethod
    async def create(self, entity: T) -> T:
        """Persist a new entity."""

    @abstractmethod
    async def get(self, entity_id: ID) -> Optional[T]:
        """Retrieve entity by identifier."""

    @abstractmethod
    async def list(self, **filters: object) -> Iterable[T]:
        """Return iterable of entities matching filters."""

    @abstractmethod
    async def update(self, entity_id: ID, data: dict[str, object]) -> Optional[T]:
        """Update existing entity with provided data."""

    @abstractmethod
    async def delete(self, entity_id: ID) -> bool:
        """Delete entity by identifier and return success flag."""
