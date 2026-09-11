# notebooks/nb_02_lab_curfew.py
# Episode 2 — The Curfew. Session II lab notebook.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 2.1 — The Curfew
    **Core exercises: 10 (+ 2 bonus).** Done early? You're free to go. Not done when the session ends? The rest is homework.

    Overnight the city posted a decree: **no delivery after 22:00.** Your
    kitchen has to know when it is allowed to send a courier out, and when it
    must say "sorry, we're closed". Tobi's plan ("we just deliver yesterday's
    orders the next morning") did not survive first contact with a lawyer.

    Today you teach the app to **decide** (`if` / `elif` / `else`), to **repeat**
    work over every order (`for` and `while` loops), and to **tidy up** the menu
    text Tobi typed in a hurry. It ends in a price war with **MunchCorp**.
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
            "it, so fix that cell first. New here? Read "
            "[How the notebook works](https://python.tobiasvlcek.com/general/notebooks.html)."
        ),
        kind="info",
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
                "Remind me: what's the company called again? Type it once and "
                "it sticks for the whole notebook. (New tab, so we ask afresh.)"
            ),
            startup_name_input,
        ]
    )
    return (startup_name_input,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(f"Back in business at **{startup_name}**. Now, about that curfew…")
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — Conditionals: comparisons & the discount ladder
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Making decisions with `if`

    A **comparison** asks a yes/no question and answers with a **boolean**:
    `True` or `False`. `3 < 5` is `True`; `10 == 9` is `False`. You feed those
    answers to `if` / `elif` / `else` to run different code in different cases:

    ```python
    if hour < 22:
        print("Open!")
    else:
        print("Curfew: closed.")
    ```

    Read and run the worked example, then handle the curfew and a discount
    ladder.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this)
    example_hour = 20
    example_open = example_hour < 22          # a boolean: True or False
    print("At", example_hour, "o'clock, open?", example_open)
    # Three branches. Python runs the FIRST one whose condition is True:
    example_rating = 4
    if example_rating >= 5:
        print("A glowing review!")
    elif example_rating >= 3:
        print("Fine, could be faster.")
    else:
        print("Tobi answers the complaint phone.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — is the kitchen open?

    An order arrives at **23:00** (`order_hour_ex11 = 23`, given below). The
    kitchen is open **only before 22:00**. Compute the boolean `is_open_ex11`
    that says whether this order may still be delivered.

    (At 23:00 the answer should come out `False`.)
    """
    )
    return


@app.cell
def _():
    order_hour_ex11 = 23
    # YOUR CODE BELOW: compare order_hour_ex11 against the 22:00 curfew
    is_open_ex11 = None
    return is_open_ex11, order_hour_ex11


@app.cell(hide_code=True)
def _(is_open_ex11, mo, show_result):
    if is_open_ex11 is None:
        ex11_ok = False
        _msg = "Not attempted — Exercise 1.1. Assign it to `is_open_ex11` (a `print` alone doesn't count) and run the cell."
    elif is_open_ex11 is False:
        ex11_ok = True
        _msg = "Correct — Exercise 1.1: `False`: 23:00 is past curfew, so the kitchen stays shut. The law is the law."
    elif is_open_ex11 is True:
        ex11_ok = False
        _msg = "Wrong — Exercise 1.1: you got `True`, but 23:00 is *after* 22:00, so the kitchen should be closed."
    else:
        ex11_ok = False
        _msg = "Wrong — Exercise 1.1: `is_open_ex11` should be a boolean (`True`/`False`) from a comparison."
    mo.callout(mo.md(_msg + show_result(is_open_ex11)), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "The kitchen is open when the hour is *below* 22. A comparison like that gives you a `True`/`False` directly (no `if` needed).",
            "Hint 2 (the structure)": "is_open_ex11 = order_hour_ex11 ___ 22 (fill the blank with the comparison that means 'before').",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — the discount ladder

    Marketing wants to reward bigger orders:

    - order total **≥ 50 EUR** → **10 %** off
    - order total **≥ 30 EUR** → **5 %** off
    - otherwise → no discount

    A customer's cart is `order_total = 36.00` (given below). Use
    `if` / `elif` / `else` to apply the right discount and store the final price
    in `final_ex12`. Wrap it in `round(..., 2)` so it lands on a clean cent.
    """
    )
    return


