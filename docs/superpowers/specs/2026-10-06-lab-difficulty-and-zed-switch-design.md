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
   laptop cannot run it (hardware, locked down, only an iPad), the
   student sets up a GitHub codespace instead and shows `ready` in its
   terminal (decision 19; pairing was the first plan).
6. **Data is a downloaded CSV next to the script**, read with a relative
   path (`pd.read_csv("orders_messy.csv")`). Background: the course host
   answers pandas' default user agent with 403 (Cloudflare blocks
   `Python-urllib`; a browser user agent gets 200, reproduced
   2026-10-06), so loading by URL from the course site is out.
7. **Downloads** use the foundations mechanism: a `code-links` entry in
   the front matter of each tutorial page, plus `project.resources` in
   `_quarto.yml`. Never `format-links`: Quarto silently drops formats it
   doesn't know. **As built (2026-10-09):** `tut_08` uses two download
   buttons in the page body with a `download` attribute, not `code-links`.
   Chromium opens a `.py` link as text in the tab (served as
   `text/x-python` or `text/plain`), and a `code-links` entry cannot carry
   the attribute. With the attribute both files download.
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
    exported. A GitHub codespace is the fallback (decision 19), not a
    browser version and no longer pairing.
13. **Vibe setup:** Mistral Vibe is installed from Zed's agent registry
    (`zed: acp registry`), not by editing `settings.json`. Tobias confirmed
    on 2026-10-09 that this works with a free account, and
    `general/ai-tools.qmd` now says so. The page also carries the Windows
    PATH fix (`uv tool update-shell`, then reopen the terminal).
14. **The "leaving the browser" reveal moves to VII/VIII.** lec_10's cold
    open refocuses on the deal closing and the project handover.
15. **No fallback plan for lab 08**: the script lab will be ready by
    3 Nov.
16. **The AI throughline is unchanged.** VIII keeps the hallucination beat;
    the agent arrives there as a tool, with one line saying "how it
    works: Session X". X keeps the "model in a loop" explanation.
17. **No hint accordions in labs 06-07** (owner, 2026-10-08). The notebook
    keeps its usual structure; worked examples, slides and the AI assistant
    replace the hints. Recorded in `docs/authoring-conventions.md`.

18. **One unannounced problem per script lab** (owner, 2026-10-09). It
    sits in the data, never in the task text: only Tobi and his export may
    be wrong, the lab's own instructions never are. No task names it and
    no check catches it, but tools from the lecture show it. Lab 08: a
    test order (id 9999, dish `TEST`, 99 euros, 0 minutes) that makes
    Nord the top zone instead of Sued. The handoff slide and the tutorial
    page say that one problem is not mentioned anywhere; the script does
    not, so the student knows something the agent does not. It is caught
    at the desk, against the key in the solution script's header. A wrong
    premise in a brief is held back for lab 09. Lab 09 as built has both:
    Tobi's two slides read the raw `orders` (the data problem, in his
    static code), and his claim "Slow deliveries cost us stars" is quoted
    in the Task 7 brief although the data does not support it (the wrong
    premise). The lab's own voice asserts neither.

19. **Fallback without Zed: a GitHub codespace** (owner, 2026-10-09).
    The student starts GitHub's **Blank** template at
    `github.com/codespaces`, follows the uv guide's macOS/Linux lines in
    its terminal (`uv init --no-package python-labs`,
    `uv add pandas matplotlib`), downloads the two lab files with
    `curl -O` from the course site (it answers curl with 200, unlike
    `Python-urllib`) and runs the same `uv run python` command. No
    starter repo: the manual steps are the ones everybody does in VII.
    Tobias tested it on an iPad on 2026-10-09. A codespace has no Zed and
    no agent panel, so these students use the chatbot tab; `vibe` in the
    codespace terminal is not verified. Free accounts get 120 core hours
    a month. The steps live in a collapsed callout on `tut_08` and in the
    "Stuck?" callout of the `lec_07` check slide; `tut_09` gets the same
    callout.

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

A3b. **Lab 06 as built (2026-10-08):** 8 coded core tasks + quiz + trace + 3
bonuses. 1.1 `crates_needed_ex11` (4 probes), 1.2 `rating_report_ex12` (dict,
import by name), 1.3 fix the bug (mean vs median), 2.1 `simulate_days_ex21`
(3 probes), 2.2 fix the bug (seed in the loop), 2.3 `weekend_order_ex23` (shuffle a
tuple roster; property check, any seeded method passes), 2.4 crates for
Tobi's week via the 1.1 function, 4.0 a 200-week stress test in three chained
cells. Verified: 60 wrong-answer variants without a check crash, and the
solution boots 9/9 green in headless Chromium (WASM).

