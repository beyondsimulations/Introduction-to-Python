"""Export all marimo notebooks to editable WASM HTML under _site/notebooks/.

Runs as a Quarto post-render step (after convert_qmd_to_md.py). Skips
underscore-prefixed files (templates). Exercises land in _site/notebooks/ too,
flat, keyed by filename stem.

Shells out to `uv run marimo` so it works regardless of how Quarto launches
this post-render script (Quarto's python vs the uv-managed project env).
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = ROOT / "notebooks"
OUT = ROOT / "_site" / "notebooks"


def export(nb: Path) -> bool:
    dest = OUT / nb.stem
    cmd = [
        "uv", "run", "marimo", "export", "html-wasm",
        str(nb), "-o", str(dest), "--mode", "edit",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAILED {nb.name}:\n{result.stderr}", file=sys.stderr)
        return False
    print(f"exported {nb.name} -> {dest.relative_to(ROOT)}")
    return True


def main() -> int:
    sources = sorted(
        p
        for pattern in ("nb_*.py", "exercises/ex_*.py")
        for p in NOTEBOOKS.glob(pattern)
        if not p.name.startswith("_")
    )
    if not sources:
        print("no notebooks found — nothing to export")
        return 0
    # Ensure the output tree exists even when run standalone (before any render).
    OUT.mkdir(parents=True, exist_ok=True)
    failures = [nb for nb in sources if not export(nb)]
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
