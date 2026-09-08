# notebooks/exercises/ex_05_b.py
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
    # Quick exercise: the crash-proof price (10 min)

    A customer typed `"drei"` into the price field instead of a number, and
    the checkout went straight to a traceback in front of the whole queue.
    The crashing line:

    ```python
    order_text = "drei"
    price = float(order_text)
    ```

    Wrap `float(order_text)` in a `try`/`except ValueError` so that when the
    text isn't a number, the checkout **survives** and `price_exb` falls back
    to `0.0` instead of crashing.

    Careful: hardcoding `price_exb = 0.0` defeats the point. Your code must
    still work when the text *is* a number.
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
    # Given: do not change this
    order_text = "drei"
    return (order_text,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    price_exb = None
    return (price_exb,)


@app.cell(hide_code=True)
def _(mo, price_exb, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if price_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet. Assign it to `price_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(price_exb, float) and price_exb == 0.0:
        _ok = True
        _msg = "✅ Correct! The checkout survives, and 0.0 flags the order for a human."
    else:
        _ok = False
        _msg = "❌ Not quite. Wrap the float() call in try/except ValueError and fall back to 0.0."
    mo.callout(mo.md(_msg + show_result(price_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
