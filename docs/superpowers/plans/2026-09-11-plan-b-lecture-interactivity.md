# Plan B — Lecture interactivity (all decks I–IX)

> **For agentic workers:** one worker per deck; each task below is self-contained. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Regular decks have 5 QR exercises (CP decks 3), every QR notebook has a core task plus a stretch task, and every block has one more predict-and-vote pair.

**Architecture:** Keep the block structure. A new mid-block QR stop is inserted after the first self-contained concept of the big blocks; exercise letters follow slide order, so existing notebooks are renamed with `git mv`. `helpers/make_qr.py` and the PNGs are regenerated once at the end by the coordinator.

Spec: `docs/superpowers/specs/2026-09-09-session-length-and-notebook-onboarding-design.md` (Workstream B). Conventions: `docs/authoring-conventions.md` (binding).

## Global Constraints

- No emojis anywhere. Verdict labels: `Correct — …`, `Wrong — …`, `Not attempted — …` (see any `notebooks/exercises/ex_02_*.py`).
- One global per cell; every answer pre-defined as `None`; every editable cell contains `# YOUR CODE BELOW`.
- Check cells never crash on a plausible wrong answer; numbers compared with `round(x, 2) == LITERAL` after `isinstance`; literals verified in Python.
- Hint accordions only in `ex_06`+ (Hint 1 nudge, Hint 2 `___` skeleton). `ex_01`–`ex_05` stay hint-free.
- Tobi's bugs: logic/runtime only, always terminating.
- MC / predict questions: options a–c, correct answer position varied, option lengths within 1.8x, no spoiler comments on question slides; `uv run python helpers/check_quiz_balance.py` must pass.
- A predict answer slide re-runs the code (`{python}` cell with `#| eval: true` / `#| output-location: fragment`); if the reveal crashes on purpose, add `#| error: true`.
- QR slide exact form (copy from an existing one in the same deck): `# Your turn — 5–10 minutes {.exercise-slide}` + URL line + `![](assets/qr/ex_XX_x.png){width=280}` + "First **predict** what happens, then run it."
- Exercise notebook title: `# Quick exercise: <name> (5–10 min)`.
- Do not touch `_repo-md/`, `_site/`, `helpers/make_qr.py`, or QR PNGs (coordinator does those).

## Placement table

| Deck | Type | New mid-block QR (insert after slide) | Letters after (git mv) | Extra predict pair per block (misconception) |
|---|---|---|---|---|
| lec_01 | regular | B1 after `## Naming rules` → **ex_01_a** (new); B3 after `## f-strings: the clean way` → **ex_01_d** (new) | old a→b, old b→c, old c→e | B1: reassignment (`price = 8.90; price = price + 1; print(price)`); B2: `10 / 2` is `5.0` (float from `/`); B3: `"3" + "4"` is `"34"` |
| lec_02 | regular | B1 after `## Combining conditions` → **ex_02_a** (new); B3 after `## break: an early exit` → **ex_02_d** (new) | old a→b, old b→c, old c→e | B1: `not a and b` precedence; B2: `range(1, 5)` yields four numbers; B3: `s.strip()` returns a new string, `s` unchanged |
| lec_03 | CP | B1 after `## Answer` of "print or return?" → **ex_03_a** (new) | old a→b, old b→c | B1: positional args swapped (`tip(15, 100)` vs `tip(100, 15)`); B2: two instances don't share attributes |
| lec_04 | regular | B1 after `## Answer` of "where does the slice stop?" → **ex_04_a** (new); B3 after `## Reading nested values` → **ex_04_d** (new) | old a→b, old b→c, old c→e | B1: `b = a; b.append(...)` also changes `a`; B2: `"Cola" in prices` checks keys, not values; B3: comprehension with an `if` filter drops items |
| lec_05 | CP | B1 after `## The big five (2)` → **ex_05_a** (new) | old a→b, old b→c | B1: `int("3.5")` raises `ValueError`, not `TypeError`; B2: a failing `assert` stops before the `print` after it |
| lec_06 | CP | B1 after `## from statistics import ...` → **ex_06_a** (new) | old a→b, old b→c | B1: `from math import pi` then `math.pi` is a `NameError`; B2: `random.choice` after the same seed picks the same item |
| lec_07 | regular | B1 after `## One operation, every element` → **ex_07_a** (new); B3 after `## axis in code` → **ex_07_d** (new) | old a→b, old b→c, old c→e | B1: `[1, 2, 3] * 2` (list repeats) vs `np.array([1, 2, 3]) * 2`; B2: `(a > 1) & (a < 5)` needs parentheses / `and` fails on arrays; B3: `.shape` of a 3x4 grid is `(3, 4)` |
| lec_08 | CP | B2 after `## Selecting a column, filtering rows` → **ex_08_b** (new) | old a stays a, old b→c | B1: `df.head(3)` vs `df.head()` row counts; B2: `df["total_eur"] > 20` is a Series of booleans, not a filtered frame |
| lec_09 | regular | B1 after `## The parts of a chart` → **ex_09_a** (new); B3 after `## The rule: growth starts at zero` → **ex_09_d** (new) | old a→b, old b→c, old c→e | B1: `plt.plot([3, 5, 4])` puts 0, 1, 2 on the x-axis; B2: histogram bins vs bar categories (how many bars for 5 categories); B3: `plt.ylim(700, 735)` makes a 3 % rise look like a doubling |

