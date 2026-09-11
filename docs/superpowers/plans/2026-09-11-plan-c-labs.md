# Plan C — Longer labs (nb_01–nb_09 + private solutions)

> **For agentic workers:** one worker per lab; each task is self-contained. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Every lab keeps the median student busy for ~75 min (regular sessions) / ~65 min (CP sessions): 10–11 core exercises, story-driven, not drills.

**Architecture:** New core exercises are added inside the section whose concept they practice, in the lab's existing cell pattern (instruction cell → your-code cell with `None` → check cell → hint accordion). The header count, progress cell, and wrap-up line update. The matching solution notebook in the private repo gets the same cells with answers filled in and no hints.

Spec: `docs/superpowers/specs/2026-09-09-session-length-and-notebook-onboarding-design.md` (Workstream C). Conventions: `docs/authoring-conventions.md` (binding). Onboarding rules from Plan A apply (marker line, verdict labels).

## Global Constraints

- No emojis anywhere. Verdict labels: `Correct — Exercise N.M: …`, `Wrong — Exercise N.M: …`, `Not attempted — Exercise N.M: … Assign it to \`x\` (a \`print\` alone doesn't count) and run the cell.`
- One global per cell; every answer pre-defined as `None`; every editable cell contains `# YOUR CODE BELOW`; name suffix `_exNM` (section N, exercise M); the check cell defines `exNM_ok`.
- Checks: `isinstance` + `round(x, 2) == LITERAL`; verify every literal in Python; never crash on a plausible wrong answer (guard `int()`/`float()`, `pd.isna`, `np.ndim`); degrade to "Not attempted" on `None`; `mo.callout` + `show_result(value)`.
- Hints on every new exercise: `Hint 1 (a nudge)` (no code) and `Hint 2 (the structure)` (`___` skeleton, never the paste-able answer).
- Tobi's bugs: logic/runtime only, always terminating, prompt states the RULE and the SYMPTOM, never the expected value.
- Story: sitcom voice, investor only cameos in labs 01–05, name-agnostic checks (never assert on the startup name).
- Data inline (string/dict) in labs 01–07; pandas labs (08–09) work on a copy for derived columns.
- Plotting labs: charts ungraded, graded names are the numbers; chart cells open with `plt.figure()` and end with `plt.gca()`.
- CP collision rule: a new exercise's expected value must differ from every graded value in the private repo's checkpoint for that span (grep `../Introduction-to-Python-checkpoints/checkpoints/cpN/` for the numbers; change the lab's inputs, never the CP).
- Do not touch `_repo-md/`, `_site/`, other labs, decks, or exercise notebooks. Do not commit in either repo.

## Per-lab table

| Lab | Session type | Core now | Add | Types (in this priority) | Chains? |
|---|---|---|---|---|---|
| nb_01_lab_founding | regular | 7 | +3 → 10 | story decision, Tobi's bug | no |
| nb_02_lab_curfew | regular (CP0 before lab) | 7 | +3 → 10 | story decision, Tobi's bug | no |
| nb_03_lab_functions | CP | 7 | +3 → 10 | story decision, Tobi's bug | no |
| nb_04_lab_menu | regular | 9 | +2 → 11 | story decision, Tobi's bug | no |
| nb_05_lab_checkout | CP | 7 | +3 → 10 | story decision, Tobi's bug | no |
| nb_06_lab_diligence | CP | 8 (7 + quiz) | +3 → 11 | story decision, Tobi's bug, chain | yes |
| nb_07_lab_metrics | regular | 9 (8 + quiz) | +2 → 11 | story decision, Tobi's bug, chain | yes |
| nb_08_lab_dataroom | CP | 10 (9 + quiz) | +1 → 11 | story decision, chain | yes |
| nb_09_lab_pitch | regular | 8 (7 + quiz) | +3 → 11 | story decision, Tobi's bug, chain | yes |

"Story decision": the computed value decides something in the episode and the success message says what happened. "Tobi's bug": a runnable cell with a logic bug and a symptom ("the investor says the number is too low"), the student fixes it in place. "Chain": the new exercise reuses a variable from the previous exercise (so a wrong earlier answer degrades gracefully: check for `None` upstream and say "finish N.M first").

## Per-lab task

**Files:** `notebooks/nb_XX_lab_*.py`; `../Introduction-to-Python-checkpoints/solutions/sol_XX_lab_*.py`.

- [ ] **Step 1: Read** the lab end to end, the matching solution notebook, and `../Introduction-to-Python-checkpoints/checkpoints/cpN/*.py` for the checkpoint(s) that test this session (CP1: I–II, CP2: III–IV, CP3: I–V, CP4: VI–VII, CP5: VIII–IX). Note the graded values.
- [ ] **Step 2: Place the new exercises.** Spread them over the sections (not all at the end). Append at the end of a section by default (no renumbering); insert earlier only if the story needs it, then renumber the section's later exercises and their `_exNM` suffixes, `exNM_ok` names, and the progress cell. The boss exercise (`_ex40`) may grow by one step but stays last-but-quiz.
- [ ] **Step 3: Author each exercise** as four cells copied from the lab's own pattern: instruction (`### Exercise N.M (core) — <title>` or `(core, fix the bug)`), your-code cell, check cell, hint accordion. Difficulty within 5–10 min each for the median student.
- [ ] **Step 4: Bookkeeping.** Header line `**Core exercises: N (+ …)**`; progress cell `_checks` list and its function signature; wrap-up "all N core exercises green?" wording; the top-of-lab overview if it lists sections.
- [ ] **Step 5: Solution notebook.** Add the same cells to `sol_XX_*.py` with the answer filled in (no `None`, no `# YOUR CODE BELOW`, no hint accordion), keeping its header/wrap-up style. Every check must be green when the solution runs.
- [ ] **Step 6: Verify.**
  - `uv run python helpers/validate_notebooks.py 'nb_XX_*.py'` → ok.
  - Solution: `cd ../Introduction-to-Python-checkpoints && uv run --project /Users/tobi/development/lectures/Introduction-to-Python python -c "import importlib.util as u; s=u.spec_from_file_location('s','solutions/sol_XX_lab_<topic>.py'); m=u.module_from_spec(s); s.loader.exec_module(m); m.app.run()"` → runs; then grep the solution for `Wrong —`/`Not attempted —` verdict strings being *selected* is not possible statically, so ALSO execute each new check cell body against the solution's answer in a scratch script and print the verdict.
  - Scratch simulation for each new check: right answer, two plausible wrong answers, `None` → Correct / Wrong / Not attempted, no exception.
  - Header count = number of entries in `_checks` = number of `(core` exercises incl. boss and quiz.
  - `grep -cP '[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}]'` over both files = 0.
  - Expected values differ from the checkpoint's graded values.

## Coordinator (after all labs)

- [ ] `uv run python helpers/validate_notebooks.py`; `uv run python helpers/check_quiz_balance.py` (labs' MCQs untouched, but run it).
- [ ] `quarto render` (full) → exports; spot-open one lab in a browser tab (threaded server) and walk one new exercise wrong → right.
- [ ] Report; no commit unless asked.
