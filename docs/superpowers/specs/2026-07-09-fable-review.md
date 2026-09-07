# Fable Design Review — Plan 1 Vertical Slice (2026-07-09)

Scope: design/pedagogy/completeness only (code correctness was reviewed separately).
Reviewed: spec + plan + spike results + follow-ups; `notebooks/_template.py`,
`nb_01_lab_founding.py`, `exercises/ex_01_{a,b,c}.py`, `tutorials/tut_01_introduction.qmd`,
`lectures/lec_01_introduction.qmd`, `_quarto.yml`, both syllabus files, and the entire
`../Introduction-to-Python-checkpoints` repo (cp0, grader, deploy script, README, rehearsal doc).

---

## Resolution (2026-07-09)

**Addressed this session:** #1 (grader now grades "write a function" via
referee-supplied `exprs` — hardcoded probes can't pass; +2 tests, 11 pass),
#2 (lec_01 factual slides corrected: passing scheme, AI-free Part I, no-install
Session I, Fall 2026), #3 (Hint 2 → skeleton-with-blanks in template + nb_01),
#6 (boss reframed to reuse `revenue_ex12`/`margin_ex22`), #8 (`show_result`
helper hidden), #9/#11 (input-above-greeting, core MCQ before bonuses, 2.1
relabelled, ex_01_a de-spoilered, investor cameos → on-canon). All validated
headless (placeholder→red, solved→green) + render + grader suite.

**Deferred to Plan 2 (scheduled, not dropped):** #4 post-session solution
notebook pattern · #5 chatbot hint-only system prompt (external, before
Session I) · #7 molab login = pre-semester gate (rehearsal B5) · #10 write down
"exercise letter = slide order" · #12 drop retired Assignments nav from
`_quarto.yml` (Plan 4). Take-down/variants stay parked.

**Plan 2 resolution (2026-07-10):** #4 RESOLVED in Plan 2 Task 2 — solution
notebooks are authored in the private repo, exported with `--mode run`, and
linked from tutorials via dormant links; runbook lives in the private README
and the conventions doc. #5 DRAFTED in Plan 2 Task 3
(`docs/chatbot-system-prompt.md`) — external installation by Tobias remains a
pre-Session-I gate. #10 CODIFIED in `docs/authoring-conventions.md` and applied
in all five decks. #7 remains user-led (dress-rehearsal B5). #12 remains
Plan 4.

## Findings (prioritized)

### 1. DESIGN-BLOCKER — Grader architecture cannot grade the "write a function" task type
`../Introduction-to-Python-checkpoints/grader/runner.py` + `grade.py`. The runner
JSON-serializes only scalars/lists/dicts (functions arrive as `repr()` strings), and
reference tests are lambdas over that JSON dict — so the server-side referee can never
*call* a student's function. Workaround-by-probe ("notebook contains `probe_t4 = f(...)`")
fails the threat model: checkpoint cells are student-editable, so a probe can be hardcoded,
and the hidden suite re-runs the student's own file. "Write a function" is one of the four
syllabus-promised task types and is needed from CP2 (Session III). The dress-rehearsal doc's
claim "the grading machinery is done and trustworthy" is true only for value-assignment tasks.
**Fix:** extend the runner to evaluate instructor-supplied expressions inside the subprocess
(e.g. `TASKS[...]["exprs"] = {"probe_t4": "tip_t4(10, 0.2)"}`, evaluated against the extracted
namespace, results JSON-emitted), and document the constraint in the checkpoints README.
Same class of constraint worth documenting: JSON coerces tuples→lists (matters by Session IV).
Settle this before any CP2+ authoring — it is the one real hole in the foundation.

### 2. SHOULD-ADDRESS — lec_01 contains factually wrong course mechanics; patch 3 slides now, don't ride the Plan-2 rewrite
`lectures/lec_01_introduction.qmd`. Deferring the full content rewrite to Plan 2 is the right
call (the teaching slides are salvageable and the scaffolding integration is clean). But three
things are not "old content", they are *wrong statements about how the course works*, and if
Plan 2 slips even a week they get said out loud in Session I:
- "Passing the Course": "2 assignments and 1 final project", "group up (3 students)" — contradicts
  5 checkpoints / individual work / project pairs (klu_syllabus.md).
