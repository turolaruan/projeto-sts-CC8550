"""Structural coverage for application factory, config and entrypoints."""

from __future__ import annotations

import importlib
import runpy
import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from fastapi.testclient import TestClient
from src.app import create_app
from src.config.settings import Settings


def test_settings_helpers_and_properties(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    settings = Settings(ENVIRONMENT="Production")

    assert settings.is_production is True
    assert settings.model_dump_public()["environment"] == "Production"
    assert settings.log_config_file == tmp_path / "config" / "logging.yaml"


def test_create_app_registers_routes_and_settings(monkeypatch) -> None:
    settings = Settings(APP_NAME="Structural API", DEBUG=False)
    monkeypatch.setattr("src.app.configure_logging", lambda *_: None)
    connect_mock = AsyncMock()
    close_mock = AsyncMock()
    monkeypatch.setattr("src.app.mongo_manager.connect", connect_mock)
    monkeypatch.setattr("src.app.mongo_manager.close", close_mock)
    monkeypatch.setattr("src.controllers.health.get_settings", lambda: settings)

    app = create_app(settings)
    with TestClient(app) as client:
        response = client.get("/api/health/")

    connect_mock.assert_awaited_once()
    close_mock.assert_awaited_once()
    assert response.json()["application"] == "Structural API"


def test_main_module_import_exposes_app(monkeypatch) -> None:
    monkeypatch.setattr("src.app.create_app", lambda: "APP")
    sys.modules.pop("src.main", None)
    module = importlib.import_module("src.main")
    assert module.app == "APP"


def test_main_entrypoint_runs_uvicorn(monkeypatch) -> None:
    run_mock = MagicMock()
    monkeypatch.setattr("src.app.create_app", lambda: "APP")
    monkeypatch.setattr("uvicorn.run", run_mock)
    sys.modules.pop("src.main", None)
    runpy.run_module("src.main", run_name="__main__")
    run_mock.assert_called_once()
