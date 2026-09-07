# Plan 5 Editing Brief — the single source of truth for the copy pass

**Date:** 2026-07-13 · **Spec:** `2026-07-13-plan5-humanizer-design.md` · **Scout data:** full-corpus sweep 2026-07-13 (74 files)

## What this is

You are rewriting student-facing prose in a Python course. This brief is your entire rulebook: what to remove, what to add, what register to write in, and what you may never touch. Work file by file. Edit prose only. When a sentence is already good, leave it alone — do not manufacture diffs. Run the self-check at the end before committing.

## AI tells to remove

The corpus was scanned; most classic AI vocabulary is **already absent** (zero hits on delve, crucial, pivotal, testament, showcase, leverage, seamless, robust, additionally/furthermore/moreover, "serves as", "at its core"…). Do not hunt for ghosts. The real findings, in priority order:

1. **Em dashes — the one big tell.** 2,171 across the corpus; the densest labs carry 90–113 each. An em dash must be a choice, not a default. Most should become a comma, a colon, a period and a new sentence, or parentheses. Keep an em dash only where the interruption is the point (a reveal, a punchline, a hard turn). Rough target: well under half of what you found, and never twice in one paragraph without a reason.
   - Before: "…just say yes to every order — today the code starts making decisions"
   - After: "…just say yes to every order. Today the code starts making decisions"
   - Keep (earned): "read, fix, recover — is what debugging *is*" (the dash sets up the landing; one per section like this is fine)
2. **Mechanical boldface.** Bold is for the term being defined or the one thing to remember on a slide, not for rhythm. If a sentence bolds two or more phrases, unbold all but the load-bearing one. (Bold inside load-bearing labels like "**assert**" when introducing the keyword is correct.)
3. **Rule of three / negative parallelism / -ing tack-ons / significance inflation.** Scan hit near zero, so treat these as things you must not *introduce*, and fix the rare one you meet. Never add "not just X, but Y", never end a sentence with ", highlighting/ensuring/reflecting…", never write "in today's world of".
4. **Filler and hedging.** "In order to" → "to", "the ability to" → "can", "it is important to note that" → cut, "at this point in time" → "now". One qualifier per claim, max.
5. **Uniform sentence length.** The subtlest tell. If three consecutive sentences have the same shape, break one: make it short. Or let one run longer than the others and land somewhere specific.

## Voice: what to add (register permitting)

- **Rhythm variation.** Short sentence after a long one. A one-word verdict is allowed ("Wrong.", "Almost.").
- **First person, sparingly** (deck register only): "I keep seeing this one in office hours" beats "This is a common error."
- **Opinions over neutral reporting** (deck register): "This error message is genuinely unhelpful, and Python should be embarrassed" is better teaching than "The error message can be difficult to interpret."
- **Specificity over vibes.** Not "this is a powerful technique" but what it actually buys: "this turns 40 lines of copy-paste into 4."
- **The cringe bar is absolute.** If a joke needs a wink to land, cut it. No memes, no "fellow kids" energy, no exclamation-mark enthusiasm. When unsure whether something is funny, it is not; write it straight.

## Register cards

- **`deck`** (lectures/lec_01–10): lively but restrained. First-person instructor asides allowed. The bar: something an instructor would say out loud to a room without wincing. Episode/story slides may sharpen jokes and dialogue; canon is frozen (see guardrails).
- **`reference`** (general/, tutorials/, index.qmd): sober, scannable, zero jokes. The reader may be debugging at 23:00. Short sentences, concrete instructions, no personality injection — clarity IS the voice here. Scrub tells, tighten, stop.
- **`notebook`** (notebooks/, exercises/, private CP + solutions): dry and precise. Students read this while thinking about code, not about you. Light warmth allowed in wrap-up cells only ("That's the whole checkout flow. Tobi owes you one."). Prompts stay strictly matter-of-fact.

## US English

Convert every UK spelling. Found in the corpus (fix all of these):
- `behaviour` → `behavior` (×11: lec_03 ×5, tut_03, nb_03 ×3, sol_03 ×2)
- `practise` (verb) → `practice` (×9: identical sentence in all nine tutorials)
- `labelled` → `labeled` (×6: git-basics ×2, nb_01, nb_09, sol_01, sol_09)
- `recognise` → `recognize` (×3), `summarise(d)` → `summarize(d)` (×5), `memorise` → `memorize` (×2), `analyse`/`analysing` → `analyze`/`analyzing` (×2), `favourite` → `favorite`, `grey` → `gray`, `modelling` → `modeling`, `travelling` → `traveling` (×1 each)
- Leave alone: `towards`, `afterwards`, `backwards` (acceptable US), and anything inside `general/imprint.qmd` / `general/privacy.qmd` (out of scope).

