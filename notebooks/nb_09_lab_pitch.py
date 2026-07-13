# notebooks/nb_09_lab_pitch.py
# Episode 9 — The Pitch Deck. Session IX lab notebook.
# Built from notebooks/nb_08_lab_dataroom.py (same-dataset predecessor) and the
# ex_09_a/b/c chart family (spec §4 rules apply): one global name per cell;
# += counts as a definition; every exercise pre-defines its answer (None);
# suffix exercise names (_exNM); underscore-prefixed names are cell-private;
# never a possible infinite loop. First lab that draws charts: matplotlib runs
# in the browser (pyodide) exactly like pandas — one import cell, then every
# chart cell opens with plt.figure() and CLOSES with plt.gca() (marimo shows the
# last expression; never plt.show(), which does nothing here). Checks are
# crash-proof: every coercion is guarded and Series/DataFrame answers degrade to
# a message instead of raising. Charts are UNGRADED (the check reads the number,
# not the art); `orders` is never mutated (derived data uses copies / new names).
#
# ledger (all values computed FROM notebooks/public/orders.csv — cross-checked
# against helpers/make_orders_csv.py; NOTE: (total_eur > 25).sum() is 20, not the
# 13 an early draft assumed — 13 is the count above 26, there is a value gap
# between 25.2 and 30.6):
#   daily = orders.groupby("day")["total_eur"].sum()
#       daily.idxmax()                                = 3   (peak day, 158.3 €)
#       daily.idxmin()                                = 6   (trough day, 51.7 €)
#       len(daily)                                    = 14  (two weeks of days)
#   orders.groupby("zone")["total_eur"].sum().round(2).to_dict()
#       = {'Altstadt': 408.4, 'Hafen': 354.2, 'Nord': 378.9, 'Sued': 430.1}
#   (orders["total_eur"] > 25).sum()                  = 20  (top-quartile tail)
#   (orders["total_eur"] > 20).sum()                  = 43  (>half — NOT a tail)
#   orders["delivery_min"].max()                      = 58
#   corr(delivery_min, total_eur)                     = -0.03  (no relationship)
#   week1 = orders[orders["day"] <= 7]["total_eur"].sum()  = 788.4
#   week2 = orders[orders["day"] >= 8]["total_eur"].sum()  = 783.2
#       (week2 - week1) / week1 * 100                 = -0.66  (essentially flat)
#   orders["total_eur"].sum()                         = 1571.6
#   groupby zone total .idxmax() (highest TOTAL)      = "Sued"
#   len(orders)                                       = 80
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 9.1 — The Pitch Deck
    **Estimated time: 45–60 min · Core exercises: 7 + 1 quiz (+ 1 trace)**

    The pitch meeting is **Friday**. Last week you turned the data room into
    honest numbers; this week those numbers have to be *seen*. The investor gave
    exactly one instruction, and she meant it as a warning:

    > **"Bring me charts I can't argue with."**

    A chart you *can* argue with is worse than no chart: it's the thing that
    sinks a pitch. So this week is two skills at once: draw the right chart for
    the question, and refuse to draw a dishonest one. Same eighty orders, same
    `orders` DataFrame, now with a picture attached.

    Kevin, naturally, has already "built the deck". His growth slide looks
    *incredible*. Your job, again, is to **supervise**: some of his charts are
    lies wearing a nice axis, and you're the one who catches them before the
    investor does.

    Two marimo habits for every chart in this notebook:

    - A chart cell **opens** with `plt.figure()` — a fresh canvas, so this chart
      doesn't draw on top of the last one.
    - A chart cell **ends** with `plt.gca()` ("get current axes") — the last
      expression is what marimo shows. Never `plt.show()`; in the browser it
      just does nothing.

    > **If the notebook fails to boot with a network error** (or the first cell
    > that imports `pandas` or `matplotlib` complains it can't be imported),
    > **reload the page once** (Cmd/Ctrl + R). The first load fetches those
    > libraries over the network and can flake; a reload almost always fixes it.

    > One more marimo habit worth naming: a typo in a column name (or a chart
    > that errors) turns the cell **red and pauses everything below it**,
    > including the progress box. Nothing is lost. Fix the red cell and it all
    > comes back.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell(hide_code=True)
def _(mo, pd):
    _loc = mo.notebook_location() / "public" / "orders.csv"
    orders = pd.read_csv(str(_loc))
    return (orders,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell(hide_code=True)
def _():
    # Helper — echoes a student's current answer as a "Your result" preview so
    # they SEE their output, not just ✅/❌. Strings render in a fenced block;
    # everything else inline. See _template.py.
    def show_result(value):
        if value is None:
            return ""
        if isinstance(value, str):
            return f"\n\n**Your result:**\n\n```\n{value}\n```"
        return f"\n\n**Your result:** `{value}`"

    return (show_result,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — The first chart
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — The first chart

    The pitch opens with momentum: **revenue, day by day.** You already know how
    to get one number per group: that was `groupby` last week. Here the group is
    the **day**, so the given cell below hands you a `daily` Series: one revenue
    total for each of the fourteen days.

    A time series like this wants a **line chart**: `plt.plot(x, y)` connects the
    dots so the eye follows the trend. Read the worked example, then draw the real
    one.
    """
    )
    return


@app.cell
def _(plt):
    # Worked example (read + run this) — a line chart, figure() to gca()
    _demo_days = [1, 2, 3]
    _demo_revenue = [90, 60, 140]
    plt.figure()  # starts a fresh figure — keeps this chart off the previous one
    plt.plot(_demo_days, _demo_revenue)
    plt.title("Demo: three days of revenue")
    plt.gca()  # the last expression is what marimo shows — never plt.show()
    return


@app.cell
def _(orders):
    # Given — do not change this. Daily revenue: one total per day (days 1–14).
    daily = orders.groupby("day")["total_eur"].sum()
    return (daily,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — the peak day

    Plot `daily` as a line chart in the cell below (that's the picture — it isn't
    graded). Then read it for the investor: **which day brought in the most
    revenue?** Don't eyeball the chart. Ask the Series. `daily.idxmax()` returns
    the *label* of its largest value (here, a day number). Store that day, as a
    plain `int`, in `best_day_ex11`.
    """
    )
    return


@app.cell
def _(daily, plt):
    plt.figure()
    # YOUR CODE BELOW — plot daily as a line (title/labels optional, ungraded)
    plt.gca()
    return


@app.cell
def _():
    # YOUR CODE BELOW — the day number with the highest revenue, as a plain int
    best_day_ex11 = None
    return (best_day_ex11,)


@app.cell(hide_code=True)
def _(best_day_ex11, mo, pd, show_result):
    if best_day_ex11 is None:
        ex11_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(best_day_ex11)
        if isinstance(best_day_ex11, (pd.Series, pd.DataFrame)):
            ex11_ok = False
            _msg = "❌ Exercise 1.1: that's still the whole `daily` table. `.idxmax()` collapses it to one label — the day. Then wrap `int(...)`."
        else:
            try:
                _n = int(best_day_ex11)
            except (TypeError, ValueError):
                _n = None
            if _n is None:
                ex11_ok = False
                _msg = "❌ Exercise 1.1: this should be a whole **number** — the day with the highest revenue, from `int(daily.idxmax())`."
            elif _n == 3:
                ex11_ok = True
                _msg = "✅ Exercise 1.1: **day 3** — the peak, at 158.3 €. `.idxmax()` reads the winning *label* off the Series; no squinting at the line."
            elif _n == 6:
                ex11_ok = False
                _msg = "❌ Exercise 1.1: day 6 is the *trough* (the lowest day, 51.7 €) — that's `.idxmin()`. You want `.idxmax()` for the peak."
            elif _n == 158 or round(float(best_day_ex11), 1) == 158.3:
                ex11_ok = False
                _msg = "❌ Exercise 1.1: 158.3 is the euro *amount* on the best day — that's `.max()`. The investor asked *which day*: `.idxmax()` returns the label."
            else:
                ex11_ok = False
                _msg = f"❌ Exercise 1.1: expected 3, got {_n}. `daily.idxmax()` returns the day with the biggest total."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`plt.plot(daily.index, daily.values)` draws the line for your eyes — the check only reads the number. `.max()` gives the biggest VALUE; `.idxmax()` gives its LABEL (the day), which is what the investor asked for.",
            "💡 Hint 2 (the structure)": "best_day_ex11 = int(daily.___())   — the method that returns the label (not the value) of the largest entry.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — chart anatomy

    A line with no labels is a Rorschach test: the investor shouldn't have to
    guess what the axes mean. Go back to your chart above (or copy it into the
    cell below) and give it the three parts every honest chart carries:

    - `plt.xlabel("Day")` — what the horizontal axis counts,
    - `plt.ylabel("Revenue (€)")` — what the vertical axis measures,
    - `plt.title("Daily revenue")` — what the whole picture is about.

    That's aesthetics, and it isn't graded. The graded question is a fact about
    the axis you just labeled: **how many days** does the chart span? `daily` has
    one entry per day, so `len(daily)` counts them. Store it, as a plain `int`, in
    `days_ex12`.
    """
    )
    return


@app.cell
def _(daily, plt):
    plt.figure()
    # YOUR CODE BELOW — plot daily again, now with xlabel / ylabel / title (ungraded)
    plt.gca()
    return


@app.cell
def _():
    # YOUR CODE BELOW — how many days the chart spans, as a plain int
    days_ex12 = None
    return (days_ex12,)


@app.cell(hide_code=True)
def _(days_ex12, mo, pd, show_result):
    if days_ex12 is None:
        ex12_ok = False
        _msg = "🔲 Exercise 1.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(days_ex12)
        if isinstance(days_ex12, (pd.Series, pd.DataFrame)):
            ex12_ok = False
            _msg = "❌ Exercise 1.2: that's still the whole `daily` table — you want one number. `len(daily)` counts its entries."
        else:
            try:
                _n = int(days_ex12)
            except (TypeError, ValueError):
                _n = None
            if _n is None:
                ex12_ok = False
                _msg = "❌ Exercise 1.2: this should be a whole **number** — the count of days, from `int(len(daily))`."
            elif _n == 14:
                ex12_ok = True
                _msg = "✅ Exercise 1.2: **14** days — two full weeks, one point per day. `len(daily)` counts the entries, and now the axes say so out loud."
            elif _n == 80:
                ex12_ok = False
                _msg = "❌ Exercise 1.2: 80 is the number of *orders* (`len(orders)`). `daily` already grouped those down to one row per day — count `daily`, not `orders`."
            else:
                ex12_ok = False
                _msg = f"❌ Exercise 1.2: expected 14, got {_n}. `len(daily)` counts the days in the grouped Series."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`daily` has one entry per day, so its length IS the number of days. `len(...)` counts entries of a Series exactly like a list. Wrap `int(...)`.",
            "💡 Hint 2 (the structure)": "days_ex12 = int(len(___))   — the blank is the grouped Series with one row per day.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — The right chart
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — The right chart

    A line was right for days, because days are a *timeline*. Most questions
    aren't. The skill this section drills is **matching the chart to the
    question**, because the wrong chart is its own kind of lie:

    - **Categories** (zones, dishes) → **bar chart** — `plt.bar(labels, heights)`.
    - **A distribution** (how one number spreads out) → **histogram** —
      `plt.hist(values)`.
    - **Two numbers per row, related or not** → **scatter** —
      `plt.scatter(x, y)`.

    Same `plt.figure()` … `plt.gca()` frame around each. Let's pick the right one
    three times.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core) — revenue by zone, as a picture

    You computed this exact breakdown in the data room last week: total revenue
    per zone. Now it becomes a **picture**. First rebuild the numbers: group by
    `zone`, sum `total_eur`, round to 2 decimals, and hand it over as a **plain
    dict** (zone → euros) in `by_zone_ex21`. Then plot those four totals as a bar
    chart (ungraded: the check reads the dict, not the bars).

    (If you end up with a Series instead of a dict, the check will nudge you.)
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — {zone: total_eur} dict, rounded to 2 decimals
    by_zone_ex21 = None
    return (by_zone_ex21,)


@app.cell
def _(by_zone_ex21, plt):
    plt.figure()
    # YOUR CODE BELOW — a bar chart of by_zone_ex21 (zones vs totals, ungraded)
    #   e.g. plt.bar(list(by_zone_ex21.keys()), list(by_zone_ex21.values()))
    plt.gca()
    return


@app.cell(hide_code=True)
def _(by_zone_ex21, mo, pd, show_result):
    _expected = {"Altstadt": 408.4, "Hafen": 354.2, "Nord": 378.9, "Sued": 430.1}
    if by_zone_ex21 is None:
        ex21_ok = False
        _msg = "🔲 Exercise 2.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(by_zone_ex21)
        if isinstance(by_zone_ex21, pd.Series):
            ex21_ok = False
            _msg = "❌ Exercise 2.1: that's a **Series**, not a dict — `.to_dict()` finishes the job. Add it to the end of your groupby."
        elif isinstance(by_zone_ex21, pd.DataFrame):
            ex21_ok = False
            _msg = "❌ Exercise 2.1: that's a whole table. Pick the `total_eur` column *before* summing: `.groupby(\"zone\")[\"total_eur\"].sum()`, then `.to_dict()`."
        elif not isinstance(by_zone_ex21, dict):
            ex21_ok = False
            _msg = "❌ Exercise 2.1: this should be a **dict** of zone → euros. Finish the groupby with `.round(2).to_dict()`."
        else:
            try:
                _got = {str(_k): round(float(_v), 2) for _k, _v in by_zone_ex21.items()}
            except (TypeError, ValueError):
                _got = None
            if _got is None:
                ex21_ok = False
                _msg = "❌ Exercise 2.1: the values should be euro numbers. Group by `zone`, sum `total_eur`, then `.round(2).to_dict()`."
            elif _got == _expected:
                ex21_ok = True
                _msg = "✅ Exercise 2.1: four zones, four bars. Same numbers you found last week — now the tallest bar makes the winner obvious at a glance. That's what a chart is *for*."
            elif set(_got) != set(_expected):
                ex21_ok = False
                _msg = "❌ Exercise 2.1: the zones don't match — you should have exactly the four keys 'Altstadt', 'Hafen', 'Nord', 'Sued'. Group by `zone`."
            else:
                ex21_ok = False
                _msg = "❌ Exercise 2.1: right zones, wrong totals. Sum `total_eur` per group: `orders.groupby(\"zone\")[\"total_eur\"].sum().round(2).to_dict()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "This is the same chain you used in the data room: split the rows by category, total each group, then turn the Series into a clean dict. For the chart, a bar wants a list of labels and a list of heights.",
            "💡 Hint 2 (the structure)": 'by_zone_ex21 = orders.groupby("___")["total_eur"].sum().round(2).___()   — the group key is the zone column; the final method turns a Series into a dict.',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — the expensive tail, counted

    Now a *distribution* question: how are order values spread out? A histogram
    answers it: `plt.hist(orders["total_eur"])` drops every order into a euro
    bucket so you see the shape. Plot it (ungraded), then look: most orders cluster
    low, with a thinning tail of pricey ones on the right.

    The investor wants that tail *quantified*. Count the orders above **25 €** (the
    genuinely expensive ones) and store the count, as a plain `int`, in
    `over_25_ex22`.

    > Why 25 and not 20? More than half the orders already sit above 20 €. Calling
    > *half your data* a "tail" would misread the histogram. 25 € is where the
    > expensive stuff actually starts.
    """
    )
    return


@app.cell
def _(orders, plt):
    plt.figure()
    # YOUR CODE BELOW — a histogram of orders["total_eur"] (ungraded)
    plt.gca()
    return


@app.cell
def _():
    # YOUR CODE BELOW — how many orders have total_eur > 25, as a plain int
    over_25_ex22 = None
    return (over_25_ex22,)


@app.cell(hide_code=True)
def _(mo, over_25_ex22, pd, show_result):
    if over_25_ex22 is None:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(over_25_ex22)
        if isinstance(over_25_ex22, (pd.Series, pd.DataFrame)):
            ex22_ok = False
            _msg = "❌ Exercise 2.2: that's the True/False column itself — `.sum()` counts the `True`s. Then wrap `int(...)`."
        else:
            try:
                _c = int(over_25_ex22)
            except (TypeError, ValueError):
                _c = None
            if _c is None:
                ex22_ok = False
                _msg = "❌ Exercise 2.2: this should be a whole **number** — the count of orders above 25 €."
            elif _c == 20:
                ex22_ok = True
                _msg = "✅ Exercise 2.2: **20** orders above 25 € — a genuine top-quartile tail, one quarter of the eighty. That's the number the histogram was hinting at."
            elif _c == 43:
                ex22_ok = False
                _msg = "❌ Exercise 2.2: 43 is the count above *20 €* — more than half the orders. That's not a tail. The threshold is 25 €: `orders[\"total_eur\"] > 25`."
            elif _c == 80:
                ex22_ok = False
                _msg = "❌ Exercise 2.2: 80 is *every* order — you counted the whole column. Count only the ones where `total_eur > 25`."
            elif _c == 60:
                ex22_ok = False
                _msg = "❌ Exercise 2.2: 60 is the *cheap* majority (25 € or less) — you flipped the comparison. The tail is `> 25`, not `<= 25`."
            else:
                ex22_ok = False
                _msg = f"❌ Exercise 2.2: expected 20, got {_c}. Build the mask `orders[\"total_eur\"] > 25`, then `.sum()` counts the `True`s."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'A comparison on a column gives a `True`/`False` mask — one per row. `.sum()` counts the `True`s (each counts as 1). So `(orders["total_eur"] > 25).sum()` is the count you want; wrap `int(...)`.',
            "💡 Hint 2 (the structure)": 'over_25_ex22 = int((orders["total_eur"] > ___).sum())   — the blank is the euro threshold that separates the tail.',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core) — does slower mean bigger?

    Kevin has a theory: "big orders take longer, obviously." A **scatter** plot is
    how you check a claim like that. Two numbers per order, one on each axis:
    `plt.scatter(orders["delivery_min"], orders["total_eur"])`. Plot it (ungraded)
    and actually *look*.

    You'll see… nothing. No upward drift, no line, just a cloud. Delivery time and
    order value have essentially **no relationship** (the correlation is about
    −0.03, which is a fancy way of saying *zero*). That's a real finding, and the
    honest chart says so. Sometimes the answer is "there's no pattern here", and
    you never describe a trend that isn't on the screen.

    So drop Kevin's theory and report the fact the investor actually asked for:
    the **slowest delivery** in the whole dataset. Store that longest delivery time,
    as a plain `int`, in `slowest_ex23`.
    """
    )
    return


@app.cell
def _(orders, plt):
    plt.figure()
    # YOUR CODE BELOW — scatter of delivery_min (x) vs total_eur (y) (ungraded)
    plt.gca()
    return


@app.cell
def _():
    # YOUR CODE BELOW — the longest delivery time in minutes, as a plain int
    slowest_ex23 = None
    return (slowest_ex23,)


@app.cell(hide_code=True)
def _(mo, pd, show_result, slowest_ex23):
    if slowest_ex23 is None:
        ex23_ok = False
        _msg = "🔲 Exercise 2.3: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(slowest_ex23)
        if isinstance(slowest_ex23, (pd.Series, pd.DataFrame)):
            ex23_ok = False
            _msg = "❌ Exercise 2.3: that's still the whole column — `.max()` picks the single longest time. Then wrap `int(...)`."
        else:
            try:
                _n = int(slowest_ex23)
            except (TypeError, ValueError):
                _n = None
            if _n is None:
                ex23_ok = False
                _msg = "❌ Exercise 2.3: this should be a whole **number** of minutes — the longest delivery, from `int(orders[\"delivery_min\"].max())`."
            elif _n == 58:
                ex23_ok = True
                _msg = "✅ Exercise 2.3: **58 minutes** — the slowest delivery on record. And the scatter earned its keep: it showed there's *no* link between speed and order size. 'No pattern' is a finding too."
            else:
                ex23_ok = False
                _msg = f"❌ Exercise 2.3: expected 58, got {_n}. Take the biggest value of the delivery column: `int(orders[\"delivery_min\"].max())`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'The scatter is for your eyes (and it shows no pattern). The graded number is just the biggest delivery time: reach into `orders["delivery_min"]` and ask it for `.max()`. Wrap `int(...)`.',
            "💡 Hint 2 (the structure)": 'slowest_ex23 = int(orders["___"].max())   — the blank is the delivery-time column.',
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — Honest charts
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — Honest charts

    A chart can be technically correct and still lie. The classic trick is the
    **y-axis that doesn't start at zero**: a flat line gets stretched into a cliff,
    and the eye believes the shape long before it reads the numbers.

    Kevin built the pitch's "growth slide" this way. The given cells below compute
    the two weekly totals (one honest number each) and Kevin's chart plots them.
    His chart *runs*; that's exactly why it's dangerous.
    """
    )
    return


