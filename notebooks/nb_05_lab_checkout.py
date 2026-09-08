# notebooks/nb_05_lab_checkout.py
# Episode 5 — The 3-AM Checkout. Session V lab notebook.
# Built from notebooks/_template.py (spec §4 rules apply):
# one global name per cell; += counts as a definition; every exercise
# pre-defines its answer (None, or an empty container); suffix exercise
# names (_exNN); underscore-prefixed names are cell-private; never a possible
# infinite loop. Tobi's bugs are logic/runtime only, always terminating.
# This is the ERRORS lab: students cause exceptions on purpose, so the marimo
# "red cell pauses everything below" behavior is taught early as a feature.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 5.1 — The 3-AM Checkout
    **Estimated time: 45–60 min · Core exercises: 7 (+ 1 trace, 2 bonus)**

    It's the last lab of Part I, and it opens on a crime scene. At 3 AM, running
    on his fourth energy drink, Tobi rewrote the entire checkout "to make it
    faster." He then went to sleep very pleased with himself. This morning, two
    things are true: the checkout is a minefield of crashes, and the **health
    inspector** just called to announce a surprise visit.

    So today you learn to work *with* things going wrong. You'll read a
    **traceback** (Python's crash report), catch failures with **try/except**,
    let your own code **refuse** bad input with **raise**, guard invariants with
    **assert**, and debug Tobi's 3-AM checkout line by line, before the
    inspector finds the bodies.
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    # Helper: echoes a student's current answer as a "Your result" preview so
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
        f"Back at **{startup_name}**, mop in one hand, debugger in the other. "
        "Let's clean up the checkout."
    )
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1 — Tracebacks and try/except
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Reading the crash: tracebacks and `try` / `except`

    When Python hits something it can't do, it stops and prints a **traceback**,
    a crash report. It looks scary, but it's read from the **bottom up**: the
    **last line** names *what* went wrong, and the lines above show *where*.

    ```
    Traceback (most recent call last):
      File "checkout.py", line 12, in <module>
        price = menu["Wrap"]
    KeyError: 'Wrap'
    ```

    Read the last line first: **`KeyError: 'Wrap'`**, a key that isn't in the
    dictionary. A few you'll meet constantly:

    - **`KeyError`**: a dictionary key that doesn't exist
    - **`ValueError`**: the right type but a nonsense value (`int("drei")`)
    - **`TypeError`**: the wrong type entirely (`"5" + 5`)
    - **`IndexError`**: a list position past the end

    You don't have to let a crash win. A **`try` / `except`** block runs risky
    code and catches the failure instead of stopping the program:

    ```python
    try:
        n = int("drei")      # this raises ValueError...
    except ValueError:
        n = 0                # ...and we land here instead of crashing
    ```

    **One marimo habit, important today.** In this lab you will cause errors
    **on purpose**. When a cell goes **red**, every cell below it pauses,
    including the progress box at the end. Nothing is lost. Read the error, fix
    the red cell, and everything below springs back to life. **That loop (crash,
    read, fix, recover) is what debugging *is*.**

    Read and run the worked example, then start.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this): try/except turns a crash into a recovery
    _raw = "twelve"
    try:
        _n = int(_raw)          # int("twelve") raises ValueError...
    except ValueError:
        _n = 0                  # ...caught here, so the program keeps going
    print("parsed value:", _n)  # 0: recovered instead of crashing
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (trace — predict first) — which crash?

    This is a **trace** exercise: predict the result first, *then* reveal it.
    Tobi's menu uses a capital W, but his lookup doesn't:

    ```python
    menu = {"Wrap": 6.90}
    print(menu["wrap"])
    ```

    What happens when this runs?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_ex11 = mo.ui.radio(
        options=[
            "a) it prints 6.90",
            "b) it prints None",
            "c) it raises a TypeError",
            "d) it raises a KeyError",
        ],
        label="Your prediction for `menu[\"wrap\"]`:",
    )
    trace_ex11
    return (trace_ex11,)


