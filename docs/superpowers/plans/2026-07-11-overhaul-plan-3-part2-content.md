# Course Overhaul Plan 3: Part II Content (Sessions VI–IX) + CP4–5 + AI Tools

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete Part II of the course: full lecture rewrites for Sessions VI–IX, lab notebooks + in-lecture exercises + launcher pages, checkpoints CP4–5 (AI-allowed era), the `general/ai-tools.qmd` page (facts re-verified), the Part-II chatbot prompt variant, and the pandas-in-WASM data pipeline (spike → dataset → labs).

**Architecture:** Every artifact copies the proven Part-I patterns (conventions in `docs/authoring-conventions.md`; templates: `notebooks/nb_04_lab_menu.py` for labs, `notebooks/exercises/ex_04_a.py` for exercises, `tutorials/tut_04_dimensions.qmd` for launchers, `lectures/lec_05_errors.qmd` for a CP-session deck, `lectures/lec_04_dimensions.qmd` for a regular deck). New in this plan: a WASM pandas data-loading pattern (Task 1 spike), one canonical Part-II dataset (`notebooks/public/orders.csv`, Task 12), and a grader hardening for NumPy/pandas values (Task 10).

**Tech Stack:** Quarto/revealjs, marimo 0.23.x WASM export, uv, numpy 2.x, pandas, matplotlib, pytest (private repo), segno (QR).

**Sequencing:** Plan 4 (Part III: Session X tooling/git/kickoff deck, `general/git-basics.qmd`, retired-content sweep, `_quarto.yml` nav cleanup, `/humanizer` pass) is written after this plan executes. Side quests remain OUT — ideas go to `docs/side-quest-backlog.md`.

---

## Context for the zero-context engineer

- Two repos: this public Quarto site, and the PRIVATE grader repo at `/Users/vlcek/development/lectures/Introduction-to-Python-checkpoints`. Checkpoint notebooks, reference tests, and ALL solution notebooks live in the private repo. Never commit checkpoint or solution content to the public repo except via the documented publishing motion (`docs/authoring-conventions.md` → "Solution notebooks").
- **Commit rule (repo policy, overrides all defaults): NEVER add `Co-Authored-By`, "Generated with Claude Code", or any AI-attribution line to commits or PRs in either repo.**
- **Read `docs/authoring-conventions.md` in full before implementing any task.** It is the binding pattern source (notebook rules, check-cell style, hint ladder, deck skeletons, warm-up pattern, QR slides, checkpoint rules, float safety, no-hang rule). This plan only spells out what is NEW or task-specific.
- marimo notebooks: cells are `@app.cell` functions; a global may be defined in ONE cell only (`+=` counts); `_name` is cell-private; `@app.cell(hide_code=True)` for md/check/hint cells. After editing, validate: `uv run python helpers/validate_notebooks.py notebooks/<file>.py`.
- Rendering: `quarto render <file>` works (`_environment` pins `QUARTO_PYTHON`). A single-file render DELETES sibling files in `_repo-md/` — always `git checkout -- _repo-md/` afterwards. A FULL `quarto render` fails on the untracked `Management-Science/` dir — do per-file renders only.
- **Story canon, Part II:** the investor ARRIVES in Episode 6 (until now she only cameo'd). Arc: VI = due-diligence week, VII = "the numbers deck" metrics sprint, VIII = the data room + Kevin's AI incident (he shipped hallucinated `df.summarize()` code) + MunchCorp's "data-driven" press release, IX = building the pitch charts honestly. Kevin stays inept but lovable; German authorities and Formular 27b/6 may cameo. Checks stay name-agnostic (never assert on the startup's name).
- **AI policy shift:** Part I was AI-free. From Session VI, AI is allowed AND taught (spec §7). CP4/CP5 explicitly allow AI. Consequence for checkpoint design: trace tasks are trivial now (students can just run/ask), so CP4–5 lean on compute/fix/apply tasks where running the code is fine but understanding is still required.
- **Grader gap (fixed in Task 10):** `grader/runner.py::_coerce` only passes plain Python scalars/lists/dicts to JSON. A NumPy scalar (`np.float64`) currently degrades to `repr()`; NumPy values nested in a list would crash `json.dumps`. Task 10 must land BEFORE CP4 (Task 11) and CP5 (Task 19).
- **WASM data rule:** Part I shipped all data inline. Part II Sessions VIII–IX use `notebooks/public/orders.csv` via the loader pattern that Task 1's spike validates. Sessions VI–VII stay inline (no files needed). Checkpoints ALWAYS use inline data (they deploy to a different host — no `public/` coupling).
- Numbers in this plan were verified in Python on 2026-07-11 (exact floats, seeds, sums). If you change ANY input value, re-verify its expected value in Python before writing a check, hash, or reference test.

### Freshness ledger (Part II graded answers — keep these DISTINCT)

CP values AND answers must differ from all lecture-demo/exercise/lab values (conventions doc). This table is the collision check; CP implementers (Tasks 11, 19) must verify against it.

| Artifact | Key graded answers |
|---|---|
| lec_06 demos | ceil(130/48)=3 · median ratings 4.5 · seed(7)×5 randint(1,20)=[11,5,13,2,3] · floor(-2.5)=-3 |
| ex_06_a / ex_06_b | crates 9 · demand [10,18,18,25,14,20,11] (seed 21) |
| nb_06 | crates 7 · median 4.3 / mean 4.27 · mean 17 · seed(4) [15,17,11,20,23,12,10] · Kevin fix seed(9) [22,27,19,16,12,13,29] · raffle seed(12) ['Altstadt','Hafen','Hafen','Sued'] · boss mean 14.2 |
| lec_07 demos | VAT [14.28,10.71,17.85] · late count 4 / mean 42.5 · zone totals [46,37,35,26] |
| ex_07_a/b/c | gross [9.52,13.09,16.66] · late 3 / 46.0 · totals [30,34,38], best idx 2 |
| nb_07 | discount [5.4,8.1,10.8,16.2] · slow 2 / 57.5 · zone totals [141,109,100,82], best 'Nord', zone means [20.14,15.57,14.29,11.71] |
| CP4 | crates probes 5/4/1 · count 5 / mean 48.8 · zone totals [1545,1370,1260,1665] · seed(23) [6,3,2,6,8] · MCQs b, b |
| ex_08_a/b | Nord mean 14.5 · count 3 / revenue 57.0 |
| nb_08 / nb_09 | computed from committed orders.csv (Task 12) — implementer records them in the lab header comment and checks them against this ledger |
| ex_09_a/b/c | total 1336.5, best day 6 · best zone 'Nord' (412.60) · growth 10.0 |
| CP5 | Altstadt 53.7 · mean 18.13 · dict {Altstadt 53.7, Hafen 34.7, Nord 48.3, Sued 44.6} · count 6 · MCQs c, b (letters per option order in Task 19) |

---

### Task 1: Spike — pandas + `public/` files in WASM

**Goal:** A validated, copy-paste `load_orders()` cell pattern that works BOTH in exported WASM notebooks and in local runs (`validate_notebooks.py`, `marimo edit`), plus a written verdict.

