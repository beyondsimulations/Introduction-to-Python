# notebooks/nb_07_lab_metrics.py
# Episode 7: The Numbers Deck. Session VII lab notebook.
import marimo

app = marimo.App(width="medium", app_title="nb_07_lab_metrics")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 7.1: The Numbers Deck
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


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**How this notebook works:** run a cell with **Cmd/Ctrl+Enter**. "
            "Only edit the cells that contain `# YOUR CODE BELOW`; the check under "
            "each exercise updates by itself. A red error pauses everything below "
            "it, so fix that cell first."
        ),
        kind="info",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**First the install.** Before you start this lab, finish the Zed "
            "install from the lecture and show your lecturer that it works. Then "
            "come back to this tab."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Core exercises: 8 + 1 quiz (+ 1 trace, + 3 bonus).** Done early? You're free to go. Not done when the session ends? The rest is homework, and the next session opens with Checkpoint 4, so finish it before then.

    The investor liked last week's numbers. Now she wants a **one-page
    metrics deck**: totals, a per-zone breakdown, the busiest day, the strongest
    zone, the kind of sheet you could slide across a table without apologizing.

    Tobi has *also* prepared a deck. It is a **40-tab spreadsheet** with a tab
    called `FINAL_final_v3` and one formula that references a cell in a workbook
    he can no longer find. It is, gently, disqualified.

    So this week you learn the tool that turns a pile of orders into metrics
    without a single hand-written loop: **NumPy**. A NumPy *array* is like a list
    that does math: multiply the whole thing at once, compare it to a number to
    get a filter, stack it into a grid and total it by row or by column. That's
    the entire deck, computed in a few lines.

    > **As in the last lab: no hint boxes.** An exercise says what the result
    > has to be. Which tool gets you there is yours to work out, with the worked
    > examples, the lecture slides and your AI assistant.

    > **The marimo rule again:** AI answers usually start with
    > `import numpy as np`. The first worked example below imports numpy
    > already, and a name can only be defined in **one** cell, so delete that
    > line from the answer.

    > **New this week: plain Python numbers.** NumPy hands back its own number
    > types (`np.int64`, `np.float64`). The checks in this lab want plain Python
    > numbers, an `int` or a `float`, and so do the checkpoints. Convert a
    > result before you store it.
    """
    )
    return


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
def _(np):
    # Tells the checks what kind of answer they are looking at.
    def kind_of(value):
        if value is None:
            return "none"
        if isinstance(value, np.generic):
            return "numpy"
        if isinstance(value, bool):
            return "bool"
        if isinstance(value, int):
            return "int"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "str"
        if isinstance(value, (list, tuple, np.ndarray)):
            return "array"
        return "other"

    return (kind_of,)


@app.cell(hide_code=True)
def _():
    # The verdict for a NumPy number where a plain Python number is expected.
    def numpy_note(label, name, value):
        return (
            f"Wrong ({label}): `{name}` is a NumPy number (`{type(value).__name__}`), "
            "not a plain Python number. The checks here and the checkpoints want "
            "plain numbers, so convert it before you store it."
        )

    return (numpy_note,)


@app.cell(hide_code=True)
def _(mo):
    startup_name_input = mo.ui.text(
        label="Your startup's name:", placeholder="e.g. SnackRocket"
    )
    mo.vstack(
        [
            mo.md(
                "Before we build the deck, what's the company called again? Type "
                "it once and it sticks for the whole notebook. (New tab, so we ask "
                "afresh.)"
            ),
            startup_name_input,
        ]
    )
    return (startup_name_input,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(
        f"Building the metrics deck for **{startup_name}**. One page, real "
        "numbers. Let's make Tobi's 40 tabs look as silly as they are."
    )
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1: Asking questions of an array
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1: Asking questions of an array

    A **NumPy array** looks like a list, but it does math on all its numbers at
    once. Compare an array to a number and you get a whole array of
    `True`/`False`, one per element. That array is a **mask**, and it is how you
    count and filter without a loop:

    ```python
    import numpy as np
    speeds = np.array([5, 12, 3, 20])
    speeds * 2                     # array([10, 24,  6, 40]): every element at once
    speeds > 10                    # array([False,  True, False,  True]): the mask
    (speeds > 10).sum()            # 2: True counts as 1, so .sum() counts the hits
    (speeds > 10).mean()           # 0.5: the share of hits
    speeds[speeds > 10]            # array([12, 20]): keep only the matching values
    (speeds > 4) & (speeds < 15)   # two conditions: & between two masks, each in parentheses
    ```

    > One marimo habit for this lab: array math and indexing are easy to get
    > slightly wrong, and a **red error pauses everything below it**, including
    > the progress box. Nothing is lost; fix the red cell and it all comes back.

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this). It also imports numpy as np for everything below
    import numpy as np
    _demo = np.array([5, 12, 3, 20])
    print("mask:", _demo > 10)
    print("count over 10:", (_demo > 10).sum())
    print("the values over 10:", _demo[_demo > 10])
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core): the critical deliveries

    The first box on the deck is a risk. Here are ten delivery times, in
    minutes:

    ```python
    delivery_times = np.array([24, 39, 55, 17, 31, 46, 20, 60, 35, 42])
    ```

    A delivery that takes **more than 50 minutes** is "critical". Store two
    numbers:

    - `critical_count_ex11`: how many deliveries were critical,
    - `critical_mean_ex11`: the average length, in minutes, of just the
      critical ones.

    Both as plain Python numbers: the count an `int`, the average a `float`.
    """
    )
    return


