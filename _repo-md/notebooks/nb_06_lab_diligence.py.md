```python
# notebooks/nb_06_lab_diligence.py
# Episode 6: Due Diligence Week. Session VI lab notebook.
import marimo

app = marimo.App(width="medium", app_title="nb_06_lab_diligence")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 6.1: Due Diligence Week
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
    mo.md(
        r"""
    **Core exercises: 8 + 1 quiz (+ 1 trace, + 3 bonus).** Done early? You're free to go. Not done when the session ends? The rest is homework.

    The investor is **here**. Not on a call, not "circling back next quarter". She is
    standing in the shop with a clipboard and a very calm smile, asking to see the
    numbers by the end of the week. Real numbers: how many crates to order, what the
    ratings actually average to, what next week's demand might look like.

    Tobi's proposal is to "go on vibes". The investor's expression does not
    change. So this week you stop hand-rolling arithmetic and reach for Python's
    **standard library**: code that already ships with Python, written and tested
    by people who are not Tobi. You'll `import math` and `statistics` for
    the arithmetic, then use `random` to *rehearse* next week's
    demand, and learn why a simulation should give the same result when run twice.

    > **New this week: AI is allowed.** From this session on you may use an AI
    > assistant; see the course's [AI tools
    > guide](https://python.tobiasvlcek.com/general/ai-tools.html).
    > One thing does not change: the checks below only go green on code that
    > actually runs. AI can draft a line for you; you still have to make it work,
    > and understand it well enough to fix it when it doesn't.

    > **Also new: no hint boxes.** From this lab on, an exercise only says what
    > the result has to be. Which tool gets you there is yours to work out, with
    > the worked examples, the lecture slides and your AI assistant. Ask the AI
    > to explain, then write the line yourself.

    > **One marimo rule your AI doesn't know:** AI answers usually start with
    > `import random` or `import math`. The worked examples below import those
    > modules already, and in marimo a name can only be defined in **one**
    > cell. With a second import both cells turn red until one of the two is
    > gone, so delete the extra import line.
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
                "Before the investor sits down, remind me what the company's "
                "called? Type it once and it sticks for the whole notebook. (New "
                "tab, so we ask afresh.)"
            ),
            startup_name_input,
        ]
    )
    return (startup_name_input,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(
        f"Due diligence at **{startup_name}** begins. Clipboard out. Let's give "
        "her numbers she can trust."
    )
    return (startup_name,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 1: Don't build it, import it
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1: Don't build it, import it

    A **module** is a bundle of ready-made code that ships with Python. You don't
    rewrite it. You `import` it and use it. Three ways to bring one in:

    ```python
    import math                      # then call math.ceil(...), math.floor(...)
    import statistics as stats       # same module, shorter name: stats.mean(...)
    from math import pi              # one tool BY NAME: use pi, without any prefix
    ```

    Two `math` tools for counting whole things: **`math.ceil(x)`** rounds *up* to
    the next whole number, **`math.floor(x)`** rounds *down*. And `statistics`
    gives you `mean` (the average) and `median` (the middle value) for free: no
    hand-rolled loops, no off-by-one bugs to explain to an investor.

    Read and run the worked example, then answer for real.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this): it also imports `math` for the exercises below
    import math
    print("ceil(10 / 3):", math.ceil(10 / 3))    # 4: always rounds UP
    print("floor(10 / 3):", math.floor(10 / 3))  # 3: always rounds DOWN
    return (math,)


@app.cell
def _():
    # Worked example (read + run this): it also imports `statistics` under the alias `stats`
    import statistics as stats
    print("stats.mean([10, 20, 30]):", stats.mean([10, 20, 30]))  # 20
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core): how many crates?

    The investor wants a reorder **rule** that is right for any order size.
    Delivery bags come in crates, and you can only buy *whole* crates:

    - **75 bags** at 12 per crate is **7** crates. Six crates (72 bags) would
      leave you three bags short.
    - **48 bags** at 12 per crate is exactly **4**.

    Write `crates_needed_ex11(items, per_crate)` so it returns the number of
    whole crates that `items` bags need, as an `int`. You will use this function
    again twice in this lab.
    """
    )
    return


@app.cell
def _():
    def crates_needed_ex11(items, per_crate):
        # YOUR CODE BELOW: return the number of whole crates needed for `items` (an int)
        return None

    return (crates_needed_ex11,)


@app.cell(hide_code=True)
def _(crates_needed_ex11, mo):
    # Reactive check.
    _probes = [(75, 12), (48, 12), (1, 12), (130, 48)]
    try:
        _got = [crates_needed_ex11(_i, _p) for _i, _p in _probes]
        _err = ""
    except Exception as _e:
        _got = None
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _got is None:
        ex11_ok = False
        _msg = f"Wrong (Exercise 1.1): calling `crates_needed_ex11(75, 12)` raises an error (`{_err}`). The function has to work for any two positive numbers."
    elif all(_v is None for _v in _got):
        ex11_ok = False
        _msg = "Not attempted (Exercise 1.1): the function still returns `None`. Use `return`, not `print`, then run the cell."
    else:
        _preview = f"\n\n**Your result:** `crates_needed_ex11(75, 12)` gives `{_got[0]}`"
        if not all(isinstance(_v, int) and not isinstance(_v, bool) for _v in _got):
            ex11_ok = False
            _msg = "Wrong (Exercise 1.1): nobody sells a fraction of a crate. Every answer has to be a whole number, an `int` like `7` (not `6.25`, and not `7.0`)."
        elif _got == [7, 4, 1, 3]:
            ex11_ok = True
            _msg = "Correct (Exercise 1.1): 75 bags need **7** crates, 48 need exactly 4, a single bag still needs 1. One rule for every order size, so you never under-order."
        elif _got[0] == 6:
            ex11_ok = False
            _msg = "Wrong (Exercise 1.1): 6 crates hold 72 bags, three short of 75. Your rule rounds the wrong way."
        elif _got[1] == 5:
            ex11_ok = False
            _msg = "Wrong (Exercise 1.1): 48 bags at 12 per crate fill exactly 4 crates, but your function orders 5. An exact fit needs no extra crate."
        elif _got[2] == 0:
            ex11_ok = False
            _msg = "Wrong (Exercise 1.1): a single bag still needs one crate, but `crates_needed_ex11(1, 12)` gives 0."
        else:
            ex11_ok = False
            _msg = f"Wrong (Exercise 1.1): 75 bags at 12 per crate need 7 crates, 48 need 4, and 130 at 48 per crate need 3. Yours gives {_got[0]}, {_got[1]} and {_got[3]}."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core): the ratings report

    The investor has two piles of ratings: the online reviews, and the five
    mystery shoppers she sent herself.

    ```python
    online_ratings = [4.7, 3.6, 4.9, 4.2, 4.4, 3.8]
    shopper_ratings = [4.1, 3.9, 4.6, 4.8, 3.7]
    ```

    For any pile she wants the same three numbers, so write
    `rating_report_ex12(ratings)`. It returns a **dict** with exactly these
    keys, every value rounded to 2 decimals:

    - `"typical"`: the middle rating,
    - `"average"`: the average rating,
    - `"gap"`: the average minus the typical rating. It shows how far a few
      extreme ratings drag the average away from the middle.

    For the shoppers the report is
    `{"typical": 4.1, "average": 4.22, "gap": 0.12}`.

    **The constraint:** import the tools you need **by name**, at the top of
    your cell, and call them without any `statistics.` prefix.

    Remember the marimo rule from the top: a name can only be defined in **one**
    cell. Import here once, and every cell below can use the same names.
    """
    )
    return


@app.cell
def _():
    online_ratings = [4.7, 3.6, 4.9, 4.2, 4.4, 3.8]
    return (online_ratings,)


@app.cell
def _():
    shopper_ratings = [4.1, 3.9, 4.6, 4.8, 3.7]
    return (shopper_ratings,)


@app.cell
def _():
    # YOUR CODE BELOW: import by name here (no `statistics.` prefix in this cell), then
    # return the dict with the keys "typical", "average" and "gap", each rounded to 2
    def rating_report_ex12(ratings):
        return None

    return (rating_report_ex12,)


@app.cell(hide_code=True)
def _(mo, rating_report_ex12):
    # Reactive check.
    _cases = [
        ([4.1, 3.9, 4.6, 4.8, 3.7], (4.1, 4.22, 0.12)),
        ([4.7, 3.6, 4.9, 4.2, 4.4, 3.8], (4.3, 4.27, -0.03)),
        ([4.5, 4.9, 1.5, 4.7, 4.4], (4.5, 4.0, -0.5)),
    ]
    _keys = ("typical", "average", "gap")
    try:
        _got = [rating_report_ex12(list(_c[0])) for _c in _cases]
        _err = ""
    except Exception as _e:
        _got = None
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _got is None:
        ex12_ok = False
        _msg = f"Wrong (Exercise 1.2): calling `rating_report_ex12(shopper_ratings)` raises an error (`{_err}`). If it is a `NameError`, check which names your import really created."
    elif all(_v is None for _v in _got):
        ex12_ok = False
        _msg = "Not attempted (Exercise 1.2): the function still returns `None`. Use `return`, not `print`, then run the cell."
    else:
        _preview = f"\n\n**Your result:** `rating_report_ex12(shopper_ratings)` gives `{_got[0]}`"
        if not all(isinstance(_v, dict) for _v in _got):
            ex12_ok = False
            _msg = "Wrong (Exercise 1.2): the report has to be a **dict**, like `{\"typical\": ..., \"average\": ..., \"gap\": ...}`."
        elif not all(_k in _v for _v in _got for _k in _keys):
            ex12_ok = False
            _missing = ", ".join(f'`"{_k}"`' for _k in _keys if _k not in _got[0])
            _msg = f"Wrong (Exercise 1.2): the report is missing a key: {_missing or 'check the spelling of all three'}. The keys are `\"typical\"`, `\"average\"` and `\"gap\"`, spelled exactly like that."
        elif not all(
            isinstance(_v[_k], (int, float)) and not isinstance(_v[_k], bool)
            for _v in _got
            for _k in _keys
        ):
            ex12_ok = False
            _msg = "Wrong (Exercise 1.2): all three values have to be **numbers**."
        else:
            _r = [tuple(round(_v[_k], 2) for _k in _keys) for _v in _got]
            _want = [_c[1] for _c in _cases]
            if _r == _want:
                ex12_ok = True
                _msg = "Correct (Exercise 1.2): the shoppers are typical 4.1, average 4.22; the online reviews are typical **4.3**, average **4.27**, gap -0.03. With six ratings there is no single middle value, and the tool you imported averaged the two middle ones for you."
            elif _r[0][:2] == (4.22, 4.1):
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): `\"typical\"` and `\"average\"` are the wrong way round. Which one is the middle value, which one adds everything up and divides?"
            elif _r[0][0] != 4.1:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): the typical shopper rating is 4.1, the middle of the five ratings once they are **sorted**. Yours is not."
            elif _r[1][0] != 4.3:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): right for the five shoppers, wrong for the six online ratings. With an even number of ratings there are **two** middle values, and the typical rating sits halfway between them."
            elif [_x[1] for _x in _r] != [_x[1] for _x in _want]:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): `\"typical\"` is right, `\"average\"` is not. For the shoppers it should be 4.22."
            elif _r[0][2] == -0.12:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): the gap has the wrong sign. It is the average **minus** the typical rating, so 0.12 for the shoppers."
            else:
                ex12_ok = False
                _msg = "Wrong (Exercise 1.2): `\"typical\"` and `\"average\"` are right, `\"gap\"` is not. It is the average minus the typical rating: 0.12 for the shoppers."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.3 (core, fix the bug): the second courier

    The investor has a staffing rule: if the **typical** delivery takes longer
    than **35 minutes**, the shop hires a second courier. Last Saturday's
    delivery times, in minutes:

    ```python
    delivery_times = [31, 26, 28, 33, 34, 29, 71]
    ```

    (The 71 was a courier stuck behind a parade.) Tobi's cell runs, no red
    error, and reports **36 minutes**. He is already writing the job ad. The
    investor looks at the list, then at Tobi: "Your *typical* delivery is slower
    than six of your seven deliveries?"

    Fix Tobi's line **in place** so `typical_ex13` holds a typical delivery time
    the investor accepts. That number decides the hire.
    """
    )
    return


@app.cell
def _():
    delivery_times = [31, 26, 28, 33, 34, 29, 71]
    return (delivery_times,)


@app.cell
def _(delivery_times, stats):
    # YOUR CODE BELOW
    # TOBI'S CODE: the typical delivery time, but it is slower than six of the seven deliveries.
    typical_ex13 = stats.mean(delivery_times)
    return (typical_ex13,)


@app.cell(hide_code=True)
def _(mo, show_result, typical_ex13):
    if typical_ex13 is None:
        ex13_ok = False
        _msg = "Not attempted (Exercise 1.3). Assign it to `typical_ex13` (a `print` alone doesn't count) and run the cell."
        _preview = ""
    elif isinstance(typical_ex13, bool) or not isinstance(typical_ex13, (int, float)):
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): the typical time has to be a single **number** of minutes."
        _preview = show_result(typical_ex13)
    elif round(typical_ex13, 2) == 31:
        ex13_ok = True
        _msg = "Correct (Exercise 1.3): **31** minutes, under the 35-minute line, so no second courier for now. One parade dragged the average to 36 and over the line. The middle value did not move, and Tobi deletes the job ad."
        _preview = show_result(typical_ex13)
    elif round(typical_ex13, 2) == 36:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): still 36, slower than six of the seven deliveries. One extreme value is pulling this number up. Which summary of a list does not care how extreme its largest value is?"
        _preview = show_result(typical_ex13)
    elif round(typical_ex13, 2) == 33:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): that's the middle of the list *as written*. The typical value is the middle of the **sorted** list."
        _preview = show_result(typical_ex13)
    else:
        ex13_ok = False
        _msg = "Wrong (Exercise 1.3): not a typical delivery time for this list. Half of the deliveries should be faster than it, half slower."
        _preview = show_result(typical_ex13)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex13_ok else "warn")
    return (ex13_ok,)


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2: Rehearsing luck: the random module
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2: Rehearsing luck: the `random` module

    The investor wants a **projection** of next week's demand. You can't know the
    future, but you can *rehearse* it: the `random` module invents plausible
    numbers so you can see how a busy week might play out.

    ```python
    import random
    random.seed(0)                 # pin the dice: same seed → same "random" run
    random.randint(1, 6)           # a whole number from 1 to 6 (both ends included)
    random.choice(["a", "b", "c"]) # one item picked at random from a list
    random.shuffle(some_list)      # reorders that list in place
    ```

    The key idea for due diligence is **`random.seed(n)`**. Random numbers are
    unpredictable by design, but if you *seed* the generator with a fixed number
    first, you get the **same sequence every time**. That's what makes a
    projection you can hand over: the investor runs it and sees exactly what you
    saw.

    One marimo habit for this section: editing a loop is easy to get slightly
    wrong, and a **red error pauses everything below it**, including the progress
    box. Nothing is lost; fix the red cell and everything comes back.

    Read and run the worked example, then simulate.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this): it also imports `random` for the exercises below
    import random
    random.seed(0)
    print("three seeded dice rolls:", [random.randint(1, 6) for _ in range(3)])
    # Run this cell again: same three numbers, because the seed was pinned first.
    return (random,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core): simulate the days

    The investor wants a projection she can re-run herself, for any number of
    days and any range of demand. Write
    `simulate_days_ex21(seed, days, low, high)`. It returns a **list** of `days`
    whole numbers, each between `low` and `high` (both ends included), and the
    same `seed` must always give the same list.

    For example, `simulate_days_ex21(4, 7, 8, 30)` is
    `[15, 17, 11, 20, 23, 12, 10]`: seven days of between 8 and 30 orders.
    """
    )
    return