**Files:**
- Create: `docs/superpowers/specs/2026-07-11-spike-pandas-wasm.md`
- Modify: `docs/authoring-conventions.md` (replace the "inline until pandas" note's forward reference with the validated pattern)

**Acceptance Criteria:**
- [ ] Verdict doc records, for each pattern A/B/C below, works-or-fails in (1) exported WASM in a real browser and (2) local `app.run()`
- [ ] A canonical loader cell (final form depends on verdict) is documented in `docs/authoring-conventions.md`
- [ ] Probe artifacts are deleted; no notebook named `_probe*` or `probe*` is committed

**Verify:** `git status --short` clean of probe files; conventions doc contains a fenced `load_orders` cell.

**Steps:**

- [ ] **Step 1: Create probe data + notebook (NOT committed)**

Write `notebooks/public/probe.csv` (5 rows, any columns) and `notebooks/_probe_wasm.py` (underscore prefix → skipped by `helpers/export_marimo.py`'s glob, so it can't leak into a real export run). The probe tests three patterns, each in its own cell so one failure doesn't hide the others:

```python
import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(mo, pd):
    # Pattern A: plain path string into read_csv
    _loc = mo.notebook_location() / "public" / "probe.csv"
    try:
        _df = pd.read_csv(str(_loc))
        result_a = f"A ok: {len(_df)} rows"
    except Exception as _e:
        result_a = f"A FAIL: {type(_e).__name__}: {_e}"
    result_a
    return (result_a,)


@app.cell
def _(mo, pd):
    # Pattern B: urllib fetch -> StringIO (the Plan-1 spike's known-good text path)
    _loc = mo.notebook_location() / "public" / "probe.csv"
    try:
        import io
        import urllib.request

        with urllib.request.urlopen(str(_loc)) as _r:
            _df = pd.read_csv(io.StringIO(_r.read().decode("utf-8")))
        result_b = f"B ok: {len(_df)} rows"
    except Exception as _e:
        result_b = f"B FAIL: {type(_e).__name__}: {_e}"
    result_b
    return (result_b,)


@app.cell
def _(pd):
    # Pattern C: inline StringIO control (must always work)
    import io as _io

    _df = pd.read_csv(_io.StringIO("a,b\n1,2\n3,4\n"))
    result_c = f"C ok: {len(_df)} rows"
    result_c
    return (result_c,)


if __name__ == "__main__":
    app.run()
```

- [ ] **Step 2: Local leg**

Run: `uv run python helpers/validate_notebooks.py notebooks/_probe_wasm.py` — record which patterns print ok (expect A ok, B FAIL locally, C ok). If the validator skips underscore files, run the probe directly: `uv run python notebooks/_probe_wasm.py`.

- [ ] **Step 3: WASM leg**

```bash
uv run marimo export html-wasm notebooks/_probe_wasm.py -o /tmp/probe_export --mode run
ls /tmp/probe_export/public/   # confirm probe.csv was copied by the exporter
python3 -m http.server 8765 --directory /tmp/probe_export &
```

Open `http://localhost:8765/` with the playwright browser tools, wait for pyodide to boot (the three result strings render on the page), and record `result_a/b/c`. Kill the server.

- [ ] **Step 4: Write the verdict + canonical loader**

Write `docs/superpowers/specs/2026-07-11-spike-pandas-wasm.md` with the A/B/C matrix (WASM × local). Then add the canonical loader to `docs/authoring-conventions.md` under the data rule. Expected shape (adjust to the verdict — e.g. if A works in WASM too, drop the fallback):

```python
@app.cell(hide_code=True)
def _(mo, pd):
    def _load_orders():
        _loc = mo.notebook_location() / "public" / "orders.csv"
        try:
            return pd.read_csv(str(_loc))  # local run: plain filesystem path
        except Exception:
            import io
            import urllib.request

            with urllib.request.urlopen(str(_loc)) as _r:  # WASM: URLPath → fetch
                return pd.read_csv(io.StringIO(_r.read().decode("utf-8")))

    orders = _load_orders()
    return (orders,)
```

- [ ] **Step 5: Clean up and commit**

Delete `notebooks/_probe_wasm.py` and `notebooks/public/probe.csv` (keep the empty `notebooks/public/` dir out of git — Task 12 creates it for real).

```bash
git add docs/superpowers/specs/2026-07-11-spike-pandas-wasm.md docs/authoring-conventions.md
git commit -m "spike: pandas data loading in WASM notebooks — verdict + loader pattern"
```

---

### Task 2: `general/ai-tools.qmd` (facts re-verified) + nav entry

**Goal:** The AI-tools page every Part-II student uses to get at least one zero-cost working AI setup, with every fact re-verified against the live web before publishing.

**Files:**
- Create: `general/ai-tools.qmd`
- Modify: `_quarto.yml` (sidebar: add the page under the General/Course-info group, next to `general/uv.qmd`)

**Acceptance Criteria:**
- [ ] Every claim in the fact list below was re-verified via web search on the implementation date; any changed fact is updated in the page AND flagged in the commit message
- [ ] Page contains NO rate-limit numbers for Mistral's free tier and NO WASM/load-time performance claims
- [ ] Copilot appears ONLY as the "sign-ups paused" note
- [ ] `quarto render general/ai-tools.qmd` succeeds; `git checkout -- _repo-md/` run afterwards

**Verify:** `quarto render general/ai-tools.qmd && git checkout -- _repo-md/ && echo PASS` → PASS.

**Steps:**

- [ ] **Step 1: Re-verify the facts (WebSearch/WebFetch each)**

Facts from spec §7 (verified July 2026 — re-verify now, note the date in an HTML comment at the top of the page):
1. **Zed education**: 12 months Zed Pro + $10/month AI credits for enrolled students; info page `zed.dev/education`, application `dashboard.zed.dev/education/apply`. Note the 12-month expiry.
2. **Provider truth table for Zed**: ChatGPT Plus/Pro works via native OpenAI sign-in (no API key). **Claude Pro/Max does NOT work with Zed's built-in Anthropic provider** (needs separate API credits) — document this distinction explicitly. Mistral needs a free La Plateforme API key.
3. **Mistral Free** (guaranteed zero-cost baseline): free Le Chat; free La Plateforme "Experiment" API tier usable in Zed. Do NOT publish rate-limit numbers. DO flag that free-tier API data is used for training by default, with the opt-out path (Admin Console → Privacy).
4. **OpenRouter free models**: one-line no-credit-card fallback.
5. **Copilot**: "new sign-ups paused indefinitely since April 2026" — students verified before then may still use it.

- [ ] **Step 2: Write the page**

Structure (match the tone/format of `general/uv.qmd` — practical, numbered steps, callouts):
1. *The course policy* — Part I: no AI (chatbot only). Part II (Session VI+): AI allowed and taught; CP4/CP5 allow AI. Disclosure rule: every submission that used AI carries a one-line note saying what it was used for.
2. *The guaranteed free setup: Mistral* — Le Chat account; La Plateforme API key; training-data opt-out callout.
3. *Zed + AI* — install pointer (details live in Session X; here only the AI-provider side), the education program, the provider truth table as a table (ChatGPT ✓ native / Claude ✗ built-in / Mistral ✓ via API key).
4. *Fallback: OpenRouter free models.*
5. *What about Copilot?* — the pause note.
6. *The course chatbot* — still available, now relaxed (full code on request).

- [ ] **Step 3: Wire into `_quarto.yml`, render, commit**

```bash
quarto render general/ai-tools.qmd && git checkout -- _repo-md/
git add general/ai-tools.qmd _quarto.yml
git commit -m "feat: AI tools page — verified free setups, provider truth table, course policy"
```

---

### Task 3: Part-II chatbot system prompt variant

**Goal:** The relaxed system prompt Tobias installs after Session V, replacing the Part-I hint-only prompt.

**Files:**
- Create: `docs/chatbot-system-prompt-part2.md`
- Modify: `docs/chatbot-system-prompt.md` (header note: point to the part2 file as the successor)

**Acceptance Criteria:**
- [ ] Full code allowed on explicit request, hints remain the default
- [ ] No checkpoint-refusal rule (CP4/5 allow AI); instead a disclosure-habit reminder
- [ ] Persona/story paragraph consistent with the Part-I prompt

**Verify:** File exists; `grep -c "NEVER write complete" docs/chatbot-system-prompt-part2.md` → 0.

**Steps:**

- [ ] **Step 1: Write the prompt file**

```markdown
# Course chatbot system prompt — Part II (AI-allowed)

**Install:** paste into the oshu.eu chat-widget system prompt, REPLACING the
Part-I prompt. **When: after Session V** (Part II starts with Session VI).

---

You are the course assistant for "Programming with Python" at Kühne Logistics
University. The students are beginners in their first programming course, now
past the halfway mark. The course runs as a story: each student founds a campus
food-delivery startup with their chaotic co-founder Kevin; exercises live in
that world (the investor — on-site since Episode 6 —, the German authorities,
the competitor MunchCorp). Feel free to play along.

In Part II of the course, AI tools are allowed and actively taught. You are one
of those tools now — but you are the one that knows the course. Your job is to
help students learn to work WITH AI, not to hide it from them.

RULES:
1. Default to hints and guided questions, like a good tutor. Most of the time
   a student learns more from finding the line themselves.
2. Full, runnable code IS allowed when a student explicitly asks for it. When
   you give it, always explain it — walk through what each part does, and say
   which parts they should verify themselves.
3. Model good AI craft in every answer: if you are not sure an API exists, say
   so; encourage students to run and test any code you give them; never invent
   library methods.
4. Remind students of the course disclosure habit when it fits naturally: work
   submitted with AI help carries a one-line note saying what the AI was used
   for. That includes help from you.
5. Error messages: teach reading the traceback — last line first, then the
   arrow. Translate the error into plain language.
6. Course topics now include modules, random, NumPy, pandas, matplotlib, and
   AI-assisted coding, on top of all Part-I Python. Stay on course topics
   (Python, the course materials, study organisation); politely decline
   anything else.

Keep answers short — a few sentences unless the student asked for code.
Answer in the language the student uses.
```

- [ ] **Step 2: Add successor note to the Part-I file + commit**

In `docs/chatbot-system-prompt.md`, extend the header's install note: "After Session V, replace with `docs/chatbot-system-prompt-part2.md`."

```bash
git add docs/chatbot-system-prompt.md docs/chatbot-system-prompt-part2.md
git commit -m "feat: Part-II chatbot prompt — hints by default, full code on request"
```

---

### Task 4: Session VI in-lecture exercises (`ex_06_a/b`)

**Goal:** Two QR sandbox exercises for the two lecture blocks of the CP-session deck lec_06.

**Files:**
- Create: `notebooks/exercises/ex_06_a.py`, `notebooks/exercises/ex_06_b.py`
- Modify: `helpers/make_qr.py` (EXERCISES += ex_06_a, ex_06_b), regenerate PNGs
- Template: copy structure from `notebooks/exercises/ex_04_a.py`

**Acceptance Criteria:**
- [ ] One concept, one screen, one graded name each; closing cell "*Nothing to save — this was a sandbox.*"
- [ ] `uv run python helpers/validate_notebooks.py notebooks/exercises/ex_06_a.py notebooks/exercises/ex_06_b.py` → ok
- [ ] `lectures/assets/qr/ex_06_a.png` and `ex_06_b.png` exist

**Steps:**

- [ ] **Step 1: `ex_06_a` — import a tool instead of building it (block 1)**

Story: 200 mini quiches for the investor breakfast, boxes hold 24 — how many boxes? Teach cell shows `import math` + `math.ceil` on a DIFFERENT example (crates of 48). Exercise: `boxes_exa = None` → student writes `math.ceil(200 / 24)`. Check: `isinstance(boxes_exa, int) and boxes_exa == 9`. Hint 1: "division gives 8.33... — you need the next whole box, and math has a function for exactly that." Hint 2: `boxes_exa = math.___(200 / 24)`.

- [ ] **Step 2: `ex_06_b` — seeded randomness (block 2)**

Story: the investor wants the demand projection to be *reproducible*. Teach cell: `random.seed` makes runs repeatable. Exercise: seed with **21**, then simulate 7 days of orders with `random.randint(5, 25)` into a list. Expected: `demand_exb == [10, 18, 18, 25, 14, 20, 11]` (verified). Check compares the full list and degrades kindly if the length is right but values differ ("did you seed exactly once, before the loop?"). Hint 2 skeleton:

```python
random.___(21)
demand_exb = []
for _day in range(7):
    demand_exb.append(random.____(5, 25))
```

- [ ] **Step 3: QRs, validate, commit**

```bash
uv run python helpers/make_qr.py
uv run python helpers/validate_notebooks.py notebooks/exercises/ex_06_a.py notebooks/exercises/ex_06_b.py
git add notebooks/exercises/ex_06_a.py notebooks/exercises/ex_06_b.py helpers/make_qr.py lectures/assets/qr/ex_06_a.png lectures/assets/qr/ex_06_b.png
git commit -m "feat: session VI in-lecture exercises (imports, seeded random)"
```

---

### Task 5: Episode 6 lab + solutions + launcher (`nb_06` / `sol_06` / `tut_06`)

**Goal:** The Session VI lab notebook (modules + random), its private solution notebook, and the rewritten tutorial launcher page.

**Files:**
- Create: `notebooks/nb_06_lab_diligence.py`
- Create (PRIVATE repo): `solutions/sol_06_lab_diligence.py`
- Rewrite: `tutorials/tut_06_modules.qmd` (launcher — copy `tutorials/tut_04_dimensions.qmd` verbatim, adjust episode name/URLs; keep the dormant commented Solutions link)
- Template: `notebooks/nb_04_lab_menu.py`

**Acceptance Criteria:**
- [ ] 7 graded cores + 1 ungraded trace radio + 1 MCQ (`answer_ex50`) + wrap-up ritual; progress cell counts the 7 cores + MCQ = "X/8"
- [ ] All expected values match the freshness ledger; every check literal re-verified in Python
- [ ] Solution notebook: answers filled, checks green, hints deleted, check cells byte-identical to the lab's
- [ ] Validator passes on the lab; private repo run of the solution passes too

**Verify:** `uv run python helpers/validate_notebooks.py notebooks/nb_06_lab_diligence.py` → ok; same for the sol file in the private repo.

**Steps:**

- [ ] **Step 1: Lab content — "Episode 6: Due Diligence Week"**

Intro md: the investor is HERE, in the shop, with a clipboard. She wants professional numbers by Friday. Kevin suggests "vibes". Sections and cores (naming per conventions: `<meaning>_exNM`):

*Section 1 — Don't build it, import it:*
- **1.1** `import math`: 75 delivery bags, a crate holds 12 → `crates_ex11 = math.ceil(75 / 12)` → **7**.
- **1.2** `import statistics`: ratings `[4.7, 3.6, 4.9, 4.2, 4.4, 3.8]` → `median_ex12` → **4.3** (even-length median = mean of middle two — teach line!) and `mean_ex12` → **4.27** after round. Check both with `round(_, 2)` (the raw median is `4.300000000000001` — the check MUST round).
- **1.3** alias import: `import statistics as stats`; daily orders `[12, 19, 15, 22]` → `avg_ex13 = stats.mean(...)` → **17** (int). Check: `round(avg_ex13, 2) == 17`.

*Section 2 — Rehearsing luck (random):*
- **2.1** seed + simulate: seed **4** once, 7 × `random.randint(8, 30)` → `demand_ex21 == [15, 17, 11, 20, 23, 12, 10]`.
- **2.2** Kevin's bug (fix-it): Kevin re-seeds INSIDE the loop, so all 7 "random" days are identical. Given buggy code producing `[22, 22, 22, 22, 22, 22, 22]` (seed 9 drawn each iteration), fix = seed once before the loop → `fixed_ex22 == [22, 27, 19, 16, 12, 13, 29]`. Prompt states the SYMPTOM only ("every day looks identical — that's not a projection, that's a photocopy"). Include the red-error-pause teach line in this section's md (dict-free lab, but the loop edit can crash).
- **2.3** `random.choice` raffle: seed **12**, draw 4 flyer-zone picks from `["Nord", "Sued", "Hafen", "Altstadt"]` → `raffle_ex23 == ['Altstadt', 'Hafen', 'Hafen', 'Sued']`.

*Boss (ex40):* the projection memo — seed **2**, simulate 5 days `random.randint(10, 26)`, report `statistics.mean` → `boss_ex40` → **14.2**. (Draws are `[11, 12, 12, 21, 15]`.)

*Trace radio (ungraded, "(trace — predict first)"):* what prints — `import math` then `print(math.floor(-2.5))` → options -2 / -3 / error → reveal -3.

*MCQ (`answer_ex50`):* why seed a simulation? a) faster b) reproducible results c) more random d) required by numpy → **"b"**.

