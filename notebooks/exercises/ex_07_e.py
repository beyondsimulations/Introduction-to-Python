# notebooks/exercises/ex_07_e.py
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
    # Quick exercise: 2D arrays and axis (5–10 min)

    A 2D array has rows and columns, and `.sum()` needs to know which one
    to collapse: `axis=0` collapses DOWN the rows (one number per column).
    `axis=1` collapses ACROSS the columns (one number per row).

    **Predict** first: what do the prints below show, then run it.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Saving your work:** this notebook runs in your browser. Press"
            "**Cmd/Ctrl+S** to save, and always save **before** menu → Download → "
            "*Download Python code*. Without a save first, the download is an empty file."
        ),
        kind="info",
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
    `sales_exe` below is four days of sales across three delivery zones
    (rows = days, columns = zones). The investor wants the total per
    zone, and which zone is winning.

    Compute `zone_totals_exe` (one total per zone) and `best_zone_exe`
    (the **index** of the best zone: `argmax` tells you WHERE the
    maximum sits).
    """
    )
    return


@app.cell
def _(np):
    # Given: do not change this
    sales_exe = np.array([[7, 12, 5], [9, 4, 14], [11, 8, 6], [3, 10, 13]])
    return (sales_exe,)


@app.cell
def _(sales_exe):
    # YOUR CODE BELOW: replace None
    zone_totals_exe = None
    return (zone_totals_exe,)


@app.cell
def _(sales_exe):
    # YOUR CODE BELOW: replace None
    best_zone_exe = None
    return (best_zone_exe,)


@app.cell(hide_code=True)
def _(best_zone_exe, mo, np, show_result, zone_totals_exe):
    # Reactive check. Re-runs when you run the cell above.
    _expected_totals = [30, 34, 38]
    _expected_best = 2
    _result = None
    try:
        _totals = [int(_v) for _v in zone_totals_exe]
    except (TypeError, ValueError):
        _totals = None
    if zone_totals_exe is None or best_zone_exe is None:
        _ok = False
        _msg = "Not attempted — Assign it to `zone_totals_exe` and `best_zone_exe` (a `print` alone doesn't count) and run the cell."
    elif _totals is not None and len(_totals) == 4:
        _ok = False
        _msg = "Wrong — You summed per DAY, not per zone. Which axis collapses the days?"
    elif _totals != _expected_totals:
        _ok = False
        _msg = "Wrong — The zone totals aren't right yet. Check `axis=0` versus `axis=1`."
    elif isinstance(best_zone_exe, (int, np.integer)) and int(best_zone_exe) == _expected_best:
        _ok = True
        _msg = "Correct — Zone 2 wins, and the totals are ready for the deck."
    else:
        _ok = False
        _msg = "Wrong — The totals are right, but the best zone isn't. Which index holds the highest total?"
    if zone_totals_exe is not None and best_zone_exe is not None:
        _result = f"zone_totals_exe={zone_totals_exe}, best_zone_exe={best_zone_exe}"
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "axis=0 collapses down the rows into one number per column (zone); once you have the per-zone totals, argmax finds the index of the biggest one.",
            "Hint 2 (the structure)": "zone_totals_exe = sales_exe.sum(axis=___)\nbest_zone_exe = int(sales_exe.sum(axis=___).___())",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor flips the question: which **day** was the best? Collapse the grid the other way and find the index of the biggest per-day total, as `best_day_exe`.
    """
    )
    return


@app.cell
def _(sales_exe):
    # YOUR CODE BELOW: replace None
    best_day_exe = None
    return (best_day_exe,)


@app.cell(hide_code=True)
def _(best_day_exe, mo, np, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 1
    try:
        _day = int(best_day_exe)
    except (TypeError, ValueError):
        _day = None
    if best_day_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `best_day_exe` (a `print` alone doesn't count) and run the cell."
    elif _day is None:
        _ok = False
        if np.ndim(best_day_exe) > 0:
            _msg = "Wrong — that's still a whole array. `argmax` reduces the per-day totals to one index."
        else:
            _msg = "Wrong — the answer is an index, one whole number."
    elif _day == _expected:
        _ok = True
        _msg = "Correct — day 1 wins with 27 sales. Other axis, same argmax."
    elif _day == 2:
        _ok = False
        _msg = "Wrong — that's the best *zone* again. Per-day totals need the days to stay, so the zones must disappear: check the axis."
    else:
        _ok = False
        _msg = "Wrong — sum across the columns first (one number per day), then ask where the maximum sits."
    mo.callout(mo.md(_msg + show_result(best_day_exe)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "One number per day means the zones (columns) must disappear: that is the other axis. Then argmax on those totals gives the day's index.",
            "Hint 2 (the structure)": "best_day_exe = int(sales_exe.sum(axis=___).___())",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
