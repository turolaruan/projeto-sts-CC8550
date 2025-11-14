"""Wrapper runner to keep pytest output minimal during mutmut runs."""

from __future__ import annotations

import os
import subprocess
import sys

DEFAULT_ARGS = ["-qq", "--disable-warnings", "--no-header", "--no-summary"]

def main() -> int:
    cmd = [sys.executable, "-m", "pytest", *DEFAULT_ARGS, *sys.argv[1:]]
    return subprocess.call(cmd, env=os.environ)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
