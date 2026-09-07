# notebooks/exercises/ex_01_b.py
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
    # Quick exercise: the sticker budget (10 min)

    Tobi has 300 EUR left and wants to know how much survives after buying
    12 boxes at 25 EUR each. **Predict the result of `300 - 12 * 25` before
    you run the cell below**. Does multiplication happen before or after
    subtraction?
    """
    )
    return


@app.cell
def _():
    # Run this after you've predicted. No editing needed.
    print(300 - 12 * 25)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Multiplication always happens before subtraction, so Tobi's 12 boxes
    (`12 * 25 = 300`) wipe out the whole budget.

    Now the real task: sticker **packs** cost `12.25` EUR each. Using `//`
    (floor division) and `%` (remainder), figure out how many packs fit in
    the 300 EUR budget and how much change is left over.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    packs_exb = None
    change_exb = None
    return (change_exb, packs_exb)


@app.cell(hide_code=True)
def _(change_exb, mo, packs_exb):
    # Reactive check. Re-runs automatically whenever the cell above changes.
    if packs_exb is None or change_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif packs_exb == 24 and round(change_exb, 2) == 6.0:
        _ok = True
        _msg = "✅ Correct! 24 packs, 6.00 EUR change. Tobi is already spending it."
    else:
        _ok = False
        _msg = "❌ Not quite. Check that you used `//` for packs and `%` for change."
    mo.callout(mo.md(_msg), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
