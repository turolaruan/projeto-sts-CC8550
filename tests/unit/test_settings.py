"""Tests for Settings loader."""

import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from config.settings import Settings


class TestSettings(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = TemporaryDirectory()
        self.addCleanup(self.tmp_dir.cleanup)
        self.env_path = Path(self.tmp_dir.name) / ".env"

    def test_settings_reads_env(self):
        self.env_path.write_text("APP_NAME=Custom App\n", encoding="utf-8")
        with patch.dict(os.environ, {"ENVIRONMENT": "test"}, clear=False):
            settings = Settings(_env_file=self.env_path)

        for attr, expected in {"app_name": "Custom App", "environment": "test"}.items():
            with self.subTest(attr=attr):
                self.assertEqual(getattr(settings, attr), expected)
