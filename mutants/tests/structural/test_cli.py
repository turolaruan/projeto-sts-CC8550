"""Structural tests targeting CLI helpers to reduce surviving mutants."""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config.settings import Settings
from src.models.enums import CategoryType
from src.interface import cli
from src.interface.cli import ServiceContainer
from tests.structural.helpers import (
    build_account,
    build_budget,
    build_category,
    build_user,
    FakeMotorClient,
)


class InputFeeder:
    """Helper that simulates user input by returning queued responses."""

    def __init__(self, responses: list[str]) -> None:
        self._responses = responses

    def __call__(self, prompt: str = "") -> str:
        if not self._responses:
            raise AssertionError(f"No more fake inputs available for prompt: {prompt}")
        return self._responses.pop(0)


@pytest.mark.asyncio
async def test_setup_and_shutdown_services_use_configured_client(monkeypatch) -> None:
    fake_client = FakeMotorClient()
    monkeypatch.setattr("src.interface.cli.AsyncIOMotorClient", lambda *_, **__: fake_client)
    settings = Settings(MONGODB_URI="mongodb://cli-test:27017", MONGODB_DB="cli_db")
    monkeypatch.setattr("src.interface.cli.get_settings", lambda: settings)

    container = await cli.setup_services()
    assert container.client is fake_client
    assert container.user_service is not None
    assert container.account_service is not None

    await cli.shutdown_services(container)
    assert fake_client.closed is True


def test_print_header_and_pause(monkeypatch, capsys) -> None:
    feeder = InputFeeder([""])
    monkeypatch.setattr("builtins.input", feeder)

    cli.print_header("Teste CLI")
    cli.pause()

    captured = capsys.readouterr().out
    assert "Teste CLI" in captured
    assert "=" * 60 in captured


def test_input_feeder_raises_when_empty() -> None:
    feeder = InputFeeder([])
    with pytest.raises(AssertionError):
        feeder("> ")


@pytest.mark.asyncio
async def test_main_menu_dispatches_action_and_handles_invalid_option(monkeypatch) -> None:
    responses = ["9", "1", "0"]
    monkeypatch.setattr("builtins.input", InputFeeder(responses))
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)

    called = []

    async def fake_action(container: ServiceContainer) -> None:
        called.append(container)

    monkeypatch.setattr(cli, "MENU_ACTIONS", {"1": fake_action})
    container = SimpleNamespace()
    await cli.main_menu(container)
    assert called == [container]


@pytest.mark.asyncio
async def test_manage_users_lists_and_creates_users(monkeypatch) -> None:
    list_users = AsyncMock(
        side_effect=[
            [SimpleNamespace(id="1", name="User", email="user@example.com", default_currency="BRL")],
            [],
        ]
    )
    create_user = AsyncMock()
    container = SimpleNamespace(user_service=SimpleNamespace(list_users=list_users, create_user=create_user))
    responses = ["1", "0"]
    monkeypatch.setattr("builtins.input", InputFeeder(responses.copy()))
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)
    await cli.manage_users(container)
    list_users.assert_awaited()

    create_inputs = ["2", "Novo Usuário", "novo@example.com", "USD", "0"]
    monkeypatch.setattr("builtins.input", InputFeeder(create_inputs))
    await cli.manage_users(container)
    assert create_user.await_count >= 1
    payload = create_user.await_args_list[0].args[0]
    assert payload.email == "novo@example.com"


@pytest.mark.asyncio
async def test_register_transaction_requires_user_and_account(monkeypatch, capsys) -> None:
    container = SimpleNamespace(
        transaction_service=SimpleNamespace(create_transaction=AsyncMock()),
        user_service=SimpleNamespace(list_users=AsyncMock(return_value=[])),
    )
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)

    await cli.register_transaction(container)
    output = capsys.readouterr().out
    assert "Cadastre um usuário primeiro." in output


@pytest.mark.asyncio
async def test_manage_accounts_handles_listing_and_creation(monkeypatch) -> None:
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)
    account_service = SimpleNamespace(
        list_accounts=AsyncMock(return_value=[]),
        create_account=AsyncMock(),
    )
    user = build_user()
    container = SimpleNamespace(
        account_service=account_service,
        user_service=SimpleNamespace(list_users=AsyncMock(return_value=[user])),
    )
    monkeypatch.setattr("builtins.input", InputFeeder(["1", "0"]))
    await cli.manage_accounts(container)
    account_service.list_accounts.assert_awaited_once()

    accounts = [build_account()]
    account_service = SimpleNamespace(
        list_accounts=AsyncMock(return_value=accounts),
        create_account=AsyncMock(),
    )
    user_service = SimpleNamespace(list_users=AsyncMock(return_value=[user]))
    container = SimpleNamespace(account_service=account_service, user_service=user_service)
    create_inputs = [
        "2",
        "1",
        "Conta CLI",
        "",
        "",
        "",
        "100.50",
        "10.00",
        "0",
    ]
    monkeypatch.setattr("builtins.input", InputFeeder(create_inputs))
    await cli.manage_accounts(container)
    assert account_service.create_account.await_count == 1


