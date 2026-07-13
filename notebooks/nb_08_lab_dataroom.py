# notebooks/nb_08_lab_dataroom.py
# Episode 8 — The Data Room. Session VIII lab notebook.
# Built from notebooks/nb_07_lab_metrics.py (spec §4 rules apply):
# one global name per cell; += counts as a definition; every exercise
# pre-defines its answer (None); suffix exercise names (_exNM); underscore-
# prefixed names are cell-private; never a possible infinite loop. First lab to
# load a real file: notebooks/public/orders.csv arrives via the pandas loader
# (see docs/authoring-conventions.md — pd.read_csv is URL-aware, works locally
# and in exported WASM, no try/except needed). Checks are crash-proof: every
# coercion is guarded and Series/DataFrame answers degrade to a message instead
# of raising (see notebooks/exercises/ex_08_a.py, ex_08_b.py).
#
# ledger (all values computed FROM notebooks/public/orders.csv — cross-checked
# against helpers/make_orders_csv.py):
#   rows len(orders)                                            = 80
#   columns orders.shape[1]                                     = 9
#   revenue orders["total_eur"].sum()                          = 1571.6
#   Nord count len(orders[zone=="Nord"])                       = 22
#   Sued & items>=2 count                                      = 15
#   Hafen revenue orders[zone=="Hafen"]["total_eur"].sum()     = 354.2
#   max eur_per_item (Miso Ramen unit price)                   = 11.9
#   groupby zone total_eur .sum() = {'Altstadt': 408.4,
#       'Hafen': 354.2, 'Nord': 378.9, 'Sued': 430.1}
#   groupby zone total_eur .mean() = {'Altstadt': 20.42,
#       'Hafen': 18.64, 'Nord': 17.22, 'Sued': 22.64}  -> idxmax = "Sued"
#   trace: orders[orders["items"]==3].shape = (27, 9)
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 8.1 — The Data Room
    **Estimated time: 45–60 min · Core exercises: 9 + 1 quiz (+ 1 trace)**

    MunchCorp went to the press with "data-driven growth". The investor was not
    impressed by a slide; she was impressed by *data*. So she slides a USB stick
    across the table: **every order, two full weeks.** "Impress me."

    That stick is now a file: `public/orders.csv`, one row per order, eighty of
    them. Too many to eyeball, too many for a hand-written loop. This is what
    **pandas** is for: it loads a whole spreadsheet into one object (a
    *DataFrame*), and answers questions about it (filter, count, total, group)
    in one honest line each.

    Kevin, meanwhile, has **discovered AI**. He now pastes every question into a
    chatbot and ships whatever comes back. Your real job this week isn't writing
    pandas from scratch. It's **supervising**: reading what the data actually
    says and catching the confident nonsense.

    > **If the notebook fails to boot with a network error** (or the very first
    > cell complains that pandas can't be imported), **reload the page once**
    > (Cmd/Ctrl + R). The first load fetches pandas over the network and can
    > flake; a reload almost always fixes it.
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


@app.cell(hide_code=True)
def _(mo):
    startup_name_input = mo.ui.text(
        label="Your startup's name:", placeholder="e.g. SnackRocket"
    )
    mo.vstack(
        [
            mo.md(
                "Before we open the data room, remind me of the company name? "
                "Type it once and it sticks for the whole notebook. (New tab, so "
                "we ask afresh.)"
            ),
            startup_name_input,
        ]
    )
    return (startup_name_input,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(
        f"Opening the data room for **{startup_name}**. Eighty orders, two weeks, "
        "one investor watching. Let's read what the data actually says, and keep "
        "Kevin's chatbot honest."
    )
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — First look: the DataFrame
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — First look: the DataFrame

    The file is already loaded for you into a **DataFrame** called `orders`, a
    spreadsheet Python can reason about. Two moves to get your bearings:

    - **`orders.head()`** shows the first five rows: a peek, not the whole thing.
    - **`len(orders)`** counts the rows; **`orders.shape`** is `(rows, columns)`,
      so `orders.shape[1]` is the number of columns.

    And to reach into one column you name it in square brackets, like a
    dictionary key: `orders["total_eur"]` is the whole euro column, and a column
    knows how to total itself: `orders["total_eur"].sum()`.

    Read and run the worked example (it prints the first five orders), then
    answer for real.
    """
    )
    return


@app.cell
def _(orders):
    # Worked example (read + run this) — peek at the first five orders
    print(orders.head())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — how many orders?

    The investor's first question is the simplest: **how many orders are on the
    stick?** Don't scroll and count. Ask the DataFrame. Store the row count, as a
    plain `int`, in `rows_ex11` (use `int(len(orders))`).
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — the number of rows in orders, as a plain int
    rows_ex11 = None
    return (rows_ex11,)


@app.cell(hide_code=True)
def _(mo, pd, rows_ex11, show_result):
    if rows_ex11 is None:
        ex11_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(rows_ex11)
        if isinstance(rows_ex11, (pd.Series, pd.DataFrame)):
            ex11_ok = False
            _msg = "❌ Exercise 1.1: that's still a whole table/column. `len(orders)` collapses it to one number — wrap `int(...)` around it."
        else:
            try:
                _n = int(rows_ex11)
            except (TypeError, ValueError):
                _n = None
            if _n is None:
                ex11_ok = False
                _msg = "❌ Exercise 1.1: this should be a whole **number** — the row count from `int(len(orders))`."
            elif _n == 80:
                ex11_ok = True
                _msg = "✅ Exercise 1.1: **80** orders. `len(orders)` counts the rows for you — no scrolling, no miscount."
            elif _n == 9:
                ex11_ok = False
                _msg = "❌ Exercise 1.1: 9 is the number of *columns*, not rows. `len(orders)` counts rows; columns come next in 1.2."
            else:
                ex11_ok = False
                _msg = f"❌ Exercise 1.1: expected 80, got {_n}. `int(len(orders))` counts every row in the file."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`len(...)` counts the rows of a DataFrame, exactly like it counts a list. Wrap `int(...)` around it so it's a plain whole number.",
            "💡 Hint 2 (the structure)": "rows_ex11 = int(len(___))   — the blank is the DataFrame the file was loaded into.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — how wide is the table?

    Every column is a fact the investor might ask about (zone, dish, delivery
    time…). **How many columns** does the file carry? `orders.shape` is a
    `(rows, columns)` pair, so the second item, `orders.shape[1]`, is the
    column count. Store it, as a plain `int`, in `n_cols_ex12`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — the number of columns, as a plain int: int(orders.shape[1])
    n_cols_ex12 = None
    return (n_cols_ex12,)


@app.cell(hide_code=True)
def _(mo, n_cols_ex12, pd, show_result):
    if n_cols_ex12 is None:
        ex12_ok = False
        _msg = "🔲 Exercise 1.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(n_cols_ex12)
        if isinstance(n_cols_ex12, (pd.Series, pd.DataFrame)):
            ex12_ok = False
            _msg = "❌ Exercise 1.2: that's still a table/column. You want one number — `orders.shape[1]`."
        elif isinstance(n_cols_ex12, tuple):
            ex12_ok = False
            _msg = "❌ Exercise 1.2: that's the whole `(rows, columns)` pair — pick the second item with `[1]`, then `int(...)`."
        else:
            try:
                _n = int(n_cols_ex12)
            except (TypeError, ValueError):
                _n = None
            if _n is None:
                ex12_ok = False
                _msg = "❌ Exercise 1.2: this should be a whole **number** — the column count from `int(orders.shape[1])`."
            elif _n == 9:
                ex12_ok = True
                _msg = "✅ Exercise 1.2: **9** columns. `orders.shape` is `(80, 9)`; `[1]` picks the width. Nine facts per order to slice."
            elif _n == 80:
                ex12_ok = False
                _msg = "❌ Exercise 1.2: 80 is the *row* count — that's `shape[0]`. The number of columns is `shape[1]`."
            else:
                ex12_ok = False
                _msg = f"❌ Exercise 1.2: expected 9, got {_n}. Take the second item of `orders.shape`: `int(orders.shape[1])`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`orders.shape` gives `(rows, columns)`. Index it with `[1]` to grab the column count (positions start at 0, so `[0]` is rows and `[1]` is columns).",
            "💡 Hint 2 (the structure)": "n_cols_ex12 = int(orders.shape[___])   — the blank picks the columns half of the `(rows, columns)` pair.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.3 (core) — two weeks of revenue

    The headline number: **total revenue** across all eighty orders. The
    `total_eur` column holds each order's euros; a column totals itself with
    `.sum()`. Store the grand total, as a plain `float`, in `revenue_ex13`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — the total of the total_eur column, as a plain float
    revenue_ex13 = None
    return (revenue_ex13,)


@app.cell(hide_code=True)
def _(mo, pd, revenue_ex13, show_result):
    if revenue_ex13 is None:
        ex13_ok = False
        _msg = "🔲 Exercise 1.3: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(revenue_ex13)
        if isinstance(revenue_ex13, (pd.Series, pd.DataFrame)):
            ex13_ok = False
            _msg = "❌ Exercise 1.3: that's still the whole column — `.sum()` collapses it to one number. Then wrap `float(...)`."
        else:
            try:
                _v = round(float(revenue_ex13), 2)
            except (TypeError, ValueError):
                _v = None
            if _v is None:
                ex13_ok = False
                _msg = "❌ Exercise 1.3: this should be a single euro **number** — total the `total_eur` column with `.sum()`."
            elif _v == 1571.6:
                ex13_ok = True
                _msg = "✅ Exercise 1.3: **1571.6 €** over two weeks. `orders[\"total_eur\"].sum()` added all eighty orders in one line — no calculator, no loop."
            else:
                ex13_ok = False
                _msg = f"❌ Exercise 1.3: expected 1571.6, got {_v}. Total the euro column: `orders[\"total_eur\"].sum()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex13_ok else "warn")
    return (ex13_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'Reach into one column by name in square brackets — `orders["total_eur"]` — then ask it to `.sum()`. Wrap `float(...)` around the result.',
            "💡 Hint 2 (the structure)": 'revenue_ex13 = float(orders["___"].sum())   — the blank is the name of the euros column.',
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Slicing the room
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Slicing the room

    Now the sharper questions: *which* orders, not just how many. A **boolean
    mask** filters a DataFrame exactly like it filtered a NumPy array last week:
    `orders[orders["zone"] == "Nord"]` keeps only the rows where the test is
    `True`. From there, `len(...)` counts them and `["total_eur"].sum()` totals
    their revenue.

    > One marimo habit for this section: a typo in a column name (or an empty
    > filter) is a **red error that pauses everything below it**, including the
    > progress box. Nothing is lost; fix the red cell and it all comes back. You
    > will meet exactly this in 2.3, on purpose.

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _(pd):
    # Worked example (read + run this) — filter, then count / total
    _demo = pd.DataFrame(
        {"zone": ["Ost", "Ost", "West"], "total_eur": [10.0, 6.0, 20.0]}
    )
    print(_demo[_demo["zone"] == "Ost"])
    print("count:", len(_demo[_demo["zone"] == "Ost"]))
    print("revenue:", _demo[_demo["zone"] == "Ost"]["total_eur"].sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core) — one zone at a time

    The **Nord** zone has been loud about its numbers. **How many orders came
    from Nord?** Filter `orders` to just that zone, then count the rows. Store the
    count, as a plain `int`, in `nord_count_ex21`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — how many orders have zone == "Nord", as a plain int
    nord_count_ex21 = None
    return (nord_count_ex21,)


@app.cell(hide_code=True)
def _(mo, nord_count_ex21, pd, show_result):
    if nord_count_ex21 is None:
        ex21_ok = False
        _msg = "🔲 Exercise 2.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(nord_count_ex21)
        if isinstance(nord_count_ex21, (pd.Series, pd.DataFrame)):
            ex21_ok = False
            _msg = "❌ Exercise 2.1: that's the filtered rows themselves. Wrap `len(...)` around the filter to count them, then `int(...)`."
        else:
            try:
                _c = int(nord_count_ex21)
            except (TypeError, ValueError):
                _c = None
            if _c is None:
                ex21_ok = False
                _msg = "❌ Exercise 2.1: this should be a whole **number** of Nord orders. Count the filtered rows with `len(...)`."
            elif _c == 22:
                ex21_ok = True
                _msg = "✅ Exercise 2.1: **22** orders from Nord. The mask `orders[\"zone\"] == \"Nord\"` kept only Nord's rows; `len(...)` counted them."
            elif _c == 80:
                ex21_ok = False
                _msg = "❌ Exercise 2.1: 80 is *every* order — you counted the whole table. Filter to `zone == \"Nord\"` first, then count."
            elif _c == 0:
                ex21_ok = False
                _msg = "❌ Exercise 2.1: zero rows — pandas is case-sensitive, so check the spelling (\"Nord\", capital N)."
            else:
                ex21_ok = False
                _msg = f"❌ Exercise 2.1: expected 22, got {_c}. Filter with `orders[orders[\"zone\"] == \"Nord\"]`, then `len(...)`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'Build the mask `orders["zone"] == "Nord"`, use it to filter `orders`, then `len(...)` counts the rows that survived. Wrap `int(...)`.',
            "💡 Hint 2 (the structure)": 'nord_count_ex21 = int(len(orders[orders["zone"] == "___"]))   — the blank is the zone name, spelled exactly.',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — two conditions at once

    The investor gets specific: **Sued orders that were also bulk** — zone is
    `"Sued"` **and** at least 2 items. Two conditions on the same rows.

    In pandas you combine masks with **`&`** (and), **`|`** (or), and **each
    condition needs its own parentheses**, because `&` binds tighter than `==`
    and `>=`. So the shape is always:

    ```python
    df[(df["col_a"] == x) & (df["col_b"] >= y)]
    ```

    Miss a pair of parentheses and pandas raises a red error. That's the syntax
    reminding you. Count the Sued-and-bulk orders and store the count, as a plain
    `int`, in `sued_bulk_ex22`.
    """
    )
    return


@app.cell
def _(pd):
    # Worked example (read + run this) — TWO conditions, each in its own ()
    _demo = pd.DataFrame({"zone": ["A", "A", "B", "A"], "items": [1, 3, 2, 2]})
    _both = _demo[(_demo["zone"] == "A") & (_demo["items"] >= 2)]
    print(_both)
    print("count:", len(_both))   # 2  — the two A rows with items >= 2
    return


@app.cell
def _():
    # YOUR CODE BELOW — count orders where zone == "Sued" AND items >= 2 (int)
    sued_bulk_ex22 = None
    return (sued_bulk_ex22,)


@app.cell(hide_code=True)
def _(mo, pd, show_result, sued_bulk_ex22):
    if sued_bulk_ex22 is None:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(sued_bulk_ex22)
        if isinstance(sued_bulk_ex22, (pd.Series, pd.DataFrame)):
            ex22_ok = False
            _msg = "❌ Exercise 2.2: that's the filtered rows themselves — wrap `len(...)` around the two-condition filter, then `int(...)`."
        else:
            try:
                _c = int(sued_bulk_ex22)
            except (TypeError, ValueError):
                _c = None
            if _c is None:
                ex22_ok = False
                _msg = "❌ Exercise 2.2: this should be a whole **number** — count the rows that pass *both* conditions."
            elif _c == 15:
                ex22_ok = True
                _msg = "✅ Exercise 2.2: **15** Sued orders with 2+ items. `(zone == \"Sued\") & (items >= 2)` — two masks, each parenthesised, joined with `&`."
            elif _c == 19:
                ex22_ok = False
                _msg = "❌ Exercise 2.2: 19 is *all* Sued orders — you dropped the items condition. Add `& (orders[\"items\"] >= 2)`."
            else:
                ex22_ok = False
                _msg = f"❌ Exercise 2.2: expected 15, got {_c}. Join both masks with `&`, each in its own parentheses, then `len(...)`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'Two masks joined by `&`. Wrap EACH mask in its own parentheses: `(orders["zone"] == "Sued") & (orders["items"] >= 2)`. Then filter, `len(...)`, `int(...)`.',
            "💡 Hint 2 (the structure)": 'sued_bulk_ex22 = int(len(orders[(orders["zone"] == "___") & (orders["items"] >= ___)]))   — zone name in the first blank, the minimum item count in the second.',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core, fix the bug) — Kevin's KeyError

    Kevin asked the AI for "Hafen's revenue" and pasted the answer straight into
    the cell below. It's waiting there as a **comment**. Uncomment his line and
    run it, exactly as it is. The cell goes **red**: `KeyError: 'Zone'`.

    That red moment is expected, and recoverable. An erroring cell pauses every
    cell below it (this check, the progress box); nothing is lost, and the
    moment you fix the bug, everything comes back.

    The clue is in the error itself: a `KeyError` names the exact column pandas
    couldn't find. Compare that name, letter by letter, with the columns
    `orders.head()` printed back in Section 1. Then fix Kevin's line (and delete
    the `None` placeholder underneath it) so it stores Hafen's total revenue, as
    a plain `float`, in `hafen_revenue_ex23`.
    """
    )
    return


@app.cell
def _():
    # Kevin's line (run it as-is first — watch it go red):
    # hafen_revenue_ex23 = float(orders[orders["Zone"] == "Hafen"]["total_eur"].sum())
    hafen_revenue_ex23 = None  # YOUR CODE BELOW — delete this line once Kevin's is fixed
    return (hafen_revenue_ex23,)


@app.cell(hide_code=True)
def _(hafen_revenue_ex23, mo, pd, show_result):
    if hafen_revenue_ex23 is None:
        ex23_ok = False
        _msg = "🔲 Exercise 2.3: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(hafen_revenue_ex23)
        if isinstance(hafen_revenue_ex23, (pd.Series, pd.DataFrame)):
            ex23_ok = False
            _msg = "❌ Exercise 2.3: that's still a column/table — `.sum()` collapses it to one number. Then wrap `float(...)`."
        else:
            try:
                _v = round(float(hafen_revenue_ex23), 2)
            except (TypeError, ValueError):
                _v = None
            if _v is None:
                ex23_ok = False
                _msg = "❌ Exercise 2.3: this should be a single euro **number** — Hafen's total. Filter, take `total_eur`, `.sum()`."
            elif pd.isna(_v):
                ex23_ok = False
                _msg = "❌ Exercise 2.3: your filter came back empty (NaN). Case matters — the zone is spelled \"Hafen\" (capital H), the column is \"zone\" (lowercase)."
            elif _v == 354.2:
                ex23_ok = True
                _msg = "✅ Exercise 2.3: **354.2 €** from Hafen. You caught Kevin's KeyError — lowercase `zone` — and the red cell went green again."
            elif _v == 1571.6:
                ex23_ok = False
                _msg = "❌ Exercise 2.3: 1571.6 is *every* zone's revenue — you forgot to filter. Keep only `zone == \"Hafen\"` first."
            else:
                ex23_ok = False
                _msg = f"❌ Exercise 2.3: expected 354.2, got {_v}. Filter to `orders[\"zone\"] == \"Hafen\"`, then `[\"total_eur\"].sum()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Read the KeyError's last line — which column name does pandas say it can't find? Compare it letter by letter with what `orders.head()` shows.",
            "💡 Hint 2 (the structure)": 'hafen_revenue_ex23 = float(orders[orders["zone"] == "___"]["total_eur"].sum())   — lowercase column name in the mask, the zone name in the blank.',
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — The questions that matter
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — The questions that matter

    Counting rows is warm-up. The investor wants **derived** numbers and
    **per-group** numbers: the two moves that turn a table into an argument.

    - A **new column** is just column arithmetic: `df["a"] / df["b"]` computes
      row by row. **Professional habit:** when you're adding a column to explore,
      work on a *copy* (`df.copy()`) so you never quietly mutate the original
      table other cells rely on.
    - **`groupby`** splits the rows by a category and runs one calculation per
      group: `df.groupby("zone")["total_eur"].sum()` gives one total per zone, all
      at once.

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _(pd):
    # Worked example (read + run this) — a new column, computed on a COPY
    _demo = pd.DataFrame({"total_eur": [10.0, 9.0], "items": [2, 3]})
    _priced = _demo.copy()                        # never mutate the original
    _priced["per_item"] = _priced["total_eur"] / _priced["items"]
    print(_priced)
    print("max per item:", _priced["per_item"].max())   # 5.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (core) — the priciest single item

    The menu has four dishes; which one is dearest **per item**? Add a column
    `eur_per_item = total_eur / items` (on a **copy** of `orders`, per the habit
    above), then take its `.max()`. Store that top unit price, rounded to 2
    decimals as a plain `float`, in `max_per_item_ex31`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — work on a copy, add eur_per_item, take its max (round 2)
    #   _priced = orders.copy()
    #   _priced["eur_per_item"] = ...
    max_per_item_ex31 = None
    return (max_per_item_ex31,)


@app.cell(hide_code=True)
def _(max_per_item_ex31, mo, pd, show_result):
    if max_per_item_ex31 is None:
        ex31_ok = False
        _msg = "🔲 Exercise 3.1: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(max_per_item_ex31)
        if isinstance(max_per_item_ex31, (pd.Series, pd.DataFrame)):
            ex31_ok = False
            _msg = "❌ Exercise 3.1: that's still a whole column — `.max()` picks the single biggest value. Then wrap `float(...)`."
        else:
            try:
                _v = round(float(max_per_item_ex31), 2)
            except (TypeError, ValueError):
                _v = None
            if _v is None:
                ex31_ok = False
                _msg = "❌ Exercise 3.1: this should be a single **number** — the highest `eur_per_item`."
            elif _v == 11.9:
                ex31_ok = True
                _msg = "✅ Exercise 3.1: **11.90 €** per item — that's the Miso Ramen, the priciest dish on the menu. And you did it on a copy, leaving `orders` untouched. 🍜"
            elif _v == 35.7:
                ex31_ok = False
                _msg = "❌ Exercise 3.1: 35.7 is a whole *order's* total (3 × Miso Ramen), not the per-item price. Divide `total_eur` by `items` first, then take the max."
            else:
                ex31_ok = False
                _msg = f"❌ Exercise 3.1: expected 11.9, got {_v}. Add `eur_per_item = total_eur / items` on a copy, then `.max()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex31_ok else "warn")
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Copy first (`_priced = orders.copy()`), add the column by dividing two columns (`_priced[\"total_eur\"] / _priced[\"items\"]`), then ask that new column for its `.max()`.",
            "💡 Hint 2 (the structure)": '_priced = orders.copy()\n_priced["eur_per_item"] = _priced["total_eur"] / _priced["items"]\nmax_per_item_ex31 = float(round(_priced["eur_per_item"].___(), 2))   — the method that finds the biggest value.',
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.2 (core) — revenue per zone, in one line

    The investor wants the **per-zone breakdown**: total revenue for each of the
    four zones, handed over as a **plain dict** (zone → euros, rounded to 2
    decimals) so it's easy to read. That's exactly what `groupby` is built for.
    The worked example below shows the whole move on toy data.

    Store the dict in `by_zone_ex32`. (If you end up with a Series instead of a
    dict, the check will nudge you.)
    """
    )
    return