@app.cell
def _():
    def simulate_days_ex21(seed, days, low, high):
        # YOUR CODE BELOW: return a list of `days` random whole numbers from `low` to `high`,
        # the same list every time for the same `seed`
        return None

    return (simulate_days_ex21,)


@app.cell(hide_code=True)
def _(mo, random, simulate_days_ex21):
    # Reactive check.
    def _expect(seed, days, low, high, top=True):
        rng = random.Random(seed)
        stop = high + 1 if top else high
        return [rng.randrange(low, stop) for _ in range(days)]

    _probes = [(4, 7, 8, 30), (1, 3, 1, 6), (21, 5, 10, 25)]
    try:
        _got = [simulate_days_ex21(*_p) for _p in _probes]
        _again = simulate_days_ex21(*_probes[0])
        _err = ""
    except Exception as _e:
        _got = None
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _got is None:
        ex21_ok = False
        _msg = f"Wrong (Exercise 2.1): calling `simulate_days_ex21(4, 7, 8, 30)` raises an error (`{_err}`)."
    elif all(_v is None for _v in _got):
        ex21_ok = False
        _msg = "Not attempted (Exercise 2.1): the function still returns `None`. Use `return`, not `print`, then run the cell."
    else:
        _preview = f"\n\n**Your result:** `simulate_days_ex21(4, 7, 8, 30)` gives `{_got[0]}`"
        if not all(isinstance(_v, list) for _v in _got):
            ex21_ok = False
            _msg = "Wrong (Exercise 2.1): the function has to return a **list**, one number per day."
        elif [len(_v) for _v in _got] != [7, 3, 5]:
            ex21_ok = False
            _msg = f"Wrong (Exercise 2.1): `simulate_days_ex21(4, 7, 8, 30)` asks for 7 days, but your list has {len(_got[0])}. The length has to follow `days`."
        elif _again != _got[0]:
            ex21_ok = False
            _msg = "Wrong (Exercise 2.1): the same call gave two different lists. The investor cannot re-run this: the `seed` is not pinning the draws yet."
        elif len(set(str(_x) for _x in _got[0])) == 1:
            ex21_ok = False
            _msg = "Wrong (Exercise 2.1): every day comes out identical. Something resets the generator to the same starting point before every single draw."
        elif _got == [_expect(*_p) for _p in _probes]:
            ex21_ok = True
            _msg = "Correct (Exercise 2.1): seven days, three days, five days, each reproducible from its seed. That is a projection the investor can run herself and land on your numbers."
        elif _got == [_expect(*_p, top=False) for _p in _probes]:
            ex21_ok = False
            _msg = "Wrong (Exercise 2.1): `high` itself can never come up. With `low` 1 and `high` 6 a 6 has to be possible: both ends are included."
        else:
            ex21_ok = False
            _msg = "Wrong (Exercise 2.1): reproducible, but not the days this seed stands for. `simulate_days_ex21(4, 7, 8, 30)` is `[15, 17, 11, 20, 23, 12, 10]`: pin the seed once per call, then draw the days in order, each a whole number from `low` to `high` with both ends included."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core, fix the bug): the photocopy projection

    Tobi also projected seven days, with his own loop. It runs (no red error),
    but every single day comes out **identical**. That's not a projection,
    that's a photocopy, and the investor noticed immediately.

    Fix Tobi's cell **in place** so `fixed_ex22` holds seven days that actually
    vary. Keep his seed (9) and his demand range (8 to 30).
    """
    )
    return


@app.cell
def _(random):
    # YOUR CODE BELOW
    # TOBI'S CODE: seven days of demand, but every day comes out identical.
    fixed_ex22 = []
    for _day in range(7):
        random.seed(9)
        fixed_ex22.append(random.randint(8, 30))
    return (fixed_ex22,)


@app.cell(hide_code=True)
def _(fixed_ex22, mo, show_result):
    _expected = [22, 27, 19, 16, 12, 13, 29]
    if fixed_ex22 is None:
        ex22_ok = False
        _msg = "Not attempted (Exercise 2.2). Assign it to `fixed_ex22` (a `print` alone doesn't count) and run the cell."
        _preview = ""
    elif not isinstance(fixed_ex22, list):
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): `fixed_ex22` should be a **list** of seven numbers."
        _preview = show_result(fixed_ex22)
    elif len(fixed_ex22) != 7:
        ex22_ok = False
        _msg = f"Wrong (Exercise 2.2): seven days expected, but you have {len(fixed_ex22)}."
        _preview = show_result(fixed_ex22)
    elif len(set(str(_x) for _x in fixed_ex22)) == 1:
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): still a photocopy: all seven days are identical. Something resets the generator to the same starting point before every single draw."
        _preview = show_result(fixed_ex22)
    elif fixed_ex22 == _expected:
        ex22_ok = True
        _msg = "Correct (Exercise 2.2): seven *different* days, a real projection. A seed pins where the sequence *starts*. Set it once and the draws continue from there; set it before every draw and each one restarts at the same number."
        _preview = show_result(fixed_ex22)
    else:
        ex22_ok = False
        _msg = "Wrong (Exercise 2.2): the days vary now, but they are not the week that seed 9 stands for. Keep Tobi's seed and his range (8 to 30), and count how many times the seed is set."
        _preview = show_result(fixed_ex22)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core): the weekend shift

    Nobody wants the weekend shift, so it is decided at random, and the
    investor wants a draw she can re-run. The five riders are stored in a
    tuple, so nobody reorders them by accident:

    ```python
    riders = ("Ana", "Ben", "Cem", "Dana", "Eli")
    ```

    Write `weekend_order_ex23(seed)`. It returns **all five riders in a random
    order**, as a **list**, and the same `seed` must always give the same order.
    The first two names in the list work the weekend.
    """
    )
    return


