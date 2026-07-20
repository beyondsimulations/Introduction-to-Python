#!/usr/bin/env python3
"""Check MC option balance in this repo's self-test questions (owner directive 2026-07-20).

Well-grounded MC questions still leak answers through *form*. Three cues are
audited here (fleet rollout of the quiz-craft skill):

  1. Length -- within a question, the longest option must be <= RATIO_MAX x the
     shortest (visible text), and correct options must not be systematically
     the longest.
  2. Position -- correct answers must not cluster on one letter/slot. Neither
     revealjs slides nor mo.ui.radio shuffle options, so SOURCE order is the
     only defense.
  3. Absolutes -- absolute terms (always, never, only, ...) must not be
     concentrated in wrong options.

This repo has three MC formats (ported/adapted from the Information-Systems-
Big-Data quizkit checker):

  A. Lecture decks (lectures/lec_*.qmd): inline option lines
       a\\) `17.8`   b) `17.80`   c) `Error`
     with the correct letter on a following reveal line starting `**b)`.
  B. Lab MCQ cells (notebooks/nb_*.py): markdown options `- **a)** text`,
     correct letter taken from the check cell comparison `== "b"`.
  C. Radio trace questions (notebooks/**/*.py): mo.ui.radio(options=[...]),
     correct option from the reveal cell comparison `<name>.value == "..."`.

Code-literal exemption: most lecture options are *program outputs* (`17.80` vs
`Error`). Their lengths are dictated by the code under discussion, not by
author laziness, so questions whose options are ALL code-y (code spans,
bare/quoted literals, error outcomes, or glue words joining those) are
reported but do NOT fail the length gate. Prose questions are gated at
RATIO_MAX. Questions with at least one genuine prose option are gated.

Exit status: 1 if any prose question exceeds RATIO_MAX (gates QA), else 0.
Position and absolutes are reported for the systematic-pattern check; judge
against the target: no letter/slot should dominate, and the absolute-term rate
in wrong options should stay close to the rate in correct options.

Usage:
  uv run python helpers/check_quiz_balance.py            # summary + violations
  uv run python helpers/check_quiz_balance.py --stats    # full per-question table
"""

from __future__ import annotations

import argparse
import ast
import collections
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

RATIO_MAX = 1.8

ABS_RE = re.compile(
    r"\b(always|never|only|all|every|eliminat\w+|guarantee\w*|impossible"
    r"|fully|completely|entirely|by definition)\b",
    re.I,
)

LECTURE_OPTION_LINE_RE = re.compile(r"^a\\\)\s")
LECTURE_REVEAL_RE = re.compile(r"^\*\*([a-d])\)")
MCQ_OPTION_RE = re.compile(r"^\s*- \*\*([a-d])\)\*\* (.+?)\s*$")
MCQ_ANSWER_RE = re.compile(r'==\s*"([a-d])"')
RADIO_RE = re.compile(r"(\w+) = mo\.ui\.radio\(")
LETTER_PREFIX_RE = re.compile(r"^[a-dA-D][)—-]\s*")
ERROR_OUTCOME_RE = re.compile(r"^(an?\s+)?(\w*error\w*)\b", re.I)
GLUE_TOKENS = {
    "and", "then", "both", "neither", "a", "an", "it",
    "prints", "raises", "adds", "error", "true", "false", "none",
}


def option_is_codey(raw: str) -> bool:
    """A code-literal option: its length is dictated by the program under
    discussion (an output, a code line, a literal, an error outcome), not by
    how much detail the author bothered to write."""
    s = LETTER_PREFIX_RE.sub("", raw.strip())
    if ERROR_OUTCOME_RE.match(s.replace("`", "")):
        return True
    s = re.sub(r"`[^`]*`", " ", s)  # drop inline code spans
    s = re.sub(r"\"[^\"]*\"|'[^']*'", " ", s)  # drop quoted literals
    tokens = [
        t for t in re.findall(r"[A-Za-z_]\w*", s)
        if not any(ch.isdigit() for ch in t)
        and not re.fullmatch(r"\w*error\w*", t, re.I)
    ]
    return all(t.lower() in GLUE_TOKENS for t in tokens)


