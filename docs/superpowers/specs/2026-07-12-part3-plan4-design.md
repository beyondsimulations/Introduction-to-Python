# Plan 4 Design — Part III: Session X, git-basics, Cleanup Sweep

**Date:** 2026-07-12
**Status:** Approved design, pending implementation plan
**Parent spec:** `2026-07-08-course-overhaul-design.md` (approved). This document refines its Part III/Session X sections into an implementable design and records the decisions taken on 2026-07-12.
**Scope:** `lectures/lec_10_projects.qmd` full rewrite · `general/git-basics.qmd` (new) · retired-content sweep (`solutions-lectures/`, `solutions-tutorials/`, `assignments/` → `archive/`) · `_quarto.yml` render+nav cleanup · `index.qmd`, `general/faq.qmd`, `general/syllabus.qmd` refresh.
**Out of scope:** the `/humanizer` copy pass (Plan 5); any Session XI–XIII materials (none exist by design); `Management-Science/` (different course, untracked); pushing the private checkpoints repo (user-led).

## Decisions taken (2026-07-12 question rounds)

| Question | Decision |
|---|---|
| CP5 timing | Start of Session X (spec default confirmed; risk-#6 fallback not needed — installs are homework per lec_09) |
| Session X shape after CP5 | **Kickoff first, tooling second** — groups form and choose ideas right after CP5; the tooling/git block then uses each pair's real project repo as the exercise |
| marimo-is-a-`.py` reveal | Episode cold-open, **played matter-of-fact** (confirmation, not surprise — most students will already suspect it) |
| GitHub auth | **Zed's built-in git panel + sign-in** as the primary interface; exact push-auth flow needs live verification (see Verification) |
| Group size | **Pairs**, solo fallback for odd counts (overrides the "up to 3" in the old deck and index.qmd; matches parent spec) |
| Project ideas | Keep the **ambitious ceiling** (students have AI); every idea gets an explicit achievable core + bonus tiers; menu refreshed |
| Deliverables | GitHub repo link on Moodle; **AI-disclosure section in the repo README**; presentation 10 + 5 min in Session XIII; commit history as process evidence |
| Old outro content | Keep, updated and trimmed (thesis/work/Advent of Code send-off stays in lec_10) |
| git-basics shape | **Zed-first + terminal equivalents**, ending in a cheatsheet table on the website |
| Sweep extras | index.qmd rewrite + FAQ additions + syllabus Session-X title tweak + stale `.gitignore` lines — all in scope |
| index.qmd AI policy | Rewrite to the **phased policy** (Part I AI-free / Part II AI allowed and taught / Part III AI encouraged with disclosure) |

## 1. `lec_10` rewrite — "Tooling, Git & Your Project"

Deck follows the established Part-II conventions: Fall 2026 header block, episode structure, `.exercise-slide` checkpoint opener, QR handed out live (never in the deck), interleaved-block rhythm. Deck title: *Lecture X — Tooling, Git & Your Project*.

### Slide flow

1. **CP5 opener** (first 40 min) — same pattern as lec_08's CP4 slide: individual work; **AI tools allowed** (verification is the graded skill); sweeps Sessions VIII–IX (pandas, cleaning, plotting, AI craft); ~6 tasks; link/QR handed out in class; download `.py` → "Checkpoint 5" assignment on Moodle; no retakes; live ✅ checks are provisional. One line of story flavor per convention ("the acquirer's final audit").
2. **Episode 10: The Exit** — MunchCorp acquires the startup. The clean data from VIII's due diligence and IX's honest dashboard are *why* the deal closed — the season's payoff. Kevin hands over the data room; the handover note carries the low-key reveal: everything built all semester is already plain `.py` files — the same files students have been downloading. Today they stop being backups and become the real thing, on the students' own machines. The students' "exit package": spin off their own idea as the final project. Tone: confirmation, not theatrics.
3. **Block 1 — Project kickoff** — the brief first: pairs (solo fallback), deliverable = GitHub repo link on Moodle with an AI-disclosure section in the README (which tools, what for, what you verified yourself), presentation 10 min + 5 min questions in Session XIII, project + presentation together = 40 of the 100 points (no finer split stated), commit history counts as process evidence, sessions XI–XII are supervised work sessions. Then the idea menu (§2), then ~20–30 min group formation and idea discussion. Groups leave the block knowing what they're building.
4. **Block 2 — Toolchain** — verify the uv + Zed installs from the Session IX homework (escape hatch: "didn't work? flag it for office hours, follow along on the slides"); `uv init` the project inside the pair's folder; open a downloaded lab notebook in Zed and run it with `uv run` — the reveal made concrete in one action; connect an AI provider in Zed per `general/ai-tools.qmd` (AI is allowed and encouraged in Part III, disclosure required).
5. **Block 3 — Git, in the project repo** — one vocabulary slide (repository, commit, push, pull, clone — what each *is*), then follow-along in Zed's git panel: create the repo, first commit, publish to GitHub, partner clones, both pull. Mistakes are cheap because the repo is minutes old. Collaboration-norms slide: pull before you work, commit small and often, conflict = call me. Terminal equivalents appear alongside each operation so the vocabulary isn't UI-bound. No branching, no PRs (parent spec).
6. **Block 4 — Send-off** (trimmed from the old deck): XI–XIII logistics recap; how to keep going (thesis, work projects, Advent of Code starting Dec 1); literature pointer; farewell.

### Explicit non-artifacts

No `nb_10`, no `ex_10_*`, no `tut_10`, no sidequest — the browser-notebook era ends with CP5, by design. The deck's "exercises" are the follow-along toolchain/git steps.

## 2. Project idea menu (slides within lec_10)

Every idea states an **achievable core** built from course concepts and **bonus tiers** where AI assistance shines. Menu of 7 + the open door:

1. **Data analytics dashboard** — core: load/clean a real CSV with pandas, answer 3 business questions with charts; bonus: interactive dashboard (streamlit), automated reporting.
2. **Web scraping pipeline** — core: scrape one site politely into a CSV and analyze it; bonus: multi-source, change detection, alerts.
3. **Simulation study** — core: Monte Carlo simulation of a business decision (pricing, staffing, inventory) with matplotlib results; bonus: interactive parameters, scenario comparison.
4. **Automation assistant** — core: a script that does a real repetitive task end-to-end with error handling and logging; bonus: scheduling, notifications, small UI.
5. **Game** — core: complete playable terminal or pygame game with save/load; bonus: levels, high scores, procedural content.
6. **ML-powered app** *(flagged ambitious, AI-assisted)* — core: train a simple model on tabular data and wrap it in a small interface; bonus: monitoring, A/B comparison.
7. **Your startup spin-off** — take any system from the course universe (courier routing, review moderation, demand forecasting) and build the real version.
8. **Your own idea** — the closer: "make it ambitious and let's discuss scope and feasibility."

Real-time computer vision and GPU acceleration leave the baseline menu (highest failure-setup risk); ambition stays available through bonus tiers and the open door. Exact slide copy is an implementation deliverable; the user prunes/extends at plan review or PR review.

## 3. `general/git-basics.qmd` (new page)

Companion reference for the Session X git block — what students open at home when the follow-along is a fading memory. Zed-first with terminal equivalents. No screenshots: text + UI-path descriptions so the page survives Zed UI changes.

Structure:

1. **Why version control** — two paragraphs, no history lesson.
2. **The five operations** — repository, commit, push, pull, clone; each as: concept → Zed git-panel path → terminal equivalent → when you need it.
3. **GitHub setup & auth** — the *verified* flow (see Verification): Zed sign-in if it authenticates pushes; otherwise the one-time `gh auth login` bridge, documented as three steps.
4. **Working as a pair** — clone your partner's repo, pull before you work, push when you stop; what a conflict looks like and "bring it to class" (conflicts are not solved solo in week 1).
5. **Troubleshooting** — auth failures, "not a git repository", committed the wrong thing (amend/new commit — no history rewriting taught).
6. **Cheatsheet** — final section: one compact table (operation / what it does / Zed path / terminal command / when), serving as the on-site git cheatsheet.

Sidebar: new entry in `_quarto.yml` directly after "Installing Python".

## 4. Cleanup sweep

- **Archive move:** `git rm -r --cached` on `solutions-lectures/`, `solutions-tutorials/`, `assignments/`; move them on disk into `archive/`; add `archive/` to `.gitignore`. Local copies preserved, tracked repo drops them. (Gitignore alone would not untrack already-tracked files — the `--cached` removal is load-bearing.) Remove the now-superseded `solutions-tutorials/tut_06`–`tut_09` gitignore lines in the same edit.
- **Delete outright** (no archive value): `lectures/hi.txt`, `lectures/hi_again.txt`, `lectures/__pycache__/`.
- **`_quarto.yml`:** remove the `assignments/*.qmd` render entry (line 12) and the "Assignments" sidebar section (lines 90–95); add the git-basics sidebar entry (§3).
- **`index.qmd`:** Course Structure item 3 → checkpoints (replacing "Assignments … groups of up to three"); "Passing the Course" → the 2026 math: 5 checkpoints × 12 pts (60) + project & presentation (40), 60/100 to pass, 75% attendance, pairs for the project; "AI Policy" → phased policy: Part I AI-free (hint-only course chatbot), Part II AI allowed and taught (CP4–5 included), Part III AI encouraged with disclosure; link to `general/ai-tools.qmd`.
- **`general/faq.qmd`:** add the parent-spec-promised entries — (a) a downloaded `.py` cannot be uploaded back into the browser editor (it is for submission, backup, and Part III use); (b) where notebook work lives (browser storage on the same machine + browser; download-as-backup habit); (c) how checkpoints are graded (live checks provisional; hidden reference tests decide); update the `KLU25` mailto subjects to 26.
- **`general/syllabus.qmd`:** retitle/redescribe Session X to tooling + git + project kickoff (titles/descriptions are the allowed tweak surface per parent spec); Sessions XI–XIII untouched.

## 5. Verification

- **Zed push-auth spike (before deck/page copy is finalized):** verify on the live web (and hands-on if needed) how a fresh Zed install authenticates a GitHub push — Zed sign-in vs. system git credentials. Whichever holds, git-basics §3 and one deck bullet state the verified flow; if Zed alone cannot authenticate, the `gh auth login` bridge becomes the documented path. Same freshness discipline as `general/ai-tools.qmd` (facts re-verified before publishing).
- **Final battery:** full `quarto render` of the course files (proves the site builds without `assignments/`); lec_10 renders as revealjs + typst; grep sweeps — no `Copilot` outside the sanctioned ai-tools framing, no references to `assignments/` or the archived solution dirs anywhere in the tracked tree, no stale `part-XX/data` paths; `helpers/validate_notebooks.py` still green (no notebook should change — this catches accidents); `git status` shows the archive dirs untracked-and-ignored, not deleted from disk.
- **Execution policy:** implementers and result-checkers run on Sonnet/Opus; no Fable fan-out (at most one Fable sub-agent, and only for critical-bug discovery, per the session cost policy). No LLM attribution or AI-process meta in commits/PR.
