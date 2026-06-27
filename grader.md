# Python Course Autograder — Skeleton

A design sketch for collecting marimo notebook submissions, grading them against
hidden tests in a sandbox, and writing scores back to your gradebook.

## Guiding principle

The autograder is a **correctness engine**, not an authorship check. A hidden test
suite gives full marks to correct code regardless of who (or what) wrote it.

- **Authorship** is solved by *observation* → Phase 1 checkpoints happen **in class**.
- **Correctness + record-keeping** is solved by this pipeline → used in **both** phases.

Same machinery in both phases; the only difference is whether the work was done in the
room (Phase 1, AI-restricted) or at home with AI (Phase 2).

---

## Architecture

```
                         ┌─────────────────────────────────────────┐
   STUDENT               │            YOUR STACK (existing)         │
 ┌──────────┐            │  Hono + Better Auth + Postgres + Drizzle │
 │ practice │  WASM      │                                          │
 │ in browser│◀──────────│  /exercises  (serves notebook .py)       │
 └──────────┘            │                                          │
       │ download .py    │                                          │
       ▼                 │                                          │
 ┌──────────┐  auth      │  POST /submit ──► submissions (status=   │
 │ solve in │  upload    │                    'queued')             │
 │  marimo  │───────────▶│                         │                │
 └──────────┘            │                         ▼                │
                         │              ┌────────────────────┐      │
                         │              │  GRADING WORKER     │ Python
                         │              │  (polls 'queued')   │      │
                         │              │   per submission:   │      │
                         │              │   docker run        │      │
                         │              │   --network none    │      │
                         │              │   pytest hidden/    │      │
                         │              │   --json-report     │      │
                         │              └─────────┬──────────┘      │
                         │                        ▼                 │
                         │   submissions.score, test_results ◀──────│
                         │                        │                 │
                         │                        ▼                 │
                         │                   gradebook view         │
                         └─────────────────────────────────────────┘
```

The web app (collection, auth, gradebook UI) stays in your TS stack. The grader is a
small **separate Python service** — it has to be Python to run pytest against student
code. The two talk only through Postgres (or one internal endpoint).

---

## The exercise contract

This is the convention that makes grading trivial. Each exercise is a **pre-scaffolded
marimo `.py`** you hand the student. They fill in function bodies; the function names are
fixed by the spec so your hidden tests know what to import.

Recommended: define solution stubs as marimo **top-level reusable functions**
(`@app.function`), because those are directly importable from the file
(`from submission import is_prime`). Fallback for anything that can't be a pure top-level
function: `marimo export script submission.py -o flat.py` and import the flattened script.

Two layers of tests:

