# Side-quest & cut-material backlog

Buffer scope (spec §4): authored last, cut first, never blocking semester start.

## Side-quest ideas (per episode)
- Ep. 2: Haggling Bot extended — multi-round supplier negotiation with mo.ui.
- (add as they come up during deck cuts)

## Material cut from lecture decks (Plan 2 rewrites)
- (one line per cut concept: "lec_02: while/else clause — niche, cut")
- lec_02: `+=` / `-=` / `*=` compound-assignment operators — useful shorthand, but the accumulator pattern is taught longhand first; revisit as a Session-IV convenience note
- lec_02: membership operators (`in` / `not in`) — belong with sequences in Session IV where lists/dicts are taught properly
- lec_02: indexing & slicing (`s[0]`, `s[-1]`, `s[start:stop:step]`) — moved to Session IV (matches lec_01's slicing cut)
- lec_02: `**` exponentiation and `dir()` introspection — niche for beginner control-flow day, cut
- lec_02: objects/methods framing slides (everything-is-an-object) — string methods now taught directly without the abstract preamble
- lec_01: input() + type conversion (int/float/str/bool of input) — WASM notebooks have no stdin; revisit if a UI-input exercise appears
- lec_01: string indexing / slicing / len() / repeat (`*`) — moved to Session IV where sequences are taught properly
- lec_01: live SyntaxError demo (broken quotes) — errors get full treatment in Session V
- lec_01: `**` exponentiation operator — niche for beginner money math, cut
- lec_01: Zen of Python (`import this`), expressions-vs-statements, and legacy `.format()` interpolation — cultural/legacy filler, cut
- lec_01: "Learning Path" slide (help-each-other, docs/StackOverflow, frustration blog post, typo-reporting process) — practical support guidance, no substitute in new deck
- lec_01: "My Recommendation" slide (3-step study recipe + Codewars pointer) — concrete external practice resource
- lec_01: "Goals of the Course" slide (named AI usage as an explicit course goal) — goals framing not fully covered by "How to use AI"
- lec_01: "Teaching" slide (lecture-vs-tutorial format mechanics) — course-mechanics info
- lec_01: "Python as Language" slide (origin/use-case orientation) — nice-to-have context
- lec_03: recursion (`fibonacci`, `countdown`) — elegant but not needed for the receipt/class arc; revisit as a side-quest
- lec_03: docstrings + `help()` on functions — good hygiene, cut for CP-day time budget; fold into a lab note
- lec_03: the `global` keyword — deliberately omitted; the course's stance is "catch the return", not mutate globals
- lec_03: inheritance / superclass-subclass slides — out of scope (course explicitly stops at one small class)
- lec_03: class attributes (shared vs instance) and the encapsulation framing slides — deeper OOP, cut for beginners
- lec_03: multiple/keyword positional-argument ordering demo (`call_parameters(b=..., a=...)`) — niche, cut for time
- lec_04: tuple methods (`.count()`, `.index()`) and tuple unpacking (`name, *rest = ...`) — one honest tuple slide replaces the full tour; revisit unpacking as a Part-II convenience note
- lec_04: tuples-returned-from-functions slide — folds naturally into the functions material; not needed for the data-structures day
- lec_04: set-theory methods (`union`, `intersection`, `isdisjoint`, `issubset`) — sets earn one uniqueness slide; the algebra is a side-quest
- lec_04: the big data-type comparison table (mutable/ordered/duplicates) + "when to use which" slides — encyclopedic; the blocks teach each type in context instead
- lec_04: `timeit` membership-speed benchmark slide — performance framing is premature for beginners, cut
- lec_04: file I/O (`open`/`with`, read/write modes, `input()`) — WASM notebooks have no filesystem; real files land in Part III, pandas in Session VIII (replaced by the inline-data slide)
- lec_04: generator expressions (`(x for x in ...)`) — niche beside list/dict comprehensions, cut for beginners