@app.cell
def _():
    riders = ("Ana", "Ben", "Cem", "Dana", "Eli")
    return (riders,)


@app.cell
def _():
    def weekend_order_ex23(seed):
        # YOUR CODE BELOW: return all five riders in a random order, as a list,
        # the same order every time for the same `seed`
        return None

    return (weekend_order_ex23,)


@app.cell(hide_code=True)
def _(weekend_order_ex23, mo):
    # Reactive check.
    _roster = ["Ana", "Ben", "Cem", "Dana", "Eli"]
    try:
        _first = weekend_order_ex23(8)
        _again = weekend_order_ex23(8)
        _others = [weekend_order_ex23(_s) for _s in (1, 2, 3, 4)]
        _err = ""
    except Exception as _e:
        _first = _again = None
        _others = []
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _err:
        ex23_ok = False
        _msg = f"Wrong (Exercise 2.3): calling `weekend_order_ex23(8)` raises an error (`{_err}`). If it complains about a tuple, remember why the riders are stored in one."
    elif _first is None:
        ex23_ok = False
        _msg = "Not attempted (Exercise 2.3): the function returns `None`. Use `return`, then run the cell. If you *are* returning something and still see this: one of the `random` tools changes a list in place and hands back `None`, so returning its result returns nothing."
    else:
        _preview = f"\n\n**Your result:** `weekend_order_ex23(8)` gives `{_first}`"
        _all = [_first] + _others
        if not all(isinstance(_v, list) for _v in _all):
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): the result has to be a **list**."
        elif not all(sorted(str(_x) for _x in _v) == _roster for _v in _all):
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): the list has to hold every rider exactly once. Yours is missing someone or lists someone twice."
        elif _first != _again:
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): the same seed gave two different orders. The investor cannot re-run this draw: the `seed` is not pinning it yet."
        elif all(_v == _first for _v in _others):
            ex23_ok = False
            _msg = "Wrong (Exercise 2.3): seeds 1, 2, 3, 4 and 8 all give the same order. Either nothing is drawn at all, or the draw ignores the `seed` it was given."
        else:
            ex23_ok = True
            _msg = f"Correct (Exercise 2.3): with seed 8, **{_first[0]}** and **{_first[1]}** work the weekend, and anyone can re-run the draw to check. The tuple stayed untouched: you drew from a copy."
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.4 (core): one trip or two?

    The investor points at Tobi's *fixed* week from 2.2, `fixed_ex22`: "Suppose
    that's the week. How many crates do we order?" One order uses one bag, a crate holds
    **12** bags, and crates only come whole. The van fits **10** crates, so the
    number decides whether it's one trip or two.

    Store the number of crates for the week in `crates_ex24`. You already wrote
    the rule in 1.1: use your own function.

    *Finish 1.1 and 2.2 first.* Without them this cell has nothing to work
    with.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: whole crates for Tobi's fixed week (12 bags per crate),
    # computed with your function from Exercise 1.1
    crates_ex24 = None
    return (crates_ex24,)


