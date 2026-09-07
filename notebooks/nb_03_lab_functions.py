# notebooks/nb_03_lab_functions.py
# Episode 3 — The Copy-Paste Soup. Session III lab notebook.
# Built from notebooks/_template.py (spec §4 rules apply):
# one global name per cell; += counts as a definition; every exercise
# pre-defines its answer (None, or a stub returning None); suffix exercise
# names (_exNN); underscore-prefixed names are cell-private; classes keep
# their natural name; never a possible infinite loop.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 3.1 — The Copy-Paste Soup
    **Estimated time: 45–60 min · Core exercises: 7 (+ 1 bonus)**

    Tobi has been "reusing" code the only way he knows how: he pasted the same
    receipt block **14 times**, once per menu item. Yesterday the wrap price
    changed by ten cents, and fixing it took him a whole afternoon. He had to
    hunt down all fourteen copies, and he *still* missed three of them.

    Today you give him the thing that ends copy-paste soup forever: the
    **function**, a named block of code you write once and call anywhere. You'll
    write functions with **parameters** and **return values**, learn why a
    function can't quietly reach out and change your variables (**scope**), give a
    parameter a **default**, and bundle data with behavior in a first **class**.
    It ends in the **Tip Calculator Championship**.
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
    mo.md(f"Kitchen open again at **{startup_name}**. Now, about all that pasting…")
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — Functions: parameters and return values
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Write it once: functions

    A **function** is a named block of code. You **define** it once with `def`,
    give it **parameters** (inputs), and it hands back a result with `return`:

    ```python
    def double_portion(grams):   # `grams` is the parameter — the input
        return grams * 2         # `return` hands the answer back to the caller
    ```

    Call it by name and it does the work every time, no pasting:
    `double_portion(150)` gives `300`.

    **`return` vs `print`** trips everyone up once. `print` *shows* a
    value on screen; `return` *hands it back* so you can store and use it. A
    function with no `return` hands back `None`. Read and run the worked example
    below and watch the difference.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — return vs print
    def _double_portion(grams):
        return grams * 2            # hands the number back to the caller

    def _show_portion(grams):
        print(grams * 2)            # shows it on screen, but hands back None

    _doubled = _double_portion(150)          # we CAPTURE the returned value
    print("double_portion handed back:", _doubled)   # 300 — usable
    _shown = _show_portion(150)              # prints 300 while running...
    print("show_portion handed back:", _shown)       # ...but this is None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — the delivery-fee function

    You already built this fee ladder by hand back in Session II. Now make it a
    **function** Tobi can call from anywhere. Write `fee_ex11(total)` that
    returns the delivery fee for an order total:

    - total **under 15 EUR** → fee **2.90**
    - total **15 up to 30 EUR** (15 counts, 30 does not) → fee **1.50**
    - total **30 EUR or more** → fee **0**

    Same logic as before, but written *once*, callable *everywhere*.
    """
    )
    return


@app.cell
def _():
    def fee_ex11(total):
        # YOUR CODE BELOW — return the delivery fee for this order total
        return None

    return (fee_ex11,)


@app.cell(hide_code=True)
def _(fee_ex11, mo, show_result):
    # Reactive check — try/except so a broken function shows ❌, never crashes.
    try:
        _a = fee_ex11(10.0)
        _b = fee_ex11(20.0)
        _c = fee_ex11(40.0)
    except Exception:
        ex11_ok = False
        _msg = "❌ Exercise 1.1: it's crashing — read the error above and fix it before the check can run."
        _preview = ""
    else:
        if _a is None:
            ex11_ok = False
            _msg = "🔲 Exercise 1.1: not attempted yet (the function still returns None)."
            _preview = ""
        elif _a == 2.90 and _b == 1.50 and _c == 0:
            ex11_ok = True
            _msg = "✅ Exercise 1.1: 2.90 / 1.50 / 0 — one function, every price band handled. Tobi never retypes the ladder again."
            _preview = show_result(_a)
        else:
            ex11_ok = False
            _msg = "❌ Exercise 1.1: the bands are off — 10 → 2.90, 20 → 1.50, 40 → 0. Check the boundaries at 15 and 30."
            _preview = show_result(_a)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Inside the function, use `if` / `elif` / `else` to pick the band, and `return` the fee for that band. Check the smallest band first, or test the boundaries carefully.",
            "💡 Hint 2 (the structure)": "def fee_ex11(total):\n    if total < 15:\n        return ___\n    elif total < 30:\n        return ___\n    else:\n        return ___   — fill the three fees.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — the tip function

    Customers can add a tip as a **percentage** of the total. Write
    `tip_ex12(total, percent)` (**two parameters** this time) that returns the
    tip amount: `percent` percent of `total`, rounded to 2 decimals.

    For example, a 10 % tip on a 20 EUR order is 2.00 EUR.
    """
    )
    return


