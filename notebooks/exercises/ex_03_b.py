# notebooks/exercises/ex_03_b.py
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
    # Quick exercise: the wrap price function (5-10 min)

    Every receipt line needs the price of `qty` Falafel Wraps, and Tobi
    keeps retyping `6.90 * qty` by hand, typos and all. Put it in a
    function so he only types it once.

    Write `wrap_price_exb(qty)` that returns the price of `qty` wraps,
    rounded to 2 decimals (each wrap costs 6.90 EUR).
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
    def wrap_price_exb(qty):
        # YOUR CODE BELOW: return the price of qty wraps, rounded to 2 decimals
        return None

    return (wrap_price_exb,)


@app.cell(hide_code=True)
def _(mo, show_result, wrap_price_exb):
    # Reactive check. Re-runs when you run the cell above.
    # Reactive check.
    try:
        _r3 = wrap_price_exb(3)
        _r1 = wrap_price_exb(1)
    except Exception:
        _ok = False
        _msg = "Wrong: Still crashing. Read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if _r3 is None:
            _ok = False
            _msg = "Not attempted: The function still returns None. Use `return`, not `print`, then run the cell."
            _preview = ""
        elif _r3 == 20.70 and _r1 == 6.90:
            _ok = True
            _msg = "Correct: Tobi can stop retyping `6.90 * qty` by hand."
            _preview = show_result(_r3)
        else:
            _ok = False
            _msg = "Wrong: Check the multiplication and the rounding."
            _preview = show_result(_r3)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the platform adds a **service fee** on top, 5 % unless
    a partner deal says otherwise. Write `wrap_bill_exb(qty, rate=0.05)`
    that reuses `wrap_price_exb` and returns the wraps plus the fee,
    rounded to 2 decimals. Calling it with just `qty` must use the 5 %.
    """
    )
    return


@app.cell
def _(wrap_price_exb):
    def wrap_bill_exb(qty, rate=0.05):
        # YOUR CODE BELOW: wrap price plus the fee, rounded to 2 decimals
        return None

    return (wrap_bill_exb,)


@app.cell(hide_code=True)
def _(mo, show_result, wrap_bill_exb, wrap_price_exb):
    # Reactive check. Re-runs when you run the cell above.
    try:
        _base = wrap_price_exb(2)
        _default = wrap_bill_exb(2)
        _deal = wrap_bill_exb(2, 0.10)
    except Exception:
        _ok = False
        _msg = "Wrong: Still crashing. Read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if _base is None:
            _ok = False
            _msg = "Not attempted: Finish `wrap_price_exb` above first; the bill builds on it."
            _preview = ""
        elif _default is None:
            _ok = False
            _msg = "Not attempted: `wrap_bill_exb` still returns None. Use `return`, not `print`, then run the cell."
            _preview = ""
        elif (
            isinstance(_default, (int, float))
            and isinstance(_deal, (int, float))
            and round(_default, 2) == 14.49
            and round(_deal, 2) == 15.18
        ):
            _ok = True
            _msg = "Correct: 13.80 EUR of wraps, 5 % on top by default, 10 % when the deal says so."
            _preview = show_result(_default)
        elif isinstance(_default, (int, float)) and round(_default, 2) == 14.49:
            _ok = False
            _msg = "Wrong: The default works, but the override does not: multiply by `rate`, not by 0.05."
            _preview = show_result(_deal)
        else:
            _ok = False
            _msg = "Wrong: Check the sum: `wrap_price_exb(qty)` plus that price times `rate`, then round."
            _preview = show_result(_default)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