@app.cell(hide_code=True)
def _(mo, trace_ex11):
    if trace_ex11.value is None:
        _msg = "🔲 Pick a prediction above first. Commit before you peek!"
    elif trace_ex11.value.startswith("d"):
        _msg = (
            "✅ Correct: **a `KeyError`**. Square-bracket lookup demands the key "
            "exist *exactly*: `\"wrap\"` (lowercase) is not `\"Wrap\"`, so Python "
            "raises `KeyError: 'wrap'`. When you meet a traceback, **read the last "
            "line first**: it names what went wrong. (Ungraded. The point is the "
            "prediction.)"
        )
    else:
        _msg = (
            "❌ Not quite: it's a **`KeyError`**. The key `\"wrap\"` doesn't exist "
            "(the menu has `\"Wrap\"`, capital W), and square brackets refuse a "
            "missing key. Next time you see a traceback, read the **last line** "
            "first. It would say `KeyError: 'wrap'`. (Ungraded.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — the price box that won't crash

    Customers type prices into a box, and some of them type `"drei"` instead of
    `3`. Right now that crashes the whole checkout. Write `safe_price_ex12(text)`
    that returns `float(text)` when it can, but if the text isn't a number,
    catch the **`ValueError`** and return `0.0` instead of crashing.
    """
    )
    return


@app.cell
def _():
    def safe_price_ex12(text):
        # YOUR CODE BELOW: return float(text), or 0.0 if that raises ValueError
        return None

    return (safe_price_ex12,)


@app.cell(hide_code=True)
def _(mo, safe_price_ex12, show_result):
    # Reactive check: try/except so a broken function shows ❌, never crashes.
    try:
        _good = safe_price_ex12("4.20")
        _bad = safe_price_ex12("drei")
    except Exception:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: it's crashing. A bad value should be *caught*, not passed on. Read the error above and wrap the conversion in `try` / `except ValueError`."
        _preview = ""
    else:
        if _good is None and _bad is None:
            ex12_ok = False
            _msg = "🔲 Exercise 1.2: not attempted yet (the function still returns None)."
            _preview = ""
        elif (
            isinstance(_good, float) and round(_good, 2) == 4.20
            and isinstance(_bad, float) and _bad == 0.0
        ):
            ex12_ok = True
            _msg = "✅ Exercise 1.2: `\"4.20\"` → 4.2, `\"drei\"` → 0.0. The checkout survives a customer who can't type. That's `try` / `except` earning its keep."
            _preview = show_result(_good)
        elif _bad == 0.0 and not isinstance(_bad, float):
            ex12_ok = False
            _msg = "❌ Exercise 1.2: `\"drei\"` came back as the integer `0`. Return the float `0.0` in the `except`, so the checkout stays in floats."
            _preview = show_result(_bad)
        elif _bad != 0.0:
            ex12_ok = False
            _msg = "❌ Exercise 1.2: `\"drei\"` should come back as `0.0`, not crash or return something else. Catch `ValueError` in the `except` and return `0.0` there."
            _preview = show_result(_bad)
        else:
            ex12_ok = False
            _msg = "❌ Exercise 1.2: a real number like `\"4.20\"` should convert to the float `4.2`. Return `float(text)` in the `try`, `0.0` in the `except`."
            _preview = show_result(_good)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Put the risky line, `float(text)`, inside a `try`. If it works, `return` the number. Add `except ValueError:` underneath and `return 0.0` there for the case where the text isn't a number.",
            "💡 Hint 2 (the structure)": "def safe_price_ex12(text):\n    try:\n        return float(___)\n    except ValueError:\n        return ___   (fill the conversion and the safe fallback)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Fixing the checkout, and raising your own errors
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — The inspector's rule: fixing bugs and `raise`

    The health inspector has one non-negotiable rule for the till: **every order
    must have a price of at least 0**, no negative prices, ever. (Tobi once
    "refunded" a salad by typing `-8.30`, and the books never recovered.)

    Sometimes *your own* code should refuse bad input on the spot. The **`raise`**
    statement throws an error deliberately, stopping the bad value before it
    spreads:

    ```python
    def check_age(age):
        if age < 0:
            raise ValueError("age cannot be negative")
        return True
    ```

    Calling `check_age(-5)` raises `ValueError`, exactly like Python's own
    crashes, but on *your* terms. Read and run the worked example, then face
    Tobi's checkout.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this): raise refuses bad input; try/except sees it
    def _check_age(age):
        if age < 0:
            raise ValueError("age cannot be negative")
        return True

    try:
        _check_age(-5)                     # this raises...
    except ValueError as _e:
        print("refused:", _e)              # refused: age cannot be negative
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core, fix the bug) — the 3-AM receipt

    Here is Tobi's checkout, exactly as he left it at 3 AM. The order is **two
    Founders Bowls at 10.90** each, plus **one side salad at 8.30**. The customer
    owes **30.10**. This cell *runs* (no red error), but it's wrong **twice
    over**: the number it stores is too small, and the receipt it prints shows a
    *different* too-small number.

    Fix both so `checkout_total_ex21` holds the real total **and** the printed
    receipt shows that same total.
    """
    )
    return


