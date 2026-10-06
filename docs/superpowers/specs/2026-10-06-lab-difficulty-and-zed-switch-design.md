# Lab difficulty and the Zed switch: design

Date: 2026-10-06. Status: decisions final (owner Q&A plus a red-team pass,
2026-10-06), awaiting written review. Applies to the **current run**.

## Problem

Session V (2026-10-06): students using AI finished the lab in ~30 min,
students working by hand in ~60 min. The slot is ~90 min. (Part I is
AI-free by policy, so the AI group was already outside the rules.)

An audit of labs 06-09 against the solution notebooks found that they are
lighter than lab 05, and that AI, allowed from Session VI, flattens them
further:

| Lab | Graded items | Est. with AI | Est. by hand |
|---|---|---|---|
| 05 checkout | 9 + MCQ + 2 bonus | ~30 (observed) | ~60 (observed) |
| 06 diligence | 11 + MCQ | 10-15 | 35-45 |
| 07 metrics | 11 + MCQ | ~15 | 40-50 |
| 08 dataroom | 11 + MCQ | 15-20 | 50-60 |
| 09 pitch | 10 + MCQ + 6 charts | 20-25 | 60-70 |

Causes:

- Every graded answer in labs 06-08 is a single line.
- The `# YOUR CODE BELOW` lines and prompts name the method, often the
  whole expression ("statistics.median of `ratings`", "via
  int(orders_week.size)", "`days = np.arange(1, 15)`"). This breaks the
  target-not-method rule in `docs/authoring-conventions.md`.
- Each task is self-contained and fully specified, so a pasted prompt
  solves it first try.
- Labs 06-09 have no stretch tier.
- The AI-supervision theme (lab 08 story, lab 09 lying charts) is not
  graded. In lab 08 exercise 2.3 the `KeyError` names the wrong column
  itself, and lab 09's chart critique is ungraded.

The 2025 run had open-ended builds done locally (own `calculator.py`
module, scrambled-word game, password checker, NASA data with `melt`).
Some of that needs files and a local Python, which the browser blocks.

## Schedule

Weekly on Tuesdays, with **20 Oct off**:

| Session | Date | Checkpoint | Lab |
|---|---|---|---|
| VI | 13 Oct | CP3 | lab 06, browser (reworked) |
| (break) | 20 Oct | | |
| VII | 27 Oct | | install (exit ticket), then lab 07, browser (reworked) |
| VIII | 3 Nov | CP4 (VI-VII) | lab 08, script in Zed |
| IX | 10 Nov | | lab 09, script in Zed (long) |
| X | 17 Nov | CP5 (VIII-IX) | project kickoff, git |

## Decisions

1. **Middle path.** Sessions VI-VII stay in the browser (marimo) with
   bigger, more open tasks. From Session VIII, labs run locally in Zed
   with the Mistral Vibe agent.
2. **Labs VIII+ are plain `.py` scripts**, split into cells by `# %%`
   lines, not marimo notebooks (the Lecture-Foundations Julia pattern,
   `standard/tooling.md` §3, carried over to Python).
3. **One run path:** `uv run python lab_08_dataroom.py` in Zed's terminal,
   inside one flat `python-labs` folder holding the scripts and CSVs.
   Zed's REPL (`# %%` cells) is mentioned as optional, not supported.
4. **Labs are ungraded.** Students show their printed numbers and chart
   files in class and may leave once they have. Only checkpoints are
   graded. No syllabus change.
5. **Session VII: install first, strict exit ticket.** After the lecture,
   everyone installs uv, Zed and Mistral Vibe in class; nobody leaves
   before the check passes. Then lab 07. Exception: if you confirm a
   laptop cannot run it (hardware, locked down), the student leaves with
   a named partner and pairs on the partner's laptop in VIII-IX.
6. **Data is a downloaded CSV next to the script**, read with a relative
   path (`pd.read_csv("orders_messy.csv")`). Background: the course host
   answers pandas' default user agent with 403 (Cloudflare blocks
   `Python-urllib`; a browser user agent gets 200, reproduced
   2026-10-06), so loading by URL from the course site is out.
