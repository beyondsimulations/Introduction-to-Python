# notebooks/exercises/ex_01_c.py
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # ⚡ Quick exercise: the first receipt line (5 min)

    A customer just ordered. Using the variables below and an f-string with
    `:.2f`, build **one** receipt line of the form
    `"2x Falafel Wrap: 13.80 EUR"` (quantity, item, total price to two
    decimals, currency).
    """
    )
    return


@app.cell
def _():
    # Given — do not change these
    item = "Falafel Wrap"
    qty = 2
    price = 6.90
    return (item, price, qty)


@app.cell
def _():
    # YOUR CODE BELOW — replace None
    line_exc = None
    return (line_exc,)


@app.cell(hide_code=True)
def _(line_exc, mo):
    # Reactive check — re-runs automatically whenever the cell above changes.
    if line_exc is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif line_exc == "2x Falafel Wrap: 13.80 EUR":
        _ok = True
        _msg = "✅ Correct! The receipt printer purrs."
    else:
        _ok = False
        _msg = "❌ Not quite — check the format `qty x item: price:.2f EUR`."
    mo.callout(mo.md(_msg), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save — this was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
