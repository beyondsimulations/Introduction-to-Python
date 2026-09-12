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
    # Quick exercise: the right chart for categories (5-10 min)

    Line charts show change over TIME. Zones aren't a timeline: they're
    categories to compare, and `plt.bar(labels, heights)` is the chart
    for that job.

    Same marimo rule as last time: the LAST expression in a cell
    displays, so chart cells end with `plt.gca()`.

    **Predict** first: look at the two demo numbers below: which bar
    will be taller?
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
    _demo_teams = ["Alpha", "Beta"]
    _demo_scores = [7, 3]
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.bar(_demo_teams, _demo_scores)
    plt.title("Demo: two teams")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `zones_exc` and `totals_exc` below are tonight's revenue by delivery
    zone. Plot a bar chart, then tell the investor which ZONE brought in
    the most, as a name, not a number.

    The chart itself isn't graded. The check below reads
    `best_zone_exc`, not your bars.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    zones_exc = ["Nord", "Sued", "Hafen", "Altstadt"]
    return (zones_exc,)


@app.cell
def _():
    # Given: do not change this
    totals_exc = [412.60, 268.40, 305.90, 351.20]
    return (totals_exc,)


@app.cell
def _(plt, totals_exc, zones_exc):
    plt.figure()
    # YOUR CODE BELOW: plot zones_exc vs totals_exc (labels/title optional, ungraded)
    plt.gca()
    return


@app.cell
def _(totals_exc, zones_exc):
    # YOUR CODE BELOW: replace None
    best_zone_exc = None
    return (best_zone_exc,)


@app.cell(hide_code=True)
def _(best_zone_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = "nord"
    _result = None
    if best_zone_exc is None:
        _ok = False
        _msg = "Not attempted: Assign it to `best_zone_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(best_zone_exc, (list, tuple)):
        _ok = False
        _result = f"best_zone_exc={best_zone_exc!r}"
        _msg = "Wrong: That's the whole list. The investor wants ONE winner, not all four zones."
    elif isinstance(best_zone_exc, (int, float)) and not isinstance(best_zone_exc, bool):
        _ok = False
        _result = f"best_zone_exc={best_zone_exc!r}"
        _msg = "Wrong: That's the bar's HEIGHT (a euro amount). The investor asked WHICH zone, by name."
    else:
        _v = str(best_zone_exc).strip().lower()
        _result = f"best_zone_exc={best_zone_exc!r}"
        if _v == _expected:
            _ok = True
            _msg = "Correct: One glance at the bar chart and the investor knows where to expand."
        else:
            _ok = False
            _msg = "Wrong: Read the tallest bar again and check its label."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`plt.bar(zones_exc, totals_exc)` draws the bars, but the check wants the zone's NAME, not its height. Which list method finds the POSITION of the largest number in `totals_exc`? Use that position to look up a name in `zones_exc`.",
            "Hint 2 (the structure)": "_best_index = totals_exc.index(___(totals_exc))\nbest_zone_exc = zones_exc[___]",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor wants the bars in order, tallest first,
    so the ranking reads left to right. Re-plot the bars sorted by
    height, then tell her which zone comes SECOND: `second_zone_exc`.
    """
    )
    return


@app.cell
def _(plt, totals_exc, zones_exc):
    plt.figure()
    # YOUR CODE BELOW: bar chart sorted by height, tallest first (ungraded)
    plt.gca()
    return


@app.cell
def _(totals_exc, zones_exc):
    # YOUR CODE BELOW: replace None
    second_zone_exc = None
    return (second_zone_exc,)


@app.cell(hide_code=True)
def _(mo, second_zone_exc, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = "altstadt"
    _result = None
    if second_zone_exc is None:
        _ok = False
        _msg = "Not attempted: Assign it to `second_zone_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(second_zone_exc, (list, tuple)):
        _ok = False
        _result = f"second_zone_exc={second_zone_exc!r}"
        _msg = "Wrong: That's a whole list (or a pair). The investor wants ONE zone name."
    elif isinstance(second_zone_exc, (int, float)) and not isinstance(second_zone_exc, bool):
        _ok = False
        _result = f"second_zone_exc={second_zone_exc!r}"
        _msg = "Wrong: That's a bar's HEIGHT. She asked for the zone's NAME."
    else:
        _v = str(second_zone_exc).strip().lower()
        _result = f"second_zone_exc={second_zone_exc!r}"
        if _v == _expected:
            _ok = True
            _msg = "Correct: Exercise 9.c stretch: Nord, then Altstadt. Sorted bars make the ranking readable at a glance."
        elif _v == "sued":
            _ok = False
            _msg = "Wrong: That's the SMALLEST zone: you sorted ascending. Tallest first means `reverse=True`."
        elif _v == "hafen":
            _ok = False
            _msg = "Wrong: That's the second entry of the ORIGINAL list order. Sort by height first, then take position 1."
        else:
            _ok = False
            _msg = "Wrong: Pair each total with its zone, sort the pairs by total (largest first), read the second pair's name."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`zip(totals_exc, zones_exc)` makes (total, zone) pairs; `sorted(...)` orders pairs by their first item. Which keyword flips the order so the largest comes first? The second pair holds your zone. For the chart, unzip the sorted pairs back into two lists.",
            "Hint 2 (the structure)": "_ranked = sorted(zip(totals_exc, zones_exc), reverse=___)\nsecond_zone_exc = _ranked[___][1]",
        }
    )
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
