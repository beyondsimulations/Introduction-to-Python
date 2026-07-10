# notebooks/exercises/ex_02_a.py
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
    # ⚡ Quick exercise: the delivery fee (5 min)

    The city allows delivery again — but the startup now charges a delivery
    fee that depends on the order size:

    | `order_total` | fee |
    |---|---|
    | < 15 | 2.90 |
    | 15 – 30 | 1.50 |
    | ≥ 30 | 0 |

    Using an `if`/`elif`/`else` ladder, compute the fee for `order_total`
    below into `fee_exa`.
    """
    )
    return


@app.cell
def _():
    # Given — do not change this
    order_total = 17.80
    return (order_total,)


@app.cell
def _():
    # YOUR CODE BELOW — replace None
    fee_exa = None
    return (fee_exa,)


@app.cell(hide_code=True)
def _(fee_exa, mo, show_result):
    # Reactive check — re-runs automatically whenever the cell above changes.
    if fee_exa is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif isinstance(fee_exa, (int, float)) and round(fee_exa, 2) == 1.50:
        _ok = True
        _msg = "✅ Correct! 17.80 EUR lands in the middle tier — 1.50 EUR fee."
    else:
        _ok = False
        _msg = "❌ Not quite — check which branch 17.80 falls into."
    mo.callout(mo.md(_msg + show_result(fee_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save — this was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
