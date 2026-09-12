# notebooks/exercises/ex_03_c.py
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
    # Quick exercise: fix the Order class (5-10 min)

    Tobi wrote the startup's first class, an `Order` that's supposed to
    compute its own total. Except a 2× Pad Thai order charges like a single
    portion. Find the bug in `total()` and fix it.
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
    # YOUR CODE BELOW
    class Order:
        def __init__(self, item, qty, price):
            self.item = item
            self.qty = qty
            self.price = price

        def total(self):
            # TOBI'S BUG: the order total ignores something
            return self.price

    return (Order,)


@app.cell(hide_code=True)
def _(Order, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    # Reactive check.
    try:
        _result = Order("Pad Thai", 2, 8.90).total()
    except Exception:
        _ok = False
        _msg = "Wrong: Still crashing. Read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if isinstance(_result, (int, float)) and round(_result, 2) == 17.80:
            _ok = True
            _msg = "Correct: The total now accounts for every portion in the order."
            _preview = show_result(_result)
        elif isinstance(_result, (int, float)) and round(_result, 2) == 8.90:
            _ok = False
            _msg = "Wrong: Still charging for one portion: `total()` isn't using `qty` yet."
            _preview = show_result(_result)
        else:
            _ok = False
            _msg = "Wrong: Check what `total()` multiplies together."
            _preview = show_result(_result)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** two orders come in at once and Tobi wants to cook the
    cheaper one first. Write `cheaper_exc(first, second)` that takes two
    `Order` objects and returns the **item name** of the one with the
    lower `total()`.
    """
    )
    return


@app.cell
def _():
    def cheaper_exc(first, second):
        # YOUR CODE BELOW: compare the two totals, return the cheaper item name
        return None

    return (cheaper_exc,)


@app.cell(hide_code=True)
def _(Order, cheaper_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    try:
        _pad = Order("Pad Thai", 2, 8.90)
        _fries = Order("Fries", 3, 3.20)
        _one = cheaper_exc(_pad, _fries)
        _two = cheaper_exc(_fries, _pad)
    except Exception:
        _ok = False
        _msg = "Wrong: Still crashing. Read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if _one is None:
            _ok = False
            _msg = "Not attempted: `cheaper_exc` still returns None. Use `return`, not `print`, then run the cell."
            _preview = ""
        elif _one == "Fries" and _two == "Fries":
            _ok = True
            _msg = "Correct: 9.60 EUR of fries beats 17.80 EUR of Pad Thai, whichever order comes first."
            _preview = show_result(_one)
        elif isinstance(_one, Order):
            _ok = False
            _msg = "Wrong: That is the whole `Order` object. Return its `.item`, the name."
            _preview = ""
        elif _one == "Fries":
            _ok = False
            _msg = "Wrong: Swapped arguments give a different answer: compare the two `.total()` values, do not assume the first is cheaper."
            _preview = show_result(_two)
        else:
            _ok = False
            _msg = "Wrong: Compare `first.total()` with `second.total()` and return the item of the smaller one."
            _preview = show_result(_one)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
