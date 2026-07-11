# notebooks/exercises/ex_05_b.py
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
    # ⚡ Quick exercise: the crash-proof price (5–10 min)

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

    Careful: hardcoding `price_exb = 0.0` defeats the point — your code must
    still work when the text *is* a number.
    """
    )
    return


@app.cell
def _():
    # Given — do not change this
    order_text = "drei"
    return (order_text,)


@app.cell
def _():
    # YOUR CODE BELOW — replace None
    price_exb = None
    return (price_exb,)


@app.cell(hide_code=True)
def _(mo, price_exb, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    if price_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif isinstance(price_exb, float) and price_exb == 0.0:
        _ok = True
        _msg = "✅ Correct! The checkout survives — 0.0 flags the order for a human."
    else:
        _ok = False
        _msg = "❌ Not quite — wrap the float() call in try/except ValueError and fall back to 0.0."
    mo.callout(mo.md(_msg + show_result(price_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save — this was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
