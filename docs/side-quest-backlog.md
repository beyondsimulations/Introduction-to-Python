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
- lec_05: custom exception classes (`class InvalidUsernameError(Exception)`) — inheritance is out of scope; the course stops at one small class in Session III
- lec_05: the full built-in-exception catalogue (`NameError`, `AttributeError`, `ImportError`, `SyntaxError`, `IndentationError`, `RuntimeError`, `FileNotFoundError`) — trimmed to the "big five" students actually hit; recognise the rest by reading the last line
- lec_05: `except ... as e` variable binding as its own teaching point — used in worked examples, but the mechanics slide is cut for CP-day time
- lec_05: IDE debugger walkthrough (Zed breakpoints / step-over / variable viewer) — no IDE in the WASM lab; `print()` is the beginner's flashlight instead
- lec_05: the `if __name__ == "__main__":` main-function pattern + script organisation slides — belongs with modules/imports (Session VI), not the errors day
- lec_05: `logging` module overview — beyond scope for beginners; a larger-codebase concern, cut

## Material cut from lecture decks (Plan 3 rewrites)
- lec_06: regular expressions (whole section — `re.search/findall/sub/split`, character classes, quantifiers, email/date patterns) — rich but heavy for a CP-day; returns as a side-quest ("regex treasure hunt": hunt patterns out of log/receipt text)
- lec_06: `os` module (`listdir`, `path.exists`, `makedirs`) — needs a real filesystem; Session X preview when we leave the WASM browser for real files
- lec_06: `csv` module (`csv.writer`/`csv.reader`, writing `secret_message.csv`) — real file I/O; Session X (and tabular data proper lands in pandas, Session VIII)
- lec_06: creating your own module files (`import lec_06_new_module`, `from ... import another_function`) — needs real `.py` files side-by-side; Session X where students work in a real editor/filesystem
- lec_06: installing packages + virtual environments with uv (`uv add`, `uv sync`, `uv run`) — no shell in the WASM lab; Session X where the local toolchain is set up
- lec_07: fancy indexing (`data[np.array([0, 2, 4])]`) — niche beside boolean masks; returns as a side-quest once positional selection is actually needed
- lec_07: dtype character codes (`'i'`/`'f'`/`'S'`/`'U'`) + bits/precision section (int8/int16/float32, ranges, `.astype`) — hardware-flavoured detail; revisit if a memory/precision bug ever bites in a later data session
- lec_07: joining arrays (`concatenate`, `hstack`, `vstack`) — array assembly is rare for beginners; folds into pandas concat/merge in Session VIII
- lec_07: heterogeneous arrays (`np.array(["s", 2, 2.0])`) — anti-pattern for beginners; one-line mention stays in the deck ("one dtype for the whole array"); full treatment only if a side quest needs mixed data
- lec_07: matrix multiplication `@` vs element-wise `*` — linear algebra is out of scope for this course; side-quest for a maths-heavy cohort
- lec_07: `np.random` (numpy's own RNG, `rand`/`randint`) — superseded by the `random` module taught in Session VI; one RNG story is enough, numpy's is cut; returns if a Part-III project needs vectorized sampling