@app.cell
def _(np):
    delivery_times = np.array([24, 39, 55, 17, 31, 46, 20, 60, 35, 42])
    return (delivery_times,)


@app.cell
def _():
    # YOUR CODE BELOW: how many delivery_times are over 50, as a plain int
    critical_count_ex11 = None
    return (critical_count_ex11,)


@app.cell
def _():
    # YOUR CODE BELOW: the average of only the delivery_times over 50, as a plain float
    critical_mean_ex11 = None
    return (critical_mean_ex11,)


@app.cell(hide_code=True)
def _(critical_count_ex11, critical_mean_ex11, kind_of, mo, numpy_note, show_result):
    _kc, _km = kind_of(critical_count_ex11), kind_of(critical_mean_ex11)
    _preview = show_result(critical_count_ex11) + show_result(critical_mean_ex11)
    if _kc == "none" and _km == "none":
        ex11_ok = False
        _msg = "Not attempted (Exercise 1.1). Assign your answers to `critical_count_ex11` and `critical_mean_ex11` (a `print` alone doesn't count) and run the cells."
    elif _kc == "none" or _km == "none":
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): both numbers are needed. Fill in `critical_count_ex11` *and* `critical_mean_ex11`."
    elif _kc == "numpy":
        ex11_ok = False
        _msg = numpy_note("Exercise 1.1", "critical_count_ex11", critical_count_ex11)
    elif _km == "numpy":
        ex11_ok = False
        _msg = numpy_note("Exercise 1.1", "critical_mean_ex11", critical_mean_ex11)
    elif _kc == "array" or _km == "array":
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): one of your answers is still a whole array. The deck needs **one number** each: a count and an average."
    elif _kc != "int" or _km not in ("int", "float"):
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): the count has to be a plain `int` and the average a plain `float`."
    elif critical_count_ex11 == 2 and round(critical_mean_ex11, 2) == 57.5:
        ex11_ok = True
        _msg = "Correct (Exercise 1.1): **2** critical deliveries, averaging **57.5** minutes. The mask picked them out, and no loop was needed."
    elif round(critical_mean_ex11, 2) == 0.2:
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): an average of 0.2 minutes? Do the couriers teleport? 0.2 is the **share** of critical deliveries. The deck wants their average **length**, in minutes."
    elif round(critical_mean_ex11, 2) == 36.9:
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): 36.9 is the average of **all ten** deliveries. The box asks about the critical ones only."
    elif critical_count_ex11 == 8:
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): 8 is the number of deliveries that were **not** critical."
    elif critical_count_ex11 != 2:
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): not the number of critical deliveries. Critical means more than 50 minutes."
    else:
        ex11_ok = False
        _msg = "Wrong (Exercise 1.1): the count is right, the average is not. It is the average of just the deliveries over 50 minutes."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core): the risk report

    The investor wants this box for every courier and every limit, so turn it
    into a function. Write `risk_report_ex12(times, limit)`. `times` is an array
    of delivery times, `limit` a number of minutes. It returns a **dict** with
    exactly these keys:

    - `"count"`: how many deliveries took longer than `limit` (a plain `int`),
    - `"share"`: that count as a share of all deliveries, between 0 and 1 (a
      plain `float`),
    - `"mean"`: the average of just those deliveries (a plain `float`).

    For the ten deliveries above and a limit of 50, the report is
    `{"count": 2, "share": 0.2, "mean": 57.5}`.

    **One rule for a perfect week:** when no delivery is over the limit, the
    report says `"mean": 0.0`.
    """
    )
    return


@app.cell
def _():
    def risk_report_ex12(times, limit):
        # YOUR CODE BELOW: return the dict with the keys "count", "share" and "mean"
        # for the deliveries over `limit`, all as plain Python numbers
        return None

    return (risk_report_ex12,)


@app.cell(hide_code=True)
def _(kind_of, mo, np, numpy_note, risk_report_ex12):
    # Reactive check.
    import warnings as _warnings

    _cases = [
        (np.array([24, 39, 55, 17, 31, 46, 20, 60, 35, 42]), 50, (2, 0.2, 57.5)),
        (np.array([12, 44, 31, 28, 36, 19, 52, 30]), 30, (4, 0.5, 40.75)),
        (np.array([18, 22, 25, 30, 14]), 30, (0, 0.0, 0.0)),
    ]
    _keys = ("count", "share", "mean")
    try:
        with _warnings.catch_warnings():
            _warnings.simplefilter("ignore")
            _got = [risk_report_ex12(_c[0].copy(), _c[1]) for _c in _cases]
        _err = ""
    except Exception as _e:
        _got = None
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _got is None:
        ex12_ok = False
        _msg = f"Wrong (Exercise 1.2): calling `risk_report_ex12(delivery_times, 50)` raises an error (`{_err}`)."
    elif all(_v is None for _v in _got):
        ex12_ok = False
        _msg = "Not attempted (Exercise 1.2): the function still returns `None`. Use `return`, not `print`, then run the cell."
    else:
        _preview = f"\n\n**Your result:** `risk_report_ex12(delivery_times, 50)` gives `{_got[0]}`"
        if not all(isinstance(_v, dict) for _v in _got):
            ex12_ok = False
            _msg = "Wrong (Exercise 1.2): the report has to be a **dict**, like `{\"count\": ..., \"share\": ..., \"mean\": ...}`."
        elif not all(_k in _v for _v in _got for _k in _keys):
            ex12_ok = False
            _missing = ", ".join(f'`"{_k}"`' for _k in _keys if _k not in _got[0])
            _msg = f"Wrong (Exercise 1.2): the report is missing a key: {_missing or 'check the spelling of all three'}. The keys are `\"count\"`, `\"share\"` and `\"mean\"`, spelled exactly like that."
        else:
            _kinds = [[kind_of(_v[_k]) for _k in _keys] for _v in _got]
            _flat = [_x for _row in _kinds for _x in _row]
            if "numpy" in _flat:
                ex12_ok = False
                _bad = next(_k for _row in _kinds for _k, _x in zip(_keys, _row) if _x == "numpy")
                _msg = numpy_note("Exercise 1.2", f'"{_bad}"', next(_v[_bad] for _v in _got if kind_of(_v[_bad]) == "numpy"))
            elif "array" in _flat:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): one of the three values is still a whole array. Each key holds **one number**."
            elif "none" in _flat:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): one of the three values is `None`. Every key needs a number, also in a perfect week: the rule says `\"mean\": 0.0` there."
            elif not all(_x in ("int", "float") for _x in _flat):
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): all three values have to be numbers."
            elif any(_v[_k] != _v[_k] for _v in _got for _k in _keys):
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): for a week with **no** delivery over the limit, your report contains `nan` (\"not a number\"). NumPy cannot average an empty selection. The rule for a perfect week says `\"mean\": 0.0`."
            elif not all(_row[0] == "int" for _row in _kinds):
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): `\"count\"` has to be a plain `int`, a whole number of deliveries."
            else:
                _r = [(_v["count"], round(float(_v["share"]), 2), round(float(_v["mean"]), 2)) for _v in _got]
                _want = [_c[2] for _c in _cases]
                if _r == _want:
                    ex12_ok = True
                    _msg = "Correct (Exercise 1.2): 2 critical deliveries out of ten, a share of 0.2, averaging 57.5 minutes, and a perfect week reports a mean of 0.0 instead of `nan`. One function for every courier and every limit."
                elif _r[1][0] == 5 or _r[2][0] == 1:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): a delivery of exactly 30 minutes is not **over** a limit of 30, but your report counts it."
                elif _r[0][1:] == (57.5, 0.2):
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): `\"share\"` and `\"mean\"` are the wrong way round."
                elif _r[0][1] == 20.0:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): the share should be a number between 0 and 1. 2 of 10 deliveries is 0.2."
                elif _r[0][2] == 36.9:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): 36.9 is the average of **all** deliveries. `\"mean\"` is the average of just the ones over the limit."
                elif [_x[0] for _x in _r] != [_x[0] for _x in _want]:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): `\"count\"` is not right. For the ten deliveries and a limit of 50 it is 2."
                elif [_x[1] for _x in _r] != [_x[1] for _x in _want]:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): `\"count\"` is right, `\"share\"` is not. It is the count divided by the number of all deliveries: 0.2 for the ten above."
                elif _r[2][2] != 0.0:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): right for the ten deliveries, but not for a perfect week. With no delivery over the limit, the rule says `\"mean\": 0.0`."
                else:
                    ex12_ok = False
                    _msg = "Wrong (Exercise 1.2): `\"count\"` and `\"share\"` are right, `\"mean\"` is not. It is 57.5 for the ten deliveries and a limit of 50."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.3 (core, fix the bug): the middle band

    The investor has a middle band of deliveries she calls "slow but
    acceptable": **more than 30 minutes, and at most 50**. Tobi counted it.
    His cell runs, no red error, and says the middle band holds **all ten**
    deliveries, the 17-minute one and the 60-minute one included.

    Fix Tobi's line **in place** so `band_count_ex13` holds the number of
    deliveries in the middle band.
    """
    )
    return


