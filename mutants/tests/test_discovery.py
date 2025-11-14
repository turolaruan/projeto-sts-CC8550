"""Custom discovery entry-point so `python -m unittest discover tests` works."""

from __future__ import annotations

import unittest
from pathlib import Path

TEST_ROOT = Path(__file__).parent
TEST_SUBDIRS = ("unit", "integration", "functional", "mutation", "performance")


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    """Aggregate tests from nested directories that don't match the default pattern."""

    suite = unittest.TestSuite()
    discovered_pattern = pattern or "test*.py"
    for subdir in TEST_SUBDIRS:
        start_dir = TEST_ROOT / subdir
        if start_dir.is_dir():
            suite.addTests(
                loader.discover(str(start_dir), pattern=discovered_pattern, top_level_dir=str(start_dir))
            )
    return suite
