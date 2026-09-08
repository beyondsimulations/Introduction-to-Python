# Authoring conventions (Plans 2–4 copy these — do not improvise)

## Repos & publishing
- Public repo: lectures, tutorials (launcher pages), lab + exercise notebooks.
- Private repo (`../Introduction-to-Python-checkpoints`): checkpoint notebooks,
  reference tests, ALL solution notebooks (`solutions/sol_XX_*.py`).
- Commit rule: never add AI-attribution lines (Co-Authored-By etc.) in either repo.
- The convert script only rebuilds `_repo-md/` on a full render (guarded by
  `QUARTO_PROJECT_RENDER_ALL`), so single-file renders leave `_repo-md/` alone.

## Notebooks (see notebooks/_template.py for the skeleton)
- One global per cell; `+=`/`*=` count as definitions; `_name` is cell-private.
- Every exercise pre-defines its answer: `fee_ex11 = None  # YOUR CODE BELOW`.
- Suffix naming: `<meaning>_exNM` (section N, exercise M); boss = `_ex40`,
  MCQ = `answer_ex50`, bonuses = `_ex60`+. Classes keep their natural name
  (`Order`), no suffix.
- Checks: `isinstance` + `round(x, 2) == LITERAL` for numbers; degrade to
  "🔲 not attempted" on None; `mo.callout` + `show_result(value)`.
- Check cells must NEVER crash on a plausible wrong answer (a crash pauses the
  progress cell and hides the ✅). Guard/try-except every coercion: `int()`/
  `float()` may hit an array/Series/string, not a scalar; use `pd.isna(x)` for a
  NaN from an empty filter (`nan != nan`, so `== LITERAL` silently fails); use
  `np.ndim(x)` to catch a still-an-array branch. Simulate the wrong paths in
  Python before committing (Plan 3, Part II data/NumPy labs).
- Float safety: expected values must survive `round(_, 2)` exactly; avoid
  `.xx5` boundaries (32.775 → 32.77!). Verify every literal in Python first.
- Hints: Hint 1 = nudge (no code); Hint 2 = skeleton with `___` blanks — never
  the paste-able answer. Full answers live in the solution notebook only.
- Tobi's bugs: logic/runtime only (never syntax errors), and always terminating
  (never a possible infinite loop — it freezes the WASM tab).
- An erroring answer cell pauses its check cell AND the progress cell (reactive
  dependency). Labs with easy-to-crash exercises (dict lookups, indexing) must
  include the "red error pauses everything below — fix it and it comes back"
  teach line.
- Trace exercises: `mo.ui.radio` + reveal, labeled "(trace — predict first)",
  ungraded (not counted in the progress cell).
- Progress cell counts core exercises only; wrap-up ritual cell closes every lab.
- Story: sitcom in notebooks, investor only cameos until Part II, name-agnostic
  checks (never assert on the startup name).
- Data in notebooks: inline string/dict data until Part III; `public/` files
  revisit with pandas in Session VIII. (Spike 2026-07-10: a `public/` file IS
  copied on WASM export and reachable, but `mo.notebook_location()` yields a
  `URLPath` — beginner-natural `open(path)` fails with `FileNotFoundError` and
  `path.read_text()` fails with `AttributeError`; only
  `urllib.request.urlopen(str(path))` works, which is not Session-IV-appropriate.
  So ship file-like data as an inline multi-line string until pandas.)
- Loading `public/*.csv` with pandas (Session VIII+, Spike 2026-07-11):
  `pd.read_csv` is NOT `open()` — it has its own URL-aware I/O layer, so the
  same one-liner works unchanged in both local runs (plain filesystem path)
  and exported WASM (`URLPath` → `http://` URL, fetched via pyodide-http). No
  `try`/`except` fallback needed; execution-verified in a real browser and
  locally. Canonical loader cell (assumes an earlier cell does
  `import pandas as pd` and returns `(pd,)` — copy that too, not just this cell):
  ```python
  @app.cell(hide_code=True)
  def _(mo, pd):
      _loc = mo.notebook_location() / "public" / "orders.csv"
      orders = pd.read_csv(str(_loc))
      return (orders,)
  ```
  (One-off flake observed once: pyodide's package CDN fetch for a pandas
  dependency can transiently fail over flaky wifi, surfacing as `import
  pandas` raising `ImportError`; a page reload fixed it. Worth a one-line
  "if pandas fails to import, reload the page" note in Session VIII lab
  instructions, not a loader-pattern change.)
- Pandas-era labs work on a COPY for any derived column (`work = orders.copy()`;
  then `work["per_item"] = …`) — never mutate the shared `orders` global, or a
  later cell reading `orders` sees the mutation and reactive re-runs diverge.

## MC questions — no answer-revealing cues (fleet directive 2026-07-20)
Applies to every MC format in this repo: lecture warm-up/predict option rows
(`a\) …   b) …   c) …` + `**x)` reveal), lab MCQ cells (`- **a)** …` +
`== "x"` check), and `mo.ui.radio` traces. Checker:
`uv run python helpers/check_quiz_balance.py` (exit 1 gates; run it after
touching any question; `--stats` for the per-question table).
- Length: within a question, longest option ≤ 1.8x shortest (visible text).
  Balance by ENRICHING distractors with specific detail — never by
  vague-ifying the correct answer. After enriching a distractor, re-verify it
  is still unambiguously wrong (RUN the code when wrongness depends on
  runtime behavior). Pure code-literal/output options are exempt (their
  length is forced by the program), but the checker must agree they are.