@app.cell
def _(delivery_times):
    # YOUR CODE BELOW
    # TOBI'S CODE: the deliveries in the middle band, but it counts all ten.
    band_count_ex13 = int(((delivery_times > 30) | (delivery_times <= 50)).sum())
    return (band_count_ex13,)


@app.cell(hide_code=True)
def _(band_count_ex13, kind_of, mo, numpy_note, show_result):
    _k = kind_of(band_count_ex13)
    _preview = show_result(band_count_ex13)
    if _k == "none":
        ex13_ok = False
        _msg = "Not attempted (Exercise 1.3). Assign it to `band_count_ex13` (a `print` alone doesn't count) and run the cell."
    elif _k == "numpy":
        ex13_ok = False
        _msg = numpy_note("Exercise 1.3", "band_count_ex13", band_count_ex13)
    elif _k != "int":
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): the answer is a count of deliveries, so one plain `int`."
    elif band_count_ex13 == 5:
        ex13_ok = True
        _msg = "Correct (Exercise 1.3): **5** deliveries are in the middle band. Tobi asked for deliveries that are over 30 **or** at most 50, and every delivery is one or the other. The band needs both conditions at once."
    elif band_count_ex13 == 10:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): still all ten. Say Tobi's condition out loud for the 17-minute delivery: is it over 30? Is it at most 50? Which of those two answers lets it in?"
    elif band_count_ex13 == 7:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): 7 is every delivery over 30 minutes, the two critical ones included. The band also has an upper end."
    elif band_count_ex13 == 8:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): 8 is every delivery of at most 50 minutes, the fast ones included. The band also has a lower end."
    else:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): not the middle band. A delivery belongs to it when it took more than 30 minutes and at most 50."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex13_ok else "warn")
    return (ex13_ok,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2: The week as a grid
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2: The week as a grid

    Here is the real week as a grid: `week_sales`, **7 days down, 4 zones
    across**, with the zone names in `zones`, left to right:

    ```python
    week_sales = np.array([[18,  7, 12,  9],
                           [22, 11,  8, 14],
                           [15, 19, 10,  6],
                           [25, 13, 17,  8],
                           [ 9, 21, 14, 12],
                           [24, 16, 20, 18],
                           [28, 22, 19, 15]])
    zones = ["Nord", "Sued", "Hafen", "Altstadt"]
    ```

    To total a grid you say which way to collapse it. `axis=0` collapses **down
    the rows** and leaves one number per column. `axis=1` collapses **across the
    columns** and leaves one number per row:

    ```python
    small = np.array([[1, 2, 3],
                      [4, 5, 6]])
    small.sum(axis=0)            # array([5, 7, 9]): one total per column
    small.sum(axis=1)            # array([ 6, 15]): one total per row
    small.sum()                  # 21: without an axis, everything collapses
    small.sum(axis=0).argmax()   # 2: the POSITION of the largest total
    ```

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _(np):
    # Worked example (read + run this): the two ways to collapse a grid
    _small = np.array([[1, 2, 3], [4, 5, 6]])
    print("per column (axis=0):", _small.sum(axis=0))
    print("per row (axis=1):   ", _small.sum(axis=1))
    return


@app.cell
def _(np):
    week_sales = np.array(
        [
            [18, 7, 12, 9],
            [22, 11, 8, 14],
            [15, 19, 10, 6],
            [25, 13, 17, 8],
            [9, 21, 14, 12],
            [24, 16, 20, 18],
            [28, 22, 19, 15],
        ]
    )
    return (week_sales,)


@app.cell
def _():
    zones = ["Nord", "Sued", "Hafen", "Altstadt"]
    return (zones,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core, fix the bug): seven numbers, not four

    The investor asked for the **orders per zone**: four numbers, one for each
    zone. Tobi sent her **seven**. His cell runs without an error.

    Fix Tobi's line **in place** so `zone_totals_ex21` holds the four zone
    totals.
    """
    )
    return


@app.cell
def _(week_sales):
    # YOUR CODE BELOW
    # TOBI'S CODE: the orders per zone, but it has seven numbers and there are four zones.
    zone_totals_ex21 = week_sales.sum(axis=1)
    return (zone_totals_ex21,)


@app.cell(hide_code=True)
def _(mo, np, zone_totals_ex21):
    try:
        _arr = None if zone_totals_ex21 is None else np.asarray(zone_totals_ex21, dtype=float)
    except Exception:
        _arr = "bad"
    _preview = "" if zone_totals_ex21 is None else f"\n\n**Your result:** `{zone_totals_ex21}`"
    if _arr is None:
        ex21_ok = False
        _msg = "Not attempted (Exercise 2.1). Assign it to `zone_totals_ex21` (a `print` alone doesn't count) and run the cell."
    elif isinstance(_arr, str):
        ex21_ok = False
        _msg = "Wrong (Exercise 2.1): `zone_totals_ex21` should hold four numbers, one per zone."
    elif _arr.shape == (4,) and _arr.tolist() == [141, 109, 100, 82]:
        ex21_ok = True
        _msg = "Correct (Exercise 2.1): **four** totals, Nord 141, Sued 109, Hafen 100, Altstadt 82. Tobi collapsed the grid the other way and got one total per day."
    elif _arr.shape == (7,):
        ex21_ok = False
        _msg = "Wrong (Exercise 2.1): still seven numbers, one per **day**. The zones run across the grid, so the days are what has to disappear."
    elif _arr.shape == ():
        ex21_ok = False
        _msg = "Wrong (Exercise 2.1): that is a single number. The investor wants four, one per zone."
    elif _arr.shape == (4,):
        ex21_ok = False
        _msg = "Wrong (Exercise 2.1): four numbers, but not the zone totals. Each one is the sum of a whole column of `week_sales`."
    else:
        ex21_ok = False
        _msg = "Wrong (Exercise 2.1): `zone_totals_ex21` should hold four numbers, one per zone."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core): each zone's share

    Totals are hard to compare at a glance, so the deck shows each zone's
    **share of the week's orders, in percent**. Store the four percentages in
    `zone_shares_ex22`, in zone order, rounded to 1 decimal. Together they come
    to about 100.

    You already have the four zone totals from 2.1.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: each zone's share of all orders of the week, in percent, rounded to 1 decimal
    zone_shares_ex22 = None
    return (zone_shares_ex22,)


@app.cell(hide_code=True)
def _(mo, np, zone_shares_ex22):
    try:
        _arr = None if zone_shares_ex22 is None else np.asarray(zone_shares_ex22, dtype=float)
    except Exception:
        _arr = "bad"
    _preview = "" if zone_shares_ex22 is None else f"\n\n**Your result:** `{zone_shares_ex22}`"
    _want = np.array([32.6, 25.2, 23.1, 19.0])
    if _arr is None:
        ex22_ok = False
        _msg = "Not attempted (Exercise 2.2). Assign it to `zone_shares_ex22` (a `print` alone doesn't count) and run the cell."
    elif isinstance(_arr, str) or _arr.shape != (4,):
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): `zone_shares_ex22` should hold four percentages, one per zone, in zone order."
    elif np.allclose(np.round(_arr, 1), _want, atol=0.01):
        ex22_ok = True
        _msg = "Correct (Exercise 2.2): Nord **32.6 %**, Sued 25.2 %, Hafen 23.1 %, Altstadt 19.0 %. One division on the whole array, and nobody wrote a loop."
    elif np.allclose(np.round(_arr * 100, 1), _want, atol=0.01):
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): these are shares between 0 and 1. The deck shows them **in percent**: Nord should read 32.6."
    elif np.allclose(_arr, [141, 109, 100, 82]):
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): these are the totals again. A share compares each total with the orders of the whole week."
    else:
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): not the four shares. Each one is a zone's total divided by all orders of the week, in percent. Together they come to about 100."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core): which zone wins?

    The headline of the deck is one name: the zone with the most orders. Next
    month the grid will hold other numbers, and maybe other zones, so write a
    function. `best_zone_ex23(grid, names)` gets a grid like `week_sales` (days
    down, zones across) and the list of zone names. It returns the **name** of
    the zone with the highest total.

    For this week, `best_zone_ex23(week_sales, zones)` is `"Nord"`.
    """
    )
    return


