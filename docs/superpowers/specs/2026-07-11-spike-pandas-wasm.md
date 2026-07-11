# Spike: pandas + `public/` files in WASM notebooks — 2026-07-11

**Purpose:** Settle the `pd.read_csv` / `public/` story for Sessions VIII–IX,
following up the 2026-07-10 spike (`docs/authoring-conventions.md`, "Data in
notebooks") which only tested `open()` / `Path.read_text()` on plain text.
This spike tests three candidate patterns for loading a `public/*.csv` file
with pandas, in both a real exported-WASM browser run and a local run.

## Environment

| Item | Value |
|---|---|
| marimo version | **0.23.13** |
| Probe notebook | `notebooks/_probe_wasm.py` (underscore-prefixed — skipped by `helpers/export_marimo.py`'s glob, deleted before commit) |
| Probe data | `notebooks/public/probe.csv` (5 data rows, header `a,b`) |
| Local leg | `importlib`-loaded probe module, `app.run()`, inspect returned defs (`helpers/validate_notebooks.py`'s own glob skips underscore-prefixed files, so it can't target the probe directly) |
| WASM export | `uv run marimo export html-wasm notebooks/_probe_wasm.py -o /tmp/probe_export --mode run` |
| WASM serve | `python3 -m http.server 8765 --directory /tmp/probe_export` (same-origin, no iframe) |
| Browser engine | Chromium via Playwright |

## Patterns tested

- **A** — plain path string into `pd.read_csv`: `pd.read_csv(str(mo.notebook_location() / "public" / "probe.csv"))`
- **B** — `urllib.request.urlopen(str(loc))` → `io.StringIO` → `pd.read_csv` (the 2026-07-10 spike's known-good text path, adapted for pandas)
- **C** — inline `io.StringIO` control (no file access at all; must always work)

## Results matrix

| Pattern | Local (`app.run()`) | WASM (real browser) |
|---|---|---|
| A (plain path → `pd.read_csv`) | ✅ `A ok: 5 rows` | ✅ `A ok: 5 rows` |
| B (`urlopen` → `StringIO` → `pd.read_csv`) | ❌ `B FAIL: ValueError: unknown url type: '/Users/.../notebooks/public/probe.csv'` | ✅ `B ok: 5 rows` |
| C (inline `StringIO`) | ✅ `C ok: 2 rows` | ✅ `C ok: 2 rows` |

Exact local output (`app.run()` returned defs):
```
A ok: 5 rows | B FAIL: ValueError: unknown url type: '/Users/vlcek/development/lectures/Introduction-to-Python/notebooks/public/probe.csv' | C ok: 2 rows
```

Exact WASM output (accessibility snapshot of the rendered cell outputs, 0
console errors on the run that produced this snapshot):
```
'A ok: 5 rows'
'B ok: 5 rows'
'C ok: 2 rows'
```

**Exporter-copies-`public/`-confirmation:** `marimo export html-wasm` printed
"The public folder next to your notebook was copied to /tmp/probe_export." and
`ls /tmp/probe_export/public/` showed `probe.csv` — the exporter copies the
whole `notebooks/public/` directory into the export root, confirming the
2026-07-10 finding still holds.

## The headline finding: Pattern A works in WASM

This **corrects** the 2026-07-10 spike's implicit generalization. That spike
found `open(path)` and `path.read_text()` fail on the `URLPath` marimo returns
in WASM, and concluded file access there needs `urllib.request.urlopen`. That
conclusion is true for `open()`/`read_text()`, but **`pd.read_csv` is not
`open()`** — pandas' CSV reader has its own I/O layer (`pandas.io.common`) that
recognizes a string beginning with a URL scheme (`http://`, `https://`, …) and
fetches it itself, independent of the builtin `open()`. In WASM,
`mo.notebook_location()` yields a `URLPath` whose `str()` is an `http://`
URL (the page's own origin), so `pd.read_csv(str(loc))` fetches it directly —
and pyodide's bundled `pyodide-http` package patches the underlying transport
so that fetch succeeds inside the pyodide sandbox. Locally,
`mo.notebook_location()` yields a plain filesystem path, and `pd.read_csv`
handles plain paths natively too. So **the same one-line call works in both
environments** — no `try`/`except` fallback is needed, unlike the plain-text
case. Pattern B (`urllib.request.urlopen`) still works in WASM (pyodide-http
patches `urllib` globally) but is unnecessary complexity for pandas loading
specifically, and it fails locally on a plain filesystem path (`urlopen`
requires a URL scheme, not a bare path — hence `ValueError: unknown url type`).

## Noise observed, not a verdict-blocker

The **first** WASM page load in this session hit a **transient CDN fetch
failure**: `python_dateutil-2.9.0.post0-py2.py3-none-any.whl` failed with
`net::ERR_SOCKET_NOT_CONNECTED` while pyodide was loading pandas' dependency
packages, which made `import pandas` itself raise `ImportError: Unable to
import required dependency dateutil` in every downstream cell. A plain
`curl -sI` against the same jsdelivr URL immediately after returned `200 OK`,
and a page reload loaded cleanly with 0 console errors and all three patterns
passing. This looks like ordinary network flakiness in package-fetching over
many small wheel downloads, not a systemic pandas/pyodide incompatibility —
but it is a real-world failure mode students may hit (slow/unstable wifi on
lab day). Not in scope to fix in this spike; worth a one-line mention in
Session VIII lab instructions ("if pandas fails to import, reload the page").

## Canonical loader — execution-verified in both environments

The probe notebook's cells were replaced with the loader pattern (verified
with `probe.csv` in place of `orders.csv`, global named `orders`; the executed
re-verification wrapped the two operations in a `_load_orders()` helper — same
path construction, same `pd.read_csv(str(_loc))` call, so the flattened
canonical form below is substantively verified) and re-run end to end:

- **Local:** `orders ok: 5 rows, cols=['a', 'b']`
- **WASM:** `'orders ok: 5 rows, cols=['a', 'b']'` rendered in the browser, 0 console errors

Canonical form (what downstream copies — `orders.csv` is the real filename;
assumes an earlier cell does `import pandas as pd` and returns `(pd,)`):

```python
@app.cell(hide_code=True)
def _(mo, pd):
    _loc = mo.notebook_location() / "public" / "orders.csv"
    orders = pd.read_csv(str(_loc))
    return (orders,)
```

No `try`/`except` fallback is required — Pattern A alone is the canonical
loader. This is simpler than the shape sketched in the task brief (which
hedged with a `urlopen` fallback based on the pre-pandas spike); the fallback
turned out to be dead code once tested.

## Verdict

`public/*.csv` + `pd.read_csv(str(mo.notebook_location() / "public" / "<file>"))`
is safe to use starting Session VIII. `docs/authoring-conventions.md`'s "Data
in notebooks" bullet is updated accordingly with this loader as the canonical
copy-paste pattern.