The misconception column is a default; a worker may replace it with a better one drawn from the same block, as long as the pair stays a predict-vote-reveal with executable reveal.

## Per-deck task (repeat for every deck)

**Files:** `lectures/lec_XX_*.qmd`; `notebooks/exercises/ex_XX_*.py` (rename + edit + create).

- [ ] **Step 1: Rename existing exercise notebooks** with `git mv` per the table, then update the `# notebooks/exercises/ex_XX_x.py` header comment, every URL `python.tobiasvlcek.com/notebooks/ex_XX_x/` and image `assets/qr/ex_XX_x.png` in the deck, and any variable suffixes that encode the letter (`_exa` → `_exb`, and so on, including in check cells).
- [ ] **Step 2: Add the stretch part to every existing exercise notebook.** After the core check cell insert: a markdown cell `**Done? Then:** <second task>` (reuses the core variables; a real step up: a second rule, an edge case, or a bug in Tobi's version), a your-code cell with the new answer pre-defined as `None` and `# YOUR CODE BELOW`, and its own check cell (same verdict style). Keep the closing "*Nothing to save. This was a sandbox.*" cell last.
- [ ] **Step 3: Create the new exercise notebook(s)** for the mid-block stop, same shape (title, save callout, core task + check, stretch + check, closing cell), on the concept of the slides just before the stop. Copy the save-callout cell verbatim from a sibling.
- [ ] **Step 4: Insert the QR slide(s)** at the placement, exact form, pointing at the new letter.
- [ ] **Step 5: Add one predict pair per block** (`## Predict: …` question slide with code block + `a\) … b) … c) …` + `. . .` + `[Predict first]{.question}. Pick a letter, then I reveal the answer.`; `## Answer: …` slide with the bold letter, one-line why, executable cell). Place it at the slide where that misconception lives.
- [ ] **Step 6: Verify**
  - `uv run python helpers/validate_notebooks.py` → all ok.
  - `uv run python helpers/check_quiz_balance.py` → exit 0 (fix option lengths/positions if not).
  - Simulate each new check with a right answer, a plausible wrong one, and `None` in plain Python (import the notebook module is not needed; copy the check logic into a scratch script).
  - `grep -c 'Your turn' lectures/lec_XX_*.qmd` equals the target (5 regular / 3 CP); `ls notebooks/exercises/ex_XX_*` matches the letters.
  - No emoji: `grep -P '[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}]'` over the touched files is empty.

## Coordinator (after all decks)

- [ ] Update `EXERCISES` in `helpers/make_qr.py` to the new letters; `uv run python helpers/make_qr.py`; delete no PNGs by hand (regenerated set overwrites; remove stale `ex_XX_x.png` only if a letter disappeared, which never happens here).
- [ ] `uv run python helpers/validate_notebooks.py`, `uv run python helpers/check_quiz_balance.py`.
- [ ] `quarto render` (full), then `uv run --with playwright ../lecture-foundations/scripts/check_slide_overflow.py`.
- [ ] Report; no commit unless asked.
