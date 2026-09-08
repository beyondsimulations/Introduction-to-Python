# notebooks/nb_07_lab_metrics.py
# Episode 7 — The Numbers Deck. Session VII lab notebook.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 7.1 — The Numbers Deck
    **Estimated time: 45–60 min · Core exercises: 8 + 1 quiz (+ 1 trace)**

    The investor liked last week's honest numbers. Now she wants a **one-page
    metrics deck**: totals, a per-zone breakdown, the busiest day, the strongest
    zone, the kind of sheet you could slide across a table without apologizing.

    Tobi has *also* prepared a deck. It is a **40-tab spreadsheet** with a tab
    called `FINAL_final_v3` and one formula that references a cell in a workbook
    he can no longer find. It is, gently, disqualified.

    So this week you learn the tool that turns a pile of orders into metrics
    without a single hand-written loop: **NumPy**. A NumPy *array* is like a list
    that does math: multiply the whole thing at once, compare it to a number to
    get a filter, stack it into a grid and total it by row or by column. That's
    the entire deck, computed in a few honest lines.
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
# SECTION 1 — Arrays: a list that does math
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Arrays: a list that does math

    A **NumPy array** looks like a list, but it's built for numbers. You make one
    from a list with `np.array([...])`, and it comes with handy facts about
    itself:

    ```python
    import numpy as np
    prices = np.array([3, 8, 5, 9])
    prices.size    # 4: how many elements
    prices.shape   # (4,): its dimensions
    prices.dtype   # int64: the type of every element (int32 in the browser)
    ```

    Two more moves you'll use constantly:

    - **Vectorized math**: `prices * 2` multiplies *every* element at once, no
      loop. That's the whole point of an array.
    - **`np.arange(start, stop)`**: builds an array of whole numbers from `start`
      up to *but not including* `stop`, like `range`, but an array you can total.

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this). It also imports numpy as np for everything below
    import numpy as np
    _demo = np.array([3, 8, 5, 9])
    print("array:", _demo)
    print(".size:", _demo.size, " .shape:", _demo.shape, " .dtype:", _demo.dtype)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — how many orders?

    Here are the individual order values (in euros) from one busy week:

    ```python
    orders_list = [8.5, 11.0, 14.5, 7.5, 22.5, 16.0, 19.5, 13.5, 25.0, 10.5, 27.0, 21.5]
    ```

    First turn that Python list into a NumPy array called `orders_week` (with
    `np.array(...)`). Then, instead of counting by hand, ask the array how many
    elements it holds and store that count in `n_orders_ex11`. Use
    `int(orders_week.size)` so it's a plain whole number.
    """
    )
    return


@app.cell
def _():
    orders_list = [8.5, 11.0, 14.5, 7.5, 22.5, 16.0, 19.5, 13.5, 25.0, 10.5, 27.0, 21.5]
    return (orders_list,)


@app.cell
def _():
    # YOUR CODE BELOW: turn orders_list into a NumPy array with np.array(...)
    orders_week = None
    return (orders_week,)


@app.cell
def _():
    # YOUR CODE BELOW: the number of orders, as a plain int via int(orders_week.size)
    n_orders_ex11 = None
    return (n_orders_ex11,)


@app.cell(hide_code=True)
def _(mo, n_orders_ex11, np, show_result):
    if n_orders_ex11 is None:
        ex11_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(n_orders_ex11)
        try:
            _n = int(n_orders_ex11)
        except (TypeError, ValueError):
            _n = None
        if _n is None:
            ex11_ok = False
            if np.ndim(n_orders_ex11) > 0:
                _msg = "❌ Exercise 1.1: that's still a whole array. `.size` is a single number. Wrap `int(...)` around `orders_week.size`."
            else:
                _msg = "❌ Exercise 1.1: this should be a whole **number**: the order count from `int(orders_week.size)`."
        elif _n == 12:
            ex11_ok = True
            _msg = "✅ Exercise 1.1: **12** orders. `.size` counts the elements for you, one honest number, no tallying by hand."
        else:
            ex11_ok = False
            _msg = f"❌ Exercise 1.1: expected 12, got {_n}. Was `orders_week` built from the *whole* list? `.size` should report 12."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Two steps in two cells: first `orders_week = np.array(orders_list)`, then ask that array for its `.size` and wrap `int(...)` around it.",
            "💡 Hint 2 (the structure)": "orders_week = np.array(___)\nn_orders_ex11 = int(orders_week.___)   (put the list in the first blank, and `size` in the second)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — happy hour, all at once

    Happy hour knocks **10% off** every price. Here are four menu prices:

    ```python
    hh_prices = np.array([6.0, 9.0, 12.0, 18.0])
    ```

    Taking 10% off means keeping 90%, so multiply by `0.9`. Do it to the **whole
    array in one expression** (no loop, no indexing) and store the result in
    `sale_ex12`.
    """
    )
    return