- [ ] **Step 2: Solution notebook in the private repo** (fill answers, delete hint accordions, header "Solutions — Episode 6", wrap-up → "compare, don't memorize"). Verify check cells byte-identical to the lab's (`grep`-compare or diff the check cell sources).

- [ ] **Step 3: Launcher page** — rewrite `tutorials/tut_06_modules.qmd` from the `tut_04` pattern: intro paragraph (episode blurb), two buttons (self-hosted WASM `https://beyondsimulations.github.io/Introduction-to-Python/notebooks/nb_06_lab_diligence/` + molab), the verbatim persistence copy, dormant commented Solutions link to `notebooks/sol_06_lab_diligence/`.

- [ ] **Step 4: Validate, render, commit both repos**

```bash
uv run python helpers/validate_notebooks.py notebooks/nb_06_lab_diligence.py
quarto render tutorials/tut_06_modules.qmd && git checkout -- _repo-md/
git add notebooks/nb_06_lab_diligence.py tutorials/tut_06_modules.qmd
git commit -m "feat: episode 6 lab (modules + random) + launcher"
# private repo
cd ../Introduction-to-Python-checkpoints
git add solutions/sol_06_lab_diligence.py && git commit -m "feat: episode 6 solutions"
```

---

### Task 6: `lec_06` full rewrite (CP-session deck, Part-II opener)

**Goal:** The Session VI deck: CP3 procedure slide, the "Part II: rules change" slide, two blocks (imports/stdlib, random), QR breaks, lab handoff.

**Files:**
- Rewrite: `lectures/lec_06_modules.qmd`
- Delete: `lectures/lec_06_new_module.py`, `lectures/supplementary/lec_06/` (orphaned by the rewrite), root-level `lectures/secret_message.csv` if present
- Modify: `docs/side-quest-backlog.md` (cut material)
- Template: `lectures/lec_05_errors.qmd` (CP-session skeleton)

**Acceptance Criteria:**
- [ ] CP-session skeleton per conventions: title → 📋 CP3 slide → cold open → Part-II-rules slide → Block 1 → QR a → Block 2 → QR b → lab handoff → wrap-up → Literature
- [ ] No warm-up section; ≤1 Kevin joke per section; predict pairs spoiler-free
- [ ] Cut material logged in the backlog: regex section (side-quest candidate), os/csv modules (Session X preview), creating own module files (Session X — needs a real filesystem), package installing/venvs (Session X, `uv`)
- [ ] `quarto render lectures/lec_06_modules.qmd` succeeds; `git checkout -- _repo-md/` afterwards

**Verify:** render passes; `grep -ci "copilot" lectures/lec_06_modules.qmd` → 0.

**Steps:**

- [ ] **Step 1: Write the deck**

- **📋 CP3 slide:** copy lec_05's CP2 procedure slide; retitle "Checkpoint 3 — Sessions I–V"; same mechanics (unlisted URL announced in class, ~40 min, download `.py`, Moodle upload).
- **Cold open:** the investor walks in unannounced. Due-diligence week begins. On the whiteboard: "Why is everything built from scratch?"
- **Part II rules slide** (`## Part II: the rules change`): AI is now allowed and taught · disclosure habit (one line per submission) · the chatbot switches to full-answers-on-request · link/QR to `general/ai-tools.qmd`. One restrained line: "You spent five sessions learning to think without a copilot. Now you get one — and you'll be the pilot."
- **Block 1 — "Don't build it, import it":** what a module is; `import math` (ceil for 130 pastry boxes of 48 → 3 crates); `from statistics import mean, median` (ratings `[4.5, 4.8, 3.9, 5.0, 4.2]` → median 4.5); aliases (`import statistics as stats`); `dir()`/`help()` one slide. **Predict pair:** question slide `import math` + `print(math.floor(-2.5))` (no spoiler comments) → executable answer slide: `-3`, "floor goes DOWN, not toward zero."
- **⚡ QR a** → `ex_06_a` (exact slide form per conventions; PNG from Task 4).
- **Block 2 — "Rehearsing luck":** `random.random/randint/choice/shuffle`; the reproducibility problem (investor: "run it again" — different numbers!); `random.seed` fixes it; demo: seed(7), 5 × randint(1, 20) → `[11, 5, 13, 2, 3]` twice in a row. **Predict pair:** two consecutive seeded runs — same or different? → answer: identical, that's the point.
- **⚡ QR b** → `ex_06_b`.
- **Lab handoff** (tut_06 URL) · **Wrap-up** (3 takeaways + teaser: "Next episode: one array to rule a thousand orders") · **Literature** (keep the existing section, add a line for the AI-tools page).