@app.cell(hide_code=True)
def _(crates_ex24, mo, show_result):
    if crates_ex24 is None:
        ex24_ok = False
        _msg = "Not attempted (Exercise 2.4). Assign it to `crates_ex24` (a `print` alone doesn't count) and run the cell. If your function from 1.1 still returns `None`, finish that one first."
        _preview = ""
    elif isinstance(crates_ex24, bool) or not isinstance(crates_ex24, int):
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): this should be a whole **number** of crates, an `int`. Nobody sells half a crate."
        _preview = show_result(crates_ex24)
    elif crates_ex24 == 12:
        ex24_ok = True
        _msg = "Correct (Exercise 2.4): **12** crates for Tobi's week. The van fits 10, so the investor writes down: two trips, or a bigger van. And you did not write the rounding rule a second time."
        _preview = show_result(crates_ex24)
    elif crates_ex24 == 13:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): 13 crates is the count for Tobi's *photocopy* week, seven days of 22. Get Exercise 2.2 green first, then this number follows."
        _preview = show_result(crates_ex24)
    elif crates_ex24 == 11:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): 11 crates hold 132 bags, six short of the week's 138. Check what your function from 1.1 does with a week that doesn't divide evenly."
        _preview = show_result(crates_ex24)
    else:
        ex24_ok = False
        _msg = "Wrong (Exercise 2.4): not the crate count for Tobi's fixed week. The week's bags are all seven days of `fixed_ex22` together."
        _preview = show_result(crates_ex24)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex24_ok else "warn")
    return (ex24_ok,)


