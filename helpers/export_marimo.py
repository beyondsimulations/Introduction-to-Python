"""Export marimo notebooks to WASM HTML under _site/notebooks/.

Runs as a Quarto post-render step (after convert_qmd_to_md.py). Skips
underscore-prefixed files (templates). Lab notebooks and exercises
(nb_*.py, exercises/ex_*.py) export editable (--mode edit); solution
notebooks (solutions/sol_*.py) export read-only (--mode run) so students
can't edit past the answers. All land in _site/notebooks/ flat, keyed by
filename stem. Every export ships the same ~700-file marimo asset bundle, so
after exporting we keep one copy at _site/notebooks/assets/ and point each
notebook at it — the browser then caches the bundle across notebooks and the
site shrinks from ~900 MB to ~30 MB.

Shells out to `uv run marimo` so it works regardless of how Quarto launches
this post-render script (Quarto's python vs the uv-managed project env).
"""
import shutil
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


def share_assets() -> None:
    """Replace the per-notebook assets/ copies with one shared folder."""
    shared = OUT / "assets"
    shutil.rmtree(shared, ignore_errors=True)
    for nb_dir in sorted(p for p in OUT.iterdir() if p.is_dir() and p != shared):
        assets = nb_dir / "assets"
        if not assets.is_dir():
            continue
        if shared.exists():
            shutil.rmtree(assets)
        else:
            assets.rename(shared)
        index = nb_dir / "index.html"
        html = index.read_text().replace('"./assets/', '"../assets/')
        # marimo's exporter embeds its default runtime config, where auto_instantiate
        # is off (0.23): cells then sit idle until Run all. Flip it so the notebook runs
        # on load (verified in headless Chromium, 2026-09-12).
        html = html.replace('auto_instantiate": false', 'auto_instantiate": true')
        index.write_text(html)
    # With the shared bundle, mo.notebook_location() resolves to _site/notebooks/,
    # so data files must live there too (spot-check 2026-09-12: pandas labs fetched
    # /notebooks/public/orders.csv, got the 404 page, and parsed it as a table).
    shutil.copytree(NOTEBOOKS / "public", OUT / "public", dirs_exist_ok=True)


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
    collisions = {p.stem for p in editable} & {p.stem for p in readonly}
    if collisions:
        print(f"stem collision between editable and solutions exports: {sorted(collisions)}", file=sys.stderr)
        return 1
    # Ensure the output tree exists even when run standalone (before any render).
    OUT.mkdir(parents=True, exist_ok=True)
    failures = [nb for nb in editable if not export(nb, "edit")]
    failures += [nb for nb in readonly if not export(nb, "run")]
    if failures:
        return 1
    share_assets()
    return 0


if __name__ == "__main__":
    sys.exit(main())
