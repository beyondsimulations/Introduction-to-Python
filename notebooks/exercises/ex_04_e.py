# notebooks/exercises/ex_04_e.py
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
    # Quick exercise: happy hour (5–10 min)

    Tobi's idea: 20% off every price on `menu`, for one hour only. Build
    `happy_exe` with a **dict comprehension**: same items, each price cut
    by 20% and rounded to 2 decimals.
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
    menu = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    return (menu,)


@app.cell
def _(menu):
    # YOUR CODE BELOW: replace None
    happy_exe = None
    return (happy_exe,)


@app.cell(hide_code=True)
def _(happy_exe, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = {"Falafel Wrap": 5.52, "Pad Thai": 7.12, "Founders Bowl": 8.32}
    try:
        _matches_rounded = (
            isinstance(happy_exe, dict)
            and set(happy_exe.keys()) == set(_expected.keys())
            and all(
                isinstance(v, (int, float)) and round(v, 2) == _expected[k]
                for k, v in happy_exe.items()
            )
        )
    except Exception:
        _matches_rounded = False

    if happy_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `happy_exe` (a `print` alone doesn't count) and run the cell."
    elif happy_exe == _expected:
        _ok = True
        _msg = "Correct — happy hour is on."
    elif _matches_rounded:
        _ok = False
        _msg = "Wrong — so close. Round each price to 2 decimals."
    else:
        _ok = False
        _msg = "Wrong — check the discount and every key against `menu`."
    mo.callout(mo.md(_msg + show_result(happy_exe)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** Tobi backs down. Happy hour only covers dishes that cost
    **less than 10 EUR** on the regular `menu`; the rest keep their price
    and stay out of the dictionary. Build `cheap_exe` with the same
    comprehension plus an `if` filter after the `for` part.
    """
    )
    return


@app.cell
def _(menu):
    # YOUR CODE BELOW: replace None
    cheap_exe = None
    return (cheap_exe,)


@app.cell(hide_code=True)
def _(cheap_exe, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = {"Falafel Wrap": 5.52, "Pad Thai": 7.12}
    try:
        _matches_rounded = (
            isinstance(cheap_exe, dict)
            and set(cheap_exe.keys()) == set(_expected.keys())
            and all(
                isinstance(v, (int, float)) and round(v, 2) == _expected[k]
                for k, v in cheap_exe.items()
            )
        )
    except Exception:
        _matches_rounded = False

    if cheap_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `cheap_exe` (a `print` alone doesn't count) and run the cell."
    elif cheap_exe == _expected:
        _ok = True
        _msg = "Correct — the Founders Bowl sits this one out."
    elif _matches_rounded:
        _ok = False
        _msg = "Wrong — right dishes, unrounded prices. Round each one to 2 decimals."
    elif isinstance(cheap_exe, dict) and "Founders Bowl" in cheap_exe:
        _ok = False
        _msg = "Wrong — the Founders Bowl costs 10.40 and slipped in. The `if` goes after the `for` part: `... for name, price in menu.items() if price < 10`."
    elif isinstance(cheap_exe, dict) and len(cheap_exe) < 2:
        _ok = False
        _msg = "Wrong — too few dishes survived. Both the Falafel Wrap and the Pad Thai are under 10 EUR; filter on the regular price, not the discounted one."
    else:
        _ok = False
        _msg = "Wrong — expected the two dishes under 10 EUR at 20% off."
    mo.callout(mo.md(_msg + show_result(cheap_exe)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
