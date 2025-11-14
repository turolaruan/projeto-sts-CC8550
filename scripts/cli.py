"""Simple CLI for interacting with the Finance Manager API."""

from __future__ import annotations

import asyncio
import json
import os

import httpx
import typer

DEFAULT_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api/v1")

app = typer.Typer(add_completion=False, help="CLI para interagir com a Finance Manager API.")


async def _request(method: str, path: str, **kwargs) -> httpx.Response:
    base_url = os.getenv("API_BASE_URL", DEFAULT_BASE_URL)
    async with httpx.AsyncClient(base_url=base_url, timeout=10) as client:
        response = await client.request(method, path, **kwargs)
        return response


def _run(coro):
    return asyncio.run(coro)


def _print_response(response: httpx.Response) -> None:
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        typer.secho(
            f"Erro {exc.response.status_code}: {exc.response.text}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)
    data = response.json()
    typer.echo(json.dumps(data, indent=2, ensure_ascii=False))


@app.command("users-list")
def users_list() -> None:
    """Listar todos os usuários cadastrados na API."""

    response = _run(_request("GET", "/users"))
    _print_response(response)


@app.command("users-create")
def users_create(
    name: str = typer.Option(..., "--name", help="Nome do usuário"),
    email: str = typer.Option(..., "--email", help="Email do usuário"),
    monthly_income: float = typer.Option(5000.0, "--monthly-income", help="Renda mensal"),
) -> None:
    """Criar um novo usuário via API."""

    payload = {"name": name, "email": email, "monthly_income": monthly_income}
    response = _run(_request("POST", "/users", json=payload))
    _print_response(response)


@app.command("accounts-list")
def accounts_list(
    user_id: str = typer.Option(..., "--user-id", help="ID do usuário dono das contas"),
) -> None:
    """Listar contas de um usuário."""

    response = _run(_request("GET", "/accounts", params={"user_id": user_id}))
    _print_response(response)


@app.command("report-export")
def report_export(
    user_id: str = typer.Option(..., "--user-id", help="ID do usuário para geração do relatório"),
) -> None:
    """Solicitar relatório de transações para um usuário."""

    response = _run(_request("GET", f"/reports/transactions/{user_id}"))
    _print_response(response)


@app.command("transactions-create")
def transactions_create(
    user_id: str = typer.Option(..., "--user-id"),
    account_id: str = typer.Option(..., "--account-id"),
    amount: float = typer.Option(..., "--amount"),
    category: str = typer.Option("general", "--category"),
    description: str = typer.Option("CLI transaction", "--description"),
    tx_type: str = typer.Option("expense", "--type", help="expense|income"),
) -> None:
    """Criar uma transação simples."""

    payload = {
        "user_id": user_id,
        "account_id": account_id,
        "amount": amount,
        "category": category,
        "description": description,
        "type": tx_type,
    }
    response = _run(_request("POST", "/transactions", json=payload))
    _print_response(response)


if __name__ == "__main__":
    app()