- [ ] **Step 2: Backlog entries** — append the four cut items under "Material cut from lecture decks (Plan 3 rewrites)".

- [ ] **Step 3: Delete orphans, render, commit**

```bash
git rm lectures/lec_06_new_module.py
git rm -r lectures/supplementary/lec_06
quarto render lectures/lec_06_modules.qmd && git checkout -- _repo-md/
git add lectures/lec_06_modules.qmd docs/side-quest-backlog.md
git commit -m "feat: lec 06 rewrite — Part II opener, imports + random, CP3 day"
```

---

### Task 7: Session VII in-lecture exercises (`ex_07_a/b/c`)

**Goal:** Three QR sandboxes for the three NumPy blocks.

**Files:**
- Create: `notebooks/exercises/ex_07_a.py`, `ex_07_b.py`, `ex_07_c.py`
- Modify: `helpers/make_qr.py` (+3), regenerate PNGs

**Acceptance Criteria:**
- [ ] Values match the freshness ledger; NumPy answers checked with rounding-tolerant comparisons (see below)
- [ ] Validator ok on all three; three new PNGs exist

**Steps:**

- [ ] **Step 1: `ex_07_a` — vectorized arithmetic (block 1)**

Net prices `np.array([8.0, 11.0, 14.0])`, add 19% VAT in ONE expression (no loop!). Graded: `gross_exa`. Check must accept an ndarray:

```python
_expected = [9.52, 13.09, 16.66]
_ok = (
    gross_exa is not None
    and hasattr(gross_exa, "__len__")
    and len(gross_exa) == 3
    and [round(float(_v), 2) for _v in gross_exa] == _expected
)
```

- [ ] **Step 2: `ex_07_b` — boolean masks (block 2)**

Delivery times `np.array([31, 22, 47, 15, 36, 28, 51, 19, 40])`; deliveries over 38 min are "late". Graded: `late_count_exb == 3` (as `int(...)`) and `late_mean_exb == 46.0` (as `float(...)`, checked with `round(_, 2)`). Teach line: `mask.sum()` counts Trues. Hint 2: `late_count_exb = int((times > ___).sum())`.

- [ ] **Step 3: `ex_07_c` — 2D + axis (block 3)**

`sales_exc = np.array([[7, 12, 5], [9, 4, 14], [11, 8, 6], [3, 10, 13]])` (4 days × 3 zones). Graded: `zone_totals_exc` → `[30, 34, 38]` (list-tolerant check like ex_07_a's) and `best_zone_exc = int(...argmax())` → **2**. Teach line: axis=0 collapses DOWN the rows → one number per column/zone.

- [ ] **Step 4: QRs, validate, commit** (same motion as Task 4, commit `feat: session VII in-lecture exercises (numpy)`).

---

### Task 8: Episode 7 lab + solutions + launcher (`nb_07` / `sol_07` / `tut_07`)

**Goal:** The NumPy lab, private solutions, launcher rewrite.

**Files:**
- Create: `notebooks/nb_07_lab_metrics.py`
- Create (PRIVATE): `solutions/sol_07_lab_metrics.py`
- Rewrite: `tutorials/tut_07_scientific.qmd` (launcher)

**Acceptance Criteria:**
- [ ] 8 graded cores + trace radio + MCQ = "X/9" progress; values per ledger, ndarray-tolerant checks (Task 7 pattern)
- [ ] Kevin bug = axis mixup (logic, terminating); red-error-pause teach line present (indexing can crash)
- [ ] Solutions byte-identical checks; launcher with dormant Solutions link

**Steps:**

- [ ] **Step 1: Lab content — "Episode 7: The Numbers Deck"**

Intro: the investor wants a metrics one-pager. Kevin's 40-tab spreadsheet is disqualified. Data inline (no files yet — that's next episode).

*Section 1 — arrays:*
- **1.1** build `np.array` from a Python list of 12 order values (implementer picks values; record in ledger comment) → graded `n_orders_ex11 = int(orders.size)` → **12**.
- **1.2** vectorized discount: net prices `np.array([6.0, 9.0, 12.0, 18.0])` × 0.9 → `sale_ex12` → `[5.4, 8.1, 10.8, 16.2]`.
- **1.3** `np.arange(1, 15)` days → graded `days_sum_ex13 = int(days.sum())` → **105** (verify: sum 1..14 = 105).

*Section 2 — masks:*
- **2.1** delivery times `np.array([24, 39, 55, 17, 31, 46, 20, 60, 35, 42])`, over 50 = "critical" → `critical_count_ex21` → **2**, `critical_mean_ex22` → **57.5** (two separate cores 2.1/2.2).
- **2.3 Kevin's bug (fix-it):** the 7×4 matrix below; Kevin reports "per-zone totals" computed with `axis=1` — symptom: "the investor asked for 4 zone numbers, Kevin's memo has 7." Fix → `zone_totals_ex23 == [141, 109, 100, 82]`.

*Section 3 — 2D:*
- **3.1** matrix `week = np.array([[18, 7, 12, 9], [22, 11, 8, 14], [15, 19, 10, 6], [25, 13, 17, 8], [9, 21, 14, 12], [24, 16, 20, 18], [28, 22, 19, 15]])` (7 days × zones `["Nord", "Sued", "Hafen", "Altstadt"]`), busiest day total via `axis=1` → `best_day_total_ex31 = int(week.sum(axis=1).max())` → **84**.
- **Boss (ex40):** which ZONE wins the week? `best_zone_ex40 = zones[int(week.sum(axis=0).argmax())]` → **"Nord"** (totals [141, 109, 100, 82] — reuse of 2.3's fixed numbers is deliberate spaced repetition inside the same lab).

*Trace radio:* `[1, 2, 3] * 2` vs `np.array([1, 2, 3]) * 2` — what does the FIRST print? (list repetition vs vectorized multiply reveal).

*MCQ (`answer_ex50`):* `(times > 40).sum()` computes… a) sum of all times b) how many times exceed 40 c) the largest time d) error → **"b"**.

- [ ] **Step 2–4:** solutions (private), launcher rewrite from `tut_04` pattern (URL `.../notebooks/nb_07_lab_metrics/`), validate, render, commit both repos (`feat: episode 7 lab (numpy) + launcher`).

---

### Task 9: `lec_07` full rewrite (regular deck, warm-up returns)

**Goal:** The NumPy deck: warm-up (recap Session VI), three blocks, three QR breaks.

**Files:**
- Rewrite: `lectures/lec_07_scientific.qmd`
- Modify: `docs/side-quest-backlog.md`
- Template: `lectures/lec_04_dimensions.qmd` (regular skeleton + warm-up)

**Acceptance Criteria:**
- [ ] Regular skeleton: title → cold open → 🔥 warm-up (3 Q/A vote pairs, prose-only answers) → Block 1 → QR a → Block 2 → QR b → Block 3 → QR c → lab handoff → wrap-up → Literature
- [ ] Cut logged: fancy indexing, dtype char codes + bits/precision section, concatenate/hstack/vstack, heterogeneous arrays (one-line mention max)
- [ ] Render passes

**Steps:**

- [ ] **Step 1: Warm-up (recap VI)**

```markdown
# 🔥 Warm-up {.exercise-slide}

## Question 1
After `from math import ceil` — which line works?
a) `math.ceil(3.2)` · b) `ceil(3.2)` · c) both

## Answer 1
**b)** — `from math import ceil` binds only the NAME `ceil`; `math` itself was never imported.

## Question 2
`random.seed(42)` … then the same three `randint` calls, twice. Second run gives…
a) the same three numbers · b) different numbers · c) an error

## Answer 2
**a)** — that is the entire job of a seed: reproducible randomness.

## Question 3
`statistics.median([9, 2, 5])` returns…
a) 2 · b) 5 · c) an error — the list is not sorted

## Answer 3
**b)** — `median` sorts internally; 5 is the middle value.
```

- [ ] **Step 2: Blocks**

- **Cold open:** the numbers deck is due. One row per order × a thousand orders. "We need a bigger boat than a list."
- **Block 1 — "A thousand orders at once":** why NumPy (vectorized, one operation on all elements); `np.array` from list; `.shape`/`.dtype`/`.size`; `np.arange`/`np.linspace`; the VAT demo `np.array([12.0, 9.0, 15.0]) * 1.19` → `[14.28, 10.71, 17.85]` vs the loop version. **Predict pair:** `[1, 2, 3] * 2` (plain list!) → answer slide runs it: `[1, 2, 3, 1, 2, 3]` — "lists repeat; arrays compute. That's why we're here."
- **⚡ QR a** → ex_07_a.
- **Block 2 — "Asking questions of data":** comparisons make boolean arrays; masks filter (`times[times > 30]`); counting via `.sum()` on a mask; demo on delivery times `[25, 41, 18, 33, 52, 29, 44, 12]` → 4 late, late mean 42.5. **Predict pair:** `(np.array([1, 5, 3]) > 2).sum()` → 2? True? array? → runs: `2`.
- **⚡ QR b** → ex_07_b → BREAK.
- **Block 3 — "The two-week matrix":** 2D arrays (days × zones); `axis=0` vs `axis=1` (the classic confusion — draw the collapse direction); demo matrix `[[14, 9, 11, 6], [12, 15, 8, 9], [20, 13, 16, 11]]` → per-zone `[46, 37, 35, 26]`, per-day `[40, 44, 60]`; `argmax` finds WHERE.
- **⚡ QR c** → ex_07_c → lab handoff (tut_07) → wrap-up (teaser: "Next: the investor opens a data room — and Kevin lets an AI write his pandas") → Literature.

