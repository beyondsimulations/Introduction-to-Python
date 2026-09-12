# notebooks/exercises/ex_02_b.py
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
    # Quick exercise: the delivery fee (5-10 min)

    The curfew stands, and on top of it the startup now charges a delivery
    fee that depends on the order size:

    | `order_total` | fee |
    |---|---|
    | `order_total < 15` | 2.90 |
    | `order_total >= 15 and order_total < 30` | 1.50 |
    | `order_total >= 30` | 0 |

    Using an `if`/`elif`/`else` ladder, store the correct fee in `fee_exb`,
    based on `order_total` below.
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
    # Given: do not change this
    order_total = 17.80
    return (order_total,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    fee_exb = None
    return (fee_exb,)


@app.cell(hide_code=True)
def _(fee_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if fee_exb is None:
        _ok = False
        _msg = "Not attempted: assign it to `fee_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(fee_exb, (int, float)) and round(fee_exb, 2) == 1.50:
        _ok = True
        _msg = "Correct: 17.80 EUR lands in the middle tier: 1.50 EUR fee."
    else:
        _ok = False
        _msg = "Wrong: check which branch 17.80 falls into."
    mo.callout(mo.md(_msg + show_result(fee_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** Gold customers never pay a delivery fee, whatever the
    total. Reuse `order_total` and the flag `is_gold` below, and store the
    fee in `fee2_exb`. The ladder still applies to everyone else.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    is_gold = True
    return (is_gold,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    fee2_exb = None
    return (fee2_exb,)


@app.cell(hide_code=True)
def _(fee2_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if fee2_exb is None:
        _ok = False
        _msg = "Not attempted: assign it to `fee2_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(fee2_exb, (int, float)) and round(fee2_exb, 2) == 0:
        _ok = True
        _msg = "Correct: 0 EUR. Gold status beats the ladder, so test `is_gold` first."
    elif isinstance(fee2_exb, (int, float)) and round(fee2_exb, 2) == 1.50:
        _ok = False
        _msg = "Wrong: that is the plain ladder. `is_gold` is `True`, so the fee must be 0 no matter the total."
    else:
        _ok = False
        _msg = "Wrong: check `is_gold` before the ladder: a Gold customer pays 0."
    mo.callout(mo.md(_msg + show_result(fee2_exb)), kind="success" if _ok else "warn")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