@dataclass
class Question:
    source: str  # "file:line"
    fmt: str  # "lecture", "mcq", "radio"
    stem: str
    options: list[tuple[bool, str]] = field(default_factory=list)  # (correct, visible)
    raw_options: list[str] = field(default_factory=list)  # before backtick-strip

    @property
    def lengths(self) -> list[int]:
        return [len(t) for _, t in self.options]

    @property
    def ratio(self) -> float:
        lengths = self.lengths
        if not lengths or min(lengths) == 0:
            return float("inf") if lengths else 0.0
        return max(lengths) / min(lengths)

    @property
    def correct_is_longest(self) -> bool:
        """True if the strictly longest option is a correct one (ties are fine)."""
        if not self.options:
            return False
        longest = max(self.lengths)
        longest_opts = [c for c, t in self.options if len(t) == longest]
        return all(longest_opts) and len(longest_opts) < len(self.options)

    @property
    def correct_index(self) -> int | None:
        idx = [i for i, (c, _) in enumerate(self.options) if c]
        return idx[0] if len(idx) == 1 else None

    @property
    def all_code(self) -> bool:
        """All options are code literals / error outcomes -> length exempt."""
        return bool(self.raw_options) and all(
            option_is_codey(o) for o in self.raw_options
        )


def visible(raw: str) -> str:
    """Markdown emphasis and backticks are visual noise, not read length."""
    return raw.replace("**", "").replace("`", "").strip()


def parse_lectures(repo: Path) -> list[Question]:
    questions: list[Question] = []
    for path in sorted((repo / "lectures").glob("lec_*.qmd")):
        lines = path.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if not LECTURE_OPTION_LINE_RE.match(line):
                continue
            # Split the inline option row on 2+ spaces before a letter marker.
            parts = re.split(r"\s{2,}(?=[a-d]\\?\))", line.strip())
            opts = []
            for part in parts:
                m = re.match(r"^([a-d])\\?\)\s*(.*)$", part)
                if m:
                    opts.append((m.group(1), m.group(2).strip()))
            if len(opts) < 2:
                continue
            # Correct letter: next reveal line `**b)` after the option row.
            correct_letter = None
            for j in range(i + 1, min(i + 40, len(lines))):
                rm = LECTURE_REVEAL_RE.match(lines[j])
                if rm:
                    correct_letter = rm.group(1)
                    break
                if LECTURE_OPTION_LINE_RE.match(lines[j]):
                    break  # next question started first
            # Stem: nearest preceding slide heading.
            stem = ""
            for j in range(i - 1, max(i - 30, -1), -1):
                if lines[j].startswith("#"):
                    stem = lines[j].lstrip("# ").strip()
                    break
            q = Question(source=f"{path.name}:{i + 1}", fmt="lecture", stem=stem)
            for letter, text in opts:
                q.raw_options.append(text)
                q.options.append((letter == correct_letter, visible(text)))
            if correct_letter is None:
                print(f"WARN: no reveal letter found for {q.source}", file=sys.stderr)
            questions.append(q)
    return questions


def parse_notebook_mcqs(repo: Path) -> list[Question]:
    questions: list[Question] = []
    for path in sorted((repo / "notebooks").rglob("*.py")):
        if path.name.startswith("_"):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        i = 0
        while i < len(lines):
            if not MCQ_OPTION_RE.match(lines[i]):
                i += 1
                continue
            start = i
            opts: list[tuple[str, str]] = []
            while i < len(lines):
                m = MCQ_OPTION_RE.match(lines[i])
                if not m:
                    break
                opts.append((m.group(1), m.group(2)))
                i += 1
            # Correct letter: first `== "x"` comparison in the following lines.
            correct_letter = None
            for j in range(i, min(i + 60, len(lines))):
                am = MCQ_ANSWER_RE.search(lines[j])
                if am:
                    correct_letter = am.group(1)
                    break
            stem = ""
            for j in range(start - 1, max(start - 20, -1), -1):
                if lines[j].lstrip().startswith("###"):
                    stem = lines[j].strip().lstrip("# ")
                    break
            q = Question(source=f"{path.name}:{start + 1}", fmt="mcq", stem=stem)
            for letter, text in opts:
                q.raw_options.append(text)
                q.options.append((letter == correct_letter, visible(text)))
            if correct_letter is None:
                print(f"WARN: no answer check found for {q.source}", file=sys.stderr)
            questions.append(q)
    return questions


