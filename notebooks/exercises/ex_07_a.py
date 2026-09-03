# notebooks/exercises/ex_07_a.py
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
    # ⚡ Quick exercise: vectorized arithmetic (10 min)

    Kevin's 40-tab spreadsheet is on its way out. The investor wants
    metrics, and numpy arrays are the replacement. The key idea: an
    operation on an array applies to *every element at once*. No loop.

    **Predict** first: what does the cell below print, then run it.
    """
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

    Compute it as `gross_exa` below.
    """
    )
    return


@app.cell
def _(np):
    # Given — do not change this
    net_prices_exa = np.array([8.0, 11.0, 14.0])
    return (net_prices_exa,)


@app.cell
def _(net_prices_exa):
    # YOUR CODE BELOW — replace None
    gross_exa = None
    return (gross_exa,)


@app.cell(hide_code=True)
def _(gross_exa, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    _expected = [9.52, 13.09, 16.66]
    # Coerce to a plain list of rounded floats first — anything that can't be
    # must degrade to a message, never crash the check.
    try:
        _values = [round(float(_v), 2) for _v in gross_exa]
    except (TypeError, ValueError):
        _values = None
    if gross_exa is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif not hasattr(gross_exa, "__len__") or len(gross_exa) != 3:
        _ok = False
        _msg = "❌ Not quite — do this as one expression on the whole array, not a single number."
    elif _values == _expected:
        _ok = True
        _msg = "✅ Correct! One expression, all three prices, VAT included — the deck is ready."
    else:
        _ok = False
        _msg = "❌ Not quite — check the VAT factor: gross = net × 1.19."
    mo.callout(mo.md(_msg + show_result(gross_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "No loop, no indexing — multiply the whole array by the VAT factor in one go.",
            "💡 Hint 2 (the structure)": "gross_exa = net_prices_exa * ___",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
