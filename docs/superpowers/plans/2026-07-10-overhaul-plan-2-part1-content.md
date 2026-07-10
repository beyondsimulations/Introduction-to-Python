# Course Overhaul Plan 2: Part I Content (Sessions I–V) + CP1–3

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete Part I of the course: full lecture rewrites for Sessions I–V, lab notebooks + in-lecture exercises + launcher pages for Sessions II–V, checkpoints CP1–3, and the four patterns deferred from the Fable review (solution notebooks, chatbot prompt, warm-up quiz, letter-order convention).

**Architecture:** Every artifact copies a proven Plan-1 pattern (`notebooks/_template.py`, `nb_01_lab_founding.py`, `tut_01`, `lec_01`'s QR slides, cp0's structure). New in this plan: a read-only solution-notebook publishing pipeline (`--mode run`), an authoring-conventions doc, a headless notebook validator, and warm-up vote slides. Spec: `docs/superpowers/specs/2026-07-08-course-overhaul-design.md`; Fable review + resolutions: `docs/superpowers/specs/2026-07-09-fable-review.md`.

**Tech Stack:** Quarto/revealjs, marimo 0.23.x WASM export, uv, pytest (checkpoints repo), segno (QR).

**Sequencing:** Plan 3 (Part II: Sessions VI–IX + CP4–5 + `general/ai-tools.qmd`) and Plan 4 (Part III, Session X, nav cleanup, `/humanizer` pass) are written after this plan executes. Side quests (`nb_XX_sidequest_*`) are explicitly OUT of this plan — ideas go to the backlog file (Task 1).

---

## Context for the zero-context engineer