@app.cell
def _(np):
    # Worked example (read + run this): one multiply touches every element
    _demo = np.array([10.0, 20.0, 50.0])
    print("half price:", _demo * 0.5)   # [ 5. 10. 25.]
    return


@app.cell
def _(np):
    hh_prices = np.array([6.0, 9.0, 12.0, 18.0])
    return (hh_prices,)


@app.cell
def _():
    # YOUR CODE BELOW: 10% off every price, in ONE expression (keep 90%)
    sale_ex12 = None
    return (sale_ex12,)


@app.cell(hide_code=True)
def _(mo, np, sale_ex12, show_result):
    _expected = [5.4, 8.1, 10.8, 16.2]
    if sale_ex12 is None:
        ex12_ok = False
        _msg = "🔲 Exercise 1.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(sale_ex12)
        try:
            _arr = np.asarray(sale_ex12, dtype=float)
        except (TypeError, ValueError):
            _arr = None
        if _arr is None:
            ex12_ok = False
            _msg = "❌ Exercise 1.2: this should be an **array of prices**. Multiply the whole `hh_prices` array by `0.9`."
        elif _arr.shape != (4,):
            ex12_ok = False
            _msg = "❌ Exercise 1.2: expected four sale prices, one per item. Multiply the *whole* `hh_prices` array by `0.9`, no loop, no indexing."
        elif np.allclose(np.round(_arr, 2), _expected):
            ex12_ok = True
            _msg = "✅ Exercise 1.2: 10% off, all four at once: `[5.4, 8.1, 10.8, 16.2]`. That's vectorization: one expression reaches every element."
        else:
            ex12_ok = False
            _msg = "❌ Exercise 1.2: not the 10%-off prices. Happy hour keeps 90% of each: `hh_prices * 0.9`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "You don't touch elements one at a time. Multiply the entire `hh_prices` array by a single number and NumPy applies it everywhere.",
            "💡 Hint 2 (the structure)": "sale_ex12 = hh_prices * ___   (the blank is the fraction of the price you keep after 10% off)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.3 (core) — the campaign calendar

    The flyer campaign runs for **14 days**, numbered 1 through 14. Build those day
    numbers with `np.arange`. Remember it stops *before* the second number, so
    reaching 14 means going up to **15**. Then total them (the array's `.sum()`)
    and store that total, as a plain `int`, in `days_sum_ex13`.

    First build the array `days = np.arange(1, 15)`, then compute the sum.
    """
    )
    return


@app.cell
def _(np):
    # Worked example (read + run this): arange stops BEFORE the second number
    _demo = np.arange(2, 7)
    print("np.arange(2, 7):", _demo, " sum:", _demo.sum())  # [2 3 4 5 6] sum: 20
    return


@app.cell
def _():
    # YOUR CODE BELOW: the 14 campaign days, 1 through 14, with np.arange
    days = None
    return (days,)


@app.cell
def _():
    # YOUR CODE BELOW: the total of all the day numbers, as a plain int
    days_sum_ex13 = None
    return (days_sum_ex13,)


@app.cell(hide_code=True)
def _(days_sum_ex13, mo, np, show_result):
    if days_sum_ex13 is None:
        ex13_ok = False
        _msg = "🔲 Exercise 1.3: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(days_sum_ex13)
        try:
            _s = int(days_sum_ex13)
        except (TypeError, ValueError):
            _s = None
        if _s is None:
            ex13_ok = False
            if np.ndim(days_sum_ex13) > 0:
                _msg = "❌ Exercise 1.3: that's still an array. `.sum()` collapses it to one number. Wrap `int(...)` around `days.sum()`."
            else:
                _msg = "❌ Exercise 1.3: this should be a whole **number**, the total of the day numbers."
        elif _s == 105:
            ex13_ok = True
            _msg = "✅ Exercise 1.3: **105**: the days 1 through 14 add up. `np.arange(1, 15)` stops before 15, so it lands exactly on 14."
        elif _s == 120:
            ex13_ok = False
            _msg = "❌ Exercise 1.3: 120 means you summed 1 through 15. `np.arange` stops *before* its second number, so `np.arange(1, 15)` gives 1…14, not 1…15."
        else:
            ex13_ok = False
            _msg = "❌ Exercise 1.3: not the expected total. Build `np.arange(1, 15)` (days 1 through 14) and take its `.sum()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex13_ok else "warn")
    return (ex13_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`np.arange(1, 15)` builds 1 through 14 (it stops before 15). Store that in `days`, then ask the array for its `.sum()` and wrap `int(...)` around it.",
            "💡 Hint 2 (the structure)": "days = np.arange(1, ___)\ndays_sum_ex13 = int(days.___())   (the blank stop is one past the last day; the method totals the array)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Masks: counting and filtering without a loop
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Masks: counting and filtering without a loop

    Compare an array to a number and you don't get one `True`/`False`. You get a
    whole array of them, one per element. That boolean array is a **mask**, and
    it's how you count and filter without writing a loop:

    ```python
    speeds = np.array([5, 12, 3, 20])
    speeds > 10            # array([False,  True, False,  True])
    (speeds > 10).sum()    # 2: True counts as 1, so .sum() counts the hits
    speeds[speeds > 10]    # array([12, 20]): keep only the matching values
    ```

    So `(array > n).sum()` **counts** how many pass, and `array[array > n]`
    **keeps** the ones that do, ready for `.mean()` or `.sum()`.

    > One marimo habit for this section: array math and indexing are easy to get
    > slightly wrong, and a **red error pauses everything below it**, including
    > the progress box. Nothing is lost; fix the red cell and it all comes back.

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _(np):
    # Worked example (read + run this): mask, count, filter
    _demo = np.array([5, 12, 3, 20])
    print("mask:", _demo > 10)
    print("count over 10:", (_demo > 10).sum())
    print("the values over 10:", _demo[_demo > 10])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core) — count the critical runs

    Here are ten delivery times, in minutes:

    ```python
    delivery_times = np.array([24, 39, 55, 17, 31, 46, 20, 60, 35, 42])
    ```

    Anything **over 50 minutes** is "critical" and goes on the deck as a risk.
    Count how many deliveries were critical and store that whole number in
    `critical_count_ex21` (use `int(...)` so it's a plain count).
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
    critical_count_ex21 = None
    return (critical_count_ex21,)


@app.cell(hide_code=True)
def _(critical_count_ex21, mo, np, show_result):
    if critical_count_ex21 is None:
        ex21_ok = False
        _msg = "🔲 Exercise 2.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(critical_count_ex21)
        try:
            _c = int(critical_count_ex21)
        except (TypeError, ValueError):
            _c = None
        if _c is None:
            ex21_ok = False
            if np.ndim(critical_count_ex21) > 0:
                _msg = "❌ Exercise 2.1: that's still a True/False array. `.sum()` turns the mask into one number by counting the Trues. Then wrap `int(...)`."
            else:
                _msg = "❌ Exercise 2.1: this should be a whole **number** of critical deliveries. Start from the mask `delivery_times > 50`."
        elif _c == 2:
            ex21_ok = True
            _msg = "✅ Exercise 2.1: **2** critical runs (the 55 and the 60). `(delivery_times > 50).sum()` counted them without a loop."
        else:
            ex21_ok = False
            _msg = f"❌ Exercise 2.1: expected 2, got {_c}. Count where the times exceed 50: `(delivery_times > 50).sum()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "First make the mask `delivery_times > 50` (a True/False array), then `.sum()` counts the Trues. Wrap the whole thing in `int(...)`.",
            "💡 Hint 2 (the structure)": "critical_count_ex21 = int((delivery_times > ___).sum())   (the blank is the threshold in minutes)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — the on-time rate

    One more trick hides in the mask: take its **`.mean()`**. `True` counts as 1
    and `False` as 0, so a True/False array's `.mean()` is the **share of Trues**:
    count ÷ total in one call. The investor loves percentages.

    A delivery is **on time** when it takes **50 minutes or less**. Using the same
    `delivery_times`, compute the share of deliveries that were on time and store
    it in `ontime_rate_ex22` as a plain `float` (a number between 0 and 1).
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the share of delivery_times that are 50 or less, as a float
    ontime_rate_ex22 = None
    return (ontime_rate_ex22,)


@app.cell(hide_code=True)
def _(mo, np, ontime_rate_ex22, show_result):
    if ontime_rate_ex22 is None:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(ontime_rate_ex22)
        try:
            _r = round(float(ontime_rate_ex22), 2)
        except (TypeError, ValueError):
            _r = None
        if _r is None:
            ex22_ok = False
            if np.ndim(ontime_rate_ex22) > 0:
                _msg = "❌ Exercise 2.2: that's still an array, probably the raw mask. `.mean()` collapses it to one number: the share of Trues."
            else:
                _msg = "❌ Exercise 2.2: this should be a single **number** between 0 and 1: the share of on-time deliveries."
        elif _r == 0.8:
            ex22_ok = True
            _msg = "✅ Exercise 2.2: **0.8**, or 80% of deliveries on time. A True/False array's `.mean()` is count ÷ total in one call; exactly the percentage the investor wants on the deck."
        elif _r in (2, 8):
            ex22_ok = False
            _msg = "❌ Exercise 2.2: that's the **count**. The rate is count ÷ total, and `.mean()` on the mask does that division for you."
        elif _r == 0.2:
            ex22_ok = False
            _msg = "❌ Exercise 2.2: 0.2 is the **late** share. That mask catches the over-50 times. On-time is 50 minutes *or less*: `delivery_times <= 50`."
        else:
            ex22_ok = False
            _msg = "❌ Exercise 2.2: not the expected rate. Take the mean of the on-time mask: `(delivery_times <= 50).mean()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Build the on-time mask first (50 or less, mind the `<=`), then take its `.mean()`: with Trues worth 1 and Falses worth 0, the mean IS the share. Wrap `float(...)` around it.",
            "💡 Hint 2 (the structure)": "ontime_rate_ex22 = float((delivery_times <= ___).___())   (the blank threshold matches 2.1; the method turns the mask into a share)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core, fix the bug) — Tobi's per-zone totals

    Tobi's spreadsheet was really a **grid**: seven days down the side, four zones
    across the top. As an array it's `week_grid` below: 7 rows, 4 columns.

    A 2-D array totals along an **axis**. `axis=0` runs *down the rows* (giving one
    total per column); `axis=1` runs *across the columns* (giving one total per
    row):

    ```python
    small = np.array([[1, 2, 3],
                      [4, 5, 6]])
    small.sum(axis=0)   # array([5, 7, 9]): one total per column (down the rows)
    small.sum(axis=1)   # array([6, 15]): one total per row (across the columns)
    ```

    The investor asked for **four zone totals**, one number per zone. Tobi sent
    her **seven** numbers. Here's the line he ran:

    ```python
    # Tobi's memo (this is what he ran, not something to run yourself):
    tobi_totals = week_grid.sum(axis=1)
    # tobi_totals → [59, 65, 58, 65, 61, 72, 52]   (seven numbers, not four)
    ```

    Store the *correct* per-zone totals (four numbers, one per zone) in
    `zone_totals_ex23`.
    """
    )
    return