@pytest.mark.asyncio
async def test_manage_categories_handles_parent_selection(monkeypatch) -> None:
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)
    user = build_user()
    parent_category = build_category(user_id=user.id)
    service = SimpleNamespace(
        list_categories=AsyncMock(return_value=[parent_category]),
        create_category=AsyncMock(),
    )
    container = SimpleNamespace(
        category_service=service,
        user_service=SimpleNamespace(list_users=AsyncMock(return_value=[user])),
    )
    inputs = ["2", "1", "Categoria CLI", "", "", "1", "0"]
    monkeypatch.setattr("builtins.input", InputFeeder(inputs))
    await cli.manage_categories(container)
    service.create_category.assert_awaited_once()


@pytest.mark.asyncio
async def test_manage_budgets_creates_budget(monkeypatch) -> None:
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)
    user = build_user()
    category = build_category(user_id=user.id, category_type=CategoryType.EXPENSE)
    service = SimpleNamespace(
        list_budgets=AsyncMock(return_value=[build_budget(user_id=user.id, category_id=category.id)]),
        create_budget=AsyncMock(),
    )
    container = SimpleNamespace(
        budget_service=service,
        user_service=SimpleNamespace(list_users=AsyncMock(return_value=[user])),
        category_service=SimpleNamespace(
            list_categories=AsyncMock(return_value=[category]),
        ),
    )
    inputs = ["2", "1", "1", "2024", "7", "500.00", "", "0"]
    monkeypatch.setattr("builtins.input", InputFeeder(inputs))
    await cli.manage_budgets(container)
    service.create_budget.assert_awaited_once()


@pytest.mark.asyncio
async def test_register_transaction_transfer_flow(monkeypatch) -> None:
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)
    user = build_user()
    accounts = [build_account(user_id=user.id), build_account(user_id=user.id)]
    category = build_category(user_id=user.id)
    container = SimpleNamespace(
        transaction_service=SimpleNamespace(create_transaction=AsyncMock()),
        user_service=SimpleNamespace(list_users=AsyncMock(return_value=[user])),
        account_service=SimpleNamespace(list_accounts=AsyncMock(return_value=accounts)),
        category_service=SimpleNamespace(list_categories=AsyncMock(return_value=[category])),
    )
    inputs = [
        "1",  # user
        "1",  # account
        "1",  # category
        "transfer",
        "250.50",
        "Transferência",
        "",
        "",
        "2024-06-15T12:00:00",
        "2",
    ]
    monkeypatch.setattr("builtins.input", InputFeeder(inputs))
    await cli.register_transaction(container)
    payload = container.transaction_service.create_transaction.await_args[0][0]
    assert payload.transfer_account_id == accounts[1].id


@pytest.mark.asyncio
async def test_show_report_displays_summary(monkeypatch, capsys) -> None:
    monkeypatch.setattr("src.interface.cli.pause", lambda: None)
    user = build_user()
    summary = SimpleNamespace(
        totals_by_type={"income": Decimal("100.00")},
        categories=[
            SimpleNamespace(
                name="Categoria",
                transaction_type="income",
                total=Decimal("100.00"),
                count=1,
                budget_amount=Decimal("150.00"),
                budget_remaining=Decimal("50.00"),
            )
        ],
    )
    container = SimpleNamespace(
        user_service=SimpleNamespace(list_users=AsyncMock(return_value=[user])),
        report_service=SimpleNamespace(
            monthly_summary=AsyncMock(return_value=summary),
        ),
    )
    inputs = ["1", "2024", "6"]
    monkeypatch.setattr("builtins.input", InputFeeder(inputs))
    await cli.show_report(container)
    output = capsys.readouterr().out
    assert "Relatório Mensal" in output


@pytest.mark.asyncio
async def test_async_main_manages_lifecycle(monkeypatch) -> None:
    container = SimpleNamespace()
    setup = AsyncMock(return_value=container)
    shutdown = AsyncMock()
    main_menu = AsyncMock()
    monkeypatch.setattr(cli, "setup_services", setup)
    monkeypatch.setattr(cli, "shutdown_services", shutdown)
    monkeypatch.setattr(cli, "main_menu", main_menu)

    await cli.async_main()

    setup.assert_awaited_once()
    main_menu.assert_awaited_once_with(container)
    shutdown.assert_awaited_once_with(container)


def test_run_invokes_asyncio_run(monkeypatch) -> None:
    async def fake_async_main() -> None:
        return None

    recorded = {}

    def fake_run(coro):
        recorded["called"] = True
        assert coro.__class__.__name__ == fake_async_main().__class__.__name__

    monkeypatch.setattr(cli, "async_main", fake_async_main)
    monkeypatch.setattr(cli.asyncio, "run", fake_run)

    cli.run()
    assert recorded["called"] is True