@app.cell
def _(orders):
    # Given — do not change this. Week 1 revenue (days 1–7).
    week1 = float(orders[orders["day"] <= 7]["total_eur"].sum())
    return (week1,)


@app.cell
def _(orders):
    # Given — do not change this. Week 2 revenue (days 8–14).
    week2 = float(orders[orders["day"] >= 8]["total_eur"].sum())
    return (week2,)


@app.cell
def _(plt, week1, week2):
    # Kevin's "growth slide" — runs fine, technically correct numbers.
    plt.figure()  # fresh canvas
    plt.plot([1, 2], [week1, week2], marker="o")
    plt.ylim(782, 789)  # <-- the trick: the axis starts at 782, not 0
    plt.xlabel("Week")
    plt.ylabel("Revenue (€)")
    plt.title("Kevin's growth slide")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (core, fix the chart) — the truth about the trend

    Look at Kevin's chart. Week 2 drops to the floor. It reads like the startup
    is **falling off a cliff**, revenue collapsing week to week. An investor
    seeing that panics. But check the y-axis: it runs from **782 to 789**. The
    *entire* chart is a five-euro sliver, magnified until a rounding-error wobble
    looks like a catastrophe.

    Two jobs.

    **First, the honest chart (ungraded):** re-plot the same `week1` and `week2`,
    but let the y-axis start at 0: `plt.ylim(0, 900)`. Watch the cliff flatten
    into what it really is: a nearly flat line, two points at almost the same
    height.

    **Then, the honest number (graded):** compute the real week-over-week change as
    a **percent**. Percent growth compares the *change* to where you *started*:
    `(week2 − week1) / week1 × 100`. Round to 2 decimals and store it, as a plain
    `float`, in `growth_pct_ex31`.
    """
    )
    return


@app.cell
def _(plt, week1, week2):
    plt.figure()
    # YOUR CODE BELOW — re-plot [week1, week2] with an honest axis: plt.ylim(0, 900)
    plt.gca()
    return


@app.cell
def _():
    # YOUR CODE BELOW — week-over-week growth as a percent, rounded to 2 (float)
    growth_pct_ex31 = None
    return (growth_pct_ex31,)


@app.cell(hide_code=True)
def _(growth_pct_ex31, mo, pd, show_result):
    if growth_pct_ex31 is None:
        ex31_ok = False
        _msg = "🔲 Exercise 3.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(growth_pct_ex31)
        if isinstance(growth_pct_ex31, (pd.Series, pd.DataFrame)):
            ex31_ok = False
            _msg = "❌ Exercise 3.1: that's a table/column — you want one number. Compute `(week2 - week1) / week1 * 100`, then `float(...)`."
        else:
            try:
                _v = round(float(growth_pct_ex31), 2)
            except (TypeError, ValueError):
                _v = None
            if _v is None:
                ex31_ok = False
                _msg = "❌ Exercise 3.1: this should be a single **percent** number — the week-over-week change."
            elif _v == -0.66:
                ex31_ok = True
                _msg = "✅ Exercise 3.1: **−0.66 %** — essentially flat. Kevin's cliff was a lie the axis told. Flat is the truth — and a flat startup that *tells* the truth is more fundable than a rocket that lies. 📉➡️"
            elif _v == 0.66:
                ex31_ok = False
                _msg = "❌ Exercise 3.1: right size, wrong sign — you divided by week 2, or swapped the weeks. Growth is measured from where you started: `(week2 - week1) / week1`."
            elif _v in (5.2, -5.2):
                ex31_ok = False
                _msg = "❌ Exercise 3.1: 5.2 is the raw *euro* difference between the weeks, not a percent. Divide that gap by week 1 and multiply by 100."
            else:
                ex31_ok = False
                _msg = f"❌ Exercise 3.1: expected -0.66, got {_v}. Percent growth = `(week2 - week1) / week1 * 100`, rounded to 2."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex31_ok else "warn")
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Percent growth compares the CHANGE (`week2 - week1`) to the STARTING value (`week1`), then ×100. A tiny negative number is the honest answer here — the weeks are almost equal.",
            "💡 Hint 2 (the structure)": "growth_pct_ex31 = float(round((week2 - ___) / ___ * 100, 2))   — the change over the starting week.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 🏆 Boss exercise (core) — assemble the pitch

    One slide, three numbers, no typos. The investor wants a single **summary
    dict** she can read in five seconds (`pitch_ex40`) with exactly these three
    keys, every value **computed from `orders`**, never hand-typed:

    - `"revenue"` — total revenue across all orders (sum of `total_eur`, rounded to
      2 decimals, a `float`).
    - `"best_zone"` — the zone with the highest **total** revenue (a string: you
      already have every zone's total from 2.1; which one is largest?).
    - `"orders"` — how many orders there are (an `int`).

    Build the dict so that if the data changed, your numbers would too. Store it in
    `pitch_ex40`.
    """
    )
    return


