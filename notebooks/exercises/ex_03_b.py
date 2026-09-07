# notebooks/exercises/ex_03_b.py
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
    # Quick exercise: fix the Order class (10 min)

    Tobi wrote the startup's first class — an `Order` that's supposed to
    compute its own total. Except a 2× Pad Thai order charges like a single
    portion. Find the bug in `total()` and fix it.
    """
    )
    return


@app.cell
def _():
    class Order:
        def __init__(self, item, qty, price):
            self.item = item
            self.qty = qty
            self.price = price

        def total(self):
            # TOBI'S BUG — the order total ignores something
            return self.price

    return (Order,)


@app.cell(hide_code=True)
def _(Order, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    # Wrapped in try/except: a broken method must show a ❌, never crash the check.
    try:
        _result = Order("Pad Thai", 2, 8.90).total()
    except Exception:
        _ok = False
        _msg = "❌ Still crashing — read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if isinstance(_result, (int, float)) and round(_result, 2) == 17.80:
            _ok = True
            _msg = "✅ Correct! The total now accounts for every portion in the order."
            _preview = show_result(_result)
        elif isinstance(_result, (int, float)) and round(_result, 2) == 8.90:
            _ok = False
            _msg = "❌ Still charging for one portion — `total()` isn't using `qty` yet."
            _preview = show_result(_result)
        else:
            _ok = False
            _msg = "❌ Not quite — check what `total()` multiplies together."
            _preview = show_result(_result)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
