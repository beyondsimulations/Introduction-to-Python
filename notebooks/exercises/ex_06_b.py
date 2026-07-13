# notebooks/exercises/ex_06_b.py
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
    # ⚡ Quick exercise: seeded randomness (5 min)

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
    called `demand_exb`.
    """
    )
    return


@app.cell
def _(random):
    # YOUR CODE BELOW — replace None
    demand_exb = None
    return (demand_exb,)


@app.cell(hide_code=True)
def _(demand_exb, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    _expected = [10, 18, 18, 25, 14, 20, 11]
    if demand_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif demand_exb == _expected:
        _ok = True
        _msg = "✅ Correct! Same seven numbers, every single run — the investor can finally trust the demo."
    elif isinstance(demand_exb, list) and len(demand_exb) == 7:
        _ok = False
        _msg = "❌ Right shape, wrong numbers — check three things: seed **21** (not another number), seeded once *before* the loop, and each draw is `random.randint(5, 25)`."
    else:
        _ok = False
        _msg = "❌ Not quite — build a list of 7 draws, one `random.randint(5, 25)` call per day."
    mo.callout(mo.md(_msg + show_result(demand_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Seed first, then draw; the seed makes every following draw predictable.",
            "💡 Hint 2 (the structure)": "random.___(21)\ndemand_exb = []\nfor _day in range(7):\n    demand_exb.append(random.____(5, 25))",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