@app.cell
def _():
    order_total = 36.00
    # YOUR CODE BELOW: pick the discount with if/elif/else, then round to 2 places
    final_ex12 = None
    return final_ex12, order_total


@app.cell(hide_code=True)
def _(final_ex12, mo, show_result):
    if final_ex12 is None:
        ex12_ok = False
        _msg = "Not attempted — Exercise 1.2. Assign it to `final_ex12` (a `print` alone doesn't count) and run the cell."
    elif isinstance(final_ex12, (int, float)) and round(final_ex12, 2) == 34.20:
        ex12_ok = True
        _msg = "Correct — Exercise 1.2: 34.20 EUR. 36 is in the ≥ 30 band, so 5 % off. The customer feels seen."
    else:
        ex12_ok = False
        _msg = "Wrong — Exercise 1.2: not 34.20: 36.00 sits in the ≥ 30 (but not ≥ 50) band, so take 5 % off."
    mo.callout(mo.md(_msg + show_result(final_ex12)), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Check the biggest threshold first. `elif` only runs when the `if` above it was `False`, so order matters: test ≥ 50 before ≥ 30.",
            "Hint 2 (the structure)": "if order_total >= 50:\n final_ex12 = round(order_total * ___, 2)\nelif order_total >= 30:\n final_ex12 = round(order_total * ___, 2)\nelse:\n final_ex12 = round(order_total, 2) (fill the two multipliers, 10 % off and 5 % off).",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.3 (core) — courier: go or no-go?

    The curfew is not the only rule. The courier's e-bike battery only makes it
    **5 km** there and back, so Tobi's dispatch rule is: send the courier only
    if the order is **before 22:00** *and* the ride is **at most 5 km**.

    An order comes in at **21:00** for an address **6.5 km** away (both given
    below). Combine the two comparisons with `and` into the boolean
    `dispatch_ex13`. The app reads it to decide between "courier on the way"
    and "pickup only".
    """
    )
    return


@app.cell
def _():
    order_hour_ex13 = 21
    ride_km_ex13 = 6.5
    # YOUR CODE BELOW: before curfew AND within 5 km, glued with `and`
    dispatch_ex13 = None
    return dispatch_ex13, order_hour_ex13, ride_km_ex13


@app.cell(hide_code=True)
def _(dispatch_ex13, mo, show_result):
    if dispatch_ex13 is None:
        ex13_ok = False
        _msg = "Not attempted — Exercise 1.3. Assign it to `dispatch_ex13` (a `print` alone doesn't count) and run the cell."
    elif dispatch_ex13 is False:
        ex13_ok = True
        _msg = (
            "Correct — Exercise 1.3: `False`. Still before curfew, but 6.5 km is out of range, "
            "so the app offers pickup only. Tobi wanted to bike it himself. The lawyer said no."
        )
    elif dispatch_ex13 is True:
        ex13_ok = False
        _msg = (
            "Wrong — Exercise 1.3: you got `True`, but 6.5 km is more than 5 km. Both "
            "conditions must hold for `and` to say `True`; did you use `or`?"
        )
    else:
        ex13_ok = False
        _msg = "Wrong — Exercise 1.3: `dispatch_ex13` should be a boolean (`True`/`False`) from two comparisons joined by `and`."
    mo.callout(mo.md(_msg + show_result(dispatch_ex13)), kind="success" if ex13_ok else "warn")
    return (ex13_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Two questions, one answer: is the hour below 22? Is the distance at most 5? `and` is `True` only when both are.",
            "Hint 2 (the structure)": "dispatch_ex13 = order_hour_ex13 ___ 22 and ride_km_ex13 ___ 5 (fill the two comparisons: 'before' and 'at most').",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Loops: doing the same thing to every order
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Loops over the day's orders

    Tobi built a "dashboard" that adds up the day's orders by hand. It is
    wrong by lunchtime every day. A **`for` loop** does the same step for every
    item in a list, without Tobi:

    ```python
    for price in [4.00, 6.50]:
        print(price)
    ```

    To repeat something a set number of times, loop over a **`range`**:

    - `range(5)` counts from 0 up to (but **not including**) 5
    - `range(1, 5)` starts at 1 and stops before 5
    - `range(0, 5, 2)` goes from 0 towards 5 in jumps of 2

    First a quick prediction, then you'll rebuild his dashboard properly.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (trace — predict first) — what does this print?

    This is a **trace** exercise: predict the output first, *then* reveal the
    answer. What numbers does this loop print?

    ```python
    for i in range(3):
        print(i * 2)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_ex21 = mo.ui.radio(
        options=["0, 2, 4", "2, 4, 6", "0, 1, 2"],
        label="Your prediction for the numbers printed:",
    )
    trace_ex21
    return (trace_ex21,)


@app.cell(hide_code=True)
def _(mo, trace_ex21):
    if trace_ex21.value is None:
        _msg = "Pick a prediction above first. Commit before you peek!"
    elif trace_ex21.value == "0, 2, 4":
        _msg = (
            "Correct: `range(3)` counts **0, 1, 2** (it starts at 0), and "
            "each one doubled is **0, 2, 4**."
        )
    else:
        _msg = (
            "Not quite. `range(3)` starts at **0**, so `i` is 0, 1, 2. "
            "Doubled, that prints **0, 2, 4**. (Ungraded: the point is the "
            "prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — total the day's orders

    Here is today's order log: `day_orders = [12.50, 8.90, 15.20, 9.99]`
    (given below). Loop over it and add every total into `revenue_ex22`.
    Round the final sum to 2 decimals.
    """
    )
    return


