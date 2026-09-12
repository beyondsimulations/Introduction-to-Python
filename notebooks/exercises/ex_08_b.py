# notebooks/exercises/ex_08_b.py
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
    # Quick exercise: one column, some rows, one number (5-10 min)

    The investor's questions all have the same shape: pick a column,
    keep some rows, collapse to one number. `df["col"]` selects a
    column, `df[df["col"] == value]` keeps the matching rows, and `.sum()`
    or `.mean()` turns what is left into a single number.

    **Predict** first: what does the cell below print, then run it.
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
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # Worked example (read + run this)
    _demo = pd.DataFrame({"team": ["Ost", "West", "Ost"], "score": [10, 6, 20]})
    print(_demo["score"])
    print(_demo[_demo["team"] == "Ost"])
    print(_demo[_demo["team"] == "Ost"]["score"].sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `orders_exb` below is tonight's order list. The investor taps the
    harbor on the map: *"What did Hafen bring in?"*

    Compute `hafen_revenue_exb`: the total `total_eur` of the orders whose
    `zone` is `"Hafen"`. The answer is a single number, not a table.
    """
    )
    return


@app.cell
def _(pd):
    # Given: do not change this
    orders_exb = pd.DataFrame(
        {
            "zone": ["Hafen", "Nord", "Sued", "Hafen", "Nord", "Hafen", "Sued", "Sued"],
            "items": [1, 2, 1, 3, 2, 1, 4, 2],
            "total_eur": [8.90, 17.40, 6.50, 26.10, 15.80, 9.70, 31.20, 13.30],
        }
    )
    return (orders_exb,)


@app.cell
def _(orders_exb):
    hafen_revenue_exb = None  # YOUR CODE BELOW
    return (hafen_revenue_exb,)


@app.cell(hide_code=True)
def _(hafen_revenue_exb, mo, pd, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 44.7
    _result = None
    if hafen_revenue_exb is None:
        _ok = False
        _msg = "Not attempted: Assign the number to `hafen_revenue_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(hafen_revenue_exb, (pd.Series, pd.DataFrame)):
        _ok = False
        _result = f"hafen_revenue_exb={hafen_revenue_exb!r}"
        _msg = "Wrong: `hafen_revenue_exb` is still a column/table. Select `total_eur` from the filtered rows and call `.sum()` to get one number."
    else:
        try:
            _v = round(float(hafen_revenue_exb), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number. Check what your last expression returns."
        else:
            _result = f"hafen_revenue_exb={hafen_revenue_exb}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: 44.70 EUR from three harbor orders. Filter the rows, pick the column, `.sum()`."
            elif _v == 128.9:
                _ok = False
                _msg = "Wrong: That's every zone. Keep only the Hafen rows before summing."
            elif _v == 0.0:
                _ok = False
                _msg = 'Wrong: Your filter matched nothing, so the sum is 0. pandas compares case-sensitively: the data spells it "Hafen".'
            elif _v == 3.0:
                _ok = False
                _msg = "Wrong: That's how many Hafen orders there are, not what they brought in. Sum `total_eur`, don't count rows."
            elif _v == 5.0:
                _ok = False
                _msg = "Wrong: That's the number of items, not euros. Sum the `total_eur` column."
            else:
                _ok = False
                _msg = 'Wrong: Filter to `zone == "Hafen"`, select `total_eur`, then `.sum()`.'
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Same order as the worked example: filter the rows with a mask, pick the `total_eur` column of what is left, then `.sum()`.",
            "Hint 2 (the structure)": '_hafen = orders_exb[orders_exb["zone"] == "___"]\nhafen_revenue_exb = float(_hafen["___"].sum())',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** next question from the investor: *"How many Sued orders
    had more than one item?"* Tobi's AI wrote the line below, and it
    printed a column of `True`/`False` instead of a number:

    ```python
    sued_multi_exb = orders_exb[orders_exb["zone"] == "Sued"]["items"] > 1
    ```

    Fix it: `sued_multi_exb` should be the **count** as one whole number.
    """
    )
    return


@app.cell
def _(orders_exb):
    sued_multi_exb = None  # YOUR CODE BELOW
    return (sued_multi_exb,)


@app.cell(hide_code=True)
def _(mo, pd, show_result, sued_multi_exb):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 2
    _result = None
    if sued_multi_exb is None:
        _ok = False
        _msg = "Not attempted: Assign the count to `sued_multi_exb` (a `print` alone doesn't count) and run the cell."
    elif isinstance(sued_multi_exb, (pd.Series, pd.DataFrame)):
        _ok = False
        _result = f"sued_multi_exb={sued_multi_exb!r}"
        _msg = "Wrong: That's Tobi's output: a mask, one boolean per row. `.sum()` on the mask counts the `True`s."
    else:
        try:
            _v = int(sued_multi_exb)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a whole number. Count the `True`s in the mask with `.sum()`."
        else:
            _result = f"sued_multi_exb={sued_multi_exb}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: Two Sued orders had more than one item. The comparison builds the mask; `.sum()` counts it."
            elif _v == 5:
                _ok = False
                _msg = "Wrong: That counts every zone. Keep the Sued filter from Tobi's line."
            elif _v == 3:
                _ok = False
                _msg = "Wrong: That's every Sued order. \"More than one\" is `> 1`, not `>= 1`."
            else:
                _ok = False
                _msg = 'Wrong: Filter to `zone == "Sued"`, compare `items > 1`, then `.sum()` the mask.'
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Tobi's line is one step short. A mask summed counts its `True`s; wrap the result in `int()` so it is a plain number.",
            "Hint 2 (the structure)": '_sued = orders_exb[orders_exb["zone"] == "___"]\nsued_multi_exb = int((_sued["items"] > ___).___())',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