- **Public** (shipped in the student's file, visible): a few basic cases rendered as a
  live reactive callout — instant "is this even working" feedback while they code.
- **Hidden** (lives only on your machine, never shipped): the edge cases that actually
  decide points. Hardcoding to pass the visible cases fails these.

---

## Data model (Postgres)

```sql
-- students come from Better Auth (users table)

create table exercises (
  id          uuid primary key default gen_random_uuid(),
  slug        text unique not null,          -- 'cp1-functions'
  title       text not null,
  phase       int  not null,                 -- 1 or 2
  max_points  int  not null,
  due_at      timestamptz,
  notebook    text not null                  -- the scaffolded .py handed to students
);

create table submissions (
  id          uuid primary key default gen_random_uuid(),
  student_id  uuid not null references users(id),
  exercise_id uuid not null references exercises(id),
  source      text not null,                 -- the submitted .py
  status      text not null default 'queued',-- queued|grading|done|error
  score       int,
  graded_at   timestamptz,
  created_at  timestamptz not null default now()
);

create table test_results (
  id            uuid primary key default gen_random_uuid(),
  submission_id uuid not null references submissions(id),
  test_name     text not null,
  passed        bool not null,
  points        int  not null default 0,
  message       text                          -- shown to student as feedback
);

-- gradebook = best score per (student, exercise), summed per student
create view gradebook as
select s.student_id,
       sum(best.score) as total_points
from (
  select distinct on (student_id, exercise_id)
         student_id, exercise_id, score
  from submissions
  where status = 'done'
  order by student_id, exercise_id, score desc
) best
join submissions s on false  -- (replace with proper join; illustrative)
group by s.student_id;
```

---

## Skeletons

### 1. Exercise notebook (student-facing, `cp1_functions.py`)

```python
import marimo
app = marimo.App()

# --- student fills this in ---
@app.function
def is_prime(n: int) -> bool:
    return ...  # your code here

# --- public self-check (visible, live feedback) ---
@app.cell
def _(mo):
    cases = [(2, True), (4, False), (17, True), (1, False)]
    results = [(f"is_prime({n}) == {exp}", _safe(lambda: is_prime(n) == exp))
               for n, exp in cases]
    passed, total = sum(ok for _, ok in results), len(results)
    mo.callout(
        mo.md(f"**{passed}/{total} public checks passing**\n\n" +
              "\n".join(f"- {'✅' if ok else '❌'} `{lbl}`" for lbl, ok in results)),
        kind="success" if passed == total else "warn",
    )

@app.cell
def _():
    import marimo as mo
    def _safe(f):
        try: return bool(f())
        except Exception: return False
    return mo, _safe
```

### 2. Hidden tests (your side only, `hidden/test_cp1_functions.py`)

```python
from submission import is_prime   # submission.py is the student's file, copied in

def test_small():
    assert is_prime(2) and is_prime(3)
    assert not is_prime(1) and not is_prime(0)

def test_edge():
    assert not is_prime(-7)          # negatives — not in the public cases
    assert is_prime(7919)            # a larger prime
    assert not is_prime(7920)
```

Weight tests however you like — equal points, or tag edge cases as worth more. Each
`test_*` maps to a row in `test_results`.

### 3. Grading runner (Python worker)

```python
# pseudo-loop: poll Postgres for queued submissions, grade, write back
def grade(submission):
    workdir = stage(submission)          # write source -> submission.py, copy hidden/
    report = run_in_sandbox(workdir)     # see #4; returns parsed pytest json
    score, rows = score_report(report, submission.exercise)
    persist(submission, score, rows)     # UPDATE submissions, INSERT test_results

def score_report(report, exercise):
    per_test = exercise.max_points / len(report["tests"])
    rows, score = [], 0
    for t in report["tests"]:
        passed = t["outcome"] == "passed"
        pts = round(per_test) if passed else 0
        score += pts
        rows.append((t["nodeid"], passed, pts, t.get("call", {}).get("longrepr")))
    return score, rows
```

### 4. Sandbox invocation (Docker — fits your Dokploy/Docker setup)

```bash
docker run --rm \
  --network none \                 # no exfiltration, no phone-home
  --memory 256m --cpus 0.5 \       # resource caps
  --pids-limit 128 \               # fork-bomb guard
  --read-only --tmpfs /tmp \       # immutable FS except scratch
  --user 1000:1000 \               # non-root
  -v "$WORKDIR":/work:ro \         # submission + hidden tests, read-only
  grader-image \
  timeout 30 pytest /work/hidden -p no:cacheprovider \
    --json-report --json-report-file=/tmp/r.json -q
# then read /tmp/r.json (bind a writable tmpfs path or capture via stdout)
```

`grader-image` is a tiny image: python + pytest + pytest-json-report + the course
packages (numpy, pandas, matplotlib). Build once.

For a small trusted class, `nsjail`/`firejail` + `resource` rlimits in a subprocess is a
lighter alternative — but Docker is the path of least resistance given you already run it.

### 5. Collection endpoint (Hono, sketch)

```ts
app.post('/submit', auth, async (c) => {
  const { exerciseId, source } = await c.req.json()
  const id = await db.insert(submissions).values({
    studentId: c.get('user').id, exerciseId, source, status: 'queued',
  }).returning({ id: submissions.id })
  return c.json({ submissionId: id })   // worker picks it up
})
```

---

## How it maps to the two phases

| | Phase 1 (basics) | Phase 2 (data science / project) |
|---|---|---|
| Where | **In class** (observed) | At home |
| AI | Restricted | Allowed & taught |
| Authorship guarantee | You're in the room | n/a — AI is the point |
| Grading | This pipeline, hidden tests | This pipeline, hidden tests |
| Public tests | Yes (live feedback) | Yes |

The autograder is identical across both. Don't let it fool you into thinking it also
handles authorship — in Phase 1 the *in-class* part does that, not the grader.

---

## Security checklist

- [ ] No network (`--network none`)
- [ ] Hard wall-clock timeout (`timeout 30`) — catches infinite loops
- [ ] Memory + CPU + PID caps
- [ ] Read-only filesystem, writable `/tmp` only
- [ ] Non-root user
- [ ] Disposable container per submission (`--rm`)
- [ ] Never run student code in the same process/host as your web app or DB creds

---

## MVP cut (build in this order)

1. **Manual loop first.** A folder of submitted `.py` + a `grade.py` that loops, runs the
   Docker sandbox, prints scores. No web upload, no DB. Proves the grading core in an hour.
2. **Add Postgres** (exercises, submissions, test_results) + the worker poll loop.
3. **Add the upload endpoint** + a minimal gradebook view in your app.
4. **Add WASM practice embeds** + per-student feedback (show `test_results.message`).

Stop at step 1 to validate; everything after is plumbing you've built before.
