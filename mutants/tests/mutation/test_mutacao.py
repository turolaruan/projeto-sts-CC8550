"""Asserts that the recorded mutation results stay consistent.

Os testes de mutação são executados via mutmut (fora do fluxo normal do pytest)
e os relatórios gerados ficam em ``tests/mutation/mutmut_*.txt``.
Este módulo garante apenas que os metadados registrados em
``mutmut_summary.json`` permanecem coerentes.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

SUMMARY_FILE = Path(__file__).with_name("mutmut_summary.json")


@pytest.mark.mutation
def test_mutmut_summary_is_consistent() -> None:
    summary = json.loads(SUMMARY_FILE.read_text(encoding="utf-8"))
    required = {"account_service", "budget_service", "transaction_service"}
    assert required.issubset(summary.keys()), "esperava dados para 3 serviços principais"

    for module_name, payload in summary.items():
        total = payload["total_mutants"]
        killed = payload["killed"]
        survived = payload["survived"]
        assert total == killed + survived, f"soma inconsistente em {module_name}"
        kill_rate = payload["kill_rate"]
        assert 0 <= kill_rate <= 1
        assert pytest.approx(killed / total, rel=1e-3) == kill_rate
