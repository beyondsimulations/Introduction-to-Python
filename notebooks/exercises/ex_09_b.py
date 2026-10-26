# notebooks/exercises/ex_09_b.py
import marimo

app = marimo.App(width="medium", app_title="ex_09_b")


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
    # Quick exercise: the question picks the chart (5-10 min)
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
    Episode 9: MunchCorp sent a new press release, again with one pie:
    their revenue per zone this month, in thousand euros. The investor
    squints at it: "Which zone is their biggest? And which comes
    second?" Four slices of nearly the same size, and nobody in the room
    agrees.

    To **compare** amounts, use bars, sorted tallest first: the eye
    compares lengths well and angles badly.

    **Predict** first: in the pie below, which zone comes second?
    """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _():
    # Given: do not change this
    zones_exb = ["Nord", "Altstadt", "Hafen", "Sued"]
    return (zones_exb,)


@app.cell
def _():
    # Given: do not change this
    munch_exb = [131, 118, 124, 127]
    return (munch_exb,)


@app.cell
def _(munch_exb, plt, zones_exb):
    # MunchCorp's chart (given)
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.pie(munch_exb, labels=zones_exb)
    plt.title("MunchCorp: revenue per zone")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Draw the same numbers as bars, **tallest first**, so the ranking
    reads left to right. Then tell the investor which zone comes
    **second**, as a name.

    The chart itself isn't graded. The check below reads
    `second_exb`, not your bars.
    """
    )
    return


@app.cell
def _(munch_exb, plt, zones_exb):
    plt.figure()
    # YOUR CODE BELOW: bars of munch_exb per zone, tallest first (ungraded)
    plt.gca()
    return


@app.cell
def _(munch_exb, zones_exb):
    # YOUR CODE BELOW: the NAME of the zone with the second-highest revenue
    second_exb = None
    return (second_exb,)


@app.cell(hide_code=True)
def _(mo, second_exb, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _result = None
    if second_exb is None:
        _ok = False
        _msg = "Not attempted: Assign it to `second_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(second_exb, (list, tuple)):
        _ok = False
        _result = f"second_exb={second_exb!r}"
        _msg = "Wrong: That's a whole list (or a pair). The investor wants ONE zone name."
    elif isinstance(second_exb, (int, float)) and not isinstance(second_exb, bool):
        _ok = False
        _result = f"second_exb={second_exb!r}"
        _msg = "Wrong: That's a bar's HEIGHT. She asked for the zone's NAME."
    else:
        _v = str(second_exb).strip().lower()
        _result = f"second_exb={second_exb!r}"
        if _v == "sued":
            _ok = True
            _msg = "Correct: Exercise 9.b: Nord, then Sued. Sorted bars settle in a second what the pie left open."
        elif _v == "nord":
            _ok = False
            _msg = "Wrong: Nord is the biggest. Sort tallest first and read the SECOND bar."
        elif _v == "altstadt":
            _ok = False
            _msg = "Wrong: Altstadt is the second entry of the ORIGINAL list, and the smallest zone. Sort by revenue first."
        elif _v == "hafen":
            _ok = False
            _msg = "Wrong: Hafen comes third, three thousand euros behind Sued. Sorted smallest first? Tallest first is the other direction."
        else:
            _ok = False
            _msg = "Wrong: Pick one of the four zone names in `zones_exb`."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`zip(munch_exb, zones_exb)` makes (revenue, zone) pairs, and `sorted(...)` orders pairs by their first item. Which keyword puts the largest first? The second pair holds your zone. For the chart, take the sorted pairs apart into names and heights again.",
            "Hint 2 (the structure)": "```python\n_ranked = sorted(zip(munch_exb, zones_exb), reverse=___)\nsecond_exb = _ranked[___][1]\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor has three more questions. For each one,
    which chart answers it: `"bar"`, `"histogram"`, `"scatter"` or
    `"line"`? Fill in the dict `charts_exb` with one chart per key:

    - `"spread"`: How are our order values spread, many small ones and a few big ones?
    - `"together"`: Do orders with more items take longer to deliver?
    - `"time"`: How did revenue develop over the last eight weeks?
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: a dict with the keys "spread", "together" and "time", one chart name each
    charts_exb = None
    return (charts_exb,)


@app.cell(hide_code=True)
def _(charts_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = {"spread": "hist", "together": "scatter", "time": "line"}
    _why = {
        "spread": "`spread`: a spread is counted per range of values, which is not a category or a moment in time.",
        "together": "`together`: two numbers per order, one on each axis, and no line joining orders that have no order.",
        "time": "`time`: eight weeks in a row is change over time, so the points follow each other.",
    }
    _result = None
    if charts_exb is None:
        _ok = False
        _msg = "Not attempted: Assign it to `charts_exb` (a `print` alone doesn't count) and run the cell."
    elif not isinstance(charts_exb, dict):
        _ok = False
        _result = f"charts_exb={charts_exb!r}"
        _msg = "Wrong: `charts_exb` should be a dict, like `{\"spread\": \"...\", \"together\": \"...\", \"time\": \"...\"}`."
    elif set(charts_exb) != set(_expected):
        _ok = False
        _result = f"charts_exb={charts_exb!r}"
        _msg = "Wrong: The dict needs exactly the keys `\"spread\"`, `\"together\"` and `\"time\"`."
    else:
        _result = f"charts_exb={charts_exb!r}"
        _off = [
            _key
            for _key, _chart in _expected.items()
            if _chart not in str(charts_exb[_key]).strip().lower()
        ]
        if not _off:
            _ok = True
            _msg = "Correct: Exercise 9.b stretch: histogram, scatter, line. Name the question first, and the chart follows."
        else:
            _ok = False
            _msg = "Wrong: " + _why[_off[0]]
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Ask what each question compares: categories (bar), how often values fall into each range (histogram), two numbers per order (scatter), or one value over time (line).",
            "Hint 2 (the structure)": "```python\ncharts_exb = {\"spread\": \"___\", \"together\": \"___\", \"time\": \"___\"}\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to hand in. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