@app.cell
def _():
    day_orders = [12.50, 8.90, 15.20, 9.99]
    return (day_orders,)


@app.cell
def _(day_orders):
    # YOUR CODE BELOW: start a running total at 0, add each order with a for loop
    revenue_ex22 = None
    return (revenue_ex22,)


@app.cell(hide_code=True)
def _(mo, revenue_ex22, show_result):
    if revenue_ex22 is None:
        ex22_ok = False
        _msg = "Not attempted — Exercise 2.2. Assign it to `revenue_ex22` (a `print` alone doesn't count) and run the cell."
    elif isinstance(revenue_ex22, (int, float)) and round(revenue_ex22, 2) == 46.59:
        ex22_ok = True
        _msg = "Correct — Exercise 2.2: 46.59 EUR for the day. The real dashboard finally agrees with reality."
    else:
        ex22_ok = False
        _msg = "Wrong — Exercise 2.2: not 46.59. Start a total at 0 and add every number in `day_orders`."
    mo.callout(mo.md(_msg + show_result(revenue_ex22)), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Make a variable that starts at 0. Inside the loop, add the current order to it. After the loop, round it.",
            "Hint 2 (the structure)": "revenue_ex22 = 0\nfor order in day_orders:\n revenue_ex22 = revenue_ex22 + ___\nrevenue_ex22 = round(revenue_ex22, 2) (the blank is the loop variable).",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core, fix the bug) — Tobi miscounts the big orders

    Tobi wants to count the **big orders**, the ones of **at least 10 EUR**,
    across `[12.50, 10.00, 8.90, 15.20]`. His dashboard says **2**, but he
    counted **3** on his fingers, and this time Tobi is right.

    His loop is below. It runs fine, but the logic is just slightly off. Fix the
    comparison so `big_orders_ex23` becomes **3**.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW
    # TOBI'S CODE: "at least 10 EUR" should include an order of exactly 10.00.
    big_order_prices = [12.50, 10.00, 8.90, 15.20]
    big_orders_ex23 = 0
    for _price in big_order_prices:
        if _price > 10:      # BUG: fix this comparison
            big_orders_ex23 = big_orders_ex23 + 1
    return (big_orders_ex23,)


