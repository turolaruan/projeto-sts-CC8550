"""Business logic for managing transactions."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import List

from src.models.enums import CategoryType, TransactionType
from src.models.transaction import (
    Transaction,
    TransactionCreate,
    TransactionUpdate,
    build_transaction,
)
from src.repositories.account_repository import AccountRepository
from src.repositories.budget_repository import BudgetRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.user_repository import UserRepository
from src.services.account_service import AccountService
from src.models.common import now_utc
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


class TransactionService:
    """Encapsulates transaction workflows and financial adjustments."""

    def xǁTransactionServiceǁ__init____mutmut_orig(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = account_service
        self._account_repository = account_repository
        self._category_repository = category_repository
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def xǁTransactionServiceǁ__init____mutmut_1(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = None
        self._account_service = account_service
        self._account_repository = account_repository
        self._category_repository = category_repository
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def xǁTransactionServiceǁ__init____mutmut_2(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = None
        self._account_repository = account_repository
        self._category_repository = category_repository
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def xǁTransactionServiceǁ__init____mutmut_3(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = account_service
        self._account_repository = None
        self._category_repository = category_repository
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def xǁTransactionServiceǁ__init____mutmut_4(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = account_service
        self._account_repository = account_repository
        self._category_repository = None
        self._user_repository = user_repository
        self._budget_repository = budget_repository

    def xǁTransactionServiceǁ__init____mutmut_5(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = account_service
        self._account_repository = account_repository
        self._category_repository = category_repository
        self._user_repository = None
        self._budget_repository = budget_repository

    def xǁTransactionServiceǁ__init____mutmut_6(
        self,
        repository: TransactionRepository,
        account_service: AccountService,
        account_repository: AccountRepository,
        category_repository: CategoryRepository,
        user_repository: UserRepository,
        budget_repository: BudgetRepository,
    ) -> None:
        self._repository = repository
        self._account_service = account_service
        self._account_repository = account_repository
        self._category_repository = category_repository
        self._user_repository = user_repository
        self._budget_repository = None
    
    xǁTransactionServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ__init____mutmut_1': xǁTransactionServiceǁ__init____mutmut_1, 
        'xǁTransactionServiceǁ__init____mutmut_2': xǁTransactionServiceǁ__init____mutmut_2, 
        'xǁTransactionServiceǁ__init____mutmut_3': xǁTransactionServiceǁ__init____mutmut_3, 
        'xǁTransactionServiceǁ__init____mutmut_4': xǁTransactionServiceǁ__init____mutmut_4, 
        'xǁTransactionServiceǁ__init____mutmut_5': xǁTransactionServiceǁ__init____mutmut_5, 
        'xǁTransactionServiceǁ__init____mutmut_6': xǁTransactionServiceǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTransactionServiceǁ__init____mutmut_orig)
    xǁTransactionServiceǁ__init____mutmut_orig.__name__ = 'xǁTransactionServiceǁ__init__'

    async def xǁTransactionServiceǁcreate_transaction__mutmut_orig(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_1(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(None)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_2(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = None
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_3(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(None)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_4(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = None
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_5(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(None)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_6(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(None, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_7(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, None, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_8(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, None)
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_9(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_10(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_11(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, )
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_12(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "XXaccountXX")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_13(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "ACCOUNT")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_14(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(None, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_15(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, None, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_16(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, None)
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_17(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_18(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_19(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, )
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_20(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "XXcategoryXX")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_21(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "CATEGORY")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_22(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(None, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_23(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, None)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_24(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_25(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, )

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_26(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = ""
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_27(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type != TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_28(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_29(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    None,
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_30(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context=None,
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_31(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_32(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_33(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "XXTransfer transactions must include destination accountXX",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_34(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_35(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "TRANSFER TRANSACTIONS MUST INCLUDE DESTINATION ACCOUNT",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_36(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"XXaccount_idXX": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_37(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"ACCOUNT_ID": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_38(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id != payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_39(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    None,
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_40(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context=None,
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_41(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_42(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_43(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "XXTransfer transactions require different source and destination accountsXX",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_44(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_45(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "TRANSFER TRANSACTIONS REQUIRE DIFFERENT SOURCE AND DESTINATION ACCOUNTS",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_46(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "XXaccount_idXX": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_47(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "ACCOUNT_ID": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_48(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "XXtransfer_account_idXX": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_49(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "TRANSFER_ACCOUNT_ID": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_50(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = None
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_51(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(None)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_52(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(None, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_53(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, None, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_54(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, None)

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_55(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_56(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_57(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, )

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_58(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "XXtransfer_accountXX")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_59(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "TRANSFER_ACCOUNT")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_60(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = None
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_61(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(None)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_62(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(None, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_63(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=None)
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_64(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_65(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, )
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_66(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal(None))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_67(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("XX0XX"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_68(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(None)
        await self._apply_balance_delta(transaction, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_69(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(None, transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_70(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, None)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_71(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction.amount)
        return transaction

    async def xǁTransactionServiceǁcreate_transaction__mutmut_72(self, payload: TransactionCreate) -> Transaction:
        """Create transaction applying business rules and updating balances."""
        await self._ensure_user_exists(payload.user_id)
        account = await self._get_account(payload.account_id)
        category = await self._get_category(payload.category_id)
        self._ensure_same_user(payload.user_id, account.user_id, "account")
        self._ensure_same_user(payload.user_id, category.user_id, "category")
        self._validate_category_for_transaction(category.category_type, payload.transaction_type)

        transfer_account = None
        if payload.transaction_type == TransactionType.TRANSFER:
            if not payload.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": payload.account_id},
                )
            if payload.transfer_account_id == payload.account_id:
                raise ValidationAppError(
                    "Transfer transactions require different source and destination accounts",
                    context={
                        "account_id": payload.account_id,
                        "transfer_account_id": payload.transfer_account_id,
                    },
                )
            transfer_account = await self._get_account(payload.transfer_account_id)
            self._ensure_same_user(payload.user_id, transfer_account.user_id, "transfer_account")

        transaction = build_transaction(payload)
        await self._ensure_budget_allows(transaction, exclude_amount=Decimal("0"))
        await self._repository.create(transaction)
        await self._apply_balance_delta(transaction, )
        return transaction
    
    xǁTransactionServiceǁcreate_transaction__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁcreate_transaction__mutmut_1': xǁTransactionServiceǁcreate_transaction__mutmut_1, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_2': xǁTransactionServiceǁcreate_transaction__mutmut_2, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_3': xǁTransactionServiceǁcreate_transaction__mutmut_3, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_4': xǁTransactionServiceǁcreate_transaction__mutmut_4, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_5': xǁTransactionServiceǁcreate_transaction__mutmut_5, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_6': xǁTransactionServiceǁcreate_transaction__mutmut_6, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_7': xǁTransactionServiceǁcreate_transaction__mutmut_7, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_8': xǁTransactionServiceǁcreate_transaction__mutmut_8, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_9': xǁTransactionServiceǁcreate_transaction__mutmut_9, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_10': xǁTransactionServiceǁcreate_transaction__mutmut_10, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_11': xǁTransactionServiceǁcreate_transaction__mutmut_11, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_12': xǁTransactionServiceǁcreate_transaction__mutmut_12, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_13': xǁTransactionServiceǁcreate_transaction__mutmut_13, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_14': xǁTransactionServiceǁcreate_transaction__mutmut_14, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_15': xǁTransactionServiceǁcreate_transaction__mutmut_15, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_16': xǁTransactionServiceǁcreate_transaction__mutmut_16, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_17': xǁTransactionServiceǁcreate_transaction__mutmut_17, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_18': xǁTransactionServiceǁcreate_transaction__mutmut_18, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_19': xǁTransactionServiceǁcreate_transaction__mutmut_19, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_20': xǁTransactionServiceǁcreate_transaction__mutmut_20, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_21': xǁTransactionServiceǁcreate_transaction__mutmut_21, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_22': xǁTransactionServiceǁcreate_transaction__mutmut_22, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_23': xǁTransactionServiceǁcreate_transaction__mutmut_23, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_24': xǁTransactionServiceǁcreate_transaction__mutmut_24, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_25': xǁTransactionServiceǁcreate_transaction__mutmut_25, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_26': xǁTransactionServiceǁcreate_transaction__mutmut_26, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_27': xǁTransactionServiceǁcreate_transaction__mutmut_27, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_28': xǁTransactionServiceǁcreate_transaction__mutmut_28, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_29': xǁTransactionServiceǁcreate_transaction__mutmut_29, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_30': xǁTransactionServiceǁcreate_transaction__mutmut_30, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_31': xǁTransactionServiceǁcreate_transaction__mutmut_31, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_32': xǁTransactionServiceǁcreate_transaction__mutmut_32, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_33': xǁTransactionServiceǁcreate_transaction__mutmut_33, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_34': xǁTransactionServiceǁcreate_transaction__mutmut_34, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_35': xǁTransactionServiceǁcreate_transaction__mutmut_35, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_36': xǁTransactionServiceǁcreate_transaction__mutmut_36, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_37': xǁTransactionServiceǁcreate_transaction__mutmut_37, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_38': xǁTransactionServiceǁcreate_transaction__mutmut_38, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_39': xǁTransactionServiceǁcreate_transaction__mutmut_39, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_40': xǁTransactionServiceǁcreate_transaction__mutmut_40, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_41': xǁTransactionServiceǁcreate_transaction__mutmut_41, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_42': xǁTransactionServiceǁcreate_transaction__mutmut_42, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_43': xǁTransactionServiceǁcreate_transaction__mutmut_43, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_44': xǁTransactionServiceǁcreate_transaction__mutmut_44, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_45': xǁTransactionServiceǁcreate_transaction__mutmut_45, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_46': xǁTransactionServiceǁcreate_transaction__mutmut_46, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_47': xǁTransactionServiceǁcreate_transaction__mutmut_47, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_48': xǁTransactionServiceǁcreate_transaction__mutmut_48, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_49': xǁTransactionServiceǁcreate_transaction__mutmut_49, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_50': xǁTransactionServiceǁcreate_transaction__mutmut_50, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_51': xǁTransactionServiceǁcreate_transaction__mutmut_51, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_52': xǁTransactionServiceǁcreate_transaction__mutmut_52, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_53': xǁTransactionServiceǁcreate_transaction__mutmut_53, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_54': xǁTransactionServiceǁcreate_transaction__mutmut_54, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_55': xǁTransactionServiceǁcreate_transaction__mutmut_55, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_56': xǁTransactionServiceǁcreate_transaction__mutmut_56, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_57': xǁTransactionServiceǁcreate_transaction__mutmut_57, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_58': xǁTransactionServiceǁcreate_transaction__mutmut_58, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_59': xǁTransactionServiceǁcreate_transaction__mutmut_59, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_60': xǁTransactionServiceǁcreate_transaction__mutmut_60, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_61': xǁTransactionServiceǁcreate_transaction__mutmut_61, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_62': xǁTransactionServiceǁcreate_transaction__mutmut_62, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_63': xǁTransactionServiceǁcreate_transaction__mutmut_63, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_64': xǁTransactionServiceǁcreate_transaction__mutmut_64, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_65': xǁTransactionServiceǁcreate_transaction__mutmut_65, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_66': xǁTransactionServiceǁcreate_transaction__mutmut_66, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_67': xǁTransactionServiceǁcreate_transaction__mutmut_67, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_68': xǁTransactionServiceǁcreate_transaction__mutmut_68, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_69': xǁTransactionServiceǁcreate_transaction__mutmut_69, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_70': xǁTransactionServiceǁcreate_transaction__mutmut_70, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_71': xǁTransactionServiceǁcreate_transaction__mutmut_71, 
        'xǁTransactionServiceǁcreate_transaction__mutmut_72': xǁTransactionServiceǁcreate_transaction__mutmut_72
    }
    
    def create_transaction(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁcreate_transaction__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁcreate_transaction__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_transaction.__signature__ = _mutmut_signature(xǁTransactionServiceǁcreate_transaction__mutmut_orig)
    xǁTransactionServiceǁcreate_transaction__mutmut_orig.__name__ = 'xǁTransactionServiceǁcreate_transaction'

    async def xǁTransactionServiceǁlist_transactions__mutmut_orig(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_1(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = None
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_2(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = None
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_3(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["XXuser_idXX"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_4(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["USER_ID"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_5(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = None
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_6(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["XXaccount_idXX"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_7(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["ACCOUNT_ID"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_8(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = None
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_9(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["XXcategory_idXX"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_10(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["CATEGORY_ID"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_11(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = None
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_12(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["XXtransaction_typeXX"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_13(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["TRANSACTION_TYPE"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_14(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_15(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = None
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_16(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["XXtransfer_account_idXX"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_17(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["TRANSFER_ACCOUNT_ID"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_18(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = None
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_19(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["XXdate_fromXX"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_20(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["DATE_FROM"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_21(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = None
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_22(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["XXdate_toXX"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_23(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["DATE_TO"] = date_to
        transactions = await self._repository.list(**filters)
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_24(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = None
        return list(transactions)

    async def xǁTransactionServiceǁlist_transactions__mutmut_25(
        self,
        *,
        user_id: str | None = None,
        account_id: str | None = None,
        category_id: str | None = None,
        transaction_type: str | None = None,
        transfer_account_id: str | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
    ) -> List[Transaction]:
        """Return transactions with optional filtering."""
        filters = {}
        if user_id:
            filters["user_id"] = user_id
        if account_id:
            filters["account_id"] = account_id
        if category_id:
            filters["category_id"] = category_id
        if transaction_type:
            filters["transaction_type"] = transaction_type
        if transfer_account_id is not None:
            filters["transfer_account_id"] = transfer_account_id
        if date_from:
            filters["date_from"] = date_from
        if date_to:
            filters["date_to"] = date_to
        transactions = await self._repository.list(**filters)
        return list(None)
    
    xǁTransactionServiceǁlist_transactions__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁlist_transactions__mutmut_1': xǁTransactionServiceǁlist_transactions__mutmut_1, 
        'xǁTransactionServiceǁlist_transactions__mutmut_2': xǁTransactionServiceǁlist_transactions__mutmut_2, 
        'xǁTransactionServiceǁlist_transactions__mutmut_3': xǁTransactionServiceǁlist_transactions__mutmut_3, 
        'xǁTransactionServiceǁlist_transactions__mutmut_4': xǁTransactionServiceǁlist_transactions__mutmut_4, 
        'xǁTransactionServiceǁlist_transactions__mutmut_5': xǁTransactionServiceǁlist_transactions__mutmut_5, 
        'xǁTransactionServiceǁlist_transactions__mutmut_6': xǁTransactionServiceǁlist_transactions__mutmut_6, 
        'xǁTransactionServiceǁlist_transactions__mutmut_7': xǁTransactionServiceǁlist_transactions__mutmut_7, 
        'xǁTransactionServiceǁlist_transactions__mutmut_8': xǁTransactionServiceǁlist_transactions__mutmut_8, 
        'xǁTransactionServiceǁlist_transactions__mutmut_9': xǁTransactionServiceǁlist_transactions__mutmut_9, 
        'xǁTransactionServiceǁlist_transactions__mutmut_10': xǁTransactionServiceǁlist_transactions__mutmut_10, 
        'xǁTransactionServiceǁlist_transactions__mutmut_11': xǁTransactionServiceǁlist_transactions__mutmut_11, 
        'xǁTransactionServiceǁlist_transactions__mutmut_12': xǁTransactionServiceǁlist_transactions__mutmut_12, 
        'xǁTransactionServiceǁlist_transactions__mutmut_13': xǁTransactionServiceǁlist_transactions__mutmut_13, 
        'xǁTransactionServiceǁlist_transactions__mutmut_14': xǁTransactionServiceǁlist_transactions__mutmut_14, 
        'xǁTransactionServiceǁlist_transactions__mutmut_15': xǁTransactionServiceǁlist_transactions__mutmut_15, 
        'xǁTransactionServiceǁlist_transactions__mutmut_16': xǁTransactionServiceǁlist_transactions__mutmut_16, 
        'xǁTransactionServiceǁlist_transactions__mutmut_17': xǁTransactionServiceǁlist_transactions__mutmut_17, 
        'xǁTransactionServiceǁlist_transactions__mutmut_18': xǁTransactionServiceǁlist_transactions__mutmut_18, 
        'xǁTransactionServiceǁlist_transactions__mutmut_19': xǁTransactionServiceǁlist_transactions__mutmut_19, 
        'xǁTransactionServiceǁlist_transactions__mutmut_20': xǁTransactionServiceǁlist_transactions__mutmut_20, 
        'xǁTransactionServiceǁlist_transactions__mutmut_21': xǁTransactionServiceǁlist_transactions__mutmut_21, 
        'xǁTransactionServiceǁlist_transactions__mutmut_22': xǁTransactionServiceǁlist_transactions__mutmut_22, 
        'xǁTransactionServiceǁlist_transactions__mutmut_23': xǁTransactionServiceǁlist_transactions__mutmut_23, 
        'xǁTransactionServiceǁlist_transactions__mutmut_24': xǁTransactionServiceǁlist_transactions__mutmut_24, 
        'xǁTransactionServiceǁlist_transactions__mutmut_25': xǁTransactionServiceǁlist_transactions__mutmut_25
    }
    
    def list_transactions(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁlist_transactions__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁlist_transactions__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_transactions.__signature__ = _mutmut_signature(xǁTransactionServiceǁlist_transactions__mutmut_orig)
    xǁTransactionServiceǁlist_transactions__mutmut_orig.__name__ = 'xǁTransactionServiceǁlist_transactions'

    async def xǁTransactionServiceǁget_transaction__mutmut_orig(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_1(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = None
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_2(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(None)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_3(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is not None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_4(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError(None, context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_5(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context=None)
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_6(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError(context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_7(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", )
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_8(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("XXTransaction not foundXX", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_9(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("transaction not found", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_10(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("TRANSACTION NOT FOUND", context={"id": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_11(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context={"XXidXX": transaction_id})
        return transaction

    async def xǁTransactionServiceǁget_transaction__mutmut_12(self, transaction_id: str) -> Transaction:
        """Retrieve transaction by identifier."""
        transaction = await self._repository.get(transaction_id)
        if transaction is None:
            raise EntityNotFoundError("Transaction not found", context={"ID": transaction_id})
        return transaction
    
    xǁTransactionServiceǁget_transaction__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁget_transaction__mutmut_1': xǁTransactionServiceǁget_transaction__mutmut_1, 
        'xǁTransactionServiceǁget_transaction__mutmut_2': xǁTransactionServiceǁget_transaction__mutmut_2, 
        'xǁTransactionServiceǁget_transaction__mutmut_3': xǁTransactionServiceǁget_transaction__mutmut_3, 
        'xǁTransactionServiceǁget_transaction__mutmut_4': xǁTransactionServiceǁget_transaction__mutmut_4, 
        'xǁTransactionServiceǁget_transaction__mutmut_5': xǁTransactionServiceǁget_transaction__mutmut_5, 
        'xǁTransactionServiceǁget_transaction__mutmut_6': xǁTransactionServiceǁget_transaction__mutmut_6, 
        'xǁTransactionServiceǁget_transaction__mutmut_7': xǁTransactionServiceǁget_transaction__mutmut_7, 
        'xǁTransactionServiceǁget_transaction__mutmut_8': xǁTransactionServiceǁget_transaction__mutmut_8, 
        'xǁTransactionServiceǁget_transaction__mutmut_9': xǁTransactionServiceǁget_transaction__mutmut_9, 
        'xǁTransactionServiceǁget_transaction__mutmut_10': xǁTransactionServiceǁget_transaction__mutmut_10, 
        'xǁTransactionServiceǁget_transaction__mutmut_11': xǁTransactionServiceǁget_transaction__mutmut_11, 
        'xǁTransactionServiceǁget_transaction__mutmut_12': xǁTransactionServiceǁget_transaction__mutmut_12
    }
    
    def get_transaction(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁget_transaction__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁget_transaction__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_transaction.__signature__ = _mutmut_signature(xǁTransactionServiceǁget_transaction__mutmut_orig)
    xǁTransactionServiceǁget_transaction__mutmut_orig.__name__ = 'xǁTransactionServiceǁget_transaction'

    async def xǁTransactionServiceǁupdate_transaction__mutmut_orig(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_1(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = None
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_2(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(None)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_3(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = None
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_4(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=None, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_5(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=None)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_6(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_7(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, )
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_8(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=False, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_9(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=False)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_10(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_11(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                None,
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_12(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context=None,
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_13(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_14(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_15(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "XXNo data provided to update transactionXX",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_16(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "no data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_17(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "NO DATA PROVIDED TO UPDATE TRANSACTION",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_18(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"XXidXX": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_19(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"ID": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_20(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = None
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_21(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal(None)
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_22(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("XX0XX")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_23(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = None
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_24(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(None)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_25(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = None

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_26(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = None
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_27(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal(None)
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_28(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("XX0XX")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_29(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month or existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_30(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year or existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_31(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year != prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_32(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month != prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_33(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id != prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_34(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = None

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_35(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(None, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_36(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=None)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_37(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_38(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, )

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_39(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "XXamountXX" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_40(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "AMOUNT" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_41(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" not in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_42(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = None
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_43(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["XXamountXX"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_44(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["AMOUNT"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_45(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = None

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_46(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(None, rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_47(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=None)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_48(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_49(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), )

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_50(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount + existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_51(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal(None), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_52(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("XX0.01XX"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_53(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = None
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_54(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            None,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_55(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            None,
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_56(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_57(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_58(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "XXupdated_atXX": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_59(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "UPDATED_AT": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_60(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is not None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_61(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError(None, context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_62(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context=None)

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_63(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError(context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_64(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", )

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_65(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("XXTransaction not foundXX", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_66(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_67(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("TRANSACTION NOT FOUND", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_68(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"XXidXX": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_69(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"ID": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_70(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta == Decimal("0"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_71(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal(None):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_72(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("XX0XX"):
            await self._apply_balance_delta(existing, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_73(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(None, amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_74(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, None)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_75(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(amount_delta)

        return result

    async def xǁTransactionServiceǁupdate_transaction__mutmut_76(
        self,
        transaction_id: str,
        payload: TransactionUpdate,
    ) -> Transaction:
        """Update transaction and adjust account balances accordingly."""
        existing = await self.get_transaction(transaction_id)
        updates = payload.model_dump(exclude_unset=True, exclude_none=True)
        if not updates:
            raise ValidationAppError(
                "No data provided to update transaction",
                context={"id": transaction_id},
            )

        amount_delta = Decimal("0")
        prospective_data = existing.model_dump()
        prospective_data.update(updates)
        prospective = Transaction(**prospective_data)

        exclude_amount = Decimal("0")
        if (
            existing.occurred_at.year == prospective.occurred_at.year
            and existing.occurred_at.month == prospective.occurred_at.month
            and existing.category_id == prospective.category_id
        ):
            exclude_amount = existing.amount

        await self._ensure_budget_allows(prospective, exclude_amount=exclude_amount)

        if "amount" in updates:
            new_amount = updates["amount"]
            amount_delta = (
                new_amount - existing.amount
            ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        result = await self._repository.update(
            transaction_id,
            {
                **updates,
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})

        if amount_delta != Decimal("0"):
            await self._apply_balance_delta(existing, )

        return result
    
    xǁTransactionServiceǁupdate_transaction__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁupdate_transaction__mutmut_1': xǁTransactionServiceǁupdate_transaction__mutmut_1, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_2': xǁTransactionServiceǁupdate_transaction__mutmut_2, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_3': xǁTransactionServiceǁupdate_transaction__mutmut_3, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_4': xǁTransactionServiceǁupdate_transaction__mutmut_4, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_5': xǁTransactionServiceǁupdate_transaction__mutmut_5, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_6': xǁTransactionServiceǁupdate_transaction__mutmut_6, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_7': xǁTransactionServiceǁupdate_transaction__mutmut_7, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_8': xǁTransactionServiceǁupdate_transaction__mutmut_8, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_9': xǁTransactionServiceǁupdate_transaction__mutmut_9, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_10': xǁTransactionServiceǁupdate_transaction__mutmut_10, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_11': xǁTransactionServiceǁupdate_transaction__mutmut_11, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_12': xǁTransactionServiceǁupdate_transaction__mutmut_12, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_13': xǁTransactionServiceǁupdate_transaction__mutmut_13, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_14': xǁTransactionServiceǁupdate_transaction__mutmut_14, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_15': xǁTransactionServiceǁupdate_transaction__mutmut_15, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_16': xǁTransactionServiceǁupdate_transaction__mutmut_16, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_17': xǁTransactionServiceǁupdate_transaction__mutmut_17, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_18': xǁTransactionServiceǁupdate_transaction__mutmut_18, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_19': xǁTransactionServiceǁupdate_transaction__mutmut_19, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_20': xǁTransactionServiceǁupdate_transaction__mutmut_20, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_21': xǁTransactionServiceǁupdate_transaction__mutmut_21, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_22': xǁTransactionServiceǁupdate_transaction__mutmut_22, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_23': xǁTransactionServiceǁupdate_transaction__mutmut_23, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_24': xǁTransactionServiceǁupdate_transaction__mutmut_24, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_25': xǁTransactionServiceǁupdate_transaction__mutmut_25, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_26': xǁTransactionServiceǁupdate_transaction__mutmut_26, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_27': xǁTransactionServiceǁupdate_transaction__mutmut_27, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_28': xǁTransactionServiceǁupdate_transaction__mutmut_28, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_29': xǁTransactionServiceǁupdate_transaction__mutmut_29, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_30': xǁTransactionServiceǁupdate_transaction__mutmut_30, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_31': xǁTransactionServiceǁupdate_transaction__mutmut_31, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_32': xǁTransactionServiceǁupdate_transaction__mutmut_32, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_33': xǁTransactionServiceǁupdate_transaction__mutmut_33, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_34': xǁTransactionServiceǁupdate_transaction__mutmut_34, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_35': xǁTransactionServiceǁupdate_transaction__mutmut_35, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_36': xǁTransactionServiceǁupdate_transaction__mutmut_36, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_37': xǁTransactionServiceǁupdate_transaction__mutmut_37, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_38': xǁTransactionServiceǁupdate_transaction__mutmut_38, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_39': xǁTransactionServiceǁupdate_transaction__mutmut_39, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_40': xǁTransactionServiceǁupdate_transaction__mutmut_40, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_41': xǁTransactionServiceǁupdate_transaction__mutmut_41, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_42': xǁTransactionServiceǁupdate_transaction__mutmut_42, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_43': xǁTransactionServiceǁupdate_transaction__mutmut_43, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_44': xǁTransactionServiceǁupdate_transaction__mutmut_44, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_45': xǁTransactionServiceǁupdate_transaction__mutmut_45, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_46': xǁTransactionServiceǁupdate_transaction__mutmut_46, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_47': xǁTransactionServiceǁupdate_transaction__mutmut_47, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_48': xǁTransactionServiceǁupdate_transaction__mutmut_48, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_49': xǁTransactionServiceǁupdate_transaction__mutmut_49, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_50': xǁTransactionServiceǁupdate_transaction__mutmut_50, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_51': xǁTransactionServiceǁupdate_transaction__mutmut_51, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_52': xǁTransactionServiceǁupdate_transaction__mutmut_52, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_53': xǁTransactionServiceǁupdate_transaction__mutmut_53, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_54': xǁTransactionServiceǁupdate_transaction__mutmut_54, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_55': xǁTransactionServiceǁupdate_transaction__mutmut_55, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_56': xǁTransactionServiceǁupdate_transaction__mutmut_56, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_57': xǁTransactionServiceǁupdate_transaction__mutmut_57, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_58': xǁTransactionServiceǁupdate_transaction__mutmut_58, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_59': xǁTransactionServiceǁupdate_transaction__mutmut_59, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_60': xǁTransactionServiceǁupdate_transaction__mutmut_60, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_61': xǁTransactionServiceǁupdate_transaction__mutmut_61, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_62': xǁTransactionServiceǁupdate_transaction__mutmut_62, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_63': xǁTransactionServiceǁupdate_transaction__mutmut_63, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_64': xǁTransactionServiceǁupdate_transaction__mutmut_64, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_65': xǁTransactionServiceǁupdate_transaction__mutmut_65, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_66': xǁTransactionServiceǁupdate_transaction__mutmut_66, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_67': xǁTransactionServiceǁupdate_transaction__mutmut_67, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_68': xǁTransactionServiceǁupdate_transaction__mutmut_68, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_69': xǁTransactionServiceǁupdate_transaction__mutmut_69, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_70': xǁTransactionServiceǁupdate_transaction__mutmut_70, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_71': xǁTransactionServiceǁupdate_transaction__mutmut_71, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_72': xǁTransactionServiceǁupdate_transaction__mutmut_72, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_73': xǁTransactionServiceǁupdate_transaction__mutmut_73, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_74': xǁTransactionServiceǁupdate_transaction__mutmut_74, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_75': xǁTransactionServiceǁupdate_transaction__mutmut_75, 
        'xǁTransactionServiceǁupdate_transaction__mutmut_76': xǁTransactionServiceǁupdate_transaction__mutmut_76
    }
    
    def update_transaction(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁupdate_transaction__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁupdate_transaction__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_transaction.__signature__ = _mutmut_signature(xǁTransactionServiceǁupdate_transaction__mutmut_orig)
    xǁTransactionServiceǁupdate_transaction__mutmut_orig.__name__ = 'xǁTransactionServiceǁupdate_transaction'

    async def xǁTransactionServiceǁdelete_transaction__mutmut_orig(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_1(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = None
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_2(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(None)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_3(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = None
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_4(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(None)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_5(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_6(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError(None, context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_7(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context=None)
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_8(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError(context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_9(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", )
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_10(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("XXTransaction not foundXX", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_11(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_12(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("TRANSACTION NOT FOUND", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_13(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"XXidXX": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_14(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"ID": transaction_id})
        await self._apply_balance_delta(transaction, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_15(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(None, -transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_16(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, None)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_17(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(-transaction.amount)

    async def xǁTransactionServiceǁdelete_transaction__mutmut_18(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, )

    async def xǁTransactionServiceǁdelete_transaction__mutmut_19(self, transaction_id: str) -> None:
        """Delete transaction and revert balance effects."""
        transaction = await self.get_transaction(transaction_id)
        deleted = await self._repository.delete(transaction_id)
        if not deleted:
            raise EntityNotFoundError("Transaction not found", context={"id": transaction_id})
        await self._apply_balance_delta(transaction, +transaction.amount)
    
    xǁTransactionServiceǁdelete_transaction__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁdelete_transaction__mutmut_1': xǁTransactionServiceǁdelete_transaction__mutmut_1, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_2': xǁTransactionServiceǁdelete_transaction__mutmut_2, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_3': xǁTransactionServiceǁdelete_transaction__mutmut_3, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_4': xǁTransactionServiceǁdelete_transaction__mutmut_4, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_5': xǁTransactionServiceǁdelete_transaction__mutmut_5, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_6': xǁTransactionServiceǁdelete_transaction__mutmut_6, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_7': xǁTransactionServiceǁdelete_transaction__mutmut_7, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_8': xǁTransactionServiceǁdelete_transaction__mutmut_8, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_9': xǁTransactionServiceǁdelete_transaction__mutmut_9, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_10': xǁTransactionServiceǁdelete_transaction__mutmut_10, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_11': xǁTransactionServiceǁdelete_transaction__mutmut_11, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_12': xǁTransactionServiceǁdelete_transaction__mutmut_12, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_13': xǁTransactionServiceǁdelete_transaction__mutmut_13, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_14': xǁTransactionServiceǁdelete_transaction__mutmut_14, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_15': xǁTransactionServiceǁdelete_transaction__mutmut_15, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_16': xǁTransactionServiceǁdelete_transaction__mutmut_16, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_17': xǁTransactionServiceǁdelete_transaction__mutmut_17, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_18': xǁTransactionServiceǁdelete_transaction__mutmut_18, 
        'xǁTransactionServiceǁdelete_transaction__mutmut_19': xǁTransactionServiceǁdelete_transaction__mutmut_19
    }
    
    def delete_transaction(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁdelete_transaction__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁdelete_transaction__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete_transaction.__signature__ = _mutmut_signature(xǁTransactionServiceǁdelete_transaction__mutmut_orig)
    xǁTransactionServiceǁdelete_transaction__mutmut_orig.__name__ = 'xǁTransactionServiceǁdelete_transaction'

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_orig(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_1(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = None
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_2(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(None, rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_3(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=None)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_4(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_5(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), )
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_6(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal(None), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_7(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("XX0.01XX"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_8(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized != Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_9(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal(None):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_10(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("XX0XX"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_11(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type != TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_12(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(None, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_13(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, None)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_14(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_15(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, )
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_16(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type != TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_17(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(None, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_18(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, None)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_19(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(-normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_20(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, )
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_21(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, +normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_22(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type != TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_23(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_24(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    None,
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_25(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context=None,
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_26(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_27(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_28(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "XXTransfer transactions must include destination accountXX",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_29(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_30(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "TRANSFER TRANSACTIONS MUST INCLUDE DESTINATION ACCOUNT",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_31(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"XXaccount_idXX": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_32(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"ACCOUNT_ID": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_33(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(None, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_34(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, None)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_35(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(-normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_36(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, )
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_37(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, +normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_38(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(None, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_39(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, None)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_40(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_41(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, )
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_42(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                None,
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_43(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context=None,
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_44(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                context={"transaction_type": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_45(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_46(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"XXtransaction_typeXX": transaction.transaction_type},
            )

    async def xǁTransactionServiceǁ_apply_balance_delta__mutmut_47(self, transaction: Transaction, delta: Decimal) -> None:
        normalized = delta.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if normalized == Decimal("0"):
            return
        if transaction.transaction_type == TransactionType.INCOME:
            await self._account_service.adjust_balance(transaction.account_id, normalized)
        elif transaction.transaction_type == TransactionType.EXPENSE:
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
        elif transaction.transaction_type == TransactionType.TRANSFER:
            if not transaction.transfer_account_id:
                raise ValidationAppError(
                    "Transfer transactions must include destination account",
                    context={"account_id": transaction.account_id},
                )
            await self._account_service.adjust_balance(transaction.account_id, -normalized)
            await self._account_service.adjust_balance(transaction.transfer_account_id, normalized)
        else:  # pragma: no cover - defensive branch
            raise ValidationAppError(
                f"Unsupported transaction type: {transaction.transaction_type}",
                context={"TRANSACTION_TYPE": transaction.transaction_type},
            )
    
    xǁTransactionServiceǁ_apply_balance_delta__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_apply_balance_delta__mutmut_1': xǁTransactionServiceǁ_apply_balance_delta__mutmut_1, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_2': xǁTransactionServiceǁ_apply_balance_delta__mutmut_2, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_3': xǁTransactionServiceǁ_apply_balance_delta__mutmut_3, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_4': xǁTransactionServiceǁ_apply_balance_delta__mutmut_4, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_5': xǁTransactionServiceǁ_apply_balance_delta__mutmut_5, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_6': xǁTransactionServiceǁ_apply_balance_delta__mutmut_6, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_7': xǁTransactionServiceǁ_apply_balance_delta__mutmut_7, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_8': xǁTransactionServiceǁ_apply_balance_delta__mutmut_8, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_9': xǁTransactionServiceǁ_apply_balance_delta__mutmut_9, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_10': xǁTransactionServiceǁ_apply_balance_delta__mutmut_10, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_11': xǁTransactionServiceǁ_apply_balance_delta__mutmut_11, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_12': xǁTransactionServiceǁ_apply_balance_delta__mutmut_12, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_13': xǁTransactionServiceǁ_apply_balance_delta__mutmut_13, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_14': xǁTransactionServiceǁ_apply_balance_delta__mutmut_14, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_15': xǁTransactionServiceǁ_apply_balance_delta__mutmut_15, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_16': xǁTransactionServiceǁ_apply_balance_delta__mutmut_16, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_17': xǁTransactionServiceǁ_apply_balance_delta__mutmut_17, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_18': xǁTransactionServiceǁ_apply_balance_delta__mutmut_18, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_19': xǁTransactionServiceǁ_apply_balance_delta__mutmut_19, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_20': xǁTransactionServiceǁ_apply_balance_delta__mutmut_20, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_21': xǁTransactionServiceǁ_apply_balance_delta__mutmut_21, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_22': xǁTransactionServiceǁ_apply_balance_delta__mutmut_22, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_23': xǁTransactionServiceǁ_apply_balance_delta__mutmut_23, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_24': xǁTransactionServiceǁ_apply_balance_delta__mutmut_24, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_25': xǁTransactionServiceǁ_apply_balance_delta__mutmut_25, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_26': xǁTransactionServiceǁ_apply_balance_delta__mutmut_26, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_27': xǁTransactionServiceǁ_apply_balance_delta__mutmut_27, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_28': xǁTransactionServiceǁ_apply_balance_delta__mutmut_28, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_29': xǁTransactionServiceǁ_apply_balance_delta__mutmut_29, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_30': xǁTransactionServiceǁ_apply_balance_delta__mutmut_30, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_31': xǁTransactionServiceǁ_apply_balance_delta__mutmut_31, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_32': xǁTransactionServiceǁ_apply_balance_delta__mutmut_32, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_33': xǁTransactionServiceǁ_apply_balance_delta__mutmut_33, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_34': xǁTransactionServiceǁ_apply_balance_delta__mutmut_34, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_35': xǁTransactionServiceǁ_apply_balance_delta__mutmut_35, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_36': xǁTransactionServiceǁ_apply_balance_delta__mutmut_36, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_37': xǁTransactionServiceǁ_apply_balance_delta__mutmut_37, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_38': xǁTransactionServiceǁ_apply_balance_delta__mutmut_38, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_39': xǁTransactionServiceǁ_apply_balance_delta__mutmut_39, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_40': xǁTransactionServiceǁ_apply_balance_delta__mutmut_40, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_41': xǁTransactionServiceǁ_apply_balance_delta__mutmut_41, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_42': xǁTransactionServiceǁ_apply_balance_delta__mutmut_42, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_43': xǁTransactionServiceǁ_apply_balance_delta__mutmut_43, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_44': xǁTransactionServiceǁ_apply_balance_delta__mutmut_44, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_45': xǁTransactionServiceǁ_apply_balance_delta__mutmut_45, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_46': xǁTransactionServiceǁ_apply_balance_delta__mutmut_46, 
        'xǁTransactionServiceǁ_apply_balance_delta__mutmut_47': xǁTransactionServiceǁ_apply_balance_delta__mutmut_47
    }
    
    def _apply_balance_delta(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_apply_balance_delta__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_apply_balance_delta__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _apply_balance_delta.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_apply_balance_delta__mutmut_orig)
    xǁTransactionServiceǁ_apply_balance_delta__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_apply_balance_delta'

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_orig(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_1(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type == TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_2(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = None
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_3(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=None,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_4(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=None,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_5(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=None,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_6(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=None,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_7(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_8(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_9(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_10(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_11(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_12(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = None
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_13(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[1]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_14(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = None
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_15(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=None,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_16(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=None,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_17(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=None,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_18(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=None,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_19(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_20(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_21(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_22(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_23(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = None
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_24(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount - transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_25(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total + exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_26(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total >= budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_27(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                None,
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_28(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context=None,
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_29(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_30(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_31(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "XXBudget limit exceeded for this category and periodXX",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_32(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_33(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "BUDGET LIMIT EXCEEDED FOR THIS CATEGORY AND PERIOD",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_34(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "XXcategory_idXX": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_35(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "CATEGORY_ID": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_36(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "XXmonthXX": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_37(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "MONTH": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_38(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "XXyearXX": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_39(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "YEAR": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_40(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "XXbudgetXX": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_41(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "BUDGET": str(budget.amount),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_42(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(None),
                    "current_total": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_43(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "XXcurrent_totalXX": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_44(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "CURRENT_TOTAL": str(adjusted_total),
                },
            )

    async def xǁTransactionServiceǁ_ensure_budget_allows__mutmut_45(
        self,
        transaction: Transaction,
        *,
        exclude_amount: Decimal,
    ) -> None:
        if transaction.transaction_type != TransactionType.EXPENSE:
            return
        budgets = await self._budget_repository.list(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        if not budgets:
            return
        budget = budgets[0]
        current_total = await self._repository.sum_for_category_period(
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            year=transaction.occurred_at.year,
            month=transaction.occurred_at.month,
        )
        adjusted_total = current_total - exclude_amount + transaction.amount
        if adjusted_total > budget.amount:
            raise ValidationAppError(
                "Budget limit exceeded for this category and period",
                context={
                    "category_id": transaction.category_id,
                    "month": transaction.occurred_at.month,
                    "year": transaction.occurred_at.year,
                    "budget": str(budget.amount),
                    "current_total": str(None),
                },
            )
    
    xǁTransactionServiceǁ_ensure_budget_allows__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_1': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_1, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_2': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_2, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_3': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_3, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_4': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_4, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_5': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_5, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_6': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_6, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_7': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_7, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_8': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_8, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_9': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_9, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_10': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_10, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_11': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_11, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_12': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_12, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_13': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_13, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_14': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_14, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_15': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_15, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_16': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_16, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_17': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_17, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_18': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_18, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_19': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_19, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_20': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_20, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_21': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_21, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_22': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_22, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_23': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_23, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_24': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_24, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_25': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_25, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_26': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_26, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_27': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_27, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_28': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_28, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_29': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_29, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_30': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_30, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_31': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_31, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_32': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_32, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_33': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_33, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_34': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_34, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_35': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_35, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_36': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_36, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_37': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_37, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_38': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_38, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_39': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_39, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_40': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_40, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_41': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_41, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_42': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_42, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_43': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_43, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_44': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_44, 
        'xǁTransactionServiceǁ_ensure_budget_allows__mutmut_45': xǁTransactionServiceǁ_ensure_budget_allows__mutmut_45
    }
    
    def _ensure_budget_allows(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_ensure_budget_allows__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_ensure_budget_allows__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_budget_allows.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_ensure_budget_allows__mutmut_orig)
    xǁTransactionServiceǁ_ensure_budget_allows__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_ensure_budget_allows'

    async def xǁTransactionServiceǁ_get_account__mutmut_orig(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_1(self, account_id: str):
        account = None
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_2(self, account_id: str):
        account = await self._account_repository.get(None)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_3(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is not None:
            raise EntityNotFoundError("Account not found", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_4(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError(None, context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_5(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context=None)
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_6(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError(context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_7(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", )
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_8(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("XXAccount not foundXX", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_9(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("account not found", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_10(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("ACCOUNT NOT FOUND", context={"id": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_11(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"XXidXX": account_id})
        return account

    async def xǁTransactionServiceǁ_get_account__mutmut_12(self, account_id: str):
        account = await self._account_repository.get(account_id)
        if account is None:
            raise EntityNotFoundError("Account not found", context={"ID": account_id})
        return account
    
    xǁTransactionServiceǁ_get_account__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_get_account__mutmut_1': xǁTransactionServiceǁ_get_account__mutmut_1, 
        'xǁTransactionServiceǁ_get_account__mutmut_2': xǁTransactionServiceǁ_get_account__mutmut_2, 
        'xǁTransactionServiceǁ_get_account__mutmut_3': xǁTransactionServiceǁ_get_account__mutmut_3, 
        'xǁTransactionServiceǁ_get_account__mutmut_4': xǁTransactionServiceǁ_get_account__mutmut_4, 
        'xǁTransactionServiceǁ_get_account__mutmut_5': xǁTransactionServiceǁ_get_account__mutmut_5, 
        'xǁTransactionServiceǁ_get_account__mutmut_6': xǁTransactionServiceǁ_get_account__mutmut_6, 
        'xǁTransactionServiceǁ_get_account__mutmut_7': xǁTransactionServiceǁ_get_account__mutmut_7, 
        'xǁTransactionServiceǁ_get_account__mutmut_8': xǁTransactionServiceǁ_get_account__mutmut_8, 
        'xǁTransactionServiceǁ_get_account__mutmut_9': xǁTransactionServiceǁ_get_account__mutmut_9, 
        'xǁTransactionServiceǁ_get_account__mutmut_10': xǁTransactionServiceǁ_get_account__mutmut_10, 
        'xǁTransactionServiceǁ_get_account__mutmut_11': xǁTransactionServiceǁ_get_account__mutmut_11, 
        'xǁTransactionServiceǁ_get_account__mutmut_12': xǁTransactionServiceǁ_get_account__mutmut_12
    }
    
    def _get_account(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_get_account__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_get_account__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_account.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_get_account__mutmut_orig)
    xǁTransactionServiceǁ_get_account__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_get_account'

    async def xǁTransactionServiceǁ_get_category__mutmut_orig(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_1(self, category_id: str):
        category = None
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_2(self, category_id: str):
        category = await self._category_repository.get(None)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_3(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is not None:
            raise EntityNotFoundError("Category not found", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_4(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError(None, context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_5(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context=None)
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_6(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError(context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_7(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", )
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_8(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("XXCategory not foundXX", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_9(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("category not found", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_10(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("CATEGORY NOT FOUND", context={"id": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_11(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"XXidXX": category_id})
        return category

    async def xǁTransactionServiceǁ_get_category__mutmut_12(self, category_id: str):
        category = await self._category_repository.get(category_id)
        if category is None:
            raise EntityNotFoundError("Category not found", context={"ID": category_id})
        return category
    
    xǁTransactionServiceǁ_get_category__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_get_category__mutmut_1': xǁTransactionServiceǁ_get_category__mutmut_1, 
        'xǁTransactionServiceǁ_get_category__mutmut_2': xǁTransactionServiceǁ_get_category__mutmut_2, 
        'xǁTransactionServiceǁ_get_category__mutmut_3': xǁTransactionServiceǁ_get_category__mutmut_3, 
        'xǁTransactionServiceǁ_get_category__mutmut_4': xǁTransactionServiceǁ_get_category__mutmut_4, 
        'xǁTransactionServiceǁ_get_category__mutmut_5': xǁTransactionServiceǁ_get_category__mutmut_5, 
        'xǁTransactionServiceǁ_get_category__mutmut_6': xǁTransactionServiceǁ_get_category__mutmut_6, 
        'xǁTransactionServiceǁ_get_category__mutmut_7': xǁTransactionServiceǁ_get_category__mutmut_7, 
        'xǁTransactionServiceǁ_get_category__mutmut_8': xǁTransactionServiceǁ_get_category__mutmut_8, 
        'xǁTransactionServiceǁ_get_category__mutmut_9': xǁTransactionServiceǁ_get_category__mutmut_9, 
        'xǁTransactionServiceǁ_get_category__mutmut_10': xǁTransactionServiceǁ_get_category__mutmut_10, 
        'xǁTransactionServiceǁ_get_category__mutmut_11': xǁTransactionServiceǁ_get_category__mutmut_11, 
        'xǁTransactionServiceǁ_get_category__mutmut_12': xǁTransactionServiceǁ_get_category__mutmut_12
    }
    
    def _get_category(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_get_category__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_get_category__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_category.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_get_category__mutmut_orig)
    xǁTransactionServiceǁ_get_category__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_get_category'

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_orig(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_1(self, user_id: str) -> None:
        user = None
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_2(self, user_id: str) -> None:
        user = await self._user_repository.get(None)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_3(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is not None:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_4(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(None, context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_5(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context=None)

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_6(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_7(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", )

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_8(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_9(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("user not found", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_10(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_11(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})

    async def xǁTransactionServiceǁ_ensure_user_exists__mutmut_12(self, user_id: str) -> None:
        user = await self._user_repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
    
    xǁTransactionServiceǁ_ensure_user_exists__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_ensure_user_exists__mutmut_1': xǁTransactionServiceǁ_ensure_user_exists__mutmut_1, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_2': xǁTransactionServiceǁ_ensure_user_exists__mutmut_2, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_3': xǁTransactionServiceǁ_ensure_user_exists__mutmut_3, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_4': xǁTransactionServiceǁ_ensure_user_exists__mutmut_4, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_5': xǁTransactionServiceǁ_ensure_user_exists__mutmut_5, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_6': xǁTransactionServiceǁ_ensure_user_exists__mutmut_6, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_7': xǁTransactionServiceǁ_ensure_user_exists__mutmut_7, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_8': xǁTransactionServiceǁ_ensure_user_exists__mutmut_8, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_9': xǁTransactionServiceǁ_ensure_user_exists__mutmut_9, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_10': xǁTransactionServiceǁ_ensure_user_exists__mutmut_10, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_11': xǁTransactionServiceǁ_ensure_user_exists__mutmut_11, 
        'xǁTransactionServiceǁ_ensure_user_exists__mutmut_12': xǁTransactionServiceǁ_ensure_user_exists__mutmut_12
    }
    
    def _ensure_user_exists(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_ensure_user_exists__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_ensure_user_exists__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_user_exists.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_ensure_user_exists__mutmut_orig)
    xǁTransactionServiceǁ_ensure_user_exists__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_ensure_user_exists'

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_orig(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_1(self, expected: str, actual: str, label: str) -> None:
        if expected == actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_2(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                None,
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_3(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context=None,
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_4(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                context={"expected_user_id": expected, "actual_user_id": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_5(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_6(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"XXexpected_user_idXX": expected, "actual_user_id": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_7(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"EXPECTED_USER_ID": expected, "actual_user_id": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_8(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "XXactual_user_idXX": actual},
            )

    def xǁTransactionServiceǁ_ensure_same_user__mutmut_9(self, expected: str, actual: str, label: str) -> None:
        if expected != actual:
            raise ValidationAppError(
                f"{label} belongs to a different user",
                context={"expected_user_id": expected, "ACTUAL_USER_ID": actual},
            )
    
    xǁTransactionServiceǁ_ensure_same_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_ensure_same_user__mutmut_1': xǁTransactionServiceǁ_ensure_same_user__mutmut_1, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_2': xǁTransactionServiceǁ_ensure_same_user__mutmut_2, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_3': xǁTransactionServiceǁ_ensure_same_user__mutmut_3, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_4': xǁTransactionServiceǁ_ensure_same_user__mutmut_4, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_5': xǁTransactionServiceǁ_ensure_same_user__mutmut_5, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_6': xǁTransactionServiceǁ_ensure_same_user__mutmut_6, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_7': xǁTransactionServiceǁ_ensure_same_user__mutmut_7, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_8': xǁTransactionServiceǁ_ensure_same_user__mutmut_8, 
        'xǁTransactionServiceǁ_ensure_same_user__mutmut_9': xǁTransactionServiceǁ_ensure_same_user__mutmut_9
    }
    
    def _ensure_same_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_ensure_same_user__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_ensure_same_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_same_user.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_ensure_same_user__mutmut_orig)
    xǁTransactionServiceǁ_ensure_same_user__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_ensure_same_user'

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_orig(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_1(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME or category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_2(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type != TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_3(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type == CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_4(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                None,
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_5(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context=None,
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_6(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_7(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_8(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "XXIncome transactions require income categoriesXX",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_9(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_10(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "INCOME TRANSACTIONS REQUIRE INCOME CATEGORIES",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_11(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"XXcategory_typeXX": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_12(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"CATEGORY_TYPE": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_13(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "XXtransaction_typeXX": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_14(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "TRANSACTION_TYPE": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_15(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE or category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_16(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type != TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_17(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type == CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_18(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                None,
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_19(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context=None,
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_20(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_21(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_22(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "XXExpense transactions require expense categoriesXX",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_23(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "expense transactions require expense categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_24(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "EXPENSE TRANSACTIONS REQUIRE EXPENSE CATEGORIES",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_25(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"XXcategory_typeXX": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_26(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"CATEGORY_TYPE": category_type, "transaction_type": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_27(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "XXtransaction_typeXX": transaction_type},
            )

    def xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_28(
        self,
        category_type: CategoryType,
        transaction_type: TransactionType,
    ) -> None:
        if transaction_type == TransactionType.INCOME and category_type != CategoryType.INCOME:
            raise ValidationAppError(
                "Income transactions require income categories",
                context={"category_type": category_type, "transaction_type": transaction_type},
            )
        if transaction_type == TransactionType.EXPENSE and category_type != CategoryType.EXPENSE:
            raise ValidationAppError(
                "Expense transactions require expense categories",
                context={"category_type": category_type, "TRANSACTION_TYPE": transaction_type},
            )
    
    xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_1': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_1, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_2': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_2, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_3': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_3, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_4': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_4, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_5': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_5, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_6': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_6, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_7': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_7, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_8': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_8, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_9': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_9, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_10': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_10, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_11': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_11, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_12': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_12, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_13': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_13, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_14': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_14, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_15': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_15, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_16': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_16, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_17': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_17, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_18': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_18, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_19': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_19, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_20': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_20, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_21': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_21, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_22': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_22, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_23': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_23, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_24': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_24, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_25': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_25, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_26': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_26, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_27': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_27, 
        'xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_28': xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_28
    }
    
    def _validate_category_for_transaction(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_orig"), object.__getattribute__(self, "xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _validate_category_for_transaction.__signature__ = _mutmut_signature(xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_orig)
    xǁTransactionServiceǁ_validate_category_for_transaction__mutmut_orig.__name__ = 'xǁTransactionServiceǁ_validate_category_for_transaction'
