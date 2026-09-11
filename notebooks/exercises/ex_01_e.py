# notebooks/exercises/ex_01_e.py
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
    # Quick exercise: the first receipt line (5–10 min)

    A customer just ordered. Using `qty`, `item`, and `total` below and an
    f-string with `:.2f`, build **one** receipt line that reads exactly
    `"2x Falafel Wrap: 13.80 EUR"`.
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
    # Given: do not change these
    item = "Falafel Wrap"
    qty = 2
    total = 13.80
    return (item, qty, total)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    line_exe = None
    return (line_exe,)


@app.cell(hide_code=True)
def _(line_exe, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if line_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `line_exe` (a `print` alone doesn't count) and run the cell."
    elif line_exe == "2x Falafel Wrap: 13.80 EUR":
        _ok = True
        _msg = "Correct — the receipt printer purrs."
    else:
        _ok = False
        _msg = "Wrong — check the format `qty x item: total:.2f EUR`."
    mo.callout(mo.md(_msg + show_result(line_exe)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the customer adds `1` Miso Ramen at `11.50` EUR. Store
    in `receipt_exe` **one** string with two lines: your `line_exe` first,
    then `1x Miso Ramen: 11.50 EUR`, separated by `\n`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    receipt_exe = None
    return (receipt_exe,)


@app.cell(hide_code=True)
def _(mo, receipt_exe, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if receipt_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `receipt_exe` (a `print` alone doesn't count) and run the cell."
    elif receipt_exe == "2x Falafel Wrap: 13.80 EUR\n1x Miso Ramen: 11.50 EUR":
        _ok = True
        _msg = "Correct — one string, two lines. `\\n` is where the printer tears."
    elif isinstance(receipt_exe, str) and "\n" not in receipt_exe:
        _ok = False
        _msg = "Wrong — the two lines ended up on one. Put `\\n` between them inside the string."
    else:
        _ok = False
        _msg = "Wrong — check both lines: `qty x item: total EUR`, two decimals each, `\\n` in between."
    mo.callout(mo.md(_msg + show_result(receipt_exe)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
