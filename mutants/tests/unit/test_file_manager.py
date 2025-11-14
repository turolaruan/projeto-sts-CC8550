"""Tests for FileManager and ReportService."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.utils import FileManager
from tests.fixtures.factories import make_transaction_model


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = TemporaryDirectory()
        self.addCleanup(self.tmp_dir.cleanup)
        self.base_path = Path(self.tmp_dir.name)

    def test_export_transactions_creates_csv(self):
        manager = FileManager(base_dir=self.base_path)
        transactions = [
            make_transaction_model(amount=100),
            make_transaction_model(amount=200),
        ]

        report = manager.export_transactions(transactions)

        self.assertTrue(Path(report.file_path).exists())
        metrics = {
            "total_transactions": report.total_transactions,
            "total_amount": report.total_income + report.total_expenses,
        }
        expected = {"total_transactions": 2, "total_amount": 300}
        for metric, expected_value in expected.items():
            with self.subTest(metric=metric):
                self.assertEqual(metrics[metric], expected_value)
