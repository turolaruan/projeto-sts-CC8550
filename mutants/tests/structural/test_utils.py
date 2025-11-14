"""Structural tests covering utility helpers such as database, serializers and logger."""

from __future__ import annotations

import importlib
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from bson import ObjectId

from src.utils import database, logger as logger_module, serializers


class TestDatabaseHelpers(unittest.TestCase):
    def setUp(self):
        database._get_client.cache_clear()

    @patch("src.utils.database.AsyncIOMotorClient")
    @patch("src.utils.database.get_settings")
    def test_get_client_is_cached(self, mock_get_settings, mock_motor_client):
        settings = SimpleNamespace(mongodb_uri="mongodb://example", mongodb_database="finance")
        mock_get_settings.return_value = settings

        first_client = database._get_client()
        second_client = database._get_client()

        self.assertIs(first_client, second_client)
        mock_motor_client.assert_called_once_with(settings.mongodb_uri)

    @patch("src.utils.database._get_client")
    @patch("src.utils.database.get_settings")
    def test_get_database_returns_named_database(self, mock_get_settings, mock_get_client):
        settings = SimpleNamespace(mongodb_database="finance")
        mock_get_settings.return_value = settings
        fake_db = MagicMock()
        mock_get_client.return_value = {settings.mongodb_database: fake_db}

        database_instance = database.get_database()

        self.assertIs(database_instance, fake_db)
        mock_get_client.assert_called_once()


class TestSerializerHelpers(unittest.TestCase):
    def test_serialize_document_converts_object_ids(self):
        doc = {"_id": "abc", "nested": ObjectId()}
        serialized = serializers.serialize_document(doc)
        self.assertNotIn("_id", serialized)
        self.assertEqual(serialized["id"], "abc")
        self.assertEqual(serialized["nested"], str(doc["nested"]))


class TestLoggerConfiguration(unittest.TestCase):
    def setUp(self):
        importlib.reload(logger_module)

    @patch("src.utils.logger.get_settings")
    def test_logger_configures_once_and_binds_name(self, mock_get_settings):
        settings = SimpleNamespace(log_level="INFO")
        mock_get_settings.return_value = settings
        fake_logger = MagicMock()
        with patch.object(logger_module, "logger", fake_logger):
            bound = logger_module.get_logger("component")
            logger_module.get_logger()  # second call should reuse configuration

        fake_logger.remove.assert_called_once()
        self.assertGreaterEqual(fake_logger.add.call_count, 2)  # console + file sink
        fake_logger.bind.assert_called_once_with(component="component")
        self.assertIs(bound, fake_logger.bind.return_value)

