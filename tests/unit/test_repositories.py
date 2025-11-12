"""Testes unitários focados nos repositórios Mongo e in-memory."""

from __future__ import annotations

import asyncio
import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import patch

from bson import ObjectId
from bson.decimal128 import Decimal128

from src.models.account import Account
from src.models.budget import Budget
from src.models.category import Category
from src.models.common import generate_object_id
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import Transaction
from src.models.user import User
from src.repositories.account_repository import (
    AccountRepository,
    InMemoryAccountRepository,
    _account_to_document,
)
from src.repositories.budget_repository import (
    BudgetRepository,
    InMemoryBudgetRepository,
    _budget_to_document,
)
from src.repositories.category_repository import (
    CategoryRepository,
    InMemoryCategoryRepository,
    _category_to_document,
)
from src.repositories.mongo_compat import ensure_motor_dependencies
from src.repositories.transaction_repository import (
    InMemoryTransactionRepository,
    TransactionRepository,
    _transaction_to_document,
)
from src.repositories.user_repository import (
    InMemoryUserRepository,
    UserRepository,
    _user_to_document,
)
from src.utils.exceptions import EntityAlreadyExistsError


UTC_NOW = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)


def sample_account(**overrides: object) -> Account:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "name": "Conta Repo",
        "account_type": AccountType.CHECKING,
        "currency": CurrencyCode.BRL,
        "description": "Conta usada nos testes",
        "minimum_balance": Decimal("10.00"),
        "balance": Decimal("100.00"),
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Account(**data)


def sample_budget(**overrides: object) -> Budget:
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


def sample_category(**overrides: object) -> Category:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "name": "Moradia",
        "category_type": CategoryType.EXPENSE,
        "description": "Categoria de teste",
        "parent_id": None,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Category(**data)


