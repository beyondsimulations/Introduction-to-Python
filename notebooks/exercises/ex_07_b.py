# notebooks/exercises/ex_07_b.py
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
    # Quick exercise: vectorized arithmetic (5–10 min)

    Tobi's 40-tab spreadsheet is on its way out. The investor wants
    metrics, and numpy arrays are the replacement. The key idea: an
    operation on an array applies to *every element at once*. No loop.

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
    _prices_demo = np.array([2.0, 4.0]) * 3
    print(f"tripled -> {_prices_demo}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The investor's numbers deck needs gross prices. Three net menu prices
    need 19% VAT added: all three, in **one expression**, no loop.

    Compute it as `gross_exb` below.
    """
    )
    return


@app.cell
def _(np):
    # Given: do not change this
    net_prices_exb = np.array([8.0, 11.0, 14.0])
    return (net_prices_exb,)


@app.cell
def _(net_prices_exb):
    # YOUR CODE BELOW: replace None
    gross_exb = None
    return (gross_exb,)


@app.cell(hide_code=True)
def _(gross_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [9.52, 13.09, 16.66]
    try:
        _values = [round(float(_v), 2) for _v in gross_exb]
    except (TypeError, ValueError):
        _values = None
    if gross_exb is None:
        _ok = False
        _msg = "Not attempted — Assign it to `gross_exb` (a `print` alone doesn't count) and run the cell."
    elif not hasattr(gross_exb, "__len__") or len(gross_exb) != 3:
        _ok = False
        _msg = "Wrong — Do this as one expression on the whole array, not a single number."
    elif _values == _expected:
        _ok = True
        _msg = "Correct — One expression, all three prices, VAT included. The deck is ready."
    else:
        _ok = False
        _msg = "Wrong — Check the VAT factor: gross = net × 1.19."
    mo.callout(mo.md(_msg + show_result(gross_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "No loop, no indexing: multiply the whole array by the VAT factor in one go.",
            "Hint 2 (the structure)": "gross_exb = net_prices_exb * ___",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the deck also gets a **price ladder**: five evenly spaced price points from 5.0 to 15.0 EUR, both ends included. Build it as `ladder_exb` without typing a single number of it.
    """
    )
    return


@app.cell
def _(np):
    # YOUR CODE BELOW: replace None
    ladder_exb = None
    return (ladder_exb,)


@app.cell(hide_code=True)
def _(ladder_exb, mo, np, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [5.0, 7.5, 10.0, 12.5, 15.0]
    try:
        _values = [round(float(_v), 2) for _v in ladder_exb]
    except (TypeError, ValueError):
        _values = None
    if ladder_exb is None:
        _ok = False
        _msg = "Not attempted — assign it to `ladder_exb` (a `print` alone doesn't count) and run the cell."
    elif np.ndim(ladder_exb) == 0 or _values is None:
        _ok = False
        _msg = "Wrong — the ladder is a whole array of five prices, not one number."
    elif _values == _expected:
        _ok = True
        _msg = "Correct — five rungs, both ends included, and nobody typed 12.5 by hand."
    elif len(_values) == 4:
        _ok = False
        _msg = "Wrong — four rungs. The builder that walks by a step stops *before* the end; you want the one that includes it."
    else:
        _ok = False
        _msg = "Wrong — check start, stop, and count: 5.0 and 15.0 must both be on the ladder, with three rungs between."
    mo.callout(mo.md(_msg + show_result(ladder_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Two builders make evenly spaced arrays: one walks by a step and stops before the end, the other splits a span into a fixed count of points, endpoints included. You want the second.",
            "Hint 2 (the structure)": "ladder_exb = np.linspace(___, ___, ___)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
