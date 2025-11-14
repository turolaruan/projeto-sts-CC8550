"""Custom site hooks used during mutation tests."""

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
os.environ.setdefault("PROJECT_ROOT", str(PROJECT_ROOT))

if Path.cwd().name == "mutants":
    os.environ.setdefault("PYTEST_ADDOPTS", "-qq --disable-warnings --no-header --no-summary")



try:
    import mutmut.__main__ as _mutmut_main  # type: ignore
except Exception:  # pragma: no cover - only during mutation runs
    _mutmut_main = None
else:
    _orig_record = getattr(_mutmut_main, "record_trampoline_hit", None)

    if _orig_record is not None:

        def _record_trampoline_hit(name: str) -> None:  # pragma: no cover - exercised by mutmut
            _orig_record(name)

        _mutmut_main.record_trampoline_hit = _record_trampoline_hit
