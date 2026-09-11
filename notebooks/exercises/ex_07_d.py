# notebooks/exercises/ex_07_d.py
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
    # Quick exercise: collapsing a grid (5–10 min)

    A 2D array has rows and columns, and `.sum()` needs to know which
    one disappears: `axis=0` collapses DOWN the rows (one number per
    column), `axis=1` collapses ACROSS the columns (one number per row).

    **Predict** first: what does the cell below print, then run it.
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
    _demo = np.array([[1, 2, 3], [4, 5, 6]])
    print(_demo.sum(axis=0))
    print(_demo.sum(axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `runs_exd` below is three days of deliveries across four zones
    (rows = days, columns = zones). Tobi's spreadsheet had a "daily
    total" column he filled in by hand. The investor wants it computed:
    **one total per day**, as `day_totals_exd`.
    """
    )
    return


@app.cell
def _(np):
    # Given: do not change this
    runs_exd = np.array([[12, 7, 9, 4], [8, 11, 6, 10], [14, 9, 13, 5]])
    return (runs_exd,)


@app.cell
def _(runs_exd):
    # YOUR CODE BELOW: replace None
    day_totals_exd = None
    return (day_totals_exd,)


@app.cell(hide_code=True)
def _(day_totals_exd, mo, np, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [32, 35, 41]
    try:
        _totals = [int(_v) for _v in day_totals_exd]
    except (TypeError, ValueError):
        _totals = None
    if day_totals_exd is None:
        _ok = False
        _msg = "Not attempted — assign it to `day_totals_exd` (a `print` alone doesn't count) and run the cell."
    elif np.ndim(day_totals_exd) == 0 or _totals is None:
        _ok = False
        _msg = "Wrong — one number came out: that's the grand total. Give `.sum()` an axis so one direction survives."
    elif len(_totals) == 4:
        _ok = False
        _msg = "Wrong — four numbers is one per *zone*: you collapsed the days. The zones must disappear instead, so pick the other axis."
    elif _totals == _expected:
        _ok = True
        _msg = "Correct — three days, three totals, and the by-hand column is gone."
    else:
        _ok = False
        _msg = "Wrong — three numbers, but not the day totals. Sum `runs_exd` itself, across the columns."
    mo.callout(mo.md(_msg + show_result(day_totals_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "One number per day means the days stay and the zones (columns) disappear. Which axis collapses ACROSS the columns?",
            "Hint 2 (the structure)": "day_totals_exd = runs_exd.sum(axis=___)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor wants a second column for the deck: the **average deliveries per zone** over the three days, as `zone_means_exd`. Other direction, other method.
    """
    )
    return


@app.cell
def _(runs_exd):
    # YOUR CODE BELOW: replace None
    zone_means_exd = None
    return (zone_means_exd,)


@app.cell(hide_code=True)
def _(mo, np, show_result, zone_means_exd):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [11.33, 9.0, 9.33, 6.33]
    try:
        _means = [round(float(_v), 2) for _v in zone_means_exd]
    except (TypeError, ValueError):
        _means = None
    if zone_means_exd is None:
        _ok = False
        _msg = "Not attempted — assign it to `zone_means_exd` (a `print` alone doesn't count) and run the cell."
    elif np.ndim(zone_means_exd) == 0 or _means is None:
        _ok = False
        _msg = "Wrong — one number came out: that's the average over the whole grid. Give `.mean()` an axis."
    elif len(_means) == 3:
        _ok = False
        _msg = "Wrong — three numbers is one per *day*. Per zone, the days must disappear: collapse DOWN the rows."
    elif _means == _expected:
        _ok = True
        _msg = "Correct — four zones, four averages. Same axis rule, any method: sum, mean, max."
    elif _means == [34.0, 27.0, 28.0, 19.0]:
        _ok = False
        _msg = "Wrong — those are the zone *totals*. The investor asked for the average per zone."
    else:
        _ok = False
        _msg = "Wrong — four numbers, but not the zone averages. Take the mean of `runs_exd` down the rows."
    mo.callout(mo.md(_msg + show_result(zone_means_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Per zone means the zones stay and the days (rows) disappear, so it is the axis you did not use before. And an average is a mean, not a sum.",
            "Hint 2 (the structure)": "zone_means_exd = runs_exd.___(axis=___)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