@app.cell
def _():
    def best_zone_ex23(grid, names):
        # YOUR CODE BELOW: return the name of the zone (column) with the highest total
        return None

    return (best_zone_ex23,)


@app.cell(hide_code=True)
def _(best_zone_ex23, mo, np):
    # Reactive check.
    _cases = [
        (
            np.array([[18, 7, 12, 9], [22, 11, 8, 14], [15, 19, 10, 6], [25, 13, 17, 8], [9, 21, 14, 12], [24, 16, 20, 18], [28, 22, 19, 15]]),
            ["Nord", "Sued", "Hafen", "Altstadt"],
            "Nord",
        ),
        (np.array([[9, 9, 20, 3], [2, 8, 12, 4], [1, 6, 9, 2]]), ["Nord", "Sued", "Hafen", "Altstadt"], "Hafen"),
        (np.array([[4, 2, 9], [3, 1, 8]]), ["Campus", "City", "Port"], "Port"),
    ]
    try:
        _got = [best_zone_ex23(_c[0].copy(), list(_c[1])) for _c in _cases]
        _err = ""
    except Exception as _e:
        _got = None
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _got is None:
        ex23_ok = False
        _msg = f"Wrong (Exercise 2.3): calling `best_zone_ex23(week_sales, zones)` raises an error (`{_err}`). If it is an `IndexError`: a position that counts days cannot be looked up in a list of zones."
    elif all(_v is None for _v in _got):
        ex23_ok = False
        _msg = "Not attempted (Exercise 2.3): the function still returns `None`. Use `return`, not `print`, then run the cell."
    else:
        _preview = f"\n\n**Your result:** `best_zone_ex23(week_sales, zones)` gives `{_got[0]!r}`"
        if not all(isinstance(_v, str) for _v in _got):
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): the function has to return the zone's **name**, a string like `\"Nord\"`. A position or a total is only half the way there."
        elif _got == [_c[2] for _c in _cases]:
            ex23_ok = True
            _msg = "Correct (Exercise 2.3): **Nord** wins this week, and the function finds Hafen and Port in two other grids. The position of the largest total, looked up in the names: a headline that updates itself."
        elif _got[0] == "Nord":
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): right for this week, wrong for another grid. In a grid where Hafen has the most orders, your function still answers something else. Is the winner typed in by hand, or is the grid collapsed the wrong way?"
        else:
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): for this week the answer is `\"Nord\"`, the zone whose column adds up to the most."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.4 (core): a business or a weekend stand?

    The investor has a rule about the busiest day: if **one day carries more
    than a quarter of the week's orders**, the company is "a weekend stand with
    a logo", and she wants a weekday campaign before she signs anything.

    Store the busiest day's share of the whole week's orders in
    `peak_share_ex24`, as a plain `float` between 0 and 1.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the busiest day's orders divided by all orders of the week, as a plain float
    peak_share_ex24 = None
    return (peak_share_ex24,)


