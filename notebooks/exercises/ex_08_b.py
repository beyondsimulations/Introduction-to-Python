# notebooks/exercises/ex_08_b.py
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
    # Quick exercise: filter + count (pandas) (10 min)

    Filtering a DataFrame with a boolean mask works exactly like NumPy:
    `df[df["col"] >= value]` keeps only the matching rows. Same mask
    idea as NumPy, pandas speaks it too.

    **Predict** first: what does the cell below print, then run it.
    """
    )
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # Worked example (read + run this)
    _demo = pd.DataFrame({"size": [1, 4, 2], "price": [3.0, 9.0, 5.0]})
    print(_demo[_demo["size"] >= 2])
    print(_demo[_demo["size"] >= 2]["price"].sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `orders_exb` below is tonight's order list. A "bulk" order is **2
    items or more**. The investor wants two numbers: how many orders
    were bulk, and how much revenue those bulk orders brought in.

    Compute `bulk_count_exb` (how many orders were bulk) and
    `bulk_revenue_exb` (the total `total_eur` of just the bulk ones).
    """
    )
    return


@app.cell
def _(pd):
    # Given — do not change this
    orders_exb = pd.DataFrame(
        {
            "zone": ["Nord", "Sued", "Hafen", "Altstadt", "Nord", "Sued"],
            "items": [1, 2, 1, 3, 1, 2],
            "total_eur": [11.20, 18.40, 6.80, 24.00, 9.50, 14.60],
        }
    )
    return (orders_exb,)


@app.cell
def _(orders_exb):
    # YOUR CODE BELOW — replace None
    bulk_count_exb = None
    return (bulk_count_exb,)


@app.cell
def _(orders_exb):
    # YOUR CODE BELOW — replace None
    bulk_revenue_exb = None
    return (bulk_revenue_exb,)


@app.cell(hide_code=True)
def _(bulk_count_exb, bulk_revenue_exb, mo, pd, show_result):
    # Reactive check — re-runs automatically whenever the cells above change.
    _expected_count = 3
    _expected_revenue = 57.0
    _result = None
    if bulk_count_exb is None or bulk_revenue_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    elif isinstance(bulk_count_exb, (pd.Series, pd.DataFrame)) or isinstance(
        bulk_revenue_exb, (pd.Series, pd.DataFrame)
    ):
        _ok = False
        _result = f"bulk_count_exb={bulk_count_exb!r}, bulk_revenue_exb={bulk_revenue_exb!r}"
        _msg = "❌ One of these is still a whole column/table — `.sum()` needs to run on the mask (for the count) or on the filtered price column (for the revenue)."
    else:
        # Coerce to plain scalars first — anything that can't be must
        # degrade to a message, never crash the check.
        try:
            _count = int(bulk_count_exb)
            _revenue = round(float(bulk_revenue_exb), 2)
        except (TypeError, ValueError):
            _ok = False
            _count = None
            _revenue = None
            _msg = "❌ These should be a whole number and a euro amount — check what your expressions actually return."
        else:
            _result = f"bulk_count_exb={bulk_count_exb}, bulk_revenue_exb={bulk_revenue_exb}"
            if _count == _expected_count and _revenue == _expected_revenue:
                _ok = True
                _msg = "✅ Correct! Three bulk orders worth 57.00 EUR."
            elif _count == 1 and _revenue == 24.0:
                _ok = False
                _msg = "❌ Bulk starts AT two items — which comparison includes the boundary, `>` or `>=`?"
            elif _revenue == 84.5:
                _ok = False
                _msg = "❌ That's the revenue of every order — filter to bulk orders before summing."
            elif _count == _expected_count:
                _ok = False
                _msg = "❌ The count is right, but the revenue isn't — filter `orders_exb` with the same mask before summing `total_eur`."
            else:
                _ok = False
                _msg = '❌ Not quite — start with the mask: `orders_exb["items"] >= 2`.'
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'Same mask idea as NumPy — build it first (`orders_exb["items"] >= 2`); `.sum()` on the mask counts the `True`s, and indexing with that same mask before `.sum()` on `total_eur` gives the revenue.',
            "💡 Hint 2 (the structure)": '_bulk = orders_exb[orders_exb["items"] >= ___]\nbulk_count_exb = int((orders_exb["items"] >= ___).sum())\nbulk_revenue_exb = float(_bulk["total_eur"].___())',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
