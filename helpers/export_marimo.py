"""Export marimo notebooks to WASM HTML under _site/notebooks/.

Runs as a Quarto post-render step. Skips
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

# marimo boots an exported notebook from the embedded <marimo-code> and never reads
# back what a save wrote (URL hash and localStorage), so a reload reset the notebook.
# This keeps the tab's last save and hands it back on load (and to a download made
# before the next save): a reload keeps the work, a new tab starts clean.
# deploy_checkpoint.sh in the checkpoints repo injects the same script, and a test
# there fails when the two differ. Gate: helpers/check_reload.py.
# ponytail: reads marimo's one per-origin save slot; two tabs saving in the same
# millisecond could cross. Add a notebook marker check if that ever shows.
KEEP_ON_RELOAD = r"""<script>
(() => {
  const key = "saved:" + location.pathname;
  const saved = sessionStorage.getItem(key);
  addEventListener("hashchange", () => {
    const code = JSON.parse(localStorage.getItem("marimo:file"));
    if (code) sessionStorage.setItem(key, code);
  });
  if (!saved) return;
  // A save writes a bare `app = marimo.App()`: put the notebook's own line back, so
  // the page width and the download's file name survive the reload.
  const el = document.querySelector("marimo-code");
  const app = /^app = marimo\.App\(.*\)$/m;
  const own = decodeURIComponent(el.textContent).match(app);
  el.textContent = encodeURIComponent(own ? saved.replace(app, () => own[0]) : saved);
  // "Download Python code" reads marimo's saved file, which is empty until the first
  // save on this page: straight after a reload it would hand out 0 bytes.
  const createUrl = URL.createObjectURL;
  URL.createObjectURL = (blob) => {
    const empty = blob instanceof Blob && blob.size === 0 && blob.type === "text/plain";
    return createUrl.call(URL, empty ? new Blob([saved], { type: blob.type }) : blob);
  };
})();
</script>"""


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
        # Autosave is off in that config too: without Cmd/Ctrl+S nothing was saved and
        # "Download Python code" handed out an empty file. Save one second after typing
        # stops (verified in Chromium and WebKit, 2026-10-11).
        html = html.replace('autosave": "off"', 'autosave": "after_delay"')
        html = html.replace("</marimo-code>", "</marimo-code>\n" + KEEP_ON_RELOAD, 1)
        if 'autosave": "after_delay"' not in html or KEEP_ON_RELOAD not in html:
            sys.exit(f"{index}: autosave flag or <marimo-code> not found; marimo may have changed its export")
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
