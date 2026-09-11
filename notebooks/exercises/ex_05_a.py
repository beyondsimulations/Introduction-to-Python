# notebooks/exercises/ex_05_a.py
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
    # Quick exercise: read the crash report (5–10 min)

    The health inspector is in the doorway and the till just died. All you
    have is the traceback Tobi left on the screen at 3 AM:

    ```
    Traceback (most recent call last):
      File "checkout.py", line 8, in <module>
        seat = table_map["C3"]
    KeyError: 'C3'
    ```

    Read it **bottom-up**. Which exception type crashed the till? Assign its
    name as text to `error_exa`, spelled the way Python prints it.
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
    # YOUR CODE BELOW: replace None
    error_exa = None
    return (error_exa,)


@app.cell(hide_code=True)
def _(error_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if error_exa is None:
        _ok = False
        _msg = "Not attempted — assign the name to `error_exa` as text (a `print` alone doesn't count) and run the cell."
    elif not isinstance(error_exa, str):
        _ok = False
        _msg = "Wrong — the answer is the name as **text**, in quotes."
    elif error_exa.strip().lower().replace(" ", "") == "keyerror":
        _ok = True
        _msg = "Correct — the last line names it: `table_map` has no key `'C3'`."
    else:
        _ok = False
        _msg = "Wrong — read the **last** line of the traceback. The word before the colon is the type."
    mo.callout(mo.md(_msg + show_result(error_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the second crash of the night ran through a function, so
    the traceback has **two** `File` lines:

    ```
    Traceback (most recent call last):
      File "checkout.py", line 14, in <module>
        share = split_bill(88.00, guests)
      File "checkout.py", line 6, in split_bill
        return round(amount / guests, 2)
    ZeroDivisionError: float division by zero
    ```

    On which **line number** did the division actually explode? Assign it as
    a number to `line_exa`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    line_exa = None
    return (line_exa,)


@app.cell(hide_code=True)
def _(line_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if line_exa is None:
        _ok = False
        _msg = "Not attempted — assign the line number to `line_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(line_exa, (int, float)) and not isinstance(line_exa, bool) and line_exa == 6:
        _ok = True
        _msg = "Correct — the lowest `File` line is where it exploded: line 6, inside `split_bill`. Line 14 only made the call."
    elif isinstance(line_exa, (int, float)) and line_exa == 14:
        _ok = False
        _msg = "Wrong — line 14 is the *caller*. Keep reading down: the last `File` line is the one that ran when it broke."
    else:
        _ok = False
        _msg = "Wrong — the answer is a plain number taken from one of the two `File ... line N` lines."
    mo.callout(mo.md(_msg + show_result(line_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
