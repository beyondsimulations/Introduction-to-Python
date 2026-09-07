# notebooks/nb_04_lab_menu.py
# Episode 4 — The Menu Grows Up. Session IV lab notebook.
# Built from notebooks/_template.py (spec §4 rules apply):
# one global name per cell; += counts as a definition; every exercise
# pre-defines its answer (None, or an empty container); suffix exercise
# names (_exNN); underscore-prefixed names are cell-private; never a possible
# infinite loop. Data ships as inline strings/dicts (public/ files don't load
# simply in WASM — see docs/authoring-conventions.md → Data in notebooks).
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 4.1 — The Menu Grows Up
    **Estimated time: 45–60 min · Core exercises: 9 (+ 1 trace, 2 bonus)**

    The menu has outgrown Tobi. Last week he was tracking prices in seventeen
    loose variables (`price1`, `price2`, `price_final`, and the notorious
    `price_final_FINAL2`) and nobody, Tobi included, could remember which was
    which. When a supplier raised the falafel price, he changed the wrong one and
    the till undercharged all afternoon.

    Today the data gets a **shape**. You'll line orders up in a **list** (ordered,
    sliceable), map dish names to prices in a **dictionary** (look one up
    instantly), count unique regulars with a **set**, reach into **nested**
    dictionaries, and rewrite the whole menu in a single **comprehension**. It
    ends with a courier run across campus. Tobi's forgotten wrap has to reach
    the dorms before it achieves sentience.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


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
    mo.md(
        f"Back in business at **{startup_name}**. Now let's get that menu under "
        "control."
    )
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — Lists: ordered, indexed, sliceable
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Line them up: lists

    A **list** holds many values in **order**. You write it with square brackets,
    reach any item by its **index** (counting from `0`), and take a **slice** with
    a colon. Negative indices count from the end: `-1` is the last item.

    ```python
    couriers = ["Amir", "Bea", "Cem"]
    couriers[0]      # "Amir"      ← first item, index 0
    couriers[-1]     # "Cem"       ← last item
    couriers[:2]     # ["Amir", "Bea"]   ← a slice: from the start up to (not incl.) index 2
    ```

    A list is **ordered**, so you can add to the end. `list + [item]` builds a new
    list with the item appended:

    ```python
    couriers + ["Dana"]   # ["Amir", "Bea", "Cem", "Dana"]
    ```

    Read and run the worked example, then build your own.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — index, slice, add to the end
    _couriers = ["Amir", "Bea", "Cem"]
    print("first:", _couriers[0])          # Amir
    print("last:", _couriers[-1])          # Cem
    print("first two:", _couriers[:2])     # ['Amir', 'Bea']
    print("with Dana:", _couriers + ["Dana"])   # a new, longer list
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — join the queue

    Four orders are already waiting in the kitchen queue (given below). A late
    order for a **Falafel Wrap** just came in. It goes to the **end** of the
    line. Build `queue_ex11`: the same four orders, with `"Falafel Wrap"` added
    as the last item.

    Use `+` here, not `.append()`: marimo re-runs a cell every time you edit it,
    and `.append()` would push another wrap onto the shared `queue` on every run.
    """
    )
    return


@app.cell
def _():
    queue = ["Pad Thai", "Founders Bowl", "Pizza Calzone", "Miso Ramen"]
    return (queue,)


@app.cell
def _():
    # YOUR CODE BELOW — the four-order queue plus "Falafel Wrap" at the very end
    queue_ex11 = None
    return (queue_ex11,)


@app.cell(hide_code=True)
def _(mo, queue_ex11, show_result):
    if queue_ex11 is None:
        ex11_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
        _preview = ""
    elif not isinstance(queue_ex11, list):
        ex11_ok = False
        _msg = "❌ Exercise 1.1: `queue_ex11` should be a **list** (square brackets). Add the wrap to the existing queue, don't replace it."
        _preview = show_result(queue_ex11)
    elif len(queue_ex11) == 5 and queue_ex11[-1] == "Falafel Wrap":
        ex11_ok = True
        _msg = "✅ Exercise 1.1: five orders, and the Falafel Wrap is last in line. Lists keep their order, so 'last' really means last."
        _preview = show_result(queue_ex11)
    elif len(queue_ex11) > 5 and queue_ex11[-1] == "Falafel Wrap":
        ex11_ok = False
        _msg = "❌ Exercise 1.1: more than 5 orders — `.append()` ran once per re-run of the cell and kept growing the shared `queue`. Use `queue + [\"Falafel Wrap\"]`, which leaves `queue` alone."
        _preview = show_result(queue_ex11)
    else:
        ex11_ok = False
        _msg = "❌ Exercise 1.1: the queue should have **5** orders with `\"Falafel Wrap\"` at the **end**. Keep the original four, then add the wrap."
        _preview = show_result(queue_ex11)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "You already have `queue`. Adding one item to the end of a list is `a_list + [the_new_item]` — note the new item goes in its own brackets.",
            "💡 Hint 2 (the structure)": "queue_ex11 = queue + [___]   — put the new order (as a string, in its own list) in the blank.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — first up

    The kitchen can only start the **first three** orders in `queue`. Take them
    with a **slice** and store the result in `first_three_ex12`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — the first three orders of `queue`, by slicing
    first_three_ex12 = None
    return (first_three_ex12,)


@app.cell(hide_code=True)
def _(first_three_ex12, mo, show_result):
    if first_three_ex12 is None:
        ex12_ok = False
        _msg = "🔲 Exercise 1.2: not attempted yet."
        _preview = ""
    elif first_three_ex12 == ["Pad Thai", "Founders Bowl", "Pizza Calzone"]:
        ex12_ok = True
        _msg = "✅ Exercise 1.2: the first three orders, in order. A slice `[:3]` takes from the start up to (but not including) index 3."
        _preview = show_result(first_three_ex12)
    else:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: that's not the first three of `queue`. A slice from the start is `queue[:3]` — it stops *before* index 3."
        _preview = show_result(first_three_ex12)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "A slice uses a colon inside the brackets. Leaving the left side empty means 'from the beginning'; the right side is where to stop (that index is *not* included).",
            "💡 Hint 2 (the structure)": "first_three_ex12 = queue[:___]   — fill the stop index so you get exactly three items.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Dictionaries and sets
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Look it up: dictionaries and sets

    A **dictionary** maps a **key** to a **value**. Instead of counting positions,
    you look a value up by its key, instantly:

    ```python
    prices = {"cola": 2.50, "water": 1.00}   # key: value, comma-separated
    prices["cola"]          # 2.50           ← read by key
    prices["water"] = 1.20  # update an existing key
    prices["juice"] = 3.00  # add a brand-new key
    ```

    A **set** is a bag of values with **no duplicates**. Wrapping a list in
    `set(...)` throws the repeats away, handy for counting *unique* things:

    ```python
    seen = ["cola", "water", "cola"]
    set(seen)        # {"cola", "water"}   ← duplicates gone
    len(set(seen))   # 2                   ← how many different drinks
    ```

    Read and run the worked example, then build the menu.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — read, update, add; then unique count
    _prices = {"cola": 2.50, "water": 1.00}
    print("cola costs:", _prices["cola"])       # 2.5
    _prices["water"] = 1.20                      # update
    _prices["juice"] = 3.00                      # add a new key
    print("updated menu:", _prices)

    _seen = ["cola", "water", "cola"]
    print("unique drinks:", len(set(_seen)))     # 2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core) — the menu, from scratch

    Build the opening menu as a dictionary in `menu_ex21`, mapping each dish name
    to its price:

    | Dish | Price |
    |------|-------|
    | Falafel Wrap | 6.90 |
    | Pad Thai | 8.90 |
    | Founders Bowl | 10.40 |
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — a dict mapping each dish name (string) to its price
    menu_ex21 = {}
    return (menu_ex21,)


@app.cell(hide_code=True)
def _(menu_ex21, mo, show_result):
    _expected = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    if not menu_ex21:
        ex21_ok = False
        _msg = "🔲 Exercise 2.1: not attempted yet (the menu is still empty)."
        _preview = ""
    elif not isinstance(menu_ex21, dict):
        ex21_ok = False
        _msg = "❌ Exercise 2.1: `menu_ex21` should be a **dictionary** — curly braces, `\"name\": price` pairs."
        _preview = show_result(menu_ex21)
    elif menu_ex21 == _expected:
        ex21_ok = True
        _msg = "✅ Exercise 2.1: three dishes, three prices, each reachable by name. No more `price1`, `price2`, `price_final_FINAL2`."
        _preview = show_result(menu_ex21)
    else:
        ex21_ok = False
        _msg = "❌ Exercise 2.1: not quite — check every name and price. Keys are the dish names (as strings), values are the prices: 6.90, 8.90, 10.40."
        _preview = show_result(menu_ex21)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "A dictionary literal is `{key: value, key: value, ...}`. Here the keys are dish names in quotes and the values are the prices.",
            "💡 Hint 2 (the structure)": "menu_ex21 = {\"Falafel Wrap\": ___, \"Pad Thai\": ___, \"Founders Bowl\": ___}   — fill in the three prices.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — the winter menu

    Winter changes the menu. Starting from `menu_ex21`, make `menu_ex22` that:

    - **raises the Founders Bowl** to `10.90`, and
    - **adds** a new dish, `"Bao Box"`, at `7.80`.

    Leave the original `menu_ex21` untouched. Make a **copy** first, then change
    the copy. (Copy a dict with `dict(other)`.)
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — copy menu_ex21, raise Founders Bowl to 10.90, add Bao Box 7.80
    menu_ex22 = {}
    return (menu_ex22,)


@app.cell(hide_code=True)
def _(menu_ex21, menu_ex22, mo, show_result):
    _expected = {
        "Falafel Wrap": 6.90,
        "Pad Thai": 8.90,
        "Founders Bowl": 10.90,
        "Bao Box": 7.80,
    }
    _original = {"Falafel Wrap": 6.90, "Pad Thai": 8.90, "Founders Bowl": 10.40}
    if not menu_ex22:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet."
        _preview = ""
    elif not isinstance(menu_ex22, dict):
        ex22_ok = False
        _msg = "❌ Exercise 2.2: `menu_ex22` should be a **dictionary**. Copy the old one, then adjust the copy."
        _preview = show_result(menu_ex22)
    elif menu_ex22 == _expected and menu_ex21 != _original:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: `menu_ex22` looks right — but the ORIGINAL menu changed too. You edited `menu_ex21` through an alias; make a real copy with `dict(...)` first, then change the copy."
        _preview = show_result(menu_ex22)
    elif menu_ex22 == _expected:
        ex22_ok = True
        _msg = "✅ Exercise 2.2: Founders Bowl up to 10.90, Bao Box on the board at 7.80 — four dishes, and the original menu is safe."
        _preview = show_result(menu_ex22)
    elif menu_ex22.get("Founders Bowl") == 10.40:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: the Founders Bowl is still 10.40 — you need to **update** its value to 10.90 after copying."
        _preview = show_result(menu_ex22)
    else:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: four dishes expected — Founders Bowl at 10.90 and a new `\"Bao Box\": 7.80`, everything else unchanged."
        _preview = show_result(menu_ex22)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "First copy: `dict(menu_ex21)` gives you an independent dictionary. Then assign into it by key — one line to change Pad Thai, one line to add Miso Ramen.",
            "💡 Hint 2 (the structure)": "menu_ex22 = dict(menu_ex21)\nmenu_ex22[\"Founders Bowl\"] = ___\nmenu_ex22[___] = 7.80   — fill the new price and the new dish name.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core) — how many regulars?

    Today's orders came from these customers (some ordered more than once):

    ```python
    customers = ["mo", "lena", "mo", "tobi", "lena"]
    ```

    Tobi wants to know how many **different** people that is. Store the count of
    **unique** customers in `n_regulars_ex23`.
    """
    )
    return


