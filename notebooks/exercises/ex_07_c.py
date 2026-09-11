# notebooks/exercises/ex_07_c.py
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
    # Quick exercise: boolean masks (5–10 min)

    Comparing an array to a number doesn't give one `True`/`False`. It
    gives a whole array of them, one per element. That array of booleans
    is a **mask**, and it's the tool for filtering and counting without a
    loop.

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
    import numpy as np
    return (np,)


@app.cell
def _(np):
    # Worked example (read + run this)
    _demo = np.array([1, 5, 3])
    print(_demo > 2)
    print((_demo > 2).sum())
    print(f"and the values themselves: {_demo[_demo > 2]}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Tonight's delivery run is in `times_exc` below, in minutes. Anything
    over 38 minutes counts as "late," and the investor wants two numbers:
    how many deliveries were late, and what those late ones averaged.

    Compute `late_count_exc` (how many deliveries were late) and
    `late_mean_exc` (the average of just the late ones).
    """
    )
    return


@app.cell
def _(np):
    # Given: do not change this
    times_exc = np.array([31, 22, 47, 15, 36, 28, 51, 19, 40])
    return (times_exc,)


@app.cell
def _(times_exc):
    # YOUR CODE BELOW: replace None
    late_count_exc = None
    return (late_count_exc,)


@app.cell
def _(times_exc):
    # YOUR CODE BELOW: replace None
    late_mean_exc = None
    return (late_mean_exc,)


@app.cell(hide_code=True)
def _(late_count_exc, late_mean_exc, mo, np, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected_count = 3
    _expected_mean = 46.0
    _result = None
    try:
        _count = int(late_count_exc)
        _mean = round(float(late_mean_exc), 2)
    except (TypeError, ValueError):
        _count = None
        _mean = None
    if late_count_exc is None or late_mean_exc is None:
        _ok = False
        _msg = "Not attempted — Assign it to `late_count_exc` and `late_mean_exc` (a `print` alone doesn't count) and run the cell."
    else:
        _result = f"late_count_exc={late_count_exc}, late_mean_exc={late_mean_exc}"
        if _count is None or _mean is None:
            _ok = False
            if np.ndim(late_count_exc) > 0 or np.ndim(late_mean_exc) > 0:
                _msg = "Wrong — One of these is still a whole array. Remember that `.sum()` counts the Trues, and `.mean()` reduces the late times to one number."
            else:
                _msg = "Wrong — Start with the comparison: `times_exc > 38` makes a True/False array first."
        elif _count == _expected_count and _mean == _expected_mean:
            _ok = True
            _msg = "Correct — Three late deliveries, and now the investor has the average too."
        elif _count == _expected_count:
            _ok = False
            _msg = "Wrong — The count is right, but the mean isn't. Filter `times_exc` with the mask *before* calling `.mean()`."
        else:
            _ok = False
            _msg = "Wrong — Start with the comparison: `times_exc > 38` makes a True/False array first."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Comparison first: `times_exc > 38` makes a True/False array; `.sum()` counts the `True`s, and indexing with that same mask keeps only the matching values.",
            "Hint 2 (the structure)": "late_count_exc = int((times_exc > ___).sum())\nlate_mean_exc = float(times_exc[times_exc > ___].___())",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor doesn't want a count, he wants a **share**: what fraction of tonight's run was late? Compute `late_share_exc` as one number between 0 and 1. No division by hand: a mask has a `.mean()`.
    """
    )
    return


@app.cell
def _(times_exc):
    # YOUR CODE BELOW: replace None
    late_share_exc = None
    return (late_share_exc,)


@app.cell(hide_code=True)
def _(late_share_exc, mo, np, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 0.33
    try:
        _share = round(float(late_share_exc), 2)
    except (TypeError, ValueError):
        _share = None
    if late_share_exc is None:
        _ok = False
        _msg = "Not attempted — assign it to `late_share_exc` (a `print` alone doesn't count) and run the cell."
    elif _share is None:
        _ok = False
        if np.ndim(late_share_exc) > 0:
            _msg = "Wrong — that's still a whole array. `.mean()` on the mask reduces it to one number."
        else:
            _msg = "Wrong — the share must be a number. Start from the mask `times_exc > 38`."
    elif _share == _expected:
        _ok = True
        _msg = "Correct — a third of the run was late. Averaging a mask gives the share of Trues."
    elif _share == 46.0:
        _ok = False
        _msg = "Wrong — that's the average *time* of the late ones. The share comes from the mask itself, not from the filtered times."
    elif _share == 3.0:
        _ok = False
        _msg = "Wrong — that's the count. `.sum()` counts the Trues; `.mean()` gives their share."
    else:
        _ok = False
        _msg = "Wrong — expected a fraction between 0 and 1: late deliveries divided by all deliveries."
    mo.callout(mo.md(_msg + show_result(late_share_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Each True counts as 1 and each False as 0, so the mean of a mask is the share of Trues. Call it on the mask, not on the filtered times.",
            "Hint 2 (the structure)": "late_share_exc = float((times_exc > ___).___())",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
