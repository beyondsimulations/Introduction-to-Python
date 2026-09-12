# notebooks/exercises/ex_01_a.py
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
    # Quick exercise: the company register (5-10 min)

    Tobi filled in the company register in a hurry and typed the name twice.
    First **predict** what `print(company)` shows below, then run the cell.
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
    # Given: Tobi's register entry. Do not change it
    company = "Wrap Speed"
    Company = "Wrapid Delivery"
    print(company)
    return (Company, company)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The registrar wants the name Tobi typed **second**. Store it in
    `company_exa` by using the right variable, not by retyping the text.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    company_exa = None
    return (company_exa,)


@app.cell(hide_code=True)
def _(company_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if company_exa is None:
        _ok = False
        _msg = "Not attempted: assign it to `company_exa` (a `print` alone doesn't count) and run the cell."
    elif company_exa == "Wrapid Delivery":
        _ok = True
        _msg = "Correct: `Company` and `company` are two different names. Capital letters count."
    elif company_exa == "Wrap Speed":
        _ok = False
        _msg = "Wrong: that is the lowercase `company`. Python is case-sensitive: look for the name with a capital C."
    else:
        _ok = False
        _msg = "Wrong: the registrar expects exactly the second name. Use the variable that holds it."
    mo.callout(mo.md(_msg + show_result(company_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the register also wants the sticker budget. Tobi had
    `300` EUR, then spent `50` more on stickers. In the cell below, first set
    `budget_exa = 300`, then on a **second line** update it from its old
    value (`budget_exa = budget_exa - 50`). Predict first: does the check see
    `300` or `250`?
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    budget_exa = None
    return (budget_exa,)


@app.cell(hide_code=True)
def _(budget_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if budget_exa is None:
        _ok = False
        _msg = "Not attempted: assign it to `budget_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(budget_exa, (int, float)) and round(budget_exa, 2) == 250:
        _ok = True
        _msg = "Correct: a name points to its latest value. The second line overwrote the first."
    elif isinstance(budget_exa, (int, float)) and round(budget_exa, 2) == 300:
        _ok = False
        _msg = "Wrong: the check sees the last value the name pointed to. Add the second line that subtracts the 50 EUR."
    else:
        _ok = False
        _msg = "Wrong: expected a number: 300 first, then 50 less on the next line."
    mo.callout(mo.md(_msg + show_result(budget_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
