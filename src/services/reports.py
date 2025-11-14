"""Service for generating reports and exports."""

from __future__ import annotations

from src.models import ReportPayload, TransactionModel
from src.repositories import TransactionRepository
from src.utils import FileManager


class ReportService:
    """Generates file based reports for the API."""

    def __init__(self, repository: TransactionRepository, file_manager: FileManager | None = None) -> None:
        self.repository = repository
        self.file_manager = file_manager or FileManager()

    async def export_transactions(self, user_id: str) -> ReportPayload:
        """Export all transactions for a user to CSV."""

        transactions = await self.repository.list({"user_id": user_id})
        return self.file_manager.export_transactions(transactions)
