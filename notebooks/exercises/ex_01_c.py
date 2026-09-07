# notebooks/exercises/ex_01_c.py
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    # Helper: echoes the student's current answer as a "Your result" preview.
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
    # Quick exercise: the first receipt line (10 min)

    A customer just ordered. Using `qty`, `item`, and `total` below and an
    f-string with `:.2f`, build **one** receipt line that reads exactly
    `"2x Falafel Wrap: 13.80 EUR"`.
    """
    )
    return


@app.cell
def _():
    # Given: do not change these
    item = "Falafel Wrap"
    qty = 2
    total = 13.80
    return (item, qty, total)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    line_exc = None
    return (line_exc,)


@app.cell(hide_code=True)
def _(line_exc, mo, show_result):
    # Reactive check. Re-runs automatically whenever the cell above changes.
    if line_exc is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif line_exc == "2x Falafel Wrap: 13.80 EUR":
        _ok = True
        _msg = "✅ Correct! The receipt printer purrs."
    else:
        _ok = False
        _msg = "❌ Not quite. Check the format `qty x item: total:.2f EUR`."
    mo.callout(mo.md(_msg + show_result(line_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
