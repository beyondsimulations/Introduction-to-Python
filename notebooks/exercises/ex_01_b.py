# notebooks/exercises/ex_01_b.py
import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Quick exercise: the founding form (5–10 min)

    Tobi filled in the company register form, as Python variables. One line
    has the wrong **value** and two have the wrong **type**. First **predict**
    which, then fix all three.
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
    # YOUR CODE BELOW
    # FIX TOBI'S FORM (some values and/or types are wrong)
    company_type = "UG (haftungsbeschränkt)"
    first_employee = "tobi "
    share_capital = "300"
    founded_year = "2026"
    return (company_type, first_employee, founded_year, share_capital)


@app.cell(hide_code=True)
def _(mo, first_employee, founded_year, share_capital):
    _ok = (
        first_employee == "Tobi"
        and share_capital == 300
        and isinstance(founded_year, int)
    )
    _msg = "Correct — Form accepted!" if _ok else "Wrong — The registrar rejects the form. Keep fixing."
    _msg += "\n\n**Your form:** " + ", ".join(
        f"`{_name} = {_value!r}` ({type(_value).__name__})"
        for _name, _value in [
            ("first_employee", first_employee),
            ("share_capital", share_capital),
            ("founded_year", founded_year),
        ]
    )
    mo.callout(mo.md(_msg), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the registrar's software checks types, not looks. Store
    in `year_type_exb` the type of `founded_year`, using `type()` on the
    variable rather than typing the word. Predict first: `<class 'int'>` or
    `<class 'str'>`?
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    year_type_exb = None
    return (year_type_exb,)


@app.cell(hide_code=True)
def _(mo, year_type_exb):
    # Reactive check. Re-runs when you run the cell above.
    if year_type_exb is None:
        _ok = False
        _msg = "Not attempted — assign it to `year_type_exb` (a `print` alone doesn't count) and run the cell."
    elif year_type_exb is int:
        _ok = True
        _msg = "Correct — `2026` without quotes is an `int`, and `type()` says so."
    elif year_type_exb is str:
        _ok = False
        _msg = "Wrong — your `founded_year` is still text. Fix the form above (drop the quotes); this check re-runs by itself."
    else:
        _ok = False
        _msg = "Wrong — expected the result of `type(founded_year)`, not a word in quotes."
    if year_type_exb is not None:
        _msg += f"\n\n**Your result:** `{year_type_exb!r}`"
    mo.callout(mo.md(_msg), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
