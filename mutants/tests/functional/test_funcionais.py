"""Functional API tests covering HTTP flows and error handling."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from src.app import create_app
from src.config.settings import Settings
from src.services.dependencies import get_user_service
from src.utils.exceptions import EntityNotFoundError
from tests.structural.helpers import build_user


@pytest.fixture()
def app_factory(monkeypatch):
    """Return a factory that builds FastAPI apps with safe side effects."""

    def factory(*, settings: Settings | None = None):
        base_settings = settings or Settings(APP_NAME="API Funcional", DEBUG=False, ENVIRONMENT="testing")

        async def noop() -> None:
            return None

        monkeypatch.setattr("src.app.configure_logging", lambda *_: None)
        monkeypatch.setattr("src.app.mongo_manager.connect", noop)
        monkeypatch.setattr("src.app.mongo_manager.close", noop)
        monkeypatch.setattr("src.controllers.health.get_settings", lambda: base_settings)
        return create_app(base_settings)

    return factory


class SuccessfulUserService:
    """Stub service used to emulate successful user operations."""

    def __init__(self, user):
        self.user = user
        self.created_payloads = []
        self.deleted_ids = []

    async def create_user(self, payload):
        self.created_payloads.append(payload)
        return self.user

    async def delete_user(self, user_id: str) -> None:
        self.deleted_ids.append(user_id)


class NotFoundUserService:
    """Stub service that always raises not-found errors."""

    def __init__(self, message: str = "User missing") -> None:
        self.message = message

    async def get_user(self, user_id: str):
        raise EntityNotFoundError(self.message)


def test_health_endpoint_returns_environment_metadata(app_factory) -> None:
    app = app_factory(settings=Settings(APP_NAME="Saude API", ENVIRONMENT="qa", DEBUG=False))

    with TestClient(app) as client:
        response = client.get("/api/health/")

    assert response.status_code == 200
    payload = response.json()
    assert payload == {"status": "ok", "application": "Saude API", "environment": "qa"}


def test_user_endpoints_support_post_and_delete(app_factory) -> None:
    app = app_factory()
    user = build_user(name="Usuario HTTP")
    service = SuccessfulUserService(user)
    app.dependency_overrides[get_user_service] = lambda: service

    with TestClient(app) as client:
        response = client.post(
            "/api/users/",
            json={
                "name": "Cliente HTTP",
                "email": "cliente@example.com",
                "default_currency": "BRL",
            },
        )
        delete_response = client.delete(f"/api/users/{user.id}")

    app.dependency_overrides.clear()
    assert response.status_code == 201
    assert response.json()["id"] == user.id
    assert delete_response.status_code == 204
    assert service.created_payloads and service.created_payloads[0].email == "cliente@example.com"
    assert service.deleted_ids == [user.id]


def test_user_get_returns_404_and_error_message(app_factory) -> None:
    app = app_factory()
    app.dependency_overrides[get_user_service] = lambda: NotFoundUserService("Usuario nao encontrado")

    with TestClient(app) as client:
        response = client.get("/api/users/inexistente")

    app.dependency_overrides.clear()
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuario nao encontrado"}