# ─────────────────────────────────────────────────────────────────────────
# PUTTING IT TOGETHER: the stress test
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Putting it together (core): the stress test

    The investor's last question decides the van: "One week proves nothing.
    Show me **200 weeks**."

    Her rule for a simulation she can audit: **week number `w` is simulated with
    seed `w`**, for the weeks 0 to 199. That way she can re-run any single week
    and get the same seven days. Each week has **7 days** of between **8 and
    30** orders, like Tobi's.

    Three steps, each in its own cell, each building on the one before:

    1. `week_totals_ex40`: a list with the **total orders of each of the 200
       weeks**, in week order.
    2. `two_trip_weeks_ex40`: **how many** of those weeks need more crates than
       the van's **10** (12 bags per crate, whole crates only).
    3. `typical_week_ex40`: the **typical** weekly total.

    You have already built most of what this needs in 1.1 and 2.1.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the 200 weekly totals, week w simulated with seed w (weeks 0 to 199)
    week_totals_ex40 = None
    return (week_totals_ex40,)


@app.cell
def _():
    # YOUR CODE BELOW: how many of the 200 weeks need more than 10 crates (an int)
    two_trip_weeks_ex40 = None
    return (two_trip_weeks_ex40,)


@app.cell
def _():
    # YOUR CODE BELOW: the typical weekly total
    typical_week_ex40 = None
    return (typical_week_ex40,)