@app.cell(hide_code=True)
def _(kind_of, mo, numpy_note, peak_share_ex24, show_result):
    _k = kind_of(peak_share_ex24)
    _preview = show_result(peak_share_ex24)
    if _k == "none":
        ex24_ok = False
        _msg = "Not attempted (Exercise 2.4). Assign it to `peak_share_ex24` (a `print` alone doesn't count) and run the cell."
    elif _k == "numpy":
        ex24_ok = False
        _msg = numpy_note("Exercise 2.4", "peak_share_ex24", peak_share_ex24)
    elif _k == "array":
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): that is still a whole array. The rule needs **one number**: the busiest day's share."
    elif _k not in ("int", "float"):
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): the share has to be one plain `float` between 0 and 1."
    elif round(peak_share_ex24, 2) == 0.19:
        ex24_ok = True
        _msg = "Correct (Exercise 2.4): the busiest day carries **0.19** of the week, about a fifth and under her quarter. A business, then. The investor does not smile, but she turns the page."
    elif peak_share_ex24 == 84:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): 84 is the busiest day's number of orders. The rule compares it with the orders of the whole week."
    elif round(peak_share_ex24, 2) == 19.44:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): that is the share in percent. Store it as a number between 0 and 1."
    elif round(peak_share_ex24, 2) == 0.33:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): 0.33 is the strongest **zone's** share. Her rule is about the busiest **day**."
    else:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): not the busiest day's share. Total each day, take the largest of the seven, and compare it with all orders of the week."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex24_ok else "warn")
    return (ex24_ok,)


