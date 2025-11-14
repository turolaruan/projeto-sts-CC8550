"""Router registration for FastAPI application."""

from fastapi import APIRouter, FastAPI

from src.controllers.accounts import router as accounts_router
from src.controllers.budgets import router as budgets_router
from src.controllers.categories import router as categories_router
from src.controllers.health import router as health_router
from src.controllers.reports import router as reports_router
from src.controllers.transactions import router as transactions_router
from src.controllers.users import router as users_router
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


def x_register_controllers__mutmut_orig(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_1(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = None
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_2(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix=None)
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_3(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="XX/apiXX")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_4(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/API")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_5(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(None)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_6(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(None)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_7(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(None)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_8(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(None)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_9(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(None)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_10(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(None)
    api_router.include_router(users_router)
    app.include_router(api_router)


def x_register_controllers__mutmut_11(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(None)
    app.include_router(api_router)


def x_register_controllers__mutmut_12(app: FastAPI) -> None:
    """Attach all routers to the FastAPI application."""
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    api_router.include_router(accounts_router)
    api_router.include_router(budgets_router)
    api_router.include_router(categories_router)
    api_router.include_router(reports_router)
    api_router.include_router(transactions_router)
    api_router.include_router(users_router)
    app.include_router(None)

x_register_controllers__mutmut_mutants : ClassVar[MutantDict] = {
'x_register_controllers__mutmut_1': x_register_controllers__mutmut_1, 
    'x_register_controllers__mutmut_2': x_register_controllers__mutmut_2, 
    'x_register_controllers__mutmut_3': x_register_controllers__mutmut_3, 
    'x_register_controllers__mutmut_4': x_register_controllers__mutmut_4, 
    'x_register_controllers__mutmut_5': x_register_controllers__mutmut_5, 
    'x_register_controllers__mutmut_6': x_register_controllers__mutmut_6, 
    'x_register_controllers__mutmut_7': x_register_controllers__mutmut_7, 
    'x_register_controllers__mutmut_8': x_register_controllers__mutmut_8, 
    'x_register_controllers__mutmut_9': x_register_controllers__mutmut_9, 
    'x_register_controllers__mutmut_10': x_register_controllers__mutmut_10, 
    'x_register_controllers__mutmut_11': x_register_controllers__mutmut_11, 
    'x_register_controllers__mutmut_12': x_register_controllers__mutmut_12
}

def register_controllers(*args, **kwargs):
    result = _mutmut_trampoline(x_register_controllers__mutmut_orig, x_register_controllers__mutmut_mutants, args, kwargs)
    return result 

register_controllers.__signature__ = _mutmut_signature(x_register_controllers__mutmut_orig)
x_register_controllers__mutmut_orig.__name__ = 'x_register_controllers'
