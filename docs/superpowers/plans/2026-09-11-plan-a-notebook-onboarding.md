# Plan A — Notebook onboarding, markers, emoji sweep

> **For agentic workers:** REQUIRED SUB-SKILL: Use `subagent-driven-development` or `executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Students know which cells to touch and what the verdicts mean; all course material is emoji-free.

**Architecture:** One new Quarto page (`general/notebooks.qmd`) with a CSS mock of the three cell kinds, linked from navbar, tutorials, FAQ, and the Session I deck. Notebooks get a uniform `# YOUR CODE BELOW` marker and a read-me callout. A one-off script (scratchpad, not committed) rewrites every emoji in both repos to a plain-text label.

**Tech Stack:** Quarto (revealjs + website), marimo 0.23.13 notebooks, Python 3.12 via uv.

Spec: `docs/superpowers/specs/2026-09-09-session-length-and-notebook-onboarding-design.md` (Workstream A, plus B4's slide retitle).

## Global Constraints

- No emojis anywhere (notebooks, slides, pages, conventions, private repo).
- Never add AI-attribution lines to commits in this repo or the checkpoints repo. Do not commit in this plan unless the user asks.
- `_repo-md/` and `_site/` are generated; only a full `quarto render` may update `_repo-md/`.
- Notebooks: one global per cell; callout `kind` carries the verdict colour.
- Private repo `../Introduction-to-Python-checkpoints`: solutions AND checkpoint notebooks get the sweep; graded values are untouched.

---

### Task 1: Emoji sweep (both repos)

**Files:**
- Create (scratchpad only): `<scratchpad>/strip_emoji.py`
- Modify: every `lectures/*.qmd`, `tutorials/*.qmd`, `notebooks/**/*.py`, `general/*.qmd`, `docs/authoring-conventions.md`, `../Introduction-to-Python-checkpoints/solutions/*.py`, `../Introduction-to-Python-checkpoints/checkpoints/*/*.py`

- [ ] **Step 1: Write the sweep script**

```python
import re, sys, pathlib
RULES = [
    (r"✅ Correct", "Correct"),
    (r"\{_done\}/\{_total\} ✅\*\*", "{_done}/{_total} correct**"),
    (r"✅/🔲 boxes", "check boxes"),
    (r"green ✅ checks", "green checks"),
    (r"earns the ✅", "turns the check green"),
    (r"live ✅/❌", "live correct/wrong verdict"),
    (r"hides the ✅", "hides the green verdict"),
    (r"✅ ", "Correct — "),
    (r"❌ Not quite", "Not quite"),
    (r"❌ ", "Wrong — "),
    (r"🔲 (.*?): not attempted yet\.", r"Not attempted — \1."),
    (r"🔲 not attempted", "Not attempted"),
    (r"🔲 (Pick|Set) ", r"\1 "),
    (r"🔲 ", "Not attempted — "),
    (r"💡 ", ""),
    (r"💾 ", ""),
    (r"# 🔥 ", "# "),
    (r"# 📋 ", "# "),
    (r"# ⚠️ ", "# "),
    (r"# 💥", "# crashes here"),
    (r"📝 ", ""),
    (r" ?(📦|📊|📤)$", ""),
]
EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-➿⭐⬆⤴⤵〰〽㊗㊙️‍]")
for arg in sys.argv[1:]:
    for p in pathlib.Path(arg).rglob("*"):
        if p.suffix not in {".py", ".qmd", ".md"} or "__pycache__" in p.parts: continue
        s = orig = p.read_text()
        for pat, rep in RULES: s = re.sub(pat, rep, s, flags=re.M)
        s = EMOJI.sub("", s)
        s = re.sub(r"[ \t]+(?=[\"'\n])", lambda m: "" if m.group(0) and m.end() < len(s) and s[m.end()] in "\"'\n" else m.group(0), s)  # drop trailing space before a closing quote / EOL
        s = re.sub(r"(?<=\S)  (?=\S)", " ", s)  # collapse doubled spaces left behind
        if s != orig: p.write_text(s); print("rewrote", p)
```

- [ ] **Step 2: Run it**

Run: `uv run python <scratchpad>/strip_emoji.py lectures tutorials notebooks general docs/authoring-conventions.md ../Introduction-to-Python-checkpoints/solutions ../Introduction-to-Python-checkpoints/checkpoints`

- [ ] **Step 3: Verify nothing is left, review the diff for awkward leftovers**

Run: `grep -rnP '[\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}]' lectures tutorials notebooks general docs/authoring-conventions.md ../Introduction-to-Python-checkpoints --include='*.qmd' --include='*.py' --include='*.md'` → no output.
Run: `git diff --stat` and `git -C ../Introduction-to-Python-checkpoints diff --stat`; skim `git diff -U0 | grep '^+' | grep -i 'correct — correct\|wrong — wrong\|— —\| \.$'` → no output. Fix by hand what the rules missed (e.g. a sentence now ending with a space, "## Compare, don't memorize" trailing spaces).

- [ ] **Step 4: Update the conventions text**

In `docs/authoring-conventions.md` (after the sweep):
- line "Every notebook opens with the save callout" already reads without the emoji; add a bullet under **Notebooks**: `- No emojis anywhere (Tobi, 2026-09-09). Verdicts are plain text: "Correct — Exercise N.M:", "Wrong — Exercise N.M:", "Not attempted — Exercise N.M." Hint accordion titles are "Hint 1 (a nudge)" / "Hint 2 (the structure)".`

- [ ] **Step 5: Run the gates**

Run: `uv run python helpers/validate_notebooks.py` → passes.
Run: `uv run python helpers/check_quiz_balance.py` → exit 0.
Run: `uv run python -c "import ast,glob;[ast.parse(open(f).read()) for f in glob.glob('../Introduction-to-Python-checkpoints/**/*.py', recursive=True) if '__pycache__' not in f]"` → no error.

### Task 2: `# YOUR CODE BELOW` marker in every editable cell

**Files:**
- Modify: notebooks listed by the audit below; `notebooks/_template.py`

**Produces:** every cell a student edits contains a line starting with `# YOUR CODE BELOW` (the page in Task 4 tells students to look for it).

- [ ] **Step 1: Run the audit**

```python
# <scratchpad>/audit_markers.py
import re, pathlib
for p in sorted(pathlib.Path("notebooks").glob("**/*.py")):
    if "__pycache__" in str(p) or p.name.startswith("_"): continue
    src = p.read_text()
    for m in re.finditer(r"@app\.cell(\([^)]*\))?\ndef _\([^)]*\):\n(.*?)\n    return", src, re.S):
        deco, body = m.group(1) or "", m.group(2)
        if "hide_code=True" in deco or "YOUR CODE BELOW" in body: continue
        if not (re.search(r"^\s*\w+ = None\b", body, re.M) or re.search(r"TOBI|FIX|YOUR|plt\.figure|^\s*(def|class) ", body, re.I | re.M)): continue
        print(f"{p}:{src[:m.start()].count(chr(10)) + 3}: {[l for l in body.splitlines() if l.strip()][0].strip()[:70]}")
```

Run: `uv run python <scratchpad>/audit_markers.py`

- [ ] **Step 2: Decide each hit and add the marker**

For each listed cell: if the student is supposed to change it (fill a `None`, finish a `def`/`class` body, fix Tobi's bug, write a plot) insert `    # YOUR CODE BELOW` as the first body line, keeping the existing comment (`# TOBI'S CODE: …` becomes the second line). Leave alone: worked examples (`# Worked example (read + run this)`), `# Given: do not change this`, `# Runs only after the button above. No editing needed.`, and cells that only set up data (`customers = [...]` with no `None` and no task). Known editable hits from the 2026-09-11 audit: `ex_01_a.py:42`, `ex_03_a.py:58`, `ex_03_b.py:55`, `ex_08_a.py:104`, `ex_09_a.py:102`, `ex_09_b.py:108`, `ex_09_c.py:171`, `nb_01:344`, `nb_02:384`, `nb_03:154,218,389,459,576,800`, `nb_04:705`, `nb_05:227,351,413,601,691`, `nb_08:557`, `nb_09:163,247,356,438,527,658` (line numbers pre-sweep; re-run the audit after Task 1).

- [ ] **Step 3: Template**

In `notebooks/_template.py`, ensure the TODO answer cell shows `    # YOUR CODE BELOW: replace None` as its first line.

- [ ] **Step 4: Verify**

Re-run the audit; every remaining hit must be one of the "leave alone" kinds. `uv run python helpers/validate_notebooks.py` passes.

### Task 3: Read-me callout in every lab

**Files:**
- Modify: `notebooks/nb_01_lab_founding.py` … `nb_09_lab_pitch.py`, `notebooks/_template.py` (insert directly after the save-callout cell)

- [ ] **Step 1: Insert this cell after the save callout in each lab and the template**

```python
@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**How this notebook works:** run a cell with **Cmd/Ctrl+Enter**. "
            "Only edit the cells that contain `# YOUR CODE BELOW`; the check under "
            "each exercise updates by itself. A red error pauses everything below "
            "it, so fix that cell first. New here? Read "
            "[How the notebook works](https://python.tobiasvlcek.com/general/notebooks.html)."
        ),
        kind="info",
    )
    return
