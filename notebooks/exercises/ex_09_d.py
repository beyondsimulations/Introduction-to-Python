# notebooks/exercises/ex_09_d.py
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
    # Quick exercise: fix the axis (5-10 min)

    Episode 9: Tobi's AI drafted the signups slide for the pitch deck.
    It runs, the line climbs like a rocket, and the investor reads the
    axis before she reads the line. The rule: a growth claim starts at
    zero.

    **Predict** first: look at the y-axis numbers below. Where does
    Tobi's axis start, and how far is that from 0?
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
def _():
    # Given: do not change this. Signups per week, week 1 → week 4.
    signups_exd = [1180, 1195, 1210, 1230]
    return (signups_exd,)


@app.cell
def _(plt, signups_exd):
    # Tobi's AI-generated chart: runs fine, the numbers are real
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.plot(range(1, 5), signups_exd, marker="o")
    plt.ylim(1170, 1240)
    plt.ylabel("Signups per week")
    plt.title("Tobi's slide")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The axis starts at 1170. Fix it: set `floor_exd` to where a growth
    chart's y-axis must start, then re-plot `signups_exd` with
    `plt.ylim(floor_exd, 1300)`.

    The chart isn't graded. The check reads `floor_exd`, the number you
    chose for the bottom of the axis.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    floor_exd = None
    return (floor_exd,)


@app.cell
def _(floor_exd, plt, signups_exd):
    plt.figure()
    # YOUR CODE BELOW: re-plot signups_exd with plt.ylim(floor_exd, 1300) (ungraded)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(floor_exd, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 0.0
    _result = None
    if floor_exd is None:
        _ok = False
        _msg = "Not attempted: Assign it to `floor_exd` (a `print` alone doesn't count) and run the cell."
    else:
        try:
            _v = round(float(floor_exd), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. `floor_exd` is where the y-axis starts."
        else:
            _result = f"floor_exd={floor_exd}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Exercise 9.d: from zero, the rocket is a gentle slope. That's the real 4 %."
            elif _v == 1170.0:
                _ok = False
                _msg = "Wrong: That's Tobi's floor, the one that makes the cliff. A growth claim starts at zero."
            elif _v == 1180.0:
                _ok = False
                _msg = "Wrong: Starting at the smallest value is the same trick with a different number. The rule says zero."
            elif _v > 0:
                _ok = False
                _msg = "Wrong: Lower, but still not the baseline. Where does a growth chart start, by the rule on the slide?"
            else:
                _ok = False
                _msg = "Wrong: Below zero only adds empty space under the line. The rule names one number."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "The slide said it in four words: growth starts at zero. `floor_exd` is that number. Then `plt.plot(range(1, 5), signups_exd)` and `plt.ylim(floor_exd, 1300)` in the chart cell.",
            "Hint 2 (the structure)": "floor_exd = ___\n\n# chart cell:\nplt.plot(range(1, 5), signups_exd, marker=\"o\")\nplt.ylim(floor_exd, ___)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the 1300 at the top was a guess. The investor's
    rule for the top of the axis: the biggest value, rounded UP to the
    next full hundred. Compute it from `signups_exd` as `top_exd`, then
    swap the 1300 in your chart for it.
    """
    )
    return


@app.cell
def _(signups_exd):
    # YOUR CODE BELOW: replace None
    top_exd = None
    return (top_exd,)


@app.cell(hide_code=True)
def _(mo, show_result, top_exd):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 1300.0
    _result = None
    if top_exd is None:
        _ok = False
        _msg = "Not attempted: Assign it to `top_exd` (a `print` alone doesn't count) and run the cell."
    else:
        try:
            _v = round(float(top_exd), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. Check what your expression returns."
        else:
            _result = f"top_exd={top_exd}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Exercise 9.d stretch: 1230 rounds up to 1300, so the top of the axis now comes from a rule instead of a guess."
            elif _v == 1230.0:
                _ok = False
                _msg = "Wrong: That's the biggest value itself. The line would touch the ceiling. Round UP to the next hundred."
            elif _v == 1200.0:
                _ok = False
                _msg = "Wrong: `//` rounds DOWN, so 1230 became 1200 and the line runs off the chart. Add one more hundred."
            else:
                _ok = False
                _msg = "Wrong: Take the biggest value, divide by 100 with `//`, add 1, multiply by 100 again."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`max(signups_exd)` is 1230. `1230 // 100` counts the full hundreds in it (12). One more hundred than that, times 100, is the next full hundred above.",
            "Hint 2 (the structure)": "top_exd = (max(___) // 100 + ___) * 100",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