# ─────────────────────────────────────────────────────────────────────────
# PUTTING IT TOGETHER: the strong days
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Putting it together (core): the strong days

    The busiest day is a single number. The investor asks the wider
    question: "How much of your week hangs on your **strong days**?" A strong
    day is a day with **more orders than the average day**.

    Three steps, each in its own cell, each building on the one before:

    1. `day_totals_ex40`: the orders of each of the seven days, as an array.
    2. `strong_days_ex40`: **how many** days are strong (a plain `int`).
    3. `strong_share_ex40`: the share of the week's orders that fell on the
       strong days (a plain `float` between 0 and 1).
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the orders of each of the seven days, as an array
    day_totals_ex40 = None
    return (day_totals_ex40,)


@app.cell
def _():
    # YOUR CODE BELOW: how many days have more orders than the average day (a plain int)
    strong_days_ex40 = None
    return (strong_days_ex40,)


@app.cell
def _():
    # YOUR CODE BELOW: the strong days' orders as a share of all orders of the week (a plain float)
    strong_share_ex40 = None
    return (strong_share_ex40,)


@app.cell(hide_code=True)
def _(day_totals_ex40, kind_of, mo, np, numpy_note, strong_days_ex40, strong_share_ex40):
    # Reactive check.
    _days = np.array([46, 55, 50, 63, 56, 78, 84])
    try:
        _arr = None if day_totals_ex40 is None else np.asarray(day_totals_ex40, dtype=float)
    except Exception:
        _arr = "bad"
    _k2, _k3 = kind_of(strong_days_ex40), kind_of(strong_share_ex40)
    _preview = ""
    if _arr is None:
        ex40_ok = False
        _msg = "Not attempted (Putting it together). Start with step 1: assign the seven day totals to `day_totals_ex40` and run the cell."
    elif isinstance(_arr, str):
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 1): `day_totals_ex40` should hold seven numbers, one per day."
    elif _arr.shape != (7,) or _arr.tolist() != _days.tolist():
        ex40_ok = False
        _preview = f"\n\n**Your result:** `{day_totals_ex40}`"
        if _arr.shape == (4,):
            _msg = "Wrong (Putting it together, step 1): four numbers, one per **zone**. A day is a row of the grid, so the zones are what has to disappear."
        elif _arr.shape == (7,):
            _msg = "Wrong (Putting it together, step 1): seven numbers, but not the day totals. The first day has 18 + 7 + 12 + 9 = 46 orders."
        else:
            _msg = "Wrong (Putting it together, step 1): `day_totals_ex40` should hold seven numbers, one per day."
    elif _k2 == "none":
        ex40_ok = False
        _msg = "Step 1 is right: seven day totals, from 46 up to 84. Now step 2: assign `strong_days_ex40`."
    elif _k2 == "numpy":
        ex40_ok = False
        _msg = numpy_note("Putting it together, step 2", "strong_days_ex40", strong_days_ex40)
    elif _k2 != "int":
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 2): `strong_days_ex40` is a count of days, so one plain `int`."
        _preview = f"\n\n**Your result:** `{strong_days_ex40}`"
    elif strong_days_ex40 != 3:
        ex40_ok = False
        _preview = f"\n\n**Your result:** `{strong_days_ex40}`"
        if strong_days_ex40 == 4:
            _msg = "Wrong (Putting it together, step 2): 4 is the number of days **below** the average day. She asked for the strong ones."
        else:
            _msg = "Wrong (Putting it together, step 2): not the number of strong days. The average day has about 61.7 orders. How many of the seven days have more?"
    elif _k3 == "none":
        ex40_ok = False
        _msg = "Steps 1 and 2 are right: 3 of the 7 days are strong. Now step 3: assign `strong_share_ex40`."
    elif _k3 == "numpy":
        ex40_ok = False
        _msg = numpy_note("Putting it together, step 3", "strong_share_ex40", strong_share_ex40)
    elif _k3 not in ("int", "float"):
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 3): the share has to be one plain `float` between 0 and 1."
        _preview = f"\n\n**Your result:** `{strong_share_ex40}`"
    elif round(strong_share_ex40, 2) == 0.52:
        ex40_ok = True
        _msg = (
            "Correct (Putting it together): **3** of the 7 days are strong, and they carry "
            "**0.52** of the week's orders, a little more than half. The investor writes in "
            "the margin: \"three days pay for the other four.\" You built the mask from "
            "numbers you had computed yourself."
        )
        _preview = f"\n\n**Your result:** `{strong_days_ex40}` strong days, share `{strong_share_ex40}`"
    else:
        ex40_ok = False
        _preview = f"\n\n**Your result:** `{strong_share_ex40}`"
        if round(strong_share_ex40, 2) == 0.43:
            _msg = "Wrong (Putting it together, step 3): 0.43 is the share of the **days** that are strong (3 of 7). She asked what share of the **orders** fell on those days."
        elif strong_share_ex40 == 225:
            _msg = "Wrong (Putting it together, step 3): 225 is the number of orders on the strong days. A share compares it with all orders of the week."
        elif round(strong_share_ex40, 2) == 52.08:
            _msg = "Wrong (Putting it together, step 3): that is the share in percent. Store it as a number between 0 and 1."
        else:
            _msg = "Wrong (Putting it together, step 3): not the strong days' share. Add up the orders of the three strong days and compare them with all orders of the week."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


