# Plan 1 — Review Follow-ups (2026-07-09)

Captured from Tobias's hands-on review walkthrough (Phases 0–4) of the Session I
vertical slice. These are corrections/polish to what Plan 1 already built — the
larger content work stays in later plans (see §Deferred).

Legend: ⬜ to do · ✅ done · 💤 deferred to a later plan

**Update 2026-07-09:** batch **A–F implemented and committed** (defaults per §3:
result preview on all single-result exercises + the in-lecture receipt; reusable
`.exercise-slide` class; `_environment` added; 1.2 hardcoding accepted). Deferred
items (§4) and the enforcement *decision* (§3.5) remain open.

---

## 1. Pending changes (batch A–F)

| # | Change | Where | Status |
|---|--------|-------|--------|
| A | Remove the misleading "round to 2 decimals" from **Ex 2.2** + the **price-war bonus** (keep it only in Ex 1.2, where the float fuzz is real). Verified: `9.99-7.40` and `8.50*0.9` are already exact. | `notebooks/nb_01_lab_founding.py` | ✅ |
| B | Add a **"Your result" preview** so students see their own output (esp. receipts). Lock the pattern in the template first. | `notebooks/_template.py` + `nb_01` + `exercises/ex_01_*` | ✅ |
| C | `ex_01_c`: give `total = 13.80` directly instead of forcing `qty*price` (pure f-string task; matches lab Ex 3.1). | `notebooks/exercises/ex_01_c.py` | ✅ |
| D | Grader: extract `STUDENT_NAME` + `STUDENT_ID`, add as **CSV columns** so folder→CSV gives names + scores to aggregate. + a test. | `../Introduction-to-Python-checkpoints/grader/` | ✅ |
| E | *(opt)* `_environment` file so plain `quarto render` uses `.venv`; update `CLAUDE.md` render note. Fixes the `No module named 'yaml'` error. | repo root, `CLAUDE.md` | ✅ |
| F | QR "Your turn" slides → brand **`codeline` (#FFEEE2)** background to match section slides, via a reusable `.exercise-slide` SCSS class. | `styles.scss` + `lectures/lec_01_introduction.qmd` | ✅ |

## 2. Recommended order

1. **E** — quarto `_environment` fix *(5 min; unblocks smooth rendering for every later verification)*.
2. **B in `_template.py`** — establish the "Your result" pattern in the canonical skeleton *first*, so Plans 2–4 inherit it and we never retrofit.
3. **A + B + C on the Session I notebooks** — one coherent pass over `nb_01` + `ex_01_a/b/c` (apply the template pattern, fix rounding, fix `ex_01_c`), then one headless re-validation (placeholder→red, solved→green).
4. **F** — add the reusable `.exercise-slide` class + apply to `lec_01`'s QR slides *(durable; survives the later lecture rewrite)*.
5. **D** — grader name/ID CSV columns + test *(separate repo; its own unit)*.
6. **Verify + commit** to PR #1 (course repo) and a local commit in the checkpoints repo.

Rationale: template/pattern change (B) before it needs retrofitting; quick
unblocker (E) first; group by file/repo to minimise re-validation; touch only the
*scaffolding* of `lec_01`, not its content.

## 3. Open decisions (need Tobias)

1. Green-light batch A–F in the order above? (batch first vs lecture rewrite first)
2. **B scope:** "Your result" on **every** exercise, or **only string/receipt**? *(rec: lightweight echo on all, rich render for strings/receipts)*
3. **E:** add the `_environment` fix? *(rec: yes)*
4. **F:** reusable `.exercise-slide` class *(rec)* vs hardcoded `#FFEEE2`?
5. **Checkpoint enforcement:** baseline = submission-window + supervision + task-design. Add **deploy→take-down** for URL hygiene? Per-student **variants** deferred or now? *(rec: baseline + take-down in Plan 2; variants only if copying proves real)*
6. **Ex 1.2 hardcoding:** accept *(rec)* vs redesign to force variable use?
7. **Lecture rewrite:** own scoped task / early Plan 2 *(rec)* vs pull into Plan 1 now?

## 4. Deferred to later plans (do NOT do now)

- 💤 **Session I lecture content rewrite** (`lec_01`): trim to 3×20-min blocks, align to new syllabus, weave startup narrative, de-dry. Needs a brainstorm → early Plan 2.
- 💤 **`/humanizer` pass** over all student-facing copy — once, at the very end when all content exists.
- 💤 *(opt)* **`marimo check --fix`** across `notebooks/` — fold into the final formatting pass.
- 💤 **Plans 2–4** — rest of the course.

## 5. Reviewed and intentionally left as-is (no action)

- **Ex 1.1 raw `NameError`** on an unquoted value — can't be intercepted; reading the error is a legit Session-I skill.
- **Ex 3.2 solution visible** in the check cell — fine for an ungraded lab (checkpoints use hashing).
- **cp0 solved quickly** — expected; 6-pt dress rehearsal vs 12-pt / ~40-min real checkpoints.

## 6. Already committed this session (context)

- Persistence copy correction (reload-keeps / tab-close-loses / download-is-only-guarantee).
- Grader **blocker fix**: a submission's `print()` no longer corrupts JSON / aborts the batch (+2 tests).
- No-LLM-coauthor rule applied; PR #1 clean.

## 7. Environmental notes

- Render lectures with **`uv run quarto render …`** (plain `quarto` grabs a system Python without Jupyter).
- A **whole-site** render currently fails on the untracked **`Management-Science/`** dir (its own `python@3.14`) — unrelated; blocks full renders until moved out.
