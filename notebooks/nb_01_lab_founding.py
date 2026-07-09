# notebooks/nb_01_lab_founding.py
# Episode 1 — The Founding. Session I lab notebook.
# Built from notebooks/_template.py (spec §4 rules apply):
# one global name per cell; += counts as a definition; every exercise
# pre-defines its answer as None; suffix exercise names (_exNN);
# underscore-prefixed names are cell-private.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 1.1 — The Founding
    **Estimated time: 45–60 min · Core exercises: 7 (+ 2 bonus)**

    Congratulations: as of today you are the (co-)founder of a campus
    food-delivery startup. It has **no name**, **no menu**, and a co-founder,
    **Kevin**, who has already spent 300 EUR of the marketing budget on
    stickers. Your job today: give the company a name, price a menu, run the
    first revenue numbers, and find out whether Kevin's "everything costs 9.99"
    theory survives contact with arithmetic.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    # Helper — echoes a student's current answer as a "Your result" preview so
    # they SEE their output (e.g. a receipt's alignment), not just ✅/❌. Strings
    # render in a fenced block; everything else inline. See _template.py.
    def show_result(value):
        if value is None:
            return ""
        if isinstance(value, str):
            return f"\n\n**Your result:**\n\n```\n{value}\n```"
        return f"\n\n**Your result:** `{value}`"

    return (show_result,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(
        f"First order of business — the name. Type it once and it sticks for "
        f"the whole notebook.\n\nWelcome to **{startup_name}**! "
        f"(Kevin already forgot it.)"
    )
    return (startup_name,)


@app.cell(hide_code=True)
def _(mo):
    startup_name_input = mo.ui.text(
        label="Your startup's name:", placeholder="e.g. SnackRocket"
    )
    startup_name_input
    return (startup_name_input,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — Variables & types
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Variables & types

    A **variable** is a labelled box you put a value in. The value has a
    **type**: text is a `str` (`"Pad Thai"`), whole numbers are `int` (`3`),
    and decimals are `float` (`8.90`). Python figures out the type from the
    value you assign. Read and run the worked example, then do the exercises.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this)
    example_item = "Cappuccino"      # str
    example_price = 3.50             # float
    example_portions = 2             # int
    print(example_item, "costs", example_price, "EUR ·", type(example_price))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — put the first menu item on the books

    Create three variables describing your signature dish:

    - `menu_item_ex11` — its name, as text (any name you like)
    - `price_ex11` — its price, the float `8.90`
    - `portions_ex11` — how many a typical order contains, the int `3`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — replace each None
    menu_item_ex11 = None
    price_ex11 = None
    portions_ex11 = None
    return menu_item_ex11, portions_ex11, price_ex11


@app.cell(hide_code=True)
def _(menu_item_ex11, mo, portions_ex11, price_ex11):
    if menu_item_ex11 is None or price_ex11 is None or portions_ex11 is None:
        ex11_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
    elif not isinstance(menu_item_ex11, str):
        ex11_ok = False
        _msg = "❌ Exercise 1.1: `menu_item_ex11` should be text (a `str`)."
    elif not (isinstance(price_ex11, float) and price_ex11 == 8.90):
        ex11_ok = False
        _msg = "❌ Exercise 1.1: `price_ex11` should be the float `8.90`."
    elif not (isinstance(portions_ex11, int) and portions_ex11 == 3):
        ex11_ok = False
        _msg = "❌ Exercise 1.1: `portions_ex11` should be the int `3`."
    else:
        ex11_ok = True
        _msg = "✅ Exercise 1.1: the menu has its first entry. The investor takes a note."
    mo.md(_msg)
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Three separate assignments with `=`. Text goes in quotes; `8.90` and `3` do not.",
            "💡 Hint 2 (the structure)": "menu_item_ex11 = \"Pad Thai\"  ·  price_ex11 = 8.90  ·  portions_ex11 = 3",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — the first revenue

    One order of your dish is `portions_ex11` portions at `price_ex11` each.
    Compute the revenue of a single order into `revenue_ex12`.

    Watch out: `8.90 * 3` in Python is `26.700000000000003` (floats are
    slightly fuzzy). Wrap your result in `round(..., 2)` so it equals `26.70`
    exactly.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — use price_ex11 and portions_ex11, then round to 2 places
    revenue_ex12 = None
    return (revenue_ex12,)


@app.cell(hide_code=True)
def _(mo, revenue_ex12, show_result):
    if revenue_ex12 is None:
        ex12_ok = False
        _msg = "🔲 Exercise 1.2: not attempted yet."
    elif revenue_ex12 == 26.70:
        ex12_ok = True
        _msg = "✅ Exercise 1.2: 26.70 EUR per order. Kevin wants to spend it already."
    else:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: not 26.70 — multiply price × portions and `round(..., 2)`."
    mo.md(_msg + show_result(revenue_ex12))
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Multiply the two variables from 1.1, then round the whole thing to 2 decimal places.",
            "💡 Hint 2 (the structure)": "revenue_ex12 = round(price_ex11 * portions_ex11, 2)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Numbers & arithmetic
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Numbers & arithmetic

    Python does `+ - * /` as expected. Two more you'll use constantly:
    `//` is **floor division** (whole part) and `%` is the **remainder**
    (modulo). Kevin, meanwhile, has a Theory™: *every item should cost exactly
    9.99, "for psychological reasons".* Let's put a number on it.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core, trace) — predict before you run

    This is a **trace** exercise: predict the output first, *then* reveal the
    answer. What does this line print?

    ```python
    print(7 // 2, 7 % 2)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_ex21 = mo.ui.radio(
        options=["3 2", "3 1", "3.5 1", "1 3"],
        label="Your prediction for `print(7 // 2, 7 % 2)`:",
    )
    trace_ex21
    return (trace_ex21,)


@app.cell(hide_code=True)
def _(mo, trace_ex21):
    if trace_ex21.value is None:
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_ex21.value == "3 1":
        _msg = (
            "✅ Correct: `7 // 2` is **3** (whole part) and `7 % 2` is **1** "
            "(remainder). Together: `3 1`."
        )
    else:
        _msg = (
            "❌ Not quite. `7 // 2` keeps the whole part → **3**; `7 % 2` is the "
            "leftover → **1**. So it prints `3 1`. (This one is ungraded — the "
            "point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — Kevin's 9.99 theory, costed

    Kevin insists everything sells at **9.99**. Each dish costs you **7.40** to
    make. Compute the **margin** (selling price minus cost) into `margin_ex22`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — 9.99 minus the 7.40 cost
    margin_ex22 = None
    return (margin_ex22,)


@app.cell(hide_code=True)
def _(margin_ex22, mo, show_result):
    if margin_ex22 is None:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet."
    elif isinstance(margin_ex22, (int, float)) and round(margin_ex22, 2) == 2.59:
        ex22_ok = True
        _msg = "✅ Exercise 2.2: 2.59 EUR per dish. Kevin calls it 'basically infinite money'."
    else:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: not 2.59 — compute `9.99 - 7.40`."
    mo.md(_msg + show_result(margin_ex22))
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Margin = price − cost. Both numbers are given in the task.",
            "💡 Hint 2 (the structure)": "margin_ex22 = 9.99 - 7.40",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core, fix the bug) — Kevin multiplied a string

    Kevin tried to total three 9.99 items and wrote the line below. It *runs*,
    but the result is nonsense (`"9.999.999.99"`) because he multiplied
    **text** by 3 instead of a **number**. Fix the value so `total_ex23`
    becomes the number `29.97`.
    """
    )
    return


@app.cell
def _():
    # KEVIN'S BUG — fix the right-hand side so this is a number, not text
    total_ex23 = "9.99" * 3
    return (total_ex23,)


@app.cell(hide_code=True)
def _(mo, show_result, total_ex23):
    if isinstance(total_ex23, str):
        ex23_ok = False
        _msg = "❌ Exercise 2.3: still text (a `str`). Drop the quotes so it's a number."
    elif isinstance(total_ex23, (int, float)) and round(total_ex23, 2) == 29.97:
        ex23_ok = True
        _msg = "✅ Exercise 2.3: 29.97 — a real number. Kevin is quietly relieved."
    else:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: not 29.97 — you want `9.99 * 3` as numbers."
    mo.md(_msg + show_result(total_ex23))
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "The quotes are the problem: `\"9.99\"` is text. What is `9.99` without quotes?",
            "💡 Hint 2 (the structure)": "total_ex23 = 9.99 * 3",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — Strings & f-strings
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — Strings & f-strings

    An **f-string** builds text with values dropped into `{}` slots:
    `f"{name}: {price:.2f} EUR"`. The `:.2f` formats a number with exactly two
    decimals. Time to print the startup's first receipt line.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (core) — the first receipt line

    Using an f-string, build `receipt_ex31` so it reads **exactly**:

    ```
    3x Pad Thai: 26.70 EUR
    ```

    The number must be formatted with two decimals (`:.2f`).
    """
    )
    return


