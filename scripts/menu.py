"""Menu interativo para a Finance Manager API."""

from __future__ import annotations

import asyncio
import os
from typing import Any, Callable, Iterable, Optional

import httpx
import typer

DEFAULT_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api/v1")
MenuAction = Callable[[], None]


def _get_base_url() -> str:
    return os.getenv("API_BASE_URL", DEFAULT_BASE_URL)


async def _request(method: str, path: str, **kwargs) -> httpx.Response:
    async with httpx.AsyncClient(base_url=_get_base_url(), timeout=15) as client:
        return await client.request(method, path, **kwargs)


def _call_api(method: str, path: str, **kwargs) -> Optional[Any]:
    try:
        response = asyncio.run(_request(method, path, **kwargs))
        response.raise_for_status()
        if response.status_code == 204:
            return None
        return response.json()
    except httpx.HTTPStatusError as exc:
        try:
            details = exc.response.json()
        except ValueError:
            details = exc.response.text
        typer.secho(f"Erro {exc.response.status_code}: {details}", fg=typer.colors.RED)
    except httpx.RequestError as exc:
        typer.secho(f"Falha ao conectar na API ({exc}).", fg=typer.colors.RED)
    return None


def _prompt_float(message: str, default: Optional[float] = None) -> float:
    while True:
        raw_value = typer.prompt(message, default=default)
        try:
            return float(raw_value)
        except (TypeError, ValueError):
            typer.secho("Informe um número válido.", fg=typer.colors.RED)


def _prompt_choice(message: str, choices: Iterable[str], default: Optional[str] = None) -> str:
    valid = [choice.lower() for choice in choices]
    label = "/".join(valid)
    while True:
        value = typer.prompt(f"{message} ({label})", default=default or (valid[0] if valid else None))
        if value is None:
            continue
        value = value.strip().lower()
        if value in valid:
            return value
        typer.secho("Opção inválida, tente novamente.", fg=typer.colors.RED)


def _prompt_optional(message: str) -> Optional[str]:
    value = typer.prompt(message, default="").strip()
    return value or None


def _fmt_money(value: Any) -> str:
    try:
        return f"R${float(value):,.2f}"
    except (TypeError, ValueError):
        return "-"


def _pause() -> None:
    typer.secho("\nPressione ENTER para voltar ao menu...", fg=typer.colors.BRIGHT_BLACK)
    try:
        input()
    except EOFError:
        pass


def _print_list(title: str, rows: list[str]) -> None:
    if not rows:
        typer.secho("Nenhum registro encontrado.", fg=typer.colors.YELLOW)
        return
    typer.secho(f"\n{title}", fg=typer.colors.CYAN, bold=True)
    for line in rows:
        typer.echo(f"- {line}")


def list_users() -> None:
    data = _call_api("GET", "/users")
    if data is None:
        return
    rows = [
        f"{user.get('id')} | {user.get('name')} | {user.get('email')} | renda: {_fmt_money(user.get('monthly_income'))}"
        for user in data
    ]
    _print_list("Usuários cadastrados", rows)


def create_user() -> None:
    typer.secho("\nNovo usuário", fg=typer.colors.CYAN)
    name = typer.prompt("Nome")
    email = typer.prompt("Email")
    monthly_income = _prompt_float("Renda mensal (R$)", default=5000.0)
    payload = {"name": name, "email": email, "monthly_income": monthly_income}
    data = _call_api("POST", "/users", json=payload)
    if data:
        typer.secho(f"Usuário criado com ID {data.get('id')}", fg=typer.colors.GREEN)


def list_accounts() -> None:
    user_id = typer.prompt("ID do usuário dono das contas").strip()
    data = _call_api("GET", "/accounts", params={"user_id": user_id})
    if data is None:
        return
    rows = [
        f"{acc.get('id')} | {acc.get('name')} ({acc.get('institution')}) | tipo: {acc.get('type')} | saldo: {_fmt_money(acc.get('balance'))}"
        for acc in data
    ]
    _print_list("Contas encontradas", rows)


