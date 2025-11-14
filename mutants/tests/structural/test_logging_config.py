"""Structural tests for the logging configuration helpers."""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest
from src.config.settings import Settings
from src.utils import logging_config


def test_configure_logging_falls_back_to_basic_config(tmp_path, caplog) -> None:
    settings = Settings(
        LOG_CONFIG_PATH=str(tmp_path / "missing.yaml"),
        LOG_LEVEL="warning",
    )
    with caplog.at_level("WARNING", logger="src.utils.logging_config"):
        logging_config.configure_logging(settings)

    assert "Using basicConfig" in caplog.text


def test_configure_logging_creates_directories_and_applies_yaml(tmp_path, monkeypatch) -> None:
    log_dir = tmp_path / "logs"
    target_file = log_dir / "app.log"
    config_path = tmp_path / "logging.yaml"
    config_path.write_text(
        dedent(
            f"""
            version: 1
            handlers:
              file:
                class: logging.FileHandler
                formatter: simple
                filename: "{target_file}"
            formatters:
              simple:
                format: "%(levelname)s - %(message)s"
            root:
              handlers: [file]
              level: INFO
            """
        ),
        encoding="utf-8",
    )

    settings = Settings(
        LOG_CONFIG_PATH=str(config_path),
        LOG_LEVEL="info",
    )

    called = {}

    def fake_dict_config(config):
        called["config"] = config

    monkeypatch.setattr(logging_config.logging.config, "dictConfig", fake_dict_config)

    logging_config.configure_logging(settings)

    assert log_dir.exists()
    assert called["config"]["handlers"]["file"]["filename"] == str(target_file)