A3c. **Lab 07 as built (2026-10-09):** 8 coded core tasks + quiz + trace + 3
bonuses, masks first because Checkpoint 4 leans on them. 1.1 count and mean
of the critical deliveries (the shape of CP4 task 2), 1.2
`risk_report_ex12` (dict, 3 probes, one with no delivery over the limit:
`nan` has to become 0.0), 1.3 fix the bug (`|` where `&` belongs), 2.1 fix
the bug (wrong `axis`, the shape of CP4 task 3), 2.2 zone shares in percent,
2.3 `best_zone_ex23` (3 grids), 2.4 the busiest day's share, 4.0 the strong
days in three chained cells. The checks reject NumPy number types and ask
for plain `int`/`float`, as the checkpoint does. The first callout tells
students to finish and show the Zed install before starting. Verified: 68
wrong-answer variants without a check crash.

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

Checked on 2026-10-09 against the labs as built: t1 by lab 06 1.1, t2 by
lab 07 1.1 and 1.2, t3 by lab 07 2.1, t4 by lab 06 2.1 and 2.2, t5 (what
`prices[prices > 10]` returns) by the filter in lab 07 1.1 and the
Section 1 recap, t6 (calling a name imported by name) by lab 06 1.2. The
checkpoint's numbers differ from every lab and QR exercise value.

## Workstream B: the tooling switch in VII

B1. **Announce in VI (13 Oct):** bring a laptop you can install software
on, plus charger, to VII on 27 Oct; create the free Mistral account in VI as
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

Built on 2026-10-09: `lec_07` ends wrap-up, then `Leaving the Browser`
(four slides: the three tools, uv and the `python-labs` folder, Zed and
Vibe, the check), then the lab handoff. `lec_10` still carries its own
toolchain slides until its rewrite.

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

C4b. **Lab 08 as built (2026-10-09):** `orders_messy.csv` has 86 rows: the
80 orders, 5 exact duplicates, 6 rows spelled `"Hafen "`, 25 orders
without a rating and the test order of decision 18. Seven tasks: 1 first
look (`raw_rows`, `unrated_rows`), 2 `clean` and `order_count`, 3 Tobi's
Hafen number (`hafen_revenue`, `clean` repaired to four zones), 4
`revenue_by_zone` and `top_share`, 5 critical deliveries on a copy
(`timed`, `critical_count`, `critical_share_by_zone`), 6 Tobi's rating
(`avg_rating`; his `fillna(0)` average of 2.76 lies below the lowest
rating given), 7 `zone_report` and a one-sentence `recommendation`. Key:
80 orders, Altstadt 376.2, Hafen 325.3, Nord 345.9, Sued 395.9, top share
27.43, 12 critical, rating 4.01; with the test order left in: 81 orders,
Nord 444.9, top share 28.85. Verified: the solution exits 0 on pandas
2.3.2 and 3.0.6, and 70 variants (wrong answers, unsolved stages, other
correct routes) each end at the intended message or pass.

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

C5b. **Lab 09 as built (2026-10-09):** `labs/lab_09_pitch.py`, same
`orders_messy.csv`. Nine tasks: 1 clean again (`clean`, `order_count`; no
problem named), 2 revenue per day (`daily.png`, `best_day`; gives the three
closing lines `plt.gca()`, `plt.savefig`, `plt.close()`), 3 revenue per
zone, highest first (`zones.png`, `top_zone`), 4 spread of the order values
(`values.png`, `big_orders` above 25 euros), 5 Tobi's growth slide with a
y-axis from 780 to 855 (`growth.png`, `week1`, `week2`, `growth_pct`),
6 Tobi's momentum slide of days 6 to 8 (`momentum.png`, `typical_day`),
7 Tobi's rider argument (`stars.png`, `stars_title`), 8 the summary
(`pitch` dict, `headline`), 9 optional own question (`own.png`). No brief
names the kind of chart. The checks read each chart through the stored
`plt.gca()` (title, labels, file written in this run, canvas closed, drawn
values agree with `clean`), and the last cell glues the six charts into
`pitch_deck.png`. Two departures from C5: a scatter task was added, and
Tobi's axis trick now shows a rocket (raw 784.4 to 849.7), not a cliff.
Key: 80 orders, best day 3, Sued, 13 big orders, weeks 731.1 and 712.2,
growth -2.59, typical day 103.09. Tobi's raw weeks kept: 784.4 and 849.7,
growth +8.32. Test order left in: 81 orders, best day 8, Nord, 14 big
orders, growth +10.96, typical day 110.16. Verified: the solution exits 0
on pandas 2.3.2 and 3.0.6 (matplotlib 3.11.2), and 135 variants (wrong
answers, unsolved stages, other correct routes, the hidden items left in)
each end at the intended message or pass. `lec_09` got the slide "A chart
in a script", the lab handoff with the two-minute download drill on
`ex_09_e`, and the "Before Session X" slide cut to the GitHub account plus
git and `gh`; `general/cheatsheet.qmd` no longer sends scripts to
`plt.show()`.

