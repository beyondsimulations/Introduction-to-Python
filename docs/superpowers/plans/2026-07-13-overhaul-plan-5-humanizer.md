# Plan 5 — Humanizer Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite all student-facing course copy against one merged editing brief (AI-tell scrub + voice strengthening + US English + term/conciseness consistency), then close with the pre-semester verify-live checklist.

**Architecture:** A coordinator-authored editing brief is the single source of truth; a calibration file (lec_01) gates the fan-out; per-file implementer+reviewer agent pairs produce one commit per file (small files batched); a final battery proves nothing broke. Approved spec: `docs/superpowers/specs/2026-07-13-plan5-humanizer-design.md`.

**Tech Stack:** Quarto (.qmd revealjs + pages), marimo notebooks (.py), `helpers/validate_notebooks.py`, private-repo pytest, grep sweeps.

---

## Shared definitions (read before any task)

### Per-file editing protocol (referenced by Tasks 2–7)

Every file unit goes through this cycle:

1. **Implementer agent** receives: the full editing brief (`docs/superpowers/specs/2026-07-13-plan5-editing-brief.md`), the target file(s), the applicable register card name, and the file-specific notes from the task. It rewrites prose only, honoring every guardrail, then self-checks against the brief's checklist and commits.
2. **Reviewer agent** receives the brief, the diff (`git show <sha>`), and the original file. It checks, in order: (a) guardrail compliance — zero changes to code cells, commands, expected values, check-cell strings, hashes, hint skeletons, story facts/numbers, links, QR slugs, YAML keys, revealjs directives; (b) meaning preservation — no instruction changed its requirements; (c) register fit — matches the file's register card; (d) cringe veto — anything that would make an instructor wince read aloud is flagged for revert; (e) residual AI tells. Findings go back to the implementer; loop until clean.
3. **Coordinator (Fable, in-session)** reads the final diff of every file before the task is marked complete.

Commit message format: `style: <file-stem> copy pass` (e.g. `style: lec_02 copy pass`); batched commits name the batch (e.g. `style: tut_01-05 copy pass`). Never any AI attribution or process meta, in either repo.

### Register cards (defined fully in the brief; names used in tasks)

- `deck` — lively but restrained; first-person instructor asides allowed; cringe = revert.
- `reference` — sober, scannable, zero jokes.
- `notebook` — dry, precise; light warmth only in wrap-up cells.

### Prose-only rule for notebooks

In `.py` notebooks, editable text lives ONLY inside `mo.md(...)` / `mo.md(r"""...""")` string literals (and module docstrings if prose-like). Code, f-string expressions inside those literals, `___` hint skeletons, and check-cell strings are untouchable. After ANY notebook edit, run the validation command for that repo before committing; a notebook that fails validation is reverted (`git checkout -- <file>`), not shipped half-edited.

### Verification commands

- Public notebooks: `uv run python helpers/validate_notebooks.py` → all 32 pass.
- Private repo tests: `cd ../Introduction-to-Python-checkpoints && uv run pytest -q` → `38 passed`.
- Full site render (foreground, long timeout): `quarto render` → exits 0, 30 output targets.
- Single-file renders are allowed for spot checks and no longer touch `_repo-md/` (guarded by `QUARTO_PROJECT_RENDER_ALL`).

### Model policy

Implementers and reviewers on **Opus**; **Sonnet** acceptable for the mechanical small batches (Task 5 tutorials, `ex_` batches in Task 6). No Fable subagents — Fable authors the brief (Task 1), decides the glossary, and reads every diff in-session.

---

### Task 1: Editing brief + term glossary

**Goal:** One committed brief that merges all four rubrics, the three register cards, the hard guardrails, and a decided course-wide term glossary.

**Files:**
- Create: `docs/superpowers/specs/2026-07-13-plan5-editing-brief.md`

