"""Structural tests for src package metadata exposure."""

from __future__ import annotations

import importlib.metadata as importlib_metadata
import os
import unittest
from unittest.mock import patch

import src
import pytest

pytestmark = pytest.mark.skipif(
    os.getenv("MUTANT_UNDER_TEST") not in (None, "0"),
    reason="Mutmut instrumentation rewrites module",
)


class TestVersionAccess(unittest.TestCase):
    def test_returns_installed_version(self):
        with patch("importlib.metadata.version", return_value="1.2.3"):
            func = getattr(src, "__getattr__", None)
            self.assertIsNotNone(func, "__getattr__ must be defined on src")
            self.assertEqual(func("__version__"), "1.2.3")

    def test_returns_default_when_package_missing(self):
        with patch(
            "importlib.metadata.version",
            side_effect=importlib_metadata.PackageNotFoundError,
        ):
            func = getattr(src, "__getattr__", None)
            self.assertIsNotNone(func, "__getattr__ must be defined on src")
            self.assertEqual(func("__version__"), "0.0.0")

    def test_unknown_attribute_raises(self):
        func = getattr(src, "__getattr__", None)
        self.assertIsNotNone(func, "__getattr__ must be defined on src")
        with self.assertRaises(AttributeError):
            func("not_there")