@app.cell
def _():
    # TOBI'S 3-AM CHECKOUT: it runs, no crash. But every number here is wrong.
    _old_total = 10.90 + 8.30                  # a leftover from the one-bowl draft
    checkout_total_ex21 = 10.90 * 2 - 8.30     # "subtracted the salad for psychological reasons"
    _summary = f"Receipt total: {_old_total:.2f} EUR"
    print(_summary)
    return (checkout_total_ex21,)


@app.cell(hide_code=True)
def _(checkout_total_ex21, mo, show_result):
    if not isinstance(checkout_total_ex21, (int, float)):
        ex21_ok = False
        _msg = "❌ Exercise 2.1: `checkout_total_ex21` should be a **number**, the amount the customer owes."
        _preview = show_result(checkout_total_ex21)
    elif round(checkout_total_ex21, 2) == 30.10:
        ex21_ok = True
        _msg = "✅ Exercise 2.1: **30.10**, two bowls *plus* the salad. (Did you also point the receipt's f-string at `checkout_total_ex21` instead of the stale `_old_total`? Re-read the printed line to be sure.)"
        _preview = show_result(checkout_total_ex21)
    elif round(checkout_total_ex21, 2) == 13.50:
        ex21_ok = False
        _msg = "❌ Exercise 2.1: 13.50 means the salad got **subtracted**. The customer is buying the salad, not returning it. That `-` should add it in."
        _preview = show_result(checkout_total_ex21)
    else:
        ex21_ok = False
        _msg = "❌ Exercise 2.1: not 30.10. Two bowls at 10.90 *plus* one salad at 8.30. Check the operator between them."
        _preview = show_result(checkout_total_ex21)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Two bugs, both logic (nothing crashes). First: the salad is part of the order, so it should be *added*, not subtracted. Second: the receipt's f-string is formatting `_old_total` (a stale leftover) when it should format the real total instead.",
            "💡 Hint 2 (the structure)": "checkout_total_ex21 = 10.90 * 2 ___ 8.30\n_summary = f\"Receipt total: {___:.2f} EUR\"   (fix the operator, and point the receipt at the real total)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core) — enforce the inspector's rule

    Make the rule official. Write `validate_order_ex22(price)` that:

    - **raises `ValueError`** if `price` is below 0 (the inspector's line in the
      sand), and
    - otherwise **returns `True`**.

    This is your own code *refusing* bad input: a negative price never makes it
    into the books again.
    """
    )
    return


@app.cell
def _():
    def validate_order_ex22(price):
        # YOUR CODE BELOW: raise ValueError if price < 0, otherwise return True
        return None

    return (validate_order_ex22,)


@app.cell(hide_code=True)
def _(mo, validate_order_ex22):
    # Reactive check: the valid call and the "does it raise?" probe are both
    # guarded so a broken function shows ❌ instead of crashing the notebook.
    _pos = None
    try:
        _pos = validate_order_ex22(9.90)
    except Exception:
        _pos = "CRASH"
    try:
        validate_order_ex22(-1.0)
        _raised = False
    except ValueError:
        _raised = True
    except Exception:
        _raised = "WRONG"
    if _pos is None and _raised is False:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet (the function still returns None)."
    elif _pos == "CRASH":
        ex22_ok = False
        _msg = "❌ Exercise 2.2: a *valid* price (9.90) is crashing. Only negative prices should raise. A price of 9.90 should return `True`."
    elif _pos is not True:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: a valid price like 9.90 should return `True` (not None or anything else). Raise only when `price < 0`."
    elif _raised == "WRONG":
        ex22_ok = False
        _msg = "❌ Exercise 2.2: a negative price *did* raise, but not a `ValueError`. Use `raise ValueError(...)` specifically so callers can catch the right type."
    elif _raised is False:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: a negative price slipped through without raising. Add `if price < 0: raise ValueError(...)` so the bad value is refused."
    else:
        ex22_ok = True
        _msg = "✅ Exercise 2.2: 9.90 returns `True`, and −1.0 raises `ValueError`. Your code now refuses what the inspector forbids before it can hit the books."
    mo.callout(mo.md(_msg), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Check the forbidden case first with an `if`. If `price < 0`, `raise ValueError(\"...\")` with a short message. If the code gets past that `if`, the price is fine: `return True`.",
            "💡 Hint 2 (the structure)": "def validate_order_ex22(price):\n    if price < 0:\n        raise ___(\"price cannot be negative\")\n    return ___   (fill the error type and the value for a valid price)",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core) — the audit

    The inspector runs an audit. Here are the prices on today's board:

    ```python
    audit_prices_ex = [6.90, 8.90, -1.0, 11.50]
    ```

    One of them breaks the rule. Loop through the list and find the **index** (the
    position, counting from 0) of the **first price below 0**. Store it in
    `bad_index_ex23`.
    """
    )
    return


