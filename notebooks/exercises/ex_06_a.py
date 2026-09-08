# notebooks/exercises/ex_06_a.py
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
    # Quick exercise: import a tool instead of building it (10 min)

    Need a whole-number result that always rounds *up*, never down? Don't
    write your own rounding logic. The standard library already has it:
    `math.ceil` always rounds up to the next whole number, exactly what
    you need whenever a fraction of a box, crate, or shipment still counts
    as a whole one.

    300 / 48 is 6.25. **Predict** what the cell below prints, then run it.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "💾 **Saving your work:** this notebook runs in your browser. Press "
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

    Compute it as `boxes_exa` below, using `math`, not guesswork.
    """
    )
    return


@app.cell
def _(math):
    # YOUR CODE BELOW: replace None
    boxes_exa = None
    return (boxes_exa,)


@app.cell(hide_code=True)
def _(boxes_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if boxes_exa is None:
        _ok = False
        _msg = "🔲 Not attempted yet. Assign it to `boxes_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(boxes_exa, int) and boxes_exa == 9:
        _ok = True
        _msg = "✅ Correct! Nine boxes. The investor breakfast is covered with quiches to spare."
    else:
        _ok = False
        _msg = "❌ Not quite. 200 / 24 isn't a whole number, and you need the next whole box up. Which `math` function rounds up?"
    mo.callout(mo.md(_msg + show_result(boxes_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "200 / 24 gives 8.33... You need the next whole box, and math has a function for exactly that.",
            "💡 Hint 2 (the structure)": "boxes_exa = math.___(200 / 24)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