- "How to use AI": "You are allowed to use AI (Claude, ChatGPT, Mistral ...)" — contradicts the
  Part I AI-free policy that the checkpoints legally lean on ("unauthorised aid").
- "Setting up Python" + "Your first code" (install uv/Zed now, create `hello.py` locally) —
  contradicts the syllabus promise "nothing to install before the first session" and the
  browser-only Part I design. (Also: header still says "Fall 2025".)
These are ~10 minutes of deletion/replacement. Cheap insurance; keep the rest deferred.

### 3. SHOULD-ADDRESS — Hint 2 is the full solution everywhere, collapsing the 2-tier ladder
`_template.py` says Hint 2 = "code skeleton with a blank to fill", but every Hint 2 in
`nb_01` (1.1, 1.2, 2.2, 2.3, 3.1, 3.2, boss) is the complete, paste-able answer. In AI-free
Part I the hint accordion is the sanctioned help channel — a one-click full solution trains
exactly the reach-for-the-answer reflex the course is trying to delay, and it makes the ✅
meaningless as self-assessment. **Fix the pattern in the template first** (Plans 2–4 copy it):
Hint 2 shows structure with a blank (`revenue_ex12 = round(??? * ???, 2)`); full solutions
belong in the post-session solution notebooks (see #4). This is the highest-leverage
pedagogy fix in the slice.

### 4. SHOULD-ADDRESS — Post-session solution notebook pattern is unproven (missing slice piece)
Spec §4/§5 promise read-only WASM solution notebooks published after each session, held in the
private repo. Plan 1's stated goal was "prove every pattern the remaining plans copy" — this
pattern (export mode? `--mode run`? where do they land in nav? publish trigger?) has no
exemplar. Author `nb_01`'s solution notebook and settle the mechanics at the very start of
Plan 2, before 8 more sessions of content assume it. (Also the natural home for the full
solutions removed from Hint 2.)

### 5. SHOULD-ADDRESS — Chatbot hint-only system prompt is scheduled in no plan
Spec §5/§7: chatbot "untouched except system-prompt update (hint-only in Part I, knows the
startup arc)". It appears in neither Plan 1 nor the sketched scope of Plans 2–4, yet it is the
sanctioned helper from Session I's lab onward — if it still gives full solutions on day one,
the AI-free story is undermined by the course's own website. Small task; just make sure it has
a home (Plan 2) and lands before Session I.

### 6. SHOULD-ADDRESS — Boss exercise doesn't actually combine the session's skills
`nb_01_lab_founding.py` ex40. Spec: the boss "combines the session's skills and resolves the
episode". As built it's "write an f-string containing the literals 26.70 and 2.59" — Hint 2
even formats literals (`{26.70:.2f}`), an idiom that teaches nothing. Reframe the task text and
hints to reuse `revenue_ex12` / `margin_ex22` (marimo's cross-cell reactivity is the whole
point being showcased), while keeping the tolerant contains-check so unsolved prerequisites
degrade to ❌ rather than error. The startup-name reuse is already the right instinct — extend
it to the numbers.

### 7. SHOULD-ADDRESS — molab button is published before the spike-3 verification
`tutorials/tut_01_introduction.qmd` ships the molab badge, but the spec (§4, §9 spike 3)
says verify the undocumented login flow before publishing the button, and dress-rehearsal
item B5 is still open. Fine on this unmerged branch; make B5 an explicit gate for merging/
semester start (or comment the badge out until verified). The URL targets `blob/main/…`,
which only resolves after merge — consistent with that gating.

### 8. SHOULD-ADDRESS (template-level, one line) — `show_result` helper cell is visible code
In `_template.py` and `nb_01` the helper cell lacks `hide_code=True`, so the first substantive
code an absolute beginner scrolls past is a `def` with `isinstance` — Session III material as
day-one noise. Hide it in the template now so Plans 2–4 inherit the fix.

### 9. NICE-TO-HAVE — nb_01 ordering and labeling wobbles
- Core MCQ (`ex50`) sits *after* the bonus price-war (`ex60`); students who stop at "bonus"
  will miss a core exercise below it. Put all cores before all bonuses.