@app.cell
def _():
    audit_prices_ex = [6.90, 8.90, -1.0, 11.50]
    return (audit_prices_ex,)


@app.cell
def _():
    # YOUR CODE BELOW: the index (0-based position) of the first negative price
    bad_index_ex23 = None
    return (bad_index_ex23,)


@app.cell(hide_code=True)
def _(bad_index_ex23, mo, show_result):
    if bad_index_ex23 is None:
        ex23_ok = False
        _msg = "🔲 Exercise 2.3: not attempted yet."
        _preview = ""
    elif isinstance(bad_index_ex23, float) and bad_index_ex23 == -1.0:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: `-1.0` is the *price*, but the check wants its POSITION in the list, not the value. You want the index it sits at, counting from 0."
        _preview = show_result(bad_index_ex23)
    elif not isinstance(bad_index_ex23, int):
        ex23_ok = False
        _msg = "❌ Exercise 2.3: this should be a whole **number** (a position in the list)."
        _preview = show_result(bad_index_ex23)
    elif bad_index_ex23 == 2:
        ex23_ok = True
        _msg = "✅ Exercise 2.3: index **2**, the `-1.0` sitting third in line. Counting from 0, that's position 2. The inspector will not be pleased."
        _preview = show_result(bad_index_ex23)
    elif bad_index_ex23 == 3:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: position 3 is `-1.0`? Count again from **0**: 6.90 is at 0, 8.90 at 1, then the bad one. Indices start at zero."
        _preview = show_result(bad_index_ex23)
    else:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: not the right position. Loop with the index, and stop at the first price that is below 0 (it's the `-1.0`)."
        _preview = show_result(bad_index_ex23)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "You need the position, so loop over the indices. `for i in range(len(audit_prices_ex)):` gives you 0, 1, 2, 3; inside, check whether `audit_prices_ex[i]` is below 0 and remember that `i`.",
            "💡 Hint 2 (the structure)": "for i in range(len(audit_prices_ex)):\n    if audit_prices_ex[i] < ___:\n        bad_index_ex23 = ___   (fill the threshold and what to store)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 3 — Safe defaults when parsing fails
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 3 — A safe default when things fail

    Catching an error doesn't have to mean giving up. A common, friendly pattern
    is: **try the risky thing; if it fails, fall back to a sensible default** so
    the program keeps moving.

    ```python
    def to_int(text):
        try:
            return int(text)
        except ValueError:
            return 0            # a sane fallback instead of a crash
    ```

    `to_int("42")` → `42`; `to_int("oops")` → `0`. The caller never has to worry
    about a crash. Read and run the worked example, then build one for the till.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this): try the conversion, fall back on failure
    def _to_int(text):
        try:
            return int(text)
        except ValueError:
            return 0            # fallback when the text isn't a whole number

    print(_to_int("42"))        # 42
    print(_to_int("oops"))      # 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 3.1 (core) — how many wraps?

    The quantity box is as unreliable as the price box. Write `parse_qty_ex31(text)`
    that returns `int(text)` when it can, but if the text isn't a whole number,
    catch the **`ValueError`** and return `1` instead. (As Tobi says, *"one wrap
    is always a safe default."*)
    """
    )
    return


@app.cell
def _():
    def parse_qty_ex31(text):
        # YOUR CODE BELOW: return int(text), or 1 if that raises ValueError
        return None

    return (parse_qty_ex31,)


@app.cell(hide_code=True)
def _(mo, parse_qty_ex31, show_result):
    try:
        _good = parse_qty_ex31("3")
        _bad = parse_qty_ex31("??")
    except Exception:
        ex31_ok = False
        _msg = "❌ Exercise 3.1: it's crashing. A bad quantity should be *caught* and replaced with 1. Wrap the conversion in `try` / `except ValueError`."
        _preview = ""
    else:
        if _good is None and _bad is None:
            ex31_ok = False
            _msg = "🔲 Exercise 3.1: not attempted yet (the function still returns None)."
            _preview = ""
        elif _good == 3 and _bad == 1:
            ex31_ok = True
            _msg = "✅ Exercise 3.1: `\"3\"` → 3, `\"??\"` → 1. Garbage in, one wrap out. The checkout never stalls on a typo again."
            _preview = show_result(_good)
        elif _bad != 1:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: `\"??\"` should fall back to `1`, not crash or return something else. Return `1` inside the `except ValueError`."
            _preview = show_result(_bad)
        else:
            ex31_ok = False
            _msg = "❌ Exercise 3.1: a real quantity like `\"3\"` should convert to the int `3`. Return `int(text)` in the `try`, `1` in the `except`."
            _preview = show_result(_good)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex31_ok else "warn")
    return (ex31_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Same shape as `safe_price_ex12`, but with `int` and a fallback of `1`. Try `int(text)` and `return` it; on `except ValueError`, `return 1`.",
            "💡 Hint 2 (the structure)": "def parse_qty_ex31(text):\n    try:\n        return int(___)\n    except ValueError:\n        return ___   (fill the conversion and the safe default quantity)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE — harden the whole checkout
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 🧾 Boss exercise (core) — harden the checkout

    The inspector wants the total to survive **anything** the day throws at it.
    Here is a batch of orders, and it's a mess:

    ```python
    orders_ex40 = [("Wrap", 13.80), ("Ramen", -2.0), ("Bowl", "kaputt"), ("Thai", 8.90)]
    ```

    Two of the four are poison: `-2.0` breaks the inspector's rule, and
    `"kaputt"` isn't even a number. Write `robust_total_ex40(orders)` that **sums
    the prices of the good orders only**, skipping any price that is **negative**
    *or* **not a number**, and returns the total, rounded to 2 decimals.

    There are two ways to skip a bad price, and both are worth knowing:

    - **Ask first (type check):** `isinstance(price, (int, float))` is `True` only
      for real numbers, so check that *before* comparing to 0.
    - **Try and recover:** attempt to use the price inside a `try`, and `except`
      the failure to skip it.

    Either route earns the ✅. Pick one.
    """
    )
    return