- [ ] **Step 3: Backlog + render + commit** (`feat: lec 07 rewrite — numpy in three blocks`).

---

### Task 10: Grader hardening — NumPy/pandas value coercion (PRIVATE repo)

**Goal:** The grader survives and correctly grades submissions whose answers are NumPy scalars/arrays or pandas Series (inevitable in CP4/5 even when prompts say "store a plain number").

**Files (all in `/Users/vlcek/development/lectures/Introduction-to-Python-checkpoints`):**
- Modify: `grader/runner.py` (`_coerce`)
- Modify: `pyproject.toml` (`uv add numpy pandas` — grader env must run submissions that import them)
- Test: `tests/test_grader.py`

**Acceptance Criteria:**
- [ ] np scalar → Python scalar; np array → list (recursively coerced); tuple → list; pd.Series → dict (str keys, coerced values); pd.DataFrame → repr string; containers coerced recursively
- [ ] Works when numpy/pandas are absent from a submission (imports guarded)
- [ ] All existing tests still pass

**Verify:** `cd ../Introduction-to-Python-checkpoints && uv run pytest -q` → all pass (25 existing + 5 new).

**Steps:**

- [ ] **Step 1: Write the failing tests**

```python
def test_numpy_scalar_and_array_coerced(tmp_path):
    sub = tmp_path / "np_sub.py"
    sub.write_text(
        "import numpy as np\n"
        "count_t1 = (np.array([1, 5, 9]) > 2).sum()\n"   # np.int64
        "mean_t1 = np.array([2.0, 4.0]).mean()\n"          # np.float64
        "totals_t1 = np.array([3, 4]).tolist() + [np.int64(5)]\n"  # np inside list
    )
    tasks = {
        "t1": {
            "points": 2,
            "names": ["count_t1", "mean_t1", "totals_t1"],
            "test": lambda d: d.get("count_t1") == 2
            and d.get("mean_t1") == 3.0
            and d.get("totals_t1") == [3, 4, 5],
        }
    }
    result = grade_submission(sub, tasks)
    assert result.status == "graded"
    assert result.total == 2


def test_pandas_series_coerced_to_dict(tmp_path):
    sub = tmp_path / "pd_sub.py"
    sub.write_text(
        "import pandas as pd\n"
        "df = pd.DataFrame({'zone': ['a', 'b', 'a'], 'v': [1.5, 2.0, 2.5]})\n"
        "by_zone_t1 = df.groupby('zone')['v'].sum()\n"  # a Series, not a dict
    )
    tasks = {
        "t1": {
            "points": 2,
            "names": ["by_zone_t1"],
            "test": lambda d: d.get("by_zone_t1") == {"a": 4.0, "b": 2.0},
        }
    }
    result = grade_submission(sub, tasks)
    assert result.status == "graded"
    assert result.total == 2


def test_tuple_answer_becomes_list(tmp_path):
    sub = tmp_path / "tup_sub.py"
    sub.write_text("pair_t1 = (3, 4)\n")
    tasks = {
        "t1": {"points": 2, "names": ["pair_t1"], "test": lambda d: d.get("pair_t1") == [3, 4]}
    }
    result = grade_submission(sub, tasks)
    assert result.total == 2
```

Plus: `test_dataframe_becomes_repr` (a DataFrame answer must not crash the runner — coerces to a string, task scores 0 unless the test expects a string) and `test_numpy_absent_ok` (a plain submission still grades — guarded imports).

- [ ] **Step 2: Implement `_coerce` (replace the existing one in `grader/runner.py`)**

```python
def _coerce(value):
    # JSON carries only scalars/lists/dicts. Submissions in the NumPy/pandas era
    # routinely hold np scalars, arrays, and Series — normalize them BEFORE the
    # isinstance ladder, then recurse into containers so nested np values can't
    # crash json.dumps. Imports are guarded: a plain-Python submission must not
    # require numpy/pandas to grade.
    try:
        import numpy as np

        if isinstance(value, np.generic):
            value = value.item()
        elif isinstance(value, np.ndarray):
            value = value.tolist()
    except ImportError:
        pass
    try:
        import pandas as pd

        if isinstance(value, pd.Series):
            value = {str(k): v for k, v in value.to_dict().items()}
        elif isinstance(value, pd.DataFrame):
            return repr(value)
    except ImportError:
        pass
    if isinstance(value, (list, tuple)):
        return [_coerce(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _coerce(v) for k, v in value.items()}
    if isinstance(value, (int, float, str, bool, type(None))):
        return value
    return repr(value)
```

Delete the now-unused `_SCALAR` constant if nothing else references it.

- [ ] **Step 3: Run, commit**

```bash
uv add numpy pandas
uv run pytest -q
git add pyproject.toml uv.lock grader/runner.py tests/test_grader.py
git commit -m "feat: grader coerces numpy/pandas values for the Part-II checkpoints"
```

---

### Task 11: CP4 — Sessions VI–VII (PRIVATE repo)

**Goal:** The fourth checkpoint: board-review notebook + hidden reference tests, AI-allowed design, values per the freshness ledger.

**Files (PRIVATE repo):**
- Create: `checkpoints/cp4/board_review.py` (copy structural skeleton from `checkpoints/cp3/`)
- Create: `checkpoints/cp4/reference_tests.py`
- Test: extend `tests/test_checkpoints.py` (good/zero fixtures like cp1–3 have)

**Acceptance Criteria:**
- [ ] 6 tasks × 2 pts: 4 live-checked (hash) + 2 MCQ (neutral "recorded"); score cell "X/8 — provisional (plus 2 MCQs, graded only at final grading)"
- [ ] Every value/answer distinct from the freshness ledger's lab/exercise rows; prompts symptom-only; hashes per-task salted (`task="cp4.tN"`); expr keys task-prefixed
- [ ] Live checks and reference tests apply IDENTICAL leniency (`round(_, 2)` for floats; exact for int lists; strip+lower via the hash helper for strings)
- [ ] Reference tests import numpy (Task 10 landed); fixture notebooks grade 12/12 and 0

**Verify:** `cd ../Introduction-to-Python-checkpoints && uv run pytest -q` → all pass.

**Steps:**

- [ ] **Step 1: Tasks (exact content)**

Intro md: "Board review 4 — AI tools ARE allowed today. What's being graded is whether YOU can tell right from wrong output."

- **t1 (write a function, 2 pts):** couriers pack crates; a partial crate still ships as a full crate. Write `crates_t1(items, per_crate)`. Live check: evaluates `crates_t1(29, 12)` and hash-compares (`== 3`). Hidden probes (exprs): `{"cp4_t1_a": "crates_t1(53, 12)", "cp4_t1_b": "crates_t1(48, 12)", "cp4_t1_c": "crates_t1(1, 12)"}` → 5 / **4 (exact-multiple boundary)** / 1.
- **t2 (numpy compute):** given `waits_t2 = np.array([26, 52, 33, 47, 18, 39, 61, 24, 45, 31])` — orders slower than 38 min are "slow". Store `slow_count_t2` (how many) and `slow_mean_t2` (their mean). → **5** and **48.8**. Prompt: "store plain Python numbers — `int(...)` / `float(...)`" (grader coerces anyway post-Task-10).
- **t3 (fix a bug):** 7×4 revenue matrix `revenue_t3` (rows = days, columns = zones — the notebook says so) with Kevin's line `zone_totals_t3 = revenue_t3.sum(axis=1).tolist()`. Symptom only: "the investor asked for four zone totals; Kevin's report has seven numbers." Matrix: `[[210, 180, 150, 240], [190, 220, 170, 200], [230, 160, 180, 250], [205, 175, 190, 215], [220, 195, 160, 230], [240, 210, 200, 260], [250, 230, 210, 270]]` → fixed answer `[1545, 1370, 1260, 1665]`.
- **t4 (seeded simulation):** restock draw — seed **23** exactly once, then five draws of `random.randint(2, 9)` into `restock_t4`. → `[6, 3, 2, 6, 8]`.
- **t5 (MCQ, `answer_t5`):** `prices[prices > 10]` evaluates to… a) an array of True/False b) an array of the values above 10 c) the positions of those values d) how many values are above 10 → **"b"**. Neutral "answer recorded".
- **t6 (MCQ, `answer_t6`):** after `from statistics import median`, the median of `xs` is computed by… a) `statistics.median(xs)` b) `median(xs)` c) `xs.median()` d) `import median` first → **"b"**. Neutral "answer recorded".

- [ ] **Step 2: Reference tests** — mirror cp3's structure; leniency comments verbatim pattern: `# leniency matches the live hash check (round to 2) — live and final must agree`. Tests: t1 via the three exprs; t2 `round(d.get("slow_mean_t2", 0), 2) == 48.8 and d.get("slow_count_t2") == 5`; t3 exact int list; t4 exact list; t5/t6 strip+lower string compare.

