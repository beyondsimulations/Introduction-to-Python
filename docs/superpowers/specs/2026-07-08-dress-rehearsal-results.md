# Dress-Rehearsal Results — Plan 1

**Purpose:** record the end-to-end checkpoint journey (author → deploy → student
flow → grade → CSV) before Session I. This file has two halves: what is
**already proven** (done automatically, deterministically, in this session) and
what **still needs a human** (external accounts + physical hardware).

Status legend: ✅ done & verified · ⬜ pending (needs Tobias) · ⏳ blocked on an application

---

## A. Proven in this session (no browser account or second machine needed)

- ✅ **Download format = decorated marimo notebook.** Verified by driving the
  actual WASM export in a real browser: menu → Download → *Download Python code*
  yields the `@app.cell` / `app.run()` format (not a flat script). Details:
  `2026-07-08-spike-results.md`.
- ✅ **Browser persistence = URL-fragment, not auto-restore.** Reload keeps work;
  a fresh bare-URL visit starts clean. This corrected the student-facing copy
  (tut_01 + template wrap-up). Details in the spike-results file.
- ✅ **Grader pipeline** (`../Introduction-to-Python-checkpoints`): `uv run pytest`
  → 5/5 green. Handles decorated-notebook submissions (primary, via `app.run()`),
  flat-script submissions (fallback), syntax errors → `manual_review`, and
  infinite loops → subprocess timeout → `manual_review`.
- ✅ **cp0 end-to-end grade (local, deterministic).** A correctly-solved cp0
  download grades **6/6**; a syntax-error submission lands in `manual_review`
  with total 0. cp0's in-notebook hashed live checks also flip green with the
  correct answers (so students get real ✅ feedback without the answers leaking).
- ✅ **cp0 WASM export** succeeds (`marimo export html-wasm --mode edit`).
- ✅ **Deploy script** `deploy_checkpoint.sh <cpN>` (in the checkpoints repo):
  exports one checkpoint notebook to an unlisted `site/<cpN>-<random>/` path.
  (Fixes the plan's glob bug that would have also tried to export
  `reference_tests.py`.)

**What this means:** the grading machinery is done and trustworthy. The
remaining work is purely operational — hosting, and a real-hardware/real-Moodle
smoke test.

---

## B. Still needs Tobias (external accounts + physical hardware)

Do these in order before Session I. Record findings inline (replace the ⬜).

### 1. ⏳ GitHub Education Teacher benefit — apply early
- Apply: <https://github.com/education/teachers>. It unlocks free GitHub Team →
  Pages on **private** repos (public-but-unlisted site, hidden source).
- **Don't block on approval.** Cloudflare Pages free tier is the verified
  fallback and needs no approval.
- Status: ⬜ applied on ______ · granted on ______

### 2. ⬜ Deploy cp0 to the separate checkpoint host
- In `../Introduction-to-Python-checkpoints`: `./deploy_checkpoint.sh cp0`.
- Publish `site/` via **either** private-repo GitHub Pages (once #1 is granted)
  **or** `npx wrangler pages deploy site/<cp0-dir> --project-name itp-checkpoints`.
- **Never** deploy through the public course repo (its source is public).
- Unlisted URL: ______________________

### 3. ⬜ Take cp0 as a student on a weak/old laptop
- Open the unlisted URL on a NON-development machine (ideally an old/weak one).
- Solve all 3 tasks, watch the live score reach 6/6, then menu → Download →
  *Download Python code*.
- Time each step (WASM cold-load, per-task, download):
  - load: ____ s · solve: ____ min · download: ____ s
- Any friction / crashes (2 GB WASM memory cap!): ______________________

### 4. ⬜ Moodle round-trip
- Upload the downloaded `.py` to a Moodle sandbox assignment; then download it
  back from Moodle and grade it:
  `cd ../Introduction-to-Python-checkpoints && uv run python -m grader.grade checkpoints/cp0 <folder-from-moodle>`
- Expect total **6**. Result: ⬜ ____ / 6 · notes: ______________________

### 5. ⬜ molab login flow (for the FAQ) — spec §9 spike 3
- Open a tutorial page's *Open in molab* badge, sign in, save, reopen on another
  device. Screenshot the **login screen** for the FAQ (the method is
  undocumented; verify before publishing the button).
- Login method observed: ______________________
- Screenshot saved to: ______________________

---

## C. Friction / notes to feed into Plan 2

- (record anything that surprised you here — timings, weak-laptop behavior,
  molab quirks, Moodle upload constraints)
