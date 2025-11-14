"""Service dependencies for FastAPI routes."""

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.database.dependencies import get_database
from src.repositories.account_repository import AccountRepository
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.services.account_service import AccountService
from src.services.budget_service import BudgetService
from src.services.category_service import CategoryService
from src.services.report_service import ReportService
from src.services.transaction_service import TransactionService
from src.services.user_service import UserService
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


def x_get_user_repository__mutmut_orig(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> UserRepository:
    """FastAPI dependency returning the user repository instance."""
    return UserRepository(db)


def x_get_user_repository__mutmut_1(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> UserRepository:
    """FastAPI dependency returning the user repository instance."""
    return UserRepository(None)

x_get_user_repository__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_user_repository__mutmut_1': x_get_user_repository__mutmut_1
}

def get_user_repository(*args, **kwargs):
    result = _mutmut_trampoline(x_get_user_repository__mutmut_orig, x_get_user_repository__mutmut_mutants, args, kwargs)
    return result 

get_user_repository.__signature__ = _mutmut_signature(x_get_user_repository__mutmut_orig)
x_get_user_repository__mutmut_orig.__name__ = 'x_get_user_repository'


def x_get_user_service__mutmut_orig(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    """FastAPI dependency returning the user service."""
    return UserService(repository)


def x_get_user_service__mutmut_1(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    """FastAPI dependency returning the user service."""
    return UserService(None)

x_get_user_service__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_user_service__mutmut_1': x_get_user_service__mutmut_1
}

def get_user_service(*args, **kwargs):
    result = _mutmut_trampoline(x_get_user_service__mutmut_orig, x_get_user_service__mutmut_mutants, args, kwargs)
    return result 

get_user_service.__signature__ = _mutmut_signature(x_get_user_service__mutmut_orig)
x_get_user_service__mutmut_orig.__name__ = 'x_get_user_service'


def x_get_account_repository__mutmut_orig(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> AccountRepository:
    """Return account repository."""
    return AccountRepository(db)


def x_get_account_repository__mutmut_1(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> AccountRepository:
    """Return account repository."""
    return AccountRepository(None)

x_get_account_repository__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_account_repository__mutmut_1': x_get_account_repository__mutmut_1
}

def get_account_repository(*args, **kwargs):
    result = _mutmut_trampoline(x_get_account_repository__mutmut_orig, x_get_account_repository__mutmut_mutants, args, kwargs)
    return result 

get_account_repository.__signature__ = _mutmut_signature(x_get_account_repository__mutmut_orig)
x_get_account_repository__mutmut_orig.__name__ = 'x_get_account_repository'


def x_get_transaction_repository__mutmut_orig(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> TransactionRepository:
    """Return transaction repository."""
    return TransactionRepository(db)


def x_get_transaction_repository__mutmut_1(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> TransactionRepository:
    """Return transaction repository."""
    return TransactionRepository(None)

x_get_transaction_repository__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_transaction_repository__mutmut_1': x_get_transaction_repository__mutmut_1
}

def get_transaction_repository(*args, **kwargs):
    result = _mutmut_trampoline(x_get_transaction_repository__mutmut_orig, x_get_transaction_repository__mutmut_mutants, args, kwargs)
    return result 

get_transaction_repository.__signature__ = _mutmut_signature(x_get_transaction_repository__mutmut_orig)
x_get_transaction_repository__mutmut_orig.__name__ = 'x_get_transaction_repository'


def x_get_account_service__mutmut_orig(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(repository, user_repository, transaction_repository)


def x_get_account_service__mutmut_1(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(None, user_repository, transaction_repository)


def x_get_account_service__mutmut_2(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(repository, None, transaction_repository)


def x_get_account_service__mutmut_3(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(repository, user_repository, None)


def x_get_account_service__mutmut_4(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(user_repository, transaction_repository)


def x_get_account_service__mutmut_5(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(repository, transaction_repository)


def x_get_account_service__mutmut_6(
    repository: AccountRepository = Depends(get_account_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> AccountService:
    """Return account service."""
    return AccountService(repository, user_repository, )

x_get_account_service__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_account_service__mutmut_1': x_get_account_service__mutmut_1, 
    'x_get_account_service__mutmut_2': x_get_account_service__mutmut_2, 
    'x_get_account_service__mutmut_3': x_get_account_service__mutmut_3, 
    'x_get_account_service__mutmut_4': x_get_account_service__mutmut_4, 
    'x_get_account_service__mutmut_5': x_get_account_service__mutmut_5, 
    'x_get_account_service__mutmut_6': x_get_account_service__mutmut_6
}

def get_account_service(*args, **kwargs):
    result = _mutmut_trampoline(x_get_account_service__mutmut_orig, x_get_account_service__mutmut_mutants, args, kwargs)
    return result 

get_account_service.__signature__ = _mutmut_signature(x_get_account_service__mutmut_orig)
x_get_account_service__mutmut_orig.__name__ = 'x_get_account_service'


def x_get_category_repository__mutmut_orig(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> CategoryRepository:
    """Return category repository."""
    return CategoryRepository(db)


def x_get_category_repository__mutmut_1(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> CategoryRepository:
    """Return category repository."""
    return CategoryRepository(None)

x_get_category_repository__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_category_repository__mutmut_1': x_get_category_repository__mutmut_1
}

def get_category_repository(*args, **kwargs):
    result = _mutmut_trampoline(x_get_category_repository__mutmut_orig, x_get_category_repository__mutmut_mutants, args, kwargs)
    return result 

get_category_repository.__signature__ = _mutmut_signature(x_get_category_repository__mutmut_orig)
x_get_category_repository__mutmut_orig.__name__ = 'x_get_category_repository'


def x_get_budget_repository__mutmut_orig(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> BudgetRepository:
    """Return budget repository."""
    return BudgetRepository(db)


def x_get_budget_repository__mutmut_1(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> BudgetRepository:
    """Return budget repository."""
    return BudgetRepository(None)

x_get_budget_repository__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_budget_repository__mutmut_1': x_get_budget_repository__mutmut_1
}

def get_budget_repository(*args, **kwargs):
    result = _mutmut_trampoline(x_get_budget_repository__mutmut_orig, x_get_budget_repository__mutmut_mutants, args, kwargs)
    return result 

get_budget_repository.__signature__ = _mutmut_signature(x_get_budget_repository__mutmut_orig)
x_get_budget_repository__mutmut_orig.__name__ = 'x_get_budget_repository'


def x_get_category_service__mutmut_orig(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        user_repository,
        transaction_repository,
        budget_repository,
    )


def x_get_category_service__mutmut_1(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        None,
        user_repository,
        transaction_repository,
        budget_repository,
    )


def x_get_category_service__mutmut_2(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        None,
        transaction_repository,
        budget_repository,
    )


def x_get_category_service__mutmut_3(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        user_repository,
        None,
        budget_repository,
    )


def x_get_category_service__mutmut_4(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        user_repository,
        transaction_repository,
        None,
    )


def x_get_category_service__mutmut_5(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        user_repository,
        transaction_repository,
        budget_repository,
    )


def x_get_category_service__mutmut_6(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        transaction_repository,
        budget_repository,
    )


def x_get_category_service__mutmut_7(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        user_repository,
        budget_repository,
    )


def x_get_category_service__mutmut_8(
    repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> CategoryService:
    """Return category service."""
    return CategoryService(
        repository,
        user_repository,
        transaction_repository,
        )

x_get_category_service__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_category_service__mutmut_1': x_get_category_service__mutmut_1, 
    'x_get_category_service__mutmut_2': x_get_category_service__mutmut_2, 
    'x_get_category_service__mutmut_3': x_get_category_service__mutmut_3, 
    'x_get_category_service__mutmut_4': x_get_category_service__mutmut_4, 
    'x_get_category_service__mutmut_5': x_get_category_service__mutmut_5, 
    'x_get_category_service__mutmut_6': x_get_category_service__mutmut_6, 
    'x_get_category_service__mutmut_7': x_get_category_service__mutmut_7, 
    'x_get_category_service__mutmut_8': x_get_category_service__mutmut_8
}

def get_category_service(*args, **kwargs):
    result = _mutmut_trampoline(x_get_category_service__mutmut_orig, x_get_category_service__mutmut_mutants, args, kwargs)
    return result 

get_category_service.__signature__ = _mutmut_signature(x_get_category_service__mutmut_orig)
x_get_category_service__mutmut_orig.__name__ = 'x_get_category_service'


def x_get_budget_service__mutmut_orig(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        user_repository,
        category_repository,
        transaction_repository,
    )


def x_get_budget_service__mutmut_1(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        None,
        user_repository,
        category_repository,
        transaction_repository,
    )


def x_get_budget_service__mutmut_2(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        None,
        category_repository,
        transaction_repository,
    )


def x_get_budget_service__mutmut_3(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        user_repository,
        None,
        transaction_repository,
    )


def x_get_budget_service__mutmut_4(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        user_repository,
        category_repository,
        None,
    )


def x_get_budget_service__mutmut_5(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        user_repository,
        category_repository,
        transaction_repository,
    )


def x_get_budget_service__mutmut_6(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        category_repository,
        transaction_repository,
    )


def x_get_budget_service__mutmut_7(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        user_repository,
        transaction_repository,
    )


def x_get_budget_service__mutmut_8(
    repository: BudgetRepository = Depends(get_budget_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
) -> BudgetService:
    """Return budget service."""
    return BudgetService(
        repository,
        user_repository,
        category_repository,
        )

x_get_budget_service__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_budget_service__mutmut_1': x_get_budget_service__mutmut_1, 
    'x_get_budget_service__mutmut_2': x_get_budget_service__mutmut_2, 
    'x_get_budget_service__mutmut_3': x_get_budget_service__mutmut_3, 
    'x_get_budget_service__mutmut_4': x_get_budget_service__mutmut_4, 
    'x_get_budget_service__mutmut_5': x_get_budget_service__mutmut_5, 
    'x_get_budget_service__mutmut_6': x_get_budget_service__mutmut_6, 
    'x_get_budget_service__mutmut_7': x_get_budget_service__mutmut_7, 
    'x_get_budget_service__mutmut_8': x_get_budget_service__mutmut_8
}

def get_budget_service(*args, **kwargs):
    result = _mutmut_trampoline(x_get_budget_service__mutmut_orig, x_get_budget_service__mutmut_mutants, args, kwargs)
    return result 

get_budget_service.__signature__ = _mutmut_signature(x_get_budget_service__mutmut_orig)
x_get_budget_service__mutmut_orig.__name__ = 'x_get_budget_service'


def x_get_transaction_service__mutmut_orig(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_1(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        None,
        account_service,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_2(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        None,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_3(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        None,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_4(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        None,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_5(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        None,
        budget_repository,
    )


def x_get_transaction_service__mutmut_6(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        user_repository,
        None,
    )


def x_get_transaction_service__mutmut_7(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        account_service,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_8(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_repository,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_9(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        category_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_10(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        user_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_11(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        budget_repository,
    )


def x_get_transaction_service__mutmut_12(
    repository: TransactionRepository = Depends(get_transaction_repository),
    account_service: AccountService = Depends(get_account_service),
    account_repository: AccountRepository = Depends(get_account_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    user_repository: UserRepository = Depends(get_user_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> TransactionService:
    """Return transaction service."""
    return TransactionService(
        repository,
        account_service,
        account_repository,
        category_repository,
        user_repository,
        )

x_get_transaction_service__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_transaction_service__mutmut_1': x_get_transaction_service__mutmut_1, 
    'x_get_transaction_service__mutmut_2': x_get_transaction_service__mutmut_2, 
    'x_get_transaction_service__mutmut_3': x_get_transaction_service__mutmut_3, 
    'x_get_transaction_service__mutmut_4': x_get_transaction_service__mutmut_4, 
    'x_get_transaction_service__mutmut_5': x_get_transaction_service__mutmut_5, 
    'x_get_transaction_service__mutmut_6': x_get_transaction_service__mutmut_6, 
    'x_get_transaction_service__mutmut_7': x_get_transaction_service__mutmut_7, 
    'x_get_transaction_service__mutmut_8': x_get_transaction_service__mutmut_8, 
    'x_get_transaction_service__mutmut_9': x_get_transaction_service__mutmut_9, 
    'x_get_transaction_service__mutmut_10': x_get_transaction_service__mutmut_10, 
    'x_get_transaction_service__mutmut_11': x_get_transaction_service__mutmut_11, 
    'x_get_transaction_service__mutmut_12': x_get_transaction_service__mutmut_12
}

def get_transaction_service(*args, **kwargs):
    result = _mutmut_trampoline(x_get_transaction_service__mutmut_orig, x_get_transaction_service__mutmut_mutants, args, kwargs)
    return result 

get_transaction_service.__signature__ = _mutmut_signature(x_get_transaction_service__mutmut_orig)
x_get_transaction_service__mutmut_orig.__name__ = 'x_get_transaction_service'


def x_get_report_service__mutmut_orig(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(transaction_repository, category_repository, budget_repository)


def x_get_report_service__mutmut_1(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(None, category_repository, budget_repository)


def x_get_report_service__mutmut_2(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(transaction_repository, None, budget_repository)


def x_get_report_service__mutmut_3(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(transaction_repository, category_repository, None)


def x_get_report_service__mutmut_4(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(category_repository, budget_repository)


def x_get_report_service__mutmut_5(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(transaction_repository, budget_repository)


def x_get_report_service__mutmut_6(
    transaction_repository: TransactionRepository = Depends(get_transaction_repository),
    category_repository: CategoryRepository = Depends(get_category_repository),
    budget_repository: BudgetRepository = Depends(get_budget_repository),
) -> ReportService:
    """Return report service."""
    return ReportService(transaction_repository, category_repository, )

x_get_report_service__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_report_service__mutmut_1': x_get_report_service__mutmut_1, 
    'x_get_report_service__mutmut_2': x_get_report_service__mutmut_2, 
    'x_get_report_service__mutmut_3': x_get_report_service__mutmut_3, 
    'x_get_report_service__mutmut_4': x_get_report_service__mutmut_4, 
    'x_get_report_service__mutmut_5': x_get_report_service__mutmut_5, 
    'x_get_report_service__mutmut_6': x_get_report_service__mutmut_6
}

def get_report_service(*args, **kwargs):
    result = _mutmut_trampoline(x_get_report_service__mutmut_orig, x_get_report_service__mutmut_mutants, args, kwargs)
    return result 

get_report_service.__signature__ = _mutmut_signature(x_get_report_service__mutmut_orig)
x_get_report_service__mutmut_orig.__name__ = 'x_get_report_service'