def sample_transaction(**overrides: object) -> Transaction:
    data = {
        "id": generate_object_id(),
        "user_id": generate_object_id(),
        "account_id": generate_object_id(),
        "category_id": generate_object_id(),
        "amount": Decimal("120.00"),
        "transaction_type": TransactionType.EXPENSE,
        "occurred_at": UTC_NOW,
        "description": "Despesa teste",
        "notes": None,
        "counterparty": None,
        "transfer_account_id": None,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return Transaction(**data)


def sample_user(**overrides: object) -> User:
    data = {
        "id": generate_object_id(),
        "name": "Usuário Repo",
        "email": "user.repo@example.com",
        "default_currency": CurrencyCode.BRL,
        "created_at": UTC_NOW,
        "updated_at": UTC_NOW,
    }
    data.update(overrides)
    return User(**data)


class FakeAsyncCursor:
    """Cursor assíncrono simples usado para simular motor."""

    def __init__(self, items: list[dict[str, object]], *, to_list_result: list[dict[str, object]] | None = None):
        self._items = list(items)
        self._to_list_result = list(to_list_result) if to_list_result is not None else list(items)
        self._iter = iter(self._items)
        self.sort_calls: list[tuple[tuple, dict]] = []

    def sort(self, *args: object, **kwargs: object) -> "FakeAsyncCursor":
        self.sort_calls.append((args, kwargs))
        return self

    def __aiter__(self) -> "FakeAsyncCursor":
        self._iter = iter(self._items)
        return self

    async def __anext__(self) -> dict[str, object]:
        try:
            return next(self._iter)
        except StopIteration:
            raise StopAsyncIteration

    async def to_list(self, length: int) -> list[dict[str, object]]:
        return self._to_list_result[:length]


class FakeCollection:
    """Coleção simulada com filas configuráveis para cada operação."""

    def __init__(self) -> None:
        self.inserted_documents: list[dict[str, object]] = []
        self.created_indexes: list[tuple[object, tuple, dict]] = []
        self.find_one_queue: list[dict[str, object] | None] = []
        self.find_results_queue: list[list[dict[str, object]]] = []
        self.aggregate_queue: list[dict[str, object]] = []
        self.find_one_and_update_result: dict[str, object] | None = None
        self.delete_result = 0
        self.count_documents_result = 0
        self.last_find_query: dict[str, object] | None = None
        self.last_find_one_query: dict[str, object] | None = None
        self.last_update_filter: dict[str, object] | None = None
        self.last_update_payload: dict[str, object] | None = None
        self.last_delete_query: dict[str, object] | None = None
        self.last_count_query: dict[str, object] | None = None
        self.last_pipeline: list[dict[str, object]] | None = None

    def queue_find_one(self, *documents: dict[str, object] | None) -> None:
        self.find_one_queue.extend(documents)

    def queue_find_results(self, *batches: list[dict[str, object]]) -> None:
        for batch in batches:
            self.find_results_queue.append(list(batch))

    def queue_aggregate(
        self,
        *,
        iter_items: list[dict[str, object]] | None = None,
        to_list_result: list[dict[str, object]] | None = None,
    ) -> None:
        self.aggregate_queue.append(
            {
                "iter_items": list(iter_items or []),
                "to_list_result": list(to_list_result) if to_list_result is not None else None,
            }
        )

    async def insert_one(self, document: dict[str, object]) -> None:
        self.inserted_documents.append(document)

    async def find_one(self, query: dict[str, object]) -> dict[str, object] | None:
        self.last_find_one_query = query
        if self.find_one_queue:
            return self.find_one_queue.pop(0)
        return None

    def find(self, query: dict[str, object]) -> FakeAsyncCursor:
        self.last_find_query = query
        batch = self.find_results_queue.pop(0) if self.find_results_queue else []
        return FakeAsyncCursor(batch)

    async def find_one_and_update(
        self,
        filter_query: dict[str, object],
        update: dict[str, object],
        *,
        return_document: object,
    ) -> dict[str, object] | None:
        self.last_update_filter = filter_query
        self.last_update_payload = update
        return self.find_one_and_update_result

    async def delete_one(self, query: dict[str, object]) -> SimpleNamespace:
        self.last_delete_query = query
        return SimpleNamespace(deleted_count=self.delete_result)

    async def create_index(self, spec: object, *args: object, **kwargs: object) -> None:
        self.created_indexes.append((spec, args, kwargs))

    async def count_documents(self, query: dict[str, object], limit: int | None = None) -> int:
        self.last_count_query = query
        return self.count_documents_result

    def aggregate(self, pipeline: list[dict[str, object]]) -> FakeAsyncCursor:
        self.last_pipeline = pipeline
        if self.aggregate_queue:
            config = self.aggregate_queue.pop(0)
        else:
            config = {"iter_items": [], "to_list_result": None}
        return FakeAsyncCursor(
            config.get("iter_items", []),
            to_list_result=config.get("to_list_result"),
        )


class FakeDatabase:
    """Banco que sempre retorna a mesma coleção simulada."""

    def __init__(self, collection: FakeCollection) -> None:
        self.collection = collection
        self.requested_names: list[str] = []

    def get_collection(self, name: str) -> FakeCollection:
        self.requested_names.append(name)
        return self.collection


class AccountRepositoryMongoTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.patch = patch("src.repositories.account_repository.ensure_motor_dependencies", autospec=True)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.collection = FakeCollection()
        self.repo = AccountRepository(FakeDatabase(self.collection))
        self.account = sample_account()
        self.document = _account_to_document(self.account)

    async def test_create_runs_index_once_and_inserts_document(self) -> None:
        await self.repo.create(self.account)
        await self.repo.create(self.account)
        self.assertEqual(len(self.collection.created_indexes), 3)
        self.assertEqual(len(self.collection.inserted_documents), 2)

    async def test_get_returns_account_and_none(self) -> None:
        self.collection.queue_find_one(self.document, None)
        account = await self.repo.get(self.account.id)
        self.assertEqual(account.id, self.account.id)
        missing = await self.repo.get(generate_object_id())
        self.assertIsNone(missing)

    async def test_list_applies_filters(self) -> None:
        self.collection.queue_find_results([self.document])
        accounts = await self.repo.list(
            user_id=self.account.user_id,
            account_type=self.account.account_type,
            currency=self.account.currency,
            name="repo",
        )
        self.assertEqual(len(accounts), 1)
        query = self.collection.last_find_query
        self.assertIsInstance(query["user_id"], ObjectId)
        self.assertIn("$regex", query["name"])

    async def test_update_handles_empty_payload_and_updates_balance(self) -> None:
        self.collection.queue_find_one(self.document)
        current = await self.repo.update(self.account.id, {})
        self.assertEqual(current.id, self.account.id)

        updated_doc = dict(self.document)
        updated_doc["balance"] = Decimal128("150.00")
        self.collection.find_one_and_update_result = updated_doc
        result = await self.repo.update(self.account.id, {"balance": Decimal("150.00")})
        self.assertEqual(result.balance, Decimal("150.00"))
        balance_payload = self.collection.last_update_payload["$set"]["balance"]
        self.assertIsInstance(balance_payload, Decimal128)

        new_user_id = generate_object_id()
        self.collection.find_one_and_update_result = self.document
        await self.repo.update(self.account.id, {"user_id": new_user_id})
        converted_user = self.collection.last_update_payload["$set"]["user_id"]
        self.assertIsInstance(converted_user, ObjectId)

        self.collection.find_one_and_update_result = None
        missing = await self.repo.update(self.account.id, {"name": "Nova"})
        self.assertIsNone(missing)

    async def test_delete_returns_flags(self) -> None:
        self.collection.delete_result = 1
        self.assertTrue(await self.repo.delete(self.account.id))
        self.collection.delete_result = 0
        self.assertFalse(await self.repo.delete(self.account.id))


class InMemoryAccountRepositoryTest(unittest.IsolatedAsyncioTestCase):
    async def test_filters_update_and_delete(self) -> None:
        repo = InMemoryAccountRepository()
        user_id = generate_object_id()
        account_a = sample_account(name="Conta Azul", currency=CurrencyCode.USD, user_id=user_id)
        account_b = sample_account(
            name="Conta Vermelha",
            account_type=AccountType.CREDIT_CARD,
            user_id=user_id,
            currency=CurrencyCode.EUR,
        )
        await repo.create(account_a)
        await repo.create(account_b)

        filtered = await repo.list(
            user_id=user_id,
            currency=CurrencyCode.USD,
            name="azul",
            account_type=account_a.account_type,
        )
        self.assertEqual([acct.id for acct in filtered], [account_a.id])

        updated = await repo.update(account_a.id, {"name": "Conta Azul Atualizada"})
        self.assertEqual(updated.name, "Conta Azul Atualizada")
        self.assertIsNone(await repo.update("missing", {"name": "Nada"}))

        self.assertTrue(await repo.delete(account_a.id))
        self.assertFalse(await repo.delete("missing"))


class BudgetRepositoryMongoTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.patch = patch("src.repositories.budget_repository.ensure_motor_dependencies", autospec=True)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.collection = FakeCollection()
        self.repo = BudgetRepository(FakeDatabase(self.collection))
        self.budget = sample_budget()
        self.document = _budget_to_document(self.budget)

    async def test_crud_and_find_by_period(self) -> None:
        await self.repo.create(self.budget)
        self.assertEqual(len(self.collection.created_indexes), 1)

        self.collection.queue_find_one(self.document, None)
        fetched = await self.repo.get(self.budget.id)
        self.assertEqual(fetched.id, self.budget.id)
        self.assertIsNone(await self.repo.get(generate_object_id()))

        self.collection.queue_find_results([self.document])
        items = await self.repo.list(
            user_id=self.budget.user_id,
            category_id=self.budget.category_id,
            year=self.budget.year,
            month=self.budget.month,
        )
        self.assertEqual(len(items), 1)

        self.collection.queue_find_one(self.document)
        copy_budget = await self.repo.update(self.budget.id, {})
        self.assertEqual(copy_budget.id, self.budget.id)

        updated_doc = dict(self.document)
        updated_doc["amount"] = Decimal128("700.00")
        self.collection.find_one_and_update_result = updated_doc
        updated = await self.repo.update(self.budget.id, {"amount": Decimal("700.00")})
        self.assertEqual(updated.amount, Decimal("700.00"))

        new_user = generate_object_id()
        new_category = generate_object_id()
        self.collection.find_one_and_update_result = self.document
        await self.repo.update(
            self.budget.id,
            {"user_id": new_user, "category_id": new_category},
        )
        payload = self.collection.last_update_payload["$set"]
        self.assertIsInstance(payload["user_id"], ObjectId)
        self.assertIsInstance(payload["category_id"], ObjectId)

        self.collection.find_one_and_update_result = None
        self.assertIsNone(await self.repo.update(self.budget.id, {"amount": Decimal("800.00")}))

        self.collection.delete_result = 1
        self.assertTrue(await self.repo.delete(self.budget.id))

        self.collection.queue_find_one(self.document, None)
        match = await self.repo.find_by_period(
            user_id=self.budget.user_id,
            category_id=self.budget.category_id,
            year=self.budget.year,
            month=self.budget.month,
        )
        self.assertEqual(match.id, self.budget.id)
        self.assertIsNone(
            await self.repo.find_by_period(
                user_id=self.budget.user_id,
                category_id=self.budget.category_id,
                year=self.budget.year,
                month=self.budget.month,
            )
        )


class InMemoryBudgetRepositoryTest(unittest.IsolatedAsyncioTestCase):
    async def test_filters_update_delete_and_find_by_period(self) -> None:
        repo = InMemoryBudgetRepository()
        user_id = generate_object_id()
        category_id = generate_object_id()
        budget = sample_budget(user_id=user_id, category_id=category_id, year=2024, month=5)
        await repo.create(budget)

        results = await repo.list(user_id=user_id, year=2024)
        self.assertEqual(len(results), 1)

        updated = await repo.update(budget.id, {"amount": Decimal("900.00")})
        self.assertEqual(updated.amount, Decimal("900.00"))
        self.assertIsNone(await repo.update("missing", {"amount": Decimal("1.00")}))

        found = await repo.find_by_period(user_id=user_id, category_id=category_id, year=2024, month=5)
        self.assertIsNotNone(found)

        self.assertTrue(await repo.delete(budget.id))
        self.assertFalse(await repo.delete(budget.id))


class CategoryRepositoryMongoTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.patch = patch("src.repositories.category_repository.ensure_motor_dependencies", autospec=True)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.collection = FakeCollection()
        self.repo = CategoryRepository(FakeDatabase(self.collection))
        self.parent_id = generate_object_id()
        self.category = sample_category(parent_id=self.parent_id)
        self.document = _category_to_document(self.category)

    async def test_list_with_filters_and_update_delete(self) -> None:
        await self.repo.create(self.category)
        await self.repo.create(sample_category(user_id=self.category.user_id))
        self.assertEqual(len(self.collection.created_indexes), 3)

        self.collection.queue_find_one(None)
        self.assertIsNone(await self.repo.get(generate_object_id()))

        self.collection.queue_find_results([self.document])
        items = await self.repo.list(
            user_id=self.category.user_id,
            category_type=self.category.category_type,
            parent_id=self.parent_id,
            name="mora",
        )
        self.assertEqual(len(items), 1)
        self.assertIsInstance(self.collection.last_find_query["parent_id"], ObjectId)

        self.collection.queue_find_results([self.document])
        await self.repo.list(parent_id=None)
        self.assertIn("parent_id", self.collection.last_find_query)

        self.collection.queue_find_one(self.document)
        base = await self.repo.update(self.category.id, {})
        self.assertEqual(base.id, self.category.id)

        updated_doc = dict(self.document)
        updated_doc["name"] = "Refeições"
        self.collection.find_one_and_update_result = updated_doc
        updated = await self.repo.update(self.category.id, {"name": "Refeições"})
        self.assertEqual(updated.name, "Refeições")

        new_user = generate_object_id()
        new_parent = generate_object_id()
        self.collection.find_one_and_update_result = self.document
        await self.repo.update(self.category.id, {"user_id": new_user, "parent_id": new_parent})
        payload = self.collection.last_update_payload["$set"]
        self.assertIsInstance(payload["user_id"], ObjectId)
        self.assertIsInstance(payload["parent_id"], ObjectId)

        self.collection.find_one_and_update_result = self.document
        await self.repo.update(self.category.id, {"parent_id": None})

        self.collection.find_one_and_update_result = None
        self.assertIsNone(await self.repo.update(self.category.id, {"name": "X"}))

        self.collection.delete_result = 1
        self.assertTrue(await self.repo.delete(self.category.id))


class InMemoryCategoryRepositoryTest(unittest.IsolatedAsyncioTestCase):
    async def test_parent_filters_and_update_delete(self) -> None:
        repo = InMemoryCategoryRepository()
        user_id = generate_object_id()
        parent_id = generate_object_id()
        child_id = generate_object_id()
        parent = sample_category(id=parent_id, name="Pai", user_id=user_id)
        child = sample_category(id=child_id, parent_id=parent_id, user_id=user_id, name="Filho")
        await repo.create(parent)
        await repo.create(child)

        results = await repo.list(
            user_id=user_id,
            category_type=child.category_type,
            parent_id=parent_id,
            name="filh",
        )
        self.assertEqual([cat.id for cat in results], [child_id])

        empty_parent = await repo.list(parent_id=None)
        self.assertTrue(empty_parent)

        updated = await repo.update(child.id, {"name": "Filho Atualizado"})
        self.assertEqual(updated.name, "Filho Atualizado")
        self.assertTrue(await repo.delete(child_id))
        self.assertIsNone(await repo.update("missing", {"name": "Nada"}))


class TransactionRepositoryMongoTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.patch = patch("src.repositories.transaction_repository.ensure_motor_dependencies", autospec=True)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.collection = FakeCollection()
        self.repo = TransactionRepository(FakeDatabase(self.collection))
        self.transaction = sample_transaction(transfer_account_id=generate_object_id())
        self.document = _transaction_to_document(self.transaction)

    async def test_full_workflow(self) -> None:
        await self.repo.create(self.transaction)
        plain_transaction = sample_transaction(
            user_id=self.transaction.user_id,
            account_id=self.transaction.account_id,
            category_id=self.transaction.category_id,
        )
        await self.repo.create(plain_transaction)
        self.assertEqual(len(self.collection.created_indexes), 4)

        self.collection.queue_find_one(self.document, None)
        fetched = await self.repo.get(self.transaction.id)
        self.assertEqual(fetched.id, self.transaction.id)
        self.assertIsNone(await self.repo.get(generate_object_id()))

        later_doc = dict(self.document)
        later_doc["occurred_at"] = UTC_NOW + timedelta(days=1)
        self.collection.queue_find_results([later_doc])
        items = await self.repo.list(
            user_id=self.transaction.user_id,
            account_id=self.transaction.account_id,
            category_id=self.transaction.category_id,
            transaction_type=self.transaction.transaction_type,
            transfer_account_id=self.transaction.transfer_account_id,
            date_from=UTC_NOW - timedelta(days=1),
            date_to=UTC_NOW + timedelta(days=1),
        )
        self.assertEqual(len(items), 1)
        self.assertIn("$gte", self.collection.last_find_query["occurred_at"])

        updated_doc = dict(self.document)
        updated_doc["amount"] = Decimal128("200.00")
        self.collection.find_one_and_update_result = updated_doc
        updated = await self.repo.update(self.transaction.id, {"amount": Decimal("200.00")})
        self.assertEqual(updated.amount, Decimal("200.00"))

        self.collection.queue_find_one(self.document)
        copy_current = await self.repo.update(self.transaction.id, {})
        self.assertEqual(copy_current.id, self.transaction.id)

        self.collection.find_one_and_update_result = None
        self.assertIsNone(await self.repo.update(self.transaction.id, {"amount": Decimal("300.00")}))

        self.collection.delete_result = 1
        self.assertTrue(await self.repo.delete(self.transaction.id))

        self.collection.count_documents_result = 1
        self.assertTrue(await self.repo.exists_for_account(self.transaction.account_id))

        self.collection.count_documents_result = 0
        self.assertFalse(
            await self.repo.exists_for_category(
                self.transaction.category_id,
                user_id=self.transaction.user_id,
                year=2024,
                month=12,
            )
        )

        self.collection.count_documents_result = 0
        await self.repo.exists_for_category(
            self.transaction.category_id,
            user_id=self.transaction.user_id,
            year=2024,
            month=6,
        )

        summary_item = {
            "category_id": ObjectId(self.transaction.category_id),
            "transaction_type": self.transaction.transaction_type,
            "total": Decimal128("50.00"),
            "count": 2,
        }
        self.collection.queue_aggregate(iter_items=[summary_item])
        summary = await self.repo.aggregate_monthly_summary(self.transaction.user_id, year=2024, month=6)
        self.assertEqual(summary[0]["total"], Decimal("50.00"))

        self.collection.queue_aggregate(to_list_result=[{"total": Decimal128("90.00")}])
        total = await self.repo.sum_for_category_period(
            user_id=self.transaction.user_id,
            category_id=self.transaction.category_id,
            year=2024,
            month=6,
        )
        self.assertEqual(total, Decimal("90.00"))

        self.collection.queue_aggregate(to_list_result=[{"total": 123}])
        generic_total = await self.repo.sum_for_category_period(
            user_id=self.transaction.user_id,
            category_id=self.transaction.category_id,
            year=2024,
            month=6,
        )
        self.assertEqual(generic_total, Decimal("123"))

        self.collection.queue_aggregate(to_list_result=[])
        zero_total = await self.repo.sum_for_category_period(
            user_id=self.transaction.user_id,
            category_id=self.transaction.category_id,
            year=2024,
            month=7,
        )
        self.assertEqual(zero_total, Decimal("0"))

        conversions = {
            "user_id": generate_object_id(),
            "account_id": generate_object_id(),
            "category_id": generate_object_id(),
            "transfer_account_id": generate_object_id(),
            "amount": Decimal("33.00"),
        }
        self.collection.find_one_and_update_result = self.document
        await self.repo.update(self.transaction.id, conversions)
        payload = self.collection.last_update_payload["$set"]
        self.assertIsInstance(payload["user_id"], ObjectId)
        self.assertIsInstance(payload["account_id"], ObjectId)
        self.assertIsInstance(payload["category_id"], ObjectId)
        self.assertIsInstance(payload["transfer_account_id"], ObjectId)
        self.assertIsInstance(payload["amount"], Decimal128)

        await self.repo._ensure_indexes()


class InMemoryTransactionRepositoryTest(unittest.IsolatedAsyncioTestCase):
    async def test_filters_and_aggregations(self) -> None:
        repo = InMemoryTransactionRepository()
        income_id = generate_object_id()
        expense_id = generate_object_id()
        user_id = "1" * 24
        other_user_id = "2" * 24
        foreign_user_id = "3" * 24
        category_common = generate_object_id()
        txn_income = sample_transaction(
            id=income_id,
            transaction_type=TransactionType.INCOME,
            amount=Decimal("500.00"),
            occurred_at=UTC_NOW,
            user_id=user_id,
            category_id=category_common,
        )
        txn_expense = sample_transaction(
            id=expense_id,
            category_id=generate_object_id(),
            transaction_type=TransactionType.EXPENSE,
            amount=Decimal("200.00"),
            occurred_at=UTC_NOW + timedelta(days=1),
            user_id=user_id,
            transfer_account_id=generate_object_id(),
        )
        txn_other_user = sample_transaction(
            user_id=other_user_id,
            category_id=category_common,
            occurred_at=UTC_NOW,
        )
        txn_other_month = sample_transaction(
            user_id=user_id,
            category_id=category_common,
            occurred_at=UTC_NOW + timedelta(days=35),
        )
        await repo.create(txn_income)
        await repo.create(txn_expense)
        await repo.create(txn_other_user)
        await repo.create(txn_other_month)

        listed = await repo.list(
            user_id=user_id,
            account_id=txn_income.account_id,
            category_id=txn_income.category_id,
            transaction_type=txn_income.transaction_type,
            date_from=UTC_NOW - timedelta(days=1),
            date_to=UTC_NOW + timedelta(days=2),
        )
        self.assertEqual(len(listed), 1)
        await repo.list(transfer_account_id=txn_expense.transfer_account_id)

        updated = await repo.update(income_id, {"amount": Decimal("600.00")})
        self.assertEqual(updated.amount, Decimal("600.00"))
        self.assertIsNone(await repo.update("missing", {"amount": Decimal("1.00")}))

        self.assertTrue(await repo.exists_for_account(txn_income.account_id))
        self.assertTrue(
            await repo.exists_for_category(
                txn_income.category_id,
                user_id=txn_income.user_id,
                year=UTC_NOW.year,
                month=UTC_NOW.month,
            )
        )
        await repo.exists_for_category(
            txn_income.category_id,
            user_id=txn_income.user_id,
            year=UTC_NOW.year + 1,
            month=UTC_NOW.month,
        )
        await repo.exists_for_category(
            txn_income.category_id,
            user_id=txn_income.user_id,
            year=UTC_NOW.year,
            month=UTC_NOW.month + 1,
        )
        await repo.exists_for_category(
            txn_income.category_id,
            user_id=foreign_user_id,
            year=UTC_NOW.year,
            month=UTC_NOW.month,
        )
        summary = await repo.aggregate_monthly_summary(
            txn_income.user_id,
            year=UTC_NOW.year,
            month=UTC_NOW.month,
        )
        self.assertTrue(summary)

        total = await repo.sum_for_category_period(
            user_id=txn_income.user_id,
            category_id=txn_income.category_id,
            year=UTC_NOW.year,
            month=UTC_NOW.month,
        )
        self.assertEqual(total, Decimal("600.00"))

        self.assertTrue(await repo.delete(income_id))


class UserRepositoryMongoTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.patch = patch("src.repositories.user_repository.ensure_motor_dependencies", autospec=True)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.collection = FakeCollection()
        self.repo = UserRepository(FakeDatabase(self.collection))
        self.user = sample_user()
        self.document = _user_to_document(self.user)

    async def test_crud_and_filters(self) -> None:
        await self.repo.create(self.user)
        self.assertEqual(len(self.collection.created_indexes), 2)

        self.collection.queue_find_one(self.document, self.document, None)
        user = await self.repo.get(self.user.id)
        self.assertEqual(user.id, self.user.id)
        email_user = await self.repo.get_by_email(self.user.email.upper())
        self.assertEqual(email_user.id, self.user.id)
        self.assertIsNone(await self.repo.get(generate_object_id()))
        self.collection.queue_find_one(None)
        self.assertIsNone(await self.repo.get_by_email("missing@example.com"))

        self.collection.queue_find_results([self.document])
        listed = await self.repo.list(name="Usuário", email=self.user.email, default_currency=self.user.default_currency)
        self.assertEqual(len(listed), 1)

        self.collection.queue_find_one(self.document)
        snapshot = await self.repo.update(self.user.id, {})
        self.assertEqual(snapshot.id, self.user.id)

        updated_doc = dict(self.document)
        updated_doc["name"] = "Outro Nome"
        self.collection.find_one_and_update_result = updated_doc
        updated = await self.repo.update(self.user.id, {"name": "Outro Nome"})
        self.assertEqual(updated.name, "Outro Nome")

        self.collection.find_one_and_update_result = None
        self.assertIsNone(await self.repo.update(self.user.id, {"name": "Nada"}))

        self.collection.delete_result = 1
        self.assertTrue(await self.repo.delete(self.user.id))


class InMemoryUserRepositoryTest(unittest.IsolatedAsyncioTestCase):
    async def test_create_duplicates_filters_update_delete(self) -> None:
        repo = InMemoryUserRepository()
        user_id = generate_object_id()
        user = sample_user(id=user_id, email="dup@example.com")
        await repo.create(user)
        with self.assertRaises(EntityAlreadyExistsError):
            await repo.create(sample_user(id=user_id, email="other@example.com"))
        with self.assertRaises(EntityAlreadyExistsError):
            await repo.create(sample_user(id=generate_object_id(), email="dup@example.com"))

        users = await repo.list(email="dup@example.com", default_currency=user.default_currency)
        self.assertEqual(len(users), 1)
        filtered_by_name = await repo.list(name="usuário")
        self.assertEqual(len(filtered_by_name), 1)

        updated = await repo.update(user_id, {"name": "Novo"})
        self.assertEqual(updated.name, "Novo")
        self.assertTrue(await repo.delete(user_id))
        self.assertIsNone(await repo.update("missing", {"name": "Nada"}))


class FakeCollectionTest(unittest.TestCase):
    def test_fallbacks_without_queued_results(self) -> None:
        collection = FakeCollection()
        self.assertIsNone(asyncio.run(collection.find_one({})))
        cursor = collection.aggregate([])
        self.assertEqual([], asyncio.run(cursor.to_list(1)))


class MongoCompatTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.original = ensure_motor_dependencies.__globals__["_IMPORT_ERROR"]

    def tearDown(self) -> None:
        ensure_motor_dependencies.__globals__["_IMPORT_ERROR"] = self.original
        super().tearDown()

    def test_ensure_motor_dependencies_raises_when_import_error(self) -> None:
        ensure_motor_dependencies.__globals__["_IMPORT_ERROR"] = RuntimeError("missing deps")
        with self.assertRaises(RuntimeError):
            ensure_motor_dependencies()

    def test_ensure_motor_dependencies_no_error(self) -> None:
        ensure_motor_dependencies.__globals__["_IMPORT_ERROR"] = None
        ensure_motor_dependencies()