@app.cell(hide_code=True)
def _(big_orders_ex23, mo, show_result):
    if big_orders_ex23 == 3:
        ex23_ok = True
        _msg = "Correct — Exercise 2.3: 3 big orders. The 10.00 EUR order counts too. Tobi's fingers are vindicated."
    else:
        ex23_ok = False
        _msg = (
            f"Wrong — Exercise 2.3: the dashboard says {big_orders_ex23}, but there are 3 "
            "orders of at least 10 EUR. Does an order of exactly 10.00 count as 'at least 10'?"
        )
    mo.callout(mo.md(_msg + show_result(big_orders_ex23)), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "'At least 10' means 10 counts. `> 10` skips a price that is exactly 10. Which comparison includes the boundary?",
            "Hint 2 (the structure)": "if _price ___ 10: Swap `>` for the operator that means 'greater than or equal to'.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.4 (core) — did marketing blow the coupon budget?

    Marketing's discount ladder from Exercise 1.2 (**≥ 50 EUR → 10 %**,
    **≥ 30 EUR → 5 %**, otherwise nothing) has a catch: the founders agreed on a
    coupon budget of **10 EUR per day**. Tobi has no idea whether today stayed
    under it.

    Today's carts are `day_carts = [36.00, 12.50, 52.00, 29.99, 30.00, 41.00]`
    (given below). Loop over them, work out the discount each cart got, and add
    it all into `coupons_ex24`, rounded to 2 decimals. The check tells you
    whether the campaign survives the night.
    """
    )
    return


@app.cell
def _():
    day_carts = [36.00, 12.50, 52.00, 29.99, 30.00, 41.00]
    return (day_carts,)


@app.cell
def _(day_carts):
    # YOUR CODE BELOW: total at 0, then for each cart add 10 %, 5 % or nothing (if/elif inside the loop)
    coupons_ex24 = None
    return (coupons_ex24,)


@app.cell(hide_code=True)
def _(coupons_ex24, mo, show_result):
    if coupons_ex24 is None:
        ex24_ok = False
        _msg = "Not attempted — Exercise 2.4. Assign it to `coupons_ex24` (a `print` alone doesn't count) and run the cell."
    elif isinstance(coupons_ex24, (int, float)) and round(coupons_ex24, 2) == 10.55:
        ex24_ok = True
        _msg = (
            "Correct — Exercise 2.4: 10.55 EUR in coupons, over the 10 EUR budget. "
            "The campaign is cancelled at 22:01. Marketing calls it 'a pivot'."
        )
    elif isinstance(coupons_ex24, (int, float)) and round(coupons_ex24, 2) == 7.95:
        ex24_ok = False
        _msg = "Wrong — Exercise 2.4: 7.95 means the 52 EUR cart got 5 % instead of 10 %. Test the ≥ 50 band *before* the ≥ 30 band."
    elif isinstance(coupons_ex24, (int, float)) and round(coupons_ex24, 2) == 9.05:
        ex24_ok = False
        _msg = "Wrong — Exercise 2.4: 9.05 skips the cart of exactly 30.00. 'At least 30' includes 30; check your comparison."
    else:
        ex24_ok = False
        _msg = "Wrong — Exercise 2.4: not 10.55. Inside the loop, pick the band with if/elif/else and add that cart's discount to the total."
    mo.callout(mo.md(_msg + show_result(coupons_ex24)), kind="success" if ex24_ok else "warn")
    return (ex24_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Same accumulator as Exercise 2.2, but inside the loop sits the ladder from Exercise 1.2. Add the discount (not the price) to the running total. The 'otherwise' band adds nothing.",
            "Hint 2 (the structure)": "coupons_ex24 = 0\nfor cart in day_carts:\n if cart >= 50:\n  coupons_ex24 = coupons_ex24 + cart * ___\n elif cart >= 30:\n  coupons_ex24 = coupons_ex24 + cart * ___\ncoupons_ex24 = round(coupons_ex24, 2) (fill the two discount rates).",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — String methods: de-shouting the menu
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — Tidying text with string methods

    Tobi typed the daily special IN ALL CAPS with stray spaces. Strings have
    **methods** that return a cleaned-up copy:

    - `.strip()` removes leading/trailing spaces
    - `.title()` Capitalizes Each Word
    - `.upper()` / `.lower()` change the case

    You can **chain** them: `text.strip().title()`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (core) — fix the daily special

    The menu system received `raw_special = "  PIZZA CALZONE  "` (given below).
    Produce `clean_ex31` that reads exactly `"Pizza Calzone"`: no surrounding
    spaces, each word Capitalized.

    A misspelled method (`.tittle()`) turns the cell **red**, and a red cell
    pauses everything below it, including the progress box. Nothing is lost;
    fix the typo and it all comes back.
    """
    )
    return


