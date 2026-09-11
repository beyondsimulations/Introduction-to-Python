# notebooks/exercises/ex_06_c.py
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
    # Quick exercise: seeded randomness (5–10 min)

    Normally `random` hands you a new sequence every time a cell reruns.
    Sometimes you want the opposite: the *same* sequence, every single
    time, so a demo or a test is reproducible. `random.seed(n)` fixes the
    starting point of the sequence. Anyone who seeds with the same number
    sees the same "random" results.

    **Predict** first: will the dice rolls below change when the cell
    reruns? Then run it (twice, if you can).
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
    import random
    return (random,)


@app.cell
def _(random):
    # Worked example (read + run this)
    random.seed(7)
    _rolls_demo = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    print(f"Three dice rolls after seed(7): {_rolls_demo}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The investor wants the demand projection to be *reproducible*: the
    same numbers every time she clicks run, no matter how often the
    notebook re-executes.

    Seed the random generator with `21` (do it exactly once), then
    simulate demand for the next 7 days: for each day, draw an order count
    with `random.randint(5, 25)` and collect the seven draws into a list
    called `demand_exc`.
    """
    )
    return


@app.cell
def _(random):
    # YOUR CODE BELOW: replace None
    demand_exc = None
    return (demand_exc,)


@app.cell(hide_code=True)
def _(demand_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = [10, 18, 18, 25, 14, 20, 11]
    if demand_exc is None:
        _ok = False
        _msg = "Not attempted — assign it to `demand_exc` (a `print` alone doesn't count) and run the cell."
    elif demand_exc == _expected:
        _ok = True
        _msg = "Correct — Same seven numbers, every single run. The investor can finally trust the demo."
    elif isinstance(demand_exc, list) and len(demand_exc) == 7:
        _ok = False
        _msg = "Wrong — Right shape, wrong numbers. Check three things: seed **21** (not another number), seeded once *before* the loop, and each draw is `random.randint(5, 25)`."
    else:
        _ok = False
        _msg = "Wrong — Build a list of 7 draws, one `random.randint(5, 25)` call per day."
    mo.callout(mo.md(_msg + show_result(demand_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Seed first, then draw; the seed makes every following draw predictable.",
            "Hint 2 (the structure)": "random.___(21)\ndemand_exc = []\nfor _day in range(7):\n demand_exc.append(random.____(5, 25))",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** one more roll of the dice. On the busiest day one zone
    gets an extra rider, and the investor wants that pick reproducible too.
    Seed with `21` **again**, then pick one zone from
    `["Nord", "Sued", "West"]` with `random.choice` and store it as `zone_exc`.
    """
    )
    return


@app.cell
def _(random):
    # YOUR CODE BELOW: replace None
    zone_exc = None
    return (zone_exc,)


@app.cell(hide_code=True)
def _(mo, show_result, zone_exc):
    # Reactive check. Re-runs when you run the cell above.
    if zone_exc is None:
        _ok = False
        _msg = "Not attempted — assign it to `zone_exc` (a `print` alone doesn't count) and run the cell."
    elif zone_exc == "Nord":
        _ok = True
        _msg = "Correct — Nord, every single run. Re-seeding rewinds the stream, so the pick is as reproducible as the demand list."
    elif zone_exc in ("Sued", "West"):
        _ok = False
        _msg = "Wrong — a valid zone, but not the one seed 21 deals first. Without a fresh `random.seed(21)` right before the pick, the stream carries on from wherever the demand draws left it."
    else:
        _ok = False
        _msg = "Wrong — `random.choice` takes the list of three zones and hands back one of them, as a string."
    mo.callout(mo.md(_msg + show_result(zone_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "The seed rewinds the stream. Seed first, in the same cell, then make the pick.",
            "Hint 2 (the structure)": "random.____(21)\nzone_exc = random.______([\"Nord\", \"Sued\", \"West\"])",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