@app.cell
def _():
    # Given values for the receipt line:
    receipt_item = "Pad Thai"
    receipt_qty = 3
    receipt_total = 26.70
    # YOUR CODE BELOW — one f-string, exactly "3x Pad Thai: 26.70 EUR"
    receipt_ex31 = None
    return receipt_item, receipt_qty, receipt_total, receipt_ex31


@app.cell(hide_code=True)
def _(mo, receipt_ex31, show_result):
    if receipt_ex31 is None:
        ex31_ok = False
        _msg = "🔲 Exercise 3.1: not attempted yet."
    elif receipt_ex31 == "3x Pad Thai: 26.70 EUR":
        ex31_ok = True
        _msg = "✅ Exercise 3.1: a real receipt line. It even lines up."
    else:
        ex31_ok = False
        _msg = (
            "❌ Exercise 3.1: not an exact match. You need "
            "`\"3x Pad Thai: 26.70 EUR\"` — mind the `x`, the colon, and `:.2f`."
        )
    mo.md(_msg + show_result(receipt_ex31))
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Start the string with `f\"`. Drop the qty, item and total into `{}` slots.",
            "💡 Hint 2 (the structure)": "receipt_ex31 = f\"{receipt_qty}x {receipt_item}: {receipt_total:.2f} EUR\"",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.2 (bonus) — a two-line receipt, right-aligned

    Real receipts line the prices up. Build `receipt_multi_ex32` as **two
    lines** joined by a newline `\n`, each price right-aligned in a width-8
    field with two decimals (`:>8.2f`):

    ```
    Pad Thai        26.70
    Falafel Wrap     4.60
    ```

    (The prices are `26.70` and `4.60`. Bonus — not required.)
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — two lines joined by "\n", prices formatted with :>8.2f
    receipt_multi_ex32 = None
    return (receipt_multi_ex32,)