7. **Downloads** use the foundations mechanism: a `code-links` entry in
   the front matter of each tutorial page, plus `project.resources` in
   `_quarto.yml`. Never `format-links`: Quarto silently drops formats it
   doesn't know.
8. **Self-checks check shape and plausibility only, never the expected
   value.** A literal in an `assert` hands the agent the answer to
   hard-code.
9. **Messy data, symptom only.** The lab CSV has a few quirks; prompts
   name the symptom ("the investor says Hafen is missing orders"),
   students find the cause and may use the agent for the fix. No new
   lec_08 content.
10. **Bug-fix lines are authored, static "Tobi's code"**, never "ask the
    agent live". The hallucination beat in lec_08 stays on the slides.
11. **The in-lecture QR exercises in VIII-IX stay in the browser.**
    Concepts are browser work; labs are local work.
12. **nb_08 and nb_09 are retired**: moved out of `notebooks/`, no longer
    exported. Pairing is the fallback, not a browser version.
13. **Vibe setup:** switch `general/ai-tools.qmd` to Zed's agent registry
    entry for Mistral Vibe if it works with the free key (verify first).
    Otherwise keep the `settings.json` block and add the Windows PATH fix
    (`uv tool update-shell`, then restart Zed).
14. **The "leaving the browser" reveal moves to VII/VIII.** lec_10's cold
    open refocuses on the deal closing and the project handover.
15. **No fallback plan for lab 08**: the script lab will be ready by
    3 Nov.
16. **The AI throughline is unchanged.** VIII keeps the hallucination beat;
    the agent arrives there as a tool, with one line saying "how it
    works: Session X". X keeps the "model in a loop" explanation.

## Time targets

Targets come from the 2026-09-09 session-length spec.

| Lab | Session type | In class | Median with AI |
|---|---|---|---|
| 06 | CP day | ~65 min by hand | 45+ min |
| 07 | regular, install first | install ~30-45 min, then lab for the rest; unfinished parts at home before CP4 | 40+ min lab |
| 08 | CP day | ~65 min by hand | 45+ min |
| 09 | regular | ~90 min by hand | 60+ min |

## Workstream A: browser labs 06-07

A1. **Strip the method from every `# YOUR CODE BELOW` line and every
prompt.** Comments name the target and its constraints only. Methods
stay in the lecture and in the two hint accordions.

A2. **Fewer, bigger core tasks in both labs** (around 8 graded items,
down from 11):

- Functions checked against several inputs, the way lab 05 and the
  checkpoints already do it (lab 06: `project_week(seed, days, low,
  high)` checked with several seeds; lab 07: `risk_report(times, limit)`
  checked with several arrays, including one with no critical run).
