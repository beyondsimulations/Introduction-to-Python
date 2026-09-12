# notebooks/exercises/ex_04_c.py
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
    # Quick exercise: the menu update (5-10 min)

    Winter menu day, first draft. Start from a **copy** of `menu` (never edit
    the original: Tobi still needs it for the archive), call it `menu_exc`,
    then: try `"Pad Thai"` at `9.20` (Tobi's draft price; the lab settles the
    real one), and add the missing `"Miso Ramen"` at `11.50`. Do it all in
    the answer cell below.
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
    menu = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    return (menu,)


@app.cell
def _(menu):
    # YOUR CODE BELOW: replace None
    menu_exc = None
    return (menu_exc,)


@app.cell(hide_code=True)
def _(menu, menu_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = {
        "Falafel Wrap": 6.90,
        "Pad Thai": 9.20,
        "Founders Bowl": 10.40,
        "Miso Ramen": 11.50,
    }
    _original = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    if menu_exc is None:
        _ok = False
        _msg = "Not attempted: assign it to `menu_exc` (a `print` alone doesn't count) and run the cell."
    elif menu_exc == _expected and menu != _original:
        _ok = False
        _msg = "Wrong: `menu_exc` looks right, but the ORIGINAL `menu` changed too. You edited it through an alias; make a real copy with `dict(...)` first, then change the copy."
    elif menu_exc == _expected:
        _ok = True
        _msg = "Correct: draft saved; the lab settles the final prices."
    elif isinstance(menu_exc, dict) and "Miso Ramen" not in menu_exc:
        _ok = False
        _msg = "Wrong: Miso Ramen never made it in."
    elif isinstance(menu_exc, dict) and menu_exc.get("Pad Thai") == 8.90:
        _ok = False
        _msg = "Wrong: Pad Thai still costs last season's price."
    else:
        _ok = False
        _msg = "Wrong: check every price and every key against the winter menu."
    mo.callout(mo.md(_msg + show_result(menu_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor asks how many *different* dishes were
    ordered on launch day. The order log is below. Store the number of
    distinct dishes in `distinct_exc`. Hint from the slides: a **set** keeps
    each value once.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    orders = ["Pad Thai", "Miso Ramen", "Pad Thai", "Falafel Wrap", "Pad Thai"]
    return (orders,)


@app.cell
def _(orders):
    # YOUR CODE BELOW: replace None
    distinct_exc = None
    return (distinct_exc,)


@app.cell(hide_code=True)
def _(distinct_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if distinct_exc is None:
        _ok = False
        _msg = "Not attempted: assign it to `distinct_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(distinct_exc, bool):
        _ok = False
        _msg = "Wrong: that's a True/False, not a count. Wrap the set in `len()`."
    elif isinstance(distinct_exc, int) and distinct_exc == 3:
        _ok = True
        _msg = "Correct: five orders, three dishes: `len(set(orders))`."
    elif isinstance(distinct_exc, int) and distinct_exc == 5:
        _ok = False
        _msg = "Wrong: that's the number of orders, not of different dishes. Turn the list into a `set()` first."
    elif isinstance(distinct_exc, (set, list)):
        _ok = False
        _msg = "Wrong: that's the collection itself, not its size. Wrap it in `len()`."
    else:
        _ok = False
        _msg = "Wrong: expected a whole number: `len()` of the set of orders."
    mo.callout(mo.md(_msg + show_result(distinct_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
