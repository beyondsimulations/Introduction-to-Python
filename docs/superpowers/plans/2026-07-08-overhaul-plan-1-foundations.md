# Course Overhaul Plan 1: Foundations + Session I Vertical Slice

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the marimo infrastructure (template, WASM export pipeline, tutorial pages, grading system) and the complete Session I content, proving every pattern the remaining 3 plans will copy.

**Architecture:** marimo `.py` notebooks in `notebooks/` are the source of truth; a post-render step exports them to editable WASM HTML inside the Quarto `_site`. Tutorial `.qmd` pages become slim launchers with two buttons (self-hosted WASM + optional molab). Checkpoints live in a separate private repo with a grading script that re-runs submissions headlessly. Spec: `docs/superpowers/specs/2026-07-08-course-overhaul-design.md` — read it first.

**Tech Stack:** Quarto website (existing), marimo (new dependency), uv, Pyodide/WASM, pytest for the grading script.

**Sequencing:** Plans 2–4 (Part I content, Part II content + AI pages, Part III/tooling/cleanup) are written after this plan is executed and its patterns are proven. Do not start them from this document.

---

## Context for the zero-context engineer

- This repo is a Quarto course website (`quarto render` → `_site/`, deployed to GitHub Pages). `_quarto.yml` drives nav; `helpers/convert_qmd_to_md.py` runs post-render. Python env is uv-managed (`uv sync`, Python 3.12).
- marimo notebooks are plain `.py` files: cells are functions decorated with `@app.cell`; parameters = dependencies, return tuple = defined names. A global may be defined in ONE cell only (`+=` counts as a definition). Underscore-prefixed names are cell-private. ALWAYS open notebooks with `uv run marimo edit <file>` after hand-editing — marimo validates and normalizes on save.
- The course storyline: students found a campus food-delivery startup; recurring cast is Tobi (inept co-founder), an investor, German authorities, competitor MunchCorp. Sitcom tone in notebooks, restrained in slides. See spec §4.
- Verified constraints you must respect (spec §9): downloaded `.py` files contain code only (never grade `mo.ui` state); WASM code is always readable (checkpoint live-checks use hashes); WASM memory cap is 2 GB (small datasets only).

---

### Task 1: Add marimo + run the two verification spikes

**Goal:** marimo installed; the two undocumented behaviors (download format, localStorage resume) verified and recorded.

**Files:**
- Modify: `pyproject.toml` (add dependency)
- Create: `docs/superpowers/specs/2026-07-08-spike-results.md`

**Acceptance Criteria:**
- [ ] `uv run marimo --version` prints a version
- [ ] Spike results file records: (a) download format = decorated notebook OR flat script, (b) localStorage resume = works / doesn't, with marimo version and browser tested

**Verify:** `uv run marimo --version` → version string; spike file exists with both verdicts filled in (no "TBD").

**Steps:**

- [ ] **Step 1: Add marimo**

```bash
uv add marimo
uv run marimo --version
```

- [ ] **Step 2: Create a minimal spike notebook**

Write `/tmp/spike_nb.py`:

```python
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("# Spike notebook — edit this cell's text, then reload the page")
    return


@app.cell
def _():
    spike_answer = None  # change to 42 in the browser
    return (spike_answer,)


if __name__ == "__main__":
    app.run()
```

- [ ] **Step 3: Export and serve**

```bash
uv run marimo export html-wasm /tmp/spike_nb.py -o /tmp/spike_out --mode edit
cd /tmp/spike_out && python -m http.server 8765
```

Open `http://localhost:8765` in a normal (non-private) browser window.

- [ ] **Step 4: Test download format**

In the browser: edit `spike_answer = None` to `spike_answer = 42`, then use the notebook menu → Download → Python. Open the downloaded file. Record in the spike file: does it contain `@app.cell` decorators (decorated notebook format → grading uses `app.run()`) or plain top-level statements (flat script → grading uses namespace-exec)? Task 8's grader handles both — this determines which path is primary.

- [ ] **Step 5: Test localStorage resume**

With the edit from Step 4 still in the browser: reload the page (Cmd+R). Does `spike_answer = 42` survive? Close the tab entirely, reopen `http://localhost:8765` — still there? Record both results.

- [ ] **Step 6: Write results + commit**

Create `docs/superpowers/specs/2026-07-08-spike-results.md` with: marimo version, browser + version, download-format verdict, localStorage verdict (reload / tab-close), any surprises. Then:

```bash
git add pyproject.toml uv.lock docs/superpowers/specs/2026-07-08-spike-results.md
git commit -m "chore: add marimo, record WASM spike results"
```