@app.cell
def _(pd):
    # Worked example (read + run this) — groupby sum, then .to_dict()
    _demo = pd.DataFrame(
        {"zone": ["A", "A", "B"], "total_eur": [5.0, 3.0, 4.0]}
    )
    print(_demo.groupby("zone")["total_eur"].sum())            # a Series
    print(_demo.groupby("zone")["total_eur"].sum().to_dict())  # {'A': 8.0, 'B': 4.0}
    return


@app.cell
def _():
    # YOUR CODE BELOW — {zone: total_eur} dict, rounded to 2 decimals
    by_zone_ex32 = None
    return (by_zone_ex32,)


@app.cell(hide_code=True)
def _(by_zone_ex32, mo, pd, show_result):
    _expected = {"Altstadt": 408.4, "Hafen": 354.2, "Nord": 378.9, "Sued": 430.1}
    if by_zone_ex32 is None:
        ex32_ok = False
        _msg = "🔲 Exercise 3.2: not attempted yet."
        _preview = ""
    else:
        _preview = show_result(by_zone_ex32)
        if isinstance(by_zone_ex32, pd.Series):
            ex32_ok = False
            _msg = "❌ Exercise 3.2: that's a **Series**, not a dict — `.to_dict()` finishes the job. Add it to the end of your groupby."
        elif isinstance(by_zone_ex32, pd.DataFrame):
            ex32_ok = False
            _msg = "❌ Exercise 3.2: that's a whole table. Pick the `total_eur` column *before* summing: `.groupby(\"zone\")[\"total_eur\"].sum()`, then `.to_dict()`."
        elif not isinstance(by_zone_ex32, dict):
            ex32_ok = False
            _msg = "❌ Exercise 3.2: this should be a **dict** of zone → euros. Finish the groupby with `.round(2).to_dict()`."
        else:
            try:
                _got = {str(_k): round(float(_v), 2) for _k, _v in by_zone_ex32.items()}
            except (TypeError, ValueError):
                _got = None
            if _got is None:
                ex32_ok = False
                _msg = "❌ Exercise 3.2: the values should be euro numbers. Group by `zone`, sum `total_eur`, then `.round(2).to_dict()`."
            elif _got == _expected:
                ex32_ok = True
                _msg = "✅ Exercise 3.2: four zones, four totals, one line — that's the `groupby` idea: split by a category, compute once per group. No loop in sight."
            elif set(_got) != set(_expected):
                ex32_ok = False
                _msg = "❌ Exercise 3.2: the zones don't match — you should have exactly the four keys 'Altstadt', 'Hafen', 'Nord', 'Sued'. Group by `zone`."
            else:
                ex32_ok = False
                _msg = "❌ Exercise 3.2: right zones, wrong totals. Sum `total_eur` per group: `orders.groupby(\"zone\")[\"total_eur\"].sum().round(2).to_dict()`."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex32_ok else "warn")
    return (ex32_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": 'Three links in a chain: `.groupby("zone")` splits the rows, `["total_eur"].sum()` totals each group, and `.round(2).to_dict()` turns the Series into a clean dict.',
            "💡 Hint 2 (the structure)": 'by_zone_ex32 = orders.groupby("___")["total_eur"].sum().round(2).___()   — the blank group key is the zone column; the final method turns a Series into a dict.',
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
    ## 🏆 Boss exercise (core) — the investor's real question

    The totals in 3.2 crown one winner. But the investor asks a trickier
    question: **which zone has the highest AVERAGE order value?** A total
    rewards whoever had the *most* orders; the average rewards whoever's orders
    were *bigger*. They need not be the same zone. Let the data decide.

    Two tools exist for exactly this: **`.mean()`** (in place of `.sum()`)
    averages each group, and **`.idxmax()`** returns the *label* of a Series'
    largest value, here a zone name. Store the winning zone's **name** (a
    string) in `best_avg_zone_ex40`.
    """
    )
    return


@app.cell
def _(pd):
    # Worked example (read + run this) — mean per group, then idxmax names the winner
    _demo = pd.DataFrame(
        {"zone": ["A", "A", "B"], "total_eur": [10.0, 20.0, 12.0]}
    )
    print(_demo.groupby("zone")["total_eur"].mean())           # A: 15.0, B: 12.0
    print(_demo.groupby("zone")["total_eur"].mean().idxmax())  # 'A'
    return


@app.cell
def _():
    # YOUR CODE BELOW — the NAME of the zone with the highest MEAN order value
    best_avg_zone_ex40 = None
    return (best_avg_zone_ex40,)


@app.cell(hide_code=True)
def _(best_avg_zone_ex40, mo, pd, show_result):
    if best_avg_zone_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
        _preview = ""
    elif isinstance(best_avg_zone_ex40, str):
        _preview = show_result(best_avg_zone_ex40)
        _v = best_avg_zone_ex40.strip()
        if _v == "Sued":
            ex40_ok = True
            _msg = "✅ Boss exercise: **Sued** — highest average order value (about 22.64 €), *and* it happened to top total revenue too. `.mean()` then `.idxmax()` named the winner for you. 🏆"
        elif _v in {"Nord", "Hafen", "Altstadt"}:
            ex40_ok = False
            _msg = "❌ Boss exercise: that zone doesn't have the highest *average*. Group by zone, take `.mean()` of `total_eur`, then `.idxmax()` for the label."
        else:
            ex40_ok = False
            _msg = "❌ Boss exercise: that isn't one of the four zone names. `.idxmax()` should return 'Nord', 'Sued', 'Hafen' or 'Altstadt'."
    elif isinstance(best_avg_zone_ex40, (pd.Series, pd.DataFrame)):
        ex40_ok = False
        _preview = show_result(str(best_avg_zone_ex40))
        _msg = "❌ Boss exercise: that's the whole per-zone table. `.idxmax()` turns it into the single winning *label* — the zone name."
    else:
        ex40_ok = False
        _preview = show_result(best_avg_zone_ex40)
        _msg = "❌ Boss exercise: expected a zone **name** (a string). `.idxmax()` on the mean-per-zone Series returns that name."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Same chain as 3.2 but with `.mean()`, and finish with `.idxmax()` — `max()` gives the biggest *value*, `idxmax()` gives its *label* (the zone name), which is what you want.",
            "💡 Hint 2 (the structure)": 'best_avg_zone_ex40 = orders.groupby("zone")["total_eur"].___().idxmax()   — the blank is the averaging method (not sum).',
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
    ### Exercise (trace — predict first) — the mask vs. the filter

    This is a **trace** exercise: predict first, *then* reveal. It's ungraded.
    The point is committing. Here are two expressions on the same data:

    ```python
    orders[orders["items"] == 3].shape     # A
    orders["items"] == 3                    # B
    ```

    One of them **is the True/False column itself** (a `True`/`False` for every
    row, the mask). The other **uses** that mask to filter, then reports the
    filtered table's `(rows, columns)`. Which expression is the mask?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_mask = mo.ui.radio(
        options=[
            'A — orders[orders["items"] == 3].shape',
            'B — orders["items"] == 3',
        ],
        label="Which expression is the True/False column (the mask)?",
    )
    trace_mask
    return (trace_mask,)


@app.cell(hide_code=True)
def _(mo, trace_mask):
    if trace_mask.value is None:
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_mask.value.startswith("B"):
        _msg = (
            "✅ Correct: **B**. `orders[\"items\"] == 3` compares every row and hands "
            "back a `True`/`False` **column** — the mask. Expression **A** *feeds* "
            "that mask back into `orders[...]` to keep the matching rows, then "
            "`.shape` reports the result's size: `(27, 9)` — 27 orders of exactly "
            "3 items, still 9 columns wide."
        )
    else:
        _msg = (
            "❌ Not quite — the mask is **B**. `orders[\"items\"] == 3` is the "
            "`True`/`False` column (one per row). **A** takes that column, filters "
            "`orders` with it, and `.shape` reports the filtered table's "
            "`(rows, columns)` — `(27, 9)`, not a column of booleans. (Ungraded — "
            "the point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ) — what does `.describe()` show?

    You'll reach for `orders.describe()` constantly, but what does it actually
    return? Assign the letter (as text) to `answer_ex50`:

    - **a)** the first five rows
    - **b)** count, mean, std, min, the quartiles and max for each numeric column
    - **c)** the column types only
    - **d)** a bar chart
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
            "✅ Quiz: **b**. `.describe()` gives a summary table — count, mean, std, "
            "min, the 25/50/75% quartiles and max — for every numeric column. One "
            "call, the whole shape of the data. (The first five rows are `.head()`; "
            "the column types are `.dtypes`.)"
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. `.head()` shows the first rows and `.dtypes` shows "
            "the types — `.describe()` returns the numeric **summary**: count, mean, "
            "std, min, quartiles and max per column."
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
    ex32_ok,
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell — the 9 core exercises plus the quiz (the trace doesn't count).
    _checks = [ex11_ok, ex12_ok, ex13_ok, ex21_ok, ex22_ok, ex23_ok, ex31_ok, ex32_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _investor = (
        "The investor pockets the USB stick and nods. That's data-driven — for real."
        if _done == _total
        else "The investor is still reading the data room, waiting for the full answer."
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

    1. Check the progress box above — all **ten** green? If not, reopen the hints,
       reread the worked examples, and try again. Load, filter, derive a column,
       group: that's the whole pandas loop, and it's the same loop on 80 rows or
       80 million.
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. Next episode: the numbers are honest. Now they need to be *seen*. You'll
       turn these totals and breakdowns into **charts the investor can't argue
       with**. **Episode 9: the pitch.**
    """
    )
    return


if __name__ == "__main__":
    app.run()
