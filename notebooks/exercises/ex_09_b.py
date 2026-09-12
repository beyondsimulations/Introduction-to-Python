# notebooks/exercises/ex_09_b.py
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    # Shows your current answer under the check.
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
    # Quick exercise: your first chart (5-10 min)

    Episode 9: the investor's one instruction was "charts I can't argue
    with." A table of seven numbers doesn't argue anything, but a line does.

    `plt.plot(x, y)` draws the line; `plt.xlabel`, `plt.ylabel`, and
    `plt.title` label it. One marimo rule that trips everyone up once:
    the LAST expression in a cell is what displays, so chart cells end
    with `plt.gca()` ("get current axes"), never `plt.show()`.

    **Predict** first: look at the numbers in the demo below: which way
    does the line slope, up or down?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Saving your work:** this notebook runs in your browser. Press "
            "**Cmd/Ctrl+S** to save, and always save **before** menu → Download → "
            "*Download Python code*. Without a save first, the download is an empty file."
        ),
        kind="info",
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
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.plot(_demo_signups)
    plt.title("Demo: three weeks of signups")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `revenues_exb` below is one real week (Monday → Sunday). Plot it the
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
    # Given: do not change this
    revenues_exb = [142.50, 168.20, 155.90, 201.40, 189.60, 246.80, 232.10]
    return (revenues_exb,)


@app.cell
def _(plt, revenues_exb):
    plt.figure()
    # YOUR CODE BELOW: plot revenues_exb (labels/title optional, ungraded)
    plt.gca()
    return


@app.cell
def _(revenues_exb):
    # YOUR CODE BELOW: replace None
    total_exb = None
    return (total_exb,)


@app.cell
def _(revenues_exb):
    # YOUR CODE BELOW: replace None
    best_day_exb = None
    return (best_day_exb,)


@app.cell(hide_code=True)
def _(best_day_exb, mo, show_result, total_exb):
    # Reactive check. Re-runs when you run the cell above.
    _expected_total = 1336.5
    _expected_day = 6
    _result = None
    if total_exb is None or best_day_exb is None:
        _ok = False
        _msg = "Not attempted: Assign it to `total_exb` and `best_day_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(total_exb, (list, tuple)) or isinstance(best_day_exb, (list, tuple)):
        _ok = False
        _result = f"total_exb={total_exb!r}, best_day_exb={best_day_exb!r}"
        _msg = "Wrong: One of these is still a whole list. The investor wants two single numbers."
    else:
        try:
            _total = round(float(total_exb), 2)
            _day = float(best_day_exb)
        except (TypeError, ValueError):
            _ok = False
            _total = None
            _day = None
            _msg = "Wrong: These should both be plain numbers. Check what your expressions actually return."
        else:
            _result = f"total_exb={total_exb}, best_day_exb={best_day_exb}"
            if _total == _expected_total and _day == _expected_day:
                _ok = True
                _msg = "Correct: A solid week, and you know exactly which day carried it."
            elif _day == 5:
                _ok = False
                _msg = "Wrong: `best_day_exb` is off by one: Python counts positions from 0, but days count from 1. What do you need to add?"
            elif _day == 246.8:
                _ok = False
                _msg = "Wrong: `best_day_exb` looks like a revenue number, not a day, so that's the VALUE. The investor asked WHICH day."
            elif _total == _expected_total:
                _ok = False
                _msg = "Wrong: Your total is right, but `best_day_exb` isn't. Find the POSITION of the biggest number, not the number itself."
            elif _day == _expected_day:
                _ok = False
                _msg = "Wrong: `best_day_exb` is right, but your total isn't. Check your sum over all seven days."
            else:
                _ok = False
                _msg = "Wrong: `total_exb` is a sum over the week, `best_day_exb` is a position from 1 to 7."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`plt.plot(range(1, 8), revenues_exb)` draws the line for your eyes, but the check only reads `total_exb` and `best_day_exb`. For the total, add up the week. For the day, find the POSITION of the biggest number, then remember days start at 1, Python starts at 0.",
            "Hint 2 (the structure)": "total_exb = float(sum(___))\nbest_day_exb = revenues_exb.index(max(revenues_exb)) + ___",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor points at the right end of your line:
    "The weekend carries you. How much of the week is that?" Compute the
    weekend's share of the week's revenue (Saturday + Sunday) as a
    **percent**: `weekend_share_exb`.
    """
    )
    return


@app.cell
def _(revenues_exb):
    # YOUR CODE BELOW: replace None
    weekend_share_exb = None
    return (weekend_share_exb,)


@app.cell(hide_code=True)
def _(mo, show_result, weekend_share_exb):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 35.83
    _result = None
    if weekend_share_exb is None:
        _ok = False
        _msg = "Not attempted: Assign it to `weekend_share_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(weekend_share_exb, (list, tuple)):
        _ok = False
        _result = f"weekend_share_exb={weekend_share_exb!r}"
        _msg = "Wrong: That's still a list. The investor wants ONE percentage."
    else:
        try:
            _v = round(float(weekend_share_exb), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. Check what your expression returns."
        else:
            _result = f"weekend_share_exb={weekend_share_exb}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Exercise 9.b stretch: over a third of the week's revenue came in on two days, which belongs on the slide."
            elif _v == 0.36:
                _ok = False
                _msg = "Wrong: That's the fraction. Percent means ×100."
            elif _v == 478.9:
                _ok = False
                _msg = "Wrong: That's the weekend's revenue in euros. A SHARE compares it to the whole week."
            elif _v == 17.37:
                _ok = False
                _msg = "Wrong: That's Sunday alone. The weekend is Saturday AND Sunday, the last two positions."
            else:
                _ok = False
                _msg = "Wrong: Share % = (Saturday + Sunday) / whole week × 100."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Saturday and Sunday are the last two entries of `revenues_exb`. A slice from position 5 grabs both. Divide their sum by the week's sum, then ×100.",
            "Hint 2 (the structure)": "weekend_share_exb = sum(revenues_exb[___:]) / sum(___) * 100",
        }
    )
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
