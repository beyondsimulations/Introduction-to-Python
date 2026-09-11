# notebooks/exercises/ex_04_b.py
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
    # Quick exercise: the order queue (5–10 min)

    The kitchen keeps today's orders in a queue:

    ```python
    queue = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]
    ```

    First a **trace** (predict, don't run yet): what is `queue[-1]`?
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
    queue = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]
    return (queue,)


@app.cell(hide_code=True)
def _(mo):
    trace_exb = mo.ui.radio(
        options=["a) \"Miso Ramen\"", "b) \"Pad Thai\"", "c) Error"],
        label="Your prediction:",
    )
    trace_exb
    return (trace_exb,)


@app.cell(hide_code=True)
def _(mo, trace_exb):
    if trace_exb.value is None:
        _msg = "Pick a prediction above first. Commit before you peek!"
    elif trace_exb.value == "a) \"Miso Ramen\"":
        _msg = (
            "Correct — a negative index counts from the end, so `-1` is"
            "the last item, `\"Miso Ramen\"`."
        )
    else:
        _msg = (
            "Wrong — a negative index counts from the end, so `-1` is"
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
    `last_two_exb`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    last_two_exb = None
    return (last_two_exb,)


@app.cell(hide_code=True)
def _(last_two_exb, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if last_two_exb is None:
        _ok = False
        _msg = "Not attempted — assign it to `last_two_exb` (a `print` alone doesn't count) and run the cell."
    elif last_two_exb == ["Pizza Calzone", "Miso Ramen"]:
        _ok = True
        _msg = "Correct — those two orders go out next."
    else:
        _ok = False
        _msg = "Wrong — try a slice from -2 to the end."
    mo.callout(mo.md(_msg + show_result(last_two_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the queue moves. The first order goes out to the courier
    and a new one, `"Green Curry"`, joins at the end. Build the new queue in
    `queue_exb` with a slice and `+`, so the original `queue` stays untouched
    (Tobi's version used `.append()` on `queue` and lost the archive).
    """
    )
    return


@app.cell
def _(queue):
    # YOUR CODE BELOW: replace None
    queue_exb = None
    return (queue_exb,)


@app.cell(hide_code=True)
def _(mo, queue, queue_exb, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = ["Founders Bowl", "Pizza Calzone", "Miso Ramen", "Green Curry"]
    _original = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]
    if queue_exb is None:
        _ok = False
        _msg = "Not attempted — assign it to `queue_exb` (a `print` alone doesn't count) and run the cell."
    elif queue != _original:
        _ok = False
        _msg = "Wrong — the ORIGINAL `queue` changed too. `.append()` edits in place; build a new list with `queue[1:] + [...]` instead."
    elif queue_exb == _expected:
        _ok = True
        _msg = "Correct — `queue[1:] + [\"Green Curry\"]`: a fresh list, the original untouched."
    elif queue_exb == ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen", "Green Curry"]:
        _ok = False
        _msg = "Wrong — the Pad Thai is still in front. Slice from index 1 to drop the first order."
    elif isinstance(queue_exb, list) and "Green Curry" not in queue_exb:
        _ok = False
        _msg = "Wrong — the Green Curry never joined. Add `+ [\"Green Curry\"]` at the end."
    else:
        _ok = False
        _msg = "Wrong — expected the three remaining orders followed by the Green Curry."
    mo.callout(mo.md(_msg + show_result(queue_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