C6. **Tutorial pages `tut_08`/`tut_09`.**
- Replace the molab/WASM buttons, the save/download warning and the
  boot callouts with download buttons for the script and the CSV
  (decision 7, as built).
- Add the run steps inline, in three lines (no separate how-to page).

C7. **Solutions** (private repo). `sol_08`/`sol_09` become scripts,
published after the session as a download button on the tutorial page, not as a
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

## Mistral changes found on 2026-10-09

Read from Mistral's pricing, docs and help pages. Tobias clicked through the
free sign-up (no phone number asked), both opt-out switches and the `vibe`
browser sign-in with a fresh free account the same day:

- **Le Chat is now Vibe** (modes: Vibe Chat, Vibe Work, Vibe Code); the API
  console is "Mistral Studio". `chat.mistral.ai` and logins are unchanged.
- **A free plan still exists.** It includes Vibe, "Vibe for code" in the
  terminal and Studio access, with "limited messages" and "limited coding
  sessions". The limits are not published. Students can get Pro for
  $5.99/month.
- **Sign-in replaces the API key.** `vibe` now signs in with the Mistral
  account in the browser by default. A key is the fallback, created under
  Code > Vibe CLI on `chat.mistral.ai`. The package (`mistral-vibe`) and the
  commands (`vibe`, `vibe-acp`) are unchanged.
- **Vibe is in the ACP agent registry**, which supports decision 13.
- **Mistral Large 4** (public preview, 6 Oct 2026) has a 1M-token context
  window; `lec_06` cites it.
- Done on 2026-10-09: `general/ai-tools.qmd` (names, sign-in, both opt-out
  paths, Session VII timing, Windows PATH line) and the three `lec_06`
  mentions. Still saying "key from Session VI": `lec_09:590`, `lec_10:291`.

## Checks closed on 2026-10-09 (owner)

- Mistral Vibe installs from Zed's agent registry with a free account
  (decision 13).
- `uv run python` works from Zed's terminal on Windows inside a uv
  project folder.
- The free plan's "limited coding sessions" are accepted as sufficient
  for labs 08-09. If they run out, the fallback is Zed's own agent on the
  student plan's credits.
- The course folder: `general/uv.qmd` now creates `python-labs` as the
  first project (it was `my-first-project`) and adds pandas and matplotlib
  there, so the folder from B2 is the one students make in Session VII.

## Deadlines

- **13 Oct (VI):** lab 06 reworked (A1-A3), `sol_06`, quiz balance,
  headless boot; the B1 announcement; `lec_06:107`.
- **27 Oct (VII):** decision 13 verified; `ai-tools.qmd` + `uv.qmd`
  fixed (B5, B2); `lec_07` install block; lab 07 reworked + `sol_07`;
  CP4 alignment (A4) checked.
- **3 Nov (VIII):** `labs/lab_08` + CSV + `sol_08`; `tut_08` download
  buttons; `_quarto.yml` resources; `lec_08` agent slide and `lec_08`
  ripples; the conventions section (C2); nb_08 retired. Built 2026-10-09.
- **10 Nov (IX):** `labs/lab_09` + `sol_09`; `tut_09`; `lec_09` slide;
  nb_09 retired. Built 2026-10-09.
- **17 Nov (X):** `lec_10` cold open and toolchain rewrite; the rest of
  the ripple sweep, `CLAUDE.md`, the foundations pointer.
