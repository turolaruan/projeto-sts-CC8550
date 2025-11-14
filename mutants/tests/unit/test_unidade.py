"""Testes unitários cobrindo regras principais do sistema."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from decimal import Decimal
from unittest.mock import patch

from bson import ObjectId
from pydantic import ValidationError

from src.models.account import AccountCreate, AccountUpdate, build_account
from src.models.budget import BudgetCreate, BudgetUpdate, build_budget
from src.models.category import CategoryCreate, CategoryUpdate, build_category
from src.models.common import (
    ensure_object_id,
    generate_object_id,
    now_utc,
    strip_and_validate_non_empty,
)
from src.models.enums import (
    AccountType,
    CategoryType,
    CurrencyCode,
    TransactionType,
)
from src.models.transaction import TransactionCreate, TransactionUpdate, build_transaction
from src.models.user import UserCreate, UserUpdate, build_user
from src.utils.exceptions import AppException, EntityNotFoundError, ValidationAppError


class ModelTestCase(unittest.TestCase):
    """Fixture base class com IDs e timestamp compartilhados."""

    def setUp(self) -> None:
        super().setUp()
        self.user_id = "64f6d1250a1b2c3d4e5f6789"
        self.account_id = "65f6d1250a1b2c3d4e5f6789"
        self.category_id = "66f6d1250a1b2c3d4e5f6789"
        self.transaction_id = "67f6d1250a1b2c3d4e5f6789"
        self.fixed_now = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)


class CommonUtilitiesTest(ModelTestCase):
    def test_generate_object_id_returns_valid_hex(self) -> None:
        object_id = generate_object_id()
        self.assertEqual(len(object_id), 24)
        int(object_id, 16)  # Não gera exceção se for hexadecimal.

    def test_generate_object_id_produces_unique_values(self) -> None:
        first = generate_object_id()
        second = generate_object_id()
        self.assertNotEqual(first, second)

    def test_ensure_object_id_valid_returns_objectid(self) -> None:
        oid = ensure_object_id(self.user_id)
        self.assertIsInstance(oid, ObjectId)
        self.assertEqual(str(oid), self.user_id)

    def test_ensure_object_id_invalid_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            ensure_object_id("invalid_object_id")

    def test_now_utc_returns_timezone_aware_datetime(self) -> None:
        timestamp = now_utc()
        self.assertIsNotNone(timestamp.tzinfo)
        self.assertEqual(timestamp.tzinfo.utcoffset(timestamp), timezone.utc.utcoffset(timestamp))

    def test_strip_and_validate_non_empty_returns_trimmed_value(self) -> None:
        result = strip_and_validate_non_empty("  nome da conta  ", "name")
        self.assertEqual(result, "nome da conta")

    def test_strip_and_validate_non_empty_raises_for_empty_string(self) -> None:
        for raw_value in ("", "   ", "\n\t"):
            with self.subTest(raw_value=raw_value):
                with self.assertRaises(ValueError):
                    strip_and_validate_non_empty(raw_value, "field")


class EnumTestCases(ModelTestCase):
    def test_currency_code_choices_matches_members(self) -> None:
        self.assertEqual(CurrencyCode.choices(), [member.value for member in CurrencyCode])

    def test_account_type_values_expected(self) -> None:
        expected = {
            AccountType.CHECKING: "checking",
            AccountType.SAVINGS: "savings",
            AccountType.CREDIT_CARD: "credit_card",
            AccountType.CASH: "cash",
            AccountType.INVESTMENT: "investment",
        }
        for member, value in expected.items():
            with self.subTest(member=member):
                self.assertEqual(member.value, value)

    def test_category_type_values_expected(self) -> None:
        expected = {
            CategoryType.INCOME: "income",
            CategoryType.EXPENSE: "expense",
        }
        for member, value in expected.items():
            with self.subTest(member=member):
                self.assertEqual(member.value, value)

    def test_transaction_type_values_expected(self) -> None:
        expected = {
            TransactionType.INCOME: "income",
            TransactionType.EXPENSE: "expense",
            TransactionType.TRANSFER: "transfer",
        }
        for member, value in expected.items():
            with self.subTest(member=member):
                self.assertEqual(member.value, value)


class ExceptionHierarchyTest(ModelTestCase):
    def test_app_exception_stores_context_dict(self) -> None:
        exc = AppException("erro crítico", context={"entity": "account"})
        self.assertEqual(exc.message, "erro crítico")
        self.assertEqual(exc.context, {"entity": "account"})

    def test_entity_not_found_error_is_subclass_of_app_exception(self) -> None:
        exc = EntityNotFoundError("não encontrado")
        self.assertIsInstance(exc, AppException)
        self.assertEqual(str(exc), "não encontrado")

    def test_validation_app_error_defaults_to_empty_context(self) -> None:
        exc = ValidationAppError("dados inválidos")
        self.assertEqual(exc.context, {})


class AccountModelTest(ModelTestCase):
    def test_account_create_normalizes_minimum_balance(self) -> None:
        payload = AccountCreate(
            user_id=self.user_id,
            name="Conta Principal",
            account_type=AccountType.CHECKING,
            currency=CurrencyCode.USD,
            description="Conta corrente",
            minimum_balance=Decimal("10.999"),
            starting_balance=Decimal("100"),
        )
        self.assertEqual(payload.minimum_balance, Decimal("11.00"))

    def test_account_create_trims_name(self) -> None:
        payload = AccountCreate(
            user_id=self.user_id,
            name="   Carteira   ",
            account_type=AccountType.CASH,
            starting_balance=Decimal("0"),
        )
        self.assertEqual(payload.name, "Carteira")

    def test_account_create_rejects_blank_name(self) -> None:
        for invalid_name in ("", "   "):
            with self.subTest(invalid_name=invalid_name):
                with self.assertRaises(ValidationError):
                    AccountCreate(
                        user_id=self.user_id,
                        name=invalid_name,
                        account_type=AccountType.CHECKING,
                        starting_balance=Decimal("0"),
                    )

    def test_account_update_allows_partial_fields(self) -> None:
        update = AccountUpdate(description="Nova descrição")
        self.assertIsNone(update.name)
        self.assertEqual(update.description, "Nova descrição")

    def test_account_update_accepts_none_name(self) -> None:
        update = AccountUpdate(name=None)
        self.assertIsNone(update.name)

    def test_account_update_trims_non_empty_name(self) -> None:
        update = AccountUpdate(name="   Nova Conta   ")
        self.assertEqual(update.name, "Nova Conta")

    def test_account_update_normalizes_minimum_balance(self) -> None:
        update = AccountUpdate(minimum_balance=Decimal("50.155"))
        self.assertEqual(update.minimum_balance, Decimal("50.16"))

    def test_account_update_minimum_balance_none(self) -> None:
        update = AccountUpdate(minimum_balance=None)
        self.assertIsNone(update.minimum_balance)

    def test_build_account_generates_ids_and_timestamps(self) -> None:
        payload = AccountCreate(
            user_id=self.user_id,
            name="Conta XP",
            account_type=AccountType.INVESTMENT,
            currency=CurrencyCode.BRL,
            starting_balance=Decimal("150.251"),
        )
        with patch("src.models.account.generate_object_id", return_value=self.account_id), patch(
            "src.models.account.now_utc", return_value=self.fixed_now
        ):
            account = build_account(payload)
        self.assertEqual(account.id, self.account_id)
        self.assertEqual(account.created_at, self.fixed_now)
        self.assertEqual(account.updated_at, self.fixed_now)
        self.assertEqual(account.balance, Decimal("150.25"))

    def test_account_currency_defaults_to_brl(self) -> None:
        payload = AccountCreate(
            user_id=self.user_id,
            name="Conta Local",
            account_type=AccountType.CHECKING,
            starting_balance=Decimal("0"),
        )
        self.assertEqual(payload.currency, CurrencyCode.BRL)


class BudgetModelTest(ModelTestCase):
    def test_budget_create_amount_is_quantized(self) -> None:
        payload = BudgetCreate(
            user_id=self.user_id,
            category_id=self.category_id,
            year=2024,
            month=5,
            amount=Decimal("100.4567"),
        )
        self.assertEqual(payload.amount, Decimal("100.46"))

    def test_budget_update_quantizes_amount_when_present(self) -> None:
        update = BudgetUpdate(amount=Decimal("55.199"))
        self.assertEqual(update.amount, Decimal("55.20"))

    def test_budget_update_allows_none_amount(self) -> None:
        update = BudgetUpdate()
        self.assertIsNone(update.amount)

    def test_budget_update_with_explicit_none_amount(self) -> None:
        update = BudgetUpdate(amount=None)
        self.assertIsNone(update.amount)

    def test_budget_alert_percentage_default(self) -> None:
        payload = BudgetCreate(
            user_id=self.user_id,
            category_id=self.category_id,
            year=2024,
            month=6,
            amount=Decimal("400"),
        )
        self.assertEqual(payload.alert_percentage, 80)

    def test_build_budget_generates_ids_and_timestamps(self) -> None:
        payload = BudgetCreate(
            user_id=self.user_id,
            category_id=self.category_id,
            year=2024,
            month=1,
            amount=Decimal("200"),
            alert_percentage=90,
        )
        with patch("src.models.budget.generate_object_id", return_value=self.transaction_id), patch(
            "src.models.budget.now_utc", return_value=self.fixed_now
        ):
            budget = build_budget(payload)
        self.assertEqual(budget.id, self.transaction_id)
        self.assertEqual(budget.created_at, self.fixed_now)
        self.assertEqual(budget.updated_at, self.fixed_now)


class CategoryModelTest(ModelTestCase):
    def test_category_create_trims_name(self) -> None:
        payload = CategoryCreate(
            user_id=self.user_id,
            name="   Moradia   ",
            category_type=CategoryType.EXPENSE,
        )
        self.assertEqual(payload.name, "Moradia")

    def test_category_create_rejects_blank_name(self) -> None:
        with self.assertRaises(ValidationError):
            CategoryCreate(user_id=self.user_id, name="   ", category_type=CategoryType.EXPENSE)

    def test_category_update_allows_none_fields(self) -> None:
        update = CategoryUpdate(description="Atualizada")
        self.assertIsNone(update.name)
        self.assertEqual(update.description, "Atualizada")

    def test_category_update_accepts_none_name(self) -> None:
        update = CategoryUpdate(name=None)
        self.assertIsNone(update.name)

    def test_category_update_rejects_blank_name(self) -> None:
        with self.assertRaises(ValidationError):
            CategoryUpdate(name="   ")

    def test_build_category_respects_parent_id(self) -> None:
        payload = CategoryCreate(
            user_id=self.user_id,
            name="Investimentos",
            category_type=CategoryType.INCOME,
            parent_id=self.category_id,
        )
        with patch("src.models.category.generate_object_id", return_value=self.category_id), patch(
            "src.models.category.now_utc", return_value=self.fixed_now
        ):
            category = build_category(payload)
        self.assertEqual(category.parent_id, self.category_id)
        self.assertEqual(category.created_at, self.fixed_now)
        self.assertEqual(category.updated_at, self.fixed_now)


class TransactionModelTest(ModelTestCase):
    def _base_transaction_payload(self, **overrides: object) -> TransactionCreate:
        data = {
            "user_id": self.user_id,
            "account_id": self.account_id,
            "category_id": self.category_id,
            "amount": Decimal("100.999"),
            "transaction_type": TransactionType.EXPENSE,
            "description": "Compra supermercado",
        }
        data.update(overrides)
        return TransactionCreate(**data)

    def test_transaction_create_amount_quantized(self) -> None:
        payload = self._base_transaction_payload()
        self.assertEqual(payload.amount, Decimal("101.00"))

    def test_transaction_create_trims_description(self) -> None:
        payload = self._base_transaction_payload(description="   Aluguel   ")
        self.assertEqual(payload.description, "Aluguel")

    def test_transaction_create_allows_none_description(self) -> None:
        payload = self._base_transaction_payload(description=None)
        self.assertIsNone(payload.description)

    def test_transaction_create_rejects_blank_description(self) -> None:
        with self.assertRaises(ValidationError):
            self._base_transaction_payload(description="   ")

    def test_transaction_update_amount_quantized(self) -> None:
        update = TransactionUpdate(amount=Decimal("45.678"))
        self.assertEqual(update.amount, Decimal("45.68"))

    def test_transaction_update_allows_none_amount(self) -> None:
        update = TransactionUpdate(amount=None)
        self.assertIsNone(update.amount)

    def test_transaction_update_trims_description(self) -> None:
        update = TransactionUpdate(description="   Ajuste   ")
        self.assertEqual(update.description, "Ajuste")

    def test_transaction_update_accepts_none_description(self) -> None:
        update = TransactionUpdate(description=None)
        self.assertIsNone(update.description)

    def test_transaction_update_rejects_blank_description(self) -> None:
        with self.assertRaises(ValidationError):
            TransactionUpdate(description="   ")

    def test_build_transaction_normalizes_amount_and_sets_timestamps(self) -> None:
        payload = self._base_transaction_payload(amount=Decimal("78.199"), notes="obs", counterparty="Loja")
        with patch("src.models.transaction.generate_object_id", return_value=self.transaction_id), patch(
            "src.models.transaction.now_utc", return_value=self.fixed_now
        ):
            transaction = build_transaction(payload)
        self.assertEqual(transaction.id, self.transaction_id)
        self.assertEqual(transaction.amount, Decimal("78.20"))
        self.assertEqual(transaction.created_at, self.fixed_now)
        self.assertEqual(transaction.updated_at, self.fixed_now)

    def test_build_transaction_preserves_payload_fields(self) -> None:
        payload = self._base_transaction_payload(
            notes="comprovante",
            counterparty="Fornecedor X",
            transfer_account_id=self.account_id,
        )
        transaction = build_transaction(payload)
        self.assertEqual(transaction.notes, "comprovante")
        self.assertEqual(transaction.counterparty, "Fornecedor X")
        self.assertEqual(transaction.transfer_account_id, self.account_id)


class UserModelTest(ModelTestCase):
    def test_user_create_trims_name(self) -> None:
        payload = UserCreate(name="   Maria Silva   ", email="user@example.com")
        self.assertEqual(payload.name, "Maria Silva")

    def test_user_create_lowercases_email(self) -> None:
        payload = UserCreate(name="Carlos", email="USER@Example.COM")
        self.assertEqual(payload.email, "user@example.com")

    def test_user_update_allows_none_fields(self) -> None:
        update = UserUpdate()
        self.assertIsNone(update.name)
        self.assertIsNone(update.default_currency)

    def test_user_update_accepts_none_name(self) -> None:
        update = UserUpdate(name=None)
        self.assertIsNone(update.name)

    def test_user_update_rejects_blank_name(self) -> None:
        with self.assertRaises(ValidationError):
            UserUpdate(name="   ")

    def test_build_user_generates_id_and_timestamps(self) -> None:
        payload = UserCreate(name="Laura", email="laura@example.com", default_currency=CurrencyCode.EUR)
        with patch("src.models.user.generate_object_id", return_value=self.user_id), patch(
            "src.models.user.now_utc", return_value=self.fixed_now
        ):
            user = build_user(payload)
        self.assertEqual(user.id, self.user_id)
        self.assertEqual(user.created_at, self.fixed_now)
        self.assertEqual(user.updated_at, self.fixed_now)
