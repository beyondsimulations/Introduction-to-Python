# helpers/validate_notebooks.py
"""Headless smoke test: every notebook must import and app.run() without raising.

Catches broken cells, bad marimo structure, and accidental infinite loops
(via a hard alarm) before anything is exported or committed.
Usage: uv run python helpers/validate_notebooks.py [pattern ...]
"""
import importlib.util
import signal
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = ROOT / "notebooks"
PATTERNS = ("nb_*.py", "exercises/ex_*.py", "solutions/sol_*.py")
TIMEOUT_S = 60


class _Timeout(Exception):
    pass


def _on_alarm(signum, frame):
    raise _Timeout(f"notebook exceeded {TIMEOUT_S}s")


def run(nb: Path) -> bool:
    signal.alarm(TIMEOUT_S)
    try:
        spec = importlib.util.spec_from_file_location(nb.stem, nb)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.app.run()
    # BaseException: also catch SystemExit from stray exit() calls and the alarm
    except BaseException as exc:
        print(f"FAIL {nb.relative_to(ROOT)}: {exc!r}", file=sys.stderr)
        return False
    finally:
        signal.alarm(0)
    print(f"ok   {nb.relative_to(ROOT)}")
    return True


def main() -> int:
    patterns = sys.argv[1:] or PATTERNS
    sources = sorted(
        p
        for pattern in patterns
        for p in NOTEBOOKS.glob(pattern)
        if not p.name.startswith("_")
    )
    if not sources:
        print("no notebooks matched", file=sys.stderr)
        return 1
    # Unix-only; must run in the main thread
    signal.signal(signal.SIGALRM, _on_alarm)
    results = [run(nb) for nb in sources]  # full list first — no short-circuit, validate everything
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
