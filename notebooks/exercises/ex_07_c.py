# notebooks/exercises/ex_07_c.py
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
    # ⚡ Quick exercise: 2D arrays and axis (5–10 min)

    A 2D array has rows and columns, and `.sum()` needs to know which one
    to collapse: `axis=0` collapses DOWN the rows — one number per column.
    `axis=1` collapses ACROSS the columns — one number per row.

    **Predict** first: what do the prints below show, then run it.
    """
    )
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(np):
    # Worked example (read + run this)
    _demo = np.array([[1, 2], [3, 4]])
    print(_demo.sum(axis=0))
    print(_demo.sum(axis=1))
    print(f"position of the biggest: {_demo.sum(axis=0).argmax()}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `sales_exc` below is four days of sales across three delivery zones
    (rows = days, columns = zones). The investor wants the total per
    zone, and which zone is winning.

    Compute `zone_totals_exc` (one total per zone) and `best_zone_exc`
    (the **index** of the best zone — `argmax` tells you WHERE the
    maximum sits).
    """
    )
    return


@app.cell
def _(np):
    # Given — do not change this
    sales_exc = np.array([[7, 12, 5], [9, 4, 14], [11, 8, 6], [3, 10, 13]])
    return (sales_exc,)


@app.cell
def _(sales_exc):
    # YOUR CODE BELOW — replace None
    zone_totals_exc = None
    return (zone_totals_exc,)


@app.cell
def _(sales_exc):
    # YOUR CODE BELOW — replace None
    best_zone_exc = None
    return (best_zone_exc,)


@app.cell(hide_code=True)
def _(best_zone_exc, mo, np, show_result, zone_totals_exc):
    # Reactive check — re-runs automatically whenever the cells above change.
    _expected_totals = [30, 34, 38]
    _expected_best = 2
    _result = None
    # Coerce to a plain list of ints first — anything that can't be must
    # degrade to a message, never crash the check.
    try:
        _totals = [int(_v) for _v in zone_totals_exc]
    except (TypeError, ValueError):
        _totals = None
    if zone_totals_exc is None or best_zone_exc is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif _totals is not None and len(_totals) == 4:
        _ok = False
        _msg = "❌ Not quite — you summed per DAY, not per zone. Which axis collapses the days?"
    elif _totals != _expected_totals:
        _ok = False
        _msg = "❌ The zone totals aren't right yet — check `axis=0` versus `axis=1`."
    elif isinstance(best_zone_exc, (int, np.integer)) and int(best_zone_exc) == _expected_best:
        _ok = True
        _msg = "✅ Correct! Zone 2 wins, and the totals are ready for the deck."
    else:
        _ok = False
        _msg = "❌ The totals are right, but the best zone isn't — which index holds the highest total?"
    if zone_totals_exc is not None and best_zone_exc is not None:
        _result = f"zone_totals_exc={zone_totals_exc}, best_zone_exc={best_zone_exc}"
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "axis=0 collapses down the rows into one number per column (zone); once you have the per-zone totals, argmax finds the index of the biggest one.",
            "💡 Hint 2 (the structure)": "zone_totals_exc = sales_exc.sum(axis=___)\nbest_zone_exc = int(sales_exc.sum(axis=___).___())",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save — this was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