@app.cell
def _():
    def tip_ex12(total, percent):
        # YOUR CODE BELOW — return `percent` percent of `total`, rounded to 2 decimals
        return None

    return (tip_ex12,)


@app.cell(hide_code=True)
def _(mo, show_result, tip_ex12):
    try:
        _a = tip_ex12(20, 10)
        _b = tip_ex12(12.0, 25)
    except Exception:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: it's crashing — read the error above and fix it before the check can run."
        _preview = ""
    else:
        if _a is None:
            ex12_ok = False
            _msg = "🔲 Exercise 1.2: not attempted yet (the function still returns None)."
            _preview = ""
        elif (
            isinstance(_a, (int, float)) and round(_a, 2) == 2.0
            and isinstance(_b, (int, float)) and round(_b, 2) == 3.0
        ):
            ex12_ok = True
            _msg = "✅ Exercise 1.2: 10 % of 20 is 2.00, 25 % of 12 is 3.00 — the tip line writes itself now."
            _preview = show_result(_a)
        else:
            ex12_ok = False
            _msg = "❌ Exercise 1.2: not 2.00 for `(20, 10)` — a percentage of a total is `total * percent / 100`, then round to 2 places."
            _preview = show_result(_a)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "A percentage is 'per hundred': `percent / 100` of `total`. Multiply, then wrap the whole thing in `round(..., 2)`.",
            "💡 Hint 2 (the structure)": "def tip_ex12(total, percent):\n    return round(total * ___ / ___, 2)   — fill in the percent and the 100.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Scope, a bug to fix, and default arguments
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Scope and defaults

    A parameter is the function's **own private copy** of its input. Changing it
    inside the function does **not** reach back out and change your variable.
    That separation is called **scope**, and it's what makes functions safe to
    reuse.

    A parameter can also carry a **default value**, used when the caller leaves
    it out:

    ```python
    def portion(size="regular"):
        return "a " + size + " portion"

    portion()          # "a regular portion"  ← default used
    portion("large")   # "a large portion"    ← default overridden
    ```

    Read and run the worked example, then predict, fix, and build.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — scope + defaults
    def _add_one(price):
        price = price + 1          # changes the function's OWN copy only
        return price

    _menu_price = 5
    print("the function returns:", _add_one(_menu_price))   # 6
    print("the original is untouched:", _menu_price)        # still 5

    def _portion(size="regular"):
        return "a " + size + " portion"

    print(_portion())          # default → "a regular portion"
    print(_portion("large"))   # overridden → "a large portion"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (trace — predict first) — does the global move?

    This is a **trace** exercise: predict the output first, *then* reveal the
    answer. `boost` adds one to its parameter and returns it. We call it, then
    print `x`. What does the **last line** print?

    ```python
    def boost(p):
        p = p + 1
        return p

    x = 5
    boost(x)
    print(x)
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_ex21 = mo.ui.radio(
        options=["6", "5", "Error"],
        label="Your prediction for what the last line prints:",
    )
    trace_ex21
    return (trace_ex21,)


@app.cell(hide_code=True)
def _(mo, trace_ex21):
    if trace_ex21.value is None:
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_ex21.value == "5":
        _msg = (
            "✅ Correct: it prints **5**. `boost` changes its **own copy** `p`, "
            "not `x`. And we never stored what `boost` returned — so the global "
            "`x` never moves."
        )
    else:
        _msg = (
            "❌ Not quite — it prints **5**. Inside `boost`, `p = p + 1` changes "
            "only the function's private copy; `x` out here is untouched. "
            "(Ungraded — the point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core, fix the bug) — the receipt total goes missing

    Tobi wrote `receipt_total_ex22(prices)` to add up a receipt. It runs
    without any error, and the total even appears on screen when he calls it,
    but every order total downstream comes out as **`None`**, and the app can't
    do anything with a `None`.

    His function is below. Make the total actually reach whoever called it, so
    that `receipt_total_ex22([4.0, 6.0])` gives back **10.0**.
    """
    )
    return


@app.cell
def _():
    # TOBI'S CODE — runs fine, the number even shows up, yet callers keep getting None.
    def receipt_total_ex22(prices):
        _running = 0
        for _p in prices:
            _running = _running + _p
        print(_running)

    return (receipt_total_ex22,)


@app.cell(hide_code=True)
def _(mo, receipt_total_ex22, show_result):
    try:
        _r = receipt_total_ex22([4.0, 6.0])
    except Exception:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: it's crashing now — read the error above and fix it before the check can run."
        _preview = ""
    else:
        if _r is None:
            ex22_ok = False
            _msg = (
                "❌ Exercise 2.2: the number appears on screen, but the function "
                "hands back `None`. The caller needs to **receive** the total, not "
                "just see it printed."
            )
            _preview = ""
        elif isinstance(_r, (int, float)) and round(_r, 2) == 10.0:
            ex22_ok = True
            _msg = "✅ Exercise 2.2: 10.0 comes straight back to the caller — the receipt total is usable everywhere at last."
            _preview = show_result(_r)
        else:
            ex22_ok = False
            _msg = "❌ Exercise 2.2: not 10.0 for `[4.0, 6.0]` — check what the function adds up and hands back."
            _preview = show_result(_r)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Look at the last line of the function. Showing a value on screen and handing it back to the caller are two different actions — which one is Tobi doing?",
            "💡 Hint 2 (the structure)": "def receipt_total_ex22(prices):\n    _running = 0\n    for _p in prices:\n        _running = _running + _p\n    ___ _running   — the last line decides what callers receive; fill the keyword that hands a value back.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core) — the greeting, with a default

    The order confirmation opens with a greeting. Write
    `greet_ex23(name, greeting="Moin")` that returns the line
    `"{greeting}, {name}!"`. The `greeting` parameter has a **default** of
    `"Moin"`, so:

    - `greet_ex23("Ada")` → `"Moin, Ada!"` (default used)
    - `greet_ex23("Ada", "Servus")` → `"Servus, Ada!"` (default overridden)
    """
    )
    return


@app.cell
def _():
    def greet_ex23(name, greeting="Moin"):
        # YOUR CODE BELOW — return the line "greeting, name!" (an f-string is easiest)
        return None

    return (greet_ex23,)


@app.cell(hide_code=True)
def _(greet_ex23, mo, show_result):
    try:
        _default = greet_ex23("Ada")
        _custom = greet_ex23("Ada", "Servus")
    except Exception:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: it's crashing — read the error above and fix it before the check can run."
        _preview = ""
    else:
        if _default is None:
            ex23_ok = False
            _msg = "🔲 Exercise 2.3: not attempted yet (the function still returns None)."
            _preview = ""
        elif _default == "Moin, Ada!" and _custom == "Servus, Ada!":
            ex23_ok = True
            _msg = "✅ Exercise 2.3: `Moin, Ada!` by default, `Servus, Ada!` when overridden — one function, both greetings."
            _preview = show_result(_default)
        else:
            ex23_ok = False
            _msg = (
                "❌ Exercise 2.3: not an exact match. `greet_ex23(\"Ada\")` should read "
                "`\"Moin, Ada!\"` — mind the comma, the space, and the `!`."
            )
            _preview = show_result(_default)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "The parameter default is already written for you in the signature. Inside, build the line from `greeting` and `name` — an f-string keeps the comma, space and `!` exactly right.",
            "💡 Hint 2 (the structure)": "def greet_ex23(name, greeting=\"Moin\"):\n    return f\"{___}, {___}!\"   — fill the two blanks with the parameter names, greeting first.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — A first class
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — Bundling data and behavior: a class

    A **class** is a blueprint that bundles some **data** with the **things you
    can do** with it. `__init__` runs when you build one and stores the data on
    `self`; a **method** is a function that lives inside the class and can read
    that data through `self`:

    ```python
    class Courier:
        def __init__(self, name):
            self.name = name                      # store data on the object

        def greeting(self):                       # a method — note `self`
            return "Hi, I'm " + self.name + "!"
    ```

    Build one and call its method: `Courier("Amir").greeting()` → `"Hi, I'm Amir!"`.
    Read and run the worked example, then write your own class. (In the example
    cell it's spelled `_Courier`. Real class names don't start with `_`; the
    underscore just keeps this scratch example private to its cell.)
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — a class bundles data with behavior
    class _Courier:
        def __init__(self, name):
            self.name = name

        def greeting(self):
            return "Hi, I'm " + self.name + "!"

    _amir = _Courier("Amir")
    print(_amir.greeting())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (core) — the `Order` class

    Give the startup a proper `Order`. The `__init__` is written for you: it
    stores `item`, `qty` and `price` on the order. Your job is **two methods**:

    - `total()` returns what this order costs: `qty` portions at `price` each,
      rounded to 2 decimals.
    - `receipt_line()` returns the receipt text from Episode 1, in the form
      `"2x Wrap: 13.80 EUR"`: quantity, `x`, item, colon, the total with two
      decimals, `EUR`. One method may call another: `self.total()`.

    A 2× Wrap order at 6.90 each should total **13.80**.
    """
    )
    return


@app.cell
def _():
    class Order:
        def __init__(self, item, qty, price):
            self.item = item
            self.qty = qty
            self.price = price

        def total(self):
            # YOUR CODE BELOW — return qty portions at price each, rounded to 2 decimals
            return None

        def receipt_line(self):
            # YOUR CODE BELOW — f"{qty}x {item}: {total:.2f} EUR", all from self
            return None

    return (Order,)


@app.cell(hide_code=True)
def _(Order, mo, show_result):
    try:
        _o = Order("Wrap", 2, 6.90)
        _t = _o.total()
        _line = _o.receipt_line()
    except Exception:
        ex31_ok = False
        _msg = "❌ Exercise 3.1: it's crashing — read the error above and fix it before the check can run."
        _preview = ""
    else:
        if _t is None:
            ex31_ok = False
            _msg = "🔲 Exercise 3.1: not attempted yet (`total()` still returns None)."
            _preview = ""
        elif isinstance(_t, (int, float)) and round(_t, 2) == 13.80 and _line == "2x Wrap: 13.80 EUR":
            ex31_ok = True
            _msg = "✅ Exercise 3.1: 13.80, and the receipt line writes itself. Data and behavior, bundled."
            _preview = show_result(_line)
        elif isinstance(_t, (int, float)) and round(_t, 2) == 13.80 and _line is None:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: `total()` is right — now `receipt_line()`, which still returns `None`. Build the f-string from `self.qty`, `self.item` and `self.total()`."
            _preview = show_result(_t)
        elif isinstance(_t, (int, float)) and round(_t, 2) == 13.80:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: `total()` is right, but `receipt_line()` should read exactly `2x Wrap: 13.80 EUR` — check the `x`, the colon, `:.2f` and `EUR`."
            _preview = show_result(_line)
        elif isinstance(_t, (int, float)) and round(_t, 2) == 6.90:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: that's the price of **one** portion — `total()` needs the quantity too. What should `self.qty` multiply?"
            _preview = show_result(_t)
        else:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: not 13.80 for a 2× order at 6.90 — `total()` returns `self.qty * self.price`, rounded to 2 decimals."
            _preview = show_result(_t)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex31_ok else "warn")
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Inside `total()`, reach the stored data through `self`: the quantity is `self.qty`, the unit price is `self.price`. Multiply them and round. `receipt_line()` is the Episode 1 f-string, with `self.total()` in the money slot.",
            "💡 Hint 2 (the structure)": "    def total(self):\n        return round(self.___ * self.___, 2)\n\n    def receipt_line(self):\n        return f\"{self.___}x {self.___}: {self.total():.2f} EUR\"   — fill in the attribute names.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE — the first Friday report
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 🧾 Boss exercise (core) — the first Friday report

    It's the first Friday, and the report has to go out. Three orders came in:

    | Item | Qty | Unit price |
    |------|-----|-----------|
    | Wrap | 2 | 6.90 |
    | Bowl | 1 | 24.90 |
    | Fries | 5 | 2.50 |

    Every order bills the customer its **item total plus its delivery fee**. You
    already have both tools: `Order` computes the item total, and `fee_ex11`
    computes the delivery fee **from that total**. Build the three orders, and
    for each one add up its `total()` **plus** its `fee_ex11(total())`. Store
    the grand total in `day_total_ex40`.

    Both `Order` and `fee_ex11` from earlier are in scope here. Reuse them, don't
    rewrite them. (That's the whole point of this episode.)

    *Finish 1.1 first:* while `fee_ex11` still returns `None`, this cell goes
    **red**, and a red cell pauses everything below it, including the progress
    box. Nothing is lost; fix the red cell and it all comes back.
    """
    )
    return


