# notebooks/exercises/ex_09_c.py
import marimo

app = marimo.App(width="medium", app_title="ex_09_c")


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
    # Quick exercise: proportional ink (5-10 min)
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
    Episode 9: Tobi's slide for the rider meeting shows each rider's
    deliveries this month. His agent picked the y-axis, and Ben's bar
    towers over Deniz's. A bar shows its number by its **length**, so a
    bar on an axis that starts at 75 has lost its first 75. Bars start
    at 0.

    **Predict** first: in the demo below, how many times as tall is the
    right bar as the left one, and how many times as big is its number?
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
    _demo_labels = ["Before", "After"]
    _demo_values = [50, 60]
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.bar(_demo_labels, _demo_values)
    plt.ylim(45, 62)  # the axis starts at 45, so the bars show only 5 and 15
    plt.title("Demo: 60 is 1.2 times 50, the bars say 3 times")
    plt.gca()
    return


@app.cell
def _():
    # Given: do not change this
    riders_exc = ["Aylin", "Ben", "Chiara", "Deniz"]
    return (riders_exc,)


@app.cell
def _():
    # Given: do not change this
    deliveries_exc = [96, 120, 104, 80]
    return (deliveries_exc,)


@app.cell
def _(deliveries_exc, plt, riders_exc):
    # Tobi's slide (given)
    plt.figure()
    plt.bar(riders_exc, deliveries_exc)
    plt.ylim(75, 125)
    plt.ylabel("Deliveries this month")
    plt.title("Ben carries the team")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The investor asks: "How many times as many deliveries as Deniz did
    Ben **really** make?" Answer with the numbers, not the bar lengths:
    `real_exc`. Then redraw Tobi's slide with the bars from 0.

    The chart itself isn't graded. The check below reads `real_exc`.
    """
    )
    return


@app.cell
def _(deliveries_exc, riders_exc):
    # YOUR CODE BELOW: how many times as many deliveries as Deniz Ben made
    real_exc = None
    return (real_exc,)


@app.cell
def _(deliveries_exc, plt, riders_exc):
    plt.figure()
    # YOUR CODE BELOW: the same bars, starting at 0, with a title that states the point (ungraded)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo, real_exc, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 1.5
    _result = None
    if real_exc is None:
        _ok = False
        _msg = "Not attempted: Assign it to `real_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(real_exc, (list, tuple)):
        _ok = False
        _result = f"real_exc={real_exc!r}"
        _msg = "Wrong: That's a list. The investor wants ONE number: how many times as many."
    else:
        try:
            _v = round(float(real_exc), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. Check what your expression returns."
        else:
            _result = f"real_exc={real_exc}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Exercise 9.c: 120 against 80, one and a half times. Ben is ahead, but he doesn't carry the team."
            elif _v == 9.0:
                _ok = False
                _msg = "Wrong: That's what Tobi's picture claims, because both bars start at 75. Use the delivery numbers themselves."
            elif _v == 40.0:
                _ok = False
                _msg = "Wrong: That's how many MORE deliveries Ben made. 'How many times as many' is a ratio."
            elif _v == 0.67:
                _ok = False
                _msg = "Wrong: Flipped: that's Deniz compared with Ben. Ben's number goes on top."
            else:
                _ok = False
                _msg = "Wrong: Divide Ben's deliveries by Deniz's."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Ben sits at position 1 in both lists, Deniz at position 3. 'How many times as many' divides one number by the other. For the chart, leave out whatever moved the axis away from 0.",
            "Hint 2 (the structure)": "```python\nreal_exc = deliveries_exc[___] / deliveries_exc[___]\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** put a number on the lie. In Tobi's chart, how many
    times as **tall** is Ben's bar as Deniz's? Every bar there starts at
    75, so only the part above 75 is visible: `picture_exc`.
    """
    )
    return


@app.cell
def _(deliveries_exc):
    # YOUR CODE BELOW: how many times as tall Ben's bar is as Deniz's in Tobi's chart
    picture_exc = None
    return (picture_exc,)


@app.cell(hide_code=True)
def _(mo, picture_exc, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 9.0
    _result = None
    if picture_exc is None:
        _ok = False
        _msg = "Not attempted: Assign it to `picture_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(picture_exc, (list, tuple)):
        _ok = False
        _result = f"picture_exc={picture_exc!r}"
        _msg = "Wrong: That's a list. The answer is ONE number."
    else:
        try:
            _v = round(float(picture_exc), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. Check what your expression returns."
        else:
            _result = f"picture_exc={picture_exc}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Exercise 9.c stretch: 45 against 5. The picture says 9 times, the data says 1.5. That gap is what 'bars start at 0' prevents."
            elif _v == 1.5:
                _ok = False
                _msg = "Wrong: That's the real ratio. In Tobi's picture each bar starts at 75: measure from there."
            elif _v == 24.0:
                _ok = False
                _msg = "Wrong: Close: you took 75 away from Deniz's bar only. Both bars start at 75."
            elif _v == 0.56:
                _ok = False
                _msg = "Wrong: Close: you took 75 away from Ben's bar only. Both bars start at 75."
            else:
                _ok = False
                _msg = "Wrong: The visible part of a bar is its number minus 75. Compare Ben's visible part with Deniz's."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Ben's bar shows 120 minus 75, Deniz's shows 80 minus 75. Divide one visible part by the other.",
            "Hint 2 (the structure)": "```python\npicture_exc = (deliveries_exc[1] - ___) / (deliveries_exc[3] - ___)\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to hand in. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