@app.cell
def _():
    customers = ["mo", "lena", "mo", "tobi", "lena"]
    return (customers,)


@app.cell
def _():
    # YOUR CODE BELOW — how many DIFFERENT customers are in `customers`?
    n_regulars_ex23 = None
    return (n_regulars_ex23,)


@app.cell(hide_code=True)
def _(mo, n_regulars_ex23, show_result):
    if n_regulars_ex23 is None:
        ex23_ok = False
        _msg = "🔲 Exercise 2.3: not attempted yet."
        _preview = ""
    elif not isinstance(n_regulars_ex23, int):
        ex23_ok = False
        _msg = "❌ Exercise 2.3: this should be a whole **number** — a count of people."
        _preview = show_result(n_regulars_ex23)
    elif n_regulars_ex23 == 3:
        ex23_ok = True
        _msg = "✅ Exercise 2.3: **3** regulars — mo, lena and tobi. A set drops the repeats, `len` counts what's left."
        _preview = show_result(n_regulars_ex23)
    elif n_regulars_ex23 == 5:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: 5 is the number of *orders*, counting mo and lena twice. Turn the list into a **set** first to drop duplicates, then count."
        _preview = show_result(n_regulars_ex23)
    else:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: not the count of unique customers. `set(customers)` removes duplicates; `len(...)` counts the remaining ones."
        _preview = show_result(n_regulars_ex23)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "A set has no duplicates. Wrap the list in `set(...)` to collapse repeats, then ask how many are left with `len(...)`.",
            "💡 Hint 2 (the structure)": "n_regulars_ex23 = len(set(___))   — put the list of customers in the blank.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — Nesting, comprehensions, and a lookup bug
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — Deeper: nesting, comprehensions, and `.get()`

    Values in a dictionary can themselves be dictionaries. That's **nesting**.
    You reach inside with a second set of brackets:

    ```python
    hours = {"mon": {"open": 11, "close": 22}, "tue": {"open": 11, "close": 20}}
    hours["mon"]            # {"open": 11, "close": 22}   ← the inner dict
    hours["mon"]["close"]   # 22                          ← one level deeper
    ```

    A **dict comprehension** builds a whole new dictionary in one line, applying
    the same transform to every pair:

    ```python
    # add a 1-euro late fee to every price
    {name: round(price + 1, 2) for name, price in prices.items()}
    ```

    And when a key might be **missing**, `menu["Sushi"]` raises a `KeyError` and
    stops everything, but `menu.get("Sushi")` quietly hands back `None` instead.

    One marimo habit to know: if a cell shows a **red error**, every cell that
    depends on it, including the progress box, pauses until you fix it. Nothing
    is lost; fix the red cell and everything comes back.

    Read and run the worked example, then use all three.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — nesting + a dict comprehension
    _hours = {"mon": {"open": 11, "close": 22}, "tue": {"open": 11, "close": 20}}
    print("monday closes at:", _hours["mon"]["close"])   # 22

    _prices = {"cola": 2.50, "water": 1.00}
    _with_fee = {_name: round(_p + 1, 2) for _name, _p in _prices.items()}
    print("with a 1-euro fee:", _with_fee)               # {'cola': 3.5, 'water': 2.0}
    return