@app.cell(hide_code=True)
def _(mo, random, two_trip_weeks_ex40, typical_week_ex40, week_totals_ex40):
    # Reactive check.
    def _week(seed):
        rng = random.Random(seed)
        return sum(rng.randint(8, 30) for _ in range(7))

    _totals = [_week(_w) for _w in range(200)]
    _crates = [(_t + 11) // 12 for _t in _totals]
    _two = sum(1 for _c in _crates if _c > 10)
    _mid = sorted(_totals)
    _typical = (_mid[99] + _mid[100]) / 2
    _preview = ""
    if week_totals_ex40 is None:
        ex40_ok = False
        _msg = "Not attempted (Putting it together). Start with step 1: assign the 200 weekly totals to `week_totals_ex40` and run the cell."
    elif not isinstance(week_totals_ex40, list):
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 1): `week_totals_ex40` has to be a **list**, one total per week."
    elif len(week_totals_ex40) != 200:
        ex40_ok = False
        _msg = f"Wrong (Putting it together, step 1): 200 weeks expected, but your list has {len(week_totals_ex40)} entries. One entry is one week's *total*, not one day."
    elif week_totals_ex40 != _totals:
        ex40_ok = False
        _preview = f"\n\n**Your first three weeks:** `{week_totals_ex40[:3]}`"
        if len(set(str(_x) for _x in week_totals_ex40)) == 1:
            _msg = "Wrong (Putting it together, step 1): all 200 weeks are identical. Every week is being simulated with the same seed."
        elif week_totals_ex40 == [_week(_w) for _w in range(1, 201)]:
            _msg = "Wrong (Putting it together, step 1): these are the weeks 1 to 200. Her weeks run from **0 to 199**."
        elif week_totals_ex40[0] == _totals[0]:
            _msg = "Wrong (Putting it together, step 1): week 0 is right, the later weeks are not. Her rule: every week gets its *own* seed, week `w` uses seed `w`."
        else:
            _msg = "Wrong (Putting it together, step 1): not the weeks her rule describes. Week 0 (seed 0) totals 133 orders, week 1 (seed 1) totals 120. Each week is 7 days of 8 to 30 orders."
    elif two_trip_weeks_ex40 is None:
        ex40_ok = False
        _msg = "Step 1 is right: 200 weeks, week 0 totals 133 orders. Now step 2: assign `two_trip_weeks_ex40`."
    elif isinstance(two_trip_weeks_ex40, bool) or not isinstance(two_trip_weeks_ex40, int):
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 2): `two_trip_weeks_ex40` is a count of weeks, so a whole number (an `int`)."
        _preview = f"\n\n**Your result:** `{two_trip_weeks_ex40}`"
    elif two_trip_weeks_ex40 != _two:
        ex40_ok = False
        _preview = f"\n\n**Your result:** `{two_trip_weeks_ex40}`"
        if two_trip_weeks_ex40 == 200 - _two:
            _msg = "Wrong (Putting it together, step 2): that's the number of weeks that *fit* in one trip. She asked for the weeks that need a second one."
        elif two_trip_weeks_ex40 == sum(1 for _c in _crates if _c >= 10):
            _msg = "Wrong (Putting it together, step 2): the van fits 10 crates, so a 10-crate week is still one trip. Count the weeks that need **more than** 10."
        elif two_trip_weeks_ex40 == sum(1 for _t in _totals if _t // 12 > 10):
            _msg = "Wrong (Putting it together, step 2): too few. A week of 121 orders already needs an 11th crate, because crates only come whole."
        else:
            _msg = "Wrong (Putting it together, step 2): not the number of two-trip weeks. For each weekly total: how many whole crates (12 bags each), and is that more than the van's 10?"
    elif typical_week_ex40 is None:
        ex40_ok = False
        _msg = f"Steps 1 and 2 are right: {_two} of 200 weeks need a second trip. Now step 3: assign `typical_week_ex40`."
    elif isinstance(typical_week_ex40, bool) or not isinstance(typical_week_ex40, (int, float)):
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 3): the typical weekly total has to be a single **number**."
        _preview = f"\n\n**Your result:** `{typical_week_ex40}`"
    elif round(typical_week_ex40, 2) == _typical:
        ex40_ok = True
        _msg = (
            f"Correct (Putting it together): **{_two}** of 200 weeks need a second trip, about "
            f"three weeks in four, and a typical week brings **{_typical}** orders, which is "
            "already 11 crates. The investor circles \"bigger van\" on her clipboard. "
            "That took all three modules from today and two of your own functions."
        )
        _preview = f"\n\n**Your result:** `{two_trip_weeks_ex40}` two-trip weeks, typical week `{typical_week_ex40}`"
    elif round(typical_week_ex40, 2) == round(sum(_totals) / 200, 2):
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 3): that's the *average* week. She asked for the typical one, the same idea as the typical delivery in 1.3."
        _preview = f"\n\n**Your result:** `{typical_week_ex40}`"
    else:
        ex40_ok = False
        _msg = "Wrong (Putting it together, step 3): not the typical weekly total. Half of the 200 weeks should be below it, half above."
        _preview = f"\n\n**Your result:** `{typical_week_ex40}`"
    mo.callout(mo.md(_msg + _preview), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


# ─────────────────────────────────────────────────────────────────────────
# TRACE + MCQ
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise (trace, predict first): which way does ceil go?

    This is a **trace** exercise: predict the answer first, *then* reveal it. It's
    ungraded. The point is the prediction. Tobi runs:

    ```python
    import math
    print(math.ceil(-2.5))
    ```

    What gets printed?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    trace_floor = mo.ui.radio(
        options=["-3", "-2", "an error"],
        label="Your prediction for `math.ceil(-2.5)`:",
    )
    trace_floor
    return (trace_floor,)


@app.cell(hide_code=True)
def _(mo, trace_floor):
    if trace_floor.value is None:
        _msg = "Pick a prediction above first. Commit before you peek!"
    elif trace_floor.value == "-2":
        _msg = (
            "Correct: **-2**. `ceil` goes UP, not away from zero. On the number "
            "line -2 sits above -2.5, so the ceiling lands on -2. (`math.floor(-2.5)`, "
            "the deck's question, goes the other way, down to -3.)"
        )
    else:
        _msg = (
            "Not quite: it's **-2**. `ceil` always rounds *up* (toward "
            "positive infinity), not away from zero. -2 is above -2.5, so that's where "
            "it lands. (Ungraded. The point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ): why seed at all?

    You seeded every simulation today. **Why** does seeding a simulation matter?
    Assign the letter (as text) to `answer_ex50`:

    - **a)** it makes the results reproducible: same seed, same sequence
    - **b)** it makes the random numbers generate faster
    - **c)** it makes the numbers more evenly spread out
    - **d)** the numpy library refuses to draw without a seed
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
    elif str(answer_ex50).strip().lower() == "a":
        ex50_ok = True
        _msg = (
            "Correct (Quiz): **a**. A seed pins the *starting point* of the sequence, so "
            "the same seed replays the same numbers. That's what let the investor "
            "re-run your projection and see exactly what you saw."
        )
    else:
        ex50_ok = False
        _msg = (
            "Wrong (Quiz): not quite. Seeding doesn't change speed or spread, and numpy "
            "draws happily without one. Think about what let your projection come "
            "out the same way twice in a row."
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
    ### Bonus: no repeats (not required)

    Three of the four districts get flyers this month, and no district twice.

    ```python
    flyer_zones = ["Nord", "Sued", "Hafen", "Altstadt"]
    ```

    Store **three different** zones, picked at random, in `flyer_picks_ex60`
    (a list). Make the pick reproducible: running the cell again must give the
    same three.
    """
    )
    return


@app.cell
def _():
    flyer_zones = ["Nord", "Sued", "Hafen", "Altstadt"]
    return (flyer_zones,)


@app.cell
def _():
    # YOUR CODE BELOW: three different zones from flyer_zones, picked at random, reproducible
    flyer_picks_ex60 = None
    return (flyer_picks_ex60,)


@app.cell(hide_code=True)
def _(flyer_picks_ex60, mo, show_result):
    _zones = {"Nord", "Sued", "Hafen", "Altstadt"}
    if flyer_picks_ex60 is None:
        _ok = False
        _msg = "Not attempted (Bonus). Assign it to `flyer_picks_ex60` (a `print` alone doesn't count) and run the cell."
        _preview = ""
    elif not isinstance(flyer_picks_ex60, list):
        _ok = False
        _msg = "Wrong (Bonus): `flyer_picks_ex60` should be a **list** of three zone names."
        _preview = show_result(flyer_picks_ex60)
    elif len(flyer_picks_ex60) != 3:
        _ok = False
        _msg = f"Wrong (Bonus): three picks expected, but you have {len(flyer_picks_ex60)}."
        _preview = show_result(flyer_picks_ex60)
    elif not all(isinstance(_z, str) and _z in _zones for _z in flyer_picks_ex60):
        _ok = False
        _msg = "Wrong (Bonus): every pick has to be one of the four zone names, spelled as in `flyer_zones`."
        _preview = show_result(flyer_picks_ex60)
    elif len(set(flyer_picks_ex60)) != 3:
        _ok = False
        _msg = "Wrong (Bonus): one district got flyers twice. The three picks have to be different."
        _preview = show_result(flyer_picks_ex60)
    else:
        _ok = True
        _msg = "Correct (Bonus): three different districts. Now run your cell twice more. If the same three come up every time, the investor can audit the draw. If they change, the seed is still missing."
        _preview = show_result(flyer_picks_ex60)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus: the scrambled special (not required)

    Tobi wants a guessing game on the menu board: today's special, with its
    letters scrambled. Write `scramble_ex61(word, seed)`. It returns a
    **string** with exactly the letters of `word`, in a random order, and the
    same word with the same seed must always give the same scramble.
    """
    )
    return


