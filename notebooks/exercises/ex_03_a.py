# notebooks/exercises/ex_03_a.py
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
    # ⚡ Quick exercise: the wrap price function (10 min)

    Every receipt line needs the price of `qty` Falafel Wraps — and Tobi
    keeps retyping `6.90 * qty` by hand, typos and all. Time to make it a
    function he can't get wrong.

    Write `wrap_price_exa(qty)` that returns the price of `qty` wraps,
    rounded to 2 decimals (each wrap costs 6.90 EUR).
    """
    )
    return


@app.cell
def _():
    def wrap_price_exa(qty):
        # YOUR CODE BELOW — return the price of qty wraps, rounded to 2 decimals
        return None

    return (wrap_price_exa,)


@app.cell(hide_code=True)
def _(mo, show_result, wrap_price_exa):
    # Reactive check — re-runs automatically whenever the cell above changes.
    # Wrapped in try/except: a broken function must show a ❌, never crash the check.
    try:
        _r3 = wrap_price_exa(3)
        _r1 = wrap_price_exa(1)
    except Exception:
        _ok = False
        _msg = "❌ Still crashing — read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if _r3 is None:
            _ok = False
            _msg = "🔲 Not attempted yet (the function still returns None)."
            _preview = ""
        elif _r3 == 20.70 and _r1 == 6.90:
            _ok = True
            _msg = "✅ Correct! Tobi can stop retyping `6.90 * qty` by hand."
            _preview = show_result(_r3)
        else:
            _ok = False
            _msg = "❌ Not quite — check the multiplication and the rounding."
            _preview = show_result(_r3)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
