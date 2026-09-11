# notebooks/exercises/ex_02_c.py
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
    # Quick exercise: loop the minutes (5–10 min)

    First a **trace** (predict, don't run yet): what does this print?

    ```python
    total = 0
    for p in [3, 5]:
        total = total + p
    print(total)
    ```
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
    trace_exc = mo.ui.radio(
        options=["a) 3", "b) 3 then 8", "c) 8"],
        label="Your prediction:",
    )
    trace_exc
    return (trace_exc,)


@app.cell(hide_code=True)
def _(mo, trace_exc):
    if trace_exc.value is None:
        _msg = "Pick a prediction above first. Commit before you peek!"
    elif trace_exc.value == "c) 8":
        _msg = (
            "Correct — the `print` line runs once, **after** the loop"
            "finishes, so it prints the final total, `8`. If `print` were "
            "indented into the loop, it would print `3` then `8`."
        )
    else:
        _msg = (
            "Wrong — `print` is **not** indented, so it only runs once,"
            "after the loop finishes: it prints the final total, `8`. (This "
            "one is ungraded. The point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now write one yourself: the curfew means every delivery minute counts.
    Sum today's three runs in `minutes` with a `for` loop into `minutes_exc`.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    minutes = [12, 7, 9]
    return (minutes,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    minutes_exc = None
    return (minutes_exc,)


@app.cell(hide_code=True)
def _(minutes_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if minutes_exc is None:
        _ok = False
        _msg = "Not attempted — assign it to `minutes_exc` (a `print` alone doesn't count) and run the cell."
    elif minutes_exc == 28:
        _ok = True
        _msg = "Correct — 12 + 7 + 9 = 28 minutes, all delivered on time."
    else:
        _ok = False
        _msg = "Wrong — make sure you add up every value in `minutes` rather than keeping only the last one."
    mo.callout(mo.md(_msg + show_result(minutes_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the courier's target is 8 minutes per run. Loop over
    `minutes` again and **count** the runs that took longer than 8, into
    `late_exc`. Same accumulator idea, but add 1 instead of the value.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    late_exc = None
    return (late_exc,)


@app.cell(hide_code=True)
def _(late_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if late_exc is None:
        _ok = False
        _msg = "Not attempted — assign it to `late_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(late_exc, (int, float)) and round(late_exc, 2) == 2:
        _ok = True
        _msg = "Correct — 2 late runs (12 and 9 minutes). The 7-minute run was fine."
    else:
        _ok = False
        _msg = "Wrong — start a counter at 0 and add 1 only when the run is **longer than** 8 (strictly)."
    mo.callout(mo.md(_msg + show_result(late_exc)), kind="success" if _ok else "warn")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