```

- [ ] **Step 2: Verify**

`grep -c 'How this notebook works' notebooks/nb_0*.py notebooks/_template.py` → 1 each. `uv run python helpers/validate_notebooks.py` passes.

### Task 4: "How the notebook works" page and links

**Files:**
- Create: `general/notebooks.qmd`
- Modify: `_quarto.yml` (navbar, after Cheatsheet), `tutorials/tut_0[1-9]_*.qmd` (one line under the buttons), `general/faq.qmd` (FAQ entry), `lectures/lec_01_introduction.qmd` ("How a notebook works" slide), `styles.scss` (mock-cell styles)

- [ ] **Step 1: Write the page**

```markdown
---
title: "How the notebook works"
subtitle: "Read this once before your first lab"
---

Every lab and every in-lecture exercise is a **marimo notebook** that runs in your browser tab. Nothing to install. This page explains what you see, what to click, and what to leave alone.

## Three kinds of cell

A notebook is a page of cells, top to bottom. Sections mirror the lecture blocks. You will meet three kinds:

::: {.nb-mock}
::: {.nb-cell .nb-read}
**Exercise 1.2 (core) — first revenue**
Multiply the price by the portions and store the result in `revenue_ex12`.
:::
::: {.nb-cell .nb-code}
```python
# YOUR CODE BELOW: replace None
revenue_ex12 = None
```
:::
::: {.nb-cell .nb-check}
Not attempted — Exercise 1.2. Assign your answer to `revenue_ex12` and run the cell.
:::
:::

