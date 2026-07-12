# Overhaul Plan 4 — Part III: Session X, git-basics, Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers-extended-cc:subagent-driven-development (recommended) or superpowers-extended-cc:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete Part III of the 2026 course overhaul — rewrite `lec_10` as the Session X "Tooling, Git & Your Project" deck, add `general/git-basics.qmd`, and sweep all pre-overhaul content (assignments, old solutions, stale copy) out of the tracked repo.

**Architecture:** Content-authoring plan on the Quarto course site. No notebooks change (the browser-notebook era ends with CP5 by design). One verification spike (Zed git auth) gates the two git-teaching deliverables. Everything else is independent page work plus one atomic retirement sweep, closed by a render/grep battery.

**Tech Stack:** Quarto (revealjs + website), git, Zed editor facts (web-verified), uv.

**Authoritative sources for implementers:**
- Spec: `docs/superpowers/specs/2026-07-12-part3-plan4-design.md` (all design decisions)
- Parent spec: `docs/superpowers/specs/2026-07-08-course-overhaul-design.md` (§3 session map, §6 grading, §7 AI story)
- Conventions: `docs/authoring-conventions.md` (deck patterns, commit rules, render caveats) — **read before any authoring task**
- Tone/pattern references: `lectures/lec_08_pandas.qmd` (CP-opener deck), `lectures/lec_09_plotting.qmd` (episode voice, Session X teaser it must connect to)

**Execution policy (binding):** implementer and checker subagents run on **Sonnet or Opus, never Fable**. No `Co-Authored-By`/"Generated with Claude Code" lines, no AI-process meta in any commit message or PR body.

**Render caveat (from conventions doc):** a single-file `quarto render <file>.qmd` deletes sibling `_repo-md/*.md` files — after every single-file render check, run `git checkout -- _repo-md/`. Only the full-site render in Task 7 may update `_repo-md/`.

---

### Task 1: Zed git auth spike (verification, gates Tasks 5 & 6)

**Goal:** Establish, from current web sources plus a local check, the exact flow a student on a fresh machine uses to publish/push a repo to GitHub from Zed — so the deck and git-basics page state verified facts, not guesses.

**Files:**
- Create: `docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md`

**Acceptance Criteria:**
- [ ] Answers, with sources and access dates: (a) which git operations Zed's git panel supports in July 2026 (stage, commit, push, pull, fetch, branch, clone, init — which exist, which don't); (b) how a push authenticates to GitHub from a fresh Zed install — does Zed's GitHub sign-in cover git push auth, or does Zed shell out to system git credentials (credential helper / `gh auth login` needed)?
- [ ] Local check recorded: does `uv init <dir>` initialize a git repository by default (current uv version)? This decides whether the Session X flow needs `git init` at all.
- [ ] Ends with a **"Copy for authors"** section: the exact auth steps git-basics §"GitHub setup & auth" and the lec_10 setup bullet must state (one primary path; `gh auth login` documented as the bridge only if Zed alone cannot authenticate).
- [ ] No unverified claims: every UI path either comes from Zed docs/release notes or is flagged "verify live before semester" in a short list at the end.

**Verify:** `test -f docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md && grep -c "Copy for authors" docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md` → ≥1

**Steps:**