@app.cell
def _():
    orders_ex40 = [("Wrap", 13.80), ("Ramen", -2.0), ("Bowl", "kaputt"), ("Thai", 8.90)]
    return (orders_ex40,)


@app.cell
def _(orders_ex40):
    def robust_total_ex40(orders):
        # YOUR CODE BELOW: sum prices that are numbers AND not negative; round 2.
        # (`orders` is a list of (name, price) pairs, like orders_ex40.)
        return None

    return (robust_total_ex40,)


@app.cell(hide_code=True)
def _(mo, orders_ex40, robust_total_ex40, show_result):
    # Two probes: the messy batch (22.70) and a clean list (3.0). The clean probe
    # stops anyone hardcoding 22.70 from passing.
    try:
        _messy = robust_total_ex40(orders_ex40)
        _clean = robust_total_ex40([("A", 1.0), ("B", 2.0)])
    except Exception:
        ex40_ok = False
        _msg = "❌ Boss exercise: it's crashing on the messy batch: the `\"kaputt\"` string is getting used as a number. Skip non-numbers *before* you add them (an `isinstance` check, or a `try` / `except`)."
        _preview = ""
    else:
        if _messy is None:
            ex40_ok = False
            _msg = "🔲 Boss exercise: not attempted yet (the function still returns None)."
            _preview = ""
        elif (
            isinstance(_messy, (int, float)) and round(_messy, 2) == 22.70
            and isinstance(_clean, (int, float)) and round(_clean, 2) == 3.0
        ):
            ex40_ok = True
            _msg = "✅ Boss exercise: **22.70**. Only the Wrap (13.80) and the Thai (8.90) counted; the negative and the `\"kaputt\"` were skipped. And a clean list still totals correctly, so you didn't hardcode the answer. The checkout is inspector-proof. 🧾"
            _preview = show_result(_messy)
        elif isinstance(_messy, (int, float)) and round(_messy, 2) == 20.70:
            ex40_ok = False
            _msg = "❌ Boss exercise: 20.70 means the `-2.0` slipped through: you skipped the `\"kaputt\"` string but still added the negative. Skip a price when it's **negative** *or* not a number."
            _preview = show_result(_messy)
        elif isinstance(_messy, (int, float)) and round(_messy, 2) == 13.80:
            ex40_ok = False
            _msg = "❌ Boss exercise: 13.80 is only the Wrap. The Thai (8.90) is a perfectly good order and should be counted too. Skip *only* the negative and the non-number."
            _preview = show_result(_messy)
        elif isinstance(_messy, (int, float)) and round(_messy, 2) == 22.70:
            ex40_ok = False
            _msg = "❌ Boss exercise: 22.70 for the messy list, but a clean list of `1.0` and `2.0` doesn't come out as 3.0. Either the number is hardcoded, or the function ignores its argument. Compute the total from the list it is given."
            _preview = show_result(_clean)
        else:
            ex40_ok = False
            _msg = "❌ Boss exercise: not 22.70. Add up only the prices that are numbers *and* ≥ 0, so the Wrap (13.80) and the Thai (8.90), then `round(..., 2)`."
            _preview = show_result(_messy)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Start a running total at 0 and loop over the orders. Each one is a `(name, price)` pair, so unpack it with `for name, price in orders:`. Before adding a price, make sure it's a number and not negative; if it fails either test, just skip it (don't add). Return the total rounded to 2 decimals.",
            "💡 Hint 2 (the structure)": "def robust_total_ex40(orders):\n    _total = 0\n    for _name, _price in orders:\n        if isinstance(_price, (int, float)) and _price ___ 0:\n            _total += _price\n    return round(_total, ___)   (fill the comparison, which keeps non-negatives, and the rounding)",
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
    ### Quiz (core, MCQ) — the wrong `except`

    A `try` block runs `int("drei")`, which raises a `ValueError`. The only
    handler is `except TypeError:`. What does the program do? Assign the letter
    (as text) to `answer_ex50`:

    - **a)** the `ValueError` is not caught: it crashes with a traceback
    - **b)** the `except TypeError` block runs anyway, any error counts
    - **c)** it skips the rest of the `try` quietly and continues after it
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: replace "" with "a", "b", or "c"
    answer_ex50 = ""
    return (answer_ex50,)