def parse_radios(repo: Path) -> list[Question]:
    questions: list[Question] = []
    for path in sorted((repo / "notebooks").rglob("*.py")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        for m in RADIO_RE.finditer(text):
            name = m.group(1)
            opt_m = re.compile(r"options=\[", re.S).search(text, m.end())
            if not opt_m:
                continue
            # Bracket-match the options list, then literal_eval it.
            depth, k = 1, opt_m.end()
            while k < len(text) and depth:
                depth += {"[": 1, "]": -1}.get(text[k], 0)
                k += 1
            try:
                options = ast.literal_eval(text[opt_m.end() - 1 : k])
            except (ValueError, SyntaxError):
                continue
            if not all(isinstance(o, str) for o in options):
                continue
            cm = re.search(
                rf"{name}\.value == (\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*')", text
            )
            correct = ast.literal_eval(cm.group(1)) if cm else None
            if correct is None:
                # Alternate reveal-cell form: <name>.value.startswith("d")
                sm = re.search(rf"{name}\.value\.startswith\(\"([^\"]+)\"\)", text)
                if sm:
                    hits = [o for o in options if o.startswith(sm.group(1))]
                    correct = hits[0] if len(hits) == 1 else None
            line_no = text.count("\n", 0, m.start()) + 1
            label_m = re.search(r'label="([^"]*)"', text[m.end() : k + 300])
            q = Question(
                source=f"{path.name}:{line_no}",
                fmt="radio",
                stem=label_m.group(1) if label_m else name,
            )
            for o in options:
                q.raw_options.append(o)
                q.options.append((o == correct, visible(o)))
            if correct is None:
                print(f"WARN: no .value check found for {q.source}", file=sys.stderr)
            questions.append(q)
    return questions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--stats", action="store_true", help="print full per-question table")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    questions = parse_lectures(repo) + parse_notebook_mcqs(repo) + parse_radios(repo)
    if not questions:
        print("No MC questions found.", file=sys.stderr)
        return 1

    any_violation = False
    pos = collections.Counter()
    n_single = 0
    abs_correct = abs_wrong = n_correct = n_wrong = 0

    by_fmt: dict[str, list[Question]] = collections.defaultdict(list)
    for q in questions:
        by_fmt[q.fmt].append(q)

    for fmt in ("lecture", "mcq", "radio"):
        qs = by_fmt.get(fmt, [])
        prose = [q for q in qs if not q.all_code]
        violations = [q for q in prose if q.ratio > RATIO_MAX]
        longest = [q for q in qs if q.correct_is_longest]
        if violations:
            any_violation = True
        print(
            f"\n[{fmt}] {len(qs)} questions ({len(prose)} prose-gated, "
            f"{len(qs) - len(prose)} code-exempt), "
            f"ratio>{RATIO_MAX}: {len(violations)}, "
            f"correct-is-longest: {len(longest)}/{len(qs)}"
        )
        for q in qs:
            ci = q.correct_index
            if ci is not None:
                pos[chr(ord("a") + ci)] += 1
                n_single += 1
            for c, t in q.options:
                hit = bool(ABS_RE.search(t))
                if c:
                    n_correct += 1
                    abs_correct += hit
                else:
                    n_wrong += 1
                    abs_wrong += hit
            if args.stats:
                lens = ",".join(str(n) for n in q.lengths)
                flags = ""
                if not q.all_code and q.ratio > RATIO_MAX:
                    flags += " RATIO"
                if q.correct_is_longest:
                    flags += " LONGEST-CORRECT"
                letter = "?" if ci is None else chr(ord("a") + ci)
                print(
                    f"  {q.source:<28} ans={letter} lens=[{lens}] "
                    f"ratio={q.ratio:.2f}{' code' if q.all_code else ''}{flags}"
                )
        if not args.stats:
            for q in violations:
                print(f"  {q.source} ratio={q.ratio:.2f} lens={q.lengths}  <- exceeds {RATIO_MAX}")

    print(f"\nPosition of correct answer ({n_single} single-answer questions):")
    for letter in sorted(pos):
        print(f"  {letter}: {pos[letter]}")
    print(
        f"Absolute terms: correct {abs_correct}/{n_correct} "
        f"({abs_correct / max(n_correct, 1):.0%}), "
        f"wrong {abs_wrong}/{n_wrong} ({abs_wrong / max(n_wrong, 1):.0%})"
    )

    if any_violation:
        print(f"\nFAIL: prose option-length ratio above {RATIO_MAX} (see above).")
        return 1
    print(f"\nPASS: all prose questions within the {RATIO_MAX} length-ratio threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
