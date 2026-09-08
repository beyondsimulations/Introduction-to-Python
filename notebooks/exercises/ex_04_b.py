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
    # Quick exercise: the menu update (10 min)

    Winter menu day, first draft. Start from a **copy** of `menu` (never edit
    the original: Tobi still needs it for the archive), call it `menu_exb`,
    then: try `"Pad Thai"` at `9.20` (Tobi's draft price; the lab settles the
    real one), and add the missing `"Miso Ramen"` at `11.50`. Do it all in
    the answer cell below.
    """
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
    menu_exb = None
    return (menu_exb,)


@app.cell(hide_code=True)
def _(menu, menu_exb, mo, show_result):
    # Reactive check. Re-runs automatically whenever the cell above changes.
    _expected = {
        "Falafel Wrap": 6.90,
        "Pad Thai": 9.20,
        "Founders Bowl": 10.40,
        "Miso Ramen": 11.50,
    }
    _original = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    if menu_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif menu_exb == _expected and menu != _original:
        _ok = False
        _msg = "❌ Not quite. `menu_exb` looks right, but the ORIGINAL `menu` changed too. You edited it through an alias; make a real copy with `dict(...)` first, then change the copy."
    elif menu_exb == _expected:
        _ok = True
        _msg = "✅ Correct! Draft saved; the lab settles the final prices."
    elif isinstance(menu_exb, dict) and "Miso Ramen" not in menu_exb:
        _ok = False
        _msg = "❌ Not quite. Miso Ramen never made it in."
    elif isinstance(menu_exb, dict) and menu_exb.get("Pad Thai") == 8.90:
        _ok = False
        _msg = "❌ Not quite. Pad Thai still costs last season's price."
    else:
        _ok = False
        _msg = "❌ Not quite. Check every price and every key against the winter menu."
    mo.callout(mo.md(_msg + show_result(menu_exb)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