---

### Task 2: Notebook template `notebooks/_template.py`

**Goal:** The canonical skeleton every course notebook copies: name input, exercise + reactive check + hints pattern, progress cell, wrap-up ritual.

**Files:**
- Create: `notebooks/_template.py`

**Acceptance Criteria:**
- [ ] `uv run marimo edit notebooks/_template.py` opens without errors; all cells run green
- [ ] Typing a name updates the greeting reactively; setting the example answer flips the check to ✅ and progress to 1/1

**Verify:** `uv run python -c "from notebooks import _template"` exits 0 (file is importable), then manual check in `marimo edit`.

**Steps:**

- [ ] **Step 1: Create the template**

```python
# notebooks/_template.py
# TEMPLATE — copy to nb_XX_lab_<topic>.py and replace TODO-marked content.
# Rules (spec §4): one global name per cell; += counts as a definition;
# every exercise pre-defines its answer as None; suffix exercise names (_ex1);
# underscore-prefixed names are cell-private.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook X.Y — TODO Title
    **Estimated time: TODO min · Core exercises: TODO**

    TODO: Story cold-open. 2–4 sentences, sitcom tone.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    startup_name_input = mo.ui.text(
        label="Your startup's name:", placeholder="e.g. SnackRocket"
    )
    startup_name_input
    return (startup_name_input,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(f"Welcome back to **{startup_name}**! Tobi already forgot the name again.")
    return (startup_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — TODO concept name

    TODO: teach the concept in 3–6 sentences, then show a worked example below.
    """
    )
    return


@app.cell
def _():
    # Worked example (students read + run this)
    example_price = 4.50
    example_total = example_price * 3
    print(f"Three portions cost {example_total:.2f} EUR")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — TODO one-line task

    TODO: task description referencing the story.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — replace None
    revenue_ex1 = None
    return (revenue_ex1,)


@app.cell(hide_code=True)
def _(mo, revenue_ex1):
    # Reactive check — re-runs automatically whenever the cell above changes.
    if revenue_ex1 is None:
        ex1_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
    elif revenue_ex1 == 13.50:  # TODO expected value
        ex1_ok = True
        _msg = "✅ Exercise 1.1: correct! The investor nods approvingly."
    else:
        ex1_ok = False
        _msg = "❌ Exercise 1.1: not quite — check your multiplication."
    mo.md(_msg)
    return (ex1_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "TODO: conceptual nudge, no code.",
            "💡 Hint 2 (the structure)": "TODO: code skeleton with a blank to fill.",
        }
    )
    return


@app.cell(hide_code=True)
def _(ex1_ok, mo):
    # Progress cell — extend the list as exercises are added.
    _checks = [ex1_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _tobi = "Tobi is impressed!" if _done == _total else "Tobi remains skeptical."
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} ✅** — {_tobi}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave 📦

    1. Check the progress box above — all green?
    2. **Download your work**: menu → Download → Python. Same computer + same
       browser usually restores your work automatically, but the download is
       the only guaranteed copy.
    3. Next episode: TODO teaser sentence.
    """
    )
    return


if __name__ == "__main__":
    app.run()
```

- [ ] **Step 2: Validate in marimo**

```bash
uv run marimo edit notebooks/_template.py
```

Confirm: no red cells, name input updates greeting, changing `revenue_ex1 = None` to `13.50` flips check + progress. Save (marimo normalizes formatting), quit.

- [ ] **Step 3: Commit**

```bash
git add notebooks/_template.py
git commit -m "feat: add marimo notebook template with check/hint/progress patterns"
```

---

### Task 3: WASM export pipeline

**Goal:** One command exports all notebooks to editable WASM inside `_site/notebooks/`, wired into `quarto render`.

**Files:**
- Create: `helpers/export_marimo.py`
- Modify: `_quarto.yml:3-4` (post-render list)
- Modify: `.gitignore` (if `_site` not already ignored, also ignore `notebooks/__marimo__/`)

**Acceptance Criteria:**
- [ ] `quarto render` produces `_site/notebooks/nb_01_lab_founding/index.html` (once Task 5 exists; with only the template present, exports every `nb_*.py` and `ex_*.py` it finds)
- [ ] `_template.py` is NOT exported (leading underscore excluded)

**Verify:** `uv run python helpers/export_marimo.py && ls _site/notebooks/` → one directory per notebook, none named `_template`.

**Steps:**

- [ ] **Step 1: Write the export script**