@app.cell(hide_code=True)
def _(mo, receipt_multi_ex32, show_result):
    _expected = f"Pad Thai {26.70:>8.2f}\nFalafel Wrap {4.60:>8.2f}"
    if receipt_multi_ex32 is None:
        ex32_ok = False
        _msg = "🔲 Bonus 3.2: not attempted yet."
    elif receipt_multi_ex32 == _expected:
        ex32_ok = True
        _msg = "✅ Bonus 3.2: pixel-perfect alignment. Kevin is weirdly moved."
    else:
        ex32_ok = False
        _msg = "❌ Bonus 3.2: not an exact match — check the `\\n` and the `:>8.2f` widths."
    mo.md(_msg + show_result(receipt_multi_ex32))
    return (ex32_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Two f-string pieces joined by `\\n`. Each price uses `{value:>8.2f}`.",
            "💡 Hint 2 (the structure)": "receipt_multi_ex32 = f\"Pad Thai {26.70:>8.2f}\\nFalafel Wrap {4.60:>8.2f}\"",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE — resolve the episode
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 🥊 Boss exercise (core) — the day-one summary

    Word arrives that **MunchCorp**, the soulless mega-competitor, just
    launched "the same app but worse". Time to show the investor your numbers.

    Write `day_one_summary_ex40`: **one f-string** that mentions your startup
    name and contains both **`26.70`** (the day-one revenue) and **`2.59`**
    (Kevin's margin), each formatted with two decimals. For example:

    ```
    SnackRocket day one: 26.70 EUR revenue, 2.59 EUR margin per dish.
    ```

    The grader only checks the numbers, so your wording (and name) can be
    anything.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — one f-string mentioning your name + the two numbers
    day_one_summary_ex40 = None
    return (day_one_summary_ex40,)


@app.cell(hide_code=True)
def _(day_one_summary_ex40, mo, show_result):
    if day_one_summary_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
    elif not isinstance(day_one_summary_ex40, str):
        ex40_ok = False
        _msg = "❌ Boss exercise: `day_one_summary_ex40` should be a string (an f-string)."
    elif "26.70" in day_one_summary_ex40 and "2.59" in day_one_summary_ex40:
        ex40_ok = True
        _msg = "✅ Boss exercise: numbers on the table. The investor stops MunchCorp mid-sentence."
    else:
        ex40_ok = False
        _msg = "❌ Boss exercise: the text must contain both `26.70` and `2.59` (use `:.2f`)."
    mo.md(_msg + show_result(day_one_summary_ex40))
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "One f-string. Put the two numbers in `{}` slots with `:.2f`, and your name too.",
            "💡 Hint 2 (the structure)": "day_one_summary_ex40 = f\"{startup_name} day one: {26.70:.2f} EUR revenue, {2.59:.2f} EUR margin per dish.\"",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus — the price war

    MunchCorp lists your dish at **8.50**. To undercut them you want to be
    **10% cheaper**. Compute that price into `price_war_ex60`.
    (Bonus — not required.)
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — 10% below 8.50
    price_war_ex60 = None
    return (price_war_ex60,)


@app.cell(hide_code=True)
def _(mo, price_war_ex60, show_result):
    if price_war_ex60 is None:
        ex60_ok = False
        _msg = "🔲 Bonus price war: not attempted yet."
    elif isinstance(price_war_ex60, (int, float)) and round(price_war_ex60, 2) == 7.65:
        ex60_ok = True
        _msg = "✅ Bonus price war: 7.65 EUR. MunchCorp's growth team notices."
    else:
        ex60_ok = False
        _msg = "❌ Bonus price war: not 7.65 — take 90% of 8.50."
    mo.md(_msg + show_result(price_war_ex60))
    return (ex60_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ) — which is a valid variable name?

    Answer by assigning the letter (as text) to `answer_ex50`:

    - **a)** `2nd_price`
    - **b)** `menu_item`
    - **c)** `class`
    - **d)** `my-price`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — replace None with "a", "b", "c", or "d"
    answer_ex50 = None
    return (answer_ex50,)


