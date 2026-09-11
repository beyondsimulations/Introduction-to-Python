# notebooks/exercises/ex_04_d.py
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
    # Quick exercise: the campus map (5–10 min)

    Tobi split the campus into two delivery zones. Each zone is its own
    dictionary inside `zones`:

    ```python
    zones = {
        "North": {"fee": 1.50, "eta": 12, "dorms": ["Dorm A", "Dorm B"]},
        "South": {"fee": 2.50, "eta": 20, "dorms": ["Dorm C"]},
    }
    ```

    A South order just came in. Read the **fee** for the South zone out
    of `zones` (two keys in a row) and store it in `south_fee_exd`.

    Heads up: a misspelled key turns the answer cell red, and a red cell
    pauses the check below it. Fix the key and the check comes back.
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
    # Given: do not change this
    zones = {
        "North": {"fee": 1.50, "eta": 12, "dorms": ["Dorm A", "Dorm B"]},
        "South": {"fee": 2.50, "eta": 20, "dorms": ["Dorm C"]},
    }
    return (zones,)


@app.cell
def _(zones):
    # YOUR CODE BELOW: replace None
    south_fee_exd = None
    return (south_fee_exd,)


@app.cell(hide_code=True)
def _(mo, show_result, south_fee_exd):
    # Reactive check. Re-runs when you run the cell above.
    if south_fee_exd is None:
        _ok = False
        _msg = "Not attempted — assign it to `south_fee_exd` (a `print` alone doesn't count) and run the cell."
    elif isinstance(south_fee_exd, (int, float)) and round(south_fee_exd, 2) == 2.50:
        _ok = True
        _msg = "Correct — `zones[\"South\"][\"fee\"]`: outer key first, then the inner one."
    elif isinstance(south_fee_exd, (int, float)) and round(south_fee_exd, 2) == 1.50:
        _ok = False
        _msg = "Wrong — that's the North fee. The order goes South."
    elif isinstance(south_fee_exd, (int, float)) and round(south_fee_exd, 2) == 20:
        _ok = False
        _msg = "Wrong — 20 is the South `eta`, in minutes. You want the `fee`."
    elif isinstance(south_fee_exd, dict):
        _ok = False
        _msg = "Wrong — that's the whole South zone. Add a second `[...]` to reach into it."
    else:
        _ok = False
        _msg = "Wrong — read it left to right: in `zones`, take `\"South\"`, then its `\"fee\"`."
    mo.callout(mo.md(_msg + show_result(south_fee_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the North courier always ends the shift at the **last**
    dorm on the North list. Store that dorm's name in `last_north_exd`. Two
    dictionary keys, then a list index: three pairs of brackets in a row.
    """
    )
    return


@app.cell
def _(zones):
    # YOUR CODE BELOW: replace None
    last_north_exd = None
    return (last_north_exd,)


@app.cell(hide_code=True)
def _(last_north_exd, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if last_north_exd is None:
        _ok = False
        _msg = "Not attempted — assign it to `last_north_exd` (a `print` alone doesn't count) and run the cell."
    elif last_north_exd == "Dorm B":
        _ok = True
        _msg = "Correct — `zones[\"North\"][\"dorms\"][-1]`: dict, dict, then list."
    elif last_north_exd == "Dorm A":
        _ok = False
        _msg = "Wrong — that's the first dorm on the list. `-1` counts from the end."
    elif last_north_exd == "Dorm C":
        _ok = False
        _msg = "Wrong — Dorm C is in the South zone. Start from `\"North\"`."
    elif isinstance(last_north_exd, list):
        _ok = False
        _msg = "Wrong — that's the whole dorm list. Add one more `[...]` with an index to pick the last one."
    else:
        _ok = False
        _msg = "Wrong — expected the name of one dorm, as a string."
    mo.callout(mo.md(_msg + show_result(last_north_exd)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