@app.cell
def _():
    raw_special = "  PIZZA CALZONE  "
    # YOUR CODE BELOW: strip the spaces and Title-Case it (chain two methods)
    clean_ex31 = None
    return clean_ex31, raw_special


@app.cell(hide_code=True)
def _(clean_ex31, mo, show_result):
    if clean_ex31 is None:
        ex31_ok = False
        _msg = "Not attempted — Exercise 3.1. Assign it to `clean_ex31` (a `print` alone doesn't count) and run the cell."
    elif clean_ex31 == "Pizza Calzone":
        ex31_ok = True
        _msg = "Correct — Exercise 3.1: `Pizza Calzone`, presentable at last. The menu no longer shouts."
    else:
        ex31_ok = False
        _msg = (
            "Wrong — Exercise 3.1: not an exact match. You want `\"Pizza Calzone\"`. "
            "Strip the spaces, then Title-Case the words."
        )
    mo.callout(mo.md(_msg + show_result(clean_ex31)), kind="success" if ex31_ok else "warn")
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Chain two methods: first drop the outer spaces, then fix the capitalization. The order matters: strip first.",
            "Hint 2 (the structure)": "clean_ex31 = raw_special.___().___() (one method removes spaces, the other Capitalizes Each Word).",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.2 (core, fix the bug) — the chalkboard still shouts

    Tobi writes tonight's special on the chalkboard by code. The rule: the
    label is `"Tonight: "` followed by the special **without** the stray
    spaces and with **Each Word Capitalized**. He even calls `.strip()` and
    `.title()`, and the cell runs without a single error.

    The symptom: the chalkboard reads `Tonight:   udon deluxe  `, spaces and
    lowercase and all, as if the cleaning never happened. Fix his code so
    `label_ex32` is the tidy label.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW
    # TOBI'S CODE: clean the special, then write the chalkboard label.
    _special = "  udon deluxe  "
    _special.strip()
    _special.title()
    label_ex32 = "Tonight: " + _special
    return (label_ex32,)


@app.cell(hide_code=True)
def _(label_ex32, mo, show_result):
    if label_ex32 is None:
        ex32_ok = False
        _msg = "Not attempted — Exercise 3.2. Assign it to `label_ex32` (a `print` alone doesn't count) and run the cell."
    elif label_ex32 == "Tonight: Udon Deluxe":
        ex32_ok = True
        _msg = "Correct — Exercise 3.2: `Tonight: Udon Deluxe`. The chalkboard finally uses its indoor voice."
    elif isinstance(label_ex32, str) and " ".join(label_ex32.split()).lower() == "tonight: udon deluxe":
        ex32_ok = False
        _msg = (
            "Wrong — Exercise 3.2: the words are right, but the spaces or the capitals are still off. "
            "A string method returns a *new* string; the cleaned copy has to be kept somewhere."
        )
    else:
        ex32_ok = False
        _msg = "Wrong — Exercise 3.2: the label should be `\"Tonight: \"` plus the special, stripped and Title-Cased. What happens to the result of `.strip()` in Tobi's code?"
    mo.callout(mo.md(_msg + show_result(label_ex32)), kind="success" if ex32_ok else "warn")
    return (ex32_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "`.strip()` and `.title()` do not change the string they are called on; they hand back a cleaned copy. Tobi never stores that copy, so the label is built from the original.",
            "Hint 2 (the structure)": "_special = _special.___().___() (assign the cleaned copy back to the name before building the label; the two blanks are the methods Tobi already calls).",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE — the price war (a while loop)
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Boss exercise (core) — the price war

    The rumor was true. A letter arrives from **MunchCorp**: they now sell a
    copy of your signature dish at 8.50 EUR. Tobi, in a panic, had just raised
    yours to 11.90. You start there and cut the price by **10 %
    each round** until you finally **undercut** them (drop *below* 8.50).

    A **`while` loop** repeats *as long as* a condition holds. Count how many
    rounds of cuts it takes, and store that in `rounds_ex40`.

    ::: {.callout-warning}
    A `while` loop only stops if each pass moves it **toward** the goal. Here the
    price shrinks by 10 % every round, so it is guaranteed to fall below 8.50.
    The loop always ends. A `while` whose condition can never become `False`
    would freeze this browser tab, so always check that something changes inside.
    :::
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this): a while loop that always ends,
    # because the number it watches shrinks on every pass:
    _stickers = 3
    while _stickers > 0:
        _stickers = _stickers - 1
        print("Tobi hands out a sticker:", _stickers, "left")
    print("Out of stickers. Tobi is devastated.")
    return