@app.cell(hide_code=True)
def _(answer_ex50, mo):
    if answer_ex50 is None:
        ex50_ok = False
        _msg = "🔲 Quiz: not attempted yet."
    elif str(answer_ex50).strip().lower() == "b":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **b**. `2nd_price` can't start with a digit, `class` is a "
            "reserved word, and `my-price` has a minus sign. `menu_item` is fine."
        )
    else:
        ex50_ok = False
        _msg = "❌ Quiz: not quite. Which name starts with a letter, has no `-`, and isn't a Python keyword?"
    mo.md(_msg)
    return (ex50_ok,)


# ─────────────────────────────────────────────────────────────────────────
# PROGRESS + WRAP-UP
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(ex11_ok, ex12_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok, mo):
    # Progress cell — core exercises only (the trace and bonuses don't count).
    _checks = [ex11_ok, ex12_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _kevin = "Kevin is genuinely impressed!" if _done == _total else "Kevin remains skeptical."
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} ✅** — {_kevin}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave 📦

    1. Check the progress box above — all seven core exercises green?
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the
       tab and reopening the link starts you fresh — the download is the only
       guaranteed copy.
    3. Next episode: the city bans deliveries after 22:00, and Kevin wants to
       build a haggling bot. You'll need `if` and loops.
    """
    )
    return


if __name__ == "__main__":
    app.run()
