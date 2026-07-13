# notebooks/exercises/ex_09_b.py
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
    # ⚡ Quick exercise: the right chart for categories (5–10 min)

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


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(plt):
    # Worked example (read + run this)
    _demo_teams = ["Alpha", "Beta"]
    _demo_scores = [7, 3]
    plt.figure()  # starts a fresh figure — keeps this chart from drawing on top of the last one
    plt.bar(_demo_teams, _demo_scores)
    plt.title("Demo: two teams")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `zones_exb` and `totals_exb` below are tonight's revenue by delivery
    zone. Plot a bar chart, then tell the investor which ZONE brought in
    the most, as a name, not a number.

    The chart itself isn't graded. The check below reads
    `best_zone_exb`, not your bars.
    """
    )
    return


@app.cell
def _():
    # Given — do not change this
    zones_exb = ["Nord", "Sued", "Hafen", "Altstadt"]
    return (zones_exb,)


@app.cell
def _():
    # Given — do not change this
    totals_exb = [412.60, 268.40, 305.90, 351.20]
    return (totals_exb,)


@app.cell
def _(plt, totals_exb, zones_exb):
    plt.figure()
    # YOUR CODE BELOW — plot zones_exb vs totals_exb (labels/title optional, ungraded)
    plt.gca()
    return


@app.cell
def _(totals_exb, zones_exb):
    # YOUR CODE BELOW — replace None
    best_zone_exb = None
    return (best_zone_exb,)


@app.cell(hide_code=True)
def _(best_zone_exb, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    _expected = "nord"
    _result = None
    if best_zone_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif isinstance(best_zone_exb, (list, tuple)):
        _ok = False
        _result = f"best_zone_exb={best_zone_exb!r}"
        _msg = "❌ That's the whole list — the investor wants ONE winner, not all four zones."
    elif isinstance(best_zone_exb, (int, float)) and not isinstance(best_zone_exb, bool):
        _ok = False
        _result = f"best_zone_exb={best_zone_exb!r}"
        _msg = "❌ That's the bar's HEIGHT (a euro amount) — the investor asked WHICH zone, by name."
    else:
        _v = str(best_zone_exb).strip().lower()
        _result = f"best_zone_exb={best_zone_exb!r}"
        if _v == _expected:
            _ok = True
            _msg = "✅ Correct! One glance at the bar chart and the investor knows where to expand."
        else:
            _ok = False
            _msg = "❌ Not quite — read the tallest bar again and check its label."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`plt.bar(zones_exb, totals_exb)` draws the bars — but the check wants the zone's NAME, not its height. Which list method finds the POSITION of the largest number in `totals_exb`? Use that position to look up a name in `zones_exb`.",
            "💡 Hint 2 (the structure)": "_best_index = totals_exb.index(___(totals_exb))\nbest_zone_exb = zones_exb[___]",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
