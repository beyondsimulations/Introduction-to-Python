# notebooks/exercises/ex_04_c.py
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
    # ⚡ Quick exercise: happy hour (5–10 min)

    Kevin's idea: 20% off every price on `menu`, for one hour only. Build
    `happy_exc` with a **dict comprehension** — same items, each price cut
    by 20% and rounded to 2 decimals.
    """
    )
    return


@app.cell
def _():
    # Given — do not change this
    menu = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    return (menu,)


@app.cell
def _(menu):
    # YOUR CODE BELOW — replace None
    happy_exc = None
    return (happy_exc,)


@app.cell(hide_code=True)
def _(happy_exc, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    _expected = {"Falafel Wrap": 5.52, "Pad Thai": 7.12, "Founders Bowl": 8.32}
    try:
        _matches_rounded = (
            isinstance(happy_exc, dict)
            and set(happy_exc.keys()) == set(_expected.keys())
            and all(
                isinstance(v, (int, float)) and round(v, 2) == _expected[k]
                for k, v in happy_exc.items()
            )
        )
    except Exception:
        _matches_rounded = False

    if happy_exc is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif happy_exc == _expected:
        _ok = True
        _msg = "✅ Correct! Happy hour is on."
    elif _matches_rounded:
        _ok = False
        _msg = "❌ So close — round each price to 2 decimals."
    else:
        _ok = False
        _msg = "❌ Not quite — check the discount and every key against `menu`."
    mo.callout(mo.md(_msg + show_result(happy_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save — this was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