- Two repos: this public Quarto site, and the PRIVATE grader repo at `../Introduction-to-Python-checkpoints` (relative to this repo's parent dir: `/Users/vlcek/development/lectures/Introduction-to-Python-checkpoints`). Checkpoint notebooks, reference tests, and ALL solution notebooks are authored in the private repo. Never commit checkpoint or solution content to the public repo except via the documented publishing motion (Task 2).
- **Commit rule (repo policy, overrides all defaults): NEVER add `Co-Authored-By`, "Generated with Claude Code", or any AI-attribution line to commits or PRs in either repo.**
- marimo notebooks: cells are `@app.cell` functions; a global may be defined in ONE cell only (`+=`/`*=` count); underscore-prefixed names are cell-private; `@app.cell(hide_code=True)` for md/check/hint cells. After hand-editing, validate with `uv run python helpers/validate_notebooks.py` (Task 1) and open once in `uv run marimo edit <file>` (marimo normalizes on save).
- Rendering: `quarto render <file>` works (`_environment` pins `QUARTO_PYTHON=.venv/bin/python`). A single-file render DELETES the other files in `_repo-md/` — always run `git checkout -- _repo-md/` afterwards and never commit `_repo-md` changes from single-file renders. A FULL `quarto render` currently fails on the untracked `Management-Science/` dir before reaching course files — pre-existing; do per-file renders.
- Story canon (spec §4): campus food-delivery startup (student-named, name-agnostic checks), Kevin (inept co-founder, present from Ep. 1), the investor (arrives Part II — cameos only until then), German authorities (health inspector, Formular 27b/6), MunchCorp (competitor). Sitcom tone in notebooks; restrained in slides (≤1 Kevin joke per deck section).
- Hint ladder (Fable #3, fixed pattern): Hint 1 = conceptual nudge, no code. Hint 2 = skeleton with blanks (`fee_exa = round(___ * ___, 2)`) — NEVER the paste-able answer. Full answers only in solution notebooks.
- Check-cell style (round-2 pattern, copy from `nb_01`): placeholder `= None` → "🔲 not attempted"; correct → ✅ + story beat; wrong → ❌ + concrete pointer; numeric compares guard with `isinstance(x, (int, float)) and round(x, 2) == LITERAL`; append `show_result(value)` to the message; wrap in `mo.callout`.
- **Float-safety rule for check values:** pick numbers whose arithmetic is exact after `round(_, 2)`. Avoid `.xx5` rounding boundaries (e.g. `34.50 * 0.95 = 32.775` rounds to 32.77 in binary floats — never use such values). Every expected literal in this plan was verified by hand; re-verify in Python before hard-coding a hash or reference test.
- **No-hang rule:** never ship a cell that can loop forever — an infinite loop freezes the student's WASM tab. Kevin's loop bugs are wrong-count/wrong-condition bugs that still terminate. (Kevin's bugs are also never syntax errors — a syntax error makes the whole `.py` unparsable.)

---

### Task 1: Authoring conventions doc + headless validator + template touch-up

**Goal:** One document that locks in every convention Plans 2–4 copy (Fable #10 included), plus an automated smoke test for all notebooks.

**Files:**
- Create: `docs/authoring-conventions.md`
- Create: `docs/side-quest-backlog.md`
- Create: `helpers/validate_notebooks.py`
- Modify: `notebooks/_template.py` (header comment: add letter-order, no-hang, float-safety rules)

**Acceptance Criteria:**
- [ ] Conventions doc covers: notebook rules, exercise-letter = slide-order rule, deck skeletons (regular + CP session), warm-up pattern, QR slide pattern, solutions publishing runbook, float-safety, no-hang, commit rule
- [ ] `uv run python helpers/validate_notebooks.py` runs `nb_01` + `ex_01_a/b/c` headless and prints `ok` for each
- [ ] Backlog file exists with a "cut lecture material" and a "side-quest ideas" section

**Verify:** `uv run python helpers/validate_notebooks.py && echo PASS` → `ok` lines + PASS.

**Steps:**

- [ ] **Step 1: Write the validator**

```python
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
```

Run it; `nb_01_lab_founding` and the three `ex_01_*` files must print `ok`.

- [ ] **Step 2: Write `docs/authoring-conventions.md`**

```markdown
# Authoring conventions (Plans 2–4 copy these — do not improvise)

## Repos & publishing
- Public repo: lectures, tutorials (launcher pages), lab + exercise notebooks.
- Private repo (`../Introduction-to-Python-checkpoints`): checkpoint notebooks,
  reference tests, ALL solution notebooks (`solutions/sol_XX_*.py`).
- Commit rule: never add AI-attribution lines (Co-Authored-By etc.) in either repo.
- Single-file `quarto render` deletes sibling `_repo-md/*.md` — run
  `git checkout -- _repo-md/` afterwards; only full renders may update `_repo-md`.

## Notebooks (see notebooks/_template.py for the skeleton)
- One global per cell; `+=`/`*=` count as definitions; `_name` is cell-private.
- Every exercise pre-defines its answer: `fee_ex11 = None  # YOUR CODE BELOW`.
- Suffix naming: `<meaning>_exNM` (section N, exercise M); boss = `_ex40`,
  MCQ = `answer_ex50`, bonuses = `_ex60`+. Classes keep their natural name
  (`Order`), no suffix.
- Checks: `isinstance` + `round(x, 2) == LITERAL` for numbers; degrade to
  "🔲 not attempted" on None; `mo.callout` + `show_result(value)`.
- Float safety: expected values must survive `round(_, 2)` exactly; avoid
  `.xx5` boundaries (32.775 → 32.77!). Verify every literal in Python first.
- Hints: Hint 1 = nudge (no code); Hint 2 = skeleton with `___` blanks — never
  the paste-able answer. Full answers live in the solution notebook only.
- Kevin's bugs: logic/runtime only (never syntax errors), and always terminating
  (never a possible infinite loop — it freezes the WASM tab).
- Trace exercises: `mo.ui.radio` + reveal, labeled "(trace — predict first)",
  ungraded (not counted in the progress cell).
- Progress cell counts core exercises only; wrap-up ritual cell closes every lab.
- Story: sitcom in notebooks, investor only cameos until Part II, name-agnostic
  checks (never assert on the startup name).

## In-lecture exercises (ex_XX_<letter>.py)
- **Letter = slide order** (Fable #10): `ex_XX_a` belongs to lecture block 1,
  `_b` to block 2, `_c` to block 3. CP sessions have 2 blocks → letters a–b only.
- One concept, one screen, 5–10 min, one exercise + one reactive check,
  closing cell: "*Nothing to save — this was a sandbox.*"

## Lecture decks (revealjs)
Regular session skeleton:
1. Title slide (Fall 2026) → 2. Cold open (1 slide, episode framing, restrained)
3. 🔥 Warm-up (3 recap questions; see below) → 4. Block 1 (≤20 min)
5. ⚡ QR exercise a → 6. Block 2 → 7. QR b → [break] → 8. Block 3 → 9. QR c
10. Lab handoff (tutorial URL) → 11. Wrap-up: 3 takeaways + next-episode teaser.
CP sessions (III, V, VI, VIII, X): title → 📋 checkpoint slide (procedure) →
cold open → Block 1 → QR a → Block 2 → QR b → lab handoff → wrap-up.
No warm-up on CP days (the checkpoint is the warm-up).

### Warm-up pattern (oral + vote)
One `# 🔥 Warm-up {.exercise-slide}` section, then per question a `##` slide
(question + options a–c) and a `##` answer slide (answer + one-line why).
Everyone commits by hand vote BEFORE the reveal — predict-first, zero infra.

### QR exercise slide (exact form)
    # ⚡ Your turn — 10 minutes {.exercise-slide}
    …URL + QR image (assets/qr/ex_XX_x.png, width 280) + "First **predict** — then run."
Add new exercises to `helpers/make_qr.py` EXERCISES and re-run it.

## Solution notebooks (Fable #4)
- Authored in the PRIVATE repo as `solutions/sol_XX_lab_<topic>.py`: the lab
  notebook with answers filled in, checks green, header "Solutions — Episode XX",
  hint accordions removed, wrap-up replaced by "compare, don't memorize" note.
- Publish AFTER the session: copy to public `notebooks/solutions/`, run
  `quarto render` (full) or `uv run python helpers/export_marimo.py`,
  un-comment the Solutions link in that episode's tutorial page, commit, push.
- Exported read-only (`--mode run`) by helpers/export_marimo.py automatically.
- Nothing in `notebooks/solutions/` before its session has happened.

## Checkpoints (private repo)
- ~6 tasks × 2 pts, all-or-nothing; answers are CODE assignments (`answer_t2 = "b"`),
  never `mo.ui` state; `STUDENT_NAME`/`STUDENT_ID` assignments at the top.
- Live checks use sha256 hashes (`grader.hashcheck.expected_hash`) — answers never
  in plaintext. Real referee = `reference_tests.py` (hidden), functions graded via
  `exprs` probes with instructor-chosen inputs.
- JSON constraint: the runner serializes to JSON — tuples become lists, sets are
  not serializable. Graded answers: numbers, strings, bools, lists, dicts only.
- CP task values must DIFFER from lab/exercise values (same skill, new numbers).
```

- [ ] **Step 3: Create `docs/side-quest-backlog.md`**

```markdown
# Side-quest & cut-material backlog

Buffer scope (spec §4): authored last, cut first, never blocking semester start.

## Side-quest ideas (per episode)
- Ep. 2: Haggling Bot extended — multi-round supplier negotiation with mo.ui.
- (add as they come up during deck cuts)

## Material cut from lecture decks (Plan 2 rewrites)
- (one line per cut concept: "lec_02: while/else clause — niche, cut")
```

- [ ] **Step 4: Extend `notebooks/_template.py` header comment**

Add to the existing rules comment block (keep existing lines):

```python
# - exercise letters in ex_XX_<letter>.py map 1:1 to lecture block order (a=block 1)
# - never a possible infinite loop (freezes the WASM tab); Kevin's bugs always terminate
# - check literals must survive round(x, 2) exactly; avoid .xx5 boundaries
```

- [ ] **Step 5: Validate + commit**

```bash
uv run python helpers/validate_notebooks.py
git add docs/authoring-conventions.md docs/side-quest-backlog.md helpers/validate_notebooks.py notebooks/_template.py
git commit -m "docs: authoring conventions, side-quest backlog, headless notebook validator"
```

---

### Task 2: Solution-notebook pipeline, proven with `sol_01`

**Goal:** The read-only solutions pattern exists end-to-end (Fable #4): private authoring → `--mode run` export → tutorial-page link, proven once with Episode 1 and then reverted to the pre-semester state.

**Files:**
- Modify: `helpers/export_marimo.py` (add `notebooks/solutions/sol_*.py`, exported with `--mode run`)
- Create (PRIVATE repo): `solutions/sol_01_lab_founding.py`
- Modify: `tutorials/tut_01_introduction.qmd` (commented-out Solutions link)
- Modify (PRIVATE repo): `README.md` (publishing runbook pointer)

**Acceptance Criteria:**
- [ ] `sol_01_lab_founding.py` = `nb_01` with every exercise solved; all checks render ✅; hint accordions removed; header says "Solutions — Episode 1"
- [ ] Export pipeline exports `notebooks/solutions/*.py` with `--mode run` (read-only) and everything else with `--mode edit`
- [ ] Full motion proven once: copy → export → serve → link works → then the copy is REMOVED again (semester hasn't started; solutions must not be live)
- [ ] `tut_01` carries the commented-out link with the publishing instruction

**Verify:** with `sol_01` temporarily copied in: `uv run python helpers/export_marimo.py && ls _site/notebooks/sol_01_lab_founding/` → export exists; served page has NO edit affordances (run mode). After revert: `git status` clean of `notebooks/solutions/`.

**Steps:**

- [ ] **Step 1: Extend the export script**

In `helpers/export_marimo.py`, change `export()` and `main()`:

```python
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
    failures = [nb for nb in editable if not export(nb, "edit")]
    failures += [nb for nb in readonly if not export(nb, "run")]
    return 1 if failures else 0
```

- [ ] **Step 2: Author `sol_01_lab_founding.py` in the private repo**

Copy `notebooks/nb_01_lab_founding.py` to `../Introduction-to-Python-checkpoints/solutions/sol_01_lab_founding.py`, then:
- Header cell: title "Solutions — Episode 1: The Founding", note "Compare with your own attempt — don't memorize. If your different solution turns the check green, it is just as correct."
- Fill every `= None` placeholder with the reference answer (the check cells define them: `revenue_ex12 = round(price_ex11 * portions_ex11, 2)` etc. — derive each from the existing check conditions, don't guess).
- Delete all hint-accordion cells.
- Replace the wrap-up cell with the compare-don't-memorize note.
- Validate: `uv run marimo edit ../Introduction-to-Python-checkpoints/solutions/sol_01_lab_founding.py` — every check ✅, progress cell full.

- [ ] **Step 3: Prove the publishing motion once, then revert**

```bash
mkdir -p notebooks/solutions
cp ../Introduction-to-Python-checkpoints/solutions/sol_01_lab_founding.py notebooks/solutions/
uv run python helpers/validate_notebooks.py 'solutions/sol_*.py'
uv run python helpers/export_marimo.py
cd _site && python -m http.server 8766   # open /notebooks/sol_01_lab_founding/ — read-only, all ✅
# then revert (semester not started):
rm -r notebooks/solutions
```

- [ ] **Step 4: Add the dormant link to `tut_01`**

At the end of `tutorials/tut_01_introduction.qmd`:

```markdown
<!-- PUBLISH AFTER SESSION I (see docs/authoring-conventions.md → Solution notebooks):
## Solutions

[Solutions notebook (read-only)](../notebooks/sol_01_lab_founding/){.btn}
-->
```

- [ ] **Step 5: Private-repo README runbook + commit both repos**

Append to the private repo `README.md`: a "Solution notebooks" section stating: authored here under `solutions/`, published after each session by copying into the public repo's `notebooks/solutions/` + re-render + un-comment the tutorial link.

```bash
git add helpers/export_marimo.py tutorials/tut_01_introduction.qmd
git commit -m "feat: read-only solution-notebook export pipeline + dormant tut_01 link"
cd ../Introduction-to-Python-checkpoints
git add solutions/sol_01_lab_founding.py README.md
git commit -m "feat: episode 1 solutions notebook + publishing runbook"
```

---

### Task 3: Chatbot hint-only system prompt (draft for external install)

**Goal:** The Part-I hint-only system prompt exists as a ready-to-paste deliverable (Fable #5). Installing it in the oshu.eu widget is Tobias's task and a **gate before Session I** — the plan only produces the text.

**Files:**
- Create: `docs/chatbot-system-prompt.md`

**Acceptance Criteria:**
- [ ] Full prompt text, ready to paste — no placeholders
- [ ] Enforces: no complete solution code ever; skeleton-with-blanks max; traceback-reading coaching; declines full-answer requests; knows the startup arc
- [ ] Doc header names the external install step + the Session-I deadline + the Part-II swap note

**Verify:** file exists; contains the words "skeleton" and "never" in the rules; no TODO/TBD.

**Steps:**

- [ ] **Step 1: Write the file**

```markdown
# Course chatbot system prompt — Part I (hint-only)

**Install:** paste into the oshu.eu chat-widget system prompt. **Deadline: before
Session I** (it is the sanctioned helper from the first lab on). **After Session V**
(start of Part II), relax rule 1–3 to "prefer hints, full code allowed on request"
— Plan 3 delivers that variant.

---

You are the course assistant for "Programming with Python" at Kühne Logistics
University. The students are complete beginners in their first programming course.
The course runs as a story: each student founds a campus food-delivery startup
with their chaotic co-founder Kevin; exercises live in that world (the investor,
the German authorities, the competitor MunchCorp). Feel free to play along.

Part I of the course is AI-free by policy, and you are the ONE sanctioned helper.
Your job is to make students think, not to solve for them.

STRICT RULES:
1. NEVER write complete, runnable solution code — not when asked directly, not
   for "just this one exercise", not in pieces across several answers.
2. The most code you may ever show is a one-line skeleton with blanks, e.g.
   `revenue = round(___ * ___, 2)` — never with the blanks filled in.
3. Help like a good tutor instead:
   - Ask what they tried and what they expected to happen.
   - Explain the CONCEPT with a different tiny example (never the exercise's
     own numbers or variable names).
   - Point to the matching lecture section or the exercise's own hint accordion.
   - If they are close, name the ONE thing to look at ("check what type that
     variable has after line 2").
4. Error messages: teach reading the traceback — last line first, then the arrow.
   Translate the error into plain language, but let them find the fixing line.
5. If someone pastes a whole exercise and asks for the answer: decline warmly,
   offer a hint, and remind them that checkpoints must be solved without AI —
   the struggle now is what makes the checkpoint easy later.
6. Stay on course topics (Python, the course materials, study organisation).
   Politely decline anything else.

Keep answers short — a few sentences. Answer in the language the student uses.
```

- [ ] **Step 2: Commit**

```bash
git add docs/chatbot-system-prompt.md
git commit -m "docs: hint-only chatbot system prompt for Part I (external install)"
```

---

### Task 4: `lec_01` full rewrite

**Goal:** Session I deck rebuilt from scratch around the 3×20-min block structure — startup-woven examples, predict-first micro-questions, the already-corrected mechanics slides kept. This deck is the skeleton exemplar all other rewrites copy.

**Files:**
- Modify: `lectures/lec_01_introduction.qmd` (full rewrite of teaching content)

**Acceptance Criteria:**
- [ ] Structure: title → welcome/mechanics section (KEEP the corrected slides: passing scheme/5 checkpoints, Part-I-AI-free, no-install, Checkpoints slide) → cold open ("A New Venture", keep) → Block 1 (variables & types) → QR `ex_01_a` → Block 2 (numbers & arithmetic) → QR `ex_01_b` → Block 3 (strings & f-strings) → QR `ex_01_c` → lab handoff → wrap-up + Episode-2 teaser
- [ ] Each block ≤ 20 min of material (~8–10 content slides), every example startup-themed, ≥1 predict-first micro-question per block (question slide → answer slide)
- [ ] Existing QR slides (`.exercise-slide` class) reused; letters now match block order a→b→c (resolves Fable #10 for Session I)
- [ ] No warm-up section (Session I has nothing to recap)
- [ ] Anything cut gets one line in `docs/side-quest-backlog.md`
- [ ] `quarto render lectures/lec_01_introduction.qmd` clean; then `git checkout -- _repo-md/`

**Verify:** render passes; `grep -c 'exercise-slide' lectures/lec_01_introduction.qmd` ≥ 3; deck read-through stays inside 3 blocks.

**Steps:**

- [ ] **Step 1: Inventory + plan the cut** — read the current deck; list each slide as keep / rewrite / cut (cuts → backlog file with one-line reason).

- [ ] **Step 2: Rewrite block by block.** Content requirements:

| Block | Slides (one idea per slide) | Startup framing |
|---|---|---|
| 1 Variables & types | what a program is (instructions, top-to-bottom) · `print()` · variables = named values · naming rules · types: `str`/`int`/`float`/`bool` · `type()` · predict-first: `print(type("9.99"))` → vote → reveal | founding data: `company_founded = 2026`, `first_employee = "Kevin"`, `sticker_budget = 300` |
| 2 Numbers & arithmetic | `+ - * /` · `//` and `%` · precedence · `round()` · int vs float in money math · predict-first: `print(300 - 12 * 25)` → vote → reveal | Kevin's 9.99-for-everything theory; margin = 9.99 − cost |
| 3 Strings & f-strings | quotes · concatenation and why it hurts · f-strings · `{value:.2f}` · `\n` · predict-first: `f"{2 * 3}"` vs `"2 * 3"` → vote → reveal | the first receipt line |

- Keep the mechanics slides verbatim (they were corrected in round-2 — factual content must not drift).
- Lab handoff slide: link to `tutorials/tut_01_introduction.html`, one sentence on the episode, "download your `.py` before you leave".
- Wrap-up: 3 takeaways + teaser "Episode 2: the city bans delivery after 22:00."

- [ ] **Step 3: Render, checkout `_repo-md`, commit**

```bash
quarto render lectures/lec_01_introduction.qmd && git checkout -- _repo-md/
git add lectures/lec_01_introduction.qmd docs/side-quest-backlog.md
git commit -m "feat: lec 01 full rewrite — 3 startup-themed blocks with predict-first questions"
```

---

### Task 5: Session II in-lecture exercises (`ex_02_a/b/c`)

**Goal:** Three one-screen exercises for lecture 2's blocks (letters = block order): conditionals, loops, string methods.

**Files:**
- Create: `notebooks/exercises/ex_02_a.py`, `ex_02_b.py`, `ex_02_c.py`
- Modify: `helpers/make_qr.py` (extend `EXERCISES`)

**Acceptance Criteria:**
- [ ] Each: one concept, ≤1 screen, placeholder + reactive check (+ `show_result`), sandbox closing line
- [ ] Validator passes; QR PNGs regenerated

**Verify:** `uv run python helpers/validate_notebooks.py 'exercises/ex_02_*.py'` → 3× ok; `ls lectures/assets/qr/ex_02_*.png` → 3 files.

**Steps:**

- [ ] **Step 1: Write the three exercises** (copy the `ex_01_c` structure: import cell, hidden `show_result` helper cell, task md cell, given-values cell, `= None` answer cell, check cell, sandbox closing):

| File | Task | Given | Answer name | Check |
|---|---|---|---|---|
| `ex_02_a` | Delivery-fee ladder with `if/elif/else`: total < 15 → 2.90, 15–30 → 1.50, ≥ 30 → 0 | `order_total = 17.80` | `fee_exa` | `round(fee_exa, 2) == 1.50` |
| `ex_02_b` | First predict (radio) what this prints — shown as a proper 4-line block: `total = 0` / `for p in [3, 5]:` / `    total = total + p` / `print(total)` (print NOT indented) → a) `3` b) `8` c) `3` then `8` → reveal b — then write a `for` loop summing `minutes = [12, 7, 9]` | `minutes = [12, 7, 9]` | `minutes_exb` | `minutes_exb == 28` |
| `ex_02_c` | De-shout Kevin's menu entry with string methods (`.strip()`, `.rstrip("!")`, `.title()`) | `raw_item = "  FALAFEL WRAP!!!  "` | `item_exc` | `item_exc == "Falafel Wrap"` |

- [ ] **Step 2: Extend `helpers/make_qr.py`**

```python
EXERCISES = [
    "ex_01_a", "ex_01_b", "ex_01_c",
    "ex_02_a", "ex_02_b", "ex_02_c",
]
```

Run `uv run python helpers/make_qr.py`.

- [ ] **Step 3: Validate, export, commit**

```bash
uv run python helpers/validate_notebooks.py 'exercises/ex_02_*.py'
uv run python helpers/export_marimo.py
git add notebooks/exercises/ex_02_*.py helpers/make_qr.py lectures/assets/qr/
git commit -m "feat: session II in-lecture exercises (conditionals, loops, string methods)"
```

---

### Task 6: Episode 2 lab notebook + solutions + launcher (`nb_02` / `sol_02` / `tut_02`)

**Goal:** The complete Session II lab (~45–60 min): conditionals, loops, string methods, comprehension seed — Episode 2 "The Curfew".

**Files:**
- Create: `notebooks/nb_02_lab_curfew.py`
- Create (PRIVATE repo): `solutions/sol_02_lab_curfew.py`
- Modify: `tutorials/tut_02_control.qmd` (full replacement → launcher page, keep filename)

**Acceptance Criteria:**
- [ ] 7 core + 1 ungraded trace + 2 bonus, per the table below; all four CP task types present (write, trace-radio, fix-Kevin, MCQ-as-code)
- [ ] Copies `nb_01` patterns exactly: name re-ask, hidden `show_result`, Hint-2 skeletons, progress cell (7 cores), wrap-up ritual
- [ ] `tut_02` = two-button launcher (browser + molab) with the persistence explainer, episode intro, dormant Solutions link
- [ ] `sol_02` solved, checks all ✅, hints removed
- [ ] Validator green; WASM export completable start-to-finish in the browser

**Verify:** `uv run python helpers/validate_notebooks.py 'nb_02*'` ok → export → solve in browser → progress 7/7.

**Steps:**

- [ ] **Step 1: Write `nb_02_lab_curfew.py`.** Story cold-open: the city decrees no delivery after 22:00; Kevin suggests "we just deliver yesterday's orders". Exercises:

| Ex | Type | Task | Check |
|---|---|---|---|
| 1.1 core | write | Curfew check: `order_hour_ex11 = 23` given; boolean `is_open_ex11 = order_hour_ex11 < 22` | `is_open_ex11 is False` |
| 1.2 core | write | Discount ladder (`if/elif/else`): total ≥ 50 → 10%, ≥ 30 → 5%, else 0; apply to `36.00` | `round(final_ex12, 2) == 34.20` |
| 2.1 core | trace (ungraded) | Radio: what does `for i in range(3): print(i * 2)` print? a) 2 4 6 b) 0 2 4 c) 0 1 2 → reveal b, one-line why | not counted |
| 2.2 core | write | `for` loop summing the day's orders `[12.50, 8.90, 15.20, 9.99]` | `round(revenue_ex22, 2) == 46.59` |
| 2.3 core | fix | Kevin counts big orders (≥ 10 EUR) over `[12.50, 10.00, 8.90, 15.20]` but wrote `>` — off-by-boundary | `big_orders_ex23 == 3` |
| 3.1 core | write | Clean `"  PIZZA CALZONE  "` with `.strip().title()` | `clean_ex31 == "Pizza Calzone"` |
| boss ex40 core | write | Price war: MunchCorp sells at 8.50; start at 11.90, cut 10% per round (`while`), count the rounds until you undercut them (price path: 11.90 → 10.71 → 9.64 → 8.68 → 7.81) | one answer name only: `rounds_ex40 == 4` (final price echoed via `show_result` by recomputing in the check cell, not graded) |
| ex50 core | mcq | "Which loop body runs exactly 5 times?" a) `for i in range(1, 5)` b) `for i in range(5)` c) `for i in range(0, 5, 2)` | `answer_ex50 == "b"` |
| ex60 bonus | write | Comprehension seed: 10%-off menu `[round(p * 0.9, 2) for p in [12.50, 10.00, 8.90, 15.20]]` | `== [11.25, 9.0, 8.01, 13.68]` |
| ex61 bonus | play (ungraded) | Haggling Bot: `mo.ui.slider` offer vs supplier's secret 7.25/kg — reactive "too low / too high / DEAL"; guess-the-number reskin, pure fun | no check |

Story beats between sections: the 22:00 decree (§1), Kevin's order-counting "dashboard" (§2), the menu Kevin typed IN ALL CAPS (§3), MunchCorp price-war letter (boss). Kevin's ex23 bug must terminate (plain `for` loop, wrong comparison only).

- [ ] **Step 2: Author `sol_02_lab_curfew.py`** in the private repo (same motion as Task 2 Step 2).

- [ ] **Step 3: Replace `tutorials/tut_02_control.qmd`** — copy `tut_01`'s launcher structure verbatim, adjust: title "Episode 2 — The Curfew", intro (3–5 sentences: curfew decree, discount rules, price war), buttons target `nb_02_lab_curfew`, dormant Solutions link → `sol_02_lab_curfew`.

- [ ] **Step 4: Validate, export, render, commit**

```bash
uv run python helpers/validate_notebooks.py
uv run python helpers/export_marimo.py     # solve nb_02 in the browser end-to-end
quarto render tutorials/tut_02_control.qmd && git checkout -- _repo-md/
git add notebooks/nb_02_lab_curfew.py tutorials/tut_02_control.qmd
git commit -m "feat: episode 2 lab — conditionals, loops, string methods"
cd ../Introduction-to-Python-checkpoints
git add solutions/sol_02_lab_curfew.py && git commit -m "feat: episode 2 solutions"
```

---

### Task 7: `lec_02` full rewrite (warm-up pattern debut)

**Goal:** Session II deck rebuilt: warm-up vote slides (the pattern's first instance), 3 blocks (conditionals / while / for + strings), QR slides for `ex_02_a/b/c`.

**Files:**
- Modify: `lectures/lec_02_control.qmd` (full rewrite)
- Modify: `docs/side-quest-backlog.md` (cuts)

**Acceptance Criteria:**
- [ ] Skeleton per conventions doc: title → cold open → 🔥 warm-up (3 questions + answer slides) → Block 1 → QR a → Block 2 → QR b → Block 3 → QR c → lab handoff → wrap-up/teaser
- [ ] Warm-up questions recap Session I (see Step 1) — question slide then answer slide, vote before reveal
- [ ] Blocks: (1) comparisons, booleans, `if/elif/else` — curfew + discount ladder; (2) `for`, `range`, iterating lists, one comprehension-seed slide — summing the day's orders; (3) `while`, `break`, loop safety — the price war — plus string methods `.strip()/.title()/.upper()` — de-shouting Kevin's menu. (Block order matches exercise letters: b = for-loop, c = strings; the while-based price war lands right before the lab whose boss is a while loop.)
- [ ] ≥1 predict-first micro-question per block; cuts logged; render clean

**Verify:** `quarto render lectures/lec_02_control.qmd` clean; `grep -c 'exercise-slide' lectures/lec_02_control.qmd` ≥ 4 (warm-up + 3 QR).

**Steps:**

- [ ] **Step 1: Warm-up section (write exactly this structure, content as given):**

```markdown
# 🔥 Warm-up {.exercise-slide}

Three questions from Episode 1. Commit — hands up before the reveal.

## Question 1

```python
price = 8.90
print(f"{price * 2:.2f}")
```

a\) `17.8`   b) `17.80`   c) `Error`

## Answer 1

**b)** — `:.2f` always prints two decimals. That's the whole receipt trick.

## Question 2

```python
print(type("9.99"))
```

a\) `float`   b) `str`   c) `int`

## Answer 2

**b)** — quotes make it text, no matter how numeric it looks. (Kevin learned this the hard way.)

## Question 3

```python
print(7 // 2, 7 % 2)
```

a\) `3.5 1`   b) `3 1`   c) `3 0.5`

## Answer 3

**b)** — `//` floors, `%` gives the remainder. Together: "how many fit, what's left."
```

- [ ] **Step 2: Rewrite the three blocks** per the acceptance criteria (inventory the old deck first; keep only explanations that survive the 20-min budget; cuts → backlog). QR slides: copy the exact `# ⚡ Your turn — 10 minutes {.exercise-slide}` form from `lec_01` with `ex_02_a/b/c` URLs + QR PNGs. No-hang teaching moment in Block 3: show a `while` that never ends, as a SCREENSHOT/static code block with a "never run this in the browser tab" warning — do not ship it runnable.

- [ ] **Step 3: Render, checkout, commit**

```bash
quarto render lectures/lec_02_control.qmd && git checkout -- _repo-md/
git add lectures/lec_02_control.qmd docs/side-quest-backlog.md
git commit -m "feat: lec 02 full rewrite — warm-up votes, control-flow blocks, QR breaks"
```

---

### Task 8: CP1 — sessions I–II (private repo)

**Goal:** Checkpoint 1 notebook + reference tests + fixtures, graded end-to-end locally. Taken at the start of Session III.

**Files (PRIVATE repo):**
- Create: `checkpoints/cp1/cp1_board_review.py`, `checkpoints/cp1/reference_tests.py`
- Create: `tests/fixtures/cp1_solved.py`, `tests/fixtures/cp1_blank.py`
- Create/Modify: `tests/test_checkpoints.py`

**Acceptance Criteria:**
- [ ] 6 tasks × 2 pts per the table; all answers code assignments; live checks hashed (no plaintext answers in the notebook); story flavor: "the quarterly board review"
- [ ] `STUDENT_NAME`/`STUDENT_ID` header cell; live score cell; download-to-Moodle closing cell
- [ ] Values differ from every lab/exercise value (same skills, new numbers)
- [ ] `uv run pytest` green; solved fixture grades 12/12, blank fixture 0/graded

**Verify:** `cd ../Introduction-to-Python-checkpoints && uv run pytest -v` all pass; `uv run python -m grader.grade checkpoints/cp1 tests/fixtures/` shows cp1_solved at 12.

**Steps:**

- [ ] **Step 1: `reference_tests.py`**

```python
"""CP1 — sessions I–II: variables, arithmetic, f-strings, conditionals, loops. 6 x 2 pts."""
TASKS = {
    "t1_price": {
        "points": 2,
        "names": ["total_t1"],
        "test": lambda d: isinstance(d.get("total_t1"), (int, float))
        and round(d["total_t1"], 2) == 31.50,
    },
    "t2_trace": {
        "points": 2,
        "names": ["answer_t2"],
        "test": lambda d: str(d.get("answer_t2", "")).strip().lower() == "c",
    },
    "t3_fix": {
        "points": 2,
        "names": ["count_t3"],
        "test": lambda d: d.get("count_t3") == 4,
    },
    "t4_loop": {
        "points": 2,
        "names": ["revenue_t4"],
        "test": lambda d: isinstance(d.get("revenue_t4"), (int, float))
        and round(d["revenue_t4"], 2) == 55.05,
    },
    "t5_receipt": {
        "points": 2,
        "names": ["line_t5"],
        "test": lambda d: d.get("line_t5") == "2x Bao Box: 19.80 EUR",
    },
    "t6_mcq": {
        "points": 2,
        "names": ["answer_t6"],
        "test": lambda d: str(d.get("answer_t6", "")).strip().lower() == "b",
    },
}
```

- [ ] **Step 2: Author `cp1_board_review.py`** (copy cp0's structure: identity header, per-task cell + hashed check cell, score cell, closing cell). Task content:

| Task | Prompt | Expected |
|---|---|---|
| t1 write | Founders Bowl: base 8.40 + topping 2.10, three portions, `round(_, 2)` | `total_t1 = 31.50` |
| t2 trace | `total = 0` · `for price in [4, 7]:` · `    total = total + price` · `    print(total)` — what is printed? a) `11` b) `4 7` c) `4` then `11` d) `7` then `11` | `answer_t2 = "c"` |
| t3 fix | Kevin counts orders ≥ 10 over `[16.40, 10.00, 9.10, 12.75, 10.00]`, wrote `>` — fix the comparison (values AND expected count deliberately differ from nb_02's ex23, so lab recall can't answer it) | `count_t3 = 4` |
| t4 write | Loop-sum the board-day orders `[14.20, 9.90, 22.50, 8.45]` | `revenue_t4 = 55.05` |
| t5 write | f-string with `:.2f` from given `qty = 2`, `item = "Bao Box"`, `total = 19.80` | `line_t5 = "2x Bao Box: 19.80 EUR"` |
| t6 mcq | Kevin writes `price = "4.99"`. `type(price)` is: a) float b) str c) int d) Error | `answer_t6 = "b"` |

Generate hash literals: `uv run python -c "from grader.hashcheck import expected_hash as h; print(h(31.50), h('c'), h(4), h(55.05), h('2x Bao Box: 19.80 EUR'), h('b'))"` — paste into the live-check cells (centralized `hash_answer` helper cell like cp0).

- [ ] **Step 3: Fixtures + test.** `cp1_solved.py`: minimal marimo notebook assigning all six names correctly + identity. `cp1_blank.py`: all answers `None`/empty. `tests/test_checkpoints.py`:

```python
"""Every authored checkpoint: solved fixture → full points, blank fixture → 0/graded."""
from pathlib import Path

import pytest

from grader.grade import grade_submission, load_tasks

ROOT = Path(__file__).parent.parent
FIXTURES = Path(__file__).parent / "fixtures"

CASES = [
    ("cp1", "cp1_solved.py", 12),
]


@pytest.mark.parametrize("cp,fixture,expected", CASES)
def test_solved_fixture_scores_full(cp, fixture, expected):
    result = grade_submission(FIXTURES / fixture, load_tasks(ROOT / "checkpoints" / cp))
    assert result.status == "graded"
    assert result.total == expected


@pytest.mark.parametrize("cp", [c[0] for c in CASES])
def test_blank_fixture_scores_zero(cp):
    result = grade_submission(
        FIXTURES / f"{cp}_blank.py", load_tasks(ROOT / "checkpoints" / cp)
    )
    assert result.status == "graded"
    assert result.total == 0
```

(Extend `CASES` in Tasks 15 and 19.)

- [ ] **Step 4: Validate WASM + grade + commit**

```bash
cd ../Introduction-to-Python-checkpoints
uv run pytest -v
uv run marimo export html-wasm checkpoints/cp1/cp1_board_review.py -o /tmp/cp1_out --mode edit
# serve /tmp/cp1_out, solve in browser: score cell reaches 12/12, no answer visible in code
git add checkpoints/cp1 tests/ && git commit -m "feat: CP1 board review — sessions I–II"
```

---

### Task 9: Session III in-lecture exercises (`ex_03_a/b`)

**Goal:** Two exercises (CP session → 2 blocks): write-a-function, fix-a-class-method.

**Files:**
- Create: `notebooks/exercises/ex_03_a.py`, `ex_03_b.py`
- Modify: `helpers/make_qr.py` (append `"ex_03_a", "ex_03_b"`)

**Acceptance Criteria / Verify:** same bar as Task 5 (`validate_notebooks.py 'exercises/ex_03_*.py'` → 2× ok; QR PNGs exist).

**Steps:**

- [ ] **Step 1: Write both:**

| File | Task | Check |
|---|---|---|
| `ex_03_a` | Write `wrap_price_exa(qty)` → `round(qty * 6.90, 2)` (the wrap costs 6.90) | check cell calls it inside try/except: `wrap_price_exa(3) == 20.70 and wrap_price_exa(1) == 6.90` |
| `ex_03_b` | Kevin's `Order` class: `total()` returns `self.price` (forgot the quantity) — fix the method | `Order("Pad Thai", 2, 8.90).total()` → `round(_, 2) == 17.80` |

Function/class check cells must guard: if the name is still `None`/undefined or the call raises, show "🔲 not attempted / ❌ still crashing" instead of erroring (wrap the probe calls in `try/except Exception`).

- [ ] **Step 2: QRs, validate, export, commit** (same commands as Task 5, adjusted paths; commit message `"feat: session III in-lecture exercises (functions, classes)"`).

---

### Task 10: Episode 3 lab + solutions + launcher (`nb_03` / `sol_03` / `tut_03`)

**Goal:** Session III lab: functions, scope, defaults, a first class — Episode 3 "The Copy-Paste Soup". Includes the Tip Calculator Championship bonus.

**Files:**
- Create: `notebooks/nb_03_lab_functions.py`
- Create (PRIVATE repo): `solutions/sol_03_lab_functions.py`
- Modify: `tutorials/tut_03_functions.qmd` (→ launcher, keep filename)

**Acceptance Criteria:** same structural bar as Task 6 (7 cores, 4 CP task types, patterns copied, launcher + dormant solutions link, validator + browser run green).

**Verify:** validator ok → export → solve in browser → progress 7/7.

**Steps:**

- [ ] **Step 1: Write `nb_03_lab_functions.py`.** Cold-open: Kevin has pasted the same receipt code 14 times; one change now takes an afternoon. Exercises:

| Ex | Type | Task | Check |
|---|---|---|---|
| 1.1 core | write | `fee_ex11(total)`: < 15 → 2.90, 15–30 → 1.50, ≥ 30 → 0 | probes `fee_ex11(10.0) == 2.90`, `(20.0) == 1.50`, `(40.0) == 0` |
| 1.2 core | write | `tip_ex12(total, percent)` → `round(total * percent / 100, 2)` | `tip_ex12(20, 10) == 2.0 and tip_ex12(12.0, 25) == 3.0` |
| 2.1 core | trace (ungraded) | Radio: `def boost(p): p = p + 1; return p` · `x = 5; boost(x); print(x)` → a) 5 b) 6 c) Error — reveal a (call doesn't change the global) | not counted |
| 2.2 core | fix | Kevin's `receipt_total_ex22(prices)` PRINTS the sum instead of returning it | `receipt_total_ex22([4.0, 6.0]) == 10.0` |
| 2.3 core | write | `greet_ex23(name, greeting="Moin")` → `f"{greeting}, {name}!"` | two probes: default + custom greeting |
| 3.1 core | write | Class `Order` with `__init__(self, item, qty, price)` + method `total()` | `Order("Wrap", 2, 6.90).total()` → 13.80 |
| boss ex40 core | write | Day report: three orders (Wrap×2 @ 6.90, Bowl×1 @ 24.90, Fries×5 @ 2.50) — use `Order` + `fee_ex11`: sum of `total()` + fee per order | `round(day_total_ex40, 2) == 58.50` (totals 13.80 + 24.90 + 12.50 = 51.20; fees 2.90 + 1.50 + 2.90 = 7.30) |
| ex50 core | mcq | Kevin's function prints instead of returns; `result = kevins_fn()` contains: a) the text b) 0 c) None d) Error | `answer_ex50 == "c"` |
| ex60 bonus | write | Championship: `tip_safe_ex60(total, percent)` returns 0.0 for negative/zero totals, else like `tip_ex12`; check runs a weird-input battery (0, −5, 100000) and crowns the survivor | probes |

All function/class probes in check cells wrapped in try/except (as in Task 9). Story: Championship framed as a class competition slide-callback; investor CAMEO max (Part-II arrival canon).

- [ ] **Step 2–4:** solutions notebook (private), `tut_03` launcher ("Episode 3 — The Copy-Paste Soup"), validate/export/render/commit — same motions as Task 6 (commit: `"feat: episode 3 lab — functions, scope, first class"`).

---

### Task 11: `lec_03` full rewrite (CP-session deck pattern debut)

**Goal:** Session III deck: the first CP-day deck — 📋 CP1 procedure slide, NO warm-up, 2 blocks (functions / scope + classes), QR a/b.

**Files:**
- Modify: `lectures/lec_03_functions.qmd` (full rewrite)
- Modify: `docs/side-quest-backlog.md`

**Acceptance Criteria:**
- [ ] Order: title → 📋 Checkpoint 1 slide → cold open → Block 1 (def, parameters, return, print-vs-return, defaults) → QR `ex_03_a` → Block 2 (scope, then a first class: `Order`, methods) → QR `ex_03_b` → lab handoff → wrap-up/teaser
- [ ] CP slide (exact content): 40 minutes, individual, no AI/neighbors; URL + QR handed out in class (NOT on the website — leave a `<!-- QR handed out live -->` placeholder comment, no URL in the deck); when done: Download → Python → Moodle "Checkpoint 1"; live checks are provisional, grading runs on our side
- [ ] ≥1 predict-first micro-question per block; cuts logged; render clean

**Verify:** render clean; `grep -c 'exercise-slide' lectures/lec_03_functions.qmd` ≥ 3 (CP slide uses `.exercise-slide` too).

**Steps:** inventory old deck → write CP slide → rewrite 2 blocks (print-vs-return gets its own predict-first question — it feeds CP-style MCQs) → QR slides → render/checkout/commit (`"feat: lec 03 full rewrite — CP1 day, functions and first class"`).

---

### Task 12: Session IV in-lecture exercises (`ex_04_a/b/c`)

**Goal:** Three exercises: list slicing, dict building, comprehension.

**Files:**
- Create: `notebooks/exercises/ex_04_a.py`, `ex_04_b.py`, `ex_04_c.py`
- Modify: `helpers/make_qr.py` (append)

**Acceptance Criteria / Verify:** Task-5 bar.

**Steps:**

- [ ] **Step 1: Write the three:**

| File | Task | Given | Check |
|---|---|---|---|
| `ex_04_a` | Predict `queue[-1]` (radio a/b/c → reveal), then write `last_two_exa = queue[-2:]` | `queue = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]` | `last_two_exa == ["Pizza Calzone", "Miso Ramen"]` |
| `ex_04_b` | Copy the menu (`dict(menu)`), raise Pad Thai to 9.20, add "Miso Ramen": 11.50 | `menu = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}` | `menu_exb == {"Falafel Wrap": 6.90, "Pad Thai": 9.20, "Founders Bowl": 10.40, "Miso Ramen": 11.50}` |
| `ex_04_c` | Happy hour: dict comprehension, 20% off everything, `round(_, 2)` each price | same `menu` as `_exb` given fresh | `happy_exc == {"Falafel Wrap": 5.52, "Pad Thai": 7.12, "Founders Bowl": 8.32}` |

- [ ] **Step 2: QRs, validate, export, commit** (`"feat: session IV in-lecture exercises (lists, dicts, comprehensions)"`).

---

### Task 13: Episode 4 lab + solutions + launcher (`nb_04` / `sol_04` / `tut_04`) — includes the `public/`-folder spike

**Goal:** Session IV lab: lists, dicts, sets, nesting, comprehensions — Episode 4 "The Menu Grows Up", boss = "A Day as a Courier" dict-map adventure. Settles how file-like data reaches WASM notebooks.

**Files:**
- Create: `notebooks/nb_04_lab_menu.py`
- Create (PRIVATE repo): `solutions/sol_04_lab_menu.py`
- Modify: `tutorials/tut_04_dimensions.qmd` (→ launcher)
- Possibly create: `notebooks/public/orders_day1.txt` (spike-dependent)
- Modify: `docs/authoring-conventions.md` (record the spike verdict)

**Acceptance Criteria:**
- [ ] 9 cores (ex11, ex12, ex21, ex22, ex23, ex32, ex33, ex40, ex50 — the MCQ counts) + 1 ungraded trace + 2 bonus per the table; patterns copied; launcher + dormant solutions link
- [ ] **Spike resolved and recorded:** either `notebooks/public/` files load in the WASM export (then the order-log exercise reads the file) or they don't (then the log ships as an inline multi-line string and the conventions doc says "inline data until Part III")
- [ ] Validator + full browser run green

**Verify:** validator ok → export → solve in browser (progress 9/9) → conventions doc has a "Data in notebooks" verdict line.

**Steps:**

- [ ] **Step 1: Spike (≤30 min, timeboxed).** Create `notebooks/public/orders_day1.txt`:

```
Falafel Wrap;2
Pad Thai;1
Founders Bowl;3
Miso Ramen;1
```

Minimal test notebook cell: `orders_text = (mo.notebook_location() / "public" / "orders_day1.txt")` — try reading it (per marimo docs, `mo.notebook_location()` yields a path/URL usable in both local and WASM contexts; in WASM plain `open()` does NOT fetch URLs). Export + serve + check the browser console. **Verdict A (works):** keep the file, exercise reads it. **Verdict B (doesn't):** delete `public/`, ship the same content as an inline string constant, add to conventions: "Inline string/dict data until Part III; `public/` files revisit with pandas in Session VIII." Record either way.

- [ ] **Step 2: Write `nb_04_lab_menu.py`.** Cold-open: the menu outgrew Kevin's seventeen variables (`price1`, `price2`, … `price_final_FINAL2`). Exercises:

| Ex | Type | Task | Check |
|---|---|---|---|
| 1.1 core | write | Order queue: given 4-item list, `queue_ex11 = queue + ["Falafel Wrap"]` (or copy+append) | `len(queue_ex11) == 5 and queue_ex11[-1] == "Falafel Wrap"` |
| 1.2 core | write | First three of the queue by slicing | `first_three_ex12 == ["Pad Thai", "Founders Bowl", "Pizza Calzone"]` |
| 2.1 core | write | Build the menu dict | `menu_ex21 == {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}` |
| 2.2 core | write | Copy + update: Pad Thai → 9.20, add Miso Ramen 11.50 | full-dict equality (4 items) |
| 2.3 core | write | Loyal regulars: `len(set(customers))` over `["mo", "lena", "mo", "kevin", "lena"]` | `n_regulars_ex23 == 3` |
| 3.1 core | trace (ungraded) | Radio: nested access `zones["north"]["fee"]` on a shown 2-level dict | reveal |
| 3.2 core | write | Happy-hour dict comprehension, 20% off the 4-item menu from 2.2, `round(_, 2)` each price | `{"Falafel Wrap": 5.52, "Pad Thai": 7.36, "Founders Bowl": 8.32, "Miso Ramen": 9.20}` |
| 3.3 core | fix | Kevin's `menu_ex22["padthai"]` KeyError — fix the key | `pad_price_ex33 == 9.20` |
| boss ex40 core | write | Courier run: follow `route = ["north", "north", "east"]` through the campus map dict with a loop, starting at `"gate"` | `destination_ex40 == "dorms"` |
| ex50 core | mcq | `menu["Sushi"]` when Sushi isn't a key: a) None b) "" c) KeyError d) adds it | `answer_ex50 == "c"` |
| ex60 bonus | write | Parse the order log (file or inline string per spike): `.splitlines()` + `.split(";")` → total portions | `portions_ex60 == 7` |
| ex61 bonus | write | Delivery fee via nested zones dict lookup for a given address zone | value equality |

Campus map for the boss (given cell):

```python
campus_map = {
    "gate":    {"north": "library", "east": "gym"},
    "library": {"north": "mensa", "south": "gate"},
    "mensa":   {"east": "dorms", "south": "library"},
    "gym":     {"west": "gate"},
    "dorms":   {"west": "mensa"},
}
```

Story: Kevin's forgotten wrap must reach the dorms before it achieves sentience.

- [ ] **Step 3–5:** solutions (private), `tut_04` launcher ("Episode 4 — The Menu Grows Up"), validate/export/render/commit both repos (`"feat: episode 4 lab — data structures and the courier run"`). Note: progress cell counts 9 cores here (header must say 9 — the MCQ is core, as in every lab).

---

### Task 14: `lec_04` full rewrite

**Goal:** Session IV deck: regular-session skeleton, warm-up recapping Session III, 3 blocks (lists+tuples / dicts+sets / nesting+comprehensions+data-in-notebooks), QR a/b/c.

**Files:**
- Modify: `lectures/lec_04_dimensions.qmd` (full rewrite)
- Modify: `docs/side-quest-backlog.md`

**Acceptance Criteria:**
- [ ] Regular skeleton per conventions; warm-up questions (vote → reveal): Q1 "function without `return` gives?" (None) · Q2 `boost(x)` scope question from the lab trace (global unchanged) · Q3 `Order("Wrap", 2, 6.90).total()` → which value (13.80)
- [ ] Block 3 includes ONE slide on getting data into notebooks matching the Task-13 spike verdict (file read demo if A, inline-string pattern + "files for real in Part III" if B)
- [ ] Tuples get one honest slide (fixed-length records; note: they become lists in some tools — foreshadows the grader constraint) — sets one slide (uniqueness)
- [ ] Cuts logged; render clean; `grep -c 'exercise-slide'` ≥ 4

**Steps:** inventory → warm-up → blocks → QR slides → render/checkout/commit (`"feat: lec 04 full rewrite — data structures blocks"`).

---

### Task 15: CP2 — sessions III–IV (private repo)

**Goal:** Checkpoint 2: the first checkpoint that grades a FUNCTION and a CLASS via `exprs` probes (the Fable-#1 mechanism, in production).

**Files (PRIVATE repo):**
- Create: `checkpoints/cp2/cp2_board_review.py`, `checkpoints/cp2/reference_tests.py`
- Create: `tests/fixtures/cp2_solved.py`, `tests/fixtures/cp2_blank.py`
- Modify: `tests/test_checkpoints.py` (extend `CASES` with `("cp2", "cp2_solved.py", 12)`)

**Acceptance Criteria:**
- [ ] 6 × 2 pts per table; function + class tasks graded via `exprs` (probe inputs differ from any shown in the notebook — hardcoding a probe result cannot pass)
- [ ] Only JSON-safe graded values (numbers/strings/lists/dicts)
- [ ] pytest green incl. solved 12/12 + blank 0

**Verify:** `uv run pytest -v` green; `uv run python -m grader.grade checkpoints/cp2 tests/fixtures/` → cp2_solved 12.

**Steps:**

- [ ] **Step 1: `reference_tests.py`**

```python
"""CP2 — sessions III–IV: functions, classes, dicts, comprehensions. 6 x 2 pts."""
TASKS = {
    "t1_function": {
        "points": 2,
        "names": [],
        "exprs": {
            "t1_low": "fee_t1(12.0)",
            "t1_mid": "fee_t1(25.0)",
            "t1_high": "fee_t1(60.0)",
        },
        "test": lambda d: d.get("t1_low") == 3.50
        and d.get("t1_mid") == 2.00
        and d.get("t1_high") == 0,
    },
    "t2_trace": {
        "points": 2,
        "names": ["answer_t2"],
        "test": lambda d: str(d.get("answer_t2", "")).strip().lower() == "a",
    },
    "t3_class": {
        "points": 2,
        "names": [],
        "exprs": {"t3_total": "Order('Ramen', 4, 11.50).total()"},
        "test": lambda d: isinstance(d.get("t3_total"), (int, float))
        and round(d["t3_total"], 2) == 46.00,
    },
    "t4_dict": {
        "points": 2,
        "names": ["menu_t4"],
        "test": lambda d: d.get("menu_t4")
        == {"Falafel Wrap": 7.20, "Pad Thai": 9.20, "Miso Ramen": 11.50},
    },
    "t5_comprehension": {
        "points": 2,
        "names": ["doubled_t5"],
        "test": lambda d: d.get("doubled_t5") == [25.0, 17.8, 30.4],
    },
    "t6_mcq": {
        "points": 2,
        "names": ["answer_t6"],
        "test": lambda d: str(d.get("answer_t6", "")).strip().lower() == "a",
    },
}
```

- [ ] **Step 2: Author `cp2_board_review.py`.** Task content (numbers differ from all labs):

| Task | Prompt | Expected |
|---|---|---|
| t1 write fn | `fee_t1(total)`: < 20 → 3.50, 20–40 → 2.00, ≥ 40 → 0 ("the new courier tariff"). Notebook live-check probes DIFFERENT inputs than the hidden suite (e.g. 15/30/45) so grader probes can't be pattern-matched | function |
| t2 trace | the `boost(p)` scope snippet with new names — printed value of the untouched global: a) 5 b) 6 c) Error | `"a"` |
| t3 fix class | Kevin's `Order.total()` returns `self.price` — fix to `qty * price` | method |
| t4 write | Build the winter menu dict: Falafel Wrap 7.20, Pad Thai 9.20, Miso Ramen 11.50 | dict |
| t5 write | Comprehension: double `[12.5, 8.9, 15.2]` | `[25.0, 17.8, 30.4]` |
| t6 mcq | `orders = [1, 2, 3]; orders.append([4, 5]); len(orders)` → a) 4 b) 5 c) Error | `"a"` |

Live checks: value tasks hashed as usual; function/class tasks live-check by calling with the IN-NOTEBOOK inputs and hashing that result (provisional feedback), while `reference_tests.py` probes different inputs — state in the notebook: "the live check is provisional; final grading uses different inputs."

- [ ] **Step 3: Fixtures + tests + WASM check + commit** (motions of Task 8 Steps 3–4; commit `"feat: CP2 board review — functions and data structures, exprs-graded"`).

---

### Task 16: Session V in-lecture exercises (`ex_05_a/b`)

**Goal:** Two exercises (CP session): which-exception predict, try/except write.

**Files:**
- Create: `notebooks/exercises/ex_05_a.py`, `ex_05_b.py`
- Modify: `helpers/make_qr.py` (append)

**Acceptance Criteria / Verify:** Task-5 bar.

**Steps:**

- [ ] **Step 1: Write both:**

| File | Task | Check |
|---|---|---|
| `ex_05_a` | Predict: `int("3.5")` → radio a) 3 b) 3.5 c) ValueError d) TypeError → reveal c + one-liner ("int() refuses decimal strings"); then fix the given line to get 3.5 as a number | `qty_exa == 3.5` |
| `ex_05_b` | Kevin's `float(order_text)` crashes on `order_text = "drei"` — wrap in try/except ValueError, default 0.0 | `price_exb == 0.0` |

- [ ] **Step 2: QRs, validate, export, commit** (`"feat: session V in-lecture exercises (exceptions)"`).

---

### Task 17: Episode 5 lab + solutions + launcher (`nb_05` / `sol_05` / `tut_05`)

**Goal:** Session V lab: tracebacks, try/except, raise, assertions, debugging — Episode 5 "The 3-AM Checkout" + the health-inspector audit.

**Files:**
- Create: `notebooks/nb_05_lab_checkout.py`
- Create (PRIVATE repo): `solutions/sol_05_lab_checkout.py`
- Modify: `tutorials/tut_05_errors.qmd` (→ launcher)

**Acceptance Criteria:** Task-6 structural bar (7 cores + trace + bonus; validator + browser run green; launcher + dormant link).

**Steps:**

- [ ] **Step 1: Write `nb_05_lab_checkout.py`.** Cold-open: Kevin rewrote the checkout at 3 AM on four energy drinks; this morning the health inspector announced a visit. Exercises:

| Ex | Type | Task | Check |
|---|---|---|---|
| 1.1 core | trace (ungraded) | Radio: `menu = {"Wrap": 6.90}; print(menu["wrap"])` → a) 6.90 b) None c) TypeError d) KeyError — reveal d + "read the last traceback line first" | not counted |
| 1.2 core | write | `safe_price_ex12(text)`: `float(text)`, on ValueError return 0.0 | probes `("4.20") == 4.2` and `("drei") == 0.0` |
| 2.1 core | fix | Kevin's checkout: `12.50 * 2 - 8.30` should be `+` (he "subtracted the salad, psychologically") plus a wrong variable name in the f-string — two bugs, both terminate | `round(checkout_total_ex21, 2) == 33.30` |
| 2.2 core | write | `validate_order_ex22(price)`: raise `ValueError` if `price < 0`, else return True (the inspector's rule: every order MUST have price ≥ 0) | probes: `(9.90) is True`; negative input raises ValueError (checked via try/except in the check cell) |
| 2.3 core | write | Audit: find the index of the invalid price in `[6.90, 8.90, -1.0, 11.50]` with a loop | `bad_index_ex23 == 2` |
| 3.1 core | write | `parse_qty_ex31(text)`: `int(text)`, on ValueError return 1 ("one wrap is always a safe default") | probes `("3") == 3`, `("??") == 1` |
| boss ex40 core | write | Harden the checkout: `robust_total_ex40(orders)` over `[("Wrap", 13.80), ("Ramen", -2.0), ("Bowl", "kaputt"), ("Thai", 8.90)]` — skip negatives and non-numbers, sum the rest | probe → `round(_, 2) == 22.70` |
| ex50 core | mcq | After the except branch runs, the program: a) crashes b) continues after the try block c) restarts the try | `answer_ex50 == "b"` |
| ex60 bonus | trace-fix | A full 6-line traceback (as text) from Kevin's code: which line number do you fix? answered as `answer_ex60 = <int>` | int equality |

All probes wrapped in try/except in check cells. Health-inspector story beats in §2; Formular 27b/6 gets its cameo in the wrap-up teaser (Episode 6 = the government episode, Plan 3).

- [ ] **Step 2–4:** solutions (private), `tut_05` launcher ("Episode 5 — The 3-AM Checkout"), validate/export/render/commit (`"feat: episode 5 lab — errors, exceptions, the inspector's audit"`).

---

### Task 18: `lec_05` full rewrite

**Goal:** Session V deck: CP-day skeleton (📋 CP2 slide, no warm-up), 2 blocks (tracebacks + try/except / debugging strategy + assertions + raise), QR a/b.

**Files:**
- Modify: `lectures/lec_05_errors.qmd` (full rewrite)
- Modify: `docs/side-quest-backlog.md`

**Acceptance Criteria:**
- [ ] CP2 slide (same content pattern as Task 11's CP1 slide, "Checkpoint 2" + Moodle label)
- [ ] Block 1: anatomy of a traceback (read bottom-up) · common exception types (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError) · try/except · except-with-type — all on Kevin's checkout examples
- [ ] Block 2: debugging strategy (read → reproduce → isolate → print/assert → fix) · `assert` for invariants (the inspector's price ≥ 0 rule) · `raise` — when your own code should refuse
- [ ] ≥1 predict-first per block (e.g. "which exception?" vote); cuts logged; render clean; `grep -c 'exercise-slide'` ≥ 3

**Steps:** inventory → CP slide → blocks → QRs → render/checkout/commit (`"feat: lec 05 full rewrite — CP2 day, errors and debugging"`).

---

### Task 19: CP3 — session V + Part I recap (private repo)

**Goal:** Checkpoint 3 (taken at start of Session VI): exceptions + a deliberate recap sweep of sessions I–IV. Closes Part I's assessment.

**Files (PRIVATE repo):**
- Create: `checkpoints/cp3/cp3_board_review.py`, `checkpoints/cp3/reference_tests.py`
- Create: `tests/fixtures/cp3_solved.py`, `tests/fixtures/cp3_blank.py`
- Modify: `tests/test_checkpoints.py` (extend `CASES` with `("cp3", "cp3_solved.py", 12)`)

**Acceptance Criteria:** Task-15 bar (6 × 2, exprs where functions, JSON-safe, pytest green, 12/12 + 0 fixtures).

**Steps:**

- [ ] **Step 1: `reference_tests.py`**

```python
"""CP3 — session V + Part I recap: exceptions, debugging, recap I–IV. 6 x 2 pts."""
TASKS = {
    "t1_safe": {
        "points": 2,
        "names": [],
        "exprs": {
            "t1_good": "safe_price_t1('4.20')",
            "t1_bad": "safe_price_t1('kaputt')",
        },
        "test": lambda d: d.get("t1_good") == 4.20 and d.get("t1_bad") == 0.0,
    },
    "t2_trace": {
        "points": 2,
        "names": ["answer_t2"],
        "test": lambda d: str(d.get("answer_t2", "")).strip().lower() == "d",
    },
    "t3_fix": {
        "points": 2,
        "names": ["orders_total_t3"],
        "test": lambda d: isinstance(d.get("orders_total_t3"), (int, float))
        and round(d["orders_total_t3"], 2) == 44.90,
    },
    "t4_recap_loop": {
        "points": 2,
        "names": ["late_t4"],
        "test": lambda d: d.get("late_t4") == 2,
    },
    "t5_recap_fstring": {
        "points": 2,
        "names": ["line_t5"],
        "test": lambda d: d.get("line_t5") == "Miso Ramen costs 11.50 EUR",
    },
    "t6_mcq": {
        "points": 2,
        "names": ["answer_t6"],
        "test": lambda d: str(d.get("answer_t6", "")).strip().lower() == "b",
    },
}
```

- [ ] **Step 2: Author `cp3_board_review.py`.** Task content:

| Task | Prompt | Expected |
|---|---|---|
| t1 write fn | `safe_price_t1(text)`: float or 0.0 on ValueError (live-check probes different strings than the hidden suite) | function |
| t2 trace | `menu = {"Wrap": 6.90}` · `print(menu["wrap"])` → a) 6.90 b) None c) TypeError d) KeyError | `"d"` |
| t3 fix | Kevin's crashing day-total over `[20.80, 15.20, 8.90]` (bug: he indexes one past the end in his loop — `range(len(prices) + 1)`) | `orders_total_t3 = 44.90` |
| t4 recap | Count deliveries over 30 min in `[12, 31, 45, 18, 22]` (loop + condition, sessions I–II recap) | `late_t4 = 2` |
| t5 recap | f-string from `item = "Miso Ramen"`, `price = 11.50`: `"Miso Ramen costs 11.50 EUR"` | string |
| t6 mcq | `try/except ValueError` around code that raises KeyError — what happens? a) except runs b) the KeyError propagates (crash) c) both | `"b"` |

- [ ] **Step 3: Fixtures + tests + WASM check + commit** (`"feat: CP3 board review — errors plus Part I recap"`).

---

### Task 20: Part-I validation pass + docs sync

**Goal:** Everything Part I proven green in one sweep; project docs and memory match reality; PR updated.

**Files:**
- Modify: `docs/superpowers/specs/2026-07-09-fable-review.md` (mark #4/#5/#10 resolved, note #7 stays a user-led merge gate)
- Modify: memory `python-course-overhaul-2026.md` (status: Plan 2 executed; next: Plan 3)
- Modify: `docs/side-quest-backlog.md` (ensure every deck cut landed)

**Acceptance Criteria:**
- [ ] `uv run python helpers/validate_notebooks.py` → all ok (nb_01–05, ex_01–05, no solutions present)
- [ ] `uv run python helpers/export_marimo.py` → all exports succeed
- [ ] All five decks + five tutorial pages render individually; `git checkout -- _repo-md/` after
- [ ] Private repo: `uv run pytest -v` fully green (grader suite + cp1–3 tests)
- [ ] `grep -ri copilot lectures/lec_0[1-5]*.qmd tutorials/tut_0[1-5]*.qmd` → no matches
- [ ] No `notebooks/solutions/` content committed in the public repo
- [ ] Push branch; PR description updated with the Plan-2 summary. **No AI-attribution lines anywhere.**

**Verify:** every command above exits 0; `gh pr view` shows the updated body.

**Steps:** run the battery → fix anything red → update the three docs → commit (`"chore: Part I validation pass + docs sync"`) → push → update PR body via `gh pr edit`.

**Remaining user-led gates (NOT tasks, tracked in dress-rehearsal §B):** molab login screenshot (#7 — gate for publishing molab badges), chatbot prompt install (Task 3's deliverable), GitHub Education / deploy, weak-laptop run, Moodle round-trip, checkpoints-repo push.

---

## Execution order & dependencies

```
Task 1 (conventions+validator) ─► everything else
Task 2 (solutions pipeline) ─► Tasks 6, 10, 13, 17 (they author solutions)
Task 3 (chatbot prompt) — independent
Task 4 (lec_01 rewrite) ─► Tasks 7, 11, 14, 18 (deck skeleton exemplar)
Session slices, in order:  [5 ─► 6 ─► 7] ─► 8 (CP1)
                           [9 ─► 10 ─► 11]
                           [12 ─► 13 ─► 14] ─► 15 (CP2, needs III+IV → after 10 & 13)
                           [16 ─► 17 ─► 18] ─► 19 (CP3, after 17)
Task 20 last (after 3, 7, 8, 11, 14, 15, 18, 19).
```

Deck tasks follow their exercise tasks (QR URLs must exist). CP tasks follow their sessions' labs (task values must consciously differ from lab values). A clean pause point exists after every session slice.
