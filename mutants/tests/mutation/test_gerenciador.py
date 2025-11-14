"""Testes de mutação focados nas regras centrais do gerenciador financeiro."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from types import SimpleNamespace

import pytest

from src.models.account import AccountCreate, build_account
from src.models.budget import BudgetCreate
from src.models.category import CategoryCreate, build_category
from src.models.common import generate_object_id
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import TransactionCreate, build_transaction
from src.models.user import UserCreate, build_user
from src.repositories.account_repository import InMemoryAccountRepository
from src.repositories.budget_repository import InMemoryBudgetRepository
from src.repositories.category_repository import InMemoryCategoryRepository
from src.repositories.transaction_repository import InMemoryTransactionRepository
from src.repositories.user_repository import InMemoryUserRepository
from src.services.account_service import AccountService
from src.services.budget_service import BudgetService
from src.services.transaction_service import TransactionService
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)

pytestmark = pytest.mark.mutation


async def build_service_context() -> SimpleNamespace:
    """Monta um cenário completo com repositórios em memória e entidades base."""
    user_repo = InMemoryUserRepository()
    account_repo = InMemoryAccountRepository()
    category_repo = InMemoryCategoryRepository()
    budget_repo = InMemoryBudgetRepository()
    transaction_repo = InMemoryTransactionRepository()

    user = build_user(
        UserCreate(
            name="Alice Mutacao",
            email="alice.mutacao@example.com",
            default_currency=CurrencyCode.BRL,
        )
    )
    await user_repo.create(user)

    primary_account = build_account(
        AccountCreate(
            user_id=user.id,
            name="Conta Principal",
            account_type=AccountType.CHECKING,
            currency=CurrencyCode.BRL,
            description="Conta utilizada nos testes de mutacao",
            minimum_balance=Decimal("100.00"),
            starting_balance=Decimal("500.00"),
        )
    )
    await account_repo.create(primary_account)

    transfer_account = build_account(
        AccountCreate(
            user_id=user.id,
            name="Conta Transferencia",
            account_type=AccountType.SAVINGS,
            currency=CurrencyCode.BRL,
            description="Conta destino das transferencias",
            minimum_balance=Decimal("0.00"),
            starting_balance=Decimal("300.00"),
        )
    )
    await account_repo.create(transfer_account)

    income_category = build_category(
        CategoryCreate(
            user_id=user.id,
            name="Receitas Fixas",
            category_type=CategoryType.INCOME,
            description="Categoria de receitas",
            parent_id=None,
        )
    )
    expense_category = build_category(
        CategoryCreate(
            user_id=user.id,
            name="Despesas Essenciais",
            category_type=CategoryType.EXPENSE,
            description="Categoria de despesas prioritarias",
            parent_id=None,
        )
    )
    await category_repo.create(income_category)
    await category_repo.create(expense_category)

    account_service = AccountService(account_repo, user_repo, transaction_repo)
    budget_service = BudgetService(budget_repo, user_repo, category_repo, transaction_repo)
    transaction_service = TransactionService(
        repository=transaction_repo,
        account_service=account_service,
        account_repository=account_repo,
        category_repository=category_repo,
        user_repository=user_repo,
        budget_repository=budget_repo,
    )

    return SimpleNamespace(
        user=user,
        account=primary_account,
        transfer_account=transfer_account,
        expense_category=expense_category,
        income_category=income_category,
        services=SimpleNamespace(
            account=account_service,
            budget=budget_service,
            transaction=transaction_service,
        ),
        repositories=SimpleNamespace(
            user=user_repo,
            account=account_repo,
            category=category_repo,
            budget=budget_repo,
            transaction=transaction_repo,
        ),
    )


@pytest.mark.asyncio
async def test_create_account_requires_existing_user() -> None:
    """Garante que contas não sejam criadas sem usuário válido."""
    service = AccountService(
        InMemoryAccountRepository(),
        InMemoryUserRepository(),
        InMemoryTransactionRepository(),
    )
    payload = AccountCreate(
        user_id=generate_object_id(),
        name="Conta Fantasma",
        account_type=AccountType.CHECKING,
        currency=CurrencyCode.BRL,
        description="Conta sem usuario cadastrado",
        minimum_balance=Decimal("0.00"),
        starting_balance=Decimal("50.00"),
    )

    with pytest.raises(EntityNotFoundError):
        await service.create_account(payload)


@pytest.mark.asyncio
async def test_adjust_balance_respects_minimum_balance() -> None:
    """Não permite que o saldo fique abaixo do mínimo configurado."""
    ctx = await build_service_context()
    with pytest.raises(ValidationAppError):
        await ctx.services.account.adjust_balance(ctx.account.id, Decimal("-450.00"))


@pytest.mark.asyncio
async def test_delete_account_fails_when_transactions_exist() -> None:
    """Evita exclusões de contas com transações relacionadas."""
    ctx = await build_service_context()
    transaction = build_transaction(
        TransactionCreate(
            user_id=ctx.user.id,
            account_id=ctx.account.id,
            category_id=ctx.expense_category.id,
            amount=Decimal("10.00"),
            transaction_type=TransactionType.EXPENSE,
            occurred_at=datetime.now(timezone.utc),
            description="Despesa pendente",
        )
    )
    await ctx.repositories.transaction.create(transaction)

    with pytest.raises(ValidationAppError):
        await ctx.services.account.delete_account(ctx.account.id)


@pytest.mark.asyncio
async def test_budget_creation_is_unique_per_period() -> None:
    """Cada categoria só pode ter um budget por período."""
    ctx = await build_service_context()
    payload = BudgetCreate(
        user_id=ctx.user.id,
        category_id=ctx.expense_category.id,
        year=2024,
        month=6,
        amount=Decimal("1000.00"),
        alert_percentage=75,
    )
    await ctx.services.budget.create_budget(payload)

    with pytest.raises(EntityAlreadyExistsError):
        await ctx.services.budget.create_budget(payload)


@pytest.mark.asyncio
async def test_budget_requires_expense_category() -> None:
    """Budget não pode ser criado para categoria de receita."""
    ctx = await build_service_context()
    payload = BudgetCreate(
        user_id=ctx.user.id,
        category_id=ctx.income_category.id,
        year=2024,
        month=5,
        amount=Decimal("800.00"),
        alert_percentage=60,
    )
    with pytest.raises(ValidationAppError):
        await ctx.services.budget.create_budget(payload)


@pytest.mark.asyncio
async def test_budget_deletion_blocks_existing_transactions() -> None:
    """Não permite remover budget com lançamentos no mesmo período."""
    ctx = await build_service_context()
    payload = BudgetCreate(
        user_id=ctx.user.id,
        category_id=ctx.expense_category.id,
        year=2024,
        month=5,
        amount=Decimal("900.00"),
        alert_percentage=80,
    )
    budget = await ctx.services.budget.create_budget(payload)

    blocking_transaction = build_transaction(
        TransactionCreate(
            user_id=ctx.user.id,
            account_id=ctx.account.id,
            category_id=ctx.expense_category.id,
            amount=Decimal("50.00"),
            transaction_type=TransactionType.EXPENSE,
            occurred_at=datetime(2024, 5, 10, tzinfo=timezone.utc),
            description="Compra dentro do orçamento",
        )
    )
    await ctx.repositories.transaction.create(blocking_transaction)

    with pytest.raises(ValidationAppError):
        await ctx.services.budget.delete_budget(budget.id)


@pytest.mark.asyncio
async def test_transfer_requires_destination_account() -> None:
    """Transferências precisam de conta de destino distinta."""
    ctx = await build_service_context()
    payload = TransactionCreate(
        user_id=ctx.user.id,
        account_id=ctx.account.id,
        category_id=ctx.expense_category.id,
        amount=Decimal("30.00"),
        transaction_type=TransactionType.TRANSFER,
        description="Transferencia incompleta",
    )

    with pytest.raises(ValidationAppError):
        await ctx.services.transaction.create_transaction(payload)


@pytest.mark.asyncio
async def test_budget_limit_is_enforced_for_expenses() -> None:
    """Garante que transações não estourem o teto do orçamento."""
    ctx = await build_service_context()
    budget_payload = BudgetCreate(
        user_id=ctx.user.id,
        category_id=ctx.expense_category.id,
        year=2024,
        month=4,
        amount=Decimal("200.00"),
        alert_percentage=70,
    )
    await ctx.services.budget.create_budget(budget_payload)

    existing_spend = build_transaction(
        TransactionCreate(
            user_id=ctx.user.id,
            account_id=ctx.account.id,
            category_id=ctx.expense_category.id,
            amount=Decimal("180.00"),
            transaction_type=TransactionType.EXPENSE,
            occurred_at=datetime(2024, 4, 5, tzinfo=timezone.utc),
            description="Gasto previo",
        )
    )
    await ctx.repositories.transaction.create(existing_spend)

    overspend_payload = TransactionCreate(
        user_id=ctx.user.id,
        account_id=ctx.account.id,
        category_id=ctx.expense_category.id,
        amount=Decimal("50.00"),
        transaction_type=TransactionType.EXPENSE,
        occurred_at=datetime(2024, 4, 15, tzinfo=timezone.utc),
        description="Tentativa de excesso",
    )

    with pytest.raises(ValidationAppError):
        await ctx.services.transaction.create_transaction(overspend_payload)


@pytest.mark.asyncio
async def test_expense_updates_account_balance() -> None:
    """Debita o saldo da conta após registrar uma despesa."""
    ctx = await build_service_context()
    original = await ctx.repositories.account.get(ctx.account.id)
    assert original is not None
    payload = TransactionCreate(
        user_id=ctx.user.id,
        account_id=ctx.account.id,
        category_id=ctx.expense_category.id,
        amount=Decimal("50.00"),
        transaction_type=TransactionType.EXPENSE,
        description="Compra de supermercado",
    )

    await ctx.services.transaction.create_transaction(payload)

    updated = await ctx.repositories.account.get(ctx.account.id)
    assert updated is not None
    assert updated.balance == original.balance - Decimal("50.00")


@pytest.mark.asyncio
async def test_category_type_must_match_transaction_type() -> None:
    """Impede que receitas usem categorias de despesa (e vice-versa)."""
    ctx = await build_service_context()
    payload = TransactionCreate(
        user_id=ctx.user.id,
        account_id=ctx.account.id,
        category_id=ctx.expense_category.id,
        amount=Decimal("200.00"),
        transaction_type=TransactionType.INCOME,
        description="Receita mal categorizada",
    )

    with pytest.raises(ValidationAppError):
        await ctx.services.transaction.create_transaction(payload)
