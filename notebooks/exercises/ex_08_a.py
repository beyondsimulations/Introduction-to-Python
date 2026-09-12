# notebooks/exercises/ex_08_a.py
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
    # Quick exercise: verifying AI code (5-10 min)

    AI wrote this for Tobi. Two things are wrong: one method doesn't
    exist, one comparison quietly returns nothing. Fix both, and you've
    done today's most important professional skill: verifying output.

    Filtering a DataFrame works just like the NumPy masks from last
    session: `df[df["col"] == value]` keeps the matching rows.

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
    _demo = pd.DataFrame({"team": ["Ost", "Ost", "West"], "score": [10, 6, 20]})
    print(_demo[_demo["team"] == "Ost"])
    print(_demo[_demo["team"] == "Ost"]["score"].mean())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `tobi_df` below stands in for the real order data. Tobi's AI draft is shown
    as a **comment** underneath it. Read it, spot the two bugs, then
    write correct code of your own to compute `mean_exa`: the average
    `total_eur` for the "Nord" zone.

    (If you paste Tobi's broken lines and run them for real, the cell
    turns red. That's expected. A red error pauses everything below it
    until you fix it; that's the workflow, not a crash.)
    """
    )
    return


@app.cell
def _(pd):
    # Given: do not change this
    tobi_df = pd.DataFrame(
        {
            "zone": ["Nord", "Nord", "Sued", "Nord", "Hafen"],
            "total_eur": [12.40, 8.90, 15.10, 22.20, 9.60],
        }
    )
    return (tobi_df,)


@app.cell
def _(tobi_df):
    # Tobi's AI draft (broken). Fix it in your own code below:
    #   nord = tobi_df[tobi_df["zone"] == "nord"]        # quietly empty… why?
    #   mean_exa = nord["total_eur"].summarize()           # AttributeError… why?
    mean_exa = None  # YOUR CODE BELOW
    return (mean_exa,)


@app.cell(hide_code=True)
def _(mean_exa, mo, pd, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 14.5
    _all_zones_mean = 13.64  # Tobi's "averaged everything" trap
    _result = None
    if mean_exa is None:
        _ok = False
        _msg = "Not attempted: Assign it to `mean_exa` (a `print` alone doesn't count) and run the cell."
    elif isinstance(mean_exa, (pd.Series, pd.DataFrame)):
        _ok = False
        _result = f"mean_exa={mean_exa!r}"
        _msg = "Wrong: `mean_exa` is still a whole column/table: `.mean()` collapses it to one number."
    else:
        try:
            _v = round(float(mean_exa), 2)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a number yet. Check what `.mean()` actually returns."
        else:
            _result = f"mean_exa={mean_exa}"
            if pd.isna(_v):
                _ok = False
                _msg = 'Wrong: Your filter came back empty. pandas comparisons are case-sensitive; check the zone spelling ("Nord" vs "nord").'
            elif _v == _expected:
                _ok = True
                _msg = "Correct: 14.5, and you just did today's most important professional skill: verifying AI output."
            elif _v == _all_zones_mean:
                _ok = False
                _msg = "Wrong: You averaged every zone instead of only Nord. Filter first, then take the mean."
            else:
                _ok = False
                _msg = 'Not quite. Filter to `zone == "Nord"` (case matters!), then call `.mean()`.'
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "String comparison is case-sensitive; and does pandas really have `summarize`? Check the docs, or ask an AI and VERIFY.",
            "Hint 2 (the structure)": '_nord = tobi_df[tobi_df["zone"] == "___"]\nmean_exa = float(_nord["total_eur"].___())',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the investor squints at the average and asks: *"and how
    many Nord orders are actually ABOVE that?"* Tobi's AI answered with
    `tobi_df[tobi_df["total_eur"] > mean_exa]` and counted the rows. That
    number is too high. Find out why, then compute `big_nord_exa`: how many
    **Nord** orders have a `total_eur` above `mean_exa`.
    """
    )
    return


@app.cell
def _(mean_exa, tobi_df):
    big_nord_exa = None  # YOUR CODE BELOW
    return (big_nord_exa,)


@app.cell(hide_code=True)
def _(big_nord_exa, mo, pd, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = 1
    _result = None
    if big_nord_exa is None:
        _ok = False
        _msg = "Not attempted: Assign the count to `big_nord_exa` (a `print` alone doesn't count) and run the cell. It needs `mean_exa` from the core task first."
    elif isinstance(big_nord_exa, (pd.Series, pd.DataFrame)):
        _ok = False
        _result = f"big_nord_exa={big_nord_exa!r}"
        _msg = "Wrong: `big_nord_exa` is still a column/table. A count is one whole number: `len(...)` of the filtered rows, or `.sum()` on the mask."
    else:
        try:
            _v = int(big_nord_exa)
        except (TypeError, ValueError):
            _ok = False
            _v = None
            _msg = "Wrong: That's not a whole number. Count the rows that survive both filters."
        else:
            _result = f"big_nord_exa={big_nord_exa}"
            if _v == _expected:
                _ok = True
                _msg = "Correct: One Nord order (22.20) beats the Nord average. Tobi's AI never filtered by zone, so the Sued order sneaked in."
            elif _v == 2:
                _ok = False
                _msg = "Wrong: That's Tobi's number. One of those two orders is from Sued: filter to Nord BEFORE comparing to the average."
            else:
                _ok = False
                _msg = 'Wrong: Filter to `zone == "Nord"` first, then keep the rows with `total_eur` above `mean_exa`, then count.'
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Two filters in a row: first the zone, then the price. Tobi's AI skipped the first one. A filtered frame can be filtered again.",
            "Hint 2 (the structure)": '_nord = tobi_df[tobi_df["zone"] == "___"]\n_big = _nord[_nord["total_eur"] > ___]\nbig_nord_exa = len(___)',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