```python
# helpers/export_marimo.py
"""Export all marimo notebooks to editable WASM HTML under _site/notebooks/.

Runs as a Quarto post-render step (after convert_qmd_to_md.py). Skips
underscore-prefixed files (templates). Exercises land in _site/notebooks/ too,
flat, keyed by filename stem.
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
    failures = [nb for nb in sources if not export(nb)]
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Wire into Quarto post-render**

In `_quarto.yml`, change:

```yaml
  post-render:
    - helpers/convert_qmd_to_md.py
```

to:

```yaml
  post-render:
    - helpers/convert_qmd_to_md.py
    - helpers/export_marimo.py
```

- [ ] **Step 3: Test with the template excluded**

```bash
uv run python helpers/export_marimo.py
```

Expected: "no notebooks found" (only `_template.py` exists, and it's skipped). Then temporarily `cp notebooks/_template.py notebooks/nb_00_smoke.py`, re-run, confirm `_site/notebooks/nb_00_smoke/` appears and serves (`cd _site && python -m http.server 8766`, open `http://localhost:8766/notebooks/nb_00_smoke/`). Delete `notebooks/nb_00_smoke.py` and the export dir afterwards.

- [ ] **Step 4: Commit**

```bash
git add helpers/export_marimo.py _quarto.yml .gitignore
git commit -m "feat: export marimo notebooks to WASM in quarto post-render"
```

---

### Task 4: Tutorial launcher page pattern (`tut_01`)

**Goal:** `tutorials/tut_01_introduction.qmd` becomes the slim two-button launcher — the pattern all tutorial pages copy.

**Files:**
- Modify: `tutorials/tut_01_introduction.qmd` (full replacement of body; keep the filename so `_quarto.yml` nav is untouched)

**Acceptance Criteria:**
- [ ] Page shows: episode intro (3–5 sentences), "Open in browser" button → `/notebooks/nb_01_lab_founding/` , "Open in molab" badge → molab GitHub URL, and the honest persistence explainer from spec §4
- [ ] No exercise content remains on the page itself (it all lives in the notebook)

**Verify:** `quarto render tutorials/tut_01_introduction.qmd` → no errors; links resolve in `_site`.

**Steps:**

- [ ] **Step 1: Replace the page content**

```markdown
---
title: "Episode 1 — The Founding"
subtitle: "Programming with Python · Tutorial 01"
---

Your food-delivery startup exists as of today. It has no name (that's your
first job), no menu (your second), and a co-founder, Tobi, who has already
spent 300 EUR on stickers. In this notebook you set up prices, calculate the
first revenues, and decide whether Tobi's 9.99-for-everything pricing theory
survives contact with arithmetic.

## Work on the notebook

[Open in browser](../notebooks/nb_01_lab_founding/){.btn .btn-primary}
[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/beyondsimulations/Introduction-to-Python/blob/main/notebooks/nb_01_lab_founding.py)

**Open in browser (recommended):** runs on your machine, in this tab — no
account, no installation, and after loading no internet needed. Your work
usually reappears when you come back **on the same computer and browser**.
It is stored only in this browser: private mode, clearing browser data, or
switching devices loses it. **Download your `.py` file before you leave**
(menu → Download → Python) — that download is the only guaranteed copy, and
handing in files works exactly like this in the checkpoints.

**Open in molab:** marimo's free cloud (account required). Your copy saves to
your account and reopens on any device. Choose this if you know you will
switch computers. Optional — nothing graded ever requires it.
```

- [ ] **Step 2: Render and click through**

```bash
quarto render tutorials/tut_01_introduction.qmd
```

Serve `_site` and verify both buttons (browser button 404s until Task 5 lands — acceptable within this task if noted; re-verify after Task 5).

- [ ] **Step 3: Commit**

```bash
git add tutorials/tut_01_introduction.qmd
git commit -m "feat: tut_01 becomes two-button marimo launcher page"
```

---

### Task 5: Session I lab notebook `nb_01_lab_founding.py`

**Goal:** The complete Episode 1 lab notebook (~45–60 min): variables, numeric types, strings/f-strings, arithmetic — all four checkpoint task types included.

**Files:**
- Create: `notebooks/nb_01_lab_founding.py` (copy `_template.py`, then build out)

