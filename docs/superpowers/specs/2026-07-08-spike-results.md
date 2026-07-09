# WASM Spike Results — 2026-07-09

**Purpose:** Settle the two day-1 spikes from the overhaul plan (Task 1) — the
download format (decides the grader's primary path) and the browser-persistence
behavior (decides the honest student-facing copy). Verified empirically by
driving the actual exported WASM notebook in a real browser engine (Playwright /
Chromium), not from docs.

## Environment

| Item | Value |
|---|---|
| marimo version | **0.23.13** |
| Export command | `uv run marimo export html-wasm spike_nb.py -o spike_out --mode edit` |
| Served as | static files over `python -m http.server` (same-origin, no iframe) |
| Browser engine | Chromium via Playwright (UA `Chrome/150.0.0.0`, macOS) |
| Notebook | 4-cell spike: `spike_answer = None`, edited to `42` in the browser |

## Spike 1 — Download format → **DECORATED NOTEBOOK** ✅

The notebook menu → **Download → "Download Python code"** produces the
**decorated marimo notebook format**, byte-for-byte:

```python
import marimo

__generated_with = "unknown"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    spike_answer = 42  # edited in browser
    return (spike_answer,)

...

if __name__ == "__main__":
    app.run()
```

- It is **not** a flat topologically-ordered script. It carries `@app.cell`
  decorators and the `if __name__ == "__main__": app.run()` footer.
- The student's edit (`spike_answer = 42`) is present — the download reflects
  the current in-browser state, not the original.
- **Grader consequence:** the `app.run()` path (Task 8's `hasattr(module, "app")`
  branch) is the **primary** path. The flat-script branch stays as a fallback
  for hand-mangled submissions but will rarely trigger. Keep both.
- Confirms spec §9 (download-as-`.py` in edit mode) and the "code only, no
  `mo.ui` state" assumption: the download is pure source.

Other download options present (not used by students): Download as HTML,
HTML (exclude code), Markdown, ipynb.

## Spike 2 — Persistence / resume → **URL-FRAGMENT based, NOT auto-restore** ⚠️

This is the important finding and it **corrects an over-optimistic claim in the
approved spec** (§4 and §9). Tested three ways:

| Scenario | Result |
|---|---|
| Edit `= 42`, save (Cmd/Ctrl+S), **reload the same URL** (hash intact) | ✅ edit **restored** |
| Edit `= 42`, save, then open the **bare URL** (`http://host/`, no `#code`) | ❌ loads **original** (`= None`) |
| Read IndexedDB `/marimo` → `FILE_DATA` after a bare-URL reload | file still contains `= 42`, but it is **not loaded into the editor** |

**Mechanism (marimo 0.23.13):** on every edit/save, marimo encodes the whole
notebook into the **URL fragment** (`#code/<lz-compressed>`), updating it live.
It *also* writes the notebook to an IndexedDB-backed virtual filesystem
(`/marimo` DB, `FILE_DATA` store). But a **fresh visit to the bare URL does NOT
auto-restore from IndexedDB** — it re-fetches the server's original notebook.
Persistence therefore rides on the **URL fragment**, which survives:

- ✅ page reload / Cmd+R (URL, including the fragment, is preserved)
- ✅ "reopen closed tab" (Cmd+Shift+T) and back/forward history (fragment preserved)
- ❌ closing the tab and re-clicking the tutorial page's link (that link is the
  **bare** URL — the student lands on a clean original)
- ❌ a different browser or machine (fragment is local to that URL entry)

localStorage itself holds only UI chrome (sidebar/panel layout) — **no notebook
content**. So the spec's phrase "stored in this browser" is technically true
(IndexedDB + the URL you kept) but the practical guarantee is much weaker than
"your work usually reappears when you come back."

### Consequence for student-facing copy (Task 4 / spec §4)

The spec's launcher copy ("Your work usually resumes automatically when you come
back **on the same computer and browser**") is **misleading** and must be
reworded to the honest version:

> Your work is kept **only in this browser tab's address**. If you **reload**
> (Cmd/Ctrl+R) it stays. But if you **close the tab and open the link again**,
> you start from a clean notebook. There is no cross-device sync in the browser.
> **Download your `.py` before you leave — that download is the only guaranteed
> copy.** (Want your work to follow you between devices? Use *Open in molab*.)

This strengthens, rather than weakens, the pedagogical goal: the weekly
"download your `.py`" ritual is now the *primary* persistence path, exactly
mirroring the checkpoint submission motion. molab remains the real
cross-device option.

**Action flagged to Tobias:** this contradicts an approved-spec sentence — the
Task 4 launcher page will use the corrected wording above (pending your OK), and
spec §4/§9 should be amended to match reality.

## Reproduction notes

- The very first `#code/` fragment captured looked "unchanged" because the
  notebook preamble is identical; the real diff is deep in the LZ payload. The
  edited fragment is measurably longer (468 vs ~440 chars) and restores `= 42`.
- IndexedDB inspection: DB name `/marimo`, object store `FILE_DATA`, key
  `/marimo/notebook.py`, `contents` is a `Uint8Array` of the decorated source.