# ─────────────────────────────────────────────────────────────────────────
# TRACE + MCQ
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise (trace, predict first): an array is not a list

    This is a **trace** exercise: predict the answer first, *then* reveal it. It's
    ungraded. The point is committing to a prediction. In the lecture, `* 2` on a
    **plain list** repeated it. Now Tobi wraps the same numbers in `np.array`:

    ```python
    print(np.array([1, 2, 3]) * 2)
    ```

    What gets printed?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_repeat = mo.ui.radio(
        options=["[1 2 3 1 2 3]", "[2 4 6]", "an error"],
        label="Your prediction for `np.array([1, 2, 3]) * 2`:",
    )
    trace_repeat
    return (trace_repeat,)


@app.cell(hide_code=True)
def _(mo, trace_repeat):
    if trace_repeat.value is None:
        _msg = "Pick a prediction above first. Commit before you peek!"
    elif trace_repeat.value == "[2 4 6]":
        _msg = (
            "Correct: **`[2 4 6]`**. On a NumPy array, `* 2` *doubles every "
            "element*; on the plain list in the lecture it *repeated* the list. "
            "Lists repeat; arrays compute, which is exactly why this episode uses "
            "arrays. (Arrays print without commas.)"
        )
    else:
        _msg = (
            "Not quite: it's **`[2 4 6]`**. `* 2` on a NumPy *array* hits every "
            "element. Only the plain *list* repeats itself, and arrays print "
            "without commas. Lists repeat; arrays compute. (Ungraded. The point is "
            "the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ): reading a mask

    You used masks all through Section 1. Given the delivery times, what does this
    expression compute?

    ```python
    (delivery_times > 40).sum()
    ```

    Assign the letter (as text) to `answer_ex50`:

    - **a)** the sum of all the delivery times
    - **b)** the largest delivery time
    - **c)** an error: you can't sum True/False values
    - **d)** how many delivery times exceed 40
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace "" with "a", "b", "c", or "d"
    answer_ex50 = ""
    return (answer_ex50,)


@app.cell(hide_code=True)
def _(answer_ex50, mo):
    if answer_ex50 == "":
        ex50_ok = False
        _msg = "Not attempted (Quiz). Set `answer_ex50` to your letter and run the cell."
    elif str(answer_ex50).strip().lower() == "d":
        ex50_ok = True
        _msg = (
            "Correct (Quiz): **d**. `delivery_times > 40` is a True/False mask; `True` "
            "counts as 1, so `.sum()` counts how many times cleared 40: a count, "
            "not a total or a maximum."
        )
    else:
        ex50_ok = False
        _msg = (
            "Wrong (Quiz): not quite. `delivery_times > 40` makes a True/False mask, and "
            "summing Trues (each worth 1) *counts* them. It doesn't total the "
            "times or find the biggest."
        )
    mo.callout(mo.md(_msg), kind="success" if ex50_ok else "warn")
    return (ex50_ok,)