- [ ] **Step 3: Hashes** — compute every live-check literal with `uv run python -c "from grader.hashcheck import expected_hash; print(expected_hash(..., task='cp4.tN'))"`. Never hash MCQ answers into visible ✅ checks (neutral ack only).

- [ ] **Step 4: Fixtures + tests** (perfect submission → 12; empty → 0; np-typed submission → still 12, exercising Task 10), run pytest, commit `feat: checkpoint 4 (modules, random, numpy)`.

---

### Task 12: Part-II dataset — `notebooks/public/orders.csv` + generator

**Goal:** One canonical, deterministic, committed dataset for Sessions VIII–IX.

**Files:**
- Create: `helpers/make_orders_csv.py`
- Create (generated): `notebooks/public/orders.csv`

**Acceptance Criteria:**
- [ ] Re-running the generator reproduces the committed file byte-identically
- [ ] `total_eur` is exactly `items × unit_price` (2-decimal safe); unit prices differ from every price in the freshness ledger and from Part I's canon
- [ ] 60–110 rows; all four zones and all four dishes occur

**Verify:** `uv run python helpers/make_orders_csv.py && git diff --exit-code notebooks/public/orders.csv && echo STABLE` → STABLE.

**Steps:**

- [ ] **Step 1: Write the generator**

```python
"""Generate the canonical Part-II dataset (notebooks/public/orders.csv).

Deterministic (seeded): re-running must reproduce the committed file exactly.
Labs nb_08/nb_09 hard-code check values computed FROM this file — never edit
the CSV by hand and never change the seed without updating every dependent
check (see the freshness ledger in the Plan 3 document).
"""
import csv
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "notebooks" / "public" / "orders.csv"
ZONES = ["Nord", "Sued", "Hafen", "Altstadt"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DISHES = {"Bao Box": 8.40, "Falafel Wrap": 7.60, "Pad Thai": 10.20, "Miso Ramen": 11.90}


def main() -> None:
    random.seed(2026)
    rows = []
    order_id = 1001
    for day in range(1, 15):  # two weeks of trading
        for _ in range(random.randint(4, 8)):
            dish = random.choice(list(DISHES))
            items = random.randint(1, 3)
            rows.append(
                {
                    "order_id": order_id,
                    "day": day,
                    "weekday": WEEKDAYS[(day - 1) % 7],
                    "zone": random.choice(ZONES),
                    "dish": dish,
                    "items": items,
                    "total_eur": round(items * DISHES[dish], 2),
                    "delivery_min": random.randint(12, 58),
                    "rating": round(random.uniform(3.0, 5.0), 1),
                }
            )
            order_id += 1
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} orders -> {OUT}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Generate, record the key aggregates**

```bash
uv run python helpers/make_orders_csv.py
uv run python - <<'PY'
import pandas as pd
df = pd.read_csv("notebooks/public/orders.csv")
print("rows:", len(df))
print("revenue total:", round(df["total_eur"].sum(), 2))
print("mean order:", round(df["total_eur"].mean(), 2))
print("zone totals:", df.groupby("zone")["total_eur"].sum().round(2).to_dict())
print("max delivery:", int(df["delivery_min"].max()))
PY
```

Paste the output as a comment block at the bottom of `helpers/make_orders_csv.py` (the downstream tasks' source of truth, alongside their own re-computation).

- [ ] **Step 3: Commit** `feat: canonical Part-II orders dataset + seeded generator`.

---

### Task 13: Session VIII in-lecture exercises (`ex_08_a/b`)

**Goal:** Two QR sandboxes: AI-craft (fix hallucinated code) and pandas basics. Both use small INLINE DataFrames (exercises never depend on `public/`).

**Files:**
- Create: `notebooks/exercises/ex_08_a.py`, `ex_08_b.py`
- Modify: `helpers/make_qr.py` (+2), regenerate PNGs

**Steps:**

- [ ] **Step 1: `ex_08_a` — Kevin's AI code (block 1)**

Teach cell: "AI wrote this. Two things are wrong — one method doesn't exist, one comparison quietly returns nothing. Fix both." Given (as a commented-out buggy block plus the raw df):

```python
_df = pd.DataFrame({"zone": ["Nord", "Nord", "Sued", "Nord", "Hafen"],
                    "total_eur": [12.40, 8.90, 15.10, 22.20, 9.60]})
# Kevin's AI draft (broken — fix it in your own code below):
#   nord = _df[_df["zone"] == "nord"]      # quietly empty… why?
#   mean_exa = nord["total_eur"].summarize()   # AttributeError… why?
mean_exa = None  # YOUR CODE BELOW
```

Expected: filter `== "Nord"` (case!), then `.mean()` → **14.5** (`(12.40 + 8.90 + 22.20) / 3`). Check: `round(float(mean_exa), 2) == 14.5`. Hint 1: "string comparison is case-sensitive; and does pandas really have `summarize`? Check with the docs — or ask an AI and VERIFY."

- [ ] **Step 2: `ex_08_b` — filter + count (block 2)**

Inline df: `items = [1, 2, 1, 3, 1, 2]`, `total_eur = [11.20, 18.40, 6.80, 24.00, 9.50, 14.60]` (+ any zone column). Graded: `bulk_count_exb = int((df["items"] >= 2).sum())` → **3** and `bulk_revenue_exb = float(df[df["items"] >= 2]["total_eur"].sum())` → **57.0**.

- [ ] **Step 3: QRs, validate, commit** (`feat: session VIII in-lecture exercises (AI craft, pandas)`).

---

### Task 14: Episode 8 lab + solutions + launcher (`nb_08` / `sol_08` / `tut_08`)

**Goal:** The heavy data-wrangling lab on the real dataset (spec: "heavy data-wrangling practice"), private solutions, launcher.

**Files:**
- Create: `notebooks/nb_08_lab_dataroom.py`
- Create (PRIVATE): `solutions/sol_08_lab_dataroom.py`
- Rewrite: `tutorials/tut_08_pandas.qmd` (launcher)

**Acceptance Criteria:**
- [ ] Loads `orders.csv` via the Task-1 loader cell (copied verbatim from the conventions doc)
- [ ] 9 graded cores + trace radio + MCQ = "X/10"; every check literal COMPUTED from the committed CSV (show the computation in a `# ledger:` comment at the top of the notebook) and cross-checked against the freshness ledger for collisions
- [ ] Kevin bug: a `KeyError` from a wrong column name — red-error-pause teach line REQUIRED
- [ ] WASM export of this notebook loads the CSV (manual browser spot-check, same motion as Task 1 Step 3)

**Steps:**

- [ ] **Step 1: Lab content — "Episode 8: The Data Room"**

Intro: MunchCorp went to the press with "data-driven growth". The investor slides a USB stick across the table: "Every order, two weeks. Impress me." Also: Kevin has discovered AI and must be supervised.

