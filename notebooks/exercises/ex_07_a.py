# notebooks/exercises/ex_07_a.py
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
    # Quick exercise: one operation, every element (5–10 min)

    Tobi's 40-tab spreadsheet is on its way out. In numpy, an operation
    on an array lands on *every element at once*: no loop, no `.append`.

    **Predict** first: what does the cell below print, then run it.
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
    import numpy as np
    return (np,)


@app.cell
def _(np):
    # Worked example (read + run this)
    _demo = np.array([2.0, 4.0, 5.0]) - 1
    print(f"one less each -> {_demo}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Three dishes, three menu prices in `prices_exa`. The courier costs
    3.50 EUR per order, whatever the dish. The investor wants the
    **margin per dish**: price minus courier cost, all three in **one
    expression**, no loop.

    Compute it as `margin_exa`.
    """
    )
    return


@app.cell
def _(np):
    # Given: do not change this
    prices_exa = np.array([9.5, 12.0, 7.5])
    return (prices_exa,)


@app.cell
def _(prices_exa):
    # YOUR CODE BELOW: replace None
    margin_exa = None
    return (margin_exa,)


@app.cell(hide_code=True)
def _(margin_exa, mo, np, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [6.0, 8.5, 4.0]
    try:
        _values = [round(float(_v), 2) for _v in margin_exa]
    except (TypeError, ValueError):
        _values = None
    if margin_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `margin_exa` (a `print` alone doesn't count) and run the cell."
    elif np.ndim(margin_exa) == 0 or _values is None:
        _ok = False
        _msg = "Wrong — one number came out. The margin is one value *per dish*: apply the operation to the whole array."
    elif len(_values) != 3:
        _ok = False
        _msg = "Wrong — three dishes, three margins. Subtract from the array itself, not from a copy you built by hand."
    elif _values == _expected:
        _ok = True
        _msg = "Correct — one subtraction, three margins. That is the bigger boat."
    else:
        _ok = False
        _msg = "Wrong — check the rule: margin = price minus 3.50, nothing else."
    mo.callout(mo.md(_msg + show_result(margin_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "No loop, no indexing: subtract the courier cost from the whole array in one go, exactly like the worked example.",
            "Hint 2 (the structure)": "margin_exa = prices_exa - ___",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the kitchen sold each dish a different number of times tonight: `counts_exa` below. The investor wants the **revenue per dish**: price times count, dish by dish. Two arrays, one operator, as `revenue_exa`.
    """
    )
    return


@app.cell
def _(np):
    # Given: do not change this
    counts_exa = np.array([4, 2, 6])
    return (counts_exa,)


@app.cell
def _(counts_exa, prices_exa):
    # YOUR CODE BELOW: replace None
    revenue_exa = None
    return (revenue_exa,)


@app.cell(hide_code=True)
def _(mo, np, revenue_exa, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [38.0, 24.0, 45.0]
    try:
        _values = [round(float(_v), 2) for _v in revenue_exa]
    except (TypeError, ValueError):
        _values = None
    if revenue_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `revenue_exa` (a `print` alone doesn't count) and run the cell."
    elif np.ndim(revenue_exa) == 0 or _values is None:
        _ok = False
        _msg = "Wrong — one number came out. Revenue is one value *per dish*; multiply the two arrays, don't total anything."
    elif len(_values) != 3:
        _ok = False
        _msg = "Wrong — three dishes, three revenues. Multiply the array of prices by the array of counts."
    elif _values == _expected:
        _ok = True
        _msg = "Correct — first with first, second with second: arrays combine element by element."
    else:
        _ok = False
        _msg = "Wrong — pair each price with its own count: `prices_exa` times `counts_exa`, in that order of elements."
    mo.callout(mo.md(_msg + show_result(revenue_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Two arrays of the same length combine element by element: the first price meets the first count, and so on. One operator between the two names does it.",
            "Hint 2 (the structure)": "revenue_exa = prices_exa ___ counts_exa",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