- [ ] **Step 1: Web research.** WebSearch/WebFetch: Zed docs on git support (`zed.dev/docs/git` or current URL), Zed release notes/blog on the git panel, GitHub docs on HTTPS auth (credential helpers, `gh auth login`). Capture: supported operations, auth mechanism, whether "Publish to GitHub" exists in Zed.
- [ ] **Step 2: Local check.** Run in a scratch dir: `uv init spike-test && ls -a spike-test` → record whether `.git/` exists. Delete the scratch dir afterwards.
- [ ] **Step 3: Write the spike doc** with sections: Findings (sourced), uv init behavior, Decision (primary auth path), Copy for authors, Verify-live-before-semester list.
- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md
git commit -m "docs: verify Zed git panel capabilities and GitHub auth flow"
```

---

### Task 2: Retired-content sweep + `_quarto.yml` cleanup (atomic)

**Goal:** Move `solutions-lectures/`, `solutions-tutorials/`, `assignments/` out of the tracked repo into an untracked local `archive/`, delete strays, and remove the assignments render/nav entries in the same commit so the site never references retired content.

**Files:**
- Modify: `.gitignore`, `_quarto.yml`
- Delete from tracking (84 files): `solutions-lectures/`, `solutions-tutorials/`, `assignments/`; delete outright: `lectures/hi.txt`, `lectures/hi_again.txt`, `_repo-md/assignments/` (2 generated files); on-disk only: `lectures/__pycache__/`

**Acceptance Criteria:**
- [ ] `git ls-files | grep -E "^(solutions-lectures|solutions-tutorials|assignments)/" | wc -l` → 0, but `ls archive/` shows all three directories with contents intact on disk
- [ ] `git status --short` shows no `archive/` (ignored), no deleted-but-present files
- [ ] `_quarto.yml` has no `assignments` render or nav entries; `- "!Management-Science/"` excludes the unrelated course dir so full-site renders stop failing on it (pre-existing blocker)
- [ ] `.gitignore` has `archive/` and no longer lists `solutions-tutorials/tut_06`–`tut_09`

**Verify:** `git ls-files | grep -cE "^(solutions-lectures|solutions-tutorials|assignments)/"` → 0 · `ls archive/` → 3 dirs · `grep -c assignments _quarto.yml` → 0

**Steps:**

- [ ] **Step 1: Untrack and move the retired dirs (order matters — untrack first, then move on disk):**

```bash
git rm -r -q --cached solutions-lectures solutions-tutorials assignments
mkdir -p archive
mv solutions-lectures solutions-tutorials assignments archive/
```

- [ ] **Step 2: Delete strays:**

```bash
git rm -q lectures/hi.txt lectures/hi_again.txt
git rm -r -q _repo-md/assignments
rm -rf lectures/__pycache__
```

- [ ] **Step 3: Edit `.gitignore`** — remove the four lines `solutions-tutorials/tut_06` … `solutions-tutorials/tut_09`; add:

```gitignore
archive/
```

- [ ] **Step 4: Edit `_quarto.yml`** — in `project.render`, delete `- assignments/*.qmd` and add the exclusion; in `website.sidebar.contents`, delete the whole Assignments section:

```yaml
# render list becomes:
  render:
    - index.qmd
    - 404.qmd
    - general/*.qmd
    - lectures/*.qmd
    - tutorials/*.qmd
    - "!Management-Science/"
```

Delete these sidebar lines (currently ~90–95):

```yaml
      - section: "Assignments"
        contents:
          - text: "01 Assignment"
            href: assignments/assignment_01.qmd
          - text: "02 Assignment"
            href: assignments/assignment_02.qmd
```

- [ ] **Step 5: Render check** (site config still valid): `quarto render index.qmd` → succeeds; then `git checkout -- _repo-md/`
- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "chore: retire pre-overhaul assignments and solutions into untracked archive"
```

---

### Task 3: `index.qmd` — checkpoint-based grading + phased AI policy

**Goal:** The landing page describes the 2026 course: checkpoints instead of assignments, real passing math, phased AI policy.

**Files:**
- Modify: `index.qmd` (Course Structure item 3, Passing the Course, AI Policy, Questions mailto)

**Acceptance Criteria:**
- [ ] No mention of "assignments" as an assessment; structure lists checkpoints
- [ ] Passing section states: 75% attendance, 5 checkpoints × 12 pts = 60, project + presentation = 40, 60/100 to pass, project in pairs with one GitHub repo per pair
- [ ] AI Policy states the three phases and links to `general/ai-tools.qmd`
- [ ] mailto subject bumped `KLU25` → `KLU26`

**Verify:** `grep -ci "two programming assignments" index.qmd` → 0 · `grep -c "ai-tools.qmd" index.qmd` → ≥1 · `quarto render index.qmd` → succeeds (then `git checkout -- _repo-md/`)

**Steps:**

- [ ] **Step 1: Replace Course Structure item 3** ("Assignments: Students will solve…") with:

```markdown
3. **Checkpoints**: Five short in-class checkpoints let you show what you have learned. They run in the browser, are solved individually, and are graded automatically.
```

- [ ] **Step 2: Replace the "Passing the Course" bullet list** ("two programming assignments and one project…", "group up (3 students)…") with:

```markdown
- 75% attendance is required to pass the course
- Five in-class checkpoints, worth 12 points each (60 points total)
- One final project with a presentation, worth 40 points
- You need 60 of 100 points to pass
- The project is done in pairs; each pair submits one GitHub repository
```

- [ ] **Step 3: Replace the AI Policy section** (drop the "Level 1: Pause" frame) with:

```markdown
## AI Policy

The course uses a phased AI policy that mirrors how the skills build on each other:

- **Part I (Sessions I–V): AI-free.** You are building foundations. The course chatbot on this website is the sanctioned helper — it gives hints, not solutions. Checkpoints 1–3 are taken without AI.
- **Part II (Sessions VI–IX): AI allowed and taught.** We bring AI in deliberately: how to prompt with context and constraints, how to verify output, how to spot invented APIs. Checkpoints 4–5 explicitly allow AI tools.
- **Part III (Sessions X–XIII): AI encouraged.** Use what makes you productive on your project — and disclose what you used in your repository's README.

Whatever the phase: understand every line you submit. See the [AI Tools guide](general/ai-tools.qmd) for free options and setup.
```

- [ ] **Step 4:** In the Questions section, change the mailto subject `ProgrammingPythonKLU25` → `ProgrammingPythonKLU26`.
- [ ] **Step 5: Render check** `quarto render index.qmd`, then `git checkout -- _repo-md/`
- [ ] **Step 6: Commit**

```bash
git add index.qmd
git commit -m "docs: index page reflects checkpoint grading and phased AI policy"
```

---

### Task 4: FAQ additions + syllabus Session X update

**Goal:** FAQ answers the three notebook/checkpoint questions the spec promises; syllabus Session X describes tooling/git/kickoff.

**Files:**
- Modify: `general/faq.qmd`, `general/syllabus.qmd`

**Acceptance Criteria:**
- [ ] FAQ contains entries covering: downloaded `.py` is one-way (cannot be uploaded back into the browser editor); where notebook work lives (reload keeps it, closing the tab loses it — wording aligned with the tut_01 launcher); how checkpoints are graded (live checks provisional, reference tests decide)
- [ ] Both FAQ mailto subjects bumped `KLU25` → `KLU26`
- [ ] Syllabus Session X entry retitled/redescribed (XI–XIII untouched)

**Verify:** `grep -c "KLU26" general/faq.qmd` → 2 · `grep -ci "uploaded back\|one-way" general/faq.qmd` → ≥1 · `quarto render general/faq.qmd general/syllabus.qmd` → succeeds (then `git checkout -- _repo-md/`)

**Steps:**

- [ ] **Step 1: Read the persistence wording** in `tutorials/tut_01_introduction.qmd` (the launcher's browser-storage copy) — the FAQ answers below must not contradict it; adjust phrasing to match its verified behavior (reload keeps work; closing the tab and reopening the link starts fresh; download is the only guaranteed copy).
- [ ] **Step 2: Add three FAQ entries** under the FAQs section (adapt wording per Step 1):

```markdown
### Can I upload my downloaded `.py` back into the browser?

No — this is a one-way door. The browser editor cannot open an uploaded file. Your download is for three things: submitting checkpoints, keeping a safety copy, and working locally in Part III of the course. To continue in the browser, keep the tab open or reload it — don't close it.

### Where is my notebook work saved?

Your work lives in the browser: reloading the page keeps it, but closing the tab and opening the course link again later starts fresh. The only guaranteed copy is menu → *Download* → *Download Python code*. Make that download a habit at the end of every session.

### How are checkpoints graded?

The green ✅ checks inside a checkpoint are provisional — they tell you you're on track. Final grading re-runs your submitted `.py` against a reference test suite on our side. Upload your download to the matching Moodle assignment before the deadline; Moodle's clock decides what is on time.
```

- [ ] **Step 3:** Bump both FAQ mailto subjects to `ProgrammingPythonKLU26Mistake` / `ProgrammingPythonKLU26`.
- [ ] **Step 4: Replace the syllabus Session X entry** ("Your first Project I (X) — Choose your project…") with:

```markdown
**Tooling, Git & Your Project (X)**\
Set up Python and an editor on your own machine, learn git and GitHub, form pairs and choose your project
```

- [ ] **Step 5: Render check** both files, then `git checkout -- _repo-md/`
- [ ] **Step 6: Commit**

```bash
git add general/faq.qmd general/syllabus.qmd
git commit -m "docs: FAQ notebook and checkpoint entries; syllabus Session X update"
```

---

### Task 5: `general/git-basics.qmd` + sidebar entry *(blocked by Task 1)*

**Goal:** The at-home companion reference for the Session X git block: Zed-first, terminal equivalents alongside, ending in an on-site cheatsheet table.

**Files:**
- Create: `general/git-basics.qmd`
- Modify: `_quarto.yml` (sidebar entry after "Installing Python")

**Acceptance Criteria:**
- [ ] Sections in order: why version control (2 paragraphs, no history lesson) → the five operations (repository/commit/push/pull/clone: concept → Zed path → terminal equivalent → when) → GitHub setup & auth (**verbatim from the spike doc's "Copy for authors"**) → working as a pair (clone, pull-before-work, push-when-you-stop, conflict = bring it to class) → troubleshooting (auth failure, "not a git repository", committed the wrong thing — no history rewriting) → cheatsheet table
- [ ] No screenshots; Zed UI referenced as text paths only, and only paths the spike verified (unverified ones use the spike's fallback wording)
- [ ] Cheatsheet is one table: operation / what it does / in Zed / terminal / when you need it
- [ ] Sidebar shows "Git Basics" between "Installing Python" and "AI Tools"

**Verify:** `quarto render general/git-basics.qmd` → succeeds (then `git checkout -- _repo-md/`) · `grep -c "git-basics" _quarto.yml` → 1

**Steps:**

- [ ] **Step 1: Read** `docs/superpowers/specs/2026-07-12-zed-git-auth-spike.md` (auth copy + verified Zed paths) and `docs/authoring-conventions.md` (voice rules).
- [ ] **Step 2: Write the page.** Frontmatter:

```yaml
---
title: "Git Basics"
subtitle: "Version control for your project, from Zed"
---
```

Content contract beyond the section list above: address the student directly ("you"), match the plain-explainer voice of `general/uv.qmd`; every one of the five operations shows the terminal command in a fenced block even when the Zed path is primary (the vocabulary must survive the UI); the pair-workflow section names the two roles explicitly (repo owner creates + invites collaborator; partner clones); the troubleshooting entries give the symptom first, then the fix; cheatsheet rows cover at minimum: init/create, stage+commit, push, pull, clone, status/history.

- [ ] **Step 3: Add the sidebar entry** in `_quarto.yml` directly after the "Installing Python" line:

```yaml
      - text: "Git Basics"
        href: general/git-basics.qmd
```

- [ ] **Step 4: Render check**, then `git checkout -- _repo-md/`
- [ ] **Step 5: Commit**

```bash
git add general/git-basics.qmd _quarto.yml
git commit -m "feat: git basics guide with Zed-first workflow and cheatsheet"
```

---

### Task 6: `lec_10` rewrite — "Tooling, Git & Your Project" *(blocked by Task 1)*

**Goal:** Full deck rewrite per spec §1–2: CP5 opener → Episode 10 (The Exit) → project kickoff → toolchain → git in the project repo → send-off.

**Files:**
- Modify (full rewrite): `lectures/lec_10_projects.qmd`

**Acceptance Criteria:**
- [ ] Deck order exactly: CP5 opener · Episode 10 · kickoff block (brief → idea menu → group formation) · toolchain block · git block · send-off; interleaved-block rhythm and `.exercise-slide`/callout conventions match lec_08
- [ ] CP5 opener follows the lec_08 CP4 slide pattern (individual, AI allowed, ~6 tasks, download → Moodle "Checkpoint 5", no retakes, provisional-✅ note) and its content description matches the actual CP5 notebook in the private repo
- [ ] Reveal is matter-of-fact (confirmation, not surprise); no branching/PRs anywhere; auth bullet matches the spike's "Copy for authors"
- [ ] Idea menu = the 8 items from spec §2, each with achievable core + bonus tier; no real-time CV / GPU baseline items
- [ ] Brief states: pairs (solo fallback), repo link on Moodle, AI-disclosure section in README (which tools, what for, what you verified), 10+5 min presentation in Session XIII, project+presentation = 40/100, commit history as process evidence, XI–XII supervised work sessions
- [ ] Old deck's Copilot line, giphy iframes, and "groups of up to 3" are gone; send-off keeps thesis/work/Advent-of-Code + literature pointer, trimmed
- [ ] Header block: Fall 2026, title "Lecture X - Tooling, Git & Your Project", `output-file: lec_10_presentation.html`

**Verify:** `quarto render lectures/lec_10_projects.qmd` → succeeds (then `git checkout -- _repo-md/`) · `grep -ci copilot lectures/lec_10_projects.qmd` → 0 · `grep -c "Checkpoint 5" lectures/lec_10_projects.qmd` → ≥1

**Steps:**

- [ ] **Step 1: Read the pattern sources**: `lectures/lec_08_pandas.qmd` (CP opener + episode + block rhythm), tail of `lectures/lec_09_plotting.qmd` (the Session X teaser this deck must pay off: "git, real files, and the project kickoff"), `docs/authoring-conventions.md`, the spike doc, and the CP5 notebook in `../Introduction-to-Python-checkpoints` (for the opener's honest task-mix description).
- [ ] **Step 2: Write the header** (matches lec_08 style):

```yaml
---
title: "Lecture X - Tooling, Git & Your Project"
subtitle: "Programming with Python"
author: "Dr. Tobias Vlćek"
institute: "Kühne Logistics University Hamburg - Fall 2026"
format:
  revealjs:
    footer: " {{< meta title >}} | {{< meta author >}} | [Home](lec_10_projects.qmd)"
    output-file: lec_10_presentation.html
---
```

- [ ] **Step 3: CP5 opener slide** — adapt this skeleton, correcting the task-mix line against the real CP5 notebook:

```markdown
# 📋 Checkpoint 5 — Sessions VIII–IX {.exercise-slide}

The first **40 minutes** are the checkpoint. It starts **now** — the acquirer runs one final audit before signing.

- **Individual work** — no neighbours, no chat
- **AI tools are allowed** — being able to **VERIFY** the output is the skill being graded
- The **link and QR** are handed out in class — open it and start
- ~6 short tasks: write code, trace code, fix a bug, answer a multiple choice
- It sweeps **Sessions VIII–IX** — pandas, cleaning messy data, plotting

<!-- QR handed out live — never in the deck -->

. . .

**When you're done:** menu → *Download* → *Download Python code* → upload the `.py` to the **"Checkpoint 5"** assignment on Moodle. **No retakes** — one sitting.

. . .

:::{.callout-note}
The green ✅ live checks are **provisional** — the final grading runs on our side. And take a breath: everything in it was rehearsed in the labs.
:::
```

- [ ] **Step 4: Episode 10 — The Exit** (2–3 slides). Beats to hit, in the established episode voice: MunchCorp buys the startup; the clean data from the due diligence (VIII) and the honest dashboard (IX) are *why* the deal closed — the season's payoff, said explicitly. Kevin hands over the data room; the handover note carries the reveal, played dry: everything the class built all semester is already plain `.py` files — the ones they've been downloading. Today they stop being backups. The students' exit package: spin off your own idea as the final project. **Tone guard:** no "surprise!", no "plot twist" — one wry line, then move on.
- [ ] **Step 5: Kickoff block** — (a) the brief slide(s) with every fact from the acceptance criterion; (b) the idea menu, one slide per 1–2 ideas, using spec §2's eight items with core/bonus split (formatting: core bullets first, then a `**Bonus:**` fragment line, mirroring the old deck's rhythm); (c) a "form your pair, pick your direction" discussion slide (~20–30 min, deck says what a good outcome of the discussion looks like: a one-sentence project pitch and a name).
- [ ] **Step 6: Toolchain block** — verify uv+Zed homework installs (escape hatch: "didn't work → office-hours flag, follow along on slides"); `uv init` the project inside the pair's folder (state what it creates, per `general/uv.qmd`, including the spike's finding on git init); open a previously downloaded lab notebook in Zed and `uv run` it — one slide, matter-of-fact, the reveal made concrete; connect an AI provider per `general/ai-tools.qmd` (AI encouraged in Part III, disclosure required).
- [ ] **Step 7: Git block** — vocabulary slide (repository, commit, push, pull, clone — one plain sentence each); follow-along slides in the pair's real repo: first commit in Zed's panel → publish/push to GitHub (auth per spike copy) → partner clones → both pull; collaboration-norms slide (pull before you work, commit small and often, conflict = call me); terminal equivalent shown beside each Zed action; pointer slide to `general/git-basics.qmd` as the at-home reference.
- [ ] **Step 8: Send-off block** (2–3 slides, trimmed from old deck): XI–XII supervised work + XIII presentations logistics; keep programming (thesis, work, Advent of Code starting Dec 1); literature pointer; farewell — no giphy iframes, match the course's current voice.
- [ ] **Step 9: Render + checks**: `quarto render lectures/lec_10_projects.qmd`, then `git checkout -- _repo-md/`; run the greps from Verify.
- [ ] **Step 10: Commit**

```bash
git add lectures/lec_10_projects.qmd
git commit -m "feat: rewrite lec_10 as Session X tooling, git and project kickoff"
```

---

### Task 7: Final battery *(blocked by Tasks 2–6)*

**Goal:** Prove the whole site builds without the retired content and nothing references it; refresh `_repo-md/` via the full render.

**Files:**
- Modify: `_repo-md/` (regenerated by full render only)

**Acceptance Criteria:**
- [ ] Full-site `quarto render` succeeds (Management-Science excluded per Task 2)
- [ ] `lectures/lec_10_projects.qmd` renders to revealjs and typst without error
- [ ] Greps clean: no tracked reference to `assignments/`, `solutions-lectures/`, `solutions-tutorials/`; no `Copilot` outside `general/ai-tools.qmd`'s sanctioned section and `_repo-md/general/ai-tools.md`; no stale `part-0[89]/data` paths
- [ ] `helpers/validate_notebooks.py` green (no notebook should have changed — this catches accidents)
- [ ] `git status` confirms `archive/` untracked-and-ignored and still present on disk

**Verify:** the command battery below, all green

**Steps:**

- [ ] **Step 1: Full render**: `quarto render` → exits 0. Commit the `_repo-md/` refresh separately if it changed.
- [ ] **Step 2: Typst check**: `quarto render lectures/lec_10_projects.qmd --to typst` → exits 0; then `git checkout -- _repo-md/` if a single-file render ran.
- [ ] **Step 3: Reference greps** (all must return 0):

```bash
git grep -l "assignments/" -- "*.qmd" "*.yml" | wc -l
git grep -l "solutions-lectures\|solutions-tutorials" -- "*.qmd" "*.yml" "*.py" | wc -l
git grep -li copilot -- "*.qmd" ":!general/ai-tools.qmd" | wc -l
git grep -l "part-08/data\|part-09/data" -- "*.py" "*.qmd" | wc -l
```

- [ ] **Step 4: Notebook validation**: `uv run python helpers/validate_notebooks.py` → same green result as on main.
- [ ] **Step 5: Archive sanity**: `git status --short | grep -c archive` → 0 and `ls archive/ | wc -l` → 3.
- [ ] **Step 6: Commit** any `_repo-md` refresh:

```bash
git add _repo-md
git commit -m "chore: refresh generated markdown for part III overhaul"
```

---

## Task dependency summary

- Task 1 (spike) blocks Tasks 5 and 6.
- Tasks 2, 3, 4 are independent of everything (and of each other).
- Task 7 is blocked by Tasks 2–6.
- Suggested order: 1 → 2 → 3 → 4 → 5 → 6 → 7 (or 2–4 in parallel with 1).
