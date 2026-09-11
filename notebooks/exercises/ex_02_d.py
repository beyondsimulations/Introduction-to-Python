# notebooks/exercises/ex_02_d.py
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
    # Quick exercise: the courier's battery (5–10 min)

    The courier's phone starts the curfew shift at **100 %** and loses
    **18 %** per delivery. Deliveries continue **as long as** the battery is at
    least 20 %; below that the app refuses to send the next one.

    With a `while` loop, count how many deliveries the courier makes and store
    the count in `runs_exd`. Predict the number first. Start from
    `battery` below, and use a cell-private name like `_battery` for the
    shrinking copy so the given value stays untouched.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Saving your work:** this notebook runs in your browser. Press"
            "**Cmd/Ctrl+S** to save, and always save **before** menu → Download → "
            "*Download Python code*. Without a save first, the download is an empty file."
        ),
        kind="info",
    )
    return


@app.cell
def _():
    # Given: do not change this
    battery = 100
    return (battery,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    runs_exd = None
    return (runs_exd,)


@app.cell(hide_code=True)
def _(mo, runs_exd, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if runs_exd is None:
        _ok = False
        _msg = "Not attempted — assign it to `runs_exd` (a `print` alone doesn't count) and run the cell."
    elif isinstance(runs_exd, (int, float)) and round(runs_exd, 2) == 5:
        _ok = True
        _msg = "Correct — 5 deliveries: 100, 82, 64, 46, 28, then 10, and the loop stops. The battery shrinks every pass, so it always ends."
    elif isinstance(runs_exd, (int, float)) and round(runs_exd, 2) == 4:
        _ok = False
        _msg = "Wrong — one short. At 28 % the courier is still allowed out (28 is at least 20); the fifth run brings it to 10."
    else:
        _ok = False
        _msg = "Wrong — loop while the battery is **at least** 20, subtract 18 and add one run per pass."
    mo.callout(mo.md(_msg + show_result(runs_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** back at the kitchen, the phone goes on the charger at
    **10 %** and gains **7 %** per minute. Tobi wrote a `while True` loop that
    stops with `break` the moment the battery reaches 50 % or more, and says
    it takes **1 minute**:

    ```python
    level = 10
    minutes = 0
    while True:
        if level >= 50:
            break
        level = level + 7
    minutes = minutes + 1
    ```

    Find Tobi's bug, write the fixed loop yourself, and store the real number
    of minutes in `charge_exd`. Keep the `while True` plus `break` shape.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    charge_exd = None
    return (charge_exd,)


@app.cell(hide_code=True)
def _(charge_exd, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if charge_exd is None:
        _ok = False
        _msg = "Not attempted — assign it to `charge_exd` (a `print` alone doesn't count) and run the cell."
    elif isinstance(charge_exd, (int, float)) and round(charge_exd, 2) == 6:
        _ok = True
        _msg = "Correct — 6 minutes: 10, 17, 24, 31, 38, 45, 52. Tobi's counter sat **outside** the loop, so it ran once, after the `break`."
    elif isinstance(charge_exd, (int, float)) and round(charge_exd, 2) == 1:
        _ok = False
        _msg = "Wrong — that is Tobi's answer. Look at the indentation of `minutes = minutes + 1`: is it inside the loop?"
    else:
        _ok = False
        _msg = "Wrong — add one minute on every pass through the loop, and `break` as soon as the level is 50 or more."
    mo.callout(mo.md(_msg + show_result(charge_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
