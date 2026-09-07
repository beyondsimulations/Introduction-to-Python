# notebooks/exercises/ex_02_b.py
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
    # Quick exercise: loop the minutes (10 min)

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
    trace_exb = mo.ui.radio(
        options=["a) 3", "b) 3 then 8", "c) 8"],
        label="Your prediction:",
    )
    trace_exb
    return (trace_exb,)


@app.cell(hide_code=True)
def _(mo, trace_exb):
    if trace_exb.value is None:
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_exb.value == "c) 8":
        _msg = (
            "✅ Correct: the `print` line runs once, **after** the loop "
            "finishes, so it prints the final total — `8`. If `print` were "
            "indented into the loop, it would print `3` then `8`."
        )
    else:
        _msg = (
            "❌ Not quite. `print` is **not** indented, so it only runs once, "
            "after the loop finishes: it prints the final total, `8`. (This "
            "one is ungraded — the point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now write one yourself: the curfew means every delivery minute counts.
    Sum today's three runs in `minutes` with a `for` loop into `minutes_exb`.
    """
    )
    return


@app.cell
def _():
    # Given — do not change this
    minutes = [12, 7, 9]
    return (minutes,)


@app.cell
def _():
    # YOUR CODE BELOW — replace None
    minutes_exb = None
    return (minutes_exb,)


@app.cell(hide_code=True)
def _(minutes_exb, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    if minutes_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif minutes_exb == 28:
        _ok = True
        _msg = "✅ Correct! 12 + 7 + 9 = 28 minutes, all delivered on time."
    else:
        _ok = False
        _msg = "❌ Not quite — make sure you add every value in `minutes`, not just the last one."
    mo.callout(mo.md(_msg + show_result(minutes_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