@app.cell
def _(Order, fee_ex11):
    # YOUR CODE BELOW — build the three orders, and sum each total() + its fee.
    # Reuse Order and fee_ex11 from the exercises above (already in scope).
    day_total_ex40 = None
    return (day_total_ex40,)


@app.cell(hide_code=True)
def _(day_total_ex40, mo, show_result):
    if day_total_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
    elif isinstance(day_total_ex40, (int, float)) and round(day_total_ex40, 2) == 58.50:
        ex40_ok = True
        _msg = "✅ Boss exercise: **58.50 EUR** billed on the first Friday — item totals plus every delivery fee. The report ships."
    elif isinstance(day_total_ex40, (int, float)) and round(day_total_ex40, 2) == 51.20:
        ex40_ok = False
        _msg = (
            "❌ Boss exercise: 51.20 is the sum of the item totals — you forgot "
            "the **delivery fees**. Add each order's `fee_ex11(total())` too."
        )
    else:
        ex40_ok = False
        _msg = (
            "❌ Boss exercise: not 58.50 — build each order, and for every one add "
            "its `total()` and its `fee_ex11(total())`."
        )
    mo.md(_msg + show_result(day_total_ex40))
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Make the three orders. Start a grand total at 0. For each order, work out its `total()` once, then add that total AND `fee_ex11` of that total to the running sum.",
            "💡 Hint 2 (the structure)": "orders = [Order(\"Wrap\", 2, 6.90), Order(\"Bowl\", 1, 24.90), Order(\"Fries\", 5, 2.50)]\nday_total_ex40 = 0\nfor order in orders:\n    _t = order.___()\n    day_total_ex40 = day_total_ex40 + _t + fee_ex11(___)\nday_total_ex40 = round(day_total_ex40, 2)   — fill the method call and the fee's argument.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# MCQ + BONUS
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ) — what lands in `result`?

    Tobi wrote a function that **prints** the total instead of **returning** it,
    then stored the call in a variable:

    ```python
    def tobis_fn():
        print(42)

    result = tobis_fn()
    ```

    What is stored in `result`? Assign the letter (as text) to `answer_ex50`:

    - **a)** `"42"`
    - **b)** `0`
    - **c)** `None`
    - **d)** an error
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
    elif str(answer_ex50).strip().lower() == "c":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **c**. `tobis_fn` prints but never `return`s, so it hands "
            "back `None` — and that `None` is what lands in `result`. Exactly the "
            "bug you fixed in 2.2."
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. `print` shows a value but hands nothing back. What "
            "does a function with no `return` give to its caller?"
        )
    mo.md(_msg)
    return (ex50_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 🏆 Bonus — the Tip Calculator Championship (not required)

    Your `tip_ex12` works on tidy inputs, but the whole class is entering their
    tip functions into a **Championship**: whose survives the weirdest receipts?
    The judges throw a battery of nasty inputs at each one: a **0** order, a
    **negative −5** refund, and a **100000** whale order, then crown the function
    that never breaks. Winner gets bragging rights and Tobi's parking spot.

    Write `tip_safe_ex60(total, percent)`: return **0.0** when `total` is zero or
    negative (no tip on nothing), otherwise the tip exactly like `tip_ex12`.
    """
    )
    return


@app.cell
def _():
    def tip_safe_ex60(total, percent):
        # YOUR CODE BELOW — 0.0 when total <= 0, otherwise percent of total rounded to 2
        return None

    return (tip_safe_ex60,)


@app.cell(hide_code=True)
def _(mo, show_result, tip_safe_ex60):
    try:
        _zero = tip_safe_ex60(0, 10)
        _neg = tip_safe_ex60(-5, 10)
        _whale = tip_safe_ex60(100000, 10)
        _normal = tip_safe_ex60(20, 10)
    except Exception:
        ex60_ok = False
        _msg = "❌ Championship: a weird receipt knocked it out — the function crashed. Guard the total before you do the math."
        _preview = ""
    else:
        if _zero is None and _normal is None:
            ex60_ok = False
            _msg = "🔲 Championship: not entered yet (the function still returns None)."
            _preview = ""
        elif _zero is None or _neg is None:
            ex60_ok = False
            _msg = "❌ Championship: a zero or negative total comes back as `None` — that branch has no `return`. Every path through the function needs one."
            _preview = ""
        elif (
            _zero == 0.0 and _neg == 0.0
            and isinstance(_whale, (int, float)) and round(_whale, 2) == 10000.0
            and isinstance(_normal, (int, float)) and round(_normal, 2) == 2.0
        ):
            ex60_ok = True
            _msg = (
                "✅ Championship: 0 → 0.0, −5 → 0.0, the 100000 whale → 10000.0, and "
                "a normal 20 → 2.0. Your function survived every weird receipt — "
                "**you win Tobi's parking spot.** 🅿️"
            )
            _preview = show_result(_zero)
        else:
            ex60_ok = False
            _msg = (
                "❌ Championship: it didn't survive the battery. A 0 or negative "
                "total must give **0.0**; a normal total tips just like `tip_ex12`."
            )
            _preview = show_result(_zero)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex60_ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Guard first: if the total is zero or negative, `return 0.0` right away. Otherwise fall through to the normal tip calculation from 1.2.",
            "💡 Hint 2 (the structure)": "def tip_safe_ex60(total, percent):\n    if total ___ 0:\n        return 0.0\n    return round(total * percent / 100, 2)   — fill the comparison that catches zero AND negatives.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# PROGRESS + WRAP-UP
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(ex11_ok, ex12_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok, mo):
    # Progress cell — core exercises only (the trace and the bonus don't count).
    _checks = [ex11_ok, ex12_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _tobi = "Tobi is genuinely impressed!" if _done == _total else "Tobi remains skeptical."
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

    1. Check the progress box above — all seven core exercises green? If not,
       that's normal: functions are the first genuinely hard idea in this course.
       Reopen the hints, reread the worked examples, and try one more time. The
       ones you fought for are the ones that stick.
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the
       tab and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. Next episode: the menu outgrows Tobi's seventeen loose variables
       (`price1`, `price2`, `price_final_FINAL2`) and nobody can find anything.
       Next week we give the data a **shape**: lists and dictionaries.
    """
    )
    return


if __name__ == "__main__":
    app.run()