@app.cell(hide_code=True)
def _(answer_ex50, mo):
    if answer_ex50 == "":
        ex50_ok = False
        _msg = "🔲 Quiz: not attempted yet."
    elif str(answer_ex50).strip().lower() == "a":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **a**. An `except` only catches the type it names. A "
            "`ValueError` walks straight past `except TypeError:` and crashes the "
            "program, which is why you catch the *specific* error you expect."
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. Read the `except` line again: which error type "
            "does it name, and is that the type being raised?"
        )
    mo.md(_msg)
    return (ex50_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 🔎 Bonus — read the traceback (not required)

    Tobi's checkout module crashed overnight and left this in the log. Read it
    **bottom to top** and find the line where the error actually happened:

    ```
    Traceback (most recent call last):
      File "checkout.py", line 47, in <module>
        receipt = build_receipt(order)
      File "checkout.py", line 31, in build_receipt
        total = subtotal + surcharge(subtotal)
      File "checkout.py", line 18, in surcharge
        return round(rate * amount, 2)
    NameError: name 'rate' is not defined
    ```

    Which **line number** is the one you'd go and fix? Store it (as an integer) in
    `answer_ex60`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the line number where the error actually occurred (an int)
    answer_ex60 = None
    return (answer_ex60,)


@app.cell(hide_code=True)
def _(answer_ex60, mo, show_result):
    if answer_ex60 is None:
        ex60_ok = False
        _msg = "🔲 Bonus: not attempted yet."
        _preview = ""
    elif not isinstance(answer_ex60, int):
        ex60_ok = False
        _msg = "❌ Bonus: the answer is a **line number**, a whole number like `18`, not text."
        _preview = show_result(answer_ex60)
    elif answer_ex60 == 18:
        ex60_ok = True
        _msg = "✅ Bonus: **line 18**: the *last* frame before the error message, inside `surcharge`, where `rate` is used but never defined. The bottom frame is always where the crash truly happened; the frames above just show how you got there."
        _preview = show_result(answer_ex60)
    elif answer_ex60 == 47:
        ex60_ok = False
        _msg = "❌ Bonus: line 47 is where the *chain started* (the top frame), not where it broke. Read to the **bottom**: the last frame, line 18, is where `rate` is actually used."
        _preview = show_result(answer_ex60)
    elif answer_ex60 == 31:
        ex60_ok = False
        _msg = "❌ Bonus: line 31 is a middle frame. It *called* the broken function but isn't itself the problem. The error is raised one frame deeper, at line 18."
        _preview = show_result(answer_ex60)
    else:
        ex60_ok = False
        _msg = "❌ Bonus: look at the **last frame** listed (just above the `NameError`). Its line number is where `rate` is used without being defined."
        _preview = show_result(answer_ex60)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex60_ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 🧷 Bonus — assert the invariant (not required)

    Experienced programmers plant **`assert`** statements to guard an
    *invariant*, a fact that should always be true. If it isn't, the program
    stops immediately with an `AssertionError`, right where the assumption broke:

    ```python
    assert total >= 0, "total went negative: something is wrong upstream"
    ```

    The inspector's rule is exactly such an invariant: **every price ≥ 0**. Here
    is a board that has already passed inspection:

    ```python
    inspected_prices_ex = [6.90, 8.90, 11.50]
    ```

    Build the boolean `all_valid_ex61`: `True` if **every** price in that list is
    `>= 0`, `False` otherwise. (With that in hand, `assert all_valid_ex61` would
    be Tobi's guard rail.)
    """
    )
    return


@app.cell
def _():
    inspected_prices_ex = [6.90, 8.90, 11.50]
    return (inspected_prices_ex,)


@app.cell
def _():
    # YOUR CODE BELOW: True if every price is >= 0, else False
    all_valid_ex61 = None
    return (all_valid_ex61,)


@app.cell(hide_code=True)
def _(all_valid_ex61, mo, show_result):
    if all_valid_ex61 is None:
        ex61_ok = False
        _msg = "🔲 Bonus: not attempted yet."
        _preview = ""
    elif not isinstance(all_valid_ex61, bool):
        ex61_ok = False
        _msg = "❌ Bonus: this should be a **boolean**, `True` or `False`. `all(...)` gives you exactly that."
        _preview = show_result(all_valid_ex61)
    elif all_valid_ex61 is True:
        ex61_ok = True
        _msg = "✅ Bonus: **True**: every price on the inspected board is ≥ 0. `all(p >= 0 for p in prices)` checks the whole list at once and returns a single boolean you could hand straight to `assert`."
        _preview = show_result(all_valid_ex61)
    else:
        ex61_ok = False
        _msg = "❌ Bonus: every price in `inspected_prices_ex` really is ≥ 0, so this should be `True`. Use `all(p >= 0 for p in inspected_prices_ex)`."
        _preview = show_result(all_valid_ex61)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex61_ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`all(...)` takes a sequence of True/False tests and returns `True` only if *every* one is True. Build one test per price, `p >= 0`, across the whole list.",
            "💡 Hint 2 (the structure)": "all_valid_ex61 = all(p >= ___ for p in ___)   (fill the threshold and the list to check)",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# PROGRESS + WRAP-UP
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(
    ex12_ok,
    ex21_ok,
    ex22_ok,
    ex23_ok,
    ex31_ok,
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell: core exercises only (the trace and the two bonuses don't count).
    _checks = [ex12_ok, ex21_ok, ex22_ok, ex23_ok, ex31_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _tobi = (
        "The checkout is inspector-ready. Tobi can sleep (decaf next time)."
        if _done == _total
        else "The inspector is at the door and the till is still throwing red."
    )
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} ✅**. {_tobi}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave 📦

    1. Check the progress box above: all **seven** core exercises green? If not,
       reopen the hints, reread the worked examples, and try again. Reading a
       traceback, catching failures, and refusing bad input are the difference
       between a program that survives real users and one that doesn't.
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. That's a wrap on **Part I**: you can now store data, shape it, loop over
       it, wrap it in functions, and keep it standing when things go wrong. Next
       session opens with **Checkpoint 3**, which sweeps everything from Episodes
       1–5, so keep this notebook (and the last four) close.
    4. And the teaser: the inspector leaves satisfied. Next week someone new
       walks into the shop, uncaps a marker, and writes one question on the
       whiteboard. **Part II begins.**
    """
    )
    return


if __name__ == "__main__":
    app.run()