@app.cell
def _(pd):
    # Worked example (read + run this) — .idxmax() names the top group
    _demo = pd.DataFrame(
        {"zone": ["A", "A", "B"], "total_eur": [10.0, 20.0, 12.0]}
    )
    print(_demo.groupby("zone")["total_eur"].sum())           # A: 30.0, B: 12.0
    print(_demo.groupby("zone")["total_eur"].sum().idxmax())  # 'A' — the label
    return


@app.cell
def _():
    # YOUR CODE BELOW — the summary dict with keys "revenue", "best_zone", "orders"
    pitch_ex40 = None
    return (pitch_ex40,)


@app.cell(hide_code=True)
def _(mo, pd, pitch_ex40, show_result):
    if pitch_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
        _preview = ""
    elif isinstance(pitch_ex40, (pd.Series, pd.DataFrame)):
        ex40_ok = False
        _preview = show_result(str(pitch_ex40))
        _msg = "❌ Boss exercise: that's a pandas object, not a plain dict. Build `{\"revenue\": ..., \"best_zone\": ..., \"orders\": ...}` yourself from the three results."
    elif not isinstance(pitch_ex40, dict):
        ex40_ok = False
        _preview = show_result(pitch_ex40)
        _msg = "❌ Boss exercise: this should be a **dict** with keys `\"revenue\"`, `\"best_zone\"`, `\"orders\"`."
    else:
        _preview = show_result(pitch_ex40)
        _needed = {"revenue", "best_zone", "orders"}
        _missing = _needed - set(pitch_ex40)
        if _missing:
            ex40_ok = False
            _msg = f"❌ Boss exercise: missing key(s): {', '.join(sorted(_missing))}. The dict needs exactly `revenue`, `best_zone`, `orders`."
        else:
            try:
                _rev = round(float(pitch_ex40["revenue"]), 2)
            except (TypeError, ValueError):
                _rev = None
            _zone = pitch_ex40["best_zone"]
            try:
                _cnt = int(pitch_ex40["orders"])
            except (TypeError, ValueError):
                _cnt = None
            if _rev is None or _cnt is None:
                ex40_ok = False
                _msg = "❌ Boss exercise: `revenue` should be a euro number and `orders` a whole count. Check what those two entries hold."
            elif not isinstance(_zone, str):
                ex40_ok = False
                _msg = "❌ Boss exercise: `best_zone` should be the zone's **name** (a string) — use `.idxmax()` on the per-zone totals, not `.max()`."
            elif _rev != 1571.6:
                ex40_ok = False
                _msg = f"❌ Boss exercise: `revenue` should be 1571.6 (got {_rev}). Sum `total_eur` across every order and round to 2."
            elif _zone.strip() != "Sued":
                ex40_ok = False
                _msg = "❌ Boss exercise: `best_zone` isn't the top earner. The highest *total* revenue belongs to one zone — `.idxmax()` on your 2.1 breakdown names it."
            elif _cnt != 80:
                ex40_ok = False
                _msg = f"❌ Boss exercise: `orders` should be 80 (got {_cnt}). That's `len(orders)`."
            else:
                ex40_ok = True
                _msg = "✅ Boss exercise: **{'revenue': 1571.6, 'best_zone': 'Sued', 'orders': 80}** — three honest numbers, all computed, none typed. That's a slide you can defend. 🏆"
    mo.callout(mo.md(_msg + _preview), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Compute the three pieces first, then put them in a dict. Revenue is `orders[\"total_eur\"].sum()` (round 2). Best zone is `.idxmax()` on the per-zone totals — the LABEL, not the value. Count is `len(orders)`.",
            "💡 Hint 2 (the structure)": 'pitch_ex40 = {\n    "revenue": float(round(orders["total_eur"].sum(), 2)),\n    "best_zone": orders.groupby("zone")["total_eur"].sum().___(),\n    "orders": int(len(orders)),\n}   — the blank names the top-total zone.',
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
    ### Exercise (trace — predict first) — why `plt.gca()`?

    This is a **trace** exercise: predict first, *then* reveal. It's ungraded. The
    point is committing. Here are two chart cells that differ only in the **last
    line**:

    ```python
    # Cell A                    # Cell B
    plt.figure()               plt.figure()
    plt.plot(xs, ys)           plt.plot(xs, ys)
                               plt.gca()
    ```

    In marimo, a cell shows its **last expression**. What does each cell display?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_gca = mo.ui.radio(
        options=[
            "A — both show the chart; the last line makes no difference",
            "B — A shows a list like [<matplotlib.lines.Line2D>]; B shows the chart",
            "C — one of them raises an error",
        ],
        label="What does each cell display?",
    )
    trace_gca
    return (trace_gca,)


@app.cell(hide_code=True)
def _(mo, trace_gca):
    if trace_gca.value is None:
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_gca.value.startswith("B"):
        _msg = (
            "✅ Correct: **B**. `plt.plot(...)` *returns* a list of the line objects "
            "it drew — so if that's the last line, marimo shows its repr, "
            "`[<matplotlib.lines.Line2D ...>]`, not a picture. `plt.gca()` "
            '("get current axes") returns the axes object marimo knows how to '
            "render **as** the chart. That's why every chart cell ends with "
            "`plt.gca()`."
        )
    else:
        _msg = (
            "❌ Not quite — the answer is **B**. Nothing errors, but the last line "
            "matters: `plt.plot(...)` returns a *list of line objects*, so cell A "
            "would show `[<matplotlib.lines.Line2D ...>]`. `plt.gca()` returns the "
            "axes, which marimo renders as the actual chart. (Ungraded — the point "
            "is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ) — pick the chart

    The investor asks: **"How are the order values distributed?"** Which chart
    answers *that* question? Assign the letter (as text) to `answer_ex50`:

    - **a)** a line chart
    - **b)** a histogram
    - **c)** a pie chart
    - **d)** a scatter plot
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — replace "" with "a", "b", "c", or "d"
    answer_ex50 = ""
    return (answer_ex50,)