@app.cell
def _():
    # YOUR CODE BELOW: start at 11.90, count rounds while you're not yet under 8.50
    rounds_ex40 = None
    return (rounds_ex40,)


@app.cell(hide_code=True)
def _(mo, rounds_ex40, show_result):
    if rounds_ex40 is None:
        ex40_ok = False
        _msg = "Not attempted — Boss exercise. Assign it to `rounds_ex40` (a `print` alone doesn't count) and run the cell."
    elif isinstance(rounds_ex40, int) and rounds_ex40 == 4:
        ex40_ok = True
        _price = 11.90
        for _ in range(rounds_ex40):
            _price = round(_price * 0.9, 2)
        _msg = (
            f"Correct — Boss exercise: **4 rounds** and the price drops to {_price:.2f} EUR, "
            "just under MunchCorp's 8.50. Tobi high-fives a lamppost."
        )
    else:
        ex40_ok = False
        if isinstance(rounds_ex40, float):
            _msg = (
                "Wrong — Boss exercise: looks like you stored the price. The check "
                "wants the number of rounds (a whole number of cuts)."
            )
        else:
            _msg = "Wrong — Boss exercise: not 4. Count each 10 % cut until the price first drops below 8.50."
    mo.callout(mo.md(_msg + show_result(rounds_ex40)), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Keep two variables: the current price and a counter. Each pass of the loop cuts the price and adds 1 to the counter. Stop once the price is below 8.50.",
            "Hint 2 (the structure)": "price = 11.90\nrounds_ex40 = 0\nwhile price >= 8.50:\n price = round(price * ___, 2)\n rounds_ex40 = rounds_ex40 + ___ (fill the 10 %-off multiplier and the step).",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# MCQ + BONUSES
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ) — which loop runs exactly 5 times?

    Which loop body runs **exactly 5 times**? Answer by assigning the letter
    (as text) to `answer_ex50`:

    - **a)** `for i in range(5):`
    - **b)** `for i in range(1, 5):`
    - **c)** `for i in range(0, 5, 2):`
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace None with "a", "b", or "c"
    answer_ex50 = None
    return (answer_ex50,)