**Acceptance Criteria:**
- [ ] Brief contains: AI-tell catalog, conciseness substitutions, US-English rules, term glossary (decided, not open questions), the three register cards, the hard guardrails, and a short implementer self-check list
- [ ] Glossary entries name a winner and the losers it replaces (e.g. "lab notebook → use *lab*; never *lab exercise*")
- [ ] Banned-word list is explicit (it feeds Task 8's grep) with its literal-use allowlist rules
- [ ] Committed on `overhaul-plan-5-humanizer`

**Verify:** `grep -c '^## ' docs/superpowers/specs/2026-07-13-plan5-editing-brief.md` → ≥ 6 sections

**Steps:**

- [ ] **Step 1: Scout sweep (Opus agent).** Dispatch one scout with read access to `lectures/`, `tutorials/`, `general/`, `index.qmd`, `notebooks/`, and `../Introduction-to-Python-checkpoints/{checkpoints,solutions}/`. It returns: (a) every course term used inconsistently, with per-variant counts and example locations (seed candidates: notebook/lab/lab notebook, checkpoint/CP, session/lecture + Roman vs Arabic numbering, exercise/task, deck/slides/lecture page, hint/tip, browser editor/playground/WASM notebook); (b) UK-spelling occurrences beyond the known ones; (c) the 20 most frequent AI-vocabulary words actually present in the copy, with counts (so the brief bans what exists, not a generic list).
- [ ] **Step 2: Coordinator writes the brief.** Fable authors `docs/superpowers/specs/2026-07-13-plan5-editing-brief.md` in-session (documented exception to subagent-only implementation, per spec §7). Required sections: `## What this is` (one paragraph + how implementers use it), `## AI tells to remove` (condensed from humanizer SKILL.md v2.3.0: significance inflation, promotional tone, -ing tack-ons, vague attribution, rule of three, negative parallelism, copula avoidance, synonym cycling, false ranges, em-dash overuse, mechanical boldface, inline-header bullets, AI vocabulary from the scout's real-occurrence list, filler, hedging, generic upbeat endings), `## Voice: what to add` (rhythm variation, first-person asides where the register allows, opinions over neutral reporting — with 2–3 before/after examples taken from actual course copy), `## Register cards` (deck / reference / notebook, as in the spec), `## US English` (rules + the scout's found offenders), `## Term glossary` (Fable-decided winners), `## Hard guardrails` (verbatim from spec §2), `## Banned-word list for the final grep` (explicit regex-ready list + allowlist rules, e.g. *underscore* exempt in Python identifier context), `## Implementer self-check` (5-line checklist run before committing).
- [ ] **Step 3: Commit.**

```bash
git add docs/superpowers/specs/2026-07-13-plan5-editing-brief.md
git commit -m "docs: plan 5 editing brief and term glossary"
```

---

### Task 2: Calibration — lec_01 full cycle + user gate

**Goal:** Prove the brief produces the right tone on one deck before touching 50+ files.

**Files:**
- Modify: `lectures/lec_01_introduction.qmd`

**Acceptance Criteria:**
- [ ] lec_01 rewritten per protocol (register: `deck`), reviewer clean, Fable read done
- [ ] Single-file render passes: `quarto render lectures/lec_01_introduction.qmd` → exit 0
- [ ] **USER GATE:** user has skimmed the lec_01 commit and confirmed the tone before any other task starts
- [ ] If the user rejects the tone: brief revised, lec_01 reverted and redone; gate repeats

**Verify:** `quarto render lectures/lec_01_introduction.qmd` → exit 0, then user confirmation in chat

**Steps:**

- [ ] **Step 1:** Run the per-file editing protocol on `lectures/lec_01_introduction.qmd` (register `deck`). File notes for the implementer: this deck was factually patched in Plan 1 but its teaching copy was never voice-rewritten; expect denser AI-tell residue than the Plan-2/3/4 decks. Story slides: Episode 1 canon (founding, Kevin, the food-delivery startup) is frozen; jokes may be sharpened.
- [ ] **Step 2:** Render check: `quarto render lectures/lec_01_introduction.qmd` → exit 0.
- [ ] **Step 3:** Commit `style: lec_01 copy pass`. Present before/after excerpts (3–4 representative slides) to the user in chat and wait for explicit approval. Do not start Tasks 3–7 before approval.

---

### Task 3: Decks lec_02–lec_10

**Goal:** The remaining nine decks pass through the protocol, one commit each.

**Files:**
- Modify: `lectures/lec_02_control.qmd`, `lectures/lec_03_functions.qmd`, `lectures/lec_04_dimensions.qmd`, `lectures/lec_05_errors.qmd`, `lectures/lec_06_modules.qmd`, `lectures/lec_07_scientific.qmd`, `lectures/lec_08_pandas.qmd`, `lectures/lec_09_plotting.qmd`, `lectures/lec_10_projects.qmd`

**Acceptance Criteria:**
- [ ] Nine commits, register `deck`, protocol followed per file
- [ ] lec_03 UK spellings gone (`behaviour` ×5), lec_10 `analyse` gone
- [ ] lec_10 uv-init slide aligned to git-basics' conditional wording (repo auto-creation only when git is installed — a short qualifier is enough for a slide)
- [ ] Episode canon intact in every deck (reviewer checks against pre-edit story facts)
- [ ] Each deck renders: `quarto render lectures/<file>.qmd` → exit 0 before its commit

**Verify:** `grep -rinE '\b(behaviour|analyse)\b' lectures/` → no matches; nine `style: lec_XX copy pass` commits

**Steps:**

- [ ] **Step 1:** For each deck in order lec_02 → lec_10: run the per-file editing protocol (register `deck`), render the single file, commit. Render files individually — combined `quarto render fileA fileB` fails (known pandoc quirk).
- [ ] **Step 2:** File notes: lec_02–05 are Plan-2 rewrites, lec_06–09 Plan-3, lec_10 Plan-4 — newer decks need lighter touches; do not manufacture diffs where copy is already clean. lec_10 additionally gets the uv-init conditional-wording alignment (see acceptance criteria; source wording in `general/git-basics.qmd`, section "GitHub setup").
- [ ] **Step 3:** After the last deck: `git checkout -- _repo-md/` is NOT needed anymore (render guard); confirm `git status` shows only intended changes.

---

### Task 4: index.qmd + general pages

**Goal:** Landing page and reference pages scrubbed at register `reference`.

**Files:**
- Modify: `index.qmd`, `general/ai-tools.qmd`, `general/faq.qmd`, `general/syllabus.qmd`, `general/uv.qmd`, `general/git-basics.qmd`, `general/cheatsheet.qmd`, `general/literature.qmd`

**Acceptance Criteria:**
- [ ] Eight commits (one per file), register `reference`, protocol followed
- [ ] `index.qmd` `organize` etc. conform to US English (already US — keep)
- [ ] `general/cheatsheet.qmd`: prose lines only; every code table row byte-identical
- [ ] `general/literature.qmd`: intro lines only; citation entries untouched
- [ ] `general/imprint.qmd` and `general/privacy.qmd` NOT touched (excluded, legal)
- [ ] git-basics: troubleshooting symptom headings stay symptom-first (that structure was a review outcome, not a style accident)

**Verify:** `git log --oneline main..HEAD -- general/ index.qmd | wc -l` → 8; `git diff main..HEAD -- general/imprint.qmd general/privacy.qmd` → empty

**Steps:**

- [ ] **Step 1:** Per-file protocol on each of the eight files (register `reference`). File notes: ai-tools facts were web-verified 2026-07-11 — wording may change, facts and dates may not; faq answers must stay aligned with tut_01's persistence wording; syllabus session titles are fixed (Plan-4 decisions), descriptions editable.
- [ ] **Step 2:** Render each edited page singly (`quarto render general/<file>.qmd`) → exit 0, commit per file.

---

### Task 5: Tutorial launchers

**Goal:** The nine small launcher pages scrubbed, two batched commits.

**Files:**
- Modify: `tutorials/tut_01_introduction.qmd` … `tutorials/tut_05_errors.qmd` (batch 1), `tutorials/tut_06_modules.qmd` … `tutorials/tut_09_plotting.qmd` (batch 2)

**Acceptance Criteria:**
- [ ] Two commits: `style: tut_01-05 copy pass`, `style: tut_06-09 copy pass`; register `reference`
- [ ] Launch buttons, notebook links, and molab URLs byte-identical
- [ ] tut_01 persistence wording stays consistent with faq (Task 4 note cuts both ways)
- [ ] tut_08/09 CDN-flake reload note preserved in meaning

**Verify:** `git diff main..HEAD --stat -- tutorials/` shows all 9 files; links grep unchanged: `grep -c 'marimo' tutorials/*.qmd` matches pre-edit counts

**Steps:**

- [ ] **Step 1:** Record pre-edit link counts: `grep -c 'href\|marimo' tutorials/*.qmd > /tmp/tut-links-before.txt` (scratchpad).
- [ ] **Step 2:** Batch 1 (tut_01–05) through the protocol as ONE implementer+reviewer cycle (Sonnet acceptable); render each singly; one commit. Then batch 2 (tut_06–09) the same way.
- [ ] **Step 3:** Re-run the link-count grep and diff against the before file → identical.

---

### Task 6: Public notebook prose

**Goal:** `mo.md()` prose in the template, 9 labs, and 23 exercises scrubbed at register `notebook`, validation-gated.

**Files:**
- Modify: `notebooks/_template.py`, `notebooks/nb_01_lab_founding.py` … `notebooks/nb_09_lab_pitch.py`, `notebooks/exercises/ex_01_a.py` … `notebooks/exercises/ex_09_c.py`

**Acceptance Criteria:**
- [ ] Commits: one for `_template.py` + one per lab (9) + one per session's exercises (9 batches: ex_01_* … ex_09_*)
- [ ] Prose-only rule enforced (see Shared definitions); hint skeletons (`___`), check cells, expected values, story numbers untouched
- [ ] Prompts stay symptom-only — reviewer explicitly re-checks no expected value or bug location crept into reworded prompts
- [ ] `uv run python helpers/validate_notebooks.py` green after every commit batch
- [ ] Any notebook failing validation reverted, not patched forward

**Verify:** `uv run python helpers/validate_notebooks.py` → 32/32 pass on the final state

**Steps:**

- [ ] **Step 1:** `_template.py` through the protocol (register `notebook`), validate, commit `style: notebook template copy pass`.
- [ ] **Step 2:** Labs nb_01 → nb_09, one protocol cycle + validation run + commit each (`style: nb_01 copy pass` …). File notes: wrap-up cells may keep light warmth; red-error-pause teach lines (crash-prone labs) keep their meaning; boss-exercise wording in nb_03 reuses revenue/margin function names — frozen.
- [ ] **Step 3:** Exercise batches ex_01_* → ex_09_* (Sonnet acceptable), one cycle + validation + commit per session (`style: ex_01 copy pass` …). QR-exercise hint accordions (Part II) keep their Hint 1 / Hint 2 structure exactly.

---

### Task 7: Private repo prose (checkpoints + solutions)

**Goal:** CP task wording and solution walkthroughs scrubbed at register `notebook`, with graded semantics frozen and 38 tests green.

**Files (in `../Introduction-to-Python-checkpoints/`):**
- Modify: `checkpoints/cp1/cp1_board_review.py`, `checkpoints/cp2/cp2_board_review.py`, `checkpoints/cp3/cp3_board_review.py`, `checkpoints/cp4/cp4_board_review.py`, `checkpoints/cp5/cp5_board_review.py`, `solutions/sol_01_lab_founding.py` … `solutions/sol_09_lab_pitch.py`

**Acceptance Criteria:**
- [ ] Commits in the private repo: one per CP (5) + two solution batches (`style: sol_01-05 copy pass`, `style: sol_06-09 copy pass`)
- [ ] CP task requirements frozen: variable names, expected values, task semantics, point values, hash salts — wording only may change
- [ ] MCQ neutrality preserved: live checks still say "recorded", never ✅/❌
- [ ] `uv run pytest -q` in the private repo → `38 passed` after every commit
- [ ] cp0 and `reference_tests.py` files untouched
- [ ] No AI attribution/process meta in private-repo commits either

**Verify:** `cd ../Introduction-to-Python-checkpoints && uv run pytest -q` → `38 passed`; `git -C ../Introduction-to-Python-checkpoints diff HEAD~7 --stat` shows only the 14 intended files

**Steps:**

- [ ] **Step 1:** CP notebooks cp1 → cp5, one protocol cycle each (register `notebook`; reviewer diff-checks that every string a reference test could key off is unchanged — cross-read `checkpoints/cpN/reference_tests.py` to know what is load-bearing). Run pytest after each; commit in the private repo.
- [ ] **Step 2:** Solution batches sol_01–05 and sol_06–09 (walkthrough prose only; code and printed values frozen). Pytest + commit per batch.

---

### Task 8: Validation battery + grep sweeps

**Goal:** Prove the whole pass shipped clean: site builds, notebooks run, tests pass, no UK spellings, no banned words, em-dash count reported.

**Files:**
- Modify: `_repo-md/` (regenerated by full render only)

**Acceptance Criteria:**
- [ ] Full `quarto render` exit 0 (run foreground with a 10-minute timeout — background renders have died silently before)
- [ ] `uv run python helpers/validate_notebooks.py` → 32/32
- [ ] Private pytest → 38 passed
- [ ] UK grep zero; banned-word grep zero after allowlist review (list from the brief)
- [ ] Em-dash per-file count reported in the task summary (target: reduced vs `main`, not zero)
- [ ] `_repo-md/` refresh committed if changed

**Verify:** all five commands below green in one session

**Steps:**

- [ ] **Step 1:** `quarto render` (foreground, timeout 600000ms) → exit 0.
- [ ] **Step 2:** `uv run python helpers/validate_notebooks.py` → 32/32.
- [ ] **Step 3:** `cd ../Introduction-to-Python-checkpoints && uv run pytest -q` → 38 passed.
- [ ] **Step 4: UK-spelling grep** (imprint/privacy excluded by scope, license is legal wording there):

```bash
grep -rinE '\b(behaviour|colour|organis(e|ed|ing)|analys(e|ed|ing)|centre|favour|optimis(e|ed|ing)|realis(e|ed|ing)|recognis(e|ed|ing)|licence)\b' \
  lectures/ tutorials/ general/ai-tools.qmd general/faq.qmd general/syllabus.qmd general/uv.qmd general/git-basics.qmd general/cheatsheet.qmd general/literature.qmd index.qmd notebooks/
```
Expected: no output.

- [ ] **Step 5: Banned-word grep** using the exact list from the brief's `## Banned-word list` section over the same paths; review each hit against the brief's allowlist rules (literal/technical uses pass, e.g. *underscore* as the `_` character); rewrite any true positives and re-run to zero. Em-dash report: `for f in lectures/*.qmd general/*.qmd index.qmd; do printf '%s %s\n' "$(grep -o '—' $f | wc -l)" "$f"; done | sort -rn` — record, compare against `git show main:<file>` counts.
- [ ] **Step 6:** Commit `_repo-md/` refresh if the render changed it: `git add _repo-md && git commit -m "chore: refresh repo-md after copy pass"`.

---

### Task 9: Verify-live finale (guided, user-led)

**Goal:** Work through the spike doc's verify-live checklist with the user live; record results; land any copy corrections.

**Files:**
- Modify: `docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md` (results recorded), possibly `general/git-basics.qmd` / `lectures/lec_10_projects.qmd` (corrections)

**Acceptance Criteria:**
- [ ] Each checklist item verified live or explicitly deferred by the user: Zed git-panel wording, `gh auth login` prompt text, `git: create remote` flow, per-OS default branch names
- [ ] Spike doc updated: each item marked verified-with-date or deferred
- [ ] Any wording mismatch found → correction commit(s) to the affected copy on this branch
- [ ] Non-blocking: if the user defers, PR #5 proceeds and this becomes a follow-up (spec §6)

**Verify:** `grep -c 'verified 2026' docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md` ≥ 1, or an explicit deferral note in the doc

**Steps:**

- [ ] **Step 1:** Coordinator (not a subagent) walks the user through each item; the user runs UI checks and pastes/screenshots results; terminal checks via `! <command>` in-session (e.g. `! gh auth status`, `! git config --get init.defaultBranch`).
- [ ] **Step 2:** Update the spike doc per item; commit `docs: verify-live results in zed git auth spike`.
- [ ] **Step 3:** If copy corrections arose: run affected files through a mini protocol cycle (implementer fix + reviewer + render) and commit.

---

## After all tasks

Final cross-task review (Opus, whole branch vs `main`), then PR #5 via the finishing-a-development-branch flow: PR body = deliverable + test plan only, no AI-process meta. Private-repo commits are already landed (no PR there).
