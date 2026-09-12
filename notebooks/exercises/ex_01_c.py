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
    # Quick exercise: the sticker budget (5-10 min)

    Tobi has 300 EUR left and wants to know how much survives after buying
    12 boxes at 25 EUR each. **Predict the result of `300 - 12 * 25` before
    you run the cell below**. Does multiplication happen before or after
    subtraction?
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


@app.cell(hide_code=True)
def _(mo):
    run_predict = mo.ui.run_button(label="I've predicted, run it")
    run_predict
    return (run_predict,)


@app.cell
def _(run_predict):
    # Runs only after the button above. No editing needed.
    result = None
    if run_predict.value:
        result = 300 - 12 * 25
        print(result)
    return (result,)


@app.cell(hide_code=True)
def _(mo, result, run_predict):
    mo.md(
        f"`300 - 12 * 25` gives **{result}**. Multiplication always happens before "
        "subtraction, so Tobi's 12 boxes (`12 * 25 = 300`) wipe out the whole budget."
        if run_predict.value
        else "*Predict, then press the button.*"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now the real task: sticker **packs** cost `12.25` EUR each. Using `//`
    (floor division) and `%` (remainder), figure out how many packs fit in
    the 300 EUR budget and how much change is left over.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    packs_exc = None
    change_exc = None
    return (change_exc, packs_exc)


@app.cell(hide_code=True)
def _(change_exc, mo, packs_exc):
    # Reactive check. Re-runs when you run the cell above.
    if packs_exc is None or change_exc is None:
        _ok = False
        _msg = "Not attempted: assign it to `packs_exc` and `change_exc` (a `print` alone doesn't count) and run the cell."
    elif packs_exc == 24 and round(change_exc, 2) == 6.0:
        _ok = True
        _msg = "Correct: 24 packs, 6.00 EUR change. Tobi is already spending it."
    else:
        _ok = False
        _msg = "Wrong: check that you used `//` for packs and `%` for change."
    if packs_exc is not None or change_exc is not None:
        _msg += f"\n\n**Your result:** `packs_exc = {packs_exc}`, `change_exc = {change_exc}`"
    mo.callout(mo.md(_msg), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** a pack holds 40 stickers, so Tobi divides `12.25 / 40`
    and proudly reports `0.30625` EUR per sticker. Prices have two decimals.
    Store the price per sticker in `per_sticker_exc`, rounded to cents.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    per_sticker_exc = None
    return (per_sticker_exc,)


@app.cell(hide_code=True)
def _(mo, per_sticker_exc):
    # Reactive check. Re-runs when you run the cell above.
    if per_sticker_exc is None:
        _ok = False
        _msg = "Not attempted: assign it to `per_sticker_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(per_sticker_exc, (int, float)) and per_sticker_exc == 0.31:
        _ok = True
        _msg = "Correct: 0.31 EUR per sticker. `round(value, 2)` turns a long tail into a price."
    elif isinstance(per_sticker_exc, (int, float)) and round(per_sticker_exc, 2) == 0.31:
        _ok = False
        _msg = "Wrong: the amount is right, but `0.30625` has too many decimals for a price. Wrap the division in `round(..., 2)`."
    else:
        _ok = False
        _msg = "Wrong: expected `12.25 / 40` rounded to two decimals."
    if per_sticker_exc is not None:
        _msg += f"\n\n**Your result:** `per_sticker_exc = {per_sticker_exc}`"
    mo.callout(mo.md(_msg), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
