"""Testes de integração cobrindo fluxos completos do domínio."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone
from decimal import Decimal

from src.models.account import AccountCreate
from src.models.budget import BudgetCreate
from src.models.category import CategoryCreate
from src.models.common import generate_object_id
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import TransactionCreate
from src.models.user import UserCreate
from src.repositories.account_repository import InMemoryAccountRepository
from src.repositories.budget_repository import InMemoryBudgetRepository
from src.repositories.category_repository import InMemoryCategoryRepository
from src.repositories.transaction_repository import InMemoryTransactionRepository
from src.repositories.user_repository import InMemoryUserRepository
from src.services.account_service import AccountService
from src.services.budget_service import BudgetService
from src.services.category_service import CategoryService
from src.services.report_service import ReportService
from src.services.transaction_service import TransactionService
from src.services.user_service import UserService
from src.utils.exceptions import ValidationAppError


class FinanceIntegrationTest(unittest.IsolatedAsyncioTestCase):
    """Orquestra os serviços reais usando repositórios em memória."""

    async def asyncSetUp(self) -> None:
        self.user_repo = InMemoryUserRepository()
        self.account_repo = InMemoryAccountRepository()
        self.category_repo = InMemoryCategoryRepository()
        self.budget_repo = InMemoryBudgetRepository()
        self.transaction_repo = InMemoryTransactionRepository()

        self.user_service = UserService(self.user_repo)
        self.account_service = AccountService(
            self.account_repo,
            self.user_repo,
            self.transaction_repo,
        )
        self.category_service = CategoryService(
            self.category_repo,
            self.user_repo,
            self.transaction_repo,
            self.budget_repo,
        )
        self.budget_service = BudgetService(
            self.budget_repo,
            self.user_repo,
            self.category_repo,
            self.transaction_repo,
        )
        self.transaction_service = TransactionService(
            self.transaction_repo,
            self.account_service,
            self.account_repo,
            self.category_repo,
            self.user_repo,
            self.budget_repo,
        )
        self.report_service = ReportService(
            self.transaction_repo,
            self.category_repo,
            self.budget_repo,
        )
        self.default_date = datetime(2024, 6, 15, 12, 0, tzinfo=timezone.utc)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _unique_email(self, prefix: str = "user") -> str:
        return f"{prefix}.{generate_object_id()}@example.com"

    def _date(self, year: int, month: int, day: int) -> datetime:
        return datetime(year, month, day, 12, 0, tzinfo=timezone.utc)

    async def _create_user(self, *, name: str = "Usuário Integração") -> object:
        payload = UserCreate(
            name=name,
            email=self._unique_email(name.split()[0].lower()),
            default_currency=CurrencyCode.BRL,
        )
        return await self.user_service.create_user(payload)

    async def _create_account(
        self,
        user,
        *,
        name: str = "Conta Corrente",
        starting_balance: Decimal = Decimal("500.00"),
        minimum: Decimal = Decimal("0"),
        account_type: AccountType = AccountType.CHECKING,
    ):
        payload = AccountCreate(
            user_id=user.id,
            name=name,
            account_type=account_type,
            currency=CurrencyCode.BRL,
            description="Conta integrada",
            minimum_balance=minimum,
            starting_balance=starting_balance,
        )
        return await self.account_service.create_account(payload)

    async def _create_category(
        self,
        user,
        *,
        name: str = "Categoria",
        category_type: CategoryType = CategoryType.EXPENSE,
        parent_id: str | None = None,
    ):
        payload = CategoryCreate(
            user_id=user.id,
            name=name,
            category_type=category_type,
            description=None,
            parent_id=parent_id,
        )
        return await self.category_service.create_category(payload)

    async def _create_budget(
        self,
        user,
        category,
        *,
        amount: Decimal = Decimal("500.00"),
        year: int = 2024,
        month: int = 6,
    ):
        payload = BudgetCreate(
            user_id=user.id,
            category_id=category.id,
            year=year,
            month=month,
            amount=amount,
            alert_percentage=80,
        )
        return await self.budget_service.create_budget(payload)

    async def _create_transaction(
        self,
        user,
        account,
        category,
        *,
        amount: Decimal,
        transaction_type: TransactionType,
        description: str,
        occurred_at: datetime | None = None,
        transfer_account=None,
    ):
        payload = TransactionCreate(
            user_id=user.id,
            account_id=account.id,
            category_id=category.id,
            amount=amount,
            transaction_type=transaction_type,
            occurred_at=occurred_at or self.default_date,
            description=description,
            transfer_account_id=transfer_account.id if transfer_account else None,
        )
        return await self.transaction_service.create_transaction(payload)

    # ------------------------------------------------------------------
    # Test cases
    # ------------------------------------------------------------------
    async def test_user_creation_and_listing_flow(self) -> None:
        ana = await self._create_user(name="Ana Integração")
        await self._create_user(name="Bruno Integração")

        filtered = await self.user_service.list_users(name="Ana")
        self.assertEqual(1, len(filtered))

        fetched = await self.user_service.get_user(ana.id)
        self.assertEqual(ana.email, fetched.email)

    async def test_account_creation_persists_starting_balance(self) -> None:
        user = await self._create_user()
        account = await self._create_account(
            user,
            starting_balance=Decimal("350.00"),
            minimum=Decimal("50.00"),
        )

        stored = await self.account_service.get_account(account.id)
        self.assertEqual(Decimal("350.00"), stored.balance)

        accounts = await self.account_service.list_accounts(user_id=user.id)
        self.assertEqual([account.id], [item.id for item in accounts])

    async def test_income_transaction_updates_balance_and_listing(self) -> None:
        user = await self._create_user()
        income_category = await self._create_category(
            user,
            name="Salário",
            category_type=CategoryType.INCOME,
        )
        account = await self._create_account(user, starting_balance=Decimal("100.00"))

        transaction = await self._create_transaction(
            user,
            account,
            income_category,
            amount=Decimal("250.00"),
            transaction_type=TransactionType.INCOME,
            description="Pagamento mensal",
        )

        updated = await self.account_service.get_account(account.id)
        self.assertEqual(Decimal("350.00"), updated.balance)

        transactions = await self.transaction_service.list_transactions(user_id=user.id)
        self.assertEqual([transaction.id], [item.id for item in transactions])

    async def test_transfer_transaction_updates_both_accounts(self) -> None:
        user = await self._create_user()
        origin = await self._create_account(
            user,
            name="Conta Origem",
            starting_balance=Decimal("500.00"),
        )
        destination = await self._create_account(
            user,
            name="Conta Destino",
            starting_balance=Decimal("150.00"),
        )
        transfer_category = await self._create_category(
            user,
            name="Transferências",
            category_type=CategoryType.EXPENSE,
        )

        await self._create_transaction(
            user,
            origin,
            transfer_category,
            amount=Decimal("200.00"),
            transaction_type=TransactionType.TRANSFER,
            description="Envio entre contas",
            transfer_account=destination,
        )

        updated_origin = await self.account_service.get_account(origin.id)
        updated_destination = await self.account_service.get_account(destination.id)
        self.assertEqual(Decimal("300.00"), updated_origin.balance)
        self.assertEqual(Decimal("350.00"), updated_destination.balance)

    async def test_expense_transaction_respects_budget_limit(self) -> None:
        user = await self._create_user()
        account = await self._create_account(user, starting_balance=Decimal("400.00"))
        expense_category = await self._create_category(
            user,
            name="Mercado",
            category_type=CategoryType.EXPENSE,
        )
        await self._create_budget(
            user,
            expense_category,
            amount=Decimal("200.00"),
            year=2024,
            month=6,
        )

        await self._create_transaction(
            user,
            account,
            expense_category,
            amount=Decimal("150.00"),
            transaction_type=TransactionType.EXPENSE,
            description="Compra semanal",
            occurred_at=self._date(2024, 6, 5),
        )

        with self.assertRaises(ValidationAppError):
            await self._create_transaction(
                user,
                account,
                expense_category,
                amount=Decimal("100.00"),
                transaction_type=TransactionType.EXPENSE,
                description="Compra que estoura limite",
                occurred_at=self._date(2024, 6, 20),
            )

    async def test_delete_transaction_reverts_account_balance(self) -> None:
        user = await self._create_user()
        account = await self._create_account(user, starting_balance=Decimal("500.00"))
        expense_category = await self._create_category(
            user,
            name="Transporte",
            category_type=CategoryType.EXPENSE,
        )
        transaction = await self._create_transaction(
            user,
            account,
            expense_category,
            amount=Decimal("120.00"),
            transaction_type=TransactionType.EXPENSE,
            description="Aplicativo de corrida",
        )

        balance_after_purchase = await self.account_service.get_account(account.id)
        self.assertEqual(Decimal("380.00"), balance_after_purchase.balance)

        await self.transaction_service.delete_transaction(transaction.id)
        restored = await self.account_service.get_account(account.id)
        self.assertEqual(Decimal("500.00"), restored.balance)

        transactions = await self.transaction_service.list_transactions(user_id=user.id)
        self.assertEqual([], list(transactions))

    async def test_delete_account_blocked_when_transactions_exist(self) -> None:
        user = await self._create_user()
        account = await self._create_account(user, starting_balance=Decimal("250.00"))
        category = await self._create_category(
            user,
            name="Restaurantes",
            category_type=CategoryType.EXPENSE,
        )
        await self._create_transaction(
            user,
            account,
            category,
            amount=Decimal("50.00"),
            transaction_type=TransactionType.EXPENSE,
            description="Almoço",
        )

        with self.assertRaises(ValidationAppError):
            await self.account_service.delete_account(account.id)

    async def test_delete_category_blocked_by_budget(self) -> None:
        user = await self._create_user()
        category = await self._create_category(
            user,
            name="Viagem",
            category_type=CategoryType.EXPENSE,
        )
        await self._create_budget(
            user,
            category,
            amount=Decimal("800.00"),
            year=2024,
            month=8,
        )

        with self.assertRaises(ValidationAppError):
            await self.category_service.delete_category(category.id)

    async def test_budget_creation_and_listing_flow(self) -> None:
        user = await self._create_user()
        category = await self._create_category(
            user,
            name="Educação",
            category_type=CategoryType.EXPENSE,
        )
        may_budget = await self._create_budget(
            user,
            category,
            amount=Decimal("300.00"),
            year=2024,
            month=5,
        )
        june_budget = await self._create_budget(
            user,
            category,
            amount=Decimal("450.00"),
            year=2024,
            month=6,
        )

        budgets = await self.budget_service.list_budgets(user_id=user.id)
        self.assertEqual([may_budget.id, june_budget.id], [budget.id for budget in budgets])

        fetched = await self.budget_service.get_budget(june_budget.id)
        self.assertEqual(Decimal("450.00"), fetched.amount)
        self.assertEqual(6, fetched.month)

    async def test_report_monthly_summary_combines_categories_and_budgets(self) -> None:
        user = await self._create_user()
        account = await self._create_account(user, starting_balance=Decimal("500.00"))
        income_category = await self._create_category(
            user,
            name="Receitas",
            category_type=CategoryType.INCOME,
        )
        expense_category = await self._create_category(
            user,
            name="Aluguel",
            category_type=CategoryType.EXPENSE,
        )
        await self._create_budget(
            user,
            expense_category,
            amount=Decimal("600.00"),
            year=2024,
            month=7,
        )

        await self._create_transaction(
            user,
            account,
            income_category,
            amount=Decimal("1000.00"),
            transaction_type=TransactionType.INCOME,
            description="Salário julho",
            occurred_at=self._date(2024, 7, 5),
        )
        await self._create_transaction(
            user,
            account,
            expense_category,
            amount=Decimal("400.00"),
            transaction_type=TransactionType.EXPENSE,
            description="Aluguel julho",
            occurred_at=self._date(2024, 7, 10),
        )

        summary = await self.report_service.monthly_summary(user.id, 2024, 7)
        self.assertEqual(user.id, summary.user_id)
        self.assertEqual(
            Decimal("1000.00"),
            summary.totals_by_type[TransactionType.INCOME],
        )
        self.assertEqual(
            Decimal("400.00"),
            summary.totals_by_type[TransactionType.EXPENSE],
        )

        expense_summary = next(
            item
            for item in summary.categories
            if item.category_id == expense_category.id
            and item.transaction_type == TransactionType.EXPENSE
        )
        self.assertEqual(Decimal("600.00"), expense_summary.budget_amount)
        self.assertEqual(Decimal("200.00"), expense_summary.budget_remaining)

        income_summary = next(
            item
            for item in summary.categories
            if item.category_id == income_category.id
            and item.transaction_type == TransactionType.INCOME
        )
        self.assertIsNone(income_summary.budget_amount)
