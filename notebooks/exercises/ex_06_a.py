# notebooks/exercises/ex_06_a.py
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
    # Quick exercise: import by name (5–10 min)

    `import statistics` puts the whole toolbox on the desk, and every tool
    needs the `statistics.` prefix. `from statistics import mean, median`
    pulls just those two tools out of the box: you call them by their bare
    names, `median(...)`, no prefix at all.

    **Predict** what the cell below prints, then run it.
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
    from statistics import mean, median
    return mean, median


@app.cell
def _(mean, median):
    # Worked example (read + run this)
    _ratings_demo = [4.5, 4.8, 1.0, 5.0, 4.2]
    print(f"mean:   {mean(_ratings_demo)}")
    print(f"median: {median(_ratings_demo)}")
    return


@app.cell
def _():
    # Delivery times in minutes, last night's shift. One went badly.
    times_exa = [12, 14, 11, 13, 58, 12]
    return (times_exa,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The investor points at the 58 and asks for the **typical** delivery
    time, the middle value that one disaster can't drag around.

    Compute it as `typical_exa` from `times_exa`, using the imported name
    directly (no `statistics.` prefix).
    """
    )
    return


@app.cell
def _(median, times_exa):
    # YOUR CODE BELOW: replace None
    typical_exa = None
    return (typical_exa,)


@app.cell(hide_code=True)
def _(mo, show_result, typical_exa):
    # Reactive check. Re-runs when you run the cell above.
    if typical_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `typical_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(typical_exa, (int, float)) and round(typical_exa, 2) == 12.5:
        _ok = True
        _msg = "Correct — 12.5 minutes. Six values, so the median averages the two in the middle, and the 58 never gets a say."
    elif isinstance(typical_exa, (int, float)) and round(typical_exa, 2) == 20.0:
        _ok = False
        _msg = "Wrong — that's the mean, and the 58 dragged it up to 20. The investor asked for the middle value."
    else:
        _ok = False
        _msg = "Wrong — sort the six times in your head: the typical one sits between the third and the fourth. Which imported name finds it?"
    mo.callout(mo.md(_msg + show_result(typical_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "The tool you need was imported by name in the cell above the worked example, so it works without any prefix.",
            "Hint 2 (the structure)": "typical_exa = ______(times_exa)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor wants a number for the damage: how many
    minutes does the one bad delivery drag the *average* above the typical
    time? Compute `drag_exa` as the mean minus the median of `times_exa`,
    both imported by name.
    """
    )
    return


@app.cell
def _(mean, median, times_exa):
    # YOUR CODE BELOW: replace None
    drag_exa = None
    return (drag_exa,)


@app.cell(hide_code=True)
def _(drag_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if drag_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `drag_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(drag_exa, (int, float)) and round(drag_exa, 2) == 7.5:
        _ok = True
        _msg = "Correct — 7.5 minutes of drag from a single delivery. That's the number the investor writes down."
    elif isinstance(drag_exa, (int, float)) and round(drag_exa, 2) == -7.5:
        _ok = False
        _msg = "Wrong — right size, wrong sign. The mean sits *above* the median here, so subtract the median from the mean."
    else:
        _ok = False
        _msg = "Wrong — two calls, one subtraction: `mean(...)` of the times minus `median(...)` of the times."
    mo.callout(mo.md(_msg + show_result(drag_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Both tools are already on the desk. Call each one on `times_exa`, then subtract.",
            "Hint 2 (the structure)": "drag_exa = ____(times_exa) - ______(times_exa)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