- Position: neither slides nor `mo.ui.radio` shuffle options, so SOURCE order
  is the only defense — do not default the correct answer to one letter
  (pre-sweep it was "b" in 41 of 56). Vary it; the checker prints the
  distribution.
- Absolutes: keep always/never/only/every-style terms at similar rates in
  wrong and correct options; soften blatant absolute distractors.
- Correctness never changes in a balance pass: reorder + update the reveal
  letter / `== "x"` letter / letter prefixes inside radio option strings
  together, and keep feedback wording in sync.

## In-lecture exercises (ex_XX_<letter>.py)
- **Letter = slide order** (Fable #10): `ex_XX_a` belongs to lecture block 1,
  `_b` to block 2, `_c` to block 3. CP sessions have 2 blocks → letters a–b only.
- One concept, one screen, 5–10 min, one exercise + one reactive check,
  closing cell: "*Nothing to save — this was a sandbox.*"
- From `ex_06` onward in-lecture exercises carry hint accordions (Hint 1 = nudge,
  Hint 2 = `___` skeleton), matching the lab hint ladder — the `ex_01`–`ex_05`
  family predates this and stays hint-free.

## Lecture decks (revealjs)
Regular session skeleton:
1. Title slide (Fall 2026) → 2. Cold open (1 slide, episode framing, restrained)
3. 🔥 Warm-up (3 recap questions; see below) → 4. Block 1 (≤20 min)
5. QR exercise a → 6. Block 2 → 7. QR b → [break] → 8. Block 3 → 9. QR c
10. Lab handoff (tutorial URL) → 11. Wrap-up: 3 takeaways + next-episode teaser
→ [break] → lab in class (unfinished parts at home).
Session II: 📋 Checkpoint 0 (dress rehearsal, 15 min, ungraded) sits right before the lab handoff.
CP sessions (III, V, VI, VIII, X): title → 📋 checkpoint slide (procedure) →
cold open → Block 1 → QR a → Block 2 → QR b → lab handoff → wrap-up.
No warm-up on CP days (the checkpoint is the warm-up).
Exception — Session X follows the Plan-4 kickoff shape instead (CP5 opener →
episode → project kickoff → toolchain → git → send-off; no QR exercises or lab
handoff by design, and no tut_10/nb_10 — see
docs/superpowers/specs/2026-07-12-part3-plan4-design.md).

### Warm-up pattern (oral + vote)
One `# 🔥 Warm-up {.exercise-slide}` section, then per question a `##` slide
(question + options a–c) and a `##` answer slide (answer + one-line why).
Everyone commits by hand vote BEFORE the reveal — predict-first, zero infra.
Warm-up answer slides are prose-only (no live execution) — deliberate: oral
pace, three questions in ~10 min. In-block predict pairs DO re-run the code
executable on the answer slide. Never annotate a question slide's code with
spoiler comments — the misconception must survive until the reveal.
Layout nicety (optional): short symbol lists may pair two items per bullet
joined by a middle dot ("`<` less than · `>` greater than").
A predict pair whose reveal is meant to CRASH (e.g. lec_08's `df.summarize()`
hallucination) must mark that cell `#| error: true` so Quarto captures the
traceback into the slide — a bare crashing cell aborts the whole render.

### QR exercise slide (exact form)
    # Your turn — 10 minutes {.exercise-slide}
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
- CP task values must DIFFER from lab/exercise values (same skill, new numbers) —
  AND the expected ANSWER must differ too (a fresh list that still sums to the
  lab's answer defeats the purpose; lab recall must never score points).
- Prompts state the RULE and the SYMPTOM, never the expected value or the bug's
  location ("the investor says the number is too low", not "should be 4" /
  "wrong comparison"). Grading is value-only — a stated answer is a free answer.
- Live checks and reference tests must apply IDENTICAL comparison leniency (the
  hash helper normalizes strip+lower — reference tests mirror it).
- MCQ/trace answers get a neutral "recorded" acknowledgment, never a live ✅/❌
  (a 4-letter space is enumerable).
- Hash literals are per-task salted (`expected_hash(answer, task="cpN.tM")`) so
  equal answers never share a literal.
- expr keys are task-prefixed and unique (enforced by `load_tasks`).
- CP5 (the Part-II finale) is deliberately all names-based — no `exprs` probe
  task — a confidence landing before the project phase; from the AI-allowed era
  (Session VI+), AI-computed graded VALUES are sanctioned at CP4/CP5 by policy
  (understanding is still required via fix/apply tasks, not trace tasks).

## Part II additions (Plan 3)
- Plotting artifacts are UNGRADED: the graded names are the NUMBERS behind a
  chart, never the figure. Every chart cell opens with `plt.figure()` (first
  occurrence commented `# fresh figure`) and ends with `plt.gca()` so marimo
  renders it inline; never call `plt.show()` (no-op in WASM, muddies the cell).
- WASM spot-check harness: serve exports with a THREADED local server
  (`ThreadingHTTPServer`) — a single-threaded `python -m http.server` deadlocks
  pyodide-http's synchronous `fetch`, so pandas labs that load `public/*.csv`
  hang forever. Pandas-heavy labs also may not auto-run every cell on cold boot;
  a one-time "Run all" (Cmd/Ctrl+Shift+R) drives them (see the dress-rehearsal
  spec for the deployed-host follow-up).