def create_account() -> None:
    typer.secho("\nNova conta", fg=typer.colors.CYAN)
    user_id = typer.prompt("ID do usuário")
    name = typer.prompt("Nome da conta (ex.: Conta Corrente)")
    institution = typer.prompt("Instituição (ex.: Nubank)")
    account_type = _prompt_choice(
        "Tipo",
        ("checking", "savings", "investment", "cash"),
        default="checking",
    )
    balance = _prompt_float("Saldo inicial", default=0.0)
    currency = typer.prompt("Moeda (ISO-4217)", default="BRL").upper()
    payload = {
        "user_id": user_id,
        "name": name,
        "institution": institution,
        "type": account_type,
        "balance": balance,
        "currency": currency,
    }
    data = _call_api("POST", "/accounts", json=payload)
    if data:
        typer.secho(f"Conta criada com ID {data.get('id')}", fg=typer.colors.GREEN)


def list_transactions() -> None:
    user_id = typer.prompt("ID do usuário das transações").strip()
    data = _call_api("GET", "/transactions", params={"user_id": user_id})
    if data is None:
        return
    rows = [
        f"{tx.get('id')} | conta: {tx.get('account_id')} | {tx.get('type')} | {tx.get('category')} | valor: {_fmt_money(tx.get('amount'))}"
        for tx in data
    ]
    _print_list("Transações", rows)


def create_transaction() -> None:
    typer.secho("\nNova transação", fg=typer.colors.CYAN)
    user_id = typer.prompt("ID do usuário")
    account_id = typer.prompt("ID da conta")
    tx_type = _prompt_choice("Tipo", ("income", "expense", "transfer"), default="expense")
    amount = _prompt_float("Valor")
    category = typer.prompt("Categoria (ex.: groceries)")
    description = typer.prompt("Descrição", default="Lançamento via menu")
    budget_id = _prompt_optional("Budget ID (ENTER para ignorar)")
    goal_id = _prompt_optional("Goal ID (ENTER para ignorar)")
    payload = {
        "user_id": user_id,
        "account_id": account_id,
        "type": tx_type,
        "amount": amount,
        "category": category,
        "description": description,
        "budget_id": budget_id,
        "goal_id": goal_id,
    }
    data = _call_api("POST", "/transactions", json=payload)
    if data:
        typer.secho(f"Transação registrada com ID {data.get('id')}", fg=typer.colors.GREEN)


def export_report() -> None:
    user_id = typer.prompt("ID do usuário para o relatório").strip()
    data = _call_api("GET", f"/reports/transactions/{user_id}")
    if data:
        typer.secho("Relatório gerado com sucesso!", fg=typer.colors.GREEN)
        typer.echo(f"Arquivo: {data.get('file_path')}")
        typer.echo(f"Total de transações: {data.get('total_transactions')}")
        typer.echo(f"Receitas: {_fmt_money(data.get('total_income'))}")
        typer.echo(f"Despesas: {_fmt_money(data.get('total_expenses'))}")


MENU_OPTIONS: list[tuple[str, str, MenuAction]] = [
    ("1", "Listar usuários", list_users),
    ("2", "Criar usuário", create_user),
    ("3", "Listar contas de um usuário", list_accounts),
    ("4", "Criar conta", create_account),
    ("5", "Listar transações de um usuário", list_transactions),
    ("6", "Registrar transação", create_transaction),
    ("7", "Exportar relatório de transações", export_report),
]


def _run_menu() -> None:
    while True:
        typer.secho("\n=== Finance Manager - Menu ===", fg=typer.colors.CYAN, bold=True)
        typer.secho(f"API alvo: {_get_base_url()}", fg=typer.colors.BRIGHT_BLACK)
        for key, label, _ in MENU_OPTIONS:
            typer.echo(f"{key}) {label}")
        typer.echo("0) Sair")
        choice = typer.prompt("Selecione uma opção").strip()
        if choice == "0":
            typer.secho("Encerrando menu. Até logo!", fg=typer.colors.GREEN)
            return
        action = next((func for key, _, func in MENU_OPTIONS if key == choice), None)
        if not action:
            typer.secho("Opção inválida, tente novamente.", fg=typer.colors.RED)
            continue
        action()
        _pause()


def main(
    base_url: str = typer.Option(
        DEFAULT_BASE_URL,
        "--base-url",
        "-b",
        help="URL base da API (ex.: http://localhost:8001/api/v1).",
    ),
) -> None:
    os.environ["API_BASE_URL"] = base_url
    try:
        _run_menu()
    except KeyboardInterrupt:
        typer.secho("\nMenu interrompido pelo usuário.", fg=typer.colors.YELLOW)


if __name__ == "__main__":
    typer.run(main)