# ─────────────────────────────────────────────────────────────────────────
# BONUS (not required)
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus: most orders is not most money (not required)

    Nord wins on orders. But an order in Altstadt is worth more than an order in
    Nord. The average order value per zone, in euros, in zone order:

    ```python
    avg_value = np.array([11.5, 14.0, 16.5, 19.0])
    ```

    Store the **name** of the zone with the highest revenue of the week in
    `top_revenue_zone_ex60`.
    """
    )
    return


@app.cell
def _(np):
    avg_value = np.array([11.5, 14.0, 16.5, 19.0])
    return (avg_value,)


@app.cell
def _():
    # YOUR CODE BELOW: the name of the zone with the highest revenue (orders times average order value)
    top_revenue_zone_ex60 = None
    return (top_revenue_zone_ex60,)


@app.cell(hide_code=True)
def _(mo, show_result, top_revenue_zone_ex60):
    if top_revenue_zone_ex60 is None:
        _ok = False
        _msg = "Not attempted (Bonus). Assign it to `top_revenue_zone_ex60` (a `print` alone doesn't count) and run the cell."
    elif not isinstance(top_revenue_zone_ex60, str):
        _ok = False
        _msg = "Wrong (Bonus): the answer is a zone **name**, a string."
    elif top_revenue_zone_ex60 == "Hafen":
        _ok = True
        _msg = "Correct (Bonus): **Hafen** earns the most, 1,650 EUR, ahead of Nord with 1,621.50, although Nord has 41 more orders. The headline depends on what you count."
    elif top_revenue_zone_ex60 == "Nord":
        _ok = False
        _msg = "Wrong (Bonus): Nord has the most **orders**. Revenue is orders times what an order is worth, and that differs by zone."
    elif top_revenue_zone_ex60 == "Altstadt":
        _ok = False
        _msg = "Wrong (Bonus): Altstadt has the most valuable **single** order. Revenue also depends on how many orders a zone has."
    else:
        _ok = False
        _msg = "Wrong (Bonus): not the zone with the highest revenue. Multiply each zone's orders by its average order value, then find the largest."
    mo.callout(mo.md(_msg + show_result(top_revenue_zone_ex60)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus: the discount ladder (not required)

    Tobi wants to test five discounts on the 12.00 EUR bowl: evenly spaced from
    **0 % to 20 %**, both ends included. Store the five resulting prices, from
    full price down, as an array in `ladder_ex61`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the 12.00 EUR price after five evenly spaced discounts from 0 % to 20 %, as an array
    ladder_ex61 = None
    return (ladder_ex61,)


@app.cell(hide_code=True)
def _(ladder_ex61, mo, np):
    try:
        _arr = None if ladder_ex61 is None else np.asarray(ladder_ex61, dtype=float)
    except Exception:
        _arr = "bad"
    _preview = "" if ladder_ex61 is None else f"\n\n**Your result:** `{ladder_ex61}`"
    if _arr is None:
        _ok = False
        _msg = "Not attempted (Bonus). Assign it to `ladder_ex61` (a `print` alone doesn't count) and run the cell."
    elif isinstance(_arr, str) or _arr.shape != (5,):
        _ok = False
        _msg = "Wrong (Bonus): `ladder_ex61` should hold five prices."
    elif np.allclose(_arr, [12.0, 11.4, 10.8, 10.2, 9.6]):
        _ok = True
        _msg = "Correct (Bonus): 12.00, 11.40, 10.80, 10.20 and 9.60 EUR. Five evenly spaced discounts, applied to the price in one expression."
    elif np.allclose(_arr, [0.0, 0.05, 0.1, 0.15, 0.2]) or np.allclose(_arr, [0, 5, 10, 15, 20]):
        _ok = False
        _msg = "Wrong (Bonus): these are the five discounts. Tobi wants the five **prices** that result from them."
    elif np.allclose(_arr, [0.0, 0.6, 1.2, 1.8, 2.4]):
        _ok = False
        _msg = "Wrong (Bonus): these are the euros taken **off**. Store what the customer still pays."
    else:
        _ok = False
        _msg = "Wrong (Bonus): not the ladder. The first price is the full 12.00 EUR, the last one is 20 % off, and the steps in between are equal."
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus: the steady cells (not required)

    Every number in `week_sales` is one zone on one day. The investor calls such
    a cell "steady" when it has **at least 10 and at most 20 orders**. Store how
    many cells are steady in `steady_cells_ex62` (a plain `int`).
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: how many cells of week_sales hold at least 10 and at most 20 orders (a plain int)
    steady_cells_ex62 = None
    return (steady_cells_ex62,)


@app.cell(hide_code=True)
def _(kind_of, mo, numpy_note, show_result, steady_cells_ex62):
    _k = kind_of(steady_cells_ex62)
    if _k == "none":
        _ok = False
        _msg = "Not attempted (Bonus). Assign it to `steady_cells_ex62` (a `print` alone doesn't count) and run the cell."
    elif _k == "numpy":
        _ok = False
        _msg = numpy_note("Bonus", "steady_cells_ex62", steady_cells_ex62)
    elif _k != "int":
        _ok = False
        _msg = "Wrong (Bonus): the answer is a count of cells, so one plain `int`."
    elif steady_cells_ex62 == 16:
        _ok = True
        _msg = "Correct (Bonus): **16** of the 28 cells are steady. A mask works on a whole grid exactly as it does on one row."
    elif steady_cells_ex62 == 14:
        _ok = False
        _msg = "Wrong (Bonus): 14 leaves out the cells with exactly 10 or exactly 20 orders. \"At least\" and \"at most\" include both ends."
    else:
        _ok = False
        _msg = "Wrong (Bonus): not the number of steady cells. A cell is steady when it holds at least 10 and at most 20 orders."
    mo.callout(mo.md(_msg + show_result(steady_cells_ex62)), kind="success" if _ok else "warn")
    return


# ─────────────────────────────────────────────────────────────────────────
# PROGRESS + WRAP-UP
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(
    ex11_ok,
    ex12_ok,
    ex13_ok,
    ex21_ok,
    ex22_ok,
    ex23_ok,
    ex24_ok,
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell: the 8 core exercises plus the quiz (the trace and the bonuses don't count).
    _checks = [ex11_ok, ex12_ok, ex13_ok, ex21_ok, ex22_ok, ex23_ok, ex24_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _investor = (
        "The investor takes the one-pager and nods. No 40 tabs required."
        if _done == _total
        else "The investor is still waiting for the full page of metrics."
    )
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} correct** · {_investor}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave

    1. Check the progress box above: all **nine** green? If not, reread the
       worked examples, ask your AI assistant to explain the part that is
       stuck, and try again.
    2. Not finished? Finish at home **before the next session**. It opens with
       Checkpoint 4, which covers Episodes 6 and 7.
    3. **Download your work**: **Cmd/Ctrl+S**, then menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    4. Next episode: the investor opens a **data room**. A real file, eighty
       rows, more than anyone wants to type by hand. Tobi, naturally, lets an
       AI write his pandas. From then on the labs run in Zed, in the
       `python-labs` folder you made today. **Episode 8: the data room.**
    """
    )
    return


if __name__ == "__main__":
    app.run()
