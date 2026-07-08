# Introduction to Python — 2026 Course Overhaul Design

**Date:** 2026-07-08
**Status:** Approved design, pending implementation plan
**Course:** Programming with Python, KLU, Semester 3 2026, pass/fail, ~10–20 students, 13 sessions × 4 academic hours (~3h real time)

## 1. Why this overhaul

- GitHub Copilot's free student access is gone → the AI tooling story must be rebuilt (Mistral Free, own subscriptions, Zed).
- Students must master basics *before* leaning on AI — the new syllabus (`klu_syllabus.md`) makes Part I AI-free and assesses via 5 in-class checkpoints.
- Lectures should be hands-on, not passive: marimo notebooks in the browser, business-student motivation via a semester-long startup narrative (modeled on the Management-Science course's `nb_XX_YY` notebooks).
- Everything must be ready **before semester start**.

## 2. Decision summary

| Topic | Decision |
|---|---|
| Marimo scope | Tutorials + short in-lecture exercises; revealjs lectures stay |
| Hosting | Self-hosted WASM exports inside the Quarto site; optional molab links |
| Part III | Plain `.py` files in Zed — **no local marimo** |
| Narrative | One fixed campus **food-delivery startup**, student-named, mini-games woven in |
| Checkpoints | 5 marimo WASM notebooks, auto-graded via embedded tests, 12 pts each |
| Submission | Download `.py` → Moodle upload; grading script re-runs reference tests |
| Session shape | Interleaved 20-min lecture blocks + 10-min exercises + ~60-min lab block |
| CP timing | First ~40 min of the *following* session (sessions III, V, VI, VIII, X) |
| Missed CPs | No make-ups; point math absorbs one miss (88 pts still reachable) |
| CP privacy | Private companion repo + unlisted deploy URLs |
| Git | Taught in Session X (trimmed 60–90 min session from the other lecture) |
| Project submission | GitHub repo per pair + AI-disclosure note |
| Chatbot | Kept as-is; hint-only mode in Part I; system prompt updated |
| AI tools | Mistral Free (guaranteed), own ChatGPT/Claude/Mistral subs, Zed + Zed student program; Copilot removed everywhere |

## 3. Course architecture

### Session map (13 × ~3h)

| # | Session | Checkpoint at start |
|---|---|---|
| I | Welcome & Introduction — startup founding, syntax, variables, types | — |
| II | Control Structures (+ comprehension seeds, idiomatic loops) | — |
| III | Functions & Classes | **CP1** (sessions I–II) |
| IV | Data Structures (lists/tuples/sets/dicts, I/O, comprehensions) | — |
| V | Errors & Debugging | **CP2** (sessions III–IV) |
| VI | Modules & Packages, random | **CP3** (session V + Part I recap) |
| VII | NumPy | — |
| VIII | Pandas + AI craft (prompting, verifying output, hallucinated APIs, disclosure; heavy data-wrangling practice) | **CP4** (sessions VI–VII) |
| IX | Plotting + AI; homework: install uv + Zed | — |
| X | **Tooling, Git & Project Kickoff** — uv, Zed + AI setup, git (init/commit/push/clone/pull, GitHub), "a marimo notebook is a `.py` file" reveal, group formation, project choice | **CP5** (sessions VIII–IX) |
| XI | Project work under assistance | — |
| XII | Project finalization | — |
| XIII | Presentations & discussion | — |

Syllabus tweaks are limited to session titles/descriptions (allowed); the 3-part structure and lecture count stay.

### Regular session shape (~180 min)

```
0:00 Warm-up / recap quiz (10)          1:25 Lecture block 3 (20)
0:10 Lecture block 1 (20)               1:45 In-lecture exercise (10)
0:30 In-lecture exercise via QR (10)    1:55 Lab: tutorial notebook in class,
0:40 Lecture block 2 (20)                    instructor circulates, chatbot
1:00 Exercise (10) → BREAK (15)              gives hints (~60)
                                        2:55 Wrap-up, preview (5)
```

Checkpoint sessions: CP occupies the first ~40 min (generous, no rush, no retake mechanism); the rest of the session compresses to 2 lecture blocks + lab.

Lectures are scoped to 3 × 20-min blocks — existing decks must be trimmed/split accordingly.

## 4. Content design

### The startup arc

One fixed **campus food-delivery startup**. Students "found" it in Notebook 1.1 and name it via `mo.ui.text`; the name propagates reactively through the notebook (first marimo wow-moment). Mechanics, data, and all grading asserts are **name-agnostic**. Each notebook re-asks the name (WASM notebooks are standalone; one input cell, two seconds).

Arc across sessions: menu & pricing → order logic (control flow) → reusable order functions → customers & delivery zones (dicts/lists) → order validation & error handling → randomized demand simulation (modules/random) → delivery metrics (NumPy) → sales analysis on messy data (Pandas) → dashboards (plotting).

Mini-games woven in where mechanics fit (slightly meta is acceptable): price-guessing game (control flow), dice-based delivery simulator (random), text-based "order adventure" (dicts). Each framed as something the startup builds or plays.

### Notebooks

- Tutorial notebooks `nb_XX_YY_*.py` (marimo format), 2–3 per lecture, styled after Management-Science: narrative intro → teaching cells → exercises marked "YOUR CODE BELOW" → `assert`-based self-tests with encouraging messages.
- In-lecture exercises `ex_XX_[a-d].py`: single-concept, 5–10 min, reached via QR/short link from slides.
- Topic gaps folded in: comprehensions/idiomatic Python (sessions II & IV), extra data wrangling incl. messy CSVs and groupby (session VIII notebooks), AI craft (session VIII lecture + woven through IX), environment/tooling + git (session X).

### Student access: two buttons, honest labeling

Every tutorial page offers both, with the differences stated plainly:

- **"Open in browser" (recommended default):** runs entirely on your machine in the browser tab — after the page loads, no internet or account is needed. Your work usually resumes automatically when you reopen the page **on the same computer and browser** (stored in browser storage — lost if you clear browser data, use private mode, or switch machines). Download your `.py` anytime as a safety copy.
- **"Open in molab" (for cross-device certainty):** marimo's free cloud service (login with GitHub/Google). Your copy autosaves to your account and reopens on any device. Use this if you know you'll switch computers or want to be certain nothing is lost. Optional — nothing graded ever requires it.

Known one-way door, stated in course FAQ: a downloaded `.py` **cannot be uploaded back** into the browser editor; it is for submission, backup, and later local use in Part III.

In-lecture exercises: browser button only (ephemeral by design). Checkpoints: neither button — unlisted URL handed out in class.

## 5. Technical architecture

### Repo layout (public course repo)

```
notebooks/                    # marimo .py sources (source of truth)
  nb_XX_YY_<topic>.py
  exercises/ex_XX_<n>.py
helpers/export_marimo.sh      # marimo export html-wasm --mode edit per notebook
helpers/convert_qmd_to_md.py  # existing post-render (kept)
lectures/lec_XX_*.qmd         # revealjs, updated: startup examples, QR exercise slides, Copilot removed
tutorials/tut_XX_*.qmd        # slimmed to intro + the two buttons per notebook
general/ai-tools.qmd          # NEW: Mistral Free, Zed student program, own subs, disclosure rules
general/git-basics.qmd        # NEW: companion page to Session X git material
```

- Build: Quarto render + marimo WASM export step (locally and/or CI) placing exports under the published site (e.g. `_site/notebooks/<name>/`). One pipeline, one URL space, course branding.
- WASM notebooks are served as normal same-origin pages (required for localStorage-based resume; **no sandboxed iframes**).
- Pyodide covers numpy/pandas/matplotlib. No network calls in notebooks; datasets ship with the notebook (inline or `public/` files).
- Existing chatbot untouched except system-prompt update (hint-only in Part I, knows the startup arc).

### Private companion repo (`Introduction-to-Python-checkpoints`)

- 5 checkpoint notebooks + reference solutions + reference test suites.
- `grade_checkpoints.py`: takes a folder of Moodle-downloaded submissions, executes each against **reference tests** (embedded tests are for live feedback only — tampering doesn't matter), emits points CSV.
- Deploy script: exports a checkpoint to WASM and publishes it to an **unlisted URL** on the course site shortly before the session; QR shared in class.

## 6. Checkpoints & grading

- 5 checkpoints × 12 points = 60; pass needs 60/100 total (project + presentation = 40) plus 75% attendance.
- Internal structure per checkpoint: ~6 tasks × 2 points, **all-or-nothing per task**; live score cell shows the provisional result before submission.
- Task mix (per syllabus): write a function, trace code ("what does this print?"), fix a bug, MCQs (`mo.ui.radio`).
- Identity: name + student-ID cell at top; filename convention `cpN_<studentid>.py` enforced by instructions and checked by the grading script.
- Flow: unlisted URL at session start → ~40 supervised minutes → download `.py` → Moodle upload with deadline. Moodle provides identity + timestamps.
- AI-free enforcement (CP1–3): supervision + AI-resistant task design (tracing, debugging, twists on in-class material, tight timing). Social enforcement, not technical lockdown.
- CP4–5: AI explicitly allowed per syllabus.
- Missed checkpoints: no make-ups; only documented long absences get individual arrangements.

## 7. AI & tooling story

- **Part I (sessions I–V):** no AI. Course chatbot (hint-only) is the sanctioned helper.
- **Part II (VI–IX):** AI allowed and taught. Session VIII front half = AI craft. `general/ai-tools.qmd` documents: Mistral Free signup (guaranteed baseline for every student), using own ChatGPT/Claude/Mistral subscriptions, Zed as AI editor + **Zed student program** link, disclosure requirements.
- **Session X:** local environment together — uv, Zed (with chosen AI provider), git session (trimmed import from the other lecture: init/commit/push/clone/pull + GitHub; no branching/PRs).
- **Part III (X–XIII):** plain `.py` development in Zed. GitHub repo per pair = collaboration + submission channel (repo link + AI-disclosure note); commit history doubles as process evidence.
- All Copilot references removed from lectures, FAQ, and installation guides.

## 8. Retired / kept

- **Retired:** the 2 assignments (replaced by checkpoints), Copilot content, tutorials as homework-style `.qmd` exercise pages.
- **Kept:** revealjs lecture format (updated), Quarto site + publishing pipeline, chatbot, uv-based Python setup (moves to Session X), Management-Science course as untouched style reference.

## 9. Risks & early verification spikes

1. **WASM download UX** (submission backbone): verify "download as `.py`" works smoothly in edit-mode exports — spike in week 1 of implementation.
2. **localStorage resume**: verify work actually survives reload on the self-hosted export (undocumented behavior we describe to students) — same spike.
3. **Pyodide performance** on weak laptops with `mo.ui`-heavy notebooks — keep notebooks lean; test on a slow machine.
4. **Checkpoint gameability**: server-side re-run against reference tests is the referee; embedded tests are convenience only.
5. **molab dependency**: optional-only by design; if the free tier changes, students lose a convenience, not a course component.
6. **Session X density** (tooling + git + kickoff + CP5): dry-run the timing; fallback is moving CP5 to end of session IX.

## 10. Out of scope

- Chatbot re-engineering (context-aware hints) — possible later project.
- GitHub Classroom / CI autograding.
- Rewriting the Management-Science course.
- Any grading beyond pass/fail mechanics.

## 11. Success criteria

- A student with zero setup can do every graded activity through session IX with only a browser and Moodle access.
- All 5 checkpoints + grading script tested end-to-end (author → deploy → student flow → grade → CSV) before session I.
- Every lecture session has its in-lecture exercises and lab notebook ready before the semester starts.
- The AI-tools page gives every student at least one zero-cost working AI setup (Mistral Free + Zed) for Part II.