**Acceptance Criteria:**
- [ ] Sections: 1 Variables (founding: name, prices), 2 Numbers & arithmetic (revenue math, Tobi's 9.99 theory), 3 Strings & f-strings (the first receipt), boss exercise (full day-one summary)
- [ ] ≥6 core exercises + ≥2 bonus; each has placeholder (`= None`), reactive check, 2-tier hint accordion
- [ ] All four CP task types present: write-code, trace (`mo.ui.radio` predict-then-reveal, ungraded), fix-Tobi's-bug, MCQ
- [ ] Progress cell counts core exercises only; wrap-up ritual cell present
- [ ] Runs clean in `marimo edit` AND as WASM export

**Verify:** `uv run python helpers/export_marimo.py && open http://localhost:8766/notebooks/nb_01_lab_founding/` — work through every exercise; progress reaches N/N.

**Steps:**

- [ ] **Step 1: Copy template and write content**

Follow the template patterns exactly. Content requirements (write real exercises from these specs — the checks and hints must match the exercise numbers):

| Ex | Type | Task | Check |
|---|---|---|---|
| 1.1 core | write | Create `menu_item_ex11` (str), `price_ex11` (float 8.90), `portions_ex11` (int 3) | types + values |
| 1.2 core | write | `revenue_ex12` = price × portions | `== 26.70` (use `round(x, 2)`) |
| 2.1 core | trace | Radio: what does `print(7 // 2, 7 % 2)` print? | reveal + explanation (ungraded) |
| 2.2 core | write | Tobi's theory: everything costs 9.99. `margin_ex22` = 9.99 − cost 7.40 | `== 2.59` |
| 2.3 core | fix | Tobi's bug: `total = "9.99" * 3` — fix to numeric | `total_ex23 == 29.97` |
| 3.1 core | write | f-string receipt line `receipt_ex31` = `"3x Pad Thai ...... 26.70 EUR"` via f-string with `:.2f` | string equality |
| 3.2 bonus | write | Multi-line receipt with `\n` and alignment `:>8` | string equality |
| boss core | write | `day_one_summary_ex40`: f-string combining name, revenue, margin | contains-checks (name-agnostic: test computed numbers, not the name) |
| MCQ core | mcq | "Which is a valid variable name?" answered as `answer_ex50 = "b"` | `== "b"` |

Story beats to include as `mo.md` cells between sections: Tobi's sticker budget (cold open, done in Task 4's intro too — repeat one line), the 9.99 "psychological pricing" argument before 2.2, MunchCorp launching "the same app but worse" as boss-exercise motivation.

- [ ] **Step 2: Validate both runtimes**

```bash
uv run marimo edit notebooks/nb_01_lab_founding.py   # all cells green, save
uv run python helpers/export_marimo.py               # export succeeds
```

Serve and complete the whole notebook in the browser as a student would.

- [ ] **Step 3: Commit**

```bash
git add notebooks/nb_01_lab_founding.py
git commit -m "feat: Episode 1 lab notebook (founding, variables, arithmetic, f-strings)"
```

---

### Task 6: Session I in-lecture exercises (3 files)

**Goal:** Three one-screen, 5–10-minute predict-first exercises for lecture 1's three blocks.

**Files:**
- Create: `notebooks/exercises/ex_01_a.py` (variables: fix the founding-form), `notebooks/exercises/ex_01_b.py` (arithmetic: the sticker budget), `notebooks/exercises/ex_01_c.py` (f-strings: one receipt line)

**Acceptance Criteria:**
- [ ] Each: ≤1 screen, one concept, one exercise + one reactive check, closes with "Nothing to save — this was a sandbox."
- [ ] Each exports via the pipeline (they match `exercises/ex_*.py`)

**Verify:** `uv run python helpers/export_marimo.py` exports all three; each completable in <10 min.

**Steps:**

- [ ] **Step 1: Write the three exercises** — pattern for `ex_01_a.py` (b and c follow identically with their own task):

```python
# notebooks/exercises/ex_01_a.py
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # ⚡ Quick exercise: the founding form (5 min)

    Tobi filled in the company register form — as Python variables. Two lines
    crash and one has the wrong type. **First predict which, then fix them.**
    """
    )
    return


@app.cell
def _():
    # FIX TOBI'S FORM BELOW (3 problems — all run, all wrong)
    company_type = "UG (haftungsbeschränkt)"
    first_employee = "tobi "       # problem 1: registrar wants exact "Tobi"
    share_capital = "300"           # problem 2: that's text, not money
    founded_year = "2026"           # problem 3: should be a number
    return (company_type, first_employee, founded_year, share_capital)


@app.cell(hide_code=True)
def _(mo, first_employee, founded_year, share_capital):
    _ok = (
        first_employee == "Tobi"
        and share_capital == 300
        and isinstance(founded_year, int)
    )
    mo.callout(
        mo.md("✅ Form accepted!" if _ok else "❌ The registrar rejects the form — keep fixing."),
        kind="success" if _ok else "warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save — this was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
```