- Multi-step chains where a later step needs an earlier result (lab 06:
  simulate 200 seeded weeks, count the weeks that need more than one van
  trip; lab 07: each zone's share of the week, then a ranking).
- Stay inside what lec_06 and lec_07 teach. Check every candidate task
  against the deck before writing it.

A3. **A stretch tier per lab**: 2-3 ungraded "Bonus (not required)"
tasks, given as a short brief instead of steps.

A4. **Checkpoint 4 alignment.** `lec_08:33` tells students everything in
CP4 was rehearsed in the labs. CP4 (`checkpoints/cp4/reference_tests.py`)
needs:

| CP4 task | Skill | Must stay rehearsed in |
|---|---|---|
| t1 | `crates_t1(n, per)` with round-up, probed with 3 inputs | lab 06 (the new multi-input function covers it) |
| t2 | count over a limit + mean of those values | lab 07 (today: 2.1 count, 2.4 masked mean) |
| t3 | fix a wrong `axis` | lab 07 (today: 2.3) |
| t4 | seeded `randint` list | lab 06 (today: 2.1) |
| t5, t6 | MCQ | check the content of both against the new labs |

Since lab 07 is squeezed by the install, its CP4 core comes first in the
lab, and the bonus tier last.

## Workstream B: the tooling switch in VII

B1. **Announce in VI (13 Oct):** bring a laptop you can install software
on, plus charger, to VII on 27 Oct; create the Mistral key in VI as
already planned (`ai-tools.qmd` schedule).

B2. **Session VII install block** (after the lecture, before lab 07):
- Steps from `general/uv.qmd` and `general/ai-tools.qmd`; no new how-to
  page. Fix both pages first: the Windows PATH step for `vibe-acp`, the
  registry path if it is verified (decision 13), and the Session VII
  timing.
- A course folder: `uv init --no-package python-labs`, then
  `uv add pandas matplotlib`. This moves from `lec_10` "Make it a Python
  project".
- **The check**: in Zed's terminal, inside `python-labs`,
  `uv run python -c "import pandas, matplotlib; print('ready')"` prints
  `ready`, and Mistral Vibe answers a question in the agent panel.
- Slides: a new "Your toolchain" block at the `lec_07` lab handoff,
  moved from `lec_10` "Check your install". This is now the
  "leaving the browser" moment (decision 14).
- `nb_07_lab_metrics.py`: the read-me notes that the install comes
  first; the wrap-up cell says what is left for home before CP4.
- Known traps to cover on the slide or the page: Zed needs DirectX 11 on
  Windows; `vibe-acp` not on PATH on Windows; wifi load with 40 parallel
  downloads (test the room if possible).

B3. **Session VIII:** one agent slide at the lab handoff: open the panel,
ask, read the diff before accepting. This moves from the first half of
`lec_10` "Connect your AI". The "model in a loop" slide stays in X.

B4. **git + `gh` stays homework before Session X.** The `lec_09` slide
"Before Session X" shrinks to those two. `lec_10` Toolchain keeps the
git/`gh` check and the repo's own `uv init`. It drops the uv/Zed/Vibe
check and the "open a lab in Zed" moment. The freed time goes to git
and the project kickoff.

B5. **`general/ai-tools.qmd`:**
- Schedule table: "Session VII (in class): uv, Zed, Mistral Vibe" and
  "Before Session X: git + gh".
- Section heading "AI inside Zed: Mistral Vibe (before Session X)" and
  its line "Nothing in this section is needed before Session IX" move to
  Session VII.
- Policy wording: from VIII the agent works inside the editor; Part II
  stays "allowed and taught".

## Workstream C: script labs 08-09

C1. **Format and location.**
- `labs/lab_08_dataroom.py`, `labs/lab_09_pitch.py`,
  `labs/orders_messy.csv`.
- `_quarto.yml` gets `project.resources: - labs/`. Everything under
  `labs/` is published, so solution scripts must not be there before
  their session (same rule as `notebooks/solutions/`).
- Move `notebooks/nb_08_*.py` and `nb_09_*.py` out (decision 12).
  `export_marimo.py` globs `nb_*.py`, so they stop being exported.
- `notebooks/public/orders.csv`: no exercise loads it (only nb_08/09
  did), but `lec_08:277` shows it in a code example. Keep it.

C2. **Script conventions** (a new "Script labs (Session VIII+)" section in
`docs/authoring-conventions.md`):
- A header comment: download both files into `python-labs`, then
  `uv run python lab_08_dataroom.py` in Zed's terminal.
- `# %%` cells, with story and prompts as comment blocks.
- `# YOUR CODE BELOW` (target, not method), and answers pre-set to
  `None`.
- Each exercise ends in `assert` lines on type, shape and plausibility
  (four zones, a share between 0 and 100, no missing values left), with
  a message saying what is wrong. A `None` answer fails with "not
  attempted yet". The script stops at the first failing assert, so
  students work top to bottom.
- Charts: `plt.savefig("<name>.png")`, then `plt.close()`; never
  `plt.show()`.
- The last cell prints a "Show this in class" summary: the numbers (and
  the chart file names) to show before leaving.

C3. **Data.** `orders_messy.csv`, a copy of the orders with 2-3 quirks
where naive code runs but gives the wrong number: a trailing space
("Hafen "), duplicate rows, and missing values in one numeric column.
Keep the quirks to what an agent can help fix once the student has
spotted the problem.

C4. **Lab 08 (normal CP-day length).** A first look at the messy data,
then 6-7 brief-style tasks:
- Count, filter, revenue per zone, a derived column.
- Two bug-fix tasks with static "Tobi's code" (decision 10) that runs
  but is wrong because of the data.

Show in class: the per-zone revenue and the cleaned row count.

C5. **Lab 09 (long).** From the messy CSV to the pitch:
- Clean the data, then save a daily-revenue line chart, a per-zone bar
  chart and a histogram as PNGs.
- Fix Tobi's lying charts: a truncated axis, then a cherry-picked
  window.
- A printed pitch summary.
- Stretch: answer your own question about the data with a chart.
- Wrap-up: a 2-minute drill of the marimo Save + Download motion on a
  browser QR exercise, because CP5 is still a marimo download.

Show in class: the PNGs and the summary.

C6. **Tutorial pages `tut_08`/`tut_09`.**
- Replace the molab/WASM buttons, the save/download warning and the
  boot callouts with `code-links` for the script and the CSV.
- Add the run steps inline, in three lines (no separate how-to page).

C7. **Solutions** (private repo). `sol_08`/`sol_09` become scripts,
published after the session as downloads via `code-links`, not as a
run-mode WASM export. They cannot go under `notebooks/solutions/`
(`helpers/validate_notebooks.py:15` treats that as marimo). Gate: every
solution script runs end to end with all asserts passing under
`uv run python`.

C8. **Checkpoint 5 alignment.** CP5 uses an inline 10-row DataFrame
(`cp5_board_review.py:122-131`), so the messy CSV does not affect it.
Its skills stay covered if lab 08 keeps filter + sum, groupby to a dict,
a count and a fix of an AI-written line, and lab 09 keeps the axis
story.

## Ripple sweep (references that go stale)

- `lec_06:107` "long before Session X"; add the VII announcement (B1).
- `lec_08:277` (`read_csv("public/orders.csv")` "in the browser"),
  `lec_08:444` "in your browser as always".
- `lec_09:583-611` "Before Session X" slide (B4).
- `lec_10:38-60` cold open "The handover note" (decision 14),
  `lec_10:185-197` "Session IX homework" and the toolchain section (B4).
- `general/cheatsheet.qmd:371` "(also in the browser)".
- `general/git-basics.qmd:10,13`, `general/faq.qmd:27` ("working
  locally in Part III") and `:39` (labs open in the browser),
  `general/syllabus.qmd:55` ("Session IX pre-work").
- `CLAUDE.md`: `labs/` in the project structure and file naming
  (`labs/lab_XX_<topic>.py`), and where Zed arrives in the throughline.
- `helpers/convert_qmd_to_md.py` mirrors only `notebooks/*.py`; `labs/`
  does not reach `_repo-md`. Fine as is; noted so nobody "fixes" it by
  accident.
- Lecture-Foundations `standard/tooling.md` §2 points at
  `lec_10:186-340` for the browser-to-local moment; update the pointer
  (that change belongs in the foundations repo).
- Run `helpers/check_quiz_balance.py` after any MC changes.

## To verify

- Zed's agent registry entry for Mistral Vibe with the free key, on macOS
  and Windows (decision 13).
- Mistral free tier: phone verification at sign-up, and rate limits under
  an agent loop.
- `uv run python` from Zed's terminal on Windows inside `python-labs`
  (the venv is picked up without activation).

## Deadlines

- **13 Oct (VI):** lab 06 reworked (A1-A3), `sol_06`, quiz balance,
  headless boot; the B1 announcement; `lec_06:107`.
- **27 Oct (VII):** decision 13 verified; `ai-tools.qmd` + `uv.qmd`
  fixed (B5, B2); `lec_07` install block; lab 07 reworked + `sol_07`;
  CP4 alignment (A4) checked.
- **3 Nov (VIII):** `labs/lab_08` + CSV + `sol_08`; `tut_08` code-links;
  `_quarto.yml` resources; `lec_08` agent slide and `lec_08` ripples;
  the conventions section (C2); nb_08 retired.
- **10 Nov (IX):** `labs/lab_09` + `sol_09`; `tut_09`; `lec_09` slide;
  nb_09 retired.
- **17 Nov (X):** `lec_10` cold open and toolchain rewrite; the rest of
  the ripple sweep, `CLAUDE.md`, the foundations pointer.
