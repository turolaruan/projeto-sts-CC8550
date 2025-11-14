"""Testes unitários para os serviços de domínio."""

from __future__ import annotations

import importlib
import importlib.util
import sys
import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from unittest.mock import AsyncMock, patch

from src.models.account import Account, AccountCreate, AccountUpdate
from src.models.budget import Budget, BudgetCreate, BudgetUpdate
from src.models.category import Category, CategoryCreate, CategoryUpdate
from src.models.common import generate_object_id
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import Transaction, TransactionCreate, TransactionUpdate
from src.models.user import User, UserCreate, UserUpdate
from src.services.account_service import AccountService
from src.services.budget_service import BudgetService
from src.services.category_service import CategoryService
from src.services.report_service import ReportService
from src.services.transaction_service import TransactionService
from src.services.user_service import UserService
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)


UTC_NOW = datetime(2024, 2, 1, 10, 0, tzinfo=timezone.utc)


def make_user(**overrides: object) -> User:
    data = {
        "id": generate_object_id(),
        "name": "Usuário Serviço",
        "email": "servico@example.com",
        "default_currency": CurrencyCode.BRL,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return User(**data)


def make_account(**overrides: object) -> Account:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "name": "Conta Serviço",
        "account_type": AccountType.CHECKING,
        "currency": CurrencyCode.BRL,
        "description": "Conta de testes",
        "minimum_balance": Decimal("50.00"),
        "balance": Decimal("150.00"),
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Account(**data)


def make_category(**overrides: object) -> Category:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "name": "Categoria Serviço",
        "category_type": CategoryType.EXPENSE,
        "description": None,
        "parent_id": None,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Category(**data)


def make_budget(**overrides: object) -> Budget:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "category_id": generate_object_id(),
        "year": 2024,
        "month": 6,
        "amount": Decimal("500.00"),
        "alert_percentage": 80,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Budget(**data)


def make_transaction(**overrides: object) -> Transaction:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "account_id": generate_object_id(),
        "category_id": generate_object_id(),
        "amount": Decimal("200.00"),
        "transaction_type": TransactionType.EXPENSE,
        "occurred_at": UTC_NOW,
        "description": "Transação Serviço",
        "notes": None,
        "counterparty": None,
        "transfer_account_id": None,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Transaction(**data)


class AccountServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.account_repo = AsyncMock()
        self.user_repo = AsyncMock()
        self.transaction_repo = AsyncMock()
        self.service = AccountService(self.account_repo, self.user_repo, self.transaction_repo)
        self.user = make_user()
        self.account = make_account(user_id=self.user.id)
        self.user_repo.get.return_value = self.user
        self.account_repo.get.return_value = self.account
        self.account_repo.update.return_value = self.account

    async def test_create_account_success(self) -> None:
        payload = AccountCreate(
            user_id=self.user.id,
            name="Conta Salário",
            account_type=AccountType.CHECKING,
            currency=CurrencyCode.BRL,
            starting_balance=Decimal("100.00"),
        )
        with patch("src.services.account_service.build_account", return_value=self.account):
            result = await self.service.create_account(payload)
        self.account_repo.create.assert_awaited_once()
        self.assertEqual(result.id, self.account.id)

    async def test_create_account_requires_existing_user(self) -> None:
        self.user_repo.get.return_value = None
        payload = AccountCreate(
            user_id=self.user.id,
            name="Conta Fantasma",
            account_type=AccountType.CHECKING,
            starting_balance=Decimal("0"),
        )
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_account(payload)

    async def test_create_account_validates_starting_balance(self) -> None:
        payload = AccountCreate(
            user_id=self.user.id,
            name="Conta Restrita",
            account_type=AccountType.CHECKING,
            minimum_balance=Decimal("200.00"),
            starting_balance=Decimal("50.00"),
        )
        with self.assertRaises(ValidationAppError):
            await self.service.create_account(payload)

    async def test_list_accounts_forward_filters(self) -> None:
        self.account_repo.list.return_value = [self.account]
        accounts = await self.service.list_accounts(
            user_id=self.user.id,
            account_type=self.account.account_type,
            currency=self.account.currency,
            name="Serviço",
        )
        self.account_repo.list.assert_awaited_once()
        self.assertEqual(len(accounts), 1)

    async def test_get_account_not_found(self) -> None:
        self.account_repo.get.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.get_account(self.account.id)

    async def test_update_account_requires_payload(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.update_account(self.account.id, AccountUpdate())

    async def test_update_account_validates_minimum_balance(self) -> None:
        self.account_repo.get.return_value = self.account.model_copy(update={"balance": Decimal("50.00")})
        with self.assertRaises(ValidationAppError):
            await self.service.update_account(
                self.account.id,
                AccountUpdate(minimum_balance=Decimal("100.00")),
            )

    async def test_update_account_success(self) -> None:
        updated = self.account.model_copy(update={"description": "Atualizada"})
        self.account_repo.update.return_value = updated
        result = await self.service.update_account(
            self.account.id,
            AccountUpdate(description="Atualizada"),
        )
        self.assertEqual(result.description, "Atualizada")

    async def test_update_account_not_found_after_repo_call(self) -> None:
        self.account_repo.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.update_account(
                self.account.id,
                AccountUpdate(description="Falha"),
            )

    async def test_delete_account_blocks_transactions(self) -> None:
        self.transaction_repo.exists_for_account.return_value = True
        with self.assertRaises(ValidationAppError):
            await self.service.delete_account(self.account.id)

    async def test_delete_account_not_found(self) -> None:
        self.transaction_repo.exists_for_account.return_value = False
        self.account_repo.delete.return_value = False
        with self.assertRaises(EntityNotFoundError):
            await self.service.delete_account(self.account.id)

    async def test_adjust_balance_prevents_below_minimum(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.adjust_balance(self.account.id, Decimal("-200.00"))

    async def test_adjust_balance_success(self) -> None:
        updated = self.account.model_copy(update={"balance": Decimal("120.00")})
        self.account_repo.update.return_value = updated
        result = await self.service.adjust_balance(self.account.id, Decimal("-30.00"))
        self.assertEqual(result.balance, Decimal("120.00"))

    async def test_adjust_balance_repo_missing(self) -> None:
        self.account_repo.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.adjust_balance(self.account.id, Decimal("-10.00"))

    async def test_set_balance_validations(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.set_balance(self.account.id, Decimal("10.00"))
        updated = self.account.model_copy(update={"balance": Decimal("300.00")})
        self.account_repo.update.return_value = updated
        result = await self.service.set_balance(self.account.id, Decimal("300.00"))
        self.assertEqual(result.balance, Decimal("300.00"))

    async def test_set_balance_repo_missing(self) -> None:
        self.account_repo.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.set_balance(self.account.id, Decimal("100.00"))


class BudgetServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.budget_repo = AsyncMock()
        self.user_repo = AsyncMock()
        self.category_repo = AsyncMock()
        self.transaction_repo = AsyncMock()
        self.service = BudgetService(
            self.budget_repo,
            self.user_repo,
            self.category_repo,
            self.transaction_repo,
        )
        self.user = make_user()
        self.category = make_category(user_id=self.user.id, category_type=CategoryType.EXPENSE)
        self.budget = make_budget(user_id=self.user.id, category_id=self.category.id)
        self.user_repo.get.return_value = self.user
        self.category_repo.get.return_value = self.category
        self.budget_repo.get.return_value = self.budget

    async def test_create_budget_blocks_duplicates(self) -> None:
        self.budget_repo.find_by_period.return_value = self.budget
        payload = BudgetCreate(
            user_id=self.user.id,
            category_id=self.category.id,
            year=2024,
            month=6,
            amount=Decimal("400.00"),
        )
        with self.assertRaises(EntityAlreadyExistsError):
            await self.service.create_budget(payload)

    async def test_create_budget_requires_expense_category(self) -> None:
        self.category_repo.get.return_value = make_category(
            user_id=self.user.id,
            category_type=CategoryType.INCOME,
        )
        payload = BudgetCreate(
            user_id=self.user.id,
            category_id=self.category.id,
            year=2024,
            month=6,
            amount=Decimal("400.00"),
        )
        with self.assertRaises(ValidationAppError):
            await self.service.create_budget(payload)

    async def test_create_budget_requires_same_user(self) -> None:
        foreign_category = make_category(user_id=generate_object_id(), category_type=CategoryType.EXPENSE)
        self.category_repo.get.return_value = foreign_category
        payload = BudgetCreate(
            user_id=self.user.id,
            category_id=foreign_category.id,
            year=2024,
            month=6,
            amount=Decimal("400.00"),
        )
        with self.assertRaises(ValidationAppError):
            await self.service.create_budget(payload)

    async def test_create_budget_requires_existing_user(self) -> None:
        self.user_repo.get.return_value = None
        payload = BudgetCreate(
            user_id=self.user.id,
            category_id=self.category.id,
            year=2024,
            month=6,
            amount=Decimal("400.00"),
        )
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_budget(payload)

    async def test_create_budget_missing_category(self) -> None:
        self.category_repo.get.return_value = None
        payload = BudgetCreate(
            user_id=self.user.id,
            category_id=self.category.id,
            year=2024,
            month=6,
            amount=Decimal("400.00"),
        )
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_budget(payload)

    async def test_create_budget_success(self) -> None:
        self.budget_repo.find_by_period.return_value = None
        payload = BudgetCreate(
            user_id=self.user.id,
            category_id=self.category.id,
            year=2024,
            month=6,
            amount=Decimal("400.00"),
        )
        with patch("src.services.budget_service.build_budget", return_value=self.budget):
            result = await self.service.create_budget(payload)
        self.budget_repo.create.assert_awaited_once()
        self.assertEqual(result.id, self.budget.id)

    async def test_list_budgets(self) -> None:
        self.budget_repo.list.return_value = [self.budget]
        results = await self.service.list_budgets(
            user_id=self.user.id,
            category_id=self.category.id,
            year=self.budget.year,
            month=self.budget.month,
        )
        self.assertEqual(len(results), 1)

    async def test_get_budget_not_found(self) -> None:
        self.budget_repo.get.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.get_budget(self.budget.id)

    async def test_update_budget_requires_payload(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.update_budget(self.budget.id, BudgetUpdate())

    async def test_update_budget_success(self) -> None:
        updated = self.budget.model_copy(update={"amount": Decimal("999.00")})
        self.budget_repo.update.return_value = updated
        result = await self.service.update_budget(self.budget.id, BudgetUpdate(amount=Decimal("999.00")))
        self.assertEqual(result.amount, Decimal("999.00"))

    async def test_update_budget_not_found_after_repo_call(self) -> None:
        self.budget_repo.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.update_budget(self.budget.id, BudgetUpdate(amount=Decimal("1.00")))

    async def test_delete_budget_blocks_transactions(self) -> None:
        self.transaction_repo.exists_for_category.return_value = True
        with self.assertRaises(ValidationAppError):
            await self.service.delete_budget(self.budget.id)

    async def test_delete_budget_missing(self) -> None:
        self.transaction_repo.exists_for_category.return_value = False
        self.budget_repo.delete.return_value = False
        result_budget = self.budget
        self.budget_repo.get.return_value = result_budget
        with self.assertRaises(EntityNotFoundError):
            await self.service.delete_budget(self.budget.id)

    async def test_delete_budget_success(self) -> None:
        self.transaction_repo.exists_for_category.return_value = False
        self.budget_repo.delete.return_value = True
        self.budget_repo.get.return_value = self.budget
        await self.service.delete_budget(self.budget.id)
        self.budget_repo.delete.assert_awaited_once()


class CategoryServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.category_repo = AsyncMock()
        self.user_repo = AsyncMock()
        self.transaction_repo = AsyncMock()
        self.budget_repo = AsyncMock()
        self.service = CategoryService(
            self.category_repo,
            self.user_repo,
            self.transaction_repo,
            self.budget_repo,
        )
        self.user = make_user()
        self.category = make_category(user_id=self.user.id)
        self.user_repo.get.return_value = self.user
        self.category_repo.get.return_value = self.category

    async def test_create_category_requires_user(self) -> None:
        self.user_repo.get.return_value = None
        payload = CategoryCreate(user_id=self.user.id, name="Nova", category_type=CategoryType.EXPENSE)
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_category(payload)

    async def test_create_category_success(self) -> None:
        payload = CategoryCreate(user_id=self.user.id, name="Sucesso", category_type=CategoryType.EXPENSE)
        with patch("src.services.category_service.build_category", return_value=self.category):
            result = await self.service.create_category(payload)
        self.assertEqual(result.id, self.category.id)

    async def test_create_category_validates_parent_user(self) -> None:
        payload = CategoryCreate(
            user_id=self.user.id,
            name="Filho",
            category_type=CategoryType.EXPENSE,
            parent_id=generate_object_id(),
        )
        foreign_parent = make_category(id=payload.parent_id, user_id=generate_object_id())
        self.category_repo.get.side_effect = [foreign_parent]
        with self.assertRaises(ValidationAppError):
            await self.service.create_category(payload)

    async def test_list_categories(self) -> None:
        self.category_repo.list.return_value = [self.category]
        results = await self.service.list_categories(
            user_id=self.user.id,
            category_type=self.category.category_type,
            parent_id="root",
            name="categoria",
        )
        self.assertEqual(len(results), 1)

    async def test_get_category_not_found(self) -> None:
        self.category_repo.get.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.get_category(self.category.id)

    async def test_update_category_requires_payload(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.update_category(self.category.id, CategoryUpdate())

    async def test_update_category_success(self) -> None:
        updated = self.category.model_copy(update={"name": "Atualizada"})
        self.category_repo.update.return_value = updated
        result = await self.service.update_category(self.category.id, CategoryUpdate(name="Atualizada"))
        self.assertEqual(result.name, "Atualizada")

    async def test_update_category_not_found_after_repo_call(self) -> None:
        self.category_repo.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.update_category(self.category.id, CategoryUpdate(description="Nada"))

    async def test_update_category_prevents_self_parent(self) -> None:
        self.category_repo.get.side_effect = [self.category, self.category]
        with self.assertRaises(ValidationAppError):
            await self.service.update_category(
                self.category.id,
                CategoryUpdate(parent_id=self.category.id),
            )

    async def test_delete_category_blocks_transactions_and_budgets(self) -> None:
        self.transaction_repo.exists_for_category.return_value = True
        with self.assertRaises(ValidationAppError):
            await self.service.delete_category(self.category.id)
        self.transaction_repo.exists_for_category.return_value = False
        self.budget_repo.list.return_value = [make_budget(category_id=self.category.id)]
        with self.assertRaises(ValidationAppError):
            await self.service.delete_category(self.category.id)

    async def test_delete_category_missing(self) -> None:
        self.transaction_repo.exists_for_category.return_value = False
        self.budget_repo.list.return_value = []
        self.category_repo.delete.return_value = False
        with self.assertRaises(EntityNotFoundError):
            await self.service.delete_category(self.category.id)

    async def test_delete_category_success(self) -> None:
        self.transaction_repo.exists_for_category.return_value = False
        self.budget_repo.list.return_value = []
        self.category_repo.delete.return_value = True
        await self.service.delete_category(self.category.id)
        self.category_repo.delete.assert_awaited_once()

    async def test_validate_parent_missing_category(self) -> None:
        self.category_repo.get.side_effect = [None]
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_category(
                CategoryCreate(
                    user_id=self.user.id,
                    name="Filho",
                    category_type=CategoryType.EXPENSE,
                    parent_id=generate_object_id(),
                )
            )


class TransactionServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.transaction_repo = AsyncMock()
        self.account_service = AsyncMock()
        self.account_repo = AsyncMock()
        self.category_repo = AsyncMock()
        self.user_repo = AsyncMock()
        self.budget_repo = AsyncMock()
        self.service = TransactionService(
            repository=self.transaction_repo,
            account_service=self.account_service,
            account_repository=self.account_repo,
            category_repository=self.category_repo,
            user_repository=self.user_repo,
            budget_repository=self.budget_repo,
        )
        self.user = make_user()
        self.account = make_account(user_id=self.user.id)
        self.transfer_account = make_account(user_id=self.user.id)
        self.category_expense = make_category(user_id=self.user.id, category_type=CategoryType.EXPENSE)
        self.category_income = make_category(user_id=self.user.id, category_type=CategoryType.INCOME)
        self.transaction = make_transaction(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_expense.id,
            amount=Decimal("200.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        self.user_repo.get.return_value = self.user
        self.account_repo.get.side_effect = self._get_account_by_id
        self.category_repo.get.side_effect = self._get_category_by_id
        self.transaction_repo.get.return_value = self.transaction
        self.transaction_repo.update.return_value = self.transaction
        self.transaction_repo.list.return_value = [self.transaction]
        self.transaction_repo.sum_for_category_period.return_value = Decimal("0")
        self.budget_repo.list.return_value = []

    def _get_account_by_id(self, account_id: str) -> Account | None:
        if account_id == self.account.id:
            return self.account
        if account_id == self.transfer_account.id:
            return self.transfer_account
        return None

    def _get_category_by_id(self, category_id: str) -> Category | None:
        if category_id == self.category_expense.id:
            return self.category_expense
        if category_id == self.category_income.id:
            return self.category_income
        return None

    async def test_create_transaction_expense_success(self) -> None:
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_expense.id,
            amount=Decimal("100.00"),
            transaction_type=TransactionType.EXPENSE,
            description="Compra",
        )
        with patch("src.services.transaction_service.build_transaction", return_value=self.transaction):
            result = await self.service.create_transaction(payload)
        self.transaction_repo.create.assert_awaited_once()
        self.account_service.adjust_balance.assert_awaited_with(self.account.id, -self.transaction.amount)
        self.assertEqual(result.id, self.transaction.id)

    async def test_create_transaction_requires_user(self) -> None:
        self.user_repo.get.return_value = None
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_expense.id,
            amount=Decimal("50.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_transaction(payload)

    async def test_create_transaction_validates_category_type(self) -> None:
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_income.id,
            amount=Decimal("50.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        with self.assertRaises(ValidationAppError):
            await self.service.create_transaction(payload)

    async def test_create_transaction_requires_account_same_user(self) -> None:
        foreign_account = self.account.model_copy(update={"user_id": generate_object_id(), "id": generate_object_id()})
        self.account_repo.get.side_effect = lambda account_id: foreign_account if account_id == foreign_account.id else self._get_account_by_id(account_id)
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=foreign_account.id,
            category_id=self.category_expense.id,
            amount=Decimal("50.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        with self.assertRaises(ValidationAppError):
            await self.service.create_transaction(payload)

    async def test_create_transaction_missing_account(self) -> None:
        self.account_repo.get.side_effect = lambda account_id: None
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=generate_object_id(),
            category_id=self.category_expense.id,
            amount=Decimal("10.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_transaction(payload)

    async def test_get_account_helper_missing(self) -> None:
        with self.assertRaises(EntityNotFoundError):
            await self.service._get_account(generate_object_id())

    async def test_create_transaction_missing_category(self) -> None:
        self.category_repo.get.side_effect = lambda _: None
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=generate_object_id(),
            amount=Decimal("10.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        with self.assertRaises(EntityNotFoundError):
            await self.service.create_transaction(payload)

    async def test_get_category_helper_missing(self) -> None:
        with self.assertRaises(EntityNotFoundError):
            await self.service._get_category(generate_object_id())

    async def test_create_transaction_transfer_requirements(self) -> None:
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_expense.id,
            amount=Decimal("50.00"),
            transaction_type=TransactionType.TRANSFER,
        )
        with self.assertRaises(ValidationAppError):
            await self.service.create_transaction(payload)
        payload.transfer_account_id = self.account.id
        with self.assertRaises(ValidationAppError):
            await self.service.create_transaction(payload)
        payload.transfer_account_id = self.transfer_account.id
        self.transfer_account = self.transfer_account.model_copy(update={"user_id": generate_object_id()})
        with self.assertRaises(ValidationAppError):
            await self.service.create_transaction(payload)

    async def test_create_transaction_budget_limit(self) -> None:
        budget = make_budget(
            user_id=self.user.id,
            category_id=self.category_expense.id,
            amount=Decimal("300.00"),
        )
        self.budget_repo.list.return_value = [budget]
        self.transaction_repo.sum_for_category_period.return_value = Decimal("250.00")
        payload = TransactionCreate(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_expense.id,
            amount=Decimal("100.00"),
            transaction_type=TransactionType.EXPENSE,
        )
        with patch("src.services.transaction_service.build_transaction", return_value=self.transaction):
            with self.assertRaises(ValidationAppError):
                await self.service.create_transaction(payload)

    async def test_list_transactions(self) -> None:
        items = await self.service.list_transactions(
            user_id=self.user.id,
            account_id=self.account.id,
            category_id=self.category_expense.id,
            transaction_type=self.transaction.transaction_type,
            transfer_account_id=self.transfer_account.id,
            date_from=UTC_NOW - timedelta(days=1),
            date_to=UTC_NOW + timedelta(days=1),
        )
        self.assertEqual(len(items), 1)

    async def test_get_transaction_missing(self) -> None:
        self.transaction_repo.get.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.get_transaction(self.transaction.id)

    async def test_update_transaction_validates_payload(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.update_transaction(self.transaction.id, TransactionUpdate())

    async def test_update_transaction_adjusts_balance_on_amount_change(self) -> None:
        updated_txn = self.transaction.model_copy(update={"amount": Decimal("250.00")})
        self.transaction_repo.update.return_value = updated_txn
        payload = TransactionUpdate(amount=Decimal("250.00"))
        await self.service.update_transaction(self.transaction.id, payload)
        self.account_service.adjust_balance.assert_awaited()

    async def test_update_transaction_missing_after_repo_call(self) -> None:
        self.transaction_repo.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.update_transaction(
                self.transaction.id,
                TransactionUpdate(description="Nada"),
            )

    async def test_delete_transaction_reverts_balance(self) -> None:
        self.transaction_repo.delete.return_value = True
        await self.service.delete_transaction(self.transaction.id)
        self.account_service.adjust_balance.assert_awaited_with(self.account.id, self.transaction.amount)

    async def test_delete_transaction_not_found(self) -> None:
        self.transaction_repo.delete.return_value = False
        with self.assertRaises(EntityNotFoundError):
            await self.service.delete_transaction(self.transaction.id)

    async def test_apply_balance_delta_handles_income_and_transfer(self) -> None:
        income_txn = self.transaction.model_copy(update={"transaction_type": TransactionType.INCOME})
        await self.service._apply_balance_delta(income_txn, Decimal("100.00"))
        self.account_service.adjust_balance.assert_awaited_with(self.account.id, Decimal("100.00"))

        transfer_txn = self.transaction.model_copy(
            update={
                "transaction_type": TransactionType.TRANSFER,
                "transfer_account_id": self.transfer_account.id,
            }
        )
        await self.service._apply_balance_delta(transfer_txn, Decimal("20.00"))
        self.assertGreaterEqual(self.account_service.adjust_balance.await_count, 2)

        broken_transfer = transfer_txn.model_copy(update={"transfer_account_id": None})
        with self.assertRaises(ValidationAppError):
            await self.service._apply_balance_delta(broken_transfer, Decimal("10.00"))
        await self.service._apply_balance_delta(self.transaction, Decimal("0"))

    async def test_ensure_budget_allows_with_budget(self) -> None:
        budget = make_budget(
            user_id=self.user.id,
            category_id=self.category_expense.id,
            amount=Decimal("400.00"),
        )
        self.budget_repo.list.return_value = [budget]
        self.transaction_repo.sum_for_category_period.return_value = Decimal("200.00")
        await self.service._ensure_budget_allows(
            self.transaction,
            exclude_amount=Decimal("0"),
        )

    async def test_ensure_budget_allows_ignores_income_transactions(self) -> None:
        income_txn = self.transaction.model_copy(update={"transaction_type": TransactionType.INCOME})
        await self.service._ensure_budget_allows(income_txn, exclude_amount=Decimal("0"))


class ReportServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.transaction_repo = AsyncMock()
        self.category_repo = AsyncMock()
        self.budget_repo = AsyncMock()
        self.service = ReportService(
            self.transaction_repo,
            self.category_repo,
            self.budget_repo,
        )
        self.user = make_user()
        self.category = make_category(user_id=self.user.id)
        self.budget = make_budget(user_id=self.user.id, category_id=self.category.id)

    async def test_monthly_summary_builds_response(self) -> None:
        summary_item = {
            "category_id": self.category.id,
            "transaction_type": TransactionType.EXPENSE.value,
            "total": Decimal("200.00"),
            "count": 2,
        }
        self.transaction_repo.aggregate_monthly_summary.return_value = [summary_item]
        self.category_repo.get.return_value = self.category
        self.budget_repo.list.return_value = [self.budget]

        summary = await self.service.monthly_summary(self.user.id, 2024, 6)
        self.assertEqual(summary.totals_by_type[TransactionType.EXPENSE], Decimal("200.00"))
        self.assertEqual(summary.categories[0].budget_remaining, Decimal("300.00"))

    async def test_monthly_summary_missing_category(self) -> None:
        self.transaction_repo.aggregate_monthly_summary.return_value = [
            {
                "category_id": self.category.id,
                "transaction_type": TransactionType.EXPENSE.value,
                "total": Decimal("50.00"),
                "count": 1,
            }
        ]
        self.category_repo.get.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.monthly_summary(self.user.id, 2024, 6)


class UserServiceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.repository = AsyncMock()
        self.service = UserService(self.repository)
        self.user = make_user()

    async def test_create_user_enforces_unique_email(self) -> None:
        self.repository.list.return_value = []
        with patch("src.services.user_service.build_user", return_value=self.user):
            result = await self.service.create_user(UserCreate(name="Teste", email="teste@example.com"))
        self.repository.create.assert_awaited_once()
        self.assertEqual(result.id, self.user.id)

        self.repository.list.return_value = [self.user]
        with self.assertRaises(EntityAlreadyExistsError):
            await self.service.create_user(UserCreate(name="Outro", email="teste@example.com"))

    async def test_list_users(self) -> None:
        self.repository.list.return_value = [self.user]
        results = await self.service.list_users(
            name="Teste",
            email="servico@example.com",
            default_currency=self.user.default_currency,
        )
        self.assertEqual(len(results), 1)

    async def test_get_user_missing(self) -> None:
        self.repository.get.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.get_user(self.user.id)

    async def test_get_user_success(self) -> None:
        self.repository.get.return_value = self.user
        result = await self.service.get_user(self.user.id)
        self.assertEqual(result.id, self.user.id)

    async def test_update_user_requires_payload(self) -> None:
        with self.assertRaises(ValidationAppError):
            await self.service.update_user(self.user.id, UserUpdate())
        self.repository.update.return_value = None
        with self.assertRaises(EntityNotFoundError):
            await self.service.update_user(self.user.id, UserUpdate(name="Atual"))
        updated = self.user.model_copy(update={"name": "Atual"})
        self.repository.update.return_value = updated
        result = await self.service.update_user(self.user.id, UserUpdate(name="Atual"))
        self.assertEqual(result.name, "Atual")

    async def test_delete_user_missing(self) -> None:
        self.repository.delete.return_value = False
        with self.assertRaises(EntityNotFoundError):
            await self.service.delete_user(self.user.id)


class TestsPackageImportTest(unittest.TestCase):
    def test_tests_init_reinserts_root_path(self) -> None:
        import tests

        root = tests.ROOT_DIR
        if str(root) in sys.path:
            sys.path.remove(str(root))
        spec = importlib.util.spec_from_file_location("tests_copy", tests.__file__)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        self.assertIn(str(root), sys.path)
