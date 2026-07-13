# Plan 5 Design — Humanizer Pass + Verify-Live Finale

**Date:** 2026-07-13
**Status:** Approved design, pending implementation plan
**Parent spec:** `2026-07-08-course-overhaul-design.md`. This is the deferred "/humanizer pass over all copy at the very end", extended per the 2026-07-13 question rounds.
**Scope:** editing pass over all student-facing course copy (site `.qmd`, public notebook prose, private-repo CP/solution prose) against a single merged editing brief; known wording alignments; the pre-semester verify-live checklist as the final task.
**Out of scope:** content changes (facts, structure, exercise design, slide order), new material, `docs/` polishing, grader/test changes beyond re-running them, `imprint.qmd`/`privacy.qmd` (legal text stays verbatim).

## Decisions taken (2026-07-13 question rounds)

| Question | Decision |
|---|---|
| Surfaces | All three: site copy (decks, tutorials, general, index) + public notebook prose (`mo.md()` cells in 32 notebooks) + private repo prose (CP1–5 task wording, sol_01–09 walkthroughs) |
| Aggressiveness | Scrub AI tells **and** strengthen voice (not scrub-only) |
| Register per surface | Decks lively but restrained; reference pages sober; notebooks/solutions dry. Overriding rule: **no cringe** — cringe is an instant revert |
| Story canon | Punch up wording/dialogue/jokes freely; episode structure, plot events, character facts, and all numbers are frozen |
| Rubrics | Humanizer (v2.3.0, Wikipedia AI-tells) + term-consistency + conciseness + english-variant, merged into one editing brief |
| English variant | **US English** (matches Python/matplotlib API spellings; `behaviour`/`analyse` currently mixed in) |
| Models | Opus implementers and reviewers; Fable (in-session) reads **every** diff |
| Verify-live checklist | Included as the final Plan 5 task (guided session on the user's machine) |
| Review gate | Per-file commits; user skims the PR; plus a calibration gate on the first file |
| Execution shape | Approach A: per-file agents working from one merged editing brief + term glossary authored in-session by Fable |

## 1. Scope and exclusions

**In scope:**

- `lectures/lec_01…lec_10` (all 10 decks)
- `tutorials/tut_01…tut_09` (9 launcher pages)
- `index.qmd`
- `general/`: `ai-tools.qmd`, `faq.qmd`, `syllabus.qmd`, `uv.qmd`, `git-basics.qmd`, `cheatsheet.qmd` (prose around the code tables only), `literature.qmd` (intro lines only)
- `notebooks/nb_01…nb_09` labs + `notebooks/exercises/ex_*` (prose in `mo.md()` cells only)
- `notebooks/_template.py` prose (it seeds future notebooks)
- Private repo `../Introduction-to-Python-checkpoints`: `cp1…cp5` task wording, `sol_01…sol_09` walkthrough prose

**Excluded:** `general/imprint.qmd`, `general/privacy.qmd` (legal), all code everywhere (code cells, commands, fenced blocks, inline code spans), `docs/` internal documents, `_repo-md/`/`_site/` (generated).

## 2. Editing brief + term glossary (authored by Fable in-session, before any rewriting)

One committed document (`docs/superpowers/specs/2026-07-13-plan5-editing-brief.md`) merging the four rubrics:

1. **Humanizer tells** (from `~/.claude/skills/humanizer/SKILL.md` v2.3.0): significance inflation, promotional tone, superficial `-ing` tack-ons, vague attributions, rule of three, negative parallelism, copula avoidance, synonym cycling, false ranges, em-dash overuse, mechanical boldface, inline-header bullet lists, AI vocabulary (delve, crucial, pivotal, testament, showcase, underscore, landscape, tapestry, vibrant, foster…), filler phrases, excessive hedging, generic upbeat conclusions.
2. **Conciseness table** (from `~/.claude/skills/conciseness/SKILL.md`): wordy → concise substitutions.
3. **US English enforcement** (from `~/.claude/skills/english-variant/SKILL.md`): -ize/-or/-er spellings; known offenders `behaviour` (lec_03 ×5, tut_03), `analyse` (lec_10).
4. **Term glossary**: produced by an Opus scout sweep listing every inconsistently-used course term (candidates: notebook/lab, checkpoint/CP, session/lecture numbering, exercise/task, and whatever the sweep finds); Fable picks the winning term for each; the glossary section of the brief is the single source of truth.

**Register cards** (one per surface):

- **Decks:** lively but restrained. First-person instructor asides allowed. Rhythm variation encouraged. The bar: something Tobias would say out loud to a room without wincing. Cringe = instant revert.
- **Reference pages** (general/, tutorials): sober, scannable, zero jokes. The reader may be debugging at 23:00; clarity beats character.
- **Notebooks + solutions:** dry, precise; light warmth allowed at wrap-up cells only.

**Hard guardrails** (violations are review-blocking):

- Never touch: code cells, commands, expected values/outputs, check-cell strings and logic, hashes, hint-skeleton structure (Hint 2 = `___` skeletons), story facts/beats/numbers, grading rules and point values, links, QR slugs, file names, YAML frontmatter keys, revealjs directives.
- Prompts stay symptom-only (no expected values or bug locations added while rewording).
- CP task wording may be reworded but requirements stay exact: variable names, expected values, and task semantics are frozen (38 reference tests key off them).
- Story canon frozen per the decisions table.

## 3. Calibration gate

`lec_01` runs the full cycle first: implementer → reviewer → Fable read → **user skims that single commit**. The fan-out over the remaining ~55 file tasks starts only after the user confirms the tone. If calibration fails, the brief is revised and lec_01 redone before anything else runs.

## 4. Execution mechanics

- Per-file Opus implementer + per-file Opus reviewer (checks meaning-preservation, guardrail compliance, register fit, cringe veto). Reviewer findings loop back to the implementer until clean.
- One commit per file. Small files batch: tutorials in two commits (tut_01–05, tut_06–09), `ex_` exercises batched per session, private solutions batched per part.
- Known alignment folded in: **lec_10's uv-init slide** states repo-creation unconditionally while git-basics conditions it on git being installed — align lec_10 to the conditional wording (deck-appropriate brevity is fine, e.g. a footnote-style qualifier).
- Public work on branch `overhaul-plan-5-humanizer` → PR #5. Private repo: direct commits, as with Plans 2–3.
- Fable reads every diff before the user's PR skim. No AI attribution or process meta in commits/PR (standing rule).

## 5. Validation

End-of-plan battery:

- Full `quarto render` green (refreshes `_repo-md/` and WASM exports; only full renders update `_repo-md/` since the `QUARTO_PROJECT_RENDER_ALL` guard).
- `helpers/validate_notebooks.py` green (32 notebooks).
- Private repo pytest green (38 tests).
- UK-spelling grep over prose → zero.
- Banned-AI-word grep over prose → zero. The authoritative word list lives in the editing brief's humanizer section (delve, pivotal, testament, tapestry, showcase, vibrant, foster, and the rest of the AI-vocabulary table), with a small allowlist where a word is used literally (e.g. Python's `_` underscore in identifier discussions).
- Em-dash count reported per file (target: reduced; not banned — decks legitimately use a few).
- Any touched notebook that fails validation reverts to its pre-pass state rather than shipping half-edited.

## 6. Verify-live finale

Final task, guided session on the user's machine, following the spike doc's "Verify-live-before-semester" list: Zed git-panel wording, `gh auth login` prompt text, `git: create remote` flow, per-OS default branch names. Results are written back into `2026-07-12-zed-git-auth-spike.md`; any resulting copy corrections land as follow-up commits on the same branch so PR #5 ships verified copy. If the user prefers to defer the live session, PR #5 can merge without it and the finale becomes a standalone follow-up — the copy pass does not block on it.

## 7. Execution policy

Implementers, reviewers, and scouts on Opus (Sonnet acceptable for mechanical batches like tutorials); no Fable subagents — Fable's role is the brief, the glossary decisions, and reading every diff in-session. No LLM attribution or AI-process meta in commits or PR bodies, in either repo.