1. **Read cells** hold the story, the instructions, and worked examples. Their code is hidden. You never edit them.
2. **Your-code cells** contain the line `# YOUR CODE BELOW`. These are the **only** cells you edit. Replace every `None` with your answer, and finish any function or class body marked this way.
3. **Check cells** sit right under a your-code cell. They run by themselves and show a verdict. You cannot edit them and never need to run them.

## Running a cell

Click into a your-code cell and press **Cmd/Ctrl+Enter** (or the play button at the cell's right edge). The output appears below the cell.

A cell shows the value of its **last line**. An assignment such as `revenue_ex12 = 26.70` shows nothing by itself. That is normal: the check cell echoes **Your result** next to the verdict, so you still see what you computed.

## What updates by itself

marimo is *reactive*: when you run a cell, every cell that depends on it re-runs. Change an answer, run the cell, and the check below updates. You never need a "run all".

## The three verdicts

| Verdict | Colour | Meaning |
|---|---|---|
| Not attempted | grey | the variable is still `None`. A `print` alone does not count; assign the value to the named variable and run the cell |
| Wrong | red | the check ran and disagrees; it tells you what it expected |
| Correct | green | done. Move on |

The **progress cell** at the bottom of a lab counts your core exercises. Bonus exercises and prediction quizzes are not counted.

## A red error pauses everything below

If a your-code cell raises an error, the traceback appears in red under it, and every cell that depends on it, including its check and the progress cell, pauses. Nothing is lost. Read the **last line** of the traceback, fix the cell, run it again, and the checks come back.

## Hints

Every exercise has two collapsed hints under the check. Open **Hint 1** first (a nudge, no code), then **Hint 2** (the structure, with blanks). Solutions appear on the tutorial page after the session.

## Saving versus downloading

- **The tab remembers you.** Reloading the page (Cmd/Ctrl+R) keeps your work. Closing the tab and opening the course link again later starts from a clean notebook.
- **Cmd/Ctrl+S** saves inside the tab.
- **Menu (top right) → Download → Download Python code** gives you the `.py` file. This is the only copy that survives, and it is exactly how you hand in a checkpoint. **Save first**: without a save, the downloaded file is empty.
- A downloaded `.py` is for backup and submission. You cannot upload it back into the browser editor.

## Buttons you can ignore

The editor shows more than you need. Leave these alone:

- the icons in the **left sidebar** (files, variables, dependency graph, packages, settings);
- the small buttons that appear when you **hover a cell**: add cell above/below, move, hide code, and the **delete** button. Deleting a check cell breaks the progress count;
- the **app view** toggle at the bottom left. If the code disappears, click it again to come back to the editor.

## Done for today

Save, download, close the tab. Done early? You are free to go. Not done when the session ends? The rest is homework; keep the tab open on your laptop.
```

- [ ] **Step 2: Mock-cell styles**

Append to `styles.scss`:

```scss
/*-- scss:rules --*/
.nb-mock { border: 1px solid #ccc; border-radius: 6px; padding: .5rem; margin: 1rem 0; max-width: 40rem; }
.nb-cell { border-left: 4px solid; padding: .4rem .8rem; margin: .4rem 0; border-radius: 3px; }
.nb-read { border-color: #999; background: #f7f7f7; }
.nb-code { border-color: #2a6fdb; background: #eef4ff; }
.nb-code pre { margin: 0; background: transparent; }
.nb-check { border-color: #888; background: #f0f0f0; color: #555; }
```

(Check whether `styles.scss` already has a `/*-- scss:rules --*/` marker; if so, append below it instead of adding a second one.)

- [ ] **Step 3: Links**

`_quarto.yml`: under the `Cheatsheet` entry add
```yaml
      - text: "How the Notebook Works"
        href: general/notebooks.qmd
```
Each `tutorials/tut_0X_*.qmd`: right after the two button lines, add the paragraph
`New here? Read [How the notebook works](../general/notebooks.qmd) first: which cells to edit, how to run them, what the verdicts mean.`
`general/faq.qmd`, entry "How do I open and work on a lab notebook?": append the sentence `The full walkthrough, with a picture of the three cell kinds, is on [How the notebook works](notebooks.qmd).`
`lectures/lec_01_introduction.qmd`, slide `## How a notebook works`: replace the bullet list with
```markdown
- A notebook is a page of **cells**; each cell holds a few lines of code
- **Run a cell**: click into it and press `Cmd/Ctrl+Enter` (or the play button at its edge). The output appears right below it
- Only edit cells that contain `# YOUR CODE BELOW`; the check under each exercise updates by itself
- A red error pauses everything below it: fix that cell first
- **Save your work**: `Cmd/Ctrl+S`, then menu (top right) → *Download* → *Download Python code*. The tab remembers you until you close it; the download is forever
- Full walkthrough: [How the notebook works](../general/notebooks.qmd)
```

- [ ] **Step 4: Verify**

`quarto render general/notebooks.qmd tutorials/tut_01_introduction.qmd` then `git checkout -- _repo-md/`. Open `_site/general/notebooks.html`; the mock shows three coloured boxes. Links resolve (`grep -o 'href="[^"]*notebooks[^"]*"' _site/tutorials/tut_01_introduction.html`).

### Task 5: QR slide retitle (spec B4)

**Files:**
- Modify: `lectures/lec_0[1-9]_*.qmd`, `docs/authoring-conventions.md` ("QR exercise slide (exact form)")

- [ ] **Step 1:** `sed -i '' 's/Your turn — 10 minutes/Your turn — 5–10 minutes/' lectures/lec_0*.qmd docs/authoring-conventions.md`
- [ ] **Step 2:** `grep -c 'Your turn — 5–10 minutes' lectures/lec_0*.qmd` → 3,3,2,3,2,2,3,2,3.

### Task 6: Full render and final verification

- [ ] **Step 1:** `quarto render` (full; regenerates `_repo-md/` and WASM exports).
- [ ] **Step 2:** Slide overflow gate on `lectures/lec_01_introduction.qmd`: `uv run ../lecture-foundations/scripts/check_slide_overflow.py _site/lectures/lec_01_introduction.html` (invoke per that script's `--help`).
- [ ] **Step 3:** Serve `_site` with a threaded server, open `notebooks/nb_01_lab_founding/`, confirm the read-me callout renders and a check cell shows "Not attempted — Exercise 1.1".
- [ ] **Step 4:** `git status` in both repos; report the file list to Tobi. No commit unless asked.