IMPORTANT authoring rule (applies to ALL fix-the-bug exercises): Tobi's bugs must be **runtime or logic errors, never syntax errors** — a syntax error inside any cell makes the whole `.py` file unparsable and the notebook won't open. Wrong types, wrong values, off-by-one: yes. Missing colons, invalid identifiers: no.
`ex_01_b.py`: predict `300 - 12 * 25` before running; then compute how many sticker packs (`12.25` each) fit in `300` using `//` and `%` (`packs_exb = 24`, `change_exb = 6.0`). `ex_01_c.py`: build one f-string receipt line with `:.2f` from given `item`, `qty`, `price` (`line_exc == "2x Falafel Wrap: 13.80 EUR"`).

- [ ] **Step 2: Export + run all three; commit**

```bash
uv run python helpers/export_marimo.py
git add notebooks/exercises/
git commit -m "feat: session I in-lecture exercises (a/b/c)"
```

---

### Task 7: Lecture 1 deck integration

**Goal:** `lectures/lec_01_introduction.qmd` gains the startup cold-open and three exercise-break slides with QR codes; loses anything Copilot.

**Files:**
- Modify: `lectures/lec_01_introduction.qmd`
- Create: `helpers/make_qr.py` (QR generator used by all lecture decks)

**Acceptance Criteria:**
- [ ] Deck opens with a 1-slide startup framing (restrained tone — one Tobi joke max)
- [ ] Three exercise-break slides at block boundaries, each: exercise URL + QR image + "10 minutes" note
- [ ] `grep -i copilot lectures/lec_01_introduction.qmd` → no matches
- [ ] Deck still renders: `quarto render lectures/lec_01_introduction.qmd`

**Steps:**

- [ ] **Step 1: QR helper**

```python
# helpers/make_qr.py
"""Generate QR PNGs for exercise URLs: uv run python helpers/make_qr.py"""
from pathlib import Path

import segno  # add first: uv add segno

BASE = "https://beyondsimulations.github.io/Introduction-to-Python/notebooks"
OUT = Path(__file__).resolve().parent.parent / "lectures" / "assets" / "qr"
EXERCISES = ["ex_01_a", "ex_01_b", "ex_01_c"]  # extend in later plans

OUT.mkdir(parents=True, exist_ok=True)
for ex in EXERCISES:
    segno.make(f"{BASE}/{ex}/").save(str(OUT / f"{ex}.png"), scale=8)
    print(f"wrote {OUT / (ex + '.png')}")
```

Run `uv add segno && uv run python helpers/make_qr.py`.

- [ ] **Step 2: Insert slides**