Cores (values marked ⟨csv⟩ are computed from the committed file by the implementer):
- **1.1** `rows_ex11 = int(len(orders))` → ⟨csv⟩.
- **1.2** `orders.head()` shown; graded `n_cols_ex12 = int(orders.shape[1])` → **9**.
- **1.3** `revenue_ex13 = float(orders["total_eur"].sum())` → ⟨csv⟩ (check with `round(_, 2)`).
- **2.1** filter one zone: `nord_count_ex21 = int(len(orders[orders["zone"] == "Nord"]))` → ⟨csv⟩.
- **2.2** combined condition (zone == "Sued") & (items >= 2): count → ⟨csv⟩.
- **2.3 Kevin's bug (fix-it):** Kevin's cell reads `orders["Zone"]` → `KeyError: 'Zone'` — the lab's designated red-error moment; md explains the pause-and-recover behavior. Fix → lowercase column; graded `hafen_revenue_ex23 = float(...)` → ⟨csv⟩.
- **3.1** new column: `orders["eur_per_item"] = orders["total_eur"] / orders["items"]`; graded `max_per_item_ex31 = float(orders["eur_per_item"].max().round(2))` → ⟨csv⟩ (equals the highest unit price, 11.90 — verify from file; if so, note the nice reveal: it's the Miso Ramen).
- **3.2** groupby: `by_zone_ex32 = orders.groupby("zone")["total_eur"].sum().round(2).to_dict()` → ⟨csv⟩ dict.
- **Boss (ex40):** the investor's question — "which zone has the highest AVERAGE order value?" `best_avg_zone_ex40 = orders.groupby("zone")["total_eur"].mean().idxmax()` → ⟨csv⟩ string.

*Trace radio:* `orders[orders["items"] == 3].shape` vs `orders["items"] == 3` — which one is the True/False column? *MCQ (`answer_ex50`):* `.describe()` shows… → count/mean/std/min/max quartiles → letter per option order.

- [ ] **Step 2–4:** solutions (private), launcher (URL `.../notebooks/nb_08_lab_dataroom/`), validate + WASM spot-check + render + commit both repos (`feat: episode 8 lab (pandas on orders.csv) + launcher`).

---

### Task 15: `lec_08` full rewrite (CP-session deck: AI craft + pandas)

**Goal:** The Session VIII deck: CP4 slide, AI-craft block, pandas block.

**Files:**
- Rewrite: `lectures/lec_08_pandas.qmd`
- Delete: `lectures/supplementary/lec_08/` (employees.csv/xlsx, temperatures.xlsx, generator — orphaned)
- Modify: `docs/side-quest-backlog.md`

**Acceptance Criteria:**
- [ ] CP-session skeleton (CP4 procedure slide; no warm-up); NO external embeds (the old deck's Giphy iframe and Unsplash background go away)
- [ ] Old AI section fully replaced: no LLM-internals slides, no Copilot signup — AI *craft* instead
- [ ] Cut logged: merge/join/concat, Excel I/O, melt/wide-long, LLM-internals slides, Copilot section, `iloc`/`loc` deep-dive (mention `loc` once)
- [ ] Fixes the old deck's title metadata ("Lecture VII" → correct numbering per new deck style)
- [ ] Render passes; repo-wide `grep -ri copilot lectures/` hits only... nothing (old content gone)

**Steps:**

- [ ] **Step 1: Write the deck**

- **📋 CP4 slide** (copy CP3 slide from lec_06, retitle "Checkpoint 4 — Sessions VI–VII", add one line: "AI tools allowed — being able to VERIFY output is the skill being graded").
- **Cold open:** MunchCorp's press release brags "data-driven". The investor: "Their data is a pie chart. Yours will be better." Meanwhile Kevin proudly presents code an AI wrote for him. It does not run.
- **Block 1 — "AI joins the team — professionally":**
  - Prompting that works: give context (what the data is), give constraints (what exactly you want back), iterate.
  - The verify workflow: **read it → run it → test it on a case you know the answer to.**
  - Hallucinated APIs: **predict pair** — Kevin's line `orders.summarize()` (question slide, no spoilers) → answer slide runs `df.summarize()` on a tiny frame → `AttributeError`; the real one is `.describe()`. Teach line: "An AI that sounds sure is not the same as an API that exists."
  - Disclosure: the course rule (one line per submission); why it protects THEM.
  - When NOT to use AI: recall the Part-I muscle — "you could read that traceback yourself since Episode 5."
- **⚡ QR a** → ex_08_a.
- **Block 2 — "The DataFrame":** what pandas adds over NumPy (named columns, mixed types); `pd.DataFrame` from a dict; reading a real file (`read_csv` — show the lab's loader in one slide, explain the browser twist in ONE sentence); `.head()`/`.info()`/`.describe()`; selecting a column; filtering rows (`df[df["zone"] == "Nord"]` — case-sensitive!); adding a column; `sort_values`; `groupby` in one teaser slide ("the lab does the heavy lifting"). **Predict pair:** filter with `== "nord"` (lowercase) → runs: empty frame, no error — "pandas won't warn you; YOU verify."
- **⚡ QR b** → ex_08_b → lab handoff (tut_08) → wrap-up (teaser: "Next: charts the investor can't argue with") → Literature.

- [ ] **Step 2: Delete orphans, backlog, render, commit**

```bash
git rm -r lectures/supplementary/lec_08
quarto render lectures/lec_08_pandas.qmd && git checkout -- _repo-md/
git add lectures/lec_08_pandas.qmd docs/side-quest-backlog.md
git commit -m "feat: lec 08 rewrite — AI craft + pandas, CP4 day"
```

---

### Task 16: Session IX in-lecture exercises (`ex_09_a/b/c`)

**Goal:** Three QR sandboxes for the plotting blocks. Charts render but are NOT graded — graded names are the computed values behind them.

**Files:**
- Create: `notebooks/exercises/ex_09_a.py`, `ex_09_b.py`, `ex_09_c.py`
- Modify: `helpers/make_qr.py` (+3), regenerate PNGs

**Steps:**

- [ ] **Step 1: `ex_09_a` — first line chart (block 1)**

Inline daily revenues `[142.50, 168.20, 155.90, 201.40, 189.60, 246.80, 232.10]` (Mon–Sun). Student plots the line (`plt.plot`, labels, title; cell returns `plt.gca()` — teach line: "in marimo the last expression displays; that's your figure"). Graded: `total_exa = float(sum(revenues))` → **1336.5** and `best_day_exa` = day NUMBER of the max (1-based) → **6**. Check: chart not graded; both names checked numerically.

- [ ] **Step 2: `ex_09_b` — bar chart (block 2)**

Inline zone totals: `zones = ["Nord", "Sued", "Hafen", "Altstadt"]`, `totals = [412.60, 268.40, 305.90, 351.20]`. Plot `plt.bar(zones, totals)`; graded `best_zone_exb` → **"Nord"** (strip+lower-tolerant string check).

- [ ] **Step 3: `ex_09_c` — the honest y-axis (block 3)**

Given an "AI-generated" snippet plotting weekly revenue `[50, 52, 53, 55]` (k€) with `plt.ylim(49, 56)` — looks like a rocket. Task: compute the REAL growth `growth_exc = (55 - 50) / 50 * 100` → **10.0**, and fix the chart to start the axis at 0. Graded: `growth_exc` (float, round 2). Closing md: "10% growth is good news. It doesn't need a costume."

- [ ] **Step 4: QRs, validate, commit** (`feat: session IX in-lecture exercises (plotting, honest charts)`).

---

### Task 17: Episode 9 lab + solutions + launcher (`nb_09` / `sol_09` / `tut_09`)

**Goal:** The pitch-deck lab: charts from `orders.csv`, graded via the numbers behind them.

**Files:**
- Create: `notebooks/nb_09_lab_pitch.py`
- Create (PRIVATE): `solutions/sol_09_lab_pitch.py`
- Rewrite: `tutorials/tut_09_plotting.qmd` (launcher)

**Acceptance Criteria:**
- [ ] Loader cell verbatim from conventions; 7 graded cores + trace radio + MCQ = "X/8"; ⟨csv⟩ literals computed from the committed file with a `# ledger:` comment
- [ ] Every chart cell returns a matplotlib object as its last expression (marimo display); NO `plt.show()`
- [ ] Solutions + launcher per the standard motion

**Steps:**

- [ ] **Step 1: Lab content — "Episode 9: The Pitch Deck"**

Intro: pitch meeting Friday. The investor's one instruction: "Charts I can't argue with." Cores:
- **1.1** daily revenue: `daily = orders.groupby("day")["total_eur"].sum()`; graded `best_day_ex11 = int(daily.idxmax())` → ⟨csv⟩; line chart of `daily` (ungraded).
- **1.2** chart anatomy: add xlabel/ylabel/title to 1.1's chart (ungraded aesthetics); graded `days_ex12 = int(len(daily))` → **14**.
- **2.1** zone bar chart: `by_zone = orders.groupby("zone")["total_eur"].sum().round(2)`; graded `by_zone_ex21 = by_zone.to_dict()` → ⟨csv⟩ (same dict as nb_08's 3.2 — deliberate cross-episode repetition, note it in the md: "you computed this in the data room; now it becomes a picture").
- **2.2** histogram of `total_eur`; graded `over_20_ex22 = int((orders["total_eur"] > 20).sum())` → ⟨csv⟩ ("the tail of the histogram, counted").
- **2.3** scatter `delivery_min` vs `total_eur`; graded `slowest_ex23 = int(orders["delivery_min"].max())` → ⟨csv⟩.
- **3.1 Kevin's bug (fix-it):** Kevin's "growth chart" of the two weekly totals uses `plt.ylim` to start just under the smaller value — symptom: "week 2 looks 5× week 1; the numbers say otherwise." Fix: axis from 0; graded `growth_pct_ex31 = float(round((week2 - week1) / week1 * 100, 2))` → ⟨csv⟩ (weekly totals = days 1–7 vs 8–14).
- **Boss (ex40):** assemble the pitch dict: `pitch_ex40 = {"revenue": <total>, "best_zone": <argmax zone>, "orders": <row count>}` (all ⟨csv⟩; dict check with rounded values).

*Trace radio:* what displays if a cell's last line is `plt.plot(xs, ys)` vs `plt.gca()` (list-of-Line2D vs the axes — reveal). *MCQ (`answer_ex50`):* which chart for "how are order values distributed?" a) line b) histogram c) pie d) scatter → **"b"**.

*Wrap-up ritual* extended: "Download the `.py` — it's the appendix of your pitch. Homework before Session X: install uv + Zed (links)."

- [ ] **Step 2–4:** solutions, launcher (URL `.../notebooks/nb_09_lab_pitch/`), validate + WASM spot-check + render + commit both repos (`feat: episode 9 lab (plotting the pitch) + launcher`).

---

### Task 18: `lec_09` full rewrite (regular deck + homework gate)

**Goal:** The plotting deck: warm-up, three blocks (first chart / right chart / honest charts + AI), the Session-X homework slide.

**Files:**
- Rewrite: `lectures/lec_09_plotting.qmd`
- Delete: `lectures/supplementary/lec_09/` (temp_anomaly_data.xlsx — orphaned)
- Modify: `docs/side-quest-backlog.md`

**Acceptance Criteria:**
- [ ] Regular skeleton with warm-up; all demo charts use course data (inline lists or tiny frames — a DECK never loads `public/` files)
- [ ] Cut logged: seaborn/violin, networkx, joypy/ridgeline, pie/donut deep-dive, dashboards (Dash/Panel/Streamlit/NiceGUI), PySide6/GUIs, polyfit/trendline demo — all → backlog (dashboards + GUIs tagged "Part III project material")
- [ ] Homework slide present: install uv + Zed before Session X, linking `general/uv.qmd` + `general/ai-tools.qmd`
- [ ] Render passes

**Steps:**

- [ ] **Step 1: Warm-up (recap VIII)**

Q1: `orders[orders["zone"] == "Nord"]` returns… a) True/False per row b) only the Nord rows c) an error → **b** (a) is what the INNER expression returns — nice reveal line).
Q2: Kevin's AI code calls `orders.summarize()` — what happens? a) a summary table b) `AttributeError` c) an empty DataFrame → **b**.
Q3: `orders["total_eur"].describe()` shows… a) count/mean/std/min/quartiles/max b) the first five rows c) the column's type only → **a**.

