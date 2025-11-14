"""Utility helpers for interacting with the filesystem."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Iterable

from config.settings import get_settings
from src.models import ReportPayload, TransactionModel, TransactionType


class FileManager:
    """Centralizes file manipulation tasks for reports and exports."""

    def __init__(self, base_dir: Path | None = None) -> None:
        settings = get_settings()
        self.base_dir = base_dir or Path(settings.export_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def export_transactions(self, transactions: Iterable[TransactionModel]) -> ReportPayload:
        """Write a CSV report with consolidated transaction totals."""

        file_path = self.base_dir / f"transactions_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        total_expenses = 0.0
        total_income = 0.0
        tx_list = list(transactions)
        with file_path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                "id",
                "user_id",
                "account_id",
                "type",
                "category",
                "amount",
                "event_date",
                "description",
            ])
            for tx in tx_list:
                if tx.type == TransactionType.EXPENSE:
                    total_expenses += tx.amount
                else:
                    total_income += tx.amount
                writer.writerow(
                    [
                        tx.id,
                        tx.user_id,
                        tx.account_id,
                        tx.type.value,
                        tx.category,
                        tx.amount,
                        tx.event_date.isoformat(),
                        tx.description,
                    ]
                )
        return ReportPayload(
            generated_at=datetime.utcnow(),
            file_path=str(file_path),
            total_transactions=len(tx_list),
            total_expenses=round(total_expenses, 2),
            total_income=round(total_income, 2),
        )
