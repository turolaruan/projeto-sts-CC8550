"""Unit tests for ReportService."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.services import ReportService
from src.utils import FileManager
from tests.fixtures.factories import make_transaction_model
from tests.fixtures.memory_repositories import MemoryTransactionRepository


class TestReportService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.repository = MemoryTransactionRepository()
        self.temp_dir = TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.service = ReportService(self.repository, FileManager(base_dir=Path(self.temp_dir.name)))

    async def test_report_service_exports_transactions(self):
        user_id = "user-report"
        tx1 = make_transaction_model(user_id=user_id)
        tx2 = make_transaction_model(user_id=user_id, amount=250)
        self.repository.storage[tx1.id] = tx1.model_dump()
        self.repository.storage[tx2.id] = tx2.model_dump()

        report = await self.service.export_transactions(user_id)

        self.assertTrue(Path(report.file_path).exists())
        for attr, expected in {"total_transactions": 2}.items():
            with self.subTest(attr=attr):
                self.assertEqual(getattr(report, attr), expected)