Read the existing deck first to match its slide idiom (`#`-titles, revealjs). Insert after the intro section, at the three block boundaries (the deck's existing topic seams: variables / numbers / strings), a slide of this exact form (adjust letter per block):

```markdown
# ⚡ Your turn — 10 minutes {background-color="#f5f0e8"}

Open the exercise (phone the QR or type the link):

**[beyondsimulations.github.io/Introduction-to-Python/notebooks/ex_01_a/](https://beyondsimulations.github.io/Introduction-to-Python/notebooks/ex_01_a/)**

![](assets/qr/ex_01_a.png){width=280}

First **predict** what happens — then run it.
```

Cold-open slide (1st content slide): "This semester you are founding a food-delivery startup. Today: it gets a name, a menu, and its first revenue calculation. (Your co-founder Tobi has already spent the marketing budget on stickers.)" — then remove/replace any Copilot-referencing slides found (`grep -ni copilot`).

- [ ] **Step 3: Render, eyeball slides, commit**

```bash
quarto render lectures/lec_01_introduction.qmd
git add lectures/lec_01_introduction.qmd lectures/assets/qr/ helpers/make_qr.py pyproject.toml uv.lock
git commit -m "feat: lec 01 startup cold-open + QR exercise breaks"
```

---

### Task 8: Private checkpoint repo + grading script (TDD)

**Goal:** The `Introduction-to-Python-checkpoints` private repo with a tested grading pipeline that handles both download formats, timeouts, and broken submissions.

**Files (in the NEW private repo, created at `../Introduction-to-Python-checkpoints/`):**
- Create: `pyproject.toml`, `grader/runner.py`, `grader/grade.py`, `grader/hashcheck.py`, `checkpoints/cp0/reference_tests.py`, `tests/test_grader.py`, `tests/fixtures/` (4 fixture submissions), `README.md`

**Acceptance Criteria:**
- [ ] `uv run pytest` green in the private repo
- [ ] Grader handles: valid notebook-format submission, flat-script submission, syntax-error submission (→ manual-review bucket), infinite-loop submission (→ timeout → manual-review bucket)
- [ ] Output CSV: `student_id,task_id,points,status` rows + per-student totals

**Verify:** `cd ../Introduction-to-Python-checkpoints && uv run pytest -v` → all pass; `uv run python -m grader.grade checkpoints/cp0 tests/fixtures/` → CSV on stdout with 4 students, one flagged `manual_review`.

**Steps:**

- [ ] **Step 1: Scaffold the repo**

```bash
mkdir -p ../Introduction-to-Python-checkpoints/{grader,checkpoints/cp0,tests/fixtures}
cd ../Introduction-to-Python-checkpoints && git init
# pyproject.toml:
```

```toml
[project]
name = "itp-checkpoints"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["marimo", "pytest"]
```

Create the repo on GitHub as **private** (`gh repo create Introduction-to-Python-checkpoints --private`).

- [ ] **Step 2: Write failing tests first**

```python
# tests/test_grader.py
import json
import subprocess
import sys
from pathlib import Path

from grader.grade import grade_submission, load_tasks
from grader.hashcheck import expected_hash, check

FIXTURES = Path(__file__).parent / "fixtures"
CP0 = Path(__file__).parent.parent / "checkpoints" / "cp0"


def test_hashcheck_roundtrip():
    h = expected_hash("B")
    assert check("B", h) is True
    assert check("b", h) is True      # case-normalized
    assert check("C", h) is False


def test_valid_notebook_submission_scores_full():
    result = grade_submission(FIXTURES / "cp0_good_notebook.py", load_tasks(CP0))
    assert result.status == "graded"
    assert result.total == 6  # 3 tasks x 2 points


def test_flat_script_submission_scores_full():
    result = grade_submission(FIXTURES / "cp0_good_flat.py", load_tasks(CP0))
    assert result.status == "graded"
    assert result.total == 6


def test_syntax_error_goes_to_manual_review():
    result = grade_submission(FIXTURES / "cp0_broken.py", load_tasks(CP0))
    assert result.status == "manual_review"
    assert result.total == 0


def test_infinite_loop_times_out_to_manual_review():
    result = grade_submission(
        FIXTURES / "cp0_hangs.py", load_tasks(CP0), timeout=5
    )
    assert result.status == "manual_review"
```

Run: `uv run pytest -v` → FAIL (modules don't exist).

- [ ] **Step 3: Implement**

```python
# grader/hashcheck.py
"""Hash-based answer checks: embeddable in WASM checkpoints without leaking answers."""
import hashlib

_SALT = "itp-2026"  # not a secret; just prevents casual rainbow lookup


def _normalize(value) -> str:
    return str(value).strip().lower()


def expected_hash(answer) -> str:
    return hashlib.sha256((_SALT + _normalize(answer)).encode()).hexdigest()


def check(answer, expected: str) -> bool:
    return expected_hash(answer) == expected
```

```python
# grader/runner.py
"""Executed in a SUBPROCESS per submission: run the file, dump requested names as JSON.

Handles both formats: marimo notebook (has `app`) via app.run(), flat script via exec.
Usage: python -m grader.runner <submission.py> <name1> <name2> ...
"""
import importlib.util
import json
import sys


def extract(path: str, names: list[str]) -> dict:
    spec = importlib.util.spec_from_file_location("submission", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # flat scripts execute fully here
    if hasattr(module, "app"):       # marimo notebook format
        _outputs, defs = module.app.run()
        namespace = dict(defs)
    else:
        namespace = vars(module)
    out = {}
    for name in names:
        if name in namespace:
            value = namespace[name]
            out[name] = value if isinstance(value, (int, float, str, bool, list, dict, type(None))) else repr(value)
    return out


if __name__ == "__main__":
    print(json.dumps(extract(sys.argv[1], sys.argv[2:])))
```

```python
# grader/grade.py
"""Grade a folder of submissions against a checkpoint's reference tests.

Usage: python -m grader.grade checkpoints/cp0 path/to/submissions/ [> points.csv]
Reference tests: checkpoints/cpN/reference_tests.py defining
TASKS = {task_id: {"points": int, "names": [str], "test": callable(defs)->bool}}
"""
import csv
import importlib.util
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

TIMEOUT_DEFAULT = 30


@dataclass
class Result:
    submission: str
    status: str                      # graded | manual_review
    total: int = 0
    per_task: dict = field(default_factory=dict)


def load_tasks(checkpoint_dir: Path) -> dict:
    ref = checkpoint_dir / "reference_tests.py"
    spec = importlib.util.spec_from_file_location("reference_tests", ref)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.TASKS


def grade_submission(path: Path, tasks: dict, timeout: int = TIMEOUT_DEFAULT) -> Result:
    names = sorted({n for t in tasks.values() for n in t["names"]})
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "grader.runner", str(path), *names],
            capture_output=True, text=True, timeout=timeout,
            cwd=Path(__file__).resolve().parent.parent,
        )
    except subprocess.TimeoutExpired:
        return Result(path.name, "manual_review")
    if proc.returncode != 0:
        return Result(path.name, "manual_review")
    defs = json.loads(proc.stdout)
    result = Result(path.name, "graded")
    for task_id, spec_ in tasks.items():
        passed = bool(spec_["test"](defs))
        result.per_task[task_id] = spec_["points"] if passed else 0
        result.total += result.per_task[task_id]
    return result


def main() -> None:
    checkpoint_dir, submissions_dir = Path(sys.argv[1]), Path(sys.argv[2])
    tasks = load_tasks(checkpoint_dir)
    writer = csv.writer(sys.stdout)
    writer.writerow(["submission", "status", *tasks.keys(), "total"])
    for sub in sorted(submissions_dir.glob("*.py")):
        r = grade_submission(sub, tasks)
        writer.writerow([r.submission, r.status, *[r.per_task.get(t, 0) for t in tasks], r.total])


if __name__ == "__main__":
    main()
```

```python
# checkpoints/cp0/reference_tests.py
"""Dress-rehearsal checkpoint: 3 tasks x 2 points."""
TASKS = {
    "t1_price": {
        "points": 2,
        "names": ["price_t1"],
        "test": lambda d: d.get("price_t1") == 12.40,
    },
    "t2_trace": {
        "points": 2,
        "names": ["answer_t2"],
        "test": lambda d: str(d.get("answer_t2", "")).strip().lower() == "b",
    },
    "t3_fix": {
        "points": 2,
        "names": ["total_t3"],
        "test": lambda d: d.get("total_t3") == 37.20,
    },
}
```

- [ ] **Step 4: Create the four fixtures**

`tests/fixtures/cp0_good_notebook.py` — a valid marimo notebook defining `price_t1 = 12.40`, `answer_t2 = "b"`, `total_t3 = 37.20` in cells (copy the minimal structure from Task 1's spike notebook). `cp0_good_flat.py` — the same three assignments as a plain script. `cp0_broken.py` — `price_t1 = 12.40` followed by a line with a syntax error (`def broken(:`). `cp0_hangs.py` — `while True: pass`.

- [ ] **Step 5: Run tests until green, commit**

```bash
uv run pytest -v          # all 5 pass
git add -A && git commit -m "feat: checkpoint grading pipeline with format autodetect and manual-review bucket"
git push -u origin main
```

---

### Task 9: Dress-rehearsal checkpoint notebook `cp0`

**Goal:** A complete practice checkpoint (marimo notebook, hash-based live checks, code-only answers) matching `cp0/reference_tests.py` — used for the end-to-end rehearsal and later in class as the CP-format demo.

**Files (private repo):**
- Create: `checkpoints/cp0/cp0_dress_rehearsal.py`

**Acceptance Criteria:**
- [ ] Header cell: `STUDENT_NAME = ""` / `STUDENT_ID = ""` as CODE assignments + instructions
- [ ] 3 tasks (write / trace-MCQ / fix-bug), each answered via code assignment; live checks use `hashlib` inline with the hashes from `grader.hashcheck.expected_hash` (t2's answer "b" must NOT appear in plaintext)
- [ ] Live score cell totals points; "download and upload to Moodle" closing cell
- [ ] Grading it with Task 8's pipeline yields 6/6 when filled correctly, 0 + manual_review when sabotaged

**Verify:** fill in correct answers in the browser → score cell shows 6/6 → download → `uv run python -m grader.grade checkpoints/cp0 <folder-with-download>` → total 6.

**Steps:**

- [ ] **Step 1: Write the notebook** — key cells (full file follows Task 2's structural conventions):

```python
@app.cell
def _():
    # FILL THIS IN FIRST — as code, exactly like this:
    STUDENT_NAME = ""   # e.g. "Ada Lovelace"
    STUDENT_ID = ""     # e.g. "k12345"
    return (STUDENT_ID, STUDENT_NAME)


@app.cell
def _():
    # Task 1 (2 pts): Board review! Compute the price of the "Founders Bowl":
    # base 9.50, plus 1.50 topping, minus 5% investor discount. Round to 2 places.
    price_t1 = None  # YOUR CODE
    return (price_t1,)


@app.cell(hide_code=True)
def _(mo, price_t1):
    import hashlib

    def _h(v):
        return hashlib.sha256(("itp-2026" + str(v).strip().lower()).encode()).hexdigest()

    # expected_hash(12.40) precomputed with grader.hashcheck — paste literal here
    t1_ok = price_t1 is not None and _h(price_t1) == "PASTE_HASH_T1"
    mo.md("✅ Task 1 looks right." if t1_ok else "🔲 Task 1 not passed (yet).")
    return (t1_ok,)
```

Task 2 (trace): show a 4-line loop snippet, options a–d in the prose, answer as `answer_t2 = ""` code assignment, hash-checked the same way. Task 3 (fix): Tobi's `total_t3 = "12.40" * 3` string-multiplication bug to fix to `37.20`. Score cell sums `[t1_ok, t2_ok, t3_ok] * 2` points. Generate the three hash literals with `uv run python -c "from grader.hashcheck import expected_hash; print(expected_hash(12.40), expected_hash('b'), expected_hash(37.20))"` and paste them in.

- [ ] **Step 2: Export, run, grade end-to-end locally; commit**

```bash
uv run marimo export html-wasm checkpoints/cp0/cp0_dress_rehearsal.py -o /tmp/cp0_out --mode edit
# serve, solve in browser, download .py to /tmp/cp0_subs/, then:
uv run python -m grader.grade checkpoints/cp0 /tmp/cp0_subs/
git add checkpoints/cp0/ && git commit -m "feat: cp0 dress-rehearsal checkpoint with hashed live checks"
```

---

### Task 10: Full dress rehearsal + deployment path

**Goal:** The entire student journey proven on real infrastructure, results recorded.

**Files:**
- Create: `docs/superpowers/specs/2026-07-08-dress-rehearsal-results.md` (in the PUBLIC course repo)
- Create (private repo): `deploy_checkpoint.sh`

**Acceptance Criteria:**
- [ ] GitHub Education Teacher benefit applied for / status recorded (gates private-repo Pages; Cloudflare Pages fallback tested if not yet granted)
- [ ] cp0 deployed to the private host at an unlisted URL; solved on a NON-development machine (ideally an old/weak laptop); downloaded; graded 6/6
- [ ] molab login flow tested once, method screenshotted for the FAQ (spec §9 spike 3)
- [ ] Results file records every step, timings, and any friction found

**Verify:** the results file exists with all four checkboxes above answered concretely (no "TBD").

**Steps:**

- [ ] **Step 1: Deploy script (private repo)**

```bash
#!/usr/bin/env bash
# deploy_checkpoint.sh <cpN> — export a checkpoint and publish to the pages branch.
set -euo pipefail
CP="$1"
uv run marimo export html-wasm "checkpoints/${CP}/"*.py -o "site/${CP}-$(openssl rand -hex 4)" --mode edit
# Then: commit site/ to the branch GitHub Pages serves (private repo), or:
#   npx wrangler pages deploy site/ --project-name itp-checkpoints   (Cloudflare fallback)
echo "Deployed. Unlisted path printed above — make the QR with helpers/make_qr.py."
```

- [ ] **Step 2: Execute the rehearsal, in order**

1. Apply: https://github.com/education/teachers (record status; don't block on approval — use Cloudflare fallback meanwhile).
2. Deploy cp0 via the script; note the unlisted URL.
3. On a different, ideally weak machine: open URL, complete cp0, download `.py`, upload to a Moodle sandbox course, download from Moodle, grade → expect 6/6. Time every step.
4. Open a tutorial notebook's molab badge URL, sign in, save, reopen — screenshot the login screen for the FAQ.
5. Write everything into the results file; flag any friction as input for Plan 2.

- [ ] **Step 3: Commit both repos**

```bash
git add docs/superpowers/specs/2026-07-08-dress-rehearsal-results.md && git commit -m "docs: dress rehearsal results"
# private repo: git add deploy_checkpoint.sh site/ && git commit -m "feat: checkpoint deploy script"
```

---

## Execution order & dependencies

```
Task 1 (spikes) ──► Task 2 (template) ──► Task 5 (lab nb) ──► Task 7 (deck)
        │                                      ▲
        └──► Task 3 (pipeline) ────────────────┘──► Task 4 (launcher page)
        └──► Task 8 (grader) ──► Task 9 (cp0) ──► Task 10 (rehearsal)
Task 6 (exercises) needs Tasks 2+3.
```

Tasks 1→2→3 strictly sequential; then {4,5,6} in any order; 7 after 6 (QRs need URLs); 8→9→10 can run in parallel with 4–7 after Task 1.
