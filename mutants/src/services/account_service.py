"""Business logic for managing accounts."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import List

from src.models.account import Account, AccountCreate, AccountUpdate, build_account
from src.models.common import now_utc
from src.repositories.account_repository import AccountRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.utils.exceptions import EntityNotFoundError, ValidationAppError
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


class AccountService:
    """Encapsulates account-related workflows."""

    def xǁAccountServiceǁ__init____mutmut_orig(
        self,
        repository: AccountRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository

    def xǁAccountServiceǁ__init____mutmut_1(
        self,
        repository: AccountRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = None
        self._user_repository = user_repository
        self._transaction_repository = transaction_repository

    def xǁAccountServiceǁ__init____mutmut_2(
        self,
        repository: AccountRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = None
        self._transaction_repository = transaction_repository

    def xǁAccountServiceǁ__init____mutmut_3(
        self,
        repository: AccountRepository,
        user_repository: UserRepository,
        transaction_repository: TransactionRepository,
    ) -> None:
        self._repository = repository
        self._user_repository = user_repository
        self._transaction_repository = None
    
    xǁAccountServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁ__init____mutmut_1': xǁAccountServiceǁ__init____mutmut_1, 
        'xǁAccountServiceǁ__init____mutmut_2': xǁAccountServiceǁ__init____mutmut_2, 
        'xǁAccountServiceǁ__init____mutmut_3': xǁAccountServiceǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁAccountServiceǁ__init____mutmut_orig)
    xǁAccountServiceǁ__init____mutmut_orig.__name__ = 'xǁAccountServiceǁ__init__'

    async def xǁAccountServiceǁcreate_account__mutmut_orig(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_1(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(None)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_2(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance <= payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_3(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                None,
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_4(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context=None,
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_5(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_6(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_7(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "XXStarting balance cannot be lower than minimum balanceXX",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_8(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_9(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "STARTING BALANCE CANNOT BE LOWER THAN MINIMUM BALANCE",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_10(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "XXstarting_balanceXX": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_11(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "STARTING_BALANCE": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_12(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(None),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_13(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "XXminimum_balanceXX": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_14(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "MINIMUM_BALANCE": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_15(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(None),
                },
            )
        account = build_account(payload)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_16(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = None
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_17(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(None)
        await self._repository.create(account)
        return account

    async def xǁAccountServiceǁcreate_account__mutmut_18(self, payload: AccountCreate) -> Account:
        """Create a new account ensuring user exists."""
        await self._ensure_user_exists(payload.user_id)
        if payload.starting_balance < payload.minimum_balance:
            raise ValidationAppError(
                "Starting balance cannot be lower than minimum balance",
                context={
                    "starting_balance": str(payload.starting_balance),
                    "minimum_balance": str(payload.minimum_balance),
                },
            )
        account = build_account(payload)
        await self._repository.create(None)
        return account
    
    xǁAccountServiceǁcreate_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁcreate_account__mutmut_1': xǁAccountServiceǁcreate_account__mutmut_1, 
        'xǁAccountServiceǁcreate_account__mutmut_2': xǁAccountServiceǁcreate_account__mutmut_2, 
        'xǁAccountServiceǁcreate_account__mutmut_3': xǁAccountServiceǁcreate_account__mutmut_3, 
        'xǁAccountServiceǁcreate_account__mutmut_4': xǁAccountServiceǁcreate_account__mutmut_4, 
        'xǁAccountServiceǁcreate_account__mutmut_5': xǁAccountServiceǁcreate_account__mutmut_5, 
        'xǁAccountServiceǁcreate_account__mutmut_6': xǁAccountServiceǁcreate_account__mutmut_6, 
        'xǁAccountServiceǁcreate_account__mutmut_7': xǁAccountServiceǁcreate_account__mutmut_7, 
        'xǁAccountServiceǁcreate_account__mutmut_8': xǁAccountServiceǁcreate_account__mutmut_8, 
        'xǁAccountServiceǁcreate_account__mutmut_9': xǁAccountServiceǁcreate_account__mutmut_9, 
        'xǁAccountServiceǁcreate_account__mutmut_10': xǁAccountServiceǁcreate_account__mutmut_10, 
        'xǁAccountServiceǁcreate_account__mutmut_11': xǁAccountServiceǁcreate_account__mutmut_11, 
        'xǁAccountServiceǁcreate_account__mutmut_12': xǁAccountServiceǁcreate_account__mutmut_12, 
        'xǁAccountServiceǁcreate_account__mutmut_13': xǁAccountServiceǁcreate_account__mutmut_13, 
        'xǁAccountServiceǁcreate_account__mutmut_14': xǁAccountServiceǁcreate_account__mutmut_14, 
        'xǁAccountServiceǁcreate_account__mutmut_15': xǁAccountServiceǁcreate_account__mutmut_15, 
        'xǁAccountServiceǁcreate_account__mutmut_16': xǁAccountServiceǁcreate_account__mutmut_16, 
        'xǁAccountServiceǁcreate_account__mutmut_17': xǁAccountServiceǁcreate_account__mutmut_17, 
        'xǁAccountServiceǁcreate_account__mutmut_18': xǁAccountServiceǁcreate_account__mutmut_18
    }
    
    def create_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁcreate_account__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁcreate_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_account.__signature__ = _mutmut_signature(xǁAccountServiceǁcreate_account__mutmut_orig)
    xǁAccountServiceǁcreate_account__mutmut_orig.__name__ = 'xǁAccountServiceǁcreate_account'

    async def xǁAccountServiceǁlist_accounts__mutmut_orig(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_1(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = None
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_2(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = None
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_3(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["XXuser_idXX"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_4(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["USER_ID"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_5(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = None
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_6(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["XXaccount_typeXX"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_7(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["ACCOUNT_TYPE"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_8(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = None
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_9(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["XXcurrencyXX"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_10(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["CURRENCY"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_11(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = None
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_12(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["XXnameXX"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_13(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["NAME"] = name
        accounts = await self._repository.list(**filters)
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_14(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = None
        return list(accounts)

    async def xǁAccountServiceǁlist_accounts__mutmut_15(
        self,
        *,
        user_id: str | None = None,
        account_type: str | None = None,
        currency: str | None = None,
        name: str | None = None,
    ) -> List[Account]:
        """Return accounts optionally filtered."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_type:
            filters["account_type"] = account_type
        if currency:
            filters["currency"] = currency
        if name:
            filters["name"] = name
        accounts = await self._repository.list(**filters)
        return list(None)
    
    xǁAccountServiceǁlist_accounts__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁlist_accounts__mutmut_1': xǁAccountServiceǁlist_accounts__mutmut_1, 
        'xǁAccountServiceǁlist_accounts__mutmut_2': xǁAccountServiceǁlist_accounts__mutmut_2, 
        'xǁAccountServiceǁlist_accounts__mutmut_3': xǁAccountServiceǁlist_accounts__mutmut_3, 
        'xǁAccountServiceǁlist_accounts__mutmut_4': xǁAccountServiceǁlist_accounts__mutmut_4, 
        'xǁAccountServiceǁlist_accounts__mutmut_5': xǁAccountServiceǁlist_accounts__mutmut_5, 
        'xǁAccountServiceǁlist_accounts__mutmut_6': xǁAccountServiceǁlist_accounts__mutmut_6, 
        'xǁAccountServiceǁlist_accounts__mutmut_7': xǁAccountServiceǁlist_accounts__mutmut_7, 
        'xǁAccountServiceǁlist_accounts__mutmut_8': xǁAccountServiceǁlist_accounts__mutmut_8, 
        'xǁAccountServiceǁlist_accounts__mutmut_9': xǁAccountServiceǁlist_accounts__mutmut_9, 
        'xǁAccountServiceǁlist_accounts__mutmut_10': xǁAccountServiceǁlist_accounts__mutmut_10, 
        'xǁAccountServiceǁlist_accounts__mutmut_11': xǁAccountServiceǁlist_accounts__mutmut_11, 
        'xǁAccountServiceǁlist_accounts__mutmut_12': xǁAccountServiceǁlist_accounts__mutmut_12, 
        'xǁAccountServiceǁlist_accounts__mutmut_13': xǁAccountServiceǁlist_accounts__mutmut_13, 
        'xǁAccountServiceǁlist_accounts__mutmut_14': xǁAccountServiceǁlist_accounts__mutmut_14, 
        'xǁAccountServiceǁlist_accounts__mutmut_15': xǁAccountServiceǁlist_accounts__mutmut_15
    }
    
    def list_accounts(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁlist_accounts__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁlist_accounts__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_accounts.__signature__ = _mutmut_signature(xǁAccountServiceǁlist_accounts__mutmut_orig)
    xǁAccountServiceǁlist_accounts__mutmut_orig.__name__ = 'xǁAccountServiceǁlist_accounts'

    async def xǁAccountServiceǁget_account__mutmut_orig(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_1(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = None
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_2(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(None)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_3(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is not None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_4(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError(None, context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_5(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context=None)
        return account

    async def xǁAccountServiceǁget_account__mutmut_6(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError(context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_7(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", )
        return account

    async def xǁAccountServiceǁget_account__mutmut_8(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("XXAccount not foundXX", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_9(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_10(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("ACCOUNT NOT FOUND", context={"id": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_11(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"XXidXX": account_id})
        return account

    async def xǁAccountServiceǁget_account__mutmut_12(self, account_id: str) -> Account:
        """Retrieve account by identifier."""
        account = await self._repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"ID": account_id})
        return account
    
    xǁAccountServiceǁget_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁget_account__mutmut_1': xǁAccountServiceǁget_account__mutmut_1, 
        'xǁAccountServiceǁget_account__mutmut_2': xǁAccountServiceǁget_account__mutmut_2, 
        'xǁAccountServiceǁget_account__mutmut_3': xǁAccountServiceǁget_account__mutmut_3, 
        'xǁAccountServiceǁget_account__mutmut_4': xǁAccountServiceǁget_account__mutmut_4, 
        'xǁAccountServiceǁget_account__mutmut_5': xǁAccountServiceǁget_account__mutmut_5, 
        'xǁAccountServiceǁget_account__mutmut_6': xǁAccountServiceǁget_account__mutmut_6, 
        'xǁAccountServiceǁget_account__mutmut_7': xǁAccountServiceǁget_account__mutmut_7, 
        'xǁAccountServiceǁget_account__mutmut_8': xǁAccountServiceǁget_account__mutmut_8, 
        'xǁAccountServiceǁget_account__mutmut_9': xǁAccountServiceǁget_account__mutmut_9, 
        'xǁAccountServiceǁget_account__mutmut_10': xǁAccountServiceǁget_account__mutmut_10, 
        'xǁAccountServiceǁget_account__mutmut_11': xǁAccountServiceǁget_account__mutmut_11, 
        'xǁAccountServiceǁget_account__mutmut_12': xǁAccountServiceǁget_account__mutmut_12
    }
    
    def get_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁget_account__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁget_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_account.__signature__ = _mutmut_signature(xǁAccountServiceǁget_account__mutmut_orig)
    xǁAccountServiceǁget_account__mutmut_orig.__name__ = 'xǁAccountServiceǁget_account'

    async def xǁAccountServiceǁupdate_account__mutmut_orig(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_1(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = None
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_2(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=None, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_3(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=None)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_4(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_5(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, )
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_6(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=False, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_7(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=False)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_8(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_9(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                None,
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_10(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context=None,
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_11(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_12(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_13(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "XXNo data provided to update accountXX",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_14(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "no data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_15(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "NO DATA PROVIDED TO UPDATE ACCOUNT",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_16(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"XXidXX": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_17(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"ID": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_18(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = None
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_19(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(None)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_20(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "XXminimum_balanceXX" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_21(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "MINIMUM_BALANCE" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_22(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" not in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_23(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = None
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_24(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["XXminimum_balanceXX"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_25(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["MINIMUM_BALANCE"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_26(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance <= new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_27(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    None,
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_28(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context=None,
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_29(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_30(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_31(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "XXCurrent balance is below the new minimum balanceXX",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_32(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_33(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "CURRENT BALANCE IS BELOW THE NEW MINIMUM BALANCE",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_34(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "XXbalanceXX": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_35(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "BALANCE": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_36(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(None),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_37(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "XXminimum_balanceXX": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_38(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "MINIMUM_BALANCE": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_39(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(None),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_40(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = None
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_41(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["XXupdated_atXX"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_42(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["UPDATED_AT"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_43(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = None
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_44(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(None, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_45(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, None)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_46(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_47(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, )
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_48(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is not None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_49(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError(None, context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_50(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context=None)
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_51(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError(context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_52(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", )
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_53(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("XXAccount not foundXX", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_54(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("account not found", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_55(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("ACCOUNT NOT FOUND", context={"id": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_56(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"XXidXX": account_id})
        return account

    async def xǁAccountServiceǁupdate_account__mutmut_57(self, account_id: str, payload: AccountUpdate) -> Account:
        """Update metadata of an account."""
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update account",
                context={"id": account_id},
            )
        current = await self.get_account(account_id)
        if "minimum_balance" in updates:
            new_min = updates["minimum_balance"]
            if current.balance < new_min:
                raise ValidationAppError(
                    "Current balance is below the new minimum balance",
                    context={
                        "balance": str(current.balance),
                        "minimum_balance": str(new_min),
                    },
                )
        updates["updated_at"] = now_utc()
        account = await self._repository.update(account_id, updates)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"ID": account_id})
        return account
    
    xǁAccountServiceǁupdate_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁupdate_account__mutmut_1': xǁAccountServiceǁupdate_account__mutmut_1, 
        'xǁAccountServiceǁupdate_account__mutmut_2': xǁAccountServiceǁupdate_account__mutmut_2, 
        'xǁAccountServiceǁupdate_account__mutmut_3': xǁAccountServiceǁupdate_account__mutmut_3, 
        'xǁAccountServiceǁupdate_account__mutmut_4': xǁAccountServiceǁupdate_account__mutmut_4, 
        'xǁAccountServiceǁupdate_account__mutmut_5': xǁAccountServiceǁupdate_account__mutmut_5, 
        'xǁAccountServiceǁupdate_account__mutmut_6': xǁAccountServiceǁupdate_account__mutmut_6, 
        'xǁAccountServiceǁupdate_account__mutmut_7': xǁAccountServiceǁupdate_account__mutmut_7, 
        'xǁAccountServiceǁupdate_account__mutmut_8': xǁAccountServiceǁupdate_account__mutmut_8, 
        'xǁAccountServiceǁupdate_account__mutmut_9': xǁAccountServiceǁupdate_account__mutmut_9, 
        'xǁAccountServiceǁupdate_account__mutmut_10': xǁAccountServiceǁupdate_account__mutmut_10, 
        'xǁAccountServiceǁupdate_account__mutmut_11': xǁAccountServiceǁupdate_account__mutmut_11, 
        'xǁAccountServiceǁupdate_account__mutmut_12': xǁAccountServiceǁupdate_account__mutmut_12, 
        'xǁAccountServiceǁupdate_account__mutmut_13': xǁAccountServiceǁupdate_account__mutmut_13, 
        'xǁAccountServiceǁupdate_account__mutmut_14': xǁAccountServiceǁupdate_account__mutmut_14, 
        'xǁAccountServiceǁupdate_account__mutmut_15': xǁAccountServiceǁupdate_account__mutmut_15, 
        'xǁAccountServiceǁupdate_account__mutmut_16': xǁAccountServiceǁupdate_account__mutmut_16, 
        'xǁAccountServiceǁupdate_account__mutmut_17': xǁAccountServiceǁupdate_account__mutmut_17, 
        'xǁAccountServiceǁupdate_account__mutmut_18': xǁAccountServiceǁupdate_account__mutmut_18, 
        'xǁAccountServiceǁupdate_account__mutmut_19': xǁAccountServiceǁupdate_account__mutmut_19, 
        'xǁAccountServiceǁupdate_account__mutmut_20': xǁAccountServiceǁupdate_account__mutmut_20, 
        'xǁAccountServiceǁupdate_account__mutmut_21': xǁAccountServiceǁupdate_account__mutmut_21, 
        'xǁAccountServiceǁupdate_account__mutmut_22': xǁAccountServiceǁupdate_account__mutmut_22, 
        'xǁAccountServiceǁupdate_account__mutmut_23': xǁAccountServiceǁupdate_account__mutmut_23, 
        'xǁAccountServiceǁupdate_account__mutmut_24': xǁAccountServiceǁupdate_account__mutmut_24, 
        'xǁAccountServiceǁupdate_account__mutmut_25': xǁAccountServiceǁupdate_account__mutmut_25, 
        'xǁAccountServiceǁupdate_account__mutmut_26': xǁAccountServiceǁupdate_account__mutmut_26, 
        'xǁAccountServiceǁupdate_account__mutmut_27': xǁAccountServiceǁupdate_account__mutmut_27, 
        'xǁAccountServiceǁupdate_account__mutmut_28': xǁAccountServiceǁupdate_account__mutmut_28, 
        'xǁAccountServiceǁupdate_account__mutmut_29': xǁAccountServiceǁupdate_account__mutmut_29, 
        'xǁAccountServiceǁupdate_account__mutmut_30': xǁAccountServiceǁupdate_account__mutmut_30, 
        'xǁAccountServiceǁupdate_account__mutmut_31': xǁAccountServiceǁupdate_account__mutmut_31, 
        'xǁAccountServiceǁupdate_account__mutmut_32': xǁAccountServiceǁupdate_account__mutmut_32, 
        'xǁAccountServiceǁupdate_account__mutmut_33': xǁAccountServiceǁupdate_account__mutmut_33, 
        'xǁAccountServiceǁupdate_account__mutmut_34': xǁAccountServiceǁupdate_account__mutmut_34, 
        'xǁAccountServiceǁupdate_account__mutmut_35': xǁAccountServiceǁupdate_account__mutmut_35, 
        'xǁAccountServiceǁupdate_account__mutmut_36': xǁAccountServiceǁupdate_account__mutmut_36, 
        'xǁAccountServiceǁupdate_account__mutmut_37': xǁAccountServiceǁupdate_account__mutmut_37, 
        'xǁAccountServiceǁupdate_account__mutmut_38': xǁAccountServiceǁupdate_account__mutmut_38, 
        'xǁAccountServiceǁupdate_account__mutmut_39': xǁAccountServiceǁupdate_account__mutmut_39, 
        'xǁAccountServiceǁupdate_account__mutmut_40': xǁAccountServiceǁupdate_account__mutmut_40, 
        'xǁAccountServiceǁupdate_account__mutmut_41': xǁAccountServiceǁupdate_account__mutmut_41, 
        'xǁAccountServiceǁupdate_account__mutmut_42': xǁAccountServiceǁupdate_account__mutmut_42, 
        'xǁAccountServiceǁupdate_account__mutmut_43': xǁAccountServiceǁupdate_account__mutmut_43, 
        'xǁAccountServiceǁupdate_account__mutmut_44': xǁAccountServiceǁupdate_account__mutmut_44, 
        'xǁAccountServiceǁupdate_account__mutmut_45': xǁAccountServiceǁupdate_account__mutmut_45, 
        'xǁAccountServiceǁupdate_account__mutmut_46': xǁAccountServiceǁupdate_account__mutmut_46, 
        'xǁAccountServiceǁupdate_account__mutmut_47': xǁAccountServiceǁupdate_account__mutmut_47, 
        'xǁAccountServiceǁupdate_account__mutmut_48': xǁAccountServiceǁupdate_account__mutmut_48, 
        'xǁAccountServiceǁupdate_account__mutmut_49': xǁAccountServiceǁupdate_account__mutmut_49, 
        'xǁAccountServiceǁupdate_account__mutmut_50': xǁAccountServiceǁupdate_account__mutmut_50, 
        'xǁAccountServiceǁupdate_account__mutmut_51': xǁAccountServiceǁupdate_account__mutmut_51, 
        'xǁAccountServiceǁupdate_account__mutmut_52': xǁAccountServiceǁupdate_account__mutmut_52, 
        'xǁAccountServiceǁupdate_account__mutmut_53': xǁAccountServiceǁupdate_account__mutmut_53, 
        'xǁAccountServiceǁupdate_account__mutmut_54': xǁAccountServiceǁupdate_account__mutmut_54, 
        'xǁAccountServiceǁupdate_account__mutmut_55': xǁAccountServiceǁupdate_account__mutmut_55, 
        'xǁAccountServiceǁupdate_account__mutmut_56': xǁAccountServiceǁupdate_account__mutmut_56, 
        'xǁAccountServiceǁupdate_account__mutmut_57': xǁAccountServiceǁupdate_account__mutmut_57
    }
    
    def update_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁupdate_account__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁupdate_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_account.__signature__ = _mutmut_signature(xǁAccountServiceǁupdate_account__mutmut_orig)
    xǁAccountServiceǁupdate_account__mutmut_orig.__name__ = 'xǁAccountServiceǁupdate_account'

    async def xǁAccountServiceǁdelete_account__mutmut_orig(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_1(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = None
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_2(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(None)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_3(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                None,
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_4(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context=None,
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_5(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_6(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_7(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "XXAccount has related transactions and cannot be deletedXX",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_8(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_9(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "ACCOUNT HAS RELATED TRANSACTIONS AND CANNOT BE DELETED",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_10(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"XXidXX": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_11(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"ID": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_12(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = None
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_13(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(None)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_14(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if deleted:
            raise EntityNotFoundError("Account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_15(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError(None, context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_16(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context=None)

    async def xǁAccountServiceǁdelete_account__mutmut_17(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError(context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_18(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", )

    async def xǁAccountServiceǁdelete_account__mutmut_19(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("XXAccount not foundXX", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_20(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("account not found", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_21(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("ACCOUNT NOT FOUND", context={"id": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_22(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"XXidXX": account_id})

    async def xǁAccountServiceǁdelete_account__mutmut_23(self, account_id: str) -> None:
        """Delete an account ensuring it exists."""
        has_transactions = await self._transaction_repository.exists_for_account(account_id)
        if has_transactions:
            raise ValidationAppError(
                "Account has related transactions and cannot be deleted",
                context={"id": account_id},
            )
        deleted = await self._repository.delete(account_id)
        if not deleted:
            raise EntityNotFoundError("Account not found", context={"ID": account_id})
    
    xǁAccountServiceǁdelete_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁdelete_account__mutmut_1': xǁAccountServiceǁdelete_account__mutmut_1, 
        'xǁAccountServiceǁdelete_account__mutmut_2': xǁAccountServiceǁdelete_account__mutmut_2, 
        'xǁAccountServiceǁdelete_account__mutmut_3': xǁAccountServiceǁdelete_account__mutmut_3, 
        'xǁAccountServiceǁdelete_account__mutmut_4': xǁAccountServiceǁdelete_account__mutmut_4, 
        'xǁAccountServiceǁdelete_account__mutmut_5': xǁAccountServiceǁdelete_account__mutmut_5, 
        'xǁAccountServiceǁdelete_account__mutmut_6': xǁAccountServiceǁdelete_account__mutmut_6, 
        'xǁAccountServiceǁdelete_account__mutmut_7': xǁAccountServiceǁdelete_account__mutmut_7, 
        'xǁAccountServiceǁdelete_account__mutmut_8': xǁAccountServiceǁdelete_account__mutmut_8, 
        'xǁAccountServiceǁdelete_account__mutmut_9': xǁAccountServiceǁdelete_account__mutmut_9, 
        'xǁAccountServiceǁdelete_account__mutmut_10': xǁAccountServiceǁdelete_account__mutmut_10, 
        'xǁAccountServiceǁdelete_account__mutmut_11': xǁAccountServiceǁdelete_account__mutmut_11, 
        'xǁAccountServiceǁdelete_account__mutmut_12': xǁAccountServiceǁdelete_account__mutmut_12, 
        'xǁAccountServiceǁdelete_account__mutmut_13': xǁAccountServiceǁdelete_account__mutmut_13, 
        'xǁAccountServiceǁdelete_account__mutmut_14': xǁAccountServiceǁdelete_account__mutmut_14, 
        'xǁAccountServiceǁdelete_account__mutmut_15': xǁAccountServiceǁdelete_account__mutmut_15, 
        'xǁAccountServiceǁdelete_account__mutmut_16': xǁAccountServiceǁdelete_account__mutmut_16, 
        'xǁAccountServiceǁdelete_account__mutmut_17': xǁAccountServiceǁdelete_account__mutmut_17, 
        'xǁAccountServiceǁdelete_account__mutmut_18': xǁAccountServiceǁdelete_account__mutmut_18, 
        'xǁAccountServiceǁdelete_account__mutmut_19': xǁAccountServiceǁdelete_account__mutmut_19, 
        'xǁAccountServiceǁdelete_account__mutmut_20': xǁAccountServiceǁdelete_account__mutmut_20, 
        'xǁAccountServiceǁdelete_account__mutmut_21': xǁAccountServiceǁdelete_account__mutmut_21, 
        'xǁAccountServiceǁdelete_account__mutmut_22': xǁAccountServiceǁdelete_account__mutmut_22, 
        'xǁAccountServiceǁdelete_account__mutmut_23': xǁAccountServiceǁdelete_account__mutmut_23
    }
    
    def delete_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁdelete_account__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁdelete_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete_account.__signature__ = _mutmut_signature(xǁAccountServiceǁdelete_account__mutmut_orig)
    xǁAccountServiceǁdelete_account__mutmut_orig.__name__ = 'xǁAccountServiceǁdelete_account'

    async def xǁAccountServiceǁadjust_balance__mutmut_orig(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_1(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = None
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_2(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(None)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_3(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = None
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_4(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            None, rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_5(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=None
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_6(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_7(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_8(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance - delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_9(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal(None), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_10(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("XX0.01XX"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_11(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance <= account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_12(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                None,
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_13(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context=None,
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_14(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_15(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_16(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "XXOperation would drop balance below the allowed minimumXX",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_17(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_18(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "OPERATION WOULD DROP BALANCE BELOW THE ALLOWED MINIMUM",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_19(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "XXminimum_balanceXX": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_20(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "MINIMUM_BALANCE": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_21(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(None),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_22(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "XXrequested_balanceXX": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_23(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "REQUESTED_BALANCE": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_24(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(None),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_25(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = None
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_26(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            None,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_27(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            None,
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_28(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_29(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_30(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"XXbalanceXX": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_31(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"BALANCE": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_32(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "XXupdated_atXX": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_33(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "UPDATED_AT": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_34(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is not None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_35(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError(None, context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_36(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context=None)
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_37(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError(context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_38(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", )
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_39(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("XXAccount not foundXX", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_40(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_41(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("ACCOUNT NOT FOUND", context={"id": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_42(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"XXidXX": account_id})
        return result

    async def xǁAccountServiceǁadjust_balance__mutmut_43(self, account_id: str, delta: Decimal) -> Account:
        """Adjust account balance by delta value."""
        account = await self.get_account(account_id)
        new_balance = (account.balance + delta).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Operation would drop balance below the allowed minimum",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"ID": account_id})
        return result
    
    xǁAccountServiceǁadjust_balance__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁadjust_balance__mutmut_1': xǁAccountServiceǁadjust_balance__mutmut_1, 
        'xǁAccountServiceǁadjust_balance__mutmut_2': xǁAccountServiceǁadjust_balance__mutmut_2, 
        'xǁAccountServiceǁadjust_balance__mutmut_3': xǁAccountServiceǁadjust_balance__mutmut_3, 
        'xǁAccountServiceǁadjust_balance__mutmut_4': xǁAccountServiceǁadjust_balance__mutmut_4, 
        'xǁAccountServiceǁadjust_balance__mutmut_5': xǁAccountServiceǁadjust_balance__mutmut_5, 
        'xǁAccountServiceǁadjust_balance__mutmut_6': xǁAccountServiceǁadjust_balance__mutmut_6, 
        'xǁAccountServiceǁadjust_balance__mutmut_7': xǁAccountServiceǁadjust_balance__mutmut_7, 
        'xǁAccountServiceǁadjust_balance__mutmut_8': xǁAccountServiceǁadjust_balance__mutmut_8, 
        'xǁAccountServiceǁadjust_balance__mutmut_9': xǁAccountServiceǁadjust_balance__mutmut_9, 
        'xǁAccountServiceǁadjust_balance__mutmut_10': xǁAccountServiceǁadjust_balance__mutmut_10, 
        'xǁAccountServiceǁadjust_balance__mutmut_11': xǁAccountServiceǁadjust_balance__mutmut_11, 
        'xǁAccountServiceǁadjust_balance__mutmut_12': xǁAccountServiceǁadjust_balance__mutmut_12, 
        'xǁAccountServiceǁadjust_balance__mutmut_13': xǁAccountServiceǁadjust_balance__mutmut_13, 
        'xǁAccountServiceǁadjust_balance__mutmut_14': xǁAccountServiceǁadjust_balance__mutmut_14, 
        'xǁAccountServiceǁadjust_balance__mutmut_15': xǁAccountServiceǁadjust_balance__mutmut_15, 
        'xǁAccountServiceǁadjust_balance__mutmut_16': xǁAccountServiceǁadjust_balance__mutmut_16, 
        'xǁAccountServiceǁadjust_balance__mutmut_17': xǁAccountServiceǁadjust_balance__mutmut_17, 
        'xǁAccountServiceǁadjust_balance__mutmut_18': xǁAccountServiceǁadjust_balance__mutmut_18, 
        'xǁAccountServiceǁadjust_balance__mutmut_19': xǁAccountServiceǁadjust_balance__mutmut_19, 
        'xǁAccountServiceǁadjust_balance__mutmut_20': xǁAccountServiceǁadjust_balance__mutmut_20, 
        'xǁAccountServiceǁadjust_balance__mutmut_21': xǁAccountServiceǁadjust_balance__mutmut_21, 
        'xǁAccountServiceǁadjust_balance__mutmut_22': xǁAccountServiceǁadjust_balance__mutmut_22, 
        'xǁAccountServiceǁadjust_balance__mutmut_23': xǁAccountServiceǁadjust_balance__mutmut_23, 
        'xǁAccountServiceǁadjust_balance__mutmut_24': xǁAccountServiceǁadjust_balance__mutmut_24, 
        'xǁAccountServiceǁadjust_balance__mutmut_25': xǁAccountServiceǁadjust_balance__mutmut_25, 
        'xǁAccountServiceǁadjust_balance__mutmut_26': xǁAccountServiceǁadjust_balance__mutmut_26, 
        'xǁAccountServiceǁadjust_balance__mutmut_27': xǁAccountServiceǁadjust_balance__mutmut_27, 
        'xǁAccountServiceǁadjust_balance__mutmut_28': xǁAccountServiceǁadjust_balance__mutmut_28, 
        'xǁAccountServiceǁadjust_balance__mutmut_29': xǁAccountServiceǁadjust_balance__mutmut_29, 
        'xǁAccountServiceǁadjust_balance__mutmut_30': xǁAccountServiceǁadjust_balance__mutmut_30, 
        'xǁAccountServiceǁadjust_balance__mutmut_31': xǁAccountServiceǁadjust_balance__mutmut_31, 
        'xǁAccountServiceǁadjust_balance__mutmut_32': xǁAccountServiceǁadjust_balance__mutmut_32, 
        'xǁAccountServiceǁadjust_balance__mutmut_33': xǁAccountServiceǁadjust_balance__mutmut_33, 
        'xǁAccountServiceǁadjust_balance__mutmut_34': xǁAccountServiceǁadjust_balance__mutmut_34, 
        'xǁAccountServiceǁadjust_balance__mutmut_35': xǁAccountServiceǁadjust_balance__mutmut_35, 
        'xǁAccountServiceǁadjust_balance__mutmut_36': xǁAccountServiceǁadjust_balance__mutmut_36, 
        'xǁAccountServiceǁadjust_balance__mutmut_37': xǁAccountServiceǁadjust_balance__mutmut_37, 
        'xǁAccountServiceǁadjust_balance__mutmut_38': xǁAccountServiceǁadjust_balance__mutmut_38, 
        'xǁAccountServiceǁadjust_balance__mutmut_39': xǁAccountServiceǁadjust_balance__mutmut_39, 
        'xǁAccountServiceǁadjust_balance__mutmut_40': xǁAccountServiceǁadjust_balance__mutmut_40, 
        'xǁAccountServiceǁadjust_balance__mutmut_41': xǁAccountServiceǁadjust_balance__mutmut_41, 
        'xǁAccountServiceǁadjust_balance__mutmut_42': xǁAccountServiceǁadjust_balance__mutmut_42, 
        'xǁAccountServiceǁadjust_balance__mutmut_43': xǁAccountServiceǁadjust_balance__mutmut_43
    }
    
    def adjust_balance(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁadjust_balance__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁadjust_balance__mutmut_mutants"), args, kwargs, self)
        return result 
    
    adjust_balance.__signature__ = _mutmut_signature(xǁAccountServiceǁadjust_balance__mutmut_orig)
    xǁAccountServiceǁadjust_balance__mutmut_orig.__name__ = 'xǁAccountServiceǁadjust_balance'

    async def xǁAccountServiceǁset_balance__mutmut_orig(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_1(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = None
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_2(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(None, rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_3(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=None)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_4(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_5(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), )
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_6(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal(None), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_7(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("XX0.01XX"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_8(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = None
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_9(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(None)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_10(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance <= account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_11(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                None,
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_12(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context=None,
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_13(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_14(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_15(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "XXBalance cannot be set below the minimum thresholdXX",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_16(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_17(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "BALANCE CANNOT BE SET BELOW THE MINIMUM THRESHOLD",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_18(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "XXminimum_balanceXX": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_19(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "MINIMUM_BALANCE": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_20(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(None),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_21(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "XXrequested_balanceXX": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_22(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "REQUESTED_BALANCE": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_23(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(None),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_24(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = None
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_25(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            None,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_26(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            None,
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_27(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_28(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_29(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"XXbalanceXX": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_30(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"BALANCE": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_31(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "XXupdated_atXX": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_32(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "UPDATED_AT": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_33(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is not None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_34(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError(None, context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_35(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context=None)
        return result

    async def xǁAccountServiceǁset_balance__mutmut_36(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError(context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_37(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", )
        return result

    async def xǁAccountServiceǁset_balance__mutmut_38(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("XXAccount not foundXX", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_39(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("account not found", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_40(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("ACCOUNT NOT FOUND", context={"id": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_41(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"XXidXX": account_id})
        return result

    async def xǁAccountServiceǁset_balance__mutmut_42(self, account_id: str, balance: Decimal) -> Account:
        """Overwrite account balance with provided value."""
        new_balance = balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        account = await self.get_account(account_id)
        if new_balance < account.minimum_balance:
            raise ValidationAppError(
                "Balance cannot be set below the minimum threshold",
                context={
                    "minimum_balance": str(account.minimum_balance),
                    "requested_balance": str(new_balance),
                },
            )
        result = await self._repository.update(
            account_id,
            {"balance": new_balance, "updated_at": now_utc()},
        )
        if result is None:
            raise EntityNotFoundError("Account not found", context={"ID": account_id})
        return result
    
    xǁAccountServiceǁset_balance__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁset_balance__mutmut_1': xǁAccountServiceǁset_balance__mutmut_1, 
        'xǁAccountServiceǁset_balance__mutmut_2': xǁAccountServiceǁset_balance__mutmut_2, 
        'xǁAccountServiceǁset_balance__mutmut_3': xǁAccountServiceǁset_balance__mutmut_3, 
        'xǁAccountServiceǁset_balance__mutmut_4': xǁAccountServiceǁset_balance__mutmut_4, 
        'xǁAccountServiceǁset_balance__mutmut_5': xǁAccountServiceǁset_balance__mutmut_5, 
        'xǁAccountServiceǁset_balance__mutmut_6': xǁAccountServiceǁset_balance__mutmut_6, 
        'xǁAccountServiceǁset_balance__mutmut_7': xǁAccountServiceǁset_balance__mutmut_7, 
        'xǁAccountServiceǁset_balance__mutmut_8': xǁAccountServiceǁset_balance__mutmut_8, 
        'xǁAccountServiceǁset_balance__mutmut_9': xǁAccountServiceǁset_balance__mutmut_9, 
        'xǁAccountServiceǁset_balance__mutmut_10': xǁAccountServiceǁset_balance__mutmut_10, 
        'xǁAccountServiceǁset_balance__mutmut_11': xǁAccountServiceǁset_balance__mutmut_11, 
        'xǁAccountServiceǁset_balance__mutmut_12': xǁAccountServiceǁset_balance__mutmut_12, 
        'xǁAccountServiceǁset_balance__mutmut_13': xǁAccountServiceǁset_balance__mutmut_13, 
        'xǁAccountServiceǁset_balance__mutmut_14': xǁAccountServiceǁset_balance__mutmut_14, 
        'xǁAccountServiceǁset_balance__mutmut_15': xǁAccountServiceǁset_balance__mutmut_15, 
        'xǁAccountServiceǁset_balance__mutmut_16': xǁAccountServiceǁset_balance__mutmut_16, 
        'xǁAccountServiceǁset_balance__mutmut_17': xǁAccountServiceǁset_balance__mutmut_17, 
        'xǁAccountServiceǁset_balance__mutmut_18': xǁAccountServiceǁset_balance__mutmut_18, 
        'xǁAccountServiceǁset_balance__mutmut_19': xǁAccountServiceǁset_balance__mutmut_19, 
        'xǁAccountServiceǁset_balance__mutmut_20': xǁAccountServiceǁset_balance__mutmut_20, 
        'xǁAccountServiceǁset_balance__mutmut_21': xǁAccountServiceǁset_balance__mutmut_21, 
        'xǁAccountServiceǁset_balance__mutmut_22': xǁAccountServiceǁset_balance__mutmut_22, 
        'xǁAccountServiceǁset_balance__mutmut_23': xǁAccountServiceǁset_balance__mutmut_23, 
        'xǁAccountServiceǁset_balance__mutmut_24': xǁAccountServiceǁset_balance__mutmut_24, 
        'xǁAccountServiceǁset_balance__mutmut_25': xǁAccountServiceǁset_balance__mutmut_25, 
        'xǁAccountServiceǁset_balance__mutmut_26': xǁAccountServiceǁset_balance__mutmut_26, 
        'xǁAccountServiceǁset_balance__mutmut_27': xǁAccountServiceǁset_balance__mutmut_27, 
        'xǁAccountServiceǁset_balance__mutmut_28': xǁAccountServiceǁset_balance__mutmut_28, 
        'xǁAccountServiceǁset_balance__mutmut_29': xǁAccountServiceǁset_balance__mutmut_29, 
        'xǁAccountServiceǁset_balance__mutmut_30': xǁAccountServiceǁset_balance__mutmut_30, 
        'xǁAccountServiceǁset_balance__mutmut_31': xǁAccountServiceǁset_balance__mutmut_31, 
        'xǁAccountServiceǁset_balance__mutmut_32': xǁAccountServiceǁset_balance__mutmut_32, 
        'xǁAccountServiceǁset_balance__mutmut_33': xǁAccountServiceǁset_balance__mutmut_33, 
        'xǁAccountServiceǁset_balance__mutmut_34': xǁAccountServiceǁset_balance__mutmut_34, 
        'xǁAccountServiceǁset_balance__mutmut_35': xǁAccountServiceǁset_balance__mutmut_35, 
        'xǁAccountServiceǁset_balance__mutmut_36': xǁAccountServiceǁset_balance__mutmut_36, 
        'xǁAccountServiceǁset_balance__mutmut_37': xǁAccountServiceǁset_balance__mutmut_37, 
        'xǁAccountServiceǁset_balance__mutmut_38': xǁAccountServiceǁset_balance__mutmut_38, 
        'xǁAccountServiceǁset_balance__mutmut_39': xǁAccountServiceǁset_balance__mutmut_39, 
        'xǁAccountServiceǁset_balance__mutmut_40': xǁAccountServiceǁset_balance__mutmut_40, 
        'xǁAccountServiceǁset_balance__mutmut_41': xǁAccountServiceǁset_balance__mutmut_41, 
        'xǁAccountServiceǁset_balance__mutmut_42': xǁAccountServiceǁset_balance__mutmut_42
    }
    
    def set_balance(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁset_balance__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁset_balance__mutmut_mutants"), args, kwargs, self)
        return result 
    
    set_balance.__signature__ = _mutmut_signature(xǁAccountServiceǁset_balance__mutmut_orig)
    xǁAccountServiceǁset_balance__mutmut_orig.__name__ = 'xǁAccountServiceǁset_balance'

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_orig(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_1(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = None
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_2(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(None)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_3(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is not None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_4(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(None, context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_5(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context=None)

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_6(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_7(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", )

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_8(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_9(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("user not found", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_10(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_11(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})

    async def xǁAccountServiceǁ_ensure_user_exists__mutmut_12(self, user_id: str) -> None:
        """Verify that the informed user exists."""
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
    
    xǁAccountServiceǁ_ensure_user_exists__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAccountServiceǁ_ensure_user_exists__mutmut_1': xǁAccountServiceǁ_ensure_user_exists__mutmut_1, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_2': xǁAccountServiceǁ_ensure_user_exists__mutmut_2, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_3': xǁAccountServiceǁ_ensure_user_exists__mutmut_3, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_4': xǁAccountServiceǁ_ensure_user_exists__mutmut_4, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_5': xǁAccountServiceǁ_ensure_user_exists__mutmut_5, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_6': xǁAccountServiceǁ_ensure_user_exists__mutmut_6, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_7': xǁAccountServiceǁ_ensure_user_exists__mutmut_7, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_8': xǁAccountServiceǁ_ensure_user_exists__mutmut_8, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_9': xǁAccountServiceǁ_ensure_user_exists__mutmut_9, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_10': xǁAccountServiceǁ_ensure_user_exists__mutmut_10, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_11': xǁAccountServiceǁ_ensure_user_exists__mutmut_11, 
        'xǁAccountServiceǁ_ensure_user_exists__mutmut_12': xǁAccountServiceǁ_ensure_user_exists__mutmut_12
    }
    
    def _ensure_user_exists(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountServiceǁ_ensure_user_exists__mutmut_orig"), object.__getattribute__(self, "xǁAccountServiceǁ_ensure_user_exists__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_user_exists.__signature__ = _mutmut_signature(xǁAccountServiceǁ_ensure_user_exists__mutmut_orig)
    xǁAccountServiceǁ_ensure_user_exists__mutmut_orig.__name__ = 'xǁAccountServiceǁ_ensure_user_exists'