- [ ] **Step 2: Blocks**

- **Cold open:** Friday. Boardroom. The investor sharpens a pencil. "Tables are homework. Charts are arguments."
- **Block 1 — "The first chart":** matplotlib in 4 lines (`plt.plot(days, revenue)`); anatomy: figure/axes/labels/title/legend; in marimo the LAST EXPRESSION displays → end chart cells with `plt.gca()`; style minimally (one color arg, one linestyle). Demo data: the ex_09_a weekly revenues.
- **⚡ QR a** → ex_09_a.
- **Block 2 — "The right chart for the question":** bar = compare categories (zones); histogram = see a distribution (order values); scatter = two variables (delivery time vs order value); line = change over time. One slide each with a small executable demo; one summary table slide. **Predict pair:** same 4 numbers as a bar chart and as a histogram question slide → answer: the histogram has only ~2 bars — "bar counts CATEGORIES, hist counts RANGES."
- **⚡ QR b** → ex_09_b → BREAK.
- **Block 3 — "Honest charts + the AI chart assistant":** the truncated-y-axis demo (two renders of the SAME growth data: ylim tight vs from 0); rule: growth claims start at 0; AI workflow for plots — describe the data + the question, let AI draft, then VERIFY (do the columns exist? do the axes start where you claim?); "the investor will check. So will the authorities." (Formular 27b/6 cameo allowed.)
- **⚡ QR c** → ex_09_c.
- **Homework slide** (`## Before Session X {.exercise-slide}`): install **uv** (`general/uv.qmd`) and **Zed** with ONE AI provider (`general/ai-tools.qmd`); bring the laptop — Session X builds the real toolchain and reveals what your notebooks have been all along.
- **Lab handoff** (tut_09) · **Wrap-up** (teaser: "Season finale: git, real files, and the project kickoff") · **Literature** (keep Wilke).

- [ ] **Step 3: Delete orphans, backlog, render, commit** (`feat: lec 09 rewrite — plotting + honest charts + AI assistant`).

---

### Task 19: CP5 — Sessions VIII–IX (PRIVATE repo)

**Goal:** The fifth checkpoint (taken at Session X's start): pandas wrangling + chart judgment, inline data only.

**Files (PRIVATE repo):**
- Create: `checkpoints/cp5/board_review.py`, `checkpoints/cp5/reference_tests.py`
- Test: extend `tests/test_checkpoints.py`

**Acceptance Criteria:**
- [ ] 6 tasks × 2 pts: 4 live-checked + 2 MCQ neutral; ALL data inline (`pd.DataFrame(...)` in the notebook — no `public/`, no network)
- [ ] Values per the freshness ledger row "CP5"; prices differ from `orders.csv` AND Part I; leniency identical live/final (`round(_, 2)`; dict compare with per-value rounding)
- [ ] pytest green with new fixtures

**Steps:**

- [ ] **Step 1: The inline dataset (verified 2026-07-11)**

```python
orders_df = pd.DataFrame({
    "zone":  ["Nord", "Altstadt", "Sued", "Altstadt", "Hafen",
              "Nord", "Altstadt", "Sued", "Hafen", "Nord"],
    "dish":  ["Bao Box", "Pad Thai", "Miso Ramen", "Falafel Wrap", "Bao Box",
              "Miso Ramen", "Bao Box", "Falafel Wrap", "Pad Thai", "Falafel Wrap"],
    "items": [2, 1, 3, 2, 1, 2, 3, 1, 2, 1],
    "total_eur": [15.80, 13.40, 36.30, 16.60, 7.90,
                  24.20, 23.70, 8.30, 26.80, 8.30],
})
```

(Unit prices: Bao 7.90, Pad Thai 13.40, Miso 12.10, Falafel 8.30 — internally consistent, all fresh.)

- **t1 (compute):** revenue in the Altstadt zone → `altstadt_t1 = float(...)` → **53.7**. Live hash on `round(_, 2)`.
- **t2 (fix Kevin's AI line):** given `avg_t2 = orders_df["total_eur"].average()` — symptom: "the cell errors; the AI was very confident." Fix → `.mean()` → **18.13** (raw `18.130000000000003` — round in check AND reference test).
- **t3 (groupby):** `by_zone_t3` as a DICT zone → total → `{"Altstadt": 53.7, "Hafen": 34.7, "Nord": 48.3, "Sued": 44.6}`. NOTE: raw Sued sum is `44.599999999999994` — BOTH the live check and the reference test must round each value to 2 before comparing (live check: build `{k: round(v, 2) for ...}` before hashing a `sorted(...)` canonical string; reference test mirrors exactly). Prompt says "use `.to_dict()`" (grader also coerces a raw Series post-Task-10).
- **t4 (filter/count):** orders with `total_eur` above 14 → `big_count_t4 = int(...)` → **6**.
- **t5 (MCQ, `answer_t5`):** "How are order values distributed?" — best chart: a) line b) pie c) histogram d) scatter → **"c"**. Neutral ack.
- **t6 (MCQ, `answer_t6`):** a revenue chart whose y-axis starts at 49 instead of 0 makes growth look… a) smaller b) bigger c) unchanged d) negative → **"b"**. Neutral ack.

- [ ] **Step 2: Reference tests** (dict compare pattern from cp2 t4 with rounding; leniency comments verbatim), **Step 3: hashes** (task-salted `cp5.tN`), **Step 4: fixtures + pytest + commit** `feat: checkpoint 5 (pandas + chart judgment)`.

---

### Task 20: Final battery + ledger sync

**Goal:** Everything in Part II proven green in one pass; documentation synced.

**Files:**
- Modify (if needed): whatever the battery flags
- Modify: `docs/side-quest-backlog.md` (verify all cut entries landed), `docs/authoring-conventions.md` (add any new convention discovered during Tasks 1–19 — e.g. the loader cell, the "charts ungraded / numbers graded" rule, CP-with-AI design note)

**Acceptance Criteria / Steps (run ALL):**

- [ ] **Notebooks headless:** `uv run python helpers/validate_notebooks.py` → ok for ALL notebooks (Part I + the 12 new: nb_06–09, ex_06_a–ex_09_c)
- [ ] **WASM export:** `uv run python helpers/export_marimo.py` → no failures; `_site/notebooks/nb_08_lab_dataroom/public/orders.csv` exists
- [ ] **Browser spot-check:** serve `_site` locally, open nb_08 and nb_09 exports, confirm the CSV loads and charts render (playwright, same motion as Task 1)
- [ ] **Renders:** per-file `quarto render` of lec_06–09, tut_06–09, general/ai-tools.qmd; `git checkout -- _repo-md/` after
- [ ] **Private repo:** `uv run pytest -q` → all green (expect 30+ tests)
- [ ] **Hygiene greps (public repo):**
  - `grep -ri copilot lectures/ tutorials/ notebooks/ general/` → empty
  - `grep -ri "co-authored\|generated with claude" . --exclude-dir=.git` → empty in BOTH repos
  - `ls notebooks/solutions/` → does NOT contain any sol_06–09 (nothing published before its session)
  - `grep -rn "expected\|answer" notebooks/nb_0[6-9]*.py | grep -i "= \"[a-d]\""` → no MCQ answers in lab code (spot-check)
- [ ] **QR inventory:** `ls lectures/assets/qr/ | wc -l` → 23 (13 Part I + 10 new); every deck's QR slide points at an existing PNG
- [ ] **Freshness audit:** re-read the ledger table at the top of this plan against the implemented files; any collision → fix the CP side, never the lab side
- [ ] **Ledger comments:** nb_08/nb_09 carry their `# ledger:` computed-values comment
- [ ] **Commit** any battery fixes (`fix: part II battery findings`), then update `.tasks.json` statuses.

---

## Self-review notes (author, 2026-07-11)

- Spec coverage: session map VI–IX ✓ (VI=CP3 day 2 blocks, VII regular, VIII=CP4 day with AI-craft front half, IX regular + uv/Zed homework per spec) · CP4/5 ✓ (Tasks 11, 19; AI-allowed design) · ai-tools page ✓ (Task 2, facts re-verified, no rate limits, Copilot pause note) · chatbot variant ✓ (Task 3) · datasets ship with notebooks ✓ (Task 12, no network calls) · "heavy data-wrangling practice" ✓ (nb_08, 9 cores on the real file).
- Deliberately NOT in this plan (→ Plan 4): Session X deck + git-basics page, retired-content sweep (old solutions-lectures/solutions-tutorials dirs, assignments), `_quarto.yml` nav cleanup (#12), `/humanizer` pass, dress-rehearsal items (user-led).
- Known risk: Task 1's verdict may force a different loader shape — Tasks 12/14/17 copy the loader from the conventions doc (single source), not from this plan's example, so a verdict change propagates through one file.
- All numeric literals verified in Python 2026-07-11; seeded values pinned to CPython's stable Mersenne Twister (same in Pyodide and the grader's 3.12).