@app.cell
def _(np):
    week_grid = np.array(
        [
            [20, 12, 18, 9],
            [25, 15, 14, 11],
            [18, 20, 12, 8],
            [22, 14, 16, 13],
            [19, 18, 10, 14],
            [21, 16, 20, 15],
            [16, 14, 10, 12],
        ]
    )
    return (week_grid,)


@app.cell
def _():
    # YOUR CODE BELOW: the FOUR per-zone totals (one number per zone)
    zone_totals_ex23 = None
    return (zone_totals_ex23,)


@app.cell(hide_code=True)
def _(mo, np, show_result, zone_totals_ex23):
    _expected = [141, 109, 100, 82]
    if zone_totals_ex23 is None:
        ex23_ok = False
        _msg = "🔲 Exercise 2.3: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(zone_totals_ex23)
        try:
            _arr = np.asarray(zone_totals_ex23, dtype=float)
        except (TypeError, ValueError):
            _arr = None
        if _arr is None:
            ex23_ok = False
            _msg = "❌ Exercise 2.3: this should be four zone totals (numbers). Total the grid along one axis."
        elif _arr.shape == (7,):
            ex23_ok = False
            _msg = "❌ Exercise 2.3: seven numbers. That's Tobi's bug. You totaled *across the zones* (one number per DAY, `axis=1`). The investor wants one number per ZONE: total *down the days* instead."
        elif _arr.shape != (4,):
            ex23_ok = False
            _msg = "❌ Exercise 2.3: expected exactly four zone totals, one per column. Total the grid down its seven days."
        elif np.allclose(np.round(_arr, 2), _expected):
            ex23_ok = True
            _msg = "✅ Exercise 2.3: `[141, 109, 100, 82]`: four zones, four numbers. Totaling *down the days* (the other axis) is what the investor actually asked for."
        else:
            ex23_ok = False
            _msg = "❌ Exercise 2.3: four numbers, but not the expected totals. Sum each column of `week_grid` down its seven days."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Tobi summed across each row (a per-day total). You want a per-column total instead, the *other* axis. Which axis runs down the rows?",
            "💡 Hint 2 (the structure)": "zone_totals_ex23 = week_grid.sum(axis=___)   (pick the axis that leaves one number per zone, per column, not per day)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — Two dimensions: the deck comes together
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — Two dimensions: the deck comes together

    Here's the real week as a grid (`week_sales`, 7 days down, 4 zones across),
    and the zone names in `zones`, left to right:

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

    Same `axis` idea as Tobi's fix: `axis=1` totals **across the zones** (one
    number per day), `axis=0` totals **down the days** (one number per zone).
    Two metrics left on the deck. Let's compute both.
    """
    )
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
    ### Exercise 3.1 (core) — the busiest day

    "Which day was busiest?" is really: total each day across its four zones
    (`axis=1`), then take the biggest of those seven day-totals (`.max()`). Store
    that single busiest-day total, as a plain `int`, in `best_day_total_ex31`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: total each day across zones, then the biggest total (int)
    best_day_total_ex31 = None
    return (best_day_total_ex31,)


@app.cell(hide_code=True)
def _(best_day_total_ex31, mo, np, show_result):
    if best_day_total_ex31 is None:
        ex31_ok = False
        _msg = "🔲 Exercise 3.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(best_day_total_ex31)
        try:
            _t = int(best_day_total_ex31)
        except (TypeError, ValueError):
            _t = None
        if _t is None:
            ex31_ok = False
            if np.ndim(best_day_total_ex31) > 0:
                _msg = "❌ Exercise 3.1: that's still an array. You have all seven day totals. `.max()` picks the single biggest one; then wrap `int(...)`."
            else:
                _msg = "❌ Exercise 3.1: this should be one whole **number**, the busiest day's total."
        elif _t == 84:
            ex31_ok = True
            _msg = "✅ Exercise 3.1: **84**, the busiest day. You totaled each day across its zones (`axis=1`), then took the max."
        elif _t == 141:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: 141 is the biggest *zone* total (totaling down the days, `axis=0`). The busiest DAY totals across the four zones (`axis=1`), then takes the max."
        else:
            ex31_ok = False
            _msg = f"❌ Exercise 3.1: expected 84, got {_t}. Total each day across its zones, then take the max: `week_sales.sum(axis=1).max()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex31_ok else "warn")
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "First get one total per day by summing across the zones (`axis=1`). That's seven numbers. Then `.max()` picks the busiest, and `int(...)` makes it plain.",
            "💡 Hint 2 (the structure)": "best_day_total_ex31 = int(week_sales.sum(axis=___).max())   (the axis totals *across* each day's zones)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 🏆 Boss exercise (core) — which zone wins the week?

    The headline metric: **which zone sold the most all week?** You already fixed
    this computation in Exercise 2.3: total down the days (`axis=0`) to get the
    four zone totals. Now go one step further: find *which* zone is biggest with
    **`.argmax()`** (it gives the *position* of the largest value, `0`–`3`), and
    use that position to look up the name in `zones`.

    Store the winning zone's **name** (a string like `"Hafen"`) in `best_zone_ex40`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the NAME of the zone with the highest all-week total
    best_zone_ex40 = None
    return (best_zone_ex40,)


@app.cell(hide_code=True)
def _(best_zone_ex40, mo, np, show_result):
    if best_zone_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
        _preview = ""
    elif isinstance(best_zone_ex40, str):
        _preview = show_result(best_zone_ex40)
        _v = best_zone_ex40.strip()
        if _v == "Nord":
            ex40_ok = True
            _msg = "✅ Boss exercise: **Nord** wins the week with 141. `argmax` turned the four zone totals into a position, and indexing `zones` turned that position into the name. 🏆"
        elif _v in {"Sued", "Hafen", "Altstadt"}:
            ex40_ok = False
            _msg = "❌ Boss exercise: that zone isn't the weekly winner. Total down the days (`axis=0`) for the four zone totals, then `argmax` to find the biggest, and index `zones` with it."
        else:
            ex40_ok = False
            _msg = "❌ Boss exercise: that isn't one of the four zone names. `zones[...]` should give 'Nord', 'Sued', 'Hafen' or 'Altstadt'."
    elif np.ndim(best_zone_ex40) > 0:
        ex40_ok = False
        _preview = show_result(best_zone_ex40)
        _msg = "❌ Boss exercise: that's still an array. You want a single zone **name**: index `zones` with the `argmax` position."
    else:
        ex40_ok = False
        _preview = show_result(best_zone_ex40)
        _msg = "❌ Boss exercise: that looks like a number, probably the `argmax` position. Use it to look up the name: `zones[that_position]`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Three moves: total down the days (`axis=0`) for four zone totals, ask `.argmax()` for the position of the biggest, then index `zones` with that position to get the name.",
            "💡 Hint 2 (the structure)": "best_zone_ex40 = zones[int(week_sales.sum(axis=___).argmax())]   (the axis totals each zone down the seven days)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# TRACE + MCQ
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise (trace — predict first) — an array is not a list

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
        _msg = "🔲 Pick a prediction above first. Commit before you peek!"
    elif trace_repeat.value == "[2 4 6]":
        _msg = (
            "✅ Correct: **`[2 4 6]`**. On a NumPy array, `* 2` *doubles every "
            "element*; on the plain list in the lecture it *repeated* the list. "
            "Lists repeat; arrays compute, which is exactly why this episode uses "
            "arrays. (Arrays print without commas.)"
        )
    else:
        _msg = (
            "❌ Not quite: it's **`[2 4 6]`**. `* 2` on a NumPy *array* hits every "
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
    ### Quiz (core, MCQ) — reading a mask

    You used masks all through Section 2. Given the delivery times, what does this
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
        _msg = "🔲 Quiz: not attempted yet."
    elif str(answer_ex50).strip().lower() == "d":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **d**. `delivery_times > 40` is a True/False mask; `True` "
            "counts as 1, so `.sum()` counts how many times cleared 40: a count, "
            "not a total or a maximum."
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. `delivery_times > 40` makes a True/False mask, and "
            "summing Trues (each worth 1) *counts* them. It doesn't total the "
            "times or find the biggest."
        )
    mo.md(_msg)
    return (ex50_ok,)


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
    ex31_ok,
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell: the 8 core exercises plus the quiz (the trace doesn't count).
    _checks = [ex11_ok, ex12_ok, ex13_ok, ex21_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _investor = (
        "The investor takes the one-pager and nods. No 40 tabs required."
        if _done == _total
        else "The investor is still waiting for the full page of metrics."
    )
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} ✅** · {_investor}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave 📊

    1. Check the progress box above: all **nine** green? If not, reopen the hints,
       reread the worked examples, and try again. Arrays, masks and axis totals are
       the whole toolkit for turning raw numbers into a metric. You'll reach for
       them any time data shows up.
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. Next episode: the investor opens a **data room**. A real file, eighty
       rows, more than anyone wants to type by hand. Tobi, naturally, lets an
       AI write his pandas. **Episode 8: the data room.**
    """
    )
    return


if __name__ == "__main__":
    app.run()
