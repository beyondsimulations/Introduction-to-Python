# Session length, lecture interactivity, and notebook onboarding — design

Date: 2026-09-09. Status: approved in conversation, awaiting written review.

## Problem

Session I (2026-09-08) ran 30–45 minutes short of the 3h + 15 min break
slot. The lecture finished in ~75 min (the three QR exercises took 3–5
min each instead of 10), and 39 of 40 students finished the lab in ~50
min. Separately, several students did not understand how the marimo lab
notebook works: which cells to edit, how to run a cell, what the check
verdicts mean, and what the menu / save / download do.

Owner preferences gathered while brainstorming:

- More hands-on inside the lecture: five QR exercises per regular session,
  each 5–10 min, plus more A/B/C/D predict-and-vote rounds ("those are
  great").
- Labs longer, but "good and interesting, not boring": story decisions and
  find-Tobi's-bug tasks; build-up chains only in the later, more advanced
  labs; no additional trace cells.
- Onboarding via a text page with a mock cell diagram (no screenshots, no
  video), plus a uniform marker in the notebooks and a short read-me cell.
- **No emojis anywhere.** Existing ones (~800 across decks, notebooks,
  FAQ, conventions) are stripped as part of this work.
- Do all sessions now, Session I included (CP0 and CP1 test it).

## Time budget (per session type)

| Part | Regular (I, II, IV, VII, IX) | CP day (III, V, VI, VIII) |
|---|---|---|
| Checkpoint | none (Session II: CP0, 15 min, before the lab) | 40 min |
| Warm-up A/B/C/D (3 Qs) | 10 min | none |
| Block content | ~55 min in 3 blocks | ~40 min in 2 blocks |
| QR exercises | 5 × ~8 min = 40 | 3 × ~8 min = 24 |
| Extra predict pairs | 3 × 3 min = 9 | 2 × 3 min = 6 |
| Lecture total | ~105 min | ~75 min after the CP |
| Lab, median student | ~75 min (Session II: ~60) | ~65 min |

Session X keeps its Plan-4 kickoff shape and is out of scope.

## Workstream A — notebook onboarding (do first)

### A1. Page `general/notebooks.qmd` — "How the notebook works"

Linked from the General navbar menu (next to Cheatsheet), from every
tutorial launcher (`tutorials/tut_0X_*.qmd`, one line under the buttons:
"New here? Read How the notebook works first."), from the FAQ entry "How do
I open and work on a lab notebook?", and from the Session I slide "How a
notebook works" (`lectures/lec_01_introduction.qmd`).

Content, in this order, plain text, no screenshots:

1. **What you are looking at.** A notebook is a page of cells. The
   sections mirror the lecture blocks. A CSS mock (three stacked boxes,
   built with fenced divs + a few lines of SCSS in the page) shows the
   three kinds of cell as they appear on screen:
   - *Read cell*: story, instructions, worked example. Code hidden. Do not
     edit.
   - *Your-code cell*: starts with `# YOUR CODE BELOW`. The only cells you
     edit. Replace every `None`.
   - *Check cell*: read-only, runs by itself, shows a verdict callout.
2. **Run a cell.** Click into it, `Cmd/Ctrl+Enter` (or the play button at
   the cell's right edge). Output appears below. A cell shows the value of
   its last line; an assignment shows nothing, so the check echoes "Your
   result".
3. **What updates by itself.** Change a your-code cell and run it; every
   cell that depends on it re-runs. You never run check cells by hand.
4. **The three verdicts.** Grey "Not attempted" (the variable is still
   `None`; a `print` alone does not count), red "Wrong" with a reason,
   green "Correct". The progress cell at the bottom counts core exercises.
5. **A red error pauses everything below.** Fix the cell with the red
   traceback and the checks come back. Read the last line of the
   traceback first.
6. **Hints.** Each exercise has two collapsed hints: a nudge, then a
   skeleton with blanks. Open them in order.
7. **Saving vs downloading.** The tab remembers you (reload is fine,
   closing the tab is not). `Cmd/Ctrl+S` saves inside the tab; menu →
   Download → Download Python code is the only copy that survives, and it
   is exactly how checkpoints are handed in. Save before download or the
   file is empty.
8. **Buttons you can ignore.** List the marimo edit-mode chrome students
   asked about and what not to click: delete cell, hide/show code toggle,
   add cell buttons, the app-view toggle, package/settings panels. Exact
   list verified against the deployed marimo version during
   implementation (`uv run marimo --version`; export one notebook locally
   and open it).
9. **Done for today.** Download, then close. Solutions appear on the
   tutorial page after the session.

### A2. Notebook markers and read-me cell

- Every editable answer cell in every lab and exercise notebook starts
  with the exact first line `# YOUR CODE BELOW` (optionally followed by a
  colon and a short instruction, as many already do). Cells that currently
  say `FIX TOBI'S FORM`, `TOBI'S CODE`, or have no marker (e.g.
  `ex_01_a.py`, `ex_03_b.py`) get the line added above their existing
  comment. This is what the page tells students to look for.
- Every lab notebook gets one read-me callout cell (`mo.callout`, kind
  "info") directly after the save callout:

  > **How this works:** run a cell with Cmd/Ctrl+Enter. Only edit the
  > cells that start with `# YOUR CODE BELOW`. The check under each
  > exercise updates by itself. A red error pauses everything below it —
  > fix that cell first. New here? Read *How the notebook works* (link).

  Exercise notebooks do not get it (10-minute sandboxes; the marker and
  the save callout are enough).
- `notebooks/_template.py` carries the read-me cell so future notebooks
  inherit it.

### A3. Emoji sweep

Mechanical, whole repo, in the same pass as A2 (touching all files
anyway):

| Current | Replacement |
|---|---|
| `❌ Exercise N.M:` | `Wrong — Exercise N.M:` |
| `✅ Exercise N.M:` | `Correct — Exercise N.M:` |
| `🔲 Exercise N.M: not attempted yet.` | `Not attempted — Exercise N.M:` |
| `💡 Hint 1 (a nudge)` / `💡 Hint 2 (the structure)` | `Hint 1 (a nudge)` / `Hint 2 (the structure)` |
| `💾 **Saving your work:**` | `**Saving your work:**` |
| `# 🔥 Warm-up` / `# 📋 Checkpoint N` slide titles | `# Warm-up` / `# Checkpoint N` |
| all other decorative emojis (🏆 📦 🧾 📊 …) | drop, keep the words |

Callout `kind` (success/warn/info) keeps carrying the state visually.
`helpers/check_quiz_balance.py` is checked for any emoji-keyed pattern
before the sweep (initial grep found none). The private repo's
`solutions/sol_0X_*.py` get the identical sweep. `docs/authoring-conventions.md`
and `general/faq.qmd` are updated to the new labels; the "no emojis" rule
is added to the conventions.

## Workstream B — lecture interactivity (per session, I–IX)

### B1. Five QR stops on regular decks, three on CP decks

Keep the block structure. Blocks 1 and 3 each get a **mid-block** QR stop
in addition to their end-of-block one; block 2 keeps its single stop. CP
decks (2 blocks) get one mid-block stop in the larger block. Resulting
counts: regular decks 3 → 5 (`ex_XX_a`–`_e`), CP decks 2 → 3 (`_a`–`_c`).
Letters follow slide order per the convention; existing notebooks are
renamed where a new stop lands before them (git mv, update
`helpers/make_qr.py`, re-run it, update the deck's QR image references).

The mid-block stop is placed after the block's first self-contained concept
(e.g. lec_01 block 1: after "Naming rules", before "Four basic types";
block 3: after "f-strings: the clean way", before formatting). Exact
placements are decided per deck in the implementation plan.

### B2. Core + stretch in every QR notebook (old and new)

Every `ex_XX_*.py` has the shape:

1. Title cell: "Quick exercise: <name> (5–10 min)" + one-paragraph
   sitcom setup + "First predict, then run."
2. Save callout (unchanged, minus emoji).
3. Core task: one your-code cell + one reactive check.
4. Stretch cell, markdown: "**Done? Then:** <second task>" — reuses the
   core task's variables, one your-code cell + its own check. The stretch
   is a genuine step up (a second rule, a bug in Tobi's version, an edge
   case), never a repeat.
5. Closing cell: "*Nothing to save. This was a sandbox.*"

Existing exercises keep their core task and gain a stretch. New exercises
are written in the same voice. Concept per exercise = the concept of the
slides just before it. Hint accordions only from `ex_06` on (existing
rule).

### B3. One extra predict pair per block

Each block gains one `## Predict: …` / `## Answer: …` pair in the existing
form (question slide with options a–c, hand vote, answer slide re-runs the
code). Placed at the misconception most likely in that block (e.g. `==`
vs `=`, `range` end exclusive, mutable aliasing, `.loc` vs boolean mask).
No spoiler comments on question slides. After each deck:
`uv run python helpers/check_quiz_balance.py` must pass, and
`../lecture-foundations/scripts/check_slide_overflow.py` on the deck.

### B4. Deck bookkeeping

- QR slides are retitled "Your turn — 5–10 minutes" (all decks, and the
  exact form in `docs/authoring-conventions.md`); the exercise title says
  the same.
- Session I: the "How a notebook works" slide links the new page and
  reads: run, edit only `# YOUR CODE BELOW` cells, checks update by
  themselves, download before leaving.
- Lab handoff slide: nothing to change beyond emoji removal.
- Cheatsheet: unchanged.

## Workstream C — labs longer (per session, I–IX)

- Each lab gains 3–4 core exercises, target 10–11 core; bonuses stay
  bonuses. New exercises are inserted into the section whose concept they
  practice (exercise numbers renumber within the section; `_exNM` suffixes
  follow). The header line "Core exercises: N (+ M bonus)" and the
  progress cell's count update.
- Exercise types, in this priority: (1) **story decision**: the value
  decides something in the episode and the check's success message says
  what happened; (2) **find Tobi's bug**: a working-looking cell with a
  logic/runtime bug and a symptom, never a syntax error, always
  terminating; (3) from Session VI on, **chains**: a new exercise reuses a
  variable from the previous one so the boss composes them.
- No new trace cells. Existing hint ladder (nudge, skeleton) for every
  new exercise. Checks follow the conventions: `isinstance`, rounded
  literals verified in Python, never crash on a plausible wrong answer,
  "Not attempted" on `None` with the unstick hint.
- Difficulty curve: the new exercises spread across the lab, not all at
  the end; the boss (`_ex40`) may grow by one step.
- Solutions: the matching `solutions/sol_0X_*.py` in the private repo gets
  the same exercises with answers filled in and checks green.
- Session I's lab is extended too (students redo it before CP0/CP1).
- WASM check: export and open each changed lab once
  (`uv run python helpers/export_marimo.py`, threaded local server per the
  conventions) and walk the new exercises with a wrong and a right answer.

## Out of scope

- Session X deck, checkpoint notebooks and reference tests (CP content
  values are unaffected; if a lab's expected answer collides with a CP
  value, the lab value changes, never the CP).
- Screenshots or video for onboarding.
- Any change to the 3-question warm-up format.
- Lecture content additions from `docs/side-quest-backlog.md`.

## Implementation order

1. Plan A (onboarding + markers + emoji sweep), one plan, whole repo +
   private solutions. Ship before Session II.
2. Plans B/C per session, Session I → IX, each plan covering that
   session's deck, QR notebooks, lab, and solution notebook together so
   the story stays coherent. Session II first after Plan A.

## Verification (every plan)

- `uv run python helpers/validate_notebooks.py`
- `uv run python helpers/check_quiz_balance.py` (after any MC change)
- `quarto render` (full; single-file renders prune `_repo-md/`)
- Slide overflow gate on touched decks.
- Grep for emoji code points returns nothing in `lectures/`, `tutorials/`,
  `notebooks/`, `general/`, `docs/authoring-conventions.md`.
