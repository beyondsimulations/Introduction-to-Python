# notebooks/exercises/ex_09_d.py
import marimo

app = marimo.App(width="medium", app_title="ex_09_d")


@app.cell(hide_code=True)
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
    # Quick exercise: make one point (5-10 min)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Episode 9: the new rider goes to the zone that **grew the most**.
    Tobi's agent drew six weeks of orders per zone: four colors, a
    legend, and the title *Orders per week*. The answer is in there,
    but the investor has to hunt for it.

    One accent color for the point and grey for the rest, the names at
    the line ends instead of a legend, and a title that states the
    point: then the chart answers before anyone asks.

    **Predict** first: in the demo below, which line do you look at
    first, and why?
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
    _demo_weeks = [1, 2, 3, 4]
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.plot(_demo_weeks, [10, 11, 10, 12], color="lightgrey")  # the rest: quiet
    plt.plot(_demo_weeks, [9, 13, 18, 24], color="darkred", linewidth=3)  # the point
    plt.text(4.1, 12, "Team A", color="grey")  # a name at the line end, no legend
    plt.text(4.1, 24, "Team B", color="darkred")
    plt.xlim(0.8, 4.8)  # room on the right for the names
    plt.title("Demo: Team B grew from 9 to 24")
    plt.gca()
    return


@app.cell
def _():
    # Given: do not change this
    weekly_exd = {
        "Nord": [40, 42, 41, 43, 42, 44],
        "Altstadt": [55, 53, 54, 52, 53, 51],
        "Hafen": [30, 34, 39, 45, 50, 57],
        "Sued": [38, 37, 39, 38, 40, 39],
    }
    return (weekly_exd,)


@app.cell
def _(plt, weekly_exd):
    # Tobi's slide (given)
    plt.figure()
    for _zone, _orders in weekly_exd.items():
        plt.plot([1, 2, 3, 4, 5, 6], _orders, marker="o", label=_zone)
    plt.legend()
    plt.xlabel("Week")
    plt.ylabel("Orders")
    plt.title("Orders per week")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Which zone grew the most from week 1 to week 6, in percent of its
    week 1? Put its name in `zone_exd`. Then redraw Tobi's slide so it
    makes that one point: your zone stands out, the others step back,
    every line carries its name, and the title says what happened.

    The chart itself isn't graded. The check below reads `zone_exd`.
    """
    )
    return


@app.cell
def _(weekly_exd):
    # YOUR CODE BELOW: the NAME of the zone that grew the most from week 1 to week 6
    zone_exd = None
    return (zone_exd,)


@app.cell
def _(plt, weekly_exd, zone_exd):
    plt.figure()
    # YOUR CODE BELOW: one accent line, grey for the rest, names at the line ends, a claim as title (ungraded)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo, show_result, zone_exd):
    # Reactive check. Re-runs when you run the cell above.
    _result = None
    if zone_exd is None:
        _ok = False
        _msg = "Not attempted: Assign it to `zone_exd` (a `print` alone doesn't count) and run the cell."
    elif isinstance(zone_exd, (list, tuple, dict)):
        _ok = False
        _result = f"zone_exd={zone_exd!r}"
        _msg = "Wrong: That's a whole collection. The rider goes to ONE zone: give its name."
    elif isinstance(zone_exd, (int, float)) and not isinstance(zone_exd, bool):
        _ok = False
        _result = f"zone_exd={zone_exd!r}"
        _msg = "Wrong: That's a number. The investor asked WHICH zone, by name."
    else:
        _v = str(zone_exd).strip().lower()
        _result = f"zone_exd={zone_exd!r}"
        if _v == "hafen":
            _ok = True
            _msg = "Correct: Exercise 9.d: Hafen, from 30 to 57 orders a week. One red line, three grey ones, and the rider's zone is obvious."
        elif _v == "altstadt":
            _ok = False
            _msg = "Wrong: Altstadt has the most orders, but it shrank from 55 to 51. The rider goes where orders GREW."
        elif _v in ("nord", "sued"):
            _ok = False
            _msg = "Wrong: That zone barely moved. Compare week 6 with week 1 for every zone."
        else:
            _ok = False
            _msg = "Wrong: Pick one of the four zone names in `weekly_exd`."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "For each zone, compare its last week with its first: `weekly_exd[\"Nord\"][-1]` against `weekly_exd[\"Nord\"][0]`. A loop over `weekly_exd.items()` keeps the zone whose ratio is the largest. For the chart: `color=\"lightgrey\"` for the quiet lines, `plt.text(x, y, name)` for the names.",
            "Hint 2 (the structure)": "```python\n_best, _best_ratio = None, 0\nfor _zone, _orders in weekly_exd.items():\n    _ratio = _orders[___] / _orders[___]\n    if _ratio > _best_ratio:\n        _best, _best_ratio = _zone, _ratio\nzone_exd = ___\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** a claim needs its proof. By how many **percent** did
    your zone grow from week 1 to week 6? That number goes into the
    title: `growth_exd`.
    """
    )
    return


@app.cell
def _(weekly_exd, zone_exd):
    # YOUR CODE BELOW: the growth of zone_exd from week 1 to week 6, in percent of week 1
    growth_exd = None
    return (growth_exd,)


@app.cell(hide_code=True)
def _(growth_exd, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 90.0
    _result = None
    if growth_exd is None:
        _ok = False
        _msg = "Not attempted: Assign it to `growth_exd` (a `print` alone doesn't count) and run the cell."
    elif isinstance(growth_exd, (list, tuple)):
        _ok = False
        _result = f"growth_exd={growth_exd!r}"
        _msg = "Wrong: That's a list. The title needs ONE number."
    else:
        try:
            _v = round(float(growth_exd), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. Check what your expression returns."
        else:
            _result = f"growth_exd={growth_exd}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Exercise 9.d stretch: +90 % in six weeks. 'Hafen grew 90 % in six weeks' is a title the investor can check."
            elif _v == 27.0:
                _ok = False
                _msg = "Wrong: That's the growth in ORDERS. The title wants it in percent of week 1."
            elif _v == 0.9:
                _ok = False
                _msg = "Wrong: That's the growth as a fraction. Times 100 makes it percent."
            elif _v == 47.37:
                _ok = False
                _msg = "Wrong: That's the growth in percent of week 6. Growth is measured from where you started: week 1."
            elif _v == 190.0:
                _ok = False
                _msg = "Wrong: That's week 6 in percent of week 1. Growth is only the part ABOVE 100 %."
            else:
                _ok = False
                _msg = "Wrong: Growth in percent is the change from week 1 to week 6, divided by week 1, times 100."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Take your zone's list from `weekly_exd`. The change is last week minus first week; divide it by the first week and multiply by 100.",
            "Hint 2 (the structure)": "```python\n_orders = weekly_exd[zone_exd]\ngrowth_exd = (_orders[___] - _orders[___]) / _orders[___] * 100\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to hand in. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
