# notebooks/exercises/ex_09_a.py
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    # Helper — echoes the student's current answer as a "Your result" preview.
    def show_result(value):
        if value is None:
            return ""
        if isinstance(value, str):
            return f"\n\n**Your result:**\n\n```\n{value}\n```"
        return f"\n\n**Your result:** `{value}`"

    return (show_result,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # ⚡ Quick exercise: your first chart (10 min)

    Episode 9: the investor's one instruction was "charts I can't argue
    with." A table of seven numbers doesn't argue anything — a line does.

    `plt.plot(x, y)` draws the line; `plt.xlabel`, `plt.ylabel`, and
    `plt.title` label it. One marimo rule that trips everyone up once:
    the LAST expression in a cell is what displays, so chart cells end
    with `plt.gca()` ("get current axes"), never `plt.show()`.

    **Predict** first: look at the numbers in the demo below: which way
    does the line slope, up or down?
    """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(plt):
    # Worked example (read + run this)
    _demo_signups = [80, 55, 20]
    plt.figure()  # starts a fresh figure — keeps this chart from drawing on top of the last one
    plt.plot(_demo_signups)
    plt.title("Demo: three weeks of signups")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `revenues_exa` below is one real week (Monday → Sunday). Plot it the
    same way as the demo, then read the chart to answer two questions
    for the investor: the week's **total** revenue, and **which day**
    (1 = Monday … 7 = Sunday) brought in the most.

    The chart itself isn't graded. The check below reads your numbers,
    not your art.
    """
    )
    return


@app.cell
def _():
    # Given — do not change this
    revenues_exa = [142.50, 168.20, 155.90, 201.40, 189.60, 246.80, 232.10]
    return (revenues_exa,)


@app.cell
def _(plt, revenues_exa):
    plt.figure()
    # YOUR CODE BELOW — plot revenues_exa (labels/title optional, ungraded)
    plt.gca()
    return


@app.cell
def _(revenues_exa):
    # YOUR CODE BELOW — replace None
    total_exa = None
    return (total_exa,)


@app.cell
def _(revenues_exa):
    # YOUR CODE BELOW — replace None
    best_day_exa = None
    return (best_day_exa,)


@app.cell(hide_code=True)
def _(best_day_exa, mo, show_result, total_exa):
    # Reactive check — re-runs automatically whenever the cells above change.
    _expected_total = 1336.5
    _expected_day = 6
    _result = None
    if total_exa is None or best_day_exa is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif isinstance(total_exa, (list, tuple)) or isinstance(best_day_exa, (list, tuple)):
        _ok = False
        _result = f"total_exa={total_exa!r}, best_day_exa={best_day_exa!r}"
        _msg = "❌ One of these is still a whole list — the investor wants two single numbers."
    else:
        # Coerce to plain numbers first — anything that can't be must
        # degrade to a message, never crash the check.
        try:
            _total = round(float(total_exa), 2)
            _day = float(best_day_exa)
        except (TypeError, ValueError):
            _ok = False
            _total = None
            _day = None
            _msg = "❌ These should both be plain numbers — check what your expressions actually return."
        else:
            _result = f"total_exa={total_exa}, best_day_exa={best_day_exa}"
            if _total == _expected_total and _day == _expected_day:
                _ok = True
                _msg = "✅ Correct! A solid week — and you know exactly which day carried it."
            elif _day == 5:
                _ok = False
                _msg = "❌ `best_day_exa` is off by one — Python counts positions from 0, but days count from 1. What do you need to add?"
            elif _day == 246.8:
                _ok = False
                _msg = "❌ `best_day_exa` looks like a revenue number, not a day — that's the VALUE. The investor asked WHICH day."
            elif _total == _expected_total:
                _ok = False
                _msg = "❌ Your total is right, but `best_day_exa` isn't — find the POSITION of the biggest number, not the number itself."
            elif _day == _expected_day:
                _ok = False
                _msg = "❌ `best_day_exa` is right, but your total isn't — check your sum over all seven days."
            else:
                _ok = False
                _msg = "❌ Not quite — `total_exa` is a sum over the week, `best_day_exa` is a position from 1 to 7."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`plt.plot(range(1, 8), revenues_exa)` draws the line for your eyes — the check only reads `total_exa` and `best_day_exa`. For the total, add up the week. For the day, find the POSITION of the biggest number — then remember days start at 1, Python starts at 0.",
            "💡 Hint 2 (the structure)": "total_exa = float(sum(___))\nbest_day_exa = revenues_exa.index(max(revenues_exa)) + ___",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