@app.cell
def _():
    def scramble_ex61(word, seed):
        # YOUR CODE BELOW: return the letters of `word` in a random order, as one string,
        # the same scramble every time for the same `seed`
        return None

    return (scramble_ex61,)


@app.cell(hide_code=True)
def _(mo, scramble_ex61):
    # Reactive check.
    try:
        _first = scramble_ex61("shakshuka", 1)
        _again = scramble_ex61("shakshuka", 1)
        _others = [scramble_ex61("shakshuka", _s) for _s in (2, 3, 4, 5)]
        _short = scramble_ex61("ramen", 7)
        _err = ""
    except Exception as _e:
        _first = _again = _short = None
        _others = []
        _err = f"{type(_e).__name__}: {_e}"
    _preview = ""
    if _err:
        _ok = False
        _msg = f"Wrong (Bonus): calling `scramble_ex61(\"shakshuka\", 1)` raises an error (`{_err}`)."
    elif _first is None:
        _ok = False
        _msg = "Not attempted (Bonus): the function returns `None`. If you *are* returning something and still see this: one of the `random` tools changes a list in place and hands back `None`."
    else:
        _preview = f"\n\n**Your result:** `scramble_ex61(\"shakshuka\", 1)` gives `{_first}`"
        _all = [_first] + _others
        if not all(isinstance(_v, str) for _v in _all + [_short]):
            _ok = False
            _msg = "Wrong (Bonus): the scramble has to come back as one **string**, not a list of letters."
        elif not all(sorted(_v) == sorted("shakshuka") for _v in _all) or sorted(_short) != sorted("ramen"):
            _ok = False
            _msg = "Wrong (Bonus): a scramble uses exactly the letters of the word, each as often as the word has it. Yours loses or adds letters."
        elif _first != _again:
            _ok = False
            _msg = "Wrong (Bonus): the same word with the same seed gave two different scrambles."
        elif all(_v == _first for _v in _others):
            _ok = False
            _msg = "Wrong (Bonus): seeds 1 to 5 all give the same result. Either nothing is scrambled, or the scramble ignores the `seed`."
        else:
            _ok = True
            _msg = "Correct (Bonus): same letters, new order, and reproducible. Tobi writes it on the board and immediately forgets which dish it was."
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Bonus: explore the toolbox (not required)

    The investor asks which star rating customers give **most often**. The
    lecture never showed a tool for that, but the `statistics` toolbox has one.
    `dir(stats)` lists every tool in it, and `help(...)` explains any of them.

    ```python
    stars = [5, 4, 5, 3, 5, 4, 2, 5, 4, 4, 5, 3, 4, 5, 4, 5, 1, 4, 5, 5]
    ```

    Store the most common star rating in `common_stars_ex62`, found with a tool
    from the toolbox, not counted by hand.
    """
    )
    return


@app.cell
def _():
    stars = [5, 4, 5, 3, 5, 4, 2, 5, 4, 4, 5, 3, 4, 5, 4, 5, 1, 4, 5, 5]
    return (stars,)


@app.cell
def _():
    # YOUR CODE BELOW: the star rating that appears most often in `stars`
    common_stars_ex62 = None
    return (common_stars_ex62,)


@app.cell(hide_code=True)
def _(common_stars_ex62, mo, show_result):
    if common_stars_ex62 is None:
        _ok = False
        _msg = "Not attempted (Bonus). Assign it to `common_stars_ex62` (a `print` alone doesn't count) and run the cell."
        _preview = ""
    elif isinstance(common_stars_ex62, bool) or not isinstance(common_stars_ex62, (int, float)):
        _ok = False
        _msg = "Wrong (Bonus): the answer is one star rating, a single **number**."
        _preview = show_result(common_stars_ex62)
    elif common_stars_ex62 == 5:
        _ok = True
        _msg = "Correct (Bonus): **5** stars, nine times out of twenty. If you found it with `stats.mode`, you just used a tool nobody taught you. That is what `dir()` and `help()` are for."
        _preview = show_result(common_stars_ex62)
    elif common_stars_ex62 == 4:
        _ok = False
        _msg = "Wrong (Bonus): 4 is the *middle* rating. She asked for the one that appears most often."
        _preview = show_result(common_stars_ex62)
    else:
        _ok = False
        _msg = "Wrong (Bonus): not the most common rating. Keep reading the list from `dir(stats)`: one name in it stands for exactly this."
        _preview = show_result(common_stars_ex62)
    mo.callout(mo.md(_msg + _preview), kind="success" if _ok else "warn")
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
    _checks = [
        ex11_ok, ex12_ok, ex13_ok,
        ex21_ok, ex22_ok, ex23_ok, ex24_ok, ex40_ok, ex50_ok,
    ]
    _done = sum(_checks)
    _total = len(_checks)
    _investor = (
        "The investor closes her clipboard, satisfied."
        if _done == _total
        else "The investor is still tapping her pen, waiting for the numbers."
    )
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} correct**. {_investor}"),
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
    2. **Download your work**: **Cmd/Ctrl+S**, then menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. **Next session we install Zed in class**, the editor you will write
       code in from then on. Bring a laptop you are allowed to install software
       on, and its charger.
    4. Next episode: the investor liked the numbers. Now she wants a **deck**.
       You'll turn a week of orders into the metrics that go on a slide: totals,
       per-zone breakdowns, the best day, which zone is strongest. **Episode 7:
       the numbers deck.**
    """
    )
    return


if __name__ == "__main__":
    app.run()
```
