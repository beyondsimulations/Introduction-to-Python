# notebooks/exercises/ex_03_a.py
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
    # Quick exercise: one receipt line, written once (5-10 min)

    Fourteen pasted copies of `round(qty * price, 2)`, one per menu item,
    and yesterday's ten-cent price change took Tobi an afternoon. He needs
    one function that does the job for every item.

    Write `line_total_exa(qty, price)` that returns `qty * price`,
    rounded to 2 decimals.
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
    def line_total_exa(qty, price):
        # YOUR CODE BELOW: return qty * price, rounded to 2 decimals
        return None

    return (line_total_exa,)


@app.cell(hide_code=True)
def _(line_total_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    try:
        _wraps = line_total_exa(2, 4.50)
        _fries = line_total_exa(5, 3.20)
    except Exception:
        _ok = False
        _msg = "Wrong: Still crashing. Read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if _wraps is None:
            _ok = False
            _msg = "Not attempted: The function still returns None. Use `return`, not `print`, then run the cell."
            _preview = ""
        elif (
            isinstance(_wraps, (int, float))
            and isinstance(_fries, (int, float))
            and round(_wraps, 2) == 9.00
            and round(_fries, 2) == 16.00
        ):
            _ok = True
            _msg = "Correct: 2 wraps at 4.50 make 9.00, 5 fries at 3.20 make 16.00. Fourteen copies retired."
            _preview = show_result(_wraps)
        else:
            _ok = False
            _msg = "Wrong: Multiply `qty` by `price`, round to 2 decimals, and `return` that."
            _preview = show_result(_wraps)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** Tobi wrote the matching receipt line, but wherever he
    stores what it hands back he gets `None`. Fix `line_label_exa` so the
    caller **receives** the text `2 x Wrap: 9.00 EUR` instead of only
    seeing it on screen.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW
    def line_label_exa(qty, item, price):
        # TOBI'S BUG: the caller gets nothing back
        print(f"{qty} x {item}: {qty * price:.2f} EUR")

    return (line_label_exa,)


@app.cell(hide_code=True)
def _(line_label_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    try:
        _label = line_label_exa(2, "Wrap", 4.50)
    except Exception:
        _ok = False
        _msg = "Wrong: Still crashing. Read the error above and fix it before it reaches the check."
        _preview = ""
    else:
        if _label is None:
            _ok = False
            _msg = "Not attempted: The caller still gets None: the line is printed, not returned. Swap `print(...)` for `return ...`, then run the cell."
            _preview = ""
        elif _label == "2 x Wrap: 9.00 EUR":
            _ok = True
            _msg = "Correct: Printing shows, returning hands back. Now the receipt can store the line."
            _preview = show_result(_label)
        else:
            _ok = False
            _msg = "Wrong: Keep the exact text `2 x Wrap: 9.00 EUR`, two decimals included."
            _preview = show_result(_label)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