@app.cell
def _():
    zones = {
        "north": {"fee": 1.50, "minutes": 20},
        "east": {"fee": 2.00, "minutes": 25},
        "dorms": {"fee": 1.20, "minutes": 15},
    }
    return (zones,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (trace — predict first) — reaching into a nest

    This is a **trace** exercise: predict the answer first, *then* reveal it. The
    delivery zones are stored as a nested dictionary:

    ```python
    zones = {
        "north": {"fee": 1.50, "minutes": 20},
        "east":  {"fee": 2.00, "minutes": 25},
        "dorms": {"fee": 1.20, "minutes": 15},
    }
    ```

    What does `zones["north"]["fee"]` give you?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_ex31 = mo.ui.radio(
        options=[
            '{"fee": 1.50, "minutes": 20}',
            "1.50",
            "a KeyError",
        ],
        label="Your prediction for `zones[\"north\"][\"fee\"]`:",
    )
    trace_ex31
    return (trace_ex31,)


@app.cell(hide_code=True)
def _(mo, trace_ex31):
    if trace_ex31.value is None:
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_ex31.value == "1.50":
        _msg = (
            "✅ Correct: **1.50**. The first `[\"north\"]` hands you the inner dict "
            "`{\"fee\": 1.50, \"minutes\": 20}`; the second `[\"fee\"]` reaches one "
            "level deeper for the number."
        )
    else:
        _msg = (
            "❌ Not quite — it's **1.50**. `zones[\"north\"]` alone would give the "
            "whole inner dict; adding `[\"fee\"]` steps inside it to the fee. "
            "(Ungraded — the point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.2 (core) — happy hour

    Happy hour knocks **30 % off** every dish. Build `happy_ex32`: a new
    dictionary from `menu_ex22` (the winter menu) where every price is **70 % of
    the original**, each rounded to 2 decimals. Do it in a single **dict
    comprehension**.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — 30% off every price in menu_ex22, rounded to 2 decimals
    happy_ex32 = None
    return (happy_ex32,)


@app.cell(hide_code=True)
def _(happy_ex32, mo, show_result):
    _expected = {
        "Falafel Wrap": 4.83,
        "Pad Thai": 6.23,
        "Founders Bowl": 7.63,
        "Bao Box": 5.46,
    }
    if happy_ex32 is None:
        ex32_ok = False
        _msg = "🔲 Exercise 3.2: not attempted yet."
        _preview = ""
    elif not isinstance(happy_ex32, dict):
        ex32_ok = False
        _msg = "❌ Exercise 3.2: `happy_ex32` should be a **dictionary** — same keys as the menu, discounted values."
        _preview = show_result(happy_ex32)
    elif happy_ex32 == _expected:
        ex32_ok = True
        _msg = "✅ Exercise 3.2: the whole menu re-priced in one line. Comprehensions turn 'do this to every item' into a single expression."
        _preview = show_result(happy_ex32)
    elif set(happy_ex32.keys()) == set(_expected.keys()):
        ex32_ok = False
        _msg = "❌ Exercise 3.2: right dishes, wrong numbers — 30 % off means `price * 0.7`, and each result must be `round(..., 2)` (otherwise you get long tails like 6.2299999)."
        _preview = show_result(happy_ex32)
    else:
        ex32_ok = False
        _msg = "❌ Exercise 3.2: build it from `menu_ex22` so every dish is there, each at 70 % of its price, rounded to 2 decimals."
        _preview = show_result(happy_ex32)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex32_ok else "warn")
    return (ex32_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "A dict comprehension looks like `{key: new_value for key, value in something.items()}`. Here the new value is 80 % of the old price, rounded to 2 decimals.",
            "💡 Hint 2 (the structure)": "happy_ex32 = {name: round(price * ___, 2) for name, price in menu_ex22.items()}   — fill the multiplier for 30 % off.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.3 (core, fix the bug) — the price comes back empty

    Tobi wired up the price lookup, and it *looks* fine: no error, no red text.
    But every time an order for Pad Thai comes through, the price on the receipt
    **comes back empty** and the customer gets charged nothing.

    His line is below. It reads the Pad Thai price out of `menu_ex22` (your winter
    menu from 2.2). Fix it so `pad_price_ex33` holds Pad Thai's actual winter
    price.
    """
    )
    return


@app.cell
def _(menu_ex22):
    # TOBI'S CODE — an order for Pad Thai, and the price keeps coming back empty.
    # (Uses menu_ex22 from Exercise 2.2 — get that one green first.)
    pad_price_ex33 = menu_ex22.get("padthai")
    return (pad_price_ex33,)


@app.cell(hide_code=True)
def _(menu_ex22, mo, pad_price_ex33, show_result):
    if pad_price_ex33 is None and not menu_ex22:
        ex33_ok = False
        _msg = "🔲 Exercise 3.3: `menu_ex22` is still empty, so there is nothing to look up yet. Get Exercise 2.2 green first."
        _preview = ""
    elif pad_price_ex33 is None:
        ex33_ok = False
        _msg = (
            "❌ Exercise 3.3: still empty (`None`). `.get(...)` hands back `None` "
            "when the key isn't found — so the key being looked up doesn't match "
            "any dish in `menu_ex22`. Compare it, character for character, with how "
            "the dish is written in the menu."
        )
        _preview = ""
    elif isinstance(pad_price_ex33, (int, float)) and round(pad_price_ex33, 2) == 8.90:
        ex33_ok = True
        _msg = (
            "✅ Exercise 3.3: 8.90 — the key now matches the menu exactly. Bonus "
            "lesson: `.get(\"padthai\")` returned `None` instead of crashing, but "
            "square brackets — `menu_ex22[\"padthai\"]` — would have raised a "
            "`KeyError` and taken the whole till down. `.get()` is the gentle lookup."
        )
        _preview = show_result(pad_price_ex33)
    else:
        ex33_ok = False
        _msg = (
            "❌ Exercise 3.3: that's not Pad Thai's winter price. Look up the exact "
            "key from your `menu_ex22`."
        )
        _preview = show_result(pad_price_ex33)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex33_ok else "warn")
    return (ex33_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Dictionary keys are exact: capitalization and spaces all matter. Look at how Pad Thai is written as a key back in Exercise 2.2, then match it here.",
            "💡 Hint 2 (the structure)": "pad_price_ex33 = menu_ex22.get(\"___\")   — put the dish's key, spelled exactly as it appears in the menu, in the blank.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE — a day as a courier
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 🛵 Boss exercise (core) — a day as a courier

    Tobi left a Falafel Wrap sitting out, and it must reach the **dorms** before
    it achieves sentience. The campus is a **nested dictionary**: each place maps
    a direction to the place it leads to.

    You'll **walk the map**: start at a position, and for each step follow the
    direction to the next place. The trick is that the *next* position becomes the
    place you look up on the following step. Here's the pattern on a tiny
    two-stop map. Read and run it:
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — walking a map with a loop
    _mini = {
        "start": {"go": "middle"},
        "middle": {"go": "end"},
    }
    _here = "start"
    for _direction in ["go", "go"]:
        _here = _mini[_here][_direction]   # step forward; _here updates each time
    print("ended up at:", _here)           # "end"
    return


@app.cell
def _():
    campus_map = {
        "gate": {"north": "library", "east": "gym"},
        "library": {"north": "mensa", "south": "gate"},
        "mensa": {"east": "dorms", "south": "library"},
        "gym": {"west": "gate"},
        "dorms": {"west": "mensa"},
    }
    return (campus_map,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The wrap starts at the `"gate"` and must follow this route, step by step:

    ```python
    route = ["north", "north", "east"]
    ```

    Walk `campus_map` from `"gate"` along `route`, and store the place the wrap
    ends up in `destination_ex40`. (If you did it right, the wrap arrives just in
    time.)
    """
    )
    return


@app.cell
def _():
    route = ["north", "north", "east"]
    return (route,)


@app.cell
def _(campus_map, route):
    # YOUR CODE BELOW — start at "gate", follow each direction in `route`,
    # and store the final place in destination_ex40. Reuse `campus_map` and `route`.
    destination_ex40 = None
    return (destination_ex40,)


@app.cell(hide_code=True)
def _(destination_ex40, mo, show_result):
    if destination_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
    elif destination_ex40 == "dorms":
        ex40_ok = True
        _msg = (
            "✅ Boss exercise: **the dorms!** gate → library → mensa → dorms, one "
            "direction at a time. The wrap is delivered and sentience is averted. 🛵"
        )
    elif destination_ex40 == "mensa":
        ex40_ok = False
        _msg = (
            "❌ Boss exercise: the mensa is only the *third* stop — you stopped one "
            "step early. All three directions in `route` need to be followed."
        )
    else:
        ex40_ok = False
        _msg = (
            "❌ Boss exercise: not the dorms. Start at `\"gate\"`, and for each "
            "direction in `route` update your position to `campus_map[position][direction]`."
        )
    mo.callout(mo.md(_msg + show_result(destination_ex40)), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Keep a variable for where the wrap currently is, starting at \"gate\". Loop over `route`; on each step, replace that variable with the place the current direction leads to — exactly like the two-stop worked example above.",
            "💡 Hint 2 (the structure)": "_pos = \"gate\"\nfor _step in route:\n    _pos = ___[___][_step]\ndestination_ex40 = _pos   — fill in what to look up, and what to look it up BY. (Which dict holds the map? And whose exits are you reading each time around the loop?)",
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
    ### Quiz (core, MCQ) — a missing key

    The menu has no `"Sushi"`. Tobi runs:

    ```python
    menu.get("Sushi", 0)
    ```

    What happens? Assign the letter (as text) to `answer_ex50`:

    - **a)** it raises a `KeyError` and stops the program
    - **b)** it returns `None`, the usual `.get()` answer
    - **c)** it silently adds `"Sushi": 0` to the menu
    - **d)** it returns `0`, the fallback, and leaves the menu alone
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
    elif str(answer_ex50).strip().lower() == "d":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **d**. `.get()` never raises and never adds: with a second "
            "argument it hands back that fallback instead of `None`. The menu is "
            "untouched."
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. Square brackets demand the key exist. What did "
            "`menu_ex22[\"padthai\"]` threaten to do in 3.3, before `.get()` softened it?"
        )
    mo.md(_msg)
    return (ex50_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 🧾 Bonus — count the day's portions (not required)

    The day's orders arrived as one text log. Each line is a dish, a semicolon,
    and how many portions:

    ```
    Falafel Wrap;2
    Pad Thai;1
    Founders Bowl;3
    Miso Ramen;1
    ```

    It's given below as the string `order_log`. Add up **all the portions** across
    every line and store the total in `portions_ex60`.

    *(Why a string and not a file? In the browser, notebooks can't just `open()` a
    file, so day-to-day data rides along as text like this. You'll load real
    files later in the course, with pandas.)*
    """
    )
    return


@app.cell
def _():
    order_log = "Falafel Wrap;2\nPad Thai;1\nFounders Bowl;3\nMiso Ramen;1"
    return (order_log,)


@app.cell
def _():
    # YOUR CODE BELOW — total the portions (the number after each semicolon)
    portions_ex60 = None
    return (portions_ex60,)


@app.cell(hide_code=True)
def _(mo, portions_ex60, show_result):
    if portions_ex60 is None:
        ex60_ok = False
        _msg = "🔲 Bonus: not attempted yet."
        _preview = ""
    elif not isinstance(portions_ex60, int):
        ex60_ok = False
        _msg = "❌ Bonus: the total should be a whole **number**. Each portion count is text like `\"2\"` — turn it into an `int` before adding."
        _preview = show_result(portions_ex60)
    elif portions_ex60 == 7:
        ex60_ok = True
        _msg = "✅ Bonus: **7** portions (2 + 1 + 3 + 1). `.splitlines()` gives you the lines, `.split(\";\")` splits each into dish and count."
        _preview = show_result(portions_ex60)
    elif portions_ex60 == 4:
        ex60_ok = False
        _msg = "❌ Bonus: 4 is the number of *lines*, not the number of *portions*. Add up the number after each semicolon, not the count of orders."
        _preview = show_result(portions_ex60)
    else:
        ex60_ok = False
        _msg = "❌ Bonus: not 7. Split each line on `\";\"`, take the second piece, turn it into an `int`, and sum them all."
        _preview = show_result(portions_ex60)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex60_ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Start a running total at 0. Loop over `order_log.splitlines()`; for each line, `line.split(\";\")` gives `[dish, count]` — the count is still text, so wrap it in `int(...)` before adding.",
            "💡 Hint 2 (the structure)": "portions_ex60 = 0\nfor line in order_log.splitlines():\n    _parts = line.split(\";\")\n    portions_ex60 = portions_ex60 + int(_parts[___])   — fill the index of the count.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 📍 Bonus — the dorm delivery fee (not required)

    Delivery fees live in the nested `zones` dictionary from Section 3. A wrap is
    going to the **dorms**. Look up the fee for the `"dorms"` zone and store it in
    `dorms_fee_ex61`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — the delivery fee for the "dorms" zone (reach into `zones`)
    dorms_fee_ex61 = None
    return (dorms_fee_ex61,)


@app.cell(hide_code=True)
def _(dorms_fee_ex61, mo, show_result):
    if dorms_fee_ex61 is None:
        ex61_ok = False
        _msg = "🔲 Bonus: not attempted yet."
        _preview = ""
    elif isinstance(dorms_fee_ex61, (int, float)) and round(dorms_fee_ex61, 2) == 1.20:
        ex61_ok = True
        _msg = "✅ Bonus: **1.20** — two brackets deep: `zones[\"dorms\"]` gives the inner dict, `[\"fee\"]` pulls out the fee."
        _preview = show_result(dorms_fee_ex61)
    else:
        ex61_ok = False
        _msg = "❌ Bonus: not the dorm fee. Reach the inner dict with `zones[\"dorms\"]`, then take its `\"fee\"`."
        _preview = show_result(dorms_fee_ex61)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex61_ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "It's a nested lookup: first reach the dorms' inner dictionary, then take the `\"fee\"` from it — two sets of brackets.",
            "💡 Hint 2 (the structure)": "dorms_fee_ex61 = zones[\"dorms\"][___]   — fill the inner key that holds the fee.",
        }
    )
    return


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
    ex32_ok,
    ex33_ok,
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell — core exercises only (the trace and the two bonuses don't count).
    _checks = [ex11_ok, ex12_ok, ex21_ok, ex22_ok, ex23_ok, ex32_ok, ex33_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _tobi = "Tobi can finally find a price!" if _done == _total else "Tobi is still hunting for `price_final_FINAL2`."
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} ✅** — {_tobi}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave 📦

    1. Check the progress box above — all **nine** core exercises green? If not,
       reopen the hints, reread the worked examples, and try again. Lists, dicts
       and sets are the containers you'll reach for in every program from here on.
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. Next episode: with real data flowing in, things start going *wrong*: a
       customer types "free" into the price box, an order has zero items, the till
       divides by nobody. Tobi rewrites the checkout at 3 AM. What could possibly
       go wrong? Next week: **errors** — catching them before they catch you.
    """
    )
    return


if __name__ == "__main__":
    app.run()