## Term glossary (decided; winners bold)

1. **Lecture ⟨Roman⟩ / Session ⟨Roman⟩ / Episode ⟨Arabic⟩ is a deliberate three-layer system — keep it.** Deck titles say **Lecture VII**; cross-references in prose say **Session VII** ("we'll meet this again in Session IX"); the story layer says **Episode 7**. Never use Arabic numerals for Lecture/Session, never Roman for Episode. Fix any stragglers to this rule; do not unify the three layers.
2. **Exercise ⟨N.N⟩ in labs and lectures; Task ⟨N⟩ in checkpoints — keep both.** The split is load-bearing (grading strings, reference tests) and useful: checkpoints should feel different. Never rename either.
3. **The lab file:** call it **the lab** in decks and casual prose, **the notebook** when pointing at the artifact ("download the notebook"). The full form "lab notebook" only on first mention per document. Internal titles ("Notebook 1.1 — …", "# [To the Lab]") are load-bearing; do not touch.
4. **Slide set = "the slides"** in student-facing prose; never call it "the deck" outside HTML comments (narrative pitch-deck/numbers-deck uses are story canon, untouched).
5. **The project:** **"your project"** in running prose; **"final project"** for the formal first mention on a page (index, syllabus, lec_10 brief slide). Kill the one stray "mini project" (`general/syllabus.qmd:50`) → "final project".
6. **Pair/partner** stays the project unit ("your pair", "your partner"); never "team"/"group" for students. (Pandas `groupby` prose and story "growth team" are unrelated — leave.)
7. **Run** a cell, never "execute" (the two explanatory uses in lec_08/uv.qmd may stay if rewording hurts precision).
8. **Browser editor** is where notebooks open ("Open in browser" button label is frozen). Do not introduce "playground"/"WASM"/"online notebook".
9. **Solution notebook** is the term; drop the one-off "walkthrough" (`lec_10_projects.qmd:282`) unless it reads better as plain "solutions".
10. **Hint 1 / Hint 2** labels and `:::{.callout-tip}` markup are two different frozen systems; never convert one to the other.

## Hard guardrails (violations are review-blocking)

Never touch: code cells; commands; expected values/outputs; check-cell strings and logic; hashes and hash salts; hint-skeleton structure (Hint 2 = `___` skeletons); story facts, plot events, character facts, and every number in the story; grading rules and point values; links and URLs; QR slugs; file names and paths; YAML frontmatter keys; revealjs directives and CSS classes (`.exercise-slide`, `{.highlight}`, `:::{.callout-*}`); button labels ("Open in browser"); Moodle labels ("Checkpoint 1"); slide-title patterns ("# [To the Lab]", "Notebook N.N"); MCQ feedback neutrality (live checks say "recorded", never ✅/❌).

Prompts stay symptom-only: rewording an exercise prompt must never add an expected value, a bug location, or a solution shape that wasn't there.

Private repo (CP notebooks): variable names, expected values, task semantics, and points are frozen — reference tests key off them. Cross-read `reference_tests.py` for the file you edit.

Story canon: episode structure, plot beats, who-did-what, and all numbers are frozen. Wording, dialogue, and jokes may be sharpened within that frame.

## Banned-word list (feeds the Task 8 grep)

Regex-ready, prose scope: `delve|delving|pivotal|testament|tapestry|showcas(e|es|ing)|vibrant|foster(s|ing)?|leverag(e|es|ing)|seamless|groundbreaking|nestled|renowned|breathtaking|stunning|garner(s|ed)?|interplay|intricate|intricacies|enduring|crucial`

Current count: zero. The grep exists to prove the pass didn't *introduce* any.

**Allowlist (named false-positive senses, excluded from the grep's judgment):** `{.highlight}` span class and "highlight" as UI/styling; the `_` underscore character (never the verb "underscores"); `:::{.callout-tip}` markup and narrative "tip" (gratuity, Tip Calculator); narrative "deck" (pitch/numbers deck) and "slides" as verb; "team"/"group" in story or pandas contexts.

## Implementer self-check (run before every commit)

1. Did I change ANY line inside a code cell, command, check cell, or frozen label? (git diff shows only prose → good.)
2. Em dashes in my file: counted before and after? Meaningfully reduced, survivors earned?
3. Does every reworded prompt still withhold expected values and bug locations?
4. Register: would this read right in its context (deck aloud / reference at 23:00 / notebook mid-task)? Anything that could be called cringe? Cut it.
5. UK spellings in my file all converted; no banned word introduced; glossary rules 1–10 respected.
