"""Export marimo notebooks to WASM HTML under _site/notebooks/.

Runs as a Quarto post-render step (after convert_qmd_to_md.py). Skips
underscore-prefixed files (templates). Lab notebooks and exercises
(nb_*.py, exercises/ex_*.py) export editable (--mode edit); solution
notebooks (solutions/sol_*.py) export read-only (--mode run) so students
can't edit past the answers. All land in _site/notebooks/ flat, keyed by
filename stem.

Shells out to `uv run marimo` so it works regardless of how Quarto launches
this post-render script (Quarto's python vs the uv-managed project env).
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = ROOT / "notebooks"
OUT = ROOT / "_site" / "notebooks"


def export(nb: Path, mode: str = "edit") -> bool:
    dest = OUT / nb.stem
    cmd = [
        "uv", "run", "marimo", "export", "html-wasm",
        str(nb), "-o", str(dest), "--mode", mode,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FAILED {nb.name}:\n{result.stderr}", file=sys.stderr)
        return False
    print(f"exported {nb.name} ({mode}) -> {dest.relative_to(ROOT)}")
    return True


def main() -> int:
    editable = sorted(
        p
        for pattern in ("nb_*.py", "exercises/ex_*.py")
        for p in NOTEBOOKS.glob(pattern)
        if not p.name.startswith("_")
    )
    readonly = sorted(
        p for p in NOTEBOOKS.glob("solutions/sol_*.py") if not p.name.startswith("_")
    )
    if not editable and not readonly:
        print("no notebooks found — nothing to export")
        return 0
    # Ensure the output tree exists even when run standalone (before any render).
    OUT.mkdir(parents=True, exist_ok=True)
    failures = [nb for nb in editable if not export(nb, "edit")]
    failures += [nb for nb in readonly if not export(nb, "run")]
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
