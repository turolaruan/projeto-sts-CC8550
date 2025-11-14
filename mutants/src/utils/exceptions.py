"""Custom exception hierarchy for the application."""

from __future__ import annotations

from typing import Any
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


class AppException(Exception):
    """Base application exception carrying optional context."""

    def xǁAppExceptionǁ__init____mutmut_orig(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = context or {}

    def xǁAppExceptionǁ__init____mutmut_1(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        super().__init__(None)
        self.message = message
        self.context = context or {}

    def xǁAppExceptionǁ__init____mutmut_2(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = None
        self.context = context or {}

    def xǁAppExceptionǁ__init____mutmut_3(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = None

    def xǁAppExceptionǁ__init____mutmut_4(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.context = context and {}
    
    xǁAppExceptionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAppExceptionǁ__init____mutmut_1': xǁAppExceptionǁ__init____mutmut_1, 
        'xǁAppExceptionǁ__init____mutmut_2': xǁAppExceptionǁ__init____mutmut_2, 
        'xǁAppExceptionǁ__init____mutmut_3': xǁAppExceptionǁ__init____mutmut_3, 
        'xǁAppExceptionǁ__init____mutmut_4': xǁAppExceptionǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAppExceptionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAppExceptionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁAppExceptionǁ__init____mutmut_orig)
    xǁAppExceptionǁ__init____mutmut_orig.__name__ = 'xǁAppExceptionǁ__init__'


class EntityNotFoundError(AppException):
    """Raised when an entity is not found in the persistence layer."""


class EntityAlreadyExistsError(AppException):
    """Raised when attempting to create an entity that already exists."""


class ValidationAppError(AppException):
    """Raised for custom validation failures in services."""
