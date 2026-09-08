# notebooks/exercises/ex_01_a.py
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
    # Quick exercise: the founding form (10 min)

    Tobi filled in the company register form, as Python variables. One line
    has the wrong **value** and two have the wrong **type**. First **predict**
    which, then fix all three.
    """
    )
    return


@app.cell
def _():
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
    _msg = "✅ Form accepted!" if _ok else "❌ The registrar rejects the form. Keep fixing."
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
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
