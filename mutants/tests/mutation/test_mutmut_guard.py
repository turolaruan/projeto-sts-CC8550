"""Auxiliary guard to trigger failures when mutmut requests it."""

from __future__ import annotations

import os

import pytest


def test_mutmut_forced_failure_guard() -> None:
    """Fail fast when mutmut sets MUTANT_UNDER_TEST=fail."""

    if os.environ.get("MUTANT_UNDER_TEST") == "fail":
        pytest.fail("Mutmut verification run", pytrace=False)
