# notebooks/exercises/ex_09_a.py
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
    # Quick exercise: label the chart (5–10 min)

    Episode 9: Tobi's first pitch-deck slide is a line with no labels.
    The investor looks at it for two seconds: "What is on the y-axis?
    Orders? Euros? Your mood?" Every honest chart names its axes.

    `plt.xlabel`, `plt.ylabel`, and `plt.title` do that job. Chart cells
    open with `plt.figure()` and end with `plt.gca()`, never `plt.show()`.

    **Predict** first: in the demo below, which line of code puts the
    word "Week" under the chart?
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
    _demo_signups = [20, 55, 80]
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.plot([1, 2, 3], _demo_signups)
    plt.xlabel("Week")  # what the x-axis counts
    plt.ylabel("Signups")  # what the y-axis measures
    plt.title("Demo: signups per week (peak 80)")  # what the picture is about
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `orders_exa` below is this week's order count, Monday to Friday.
    Plot it, label both axes, and give it a title that carries the one
    number the investor will ask for: the **average orders per day**.

    The chart itself isn't graded. The check below reads `avg_exa`, the
    number in your title, not your art.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    orders_exa = [31, 28, 35, 40, 38]
    return (orders_exa,)


@app.cell
def _(orders_exa):
    # YOUR CODE BELOW: replace None
    avg_exa = None
    return (avg_exa,)


@app.cell
def _(avg_exa, orders_exa, plt):
    plt.figure()
    # YOUR CODE BELOW: plot orders_exa, label both axes, put avg_exa in the title (ungraded)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(avg_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 34.4
    _result = None
    if avg_exa is None:
        _ok = False
        _msg = "Not attempted — Assign it to `avg_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(avg_exa, (list, tuple)):
        _ok = False
        _result = f"avg_exa={avg_exa!r}"
        _msg = "Wrong — That's still the whole list. The title needs ONE number."
    else:
        try:
            _v = round(float(avg_exa), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong — That's not a number yet. Check what your expression returns."
        else:
            _result = f"avg_exa={avg_exa}"
            if _v == _expected:
                _ok = True
                _msg = "Correct — Exercise 9.a: the title now says what the picture is about, number included."
            elif _v == 172.0:
                _ok = False
                _msg = "Wrong — That's the week's TOTAL. Average means total divided by the number of days."
            elif _v == 34.0:
                _ok = False
                _msg = "Wrong — So close: `//` throws away the decimals. Use `/` for the average."
            elif _v == 40.0:
                _ok = False
                _msg = "Wrong — That's the best day, not the average day."
            else:
                _ok = False
                _msg = "Wrong — Average = sum of the orders / number of days."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`plt.plot(range(1, 6), orders_exa)` draws the line, `plt.xlabel(...)` and `plt.ylabel(...)` name the axes. For the title, `f\"Orders per day (avg {avg_exa})\"` works once `avg_exa` is a number: total of the list divided by how many days it holds.",
            "Hint 2 (the structure)": "avg_exa = sum(___) / len(___)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor wants last week on the same chart, for
    comparison. `last_week_exa` is below. Plot both lines with a
    `label=` each and call `plt.legend()`, then count on how many days
    THIS week beat last week: `days_ahead_exa`.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    last_week_exa = [29, 31, 33, 36, 39]
    return (last_week_exa,)


@app.cell
def _(last_week_exa, orders_exa, plt):
    plt.figure()
    # YOUR CODE BELOW: two lines with label=, then plt.legend() (ungraded)
    plt.gca()
    return


@app.cell
def _(last_week_exa, orders_exa):
    # YOUR CODE BELOW: replace None
    days_ahead_exa = None
    return (days_ahead_exa,)


@app.cell(hide_code=True)
def _(days_ahead_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 3
    _result = None
    if days_ahead_exa is None:
        _ok = False
        _msg = "Not attempted — Assign it to `days_ahead_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(days_ahead_exa, (list, tuple)):
        _ok = False
        _result = f"days_ahead_exa={days_ahead_exa!r}"
        _msg = "Wrong — That's a list of days. The investor wants a COUNT: how many days."
    else:
        try:
            _v = round(float(days_ahead_exa), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong — That's not a number yet. Check what your expression returns."
        else:
            _result = f"days_ahead_exa={days_ahead_exa}"
            if _v == _expected:
                _ok = True
                _msg = "Correct — Exercise 9.a stretch: three of five days ahead. The legend tells the room which line is which."
            elif _v == 2.0:
                _ok = False
                _msg = "Wrong — You counted the days this week fell BEHIND. Flip the comparison."
            elif _v == 5.0:
                _ok = False
                _msg = "Wrong — That's every day. Only the days where this week's number is BIGGER count."
            else:
                _ok = False
                _msg = "Wrong — Walk both lists side by side and count the days where this week > last week."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`zip(orders_exa, last_week_exa)` hands you one pair per day. Compare the two numbers in each pair and count the pairs where this week wins. For the chart, `plt.plot(..., label=\"This week\")` and `plt.plot(..., label=\"Last week\")`, then `plt.legend()`.",
            "Hint 2 (the structure)": "days_ahead_exa = sum(1 for _this, _last in zip(orders_exa, last_week_exa) if ___)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
