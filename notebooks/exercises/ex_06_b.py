# notebooks/exercises/ex_06_b.py
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
    # Quick exercise: import a tool instead of building it (5-10 min)

    Need a whole-number result that rounds *up*? Don't write your own
    rounding logic. The standard library already has it: `math.ceil` rounds
    up to the next whole number, which is what you need whenever a fraction
    of a crate still counts as a whole one.

    300 / 48 is 6.25. **Predict** what the cell below prints, then run it.
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
    import math
    return (math,)


@app.cell
def _(math):
    # Worked example (read + run this)
    _crates_demo = math.ceil(300 / 48)
    print(f"300 avocados in crates of 48 -> {_crates_demo} crates")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The investor breakfast is tomorrow: 200 mini quiches need to go out,
    and the bakery boxes hold 24 quiches each. How many boxes does Tobi
    need to order?

    Compute it as `boxes_exb` below, using `math`.
    """
    )
    return


@app.cell
def _(math):
    # YOUR CODE BELOW: replace None
    boxes_exb = None
    return (boxes_exb,)


@app.cell(hide_code=True)
def _(boxes_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if boxes_exb is None:
        _ok = False
        _msg = "Not attempted: assign it to `boxes_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(boxes_exb, int) and boxes_exb == 9:
        _ok = True
        _msg = "Correct: Nine boxes. The investor breakfast is covered with quiches to spare."
    else:
        _ok = False
        _msg = "Wrong: 200 / 24 isn't a whole number, and you need the next whole box up. Which `math` function rounds up?"
    mo.callout(mo.md(_msg + show_result(boxes_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "200 / 24 gives 8.33... You need the next whole box, and math has a function for exactly that.",
            "Hint 2 (the structure)": "boxes_exb = math.___(200 / 24)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor caps the box budget at **10.00 EUR**, and
    a box costs **1.35 EUR**. How many boxes can Tobi actually afford? This
    time a fraction of a box is *not* a box you can buy.

    Compute it as `affordable_exb`, again with `math`.
    """
    )
    return


@app.cell
def _(math):
    # YOUR CODE BELOW: replace None
    affordable_exb = None
    return (affordable_exb,)


@app.cell(hide_code=True)
def _(affordable_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if affordable_exb is None:
        _ok = False
        _msg = "Not attempted: assign it to `affordable_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(affordable_exb, int) and affordable_exb == 7:
        _ok = True
        _msg = "Correct: seven boxes, two short of the nine Tobi needs. The investor now has a budget conversation to start."
    elif isinstance(affordable_exb, int) and affordable_exb == 8:
        _ok = False
        _msg = "Wrong: eight boxes cost 10.80 EUR, over the cap. Rounding up was right for *needed* boxes; for *affordable* ones you round down."
    else:
        _ok = False
        _msg = "Wrong: 10 / 1.35 is 7.4 boxes, and the last 0.4 of a box isn't for sale. Which `math` function rounds down?"
    mo.callout(mo.md(_msg + show_result(affordable_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`ceil` rounds up; its partner in `math` rounds down. Same shape of call, opposite direction.",
            "Hint 2 (the structure)": "affordable_exb = math.___(10 / 1.35)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
