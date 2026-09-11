# notebooks/exercises/ex_08_c.py
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
    # Quick exercise: filter + count (pandas) (5–10 min)

    Filtering a DataFrame with a boolean mask works exactly like NumPy:
    `df[df["col"] >= value]` keeps only the matching rows. Same mask
    idea as NumPy, pandas speaks it too.

    **Predict** first: what does the cell below print, then run it.
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
    `orders_exc` below is tonight's order list. A "bulk" order is **2
    items or more**. The investor wants two numbers: how many orders
    were bulk, and how much revenue those bulk orders brought in.

    Compute `bulk_count_exc` (how many orders were bulk) and
    `bulk_revenue_exc` (the total `total_eur` of just the bulk ones).
    """
    )
    return


@app.cell
def _(pd):
    # Given: do not change this
    orders_exc = pd.DataFrame(
        {
            "zone": ["Nord", "Sued", "Hafen", "Altstadt", "Nord", "Sued"],
            "items": [1, 2, 1, 3, 1, 2],
            "total_eur": [11.20, 18.40, 6.80, 24.00, 9.50, 14.60],
        }
    )
    return (orders_exc,)


@app.cell
def _(orders_exc):
    # YOUR CODE BELOW: replace None
    bulk_count_exc = None
    return (bulk_count_exc,)


@app.cell
def _(orders_exc):
    # YOUR CODE BELOW: replace None
    bulk_revenue_exc = None
    return (bulk_revenue_exc,)


@app.cell(hide_code=True)
def _(bulk_count_exc, bulk_revenue_exc, mo, pd, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected_count = 3
    _expected_revenue = 57.0
    _result = None
    if bulk_count_exc is None or bulk_revenue_exc is None:
        _ok = False
        _msg = "Not attempted — Assign it to `bulk_count_exc` and `bulk_revenue_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(bulk_count_exc, (pd.Series, pd.DataFrame)) or isinstance(
        bulk_revenue_exc, (pd.Series, pd.DataFrame)
    ):
        _ok = False
        _result = f"bulk_count_exc={bulk_count_exc!r}, bulk_revenue_exc={bulk_revenue_exc!r}"
        _msg = "Wrong — One of these is still a whole column/table. `.sum()` needs to run on the mask (for the count) or on the filtered price column (for the revenue)."
    else:
        try:
            _count = int(bulk_count_exc)
            _revenue = round(float(bulk_revenue_exc), 2)
        except (TypeError, ValueError):
            _ok = False
            _count = None
            _revenue = None
            _msg = "Wrong — These should be a whole number and a euro amount. Check what your expressions actually return."
        else:
            _result = f"bulk_count_exc={bulk_count_exc}, bulk_revenue_exc={bulk_revenue_exc}"
            if _count == _expected_count and _revenue == _expected_revenue:
                _ok = True
                _msg = "Correct — Three bulk orders worth 57.00 EUR."
            elif _count == 1 and _revenue == 24.0:
                _ok = False
                _msg = "Wrong — Bulk starts AT two items. Which comparison includes the boundary, `>` or `>=`?"
            elif _revenue == 84.5:
                _ok = False
                _msg = "Wrong — That's the revenue of every order. Filter to bulk orders before summing."
            elif _count == _expected_count:
                _ok = False
                _msg = "Wrong — The count is right, but the revenue isn't. Filter `orders_exc` with the same mask before summing `total_eur`."
            else:
                _ok = False
                _msg = 'Not quite. Start with the mask: `orders_exc["items"] >= 2`.'
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": 'Same mask idea as NumPy: build it first (`orders_exc["items"] >= 2`); `.sum()` on the mask counts the `True`s, and indexing with that same mask before `.sum()` on `total_eur` gives the revenue.',
            "Hint 2 (the structure)": '_bulk = orders_exc[orders_exc["items"] >= ___]\nbulk_count_exc = int((orders_exc["items"] >= ___).sum())\nbulk_revenue_exc = float(_bulk["total_eur"].___())',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor wants to know whether bulk orders are also
    the *lucrative* ones. Add a column `per_item` (`total_eur` divided by
    `items`) on a **copy** of `orders_exc`, then compute `best_per_item_exc`:
    the highest `per_item` among the **bulk** orders. One number.
    """
    )
    return


@app.cell
def _(orders_exc):
    best_per_item_exc = None  # YOUR CODE BELOW
    return (best_per_item_exc,)


@app.cell(hide_code=True)
def _(best_per_item_exc, mo, pd, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 9.2
    _result = None
    if best_per_item_exc is None:
        _ok = False
        _msg = "Not attempted — Assign the number to `best_per_item_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(best_per_item_exc, (pd.Series, pd.DataFrame)):
        _ok = False
        _result = f"best_per_item_exc={best_per_item_exc!r}"
        _msg = "Wrong — `best_per_item_exc` is still a column/table: `.max()` collapses the filtered `per_item` column to one number."
    else:
        try:
            _v = round(float(best_per_item_exc), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong — That's not a number. Check what your last expression returns."
        else:
            _result = f"best_per_item_exc={best_per_item_exc}"
            if pd.isna(_v):
                _ok = False
                _msg = "Wrong — Your filter came back empty, so `.max()` is NaN. Check the column name and the `>= 2` rule."
            elif _v == _expected:
                _ok = True
                _msg = "Correct — 9.20 EUR per item, the Sued order with two items. Bulk and lucrative are not the same thing."
            elif _v == 11.2:
                _ok = False
                _msg = "Wrong — That's a single-item order. Filter to bulk (`items >= 2`) before taking the max."
            elif _v == 24.0:
                _ok = False
                _msg = "Wrong — That's the biggest `total_eur`, not the biggest per item. Divide by `items` first."
            elif _v == 8.0:
                _ok = False
                _msg = "Wrong — Bulk starts AT two items: `>=`, not `>`."
            else:
                _ok = False
                _msg = "Wrong — Copy, add `per_item`, filter to `items >= 2`, then `.max()` on the new column."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Three moves from the slides: `.copy()`, a new column from two others, then the same bulk mask as the core task. `.max()` on the filtered new column gives the one number.",
            "Hint 2 (the structure)": '_work = orders_exc.copy()\n_work["per_item"] = _work["total_eur"] / _work["___"]\n_bulk = _work[_work["items"] >= ___]\nbest_per_item_exc = float(_bulk["per_item"].___())',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