- Ex 2.1 is labeled "(core, trace)" but doesn't count in the 7-core progress cell (header
  promises 7, and 8 items say "core"). Relabel "(trace — ungraded)".
- The "Welcome to **{name}**!" greeting cell renders *above* the name input, so the payoff
  fires before the student finds the box — weakens the first marimo wow-moment. Swap the cells.

### 10. NICE-TO-HAVE — In-lecture exercise letters don't match presentation order
Deck order is a → c → b (variables, f-strings, arithmetic) because the old deck's topic order
differs from the lab's. Spec says letters map to lecture blocks 1:1. Likely self-resolves in
the Plan-2 lecture rewrite — but write the rule down now (letters = slide order) so the
naming convention Plans 2–4 copy is unambiguous.

### 11. NICE-TO-HAVE — Small exercise-design frictions
- `ex_01_a`: instructs "first predict which lines are wrong", but inline comments label all
  three problems. Keep the gentle version, drop the fake predict framing (or drop the labels).
- `ex_01_b`: packs two concepts (precedence prediction + floor/mod computation) into one
  "5 min" sandbox — mildly over the one-concept rule; acceptable, but expect 8–10 min.
- Investor cameos throughout Session I check messages ("the investor nods…"), though spec
  casts the investor as a Part-II arrival. Accept as cameo or swap lines to Tobi — just keep
  the canon deliberate.

### 12. DEFERRAL-OK — Correctly deferred, with two scheduling notes
- `nb_01_sidequest_*`: buffer scope by spec — fine. (Fast finishers currently have ~10 min of
  bonus; acceptable for Session I.)
- `general/ai-tools.qmd`, `general/git-basics.qmd`: Part II / Session X — fine.
- Lecture content rewrite (beyond #2's factual patches), `/humanizer` pass, warm-up-quiz
  pattern (first needed Session II), tutorials 02–09 conversion — fine.
- **Nav cleanup**: `_quarto.yml` still lists the retired Assignments section and old
  tutorial pages — must be in Plan 4's cleanup checklist, not forgotten.
- Take-down-after-CP and per-student variants: explicitly parked as an open decision
  (follow-ups §3.5) — the baseline model is honest without them; fine.

---

## Reviewed and found sound
- **End-to-end coherence:** template → lab → exercises → launcher → QR slides → cp0 → grader
  genuinely hang together; every pattern the plan promised exists and is copied consistently.
- **Weekly rehearsal loop is real:** all four CP task types are practised in nb_01 (write ×3,
  radio-trace, fix-Tobi's-bug, MCQ-as-code), the progress cell mirrors the CP score cell, and
  the wrap-up ritual mirrors the submission motion. cp0 is a faithful mini (3×2 pts vs 6×2).
- **Honest persistence story, everywhere:** the spike-corrected reload-keeps/tab-close-loses/
  download-is-the-only-guaranteed-copy wording is consistent across template, nb_01 wrap-up,
  and tut_01 — and it strengthens the download ritual rather than weakening it. Exemplary
  spike→copy correction loop.
- **Checkpoint enforcement model:** submission window + supervision + AI-resistant task design
  + hashed live checks + hidden server suite + manual-review bucket + public/private repo
  separation (deploy script refuses the public path) is coherent and honest about its limits.
- **Difficulty ramp & dosage:** 1.1→boss ramps sensibly for absolute beginners; 45–60 min is
  realistic; `show_result` (esp. fenced-block string echo for receipts) is a genuinely good
  addition; sitcom-in-notebooks / restrained-in-slides split is executed as specced, and the
  Tobi/authorities/MunchCorp beats land at the right dosage — motivating, not gimmicky.
- **Syllabus alignment:** Session I content (syntax, variables, types, arithmetic, strings/
  f-strings) matches both syllabus texts and the Episode-I beats (founding, naming, 9.99
  theory) with no scope creep.

---

**Verdict:** Yes — the Plan-1 slice is a sound foundation for Plans 2–4, provided the grader's
function-task gap (#1) is settled before CP2 authoring and the three factually-wrong lec_01
slides (#2) are patched rather than left to ride on Plan 2's schedule.
