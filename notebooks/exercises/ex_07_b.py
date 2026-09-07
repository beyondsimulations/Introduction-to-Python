# notebooks/exercises/ex_07_b.py
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
    # Quick exercise: boolean masks (10 min)

    Comparing an array to a number doesn't give one `True`/`False`. It
    gives a whole array of them, one per element. That array of booleans
    is a **mask**, and it's the tool for filtering and counting without a
    loop.

    **Predict** first: what does the cell below print, then run it.
    """
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
    Tonight's delivery run is in `times_exb` below, in minutes. Anything
    over 38 minutes counts as "late," and the investor wants two numbers:
    how many deliveries were late, and what those late ones averaged.

    Compute `late_count_exb` (how many deliveries were late) and
    `late_mean_exb` (the average of just the late ones).
    """
    )
    return


@app.cell
def _(np):
    # Given — do not change this
    times_exb = np.array([31, 22, 47, 15, 36, 28, 51, 19, 40])
    return (times_exb,)


@app.cell
def _(times_exb):
    # YOUR CODE BELOW — replace None
    late_count_exb = None
    return (late_count_exb,)


@app.cell
def _(times_exb):
    # YOUR CODE BELOW — replace None
    late_mean_exb = None
    return (late_mean_exb,)


@app.cell(hide_code=True)
def _(late_count_exb, late_mean_exb, mo, np, show_result):
    # Reactive check — re-runs automatically whenever the cells above change.
    _expected_count = 3
    _expected_mean = 46.0
    _result = None
    # Coerce to plain scalars first — a leftover array (or anything else
    # non-numeric) must degrade to a message, never crash the check.
    try:
        _count = int(late_count_exb)
        _mean = round(float(late_mean_exb), 2)
    except (TypeError, ValueError):
        _count = None
        _mean = None
    if late_count_exb is None or late_mean_exb is None:
        _ok = False
        _msg = "🔲 Not attempted yet."
    else:
        _result = f"late_count_exb={late_count_exb}, late_mean_exb={late_mean_exb}"
        if _count is None or _mean is None:
            _ok = False
            if np.ndim(late_count_exb) > 0 or np.ndim(late_mean_exb) > 0:
                _msg = "❌ One of these is still a whole array — `.sum()` counts the Trues, and `.mean()` reduces the late times to one number."
            else:
                _msg = "❌ Not quite — start with the comparison: `times_exb > 38` makes a True/False array first."
        elif _count == _expected_count and _mean == _expected_mean:
            _ok = True
            _msg = "✅ Correct! Three late deliveries, and now the investor has the average too."
        elif _count == _expected_count:
            _ok = False
            _msg = "❌ The count is right, but the mean isn't — filter `times_exb` with the mask *before* calling `.mean()`."
        else:
            _ok = False
            _msg = "❌ Not quite — start with the comparison: `times_exb > 38` makes a True/False array first."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Comparison first — `times_exb > 38` makes a True/False array; `.sum()` counts the `True`s, and indexing with that same mask keeps only the matching values.",
            "💡 Hint 2 (the structure)": "late_count_exb = int((times_exb > ___).sum())\nlate_mean_exb = float(times_exb[times_exb > ___].___())",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
