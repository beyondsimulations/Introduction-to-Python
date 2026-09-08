# notebooks/exercises/ex_09_c.py
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
    # Quick exercise: the honest y-axis (10 min)

    Tobi asked an AI to chart this week's growth for the pitch deck. It
    ran without errors. Before you believe a chart, check one thing
    first: where does the y-axis START?

    **Predict** first: look at the y-axis numbers below before you look
    at the slope.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "💾 **Saving your work:** this notebook runs in your browser. Press "
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
def _():
    # Given: do not change this. Orders per week, week 1 → week 4.
    weekly_exc = [50, 52, 53, 55]
    return (weekly_exc,)


@app.cell
def _(plt, weekly_exc):
    # Tobi's AI-generated chart: runs fine, technically correct numbers
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.plot(range(1, 5), weekly_exc)
    plt.ylim(49, 56)
    plt.ylabel("Orders per week")
    plt.title("Tobi's chart")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Looks like a rocket, doesn't it? Check the y-axis: it starts at 49,
    not 0. A few orders of real growth gets stretched into a near-vertical
    line.

    The investor wants the real growth number for the pitch. Compute
    the growth from week 1 to week 4 as a **percent**: `growth_exc`.
    Percent growth compares the CHANGE to where you STARTED, then
    multiplies by 100.
    """
    )
    return


@app.cell
def _(weekly_exc):
    # YOUR CODE BELOW: replace None
    growth_exc = None
    return (growth_exc,)


@app.cell(hide_code=True)
def _(growth_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 10.0
    _result = None
    if growth_exc is None:
        _ok = False
        _msg = "🔲 Not attempted yet. Assign it to `growth_exc` (a `print` alone doesn't count) and run the cell."
    else:
        try:
            _v = round(float(growth_exc), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "❌ That's not a number yet. Check what your expression returns."
        else:
            _result = f"growth_exc={growth_exc}"
            if _v == _expected:
                _ok = True
                _msg = "✅ Correct! That's the honest number, no costume required."
            elif _v == 0.1:
                _ok = False
                _msg = "❌ That's the fraction. Percent means ×100."
            elif _v == 5.0:
                _ok = False
                _msg = "❌ 5 orders more, yes, but the investor asked for PERCENT of where you started, not the raw difference."
            elif _v == 9.09:
                _ok = False
                _msg = "❌ Growth is measured from the START value, not the end. Check your denominator."
            else:
                _ok = False
                _msg = "❌ Not quite. Growth % = (end − start) / start × 100."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Percent growth compares the CHANGE to the STARTING value, then multiplies by 100. Neither the ending value nor the raw difference in k€ gives you that.",
            "💡 Hint 2 (the structure)": "growth_exc = (___ - ___) / ___ * 100",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Now fix the chart

    Re-plot the same `weekly_exc` data, but this time let the y-axis
    start at 0 (`plt.ylim(0, 60)`). Same numbers, honest axis. Watch
    how much the slope changes just by telling the truth about the
    baseline.

    This chart isn't graded either. Look at it, then move on.
    """
    )
    return


@app.cell
def _(plt, weekly_exc):
    plt.figure()
    # YOUR CODE BELOW: re-plot weekly_exc with plt.ylim(0, 60)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("10% growth is good news. It doesn't need a costume.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
