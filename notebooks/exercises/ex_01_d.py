# notebooks/exercises/ex_01_d.py
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
    # Quick exercise: the kitchen board (5-10 min)

    The kitchen wants each order on its board as one short line. Using `qty`
    and `item` below and an **f-string**, build `board_exd` so it reads
    exactly `"3x Pad Thai"`. Predict first: what happens if you forget the
    `f` before the quote?
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
    # Given: do not change these
    item = "Pad Thai"
    qty = 3
    price = 8.50
    return (item, price, qty)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    board_exd = None
    return (board_exd,)


@app.cell(hide_code=True)
def _(board_exd, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if board_exd is None:
        _ok = False
        _msg = "Not attempted: assign it to `board_exd` (a `print` alone doesn't count) and run the cell."
    elif board_exd == "3x Pad Thai":
        _ok = True
        _msg = "Correct: the braces were filled in. The kitchen starts cooking."
    elif isinstance(board_exd, str) and "{" in board_exd:
        _ok = False
        _msg = "Wrong: the braces stayed as text. Without the `f` before the quote, Python keeps `{qty}` literally."
    else:
        _ok = False
        _msg = "Wrong: the board wants exactly `3x Pad Thai`: the number, an `x`, a space, the item."
    mo.callout(mo.md(_msg + show_result(board_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the board should also show what the order is worth.
    Build `kitchen_exd` so it reads exactly `"3x Pad Thai = 25.5 EUR"`, and
    compute the total **inside the braces** from `qty` and `price`, so no
    extra variable is needed.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    kitchen_exd = None
    return (kitchen_exd,)


@app.cell(hide_code=True)
def _(kitchen_exd, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if kitchen_exd is None:
        _ok = False
        _msg = "Not attempted: assign it to `kitchen_exd` (a `print` alone doesn't count) and run the cell."
    elif kitchen_exd == "3x Pad Thai = 25.5 EUR":
        _ok = True
        _msg = "Correct: an f-string can hold a calculation. The receipt printer will want two decimals, though: next slide."
    elif isinstance(kitchen_exd, str) and "{" in kitchen_exd:
        _ok = False
        _msg = "Wrong: the braces stayed as text. Check for the `f` before the quote."
    else:
        _ok = False
        _msg = "Wrong: expected `3x Pad Thai = 25.5 EUR`. Put `qty * price` inside `{ }`."
    mo.callout(mo.md(_msg + show_result(kitchen_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