@app.cell(hide_code=True)
def _(answer_ex50, mo):
    if answer_ex50 == "":
        ex50_ok = False
        _msg = "🔲 Quiz: not attempted yet."
    elif str(answer_ex50).strip().lower() == "b":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **b**. *Distribution* — how one column of numbers spreads out — "
            "is exactly what a **histogram** shows. A line is for change over time, a "
            "bar is for comparing categories, and a scatter is for two numbers per "
            "row. Right question, right chart."
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. A line tracks change over time, a bar compares "
            "categories, a scatter relates two numbers. The spread of a *single* "
            "column of values is a **histogram** — that's what 'distributed' asks for."
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
    ex21_ok,
    ex22_ok,
    ex23_ok,
    ex31_ok,
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell — the 7 core exercises plus the quiz (the trace doesn't count).
    _checks = [ex11_ok, ex12_ok, ex21_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _investor = (
        "The investor closes the deck and smiles. Charts she can't argue with — because they're true."
        if _done == _total
        else "The investor is still flipping through the deck, waiting for a chart she can trust."
    )
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} ✅** — {_investor}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave 📊

    1. Check the progress box above — all **eight** green? If not, reopen the
       hints, reread the worked examples, and try again. Right chart for the
       question, honest axis, numbers you can defend: that's the whole job.
    2. **Download your work**: menu → Download → *Download Python code*. This one
       is more than a backup: it's the **appendix of your pitch**, the file that
       proves every chart came from the real data. Reloading this tab (Cmd/Ctrl+R)
       keeps your work; closing it and reopening the link starts you fresh, so the
       download is the only guaranteed copy.

    ---

    ### 🧰 Homework before Session X — set up the real toolchain

    So far everything has run in the browser. The season finale moves to your own
    machine, and you'll want two tools installed **before** you arrive:

    - **uv** — the Python environment manager this course uses. Follow
      [the uv guide](https://beyondsimulations.github.io/Introduction-to-Python/general/uv.html).
    - **Zed** (with its AI assistant) — the editor you'll actually write code in.
      Follow [the AI-tools guide](https://beyondsimulations.github.io/Introduction-to-Python/general/ai-tools.html).

    Do this in advance: Session X *builds on* a working toolchain — it doesn't wait
    for one. Budget about 15 minutes; if the install fights you, bring it to office
    hours before Session X. Don't burn an evening on it.

    **Season finale next:** git, real files on your own disk, and the project
    kickoff. See you there. 🎬
    """
    )
    return


if __name__ == "__main__":
    app.run()
