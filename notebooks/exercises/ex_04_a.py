# notebooks/exercises/ex_04_a.py
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
    # Quick exercise: the order queue (10 min)

    The kitchen keeps today's orders in a queue:

    ```python
    queue = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]
    ```

    First a **trace** (predict, don't run yet): what is `queue[-1]`?
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    queue = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]
    return (queue,)


@app.cell(hide_code=True)
def _(mo):
    trace_exa = mo.ui.radio(
        options=["a) \"Miso Ramen\"", "b) \"Pad Thai\"", "c) Error"],
        label="Your prediction:",
    )
    trace_exa
    return (trace_exa,)


@app.cell(hide_code=True)
def _(mo, trace_exa):
    if trace_exa.value is None:
        _msg = "🔲 Pick a prediction above first. Commit before you peek!"
    elif trace_exa.value == "a) \"Miso Ramen\"":
        _msg = (
            "✅ Correct: a negative index counts from the end, so `-1` is "
            "the last item, `\"Miso Ramen\"`."
        )
    else:
        _msg = (
            "❌ Not quite. A negative index counts from the end, so `-1` is "
            "the last item, `\"Miso Ramen\"`. (This one is ungraded. The "
            "point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now write a slice: capture the last two orders in `queue` into
    `last_two_exa`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    last_two_exa = None
    return (last_two_exa,)


@app.cell(hide_code=True)
def _(last_two_exa, mo, show_result):
    # Reactive check. Re-runs automatically whenever the cell above changes.
    if last_two_exa is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif last_two_exa == ["Pizza Calzone", "Miso Ramen"]:
        _ok = True
        _msg = "✅ Correct! Those two orders go out next."
    else:
        _ok = False
        _msg = "❌ Not quite. Try a slice from -2 to the end."
    mo.callout(mo.md(_msg + show_result(last_two_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
