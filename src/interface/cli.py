"""Interactive CLI for the Personal Finance Manager."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Callable, Coroutine, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from src.config import get_settings
from src.models.account import AccountCreate
from src.models.budget import BudgetCreate
from src.models.category import CategoryCreate
from src.models.enums import AccountType, CategoryType, CurrencyCode, TransactionType
from src.models.transaction import TransactionCreate
from src.models.user import UserCreate
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
from src.utils.exceptions import AppException


@dataclass
class ServiceContainer:
    client: AsyncIOMotorClient
    user_service: UserService
    account_service: AccountService
    category_service: CategoryService
    transaction_service: TransactionService
    budget_service: BudgetService
    report_service: ReportService


async def setup_services() -> ServiceContainer:
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongodb_uri, uuidRepresentation="standard")
    db = client[settings.mongodb_db]

    user_repo = UserRepository(db)
    account_repo = AccountRepository(db)
    category_repo = CategoryRepository(db)
    transaction_repo = TransactionRepository(db)
    budget_repo = BudgetRepository(db)

    user_service = UserService(user_repo)
    account_service = AccountService(account_repo, user_repo, transaction_repo)
    category_service = CategoryService(category_repo, user_repo, transaction_repo, budget_repo)
    budget_service = BudgetService(budget_repo, user_repo, category_repo, transaction_repo)
    transaction_service = TransactionService(
        transaction_repo,
        account_service,
        account_repo,
        category_repo,
        user_repo,
        budget_repo,
    )
    report_service = ReportService(transaction_repo, category_repo, budget_repo)

    return ServiceContainer(
        client=client,
        user_service=user_service,
        account_service=account_service,
        category_service=category_service,
        transaction_service=transaction_service,
        budget_service=budget_service,
        report_service=report_service,
    )


async def shutdown_services(container: ServiceContainer) -> None:
    container.client.close()


def print_header(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def pause() -> None:
    input("\nPressione Enter para continuar...")


async def manage_users(container: ServiceContainer) -> None:
    service = container.user_service
    while True:
        print_header("Usuários")
        print("1. Listar usuários")
        print("2. Criar usuário")
        print("0. Voltar")
        choice = input("> ").strip()
        if choice == "1":
            users = await service.list_users()
            if not users:
                print("Nenhum usuário cadastrado.")
            for user in users:
                print(f"- {user.id} | {user.name} | {user.email} | {user.default_currency}")
            pause()
        elif choice == "2":
            name = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            currency = input(f"Moeda padrão [{CurrencyCode.BRL.value}]: ").strip() or CurrencyCode.BRL.value
            try:
                await service.create_user(UserCreate(name=name, email=email, default_currency=currency))
                print("Usuário criado com sucesso!")
            except Exception as exc:
                print(f"Erro: {exc}")
            pause()
        elif choice == "0":
            break
        else:
            print("Opção inválida.")


async def manage_accounts(container: ServiceContainer) -> None:
    service = container.account_service
    user_service = container.user_service
    while True:
        print_header("Contas")
        print("1. Listar contas")
        print("2. Criar conta")
        print("0. Voltar")
        choice = input("> ").strip()
        if choice == "1":
            accounts = await service.list_accounts()
            if not accounts:
                print("Nenhuma conta cadastrada.")
            for account in accounts:
                print(
                    f"- {account.id} | Usuário: {account.user_id} | {account.name} | "
                    f"{account.account_type} | Saldo: {account.balance}"
                )
            pause()
        elif choice == "2":
            users = await user_service.list_users()
            if not users:
                print("Cadastre um usuário antes de criar contas.")
                pause()
                continue
            for idx, user in enumerate(users, start=1):
                print(f"{idx}. {user.name} ({user.email})")
            selected = int(input("Selecione o usuário: ").strip())
            target_user = users[selected - 1]
            name = input("Nome da conta: ").strip()
            account_type = input(f"Tipo [{AccountType.CHECKING.value}]: ").strip() or AccountType.CHECKING.value
            currency = input(f"Moeda [{CurrencyCode.BRL.value}]: ").strip() or CurrencyCode.BRL.value
            description = input("Descrição (opcional): ").strip()
            starting_balance = Decimal(input("Saldo inicial [0]: ") or "0")
            minimum_balance = Decimal(input("Saldo mínimo [0]: ") or "0")
            try:
                await service.create_account(
                    AccountCreate(
                        user_id=target_user.id,
                        name=name,
                        account_type=account_type,
                        currency=currency,
                        description=description or None,
                        starting_balance=starting_balance,
                        minimum_balance=minimum_balance,
                    )
                )
                print("Conta criada com sucesso!")
            except AppException as exc:
                print(f"Erro: {exc.message}")
            pause()
        elif choice == "0":
            break
        else:
            print("Opção inválida.")


async def manage_categories(container: ServiceContainer) -> None:
    service = container.category_service
    user_service = container.user_service
    while True:
        print_header("Categorias")
        print("1. Listar categorias")
        print("2. Criar categoria")
        print("0. Voltar")
        choice = input("> ").strip()
        if choice == "1":
            categories = await service.list_categories()
            if not categories:
                print("Nenhuma categoria cadastrada.")
            for category in categories:
                parent = category.parent_id or "-"
                print(
                    f"- {category.id} | Usuário: {category.user_id} | {category.name} | "
                    f"{category.category_type} | Pai: {parent}"
                )
            pause()
        elif choice == "2":
            users = await user_service.list_users()
            if not users:
                print("Cadastre um usuário antes de criar categorias.")
                pause()
                continue
            for idx, user in enumerate(users, start=1):
                print(f"{idx}. {user.name}")
            target_user = users[int(input("Selecione o usuário: ").strip()) - 1]
            name = input("Nome: ").strip()
            category_type = input(f"Tipo [{CategoryType.EXPENSE.value}]: ").strip() or CategoryType.EXPENSE.value
            description = input("Descrição (opcional): ").strip()
            existing = await service.list_categories(user_id=target_user.id)
            parent_id: Optional[str] = None
            if existing:
                print("Categorias existentes:")
                print("0. Nenhuma")
                for idx, cat in enumerate(existing, start=1):
                    print(f"{idx}. {cat.name} ({cat.category_type})")
                choice_parent = int(input("Categoria pai: ").strip() or "0")
                if choice_parent > 0:
                    parent_id = existing[choice_parent - 1].id
            try:
                await service.create_category(
                    CategoryCreate(
                        user_id=target_user.id,
                        name=name,
                        category_type=category_type,
                        description=description or None,
                        parent_id=parent_id,
                    )
                )
                print("Categoria criada com sucesso!")
            except AppException as exc:
                print(f"Erro: {exc.message}")
            pause()
        elif choice == "0":
            break
        else:
            print("Opção inválida.")


async def register_transaction(container: ServiceContainer) -> None:
    service = container.transaction_service
    users = await container.user_service.list_users()
    if not users:
        print("Cadastre um usuário primeiro.")
        pause()
        return
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. {user.name}")
    user = users[int(input("Usuário: ").strip()) - 1]

    accounts = await container.account_service.list_accounts(user_id=user.id)
    if not accounts:
        print("Cadastre uma conta primeiro.")
        pause()
        return
    for idx, account in enumerate(accounts, start=1):
        print(f"{idx}. {account.name}")
    account = accounts[int(input("Conta: ").strip()) - 1]

    categories = await container.category_service.list_categories(user_id=user.id)
    if not categories:
        print("Cadastre uma categoria primeiro.")
        pause()
        return
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category.name} ({category.category_type})")
    category = categories[int(input("Categoria: ").strip()) - 1]

    transaction_type = input("Tipo [expense/income/transfer]: ").strip() or TransactionType.EXPENSE.value
    amount = Decimal(input("Valor: ").strip())
    description = input("Descrição: ").strip()
    notes = input("Notas: ").strip()
    counterparty = input("Contraparte: ").strip()
    occurred_str = input("Data (ISO opcional): ").strip()
    transfer_account_id: Optional[str] = None
    if transaction_type == TransactionType.TRANSFER.value:
        for idx, acc in enumerate(accounts, start=1):
            print(f"{idx}. {acc.name}")
        transfer_account_id = accounts[int(input("Conta destino: ").strip()) - 1].id

    payload = {
        "user_id": user.id,
        "account_id": account.id,
        "category_id": category.id,
        "transaction_type": transaction_type,
        "amount": amount,
        "description": description or None,
        "notes": notes or None,
        "counterparty": counterparty or None,
        "transfer_account_id": transfer_account_id,
    }
    if occurred_str:
        payload["occurred_at"] = datetime.fromisoformat(occurred_str)
    try:
        await service.create_transaction(TransactionCreate(**payload))
        print("Transação registrada com sucesso!")
    except AppException as exc:
        print(f"Erro: {exc.message}")
    pause()


async def manage_budgets(container: ServiceContainer) -> None:
    service = container.budget_service
    user_service = container.user_service
    category_service = container.category_service
    while True:
        print_header("Budgets")
        print("1. Listar budgets")
        print("2. Criar budget")
        print("0. Voltar")
        choice = input("> ").strip()
        if choice == "1":
            budgets = await service.list_budgets()
            if not budgets:
                print("Nenhum budget cadastrado.")
            for budget in budgets:
                print(
                    f"- {budget.id} | Usuário: {budget.user_id} | Categoria: {budget.category_id} | "
                    f"{budget.month:02d}/{budget.year} | Valor: {budget.amount}"
                )
            pause()
        elif choice == "2":
            users = await user_service.list_users()
            if not users:
                print("Cadastre um usuário antes de criar budgets.")
                pause()
                continue
            for idx, user in enumerate(users, start=1):
                print(f"{idx}. {user.name}")
            user = users[int(input("Usuário: ").strip()) - 1]
            categories = await category_service.list_categories(user_id=user.id, category_type=CategoryType.EXPENSE.value)
            if not categories:
                print("Cadastre uma categoria de despesa antes de criar budgets.")
                pause()
                continue
            for idx, category in enumerate(categories, start=1):
                print(f"{idx}. {category.name}")
            category = categories[int(input("Categoria: ").strip()) - 1]
            year = int(input("Ano: ").strip())
            month = int(input("Mês: ").strip())
            amount = Decimal(input("Valor: ").strip())
            alert = int(input("Alerta (%): ").strip() or "80")
            try:
                await service.create_budget(
                    BudgetCreate(
                        user_id=user.id,
                        category_id=category.id,
                        year=year,
                        month=month,
                        amount=amount,
                        alert_percentage=alert,
                    )
                )
                print("Budget criado com sucesso!")
            except AppException as exc:
                print(f"Erro: {exc.message}")
            pause()
        elif choice == "0":
            break
        else:
            print("Opção inválida.")


async def show_report(container: ServiceContainer) -> None:
    users = await container.user_service.list_users()
    if not users:
        print("Cadastre um usuário primeiro.")
        pause()
        return
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. {user.name}")
    user = users[int(input("Usuário: ").strip()) - 1]
    year = int(input("Ano: ").strip())
    month = int(input("Mês: ").strip())
    summary = await container.report_service.monthly_summary(user.id, year, month)
    print_header("Relatório Mensal")
    print(f"Usuário: {user.name} | Período: {month:02d}/{year}")
    print("\nTotais por tipo:")
    for key, value in summary.totals_by_type.items():
        print(f"- {key}: {value}")
    print("\nCategorias:")
    for category in summary.categories:
        print(
            f"- {category.name} ({category.transaction_type}) | Total: {category.total} | "
            f"Transações: {category.count} | Budget: {category.budget_amount or '-'} | "
            f"Restante: {category.budget_remaining or '-'}"
        )
    pause()


MENU_ACTIONS: dict[str, Callable[[ServiceContainer], Coroutine[Any, Any, None]]] = {
    "1": manage_users,
    "2": manage_accounts,
    "3": manage_categories,
    "4": register_transaction,
    "5": manage_budgets,
    "6": show_report,
}


async def main_menu(container: ServiceContainer) -> None:
    while True:
        print_header("Menu Principal")
        print("1. Gerenciar usuários")
        print("2. Gerenciar contas")
        print("3. Gerenciar categorias")
        print("4. Registrar transação")
        print("5. Gerenciar budgets")
        print("6. Relatório mensal")
        print("0. Sair")
        choice = input("> ").strip()
        if choice == "0":
            print("Encerrando...")
            break
        action = MENU_ACTIONS.get(choice)
        if action:
            await action(container)
        else:
            print("Opção inválida.")
            pause()


async def async_main() -> None:
    container = await setup_services()
    try:
        await main_menu(container)
    finally:
        await shutdown_services(container)


def run() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    run()
