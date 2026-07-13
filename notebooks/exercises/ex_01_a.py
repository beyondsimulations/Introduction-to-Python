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
    # ⚡ Quick exercise: the founding form (5 min)

    Kevin filled in the company register form, as Python variables. One line
    has the wrong **value** and two have the wrong **type**. First **predict**
    which, then fix all three.
    """
    )
    return


@app.cell
def _():
    # FIX KEVIN'S FORM (some values and/or types are wrong)
    company_type = "UG (haftungsbeschränkt)"
    first_employee = "kevin "
    share_capital = "300"
    founded_year = "2026"
    return (company_type, first_employee, founded_year, share_capital)


@app.cell(hide_code=True)
def _(mo, first_employee, founded_year, share_capital):
    _ok = (
        first_employee == "Kevin"
        and share_capital == 300
        and isinstance(founded_year, int)
    )
    mo.callout(
        mo.md("✅ Form accepted!" if _ok else "❌ The registrar rejects the form — keep fixing."),
        kind="success" if _ok else "warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
