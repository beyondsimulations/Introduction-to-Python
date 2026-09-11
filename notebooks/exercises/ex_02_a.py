# notebooks/exercises/ex_02_a.py
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
    # Quick exercise: is the kitchen open? (5–10 min)

    The city's curfew starts at **22:00**. The kitchen opens at **11:00**.
    An order comes in at `delivery_hour` below.

    Write **one comparison expression** (no `if` yet, that comes next) that is
    `True` when the kitchen is open and `False` otherwise, and store it in
    `open_exa`. Predict the value before you run it.
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
    delivery_hour = 22
    return (delivery_hour,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    open_exa = None
    return (open_exa,)


@app.cell(hide_code=True)
def _(mo, open_exa, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if open_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `open_exa` (a `print` alone doesn't count) and run the cell."
    elif open_exa is False:
        _ok = True
        _msg = "Correct — `False`. 22:00 sharp is already curfew: `<` is strict, and `22 < 22` is not true."
    elif open_exa is True:
        _ok = False
        _msg = "Wrong — at 22:00 sharp the kitchen is closed. Did you write `<=` where the curfew needs `<`?"
    else:
        _ok = False
        _msg = "Wrong — the answer must be a boolean (`True` or `False`): the result of a comparison, not a number."
    mo.callout(mo.md(_msg + show_result(open_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the lawyer found a loophole: pharmacy runs are allowed at
    any hour. Reuse `delivery_hour` and the flag `is_pharmacy` below, and store
    in `allowed_exa` whether this run may go out: open hours, **or** a pharmacy
    run.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    is_pharmacy = True
    return (is_pharmacy,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    allowed_exa = None
    return (allowed_exa,)


@app.cell(hide_code=True)
def _(allowed_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if allowed_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `allowed_exa` (a `print` alone doesn't count) and run the cell."
    elif allowed_exa is True:
        _ok = True
        _msg = "Correct — `True`. The kitchen is closed, but `or` needs only one side: the pharmacy flag carries it."
    elif allowed_exa is False:
        _ok = False
        _msg = "Wrong — a pharmacy run at 22:00 is allowed. `and` needs both sides; `or` is happy with one."
    else:
        _ok = False
        _msg = "Wrong — the answer must be a boolean (`True` or `False`), built with `or`."
    mo.callout(mo.md(_msg + show_result(allowed_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