@app.cell(hide_code=True)
def _(answer_ex50, mo):
    if answer_ex50 is None:
        ex50_ok = False
        _msg = "Not attempted — Quiz. Set `answer_ex50` to your letter and run the cell."
    elif str(answer_ex50).strip().lower() == "a":
        ex50_ok = True
        _msg = (
            "Correct — Quiz: **a**. `range(5)` gives 0, 1, 2, 3, 4: five passes. "
            "`range(1, 5)` gives only four, and `range(0, 5, 2)` steps by 2 → just three."
        )
    else:
        ex50_ok = False
        _msg = "Wrong — Quiz: not quite. Which `range(...)` produces exactly five numbers starting at 0?"
    mo.callout(mo.md(_msg), kind="success" if ex50_ok else "warn")
    return (ex50_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus — a menu discount in one line (comprehension seed)

    Here is a preview of something Session IV covers properly: a **for-loop in
    one line**, called a *list comprehension*. Build `discounted_ex60`: take
    each price in `[12.50, 10.00, 8.90, 15.20]`, knock **10 %** off, and round
    to 2 decimals, all in a single list. (Bonus, not required.)
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: one list, 10 % off each price, rounded to 2 decimals
    discounted_ex60 = None
    return (discounted_ex60,)


@app.cell(hide_code=True)
def _(discounted_ex60, mo, show_result):
    if discounted_ex60 is None:
        ex60_ok = False
        _msg = "Not attempted — Bonus comprehension. Assign it to `discounted_ex60` (a `print` alone doesn't count) and run the cell."
    elif discounted_ex60 == [11.25, 9.0, 8.01, 13.68]:
        ex60_ok = True
        _msg = "Correct — Bonus comprehension: `[11.25, 9.0, 8.01, 13.68]`, a whole loop in one line. Session IV makes this a habit."
    else:
        ex60_ok = False
        _msg = "Wrong — Bonus comprehension: expected `[11.25, 9.0, 8.01, 13.68]`: 10 % off each price, each `round(..., 2)`."
    mo.callout(mo.md(_msg + show_result(discounted_ex60)), kind="success" if ex60_ok else "warn")
    return (ex60_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "A comprehension has the shape `[ do-something-to price for price in the-list ]`. 'Do something' here is 90 % of the price, rounded.",
            "Hint 2 (the structure)": "discounted_ex60 = [round(price * ___, 2) for price in [12.50, 10.00, 8.90, 15.20]] (fill the 10 %-off multiplier).",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus — the Haggling Bot (just for fun, ungraded)

    A falafel supplier will sell you chickpeas, but won't name a price. The
    supplier has a number in mind, and you have to find the exact price they'll
    accept. Drag the slider to make an offer; the bot reacts. There's nothing
    to submit here; this one is purely for fun.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    offer_slider_ex61 = mo.ui.slider(
        start=5.00, stop=10.00, step=0.05, value=5.00,
        label="Your offer (EUR/kg):", show_value=True,
    )
    offer_slider_ex61
    return (offer_slider_ex61,)


@app.cell(hide_code=True)
def _(mo, offer_slider_ex61):
    _secret = 7.25
    _offer = offer_slider_ex61.value
    if abs(_offer - _secret) < 0.001:
        _msg = " **DEAL at 7.25 EUR/kg!** The supplier shakes your hand. Falafel is secured."
        _kind = "success"
    elif _offer < _secret:
        _msg = f" {_offer:.2f} EUR/kg is **too low**. The supplier laughs and looks away."
        _kind = "warn"
    else:
        _msg = f" {_offer:.2f} EUR/kg is **too high** (you'd be leaving money on the table)."
        _kind = "info"
    mo.callout(mo.md(_msg), kind=_kind)
    return


# ─────────────────────────────────────────────────────────────────────────
# PROGRESS + WRAP-UP
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(
    ex11_ok, ex12_ok, ex13_ok, ex22_ok, ex23_ok, ex24_ok, ex31_ok, ex32_ok, ex40_ok, ex50_ok, mo
):
    # Progress cell: core exercises only (the trace and bonuses don't count).
    _checks = [ex11_ok, ex12_ok, ex13_ok, ex22_ok, ex23_ok, ex24_ok, ex31_ok, ex32_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _tobi = "Tobi is genuinely impressed!" if _done == _total else "Tobi remains skeptical."
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} correct** · {_tobi}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave

    1. Check the progress box above: all ten core exercises green?
    2. **Download your work**: **Cmd/Ctrl+S**, then menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the
       tab and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. Next episode: Tobi has pasted the same receipt code **14 times**, and
       one small change now takes him an afternoon. Next week we teach him
       **functions**.
    """
    )
    return


if __name__ == "__main__":
    app.run()
