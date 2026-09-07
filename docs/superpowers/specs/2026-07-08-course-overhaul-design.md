# Introduction to Python — 2026 Course Overhaul Design

**Date:** 2026-07-08
**Status:** Approved design, pending implementation plan
**Course:** Programming with Python, KLU, Semester 3 2026, pass/fail, ~10–20 students, 13 sessions × 4 academic hours (~3h real time)

## 1. Why this overhaul

- GitHub Copilot's free student plan has **new sign-ups paused indefinitely since April 2026** (existing verified students keep it with restricted model choice) — a fresh cohort cannot rely on it, so the AI tooling story must be rebuilt (Mistral Free, own subscriptions, Zed). Course materials say "paused", not "ended".
- Students must master basics *before* leaning on AI — the new syllabus (`klu_syllabus.md`) keeps Part I AI-free. **Parts I and II are both assessed via the 5 in-class checkpoints** (CP1–3 on Part I material, AI-free; CP4–5 on Part II material, AI allowed).
- Lectures should be hands-on, not passive: marimo notebooks in the browser, business-student motivation via a semester-long startup narrative (modeled on the Management-Science course's `nb_XX_YY` notebooks).
- Everything must be ready **before semester start**.

## 2. Decision summary

| Topic | Decision |
|---|---|
| Marimo scope | Tutorials + short in-lecture exercises; revealjs lectures stay |
| Hosting | Self-hosted WASM exports inside the Quarto site; optional molab links |
| Part III | Plain `.py` files in Zed — **no local marimo** |
| Narrative | One fixed campus **food-delivery startup**, student-named, mini-games woven in |
| Checkpoints | 5 marimo WASM notebooks, auto-graded via embedded tests, 12 pts each |
| Submission | Download `.py` → Moodle upload; grading script re-runs reference tests |
| Session shape | Interleaved 20-min lecture blocks + 10-min exercises + ~60-min lab block |
| CP timing | First ~40 min of the *following* session (sessions III, V, VI, VIII, X) |
| Missed CPs | No make-ups; point math absorbs one miss (88 pts still reachable) |
| CP privacy | Private companion repo; WASM deploys to a **separate host** (private-repo GitHub Pages via free GitHub Education Team, or Cloudflare Pages) — never through the public course repo |
| Git | Taught in Session X (trimmed 60–90 min session from the other lecture) |
| Project submission | GitHub repo per pair + AI-disclosure note |
| Chatbot | Kept as-is; hint-only mode in Part I; system prompt updated |
| AI tools | Mistral Free (guaranteed), own ChatGPT/Claude/Mistral subs, Zed + Zed student program; Copilot removed everywhere |

## 3. Course architecture

### Session map (13 × ~3h)

| # | Session | Checkpoint at start |
|---|---|---|
| I | Welcome & Introduction — startup founding, syntax, variables, types | — |
| II | Control Structures (+ comprehension seeds, idiomatic loops) | — |
| III | Functions & Classes | **CP1** (sessions I–II) |
| IV | Data Structures (lists/tuples/sets/dicts, I/O, comprehensions) | — |
| V | Errors & Debugging | **CP2** (sessions III–IV) |
| VI | Modules & Packages, random | **CP3** (session V + Part I recap) |
| VII | NumPy | — |
| VIII | Pandas + AI craft (prompting, verifying output, hallucinated APIs, disclosure; heavy data-wrangling practice) | **CP4** (sessions VI–VII) |
| IX | Plotting + AI; homework: install uv + Zed | — |
| X | **Tooling, Git & Project Kickoff** — uv, Zed + AI setup, git (init/commit/push/clone/pull, GitHub), "a marimo notebook is a `.py` file" reveal, group formation, project choice | **CP5** (sessions VIII–IX) |
| XI | Project work under assistance | — |
| XII | Project finalization | — |
| XIII | Presentations & discussion | — |

Syllabus tweaks are limited to session titles/descriptions (allowed); the 3-part structure and lecture count stay.

### Regular session shape (~180 min)

```
0:00 Warm-up / recap quiz (10)          1:25 Lecture block 3 (20)
0:10 Lecture block 1 (20)               1:45 In-lecture exercise (10)
0:30 In-lecture exercise via QR (10)    1:55 Lab: tutorial notebook in class,
0:40 Lecture block 2 (20)                    instructor circulates, chatbot
1:00 Exercise (10) → BREAK (15)              gives hints (~60)
                                        2:55 Wrap-up, preview (5)
```

Checkpoint sessions: CP occupies the first ~40 min (generous, no rush, no retake mechanism); the rest of the session compresses to 2 lecture blocks + lab.

Lectures are scoped to 3 × 20-min blocks — existing decks must be trimmed/split accordingly.

## 4. Content design

### The startup arc — a sitcom in 9 episodes

One fixed **campus food-delivery startup**. Students "found" it in Notebook 1.1 and name it via `mo.ui.text`; the name propagates reactively through the notebook (first marimo wow-moment). Mechanics, data, and all grading asserts are **name-agnostic**. Each notebook re-asks the name in its first cell — WASM notebooks are standalone, so no cross-notebook state; the re-ask is a deliberate, robust design choice (works identically in browser/molab/local; can be played for laughs).

**Tone:** full sitcom in the notebooks; slides stay restrained (story as framing, jokes sparse).

**Recurring cast:**
- **Tobi, the co-founder** — confident, terrible ideas, worse code. Source of debugging exercises (his 3-AM checkout script), messy data (his Excel exports), and chart crimes (his pitch slides).
- **The investor** — appears in Part II demanding numbers, dashboards, "insights by Friday."
- **The authorities** — German bureaucracy as running gag (health inspector, data-protection office, *Formular 27b/6*).
- **MunchCorp** — the soulless mega-competitor (price wars, competitive analysis).

**Episode beats (session → story → topic):**

| # | Episode | Topic payload |
|---|---|---|
| I | Founding: name the company, first menu; Tobi wants all prices at 9.99 "for psychological reasons" | syntax, variables, types, arithmetic |
| II | City decrees no delivery after 22:00; discount rules; **Haggling Bot** game (guess-the-number reskin) | conditionals, loops, string methods |
| III | Copy-paste soup → reusable receipt/tip/discount functions, `Order` class; **Tip Calculator Championship** (whose function survives the weirdest inputs) | functions, scope, classes |
| IV | Menu becomes a dict, delivery zones nested structures; **A Day as a Courier** text adventure on a dict-based campus map | lists, tuples, sets, dicts, I/O |
| V | Tobi coded the checkout at 3 AM on energy drinks — debug it; health-inspector audit ("every order MUST have price ≥ 0") | exceptions, try/except, debugging, assertions |
| VI | Demand simulation with event cards ("influencer visits", "rain doubles orders"), dice-delivery mini-game; **the government episode**: data-protection office demands all emails/phones/names redacted from a reviews file before publication | modules, random, string methods, `re` |
| VII | Investor wants delivery-time statistics; zone×hour arrays; **Beat the Average** (optimize a schedule against class stats) | NumPy |
| VIII | Due diligence: sales data is Tobi's Excel export (duplicates, "12,50 €" as text, three date formats); AI allowed as the new intern whose work must be verified | Pandas, data cleaning, AI craft |
| IX | The pitch deck; **Chart Crimes** — spot Tobi's manipulated axes, then build the honest dashboard | Matplotlib, data literacy, critiquing AI output |
| X–XIII | Exit: the startup "gets acquired"; students spin off their own ideas as the final project | project phase handoff |

Checkpoints get one line of story flavor each ("quarterly board review") — zero extra grading complexity. No KLU-specific locations (no campus cafeteria exists); campus references stay generic.

### Notebooks

**Per lecture: one main lab notebook + one optional side quest** (not 2–3 equal notebooks):

- `nb_XX_lab_<topic>.py` — ~45–60 min of core exercises for the consecutive end-of-session lab block. Arc: story cold-open → teach/try sections → one **boss exercise** combining the session's skills and resolving the episode. Exercises marked *core* vs *bonus*.
- `nb_XX_sidequest_<topic>.py` — optional extra practice for fast students / homework. Never required.
- In-lecture exercises `ex_XX_[a-d].py`: single-concept, 5–10 min, one screen (no scrolling), named by lecture block so slides map 1:1. **Predict-first pattern**: slide shows code → students commit to a prediction → then run to verify. Each ends with "nothing to save — this was a sandbox."

**Reactive-notebook mechanics (the marimo advantage over the Jupyter-style Management-Science pattern):**

- **Reactive checks, not test cells**: a check cell below each exercise re-runs automatically on any code change and renders ✅/❌ with a message — no "run the test cell" step.
- **Live progress cell** at the bottom of every notebook ("Core exercises: 6/8 ✅", story-skinned as Tobi's approval) — the same mechanic as the checkpoint score cell, rehearsed weekly from Notebook 1.1.
- **Graduated hints** per exercise via `mo.accordion`: Hint 1 (nudge) → Hint 2 (structure). Full solutions published *after* each session as separate read-only WASM notebooks. Built-in help reduces AI temptation in the AI-free phase.
- **Checkpoint task types rehearsed weekly**: every lab notebook contains all four CP task types — write a function, trace code (predict-before-run via `mo.ui.radio` with reveal), fix a bug (Tobi's code), MCQ. By CP1, only the stakes are new.
- **Wrap-up ritual** (last 5 min of lab): progress-cell check, download-your-`.py` reminder, next-episode teaser — weekly rehearsal of the checkpoint submission motion.

**Authoring rules:**

- `notebooks/_template.py` is built first and every notebook inherits its skeleton (cold-open, section rhythm, check-cell pattern, hint accordion, progress cell, estimated time at top, download reminder, teaser).
- Marimo forbids redefining a global across cells — **and `+=`/`-=` count as redefinitions**. Exercise cells use disciplined suffix naming (`price_ex2`); underscore-prefixed names (`_tmp`) are cell-private and reusable. Codified in the template, not tribal knowledge.
- **Placeholder discipline:** every exercise cell pre-defines its answer name (`revenue_ex2 = None  # YOUR CODE BELOW`) so reactive check cells always run and degrade to "not attempted yet" instead of erroring.
- Datasets load via `mo.notebook_location()` from a `public/` folder (documented to work in WASM and locally). Keep datasets small: WASM has a **2 GB memory cap** and weak laptops crash on data-heavy cells.
- Side quests are **buffer scope**: authored last, cut first, never blocking semester start.

Topic gaps folded in: comprehensions/idiomatic Python (sessions II & IV), extra data wrangling incl. messy CSVs and groupby (session VIII notebooks), AI craft (session VIII lecture + woven through IX), environment/tooling + git (session X).

### Student access: two buttons, honest labeling

Every tutorial page offers both, with the differences stated plainly:

- **"Open in browser" (recommended default):** runs entirely on your machine in the browser tab — after the page loads, no internet or account is needed. Your work usually resumes automatically when you reopen the page **on the same computer and browser** (stored in browser storage — lost if you clear browser data, use private mode, or switch machines). Download your `.py` anytime as a safety copy.
- **"Open in molab" (for cross-device certainty):** marimo's free cloud service (account required; the login method is undocumented — verify on the live site before publishing instructions). Opening our notebook forks a personal copy that autosaves to the student's account and reopens on any device. Use this if you know you'll switch computers or want to be certain nothing is lost. Optional — nothing graded ever requires it. Note for students: sessions idle >90 min are shut down (work is saved).

Known one-way door, stated in course FAQ: a downloaded `.py` **cannot be uploaded back** into the browser editor; it is for submission, backup, and later local use in Part III.

In-lecture exercises: browser button only (ephemeral by design). Checkpoints: neither button — unlisted URL handed out in class.

## 5. Technical architecture

### Repo layout (public course repo)

```
notebooks/                    # marimo .py sources (source of truth)
  _template.py                # skeleton every notebook inherits (built first)
  nb_XX_lab_<topic>.py        # main lab notebook per lecture
  nb_XX_sidequest_<topic>.py  # optional extra practice
  exercises/ex_XX_<a-d>.py    # in-lecture, named by lecture block
helpers/export_marimo.sh      # marimo export html-wasm --mode edit per notebook
helpers/convert_qmd_to_md.py  # existing post-render (kept)
lectures/lec_XX_*.qmd         # revealjs, updated: startup examples, QR exercise slides, Copilot removed
tutorials/tut_XX_*.qmd        # slimmed to intro + the two buttons per notebook
general/ai-tools.qmd          # NEW: Mistral Free, Zed student program, own subs, disclosure rules
general/git-basics.qmd        # NEW: companion page to Session X git material
```

- Build: Quarto render + marimo WASM export step (locally and/or CI) placing exports under the published site (e.g. `_site/notebooks/<name>/`). One pipeline, one URL space, course branding.
- WASM notebooks are served as normal same-origin pages (required for localStorage-based resume; **no sandboxed iframes**).
- Pyodide covers numpy/pandas/matplotlib. No network calls in notebooks; datasets ship with the notebook (inline or `public/` files).
- Existing chatbot untouched except system-prompt update (hint-only in Part I, knows the startup arc).

### Private companion repo (`Introduction-to-Python-checkpoints`)

- 5 checkpoint notebooks + reference solutions + **hidden reference test suites** (extra cases beyond the embedded live checks) + post-session solution notebooks for the tutorials (committed to the public repo only after the relevant session).
- `grade_checkpoints.py`: takes a folder of Moodle-downloaded submissions, executes each in an isolated subprocess with a timeout, extracts defined names (via marimo's documented `outputs, defs = app.run()` if the download is notebook-format, or namespace-exec if it is a flat script — day-1 spike settles which), runs the reference tests, emits a points CSV. Submissions that fail to execute (syntax errors, renamed cells) land in a **manual-review bucket**, never crash the run.
- **Deploy target is NOT the public course site** (its repo is public — exported WASM assets would expose checkpoint source pre-session, with CI-minutes latency at that). Instead: GitHub Pages of a private repo — free via the **GitHub Education Teacher benefit** (free GitHub Team unlocks Pages on private repos; the served site is public-but-unlisted, source stays hidden) — or Cloudflare Pages free tier as fallback. QR/short link shared in class.
- Checkpoint WASM code is **always retrievable by students** (marimo docs: code-hiding flags are "aesthetic choices, not security features"). Therefore: live feedback checks in checkpoints use **hashed expected values** (`sha256(answer) == "<hash>"`) so they can't leak trace/MCQ answers, and the real referee is the hidden server-side suite.

## 6. Checkpoints & grading

- 5 checkpoints × 12 points = 60; pass needs 60/100 total (project + presentation = 40) plus 75% attendance.
- Internal structure per checkpoint: ~6 tasks × 2 points, **all-or-nothing per task**; live score cell shows the provisional result before submission.
- **Everything graded is a code assignment, never UI-element state** (verified: the downloaded `.py` contains code only — `mo.ui` values are not serialized). MCQs are answered as `answer_q3 = "B"`; identity is `STUDENT_NAME = "..."` / `STUDENT_ID = "..."` assignments at the top. `mo.ui` widgets appear in checkpoints only for ungraded convenience, if at all.
- Task mix (per syllabus): write a function, trace code ("what does this print?"), fix a bug, MCQs — all as code assignments per the rule above.
- Identity: Moodle identifies the uploader (primary); the in-file `STUDENT_ID` assignment is the cross-check. Filename convention is a nice-to-have, not load-bearing.
- Flow: unlisted URL at session start → ~40 supervised minutes → download `.py` → Moodle upload with deadline. Moodle provides identity + timestamps.
- AI-free enforcement (CP1–3): supervision + AI-resistant task design (tracing, debugging, twists on in-class material, tight timing). Social enforcement, not technical lockdown.
- CP4–5: AI explicitly allowed per syllabus.
- Missed checkpoints: no make-ups; only documented long absences get individual arrangements.

## 7. AI & tooling story

- **Part I (sessions I–V):** no AI. Course chatbot (hint-only) is the sanctioned helper.
- **Part II (VI–IX):** AI allowed and taught. Session VIII front half = AI craft. `general/ai-tools.qmd` documents (all facts verified July 2026, re-verify before publishing):
  - **Zed education**: 12 months Zed Pro + $10/month AI credits for enrolled students; info at zed.dev/education, apply at dashboard.zed.dev/education/apply. Note the 12-month expiry.
  - **Provider truth table for Zed**: ChatGPT Plus/Pro works via native OpenAI sign-in (no API key); **Claude Pro/Max does NOT work with Zed's built-in Anthropic provider** (needs separate API credits — document the distinction so students aren't surprised); Mistral requires a free La Plateforme API key.
  - **Mistral Free** (the guaranteed zero-cost baseline): free Le Chat + free La Plateforme Experiment API tier usable in Zed. Do **not** publish rate-limit numbers (account-specific, unpublished); do flag that free-tier API data is used for training by default and show the opt-out (Admin Console → Privacy).
  - **OpenRouter free models** as one-line no-credit-card fallback.
  - **Copilot**: described as "new sign-ups paused indefinitely since April 2026" — students verified before then may still have it and may use it.
- **Session X:** local environment together — uv, Zed (with chosen AI provider), git session (trimmed import from the other lecture: init/commit/push/clone/pull + GitHub; no branching/PRs).
- **Part III (X–XIII):** plain `.py` development in Zed. GitHub repo per pair = collaboration + submission channel (repo link + AI-disclosure note); commit history doubles as process evidence.
- All Copilot references removed from lectures, FAQ, and installation guides.

## 8. Retired / kept

- **Retired:** the 2 assignments (replaced by checkpoints), Copilot content, tutorials as homework-style `.qmd` exercise pages.
- **Kept:** revealjs lecture format (updated), Quarto site + publishing pipeline, chatbot, uv-based Python setup (moves to Session X), Management-Science course as untouched style reference.

## 9. Risks & early verification spikes

Verification status (July 2026, three-agent doc/web review): download-as-`.py` in WASM edit mode CONFIRMED (recently hardened, PR #9268); localStorage persistence on same-origin pages CONFIRMED (embedding guide); UI-state-not-in-`.py` CONFIRMED; `app.run()` grading path CONFIRMED; numpy/pandas/matplotlib preinstalled in WASM CONFIRMED (2 GB memory cap); `mo.notebook_location()` CONFIRMED; single-definition constraint CONFIRMED. Remaining spikes:

1. **Download format** (day-1 spike): confirm whether the edit-mode download produces the decorated notebook format (gradable via `app.run()`) or a flat topologically-ordered script (gradable via namespace-exec) — the grading script supports whichever it is; graded names are plain assignments either way.
2. **End-to-end dress rehearsal**: author one dummy checkpoint, deploy to the private-Pages host, take it as a student on a weak laptop, download, upload to Moodle, grade — before session I.
3. **molab login flow**: undocumented — do one live pass and screenshot it for the course FAQ before publishing the button.
4. **GitHub Education Teacher verification**: apply early; it gates the private-repo Pages deploy path (fallback: Cloudflare Pages free tier, verified viable).
5. **Checkpoint gameability**: hidden server-side reference suite is the referee; embedded live checks use hashed expected values. Accepted residual risk: a determined student can read checkpoint code — supervision + task design carry the rest.
6. **Session X density** (tooling + git + kickoff + CP5): dry-run the timing; fallback is moving CP5 to end of session IX.
7. **molab dependency**: optional-only by design ("free as long as usage is reasonable" is a soft promise); if it tightens, students lose a convenience, not a course component.
8. **No load-time claims**: do not publish WASM startup-time numbers in course materials without measuring on real hardware.

## 10. Out of scope

- Chatbot re-engineering (context-aware hints) — possible later project.
- GitHub Classroom / CI autograding.
- Rewriting the Management-Science course.
- Any grading beyond pass/fail mechanics.

## 11. Success criteria

- A student with zero setup can do every graded activity through session IX with only a browser and Moodle access.
- All 5 checkpoints + grading script tested end-to-end (author → deploy → student flow → grade → CSV) before session I.
- Every lecture session has its in-lecture exercises and lab notebook ready before the semester starts.
- The AI-tools page gives every student at least one zero-cost working AI setup (Mistral Free + Zed) for Part II.
