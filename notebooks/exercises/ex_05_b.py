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
    # Quick exercise: which error? (5–10 min)

    The checkout crashed live during the lunch rush. Tobi swears he only
    changed "one tiny thing". Here's the crashing line:

    ```python
    qty_text = "3.5"
    qty = int(qty_text)
    ```

    First a **trace** (predict, don't run yet): what does `int("3.5")` do?
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
    trace_exb = mo.ui.radio(
        options=["a) 3.5", "b) ValueError", "c) 3", "d) TypeError"],
        label="Your prediction:",
    )
    trace_exb
    return (trace_exb,)


@app.cell(hide_code=True)
def _(mo, trace_exb):
    if trace_exb.value is None:
        _msg = "Pick a prediction above first. Commit before you peek!"
    elif trace_exb.value == "b) ValueError":
        _msg = (
            "Correct: `int()` refuses decimal **strings**, and reading the"
            "last line of the traceback tells you this."
        )
    else:
        _msg = (
            "Wrong — `int()` refuses decimal **strings**, and reading the"
            "last line of the traceback tells you this. (This one is "
            "ungraded. The point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now fix it for real. Given `qty_text` below, write `qty_exb` so the
    quantity arrives as a proper number (not a crash).
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    qty_text = "3.5"
    return (qty_text,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    qty_exb = None
    return (qty_exb,)


@app.cell(hide_code=True)
def _(mo, qty_exb, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if qty_exb is None:
        _ok = False
        _msg = "Not attempted — assign it to `qty_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(qty_exb, float) and qty_exb == 3.5:
        _ok = True
        _msg = "Correct — the quantity now arrives as a proper number."
    else:
        _ok = False
        _msg = "Wrong — `int()` can't read decimals from text. Which converter can?"
    mo.callout(mo.md(_msg + show_result(qty_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the kitchen can't cook half a bowl. Tobi's whole-bowl
    version crashes on the same text:

    ```python
    bowls = int(qty_text)   # ValueError again
    ```

    Starting from `qty_text`, compute `bowls_exb`: the number of **whole**
    bowls as an `int` (drop the half), without a crash. Two converters, one
    after the other.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    bowls_exb = None
    return (bowls_exb,)


@app.cell(hide_code=True)
def _(bowls_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if bowls_exb is None:
        _ok = False
        _msg = "Not attempted — assign it to `bowls_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(bowls_exb, int) and not isinstance(bowls_exb, bool) and bowls_exb == 3:
        _ok = True
        _msg = "Correct — `float()` reads the text, `int()` drops the half: 3 whole bowls."
    elif isinstance(bowls_exb, float) and bowls_exb == 3.5:
        _ok = False
        _msg = "Wrong — 3.5 is still half a bowl. Hand the float to `int()` as a second step."
    else:
        _ok = False
        _msg = "Wrong — expected the whole number of bowls in `\"3.5\"`, as an `int`."
    mo.callout(mo.md(_msg + show_result(bowls_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
