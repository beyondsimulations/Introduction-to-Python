# notebooks/nb_06_lab_diligence.py
# Episode 6 — Due Diligence Week. Session VI lab notebook.
# Built from notebooks/nb_04_lab_menu.py (spec §4 rules apply):
# one global name per cell; += counts as a definition; every exercise
# pre-defines its answer (None); suffix exercise names (_exNM); underscore-
# prefixed names are cell-private; never a possible infinite loop. Data ships
# inline (public/ files don't load simply in WASM — see docs/authoring-conventions.md).
# First Part-II lab: AI tools are now allowed, but the checks still only pass on
# working code.
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook 6.1 — Due Diligence Week
    **Estimated time: 45–60 min · Core exercises: 7 + 1 quiz (+ 1 trace)**

    The investor is **here**. Not on a call, not "circling back next quarter" —
    standing in the shop with a clipboard and a very calm smile, asking to see the
    numbers before Friday. Real numbers: how many crates to order, what the
    ratings actually average to, what next week's demand might look like.

    Tobi's proposal is to "go on vibes". The investor's expression does not
    change. So this week you stop hand-rolling arithmetic and reach for Python's
    **standard library**: code that already ships with Python, written and tested
    by people who are not Tobi. You'll `import math` and `statistics` for
    professional-grade numbers, then use `random` to *rehearse* next week's
    demand, and learn why a good simulation is one you can run twice and trust.

    > **New this week: AI is allowed.** From this session on you may use an AI
    > assistant; see the course's [AI tools
    > guide](https://beyondsimulations.github.io/Introduction-to-Python/general/ai-tools.html).
    > One thing does not change: the ✅ checks below only go green on code that
    > actually runs. AI can draft a line for you; you still have to make it work,
    > and understand it well enough to fix it when it doesn't.
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
# SECTION 1 — Don't build it, import it
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — Don't build it, import it

    A **module** is a bundle of ready-made code that ships with Python. You don't
    rewrite it. You `import` it and use it. Three ways to bring one in:

    ```python
    import math                      # then call math.ceil(...), math.floor(...)
    import statistics                # then statistics.mean(...), statistics.median(...)
    import statistics as stats       # same module, shorter name: stats.mean(...)
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
    # Worked example (read + run this) — it also imports `math` for the exercises below
    import math
    print("ceil(10 / 3):", math.ceil(10 / 3))    # 4  — always rounds UP
    print("floor(10 / 3):", math.floor(10 / 3))  # 3  — always rounds DOWN
    return (math,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — how many crates?

    The investor wants to know the reorder. There are **75 delivery bags** to
    stock, and a crate holds **12**. You can only buy *whole* crates, so 6 crates
    (72 bags) wouldn't be enough. You need to round **up**. Use `math.ceil` to
    store the number of crates in `crates_ex11`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — whole crates needed for 75 bags, 12 per crate (round UP)
    crates_ex11 = None
    return (crates_ex11,)


@app.cell(hide_code=True)
def _(crates_ex11, mo, show_result):
    if crates_ex11 is None:
        ex11_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
        _preview = ""
    elif not isinstance(crates_ex11, int):
        ex11_ok = False
        _msg = "❌ Exercise 1.1: this should be a whole **number** of crates. `math.ceil(...)` returns an `int` — did you divide 75 by 12 inside it?"
        _preview = show_result(crates_ex11)
    elif crates_ex11 == 7:
        ex11_ok = True
        _msg = "✅ Exercise 1.1: **7** crates. Six would leave you three bags short — `math.ceil` rounds up so you never under-order."
        _preview = show_result(crates_ex11)
    elif crates_ex11 == 6:
        ex11_ok = False
        _msg = "❌ Exercise 1.1: 6 crates is 72 bags — three short. `math.ceil` rounds *up* to the next whole crate, unlike plain integer division."
        _preview = show_result(crates_ex11)
    else:
        ex11_ok = False
        _msg = "❌ Exercise 1.1: not quite. Feed `75 / 12` into `math.ceil(...)` and store the result."
        _preview = show_result(crates_ex11)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex11_ok else "warn")
    return (ex11_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`math` is already imported from the worked example. `math.ceil(...)` takes one number and rounds it up. The number you want to round is the bags divided by the crate size.",
            "💡 Hint 2 (the structure)": "crates_ex11 = math.ceil(___ / ___)   — put the number of bags and the crate size in the blanks.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.2 (core) — the honest average

    The investor read the reviews and wants the ratings summarized properly.
    Here are the six ratings:

    ```python
    ratings = [4.7, 3.6, 4.9, 4.2, 4.4, 3.8]
    ```

    Report two numbers using the `statistics` module:

    - `median_ex12` — the **middle** rating (`statistics.median`), and
    - `mean_ex12` — the **average** rating (`statistics.mean`).

    One thing to notice: this list has an **even** number of ratings, so there's
    no single middle value: the median is the **mean of the two middle** values
    once they're sorted. `statistics.median` handles that for you.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — it also imports `statistics` for the exercises below
    import statistics
    print("median of [2, 4, 6, 8]:", statistics.median([2, 4, 6, 8]))  # 5.0 (mean of 4 and 6)
    print("mean of [2, 4, 6, 8]:", statistics.mean([2, 4, 6, 8]))      # 5.0
    return (statistics,)


@app.cell
def _():
    ratings = [4.7, 3.6, 4.9, 4.2, 4.4, 3.8]
    return (ratings,)


@app.cell
def _():
    # YOUR CODE BELOW — the MIDDLE rating (statistics.median of `ratings`)
    median_ex12 = None
    return (median_ex12,)


@app.cell
def _():
    # YOUR CODE BELOW — the AVERAGE rating (statistics.mean of `ratings`)
    mean_ex12 = None
    return (mean_ex12,)


@app.cell(hide_code=True)
def _(mean_ex12, median_ex12, mo, show_result):
    if median_ex12 is None and mean_ex12 is None:
        ex12_ok = False
        _msg = "🔲 Exercise 1.2: not attempted yet."
        _preview = ""
    elif median_ex12 is None or mean_ex12 is None:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: both numbers are needed — fill in `median_ex12` *and* `mean_ex12`."
        _preview = show_result(median_ex12) + show_result(mean_ex12)
    elif not isinstance(median_ex12, (int, float)) or not isinstance(mean_ex12, (int, float)):
        ex12_ok = False
        _msg = "❌ Exercise 1.2: both should be **numbers**. Pass the whole `ratings` list into `statistics.median(...)` and `statistics.mean(...)`."
        _preview = show_result(median_ex12) + show_result(mean_ex12)
    elif round(median_ex12, 2) == 4.3 and round(mean_ex12, 2) == 4.27:
        ex12_ok = True
        _msg = "✅ Exercise 1.2: median **4.3**, mean **4.27**. With six ratings the median is the average of the two middle ones — `statistics.median` sorted and split them for you."
        _preview = show_result(median_ex12) + show_result(mean_ex12)
    elif round(median_ex12, 2) == 4.27 and round(mean_ex12, 2) == 4.3:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: looks like these two are the wrong way round — which one is the middle value, which one the average?"
        _preview = show_result(median_ex12) + show_result(mean_ex12)
    elif round(median_ex12, 2) != 4.3:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: the median isn't right yet. It's `statistics.median(ratings)` — the middle of the *sorted* ratings (here, the mean of the two middle values)."
        _preview = show_result(median_ex12) + show_result(mean_ex12)
    else:
        ex12_ok = False
        _msg = "❌ Exercise 1.2: the mean isn't right yet. It's `statistics.mean(ratings)` — the sum of all six ratings divided by six."
        _preview = show_result(median_ex12) + show_result(mean_ex12)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex12_ok else "warn")
    return (ex12_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "`statistics` is imported from the worked example. Both functions take the list itself: `statistics.median(the_list)` and `statistics.mean(the_list)`. You don't need to sort anything by hand.",
            "💡 Hint 2 (the structure)": "median_ex12 = statistics.median(___)\nmean_ex12 = statistics.mean(___)   — put the ratings list in each blank.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.3 (core) — a shorter name

    Typing `statistics` over and over gets old, so people **alias** it on import:
    `import statistics as stats` gives the same module a shorter name. The daily
    order counts for the week were:

    ```python
    daily_orders = [12, 19, 15, 22]
    ```

    Using the alias `stats`, store the **average** number of daily orders in
    `avg_ex13`.
    """
    )
    return


@app.cell
def _():
    # Worked example (read + run this) — the SAME statistics module, aliased to `stats`
    import statistics as stats
    print("stats.mean([10, 20, 30]):", stats.mean([10, 20, 30]))  # 20
    return (stats,)


@app.cell
def _():
    daily_orders = [12, 19, 15, 22]
    return (daily_orders,)


@app.cell
def _():
    # YOUR CODE BELOW — the average of `daily_orders`, using the alias `stats`
    avg_ex13 = None
    return (avg_ex13,)


@app.cell(hide_code=True)
def _(avg_ex13, mo, show_result):
    if avg_ex13 is None:
        ex13_ok = False
        _msg = "🔲 Exercise 1.3: not attempted yet."
        _preview = ""
    elif not isinstance(avg_ex13, (int, float)):
        ex13_ok = False
        _msg = "❌ Exercise 1.3: the average should be a **number**. Pass `daily_orders` into `stats.mean(...)`."
        _preview = show_result(avg_ex13)
    elif round(avg_ex13, 2) == 17:
        ex13_ok = True
        _msg = "✅ Exercise 1.3: **17** orders a day on average. `import statistics as stats` and `import statistics` reach the exact same code — the alias is just a nickname."
        _preview = show_result(avg_ex13)
    else:
        ex13_ok = False
        _msg = "❌ Exercise 1.3: not the average of the four counts. It's `stats.mean(daily_orders)` — add the four up, divide by four."
        _preview = show_result(avg_ex13)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex13_ok else "warn")
    return (ex13_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "The alias `stats` behaves exactly like `statistics`. Call `.mean(...)` on it and hand it the list of daily orders.",
            "💡 Hint 2 (the structure)": "avg_ex13 = stats.mean(___)   — put the daily_orders list in the blank.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# SECTION 2 — Rehearsing luck: the random module
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 2 — Rehearsing luck: the `random` module

    The investor wants a **projection** of next week's demand. You can't know the
    future, but you can *rehearse* it: the `random` module invents plausible
    numbers so you can see how a busy week might play out.

    ```python
    import random
    random.seed(0)                 # pin the dice: same seed → same "random" run
    random.randint(1, 6)           # a whole number from 1 to 6 (both ends included)
    random.choice(["a", "b", "c"]) # one item picked at random from a list
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
    # Worked example (read + run this) — it also imports `random` for the exercises below
    import random
    random.seed(0)
    print("three seeded dice rolls:", [random.randint(1, 6) for _ in range(3)])
    # Run this cell again — same three numbers, because the seed was pinned first.
    return (random,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.1 (core) — simulate the week

    Project **7 days** of demand. First `random.seed(4)` **once**, then draw seven
    values with `random.randint(8, 30)` (each a whole number from 8 to 30) and
    collect them, in order, into the list `demand_ex21`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — seed with 4, then 7 × random.randint(8, 30) into a list
    demand_ex21 = None
    return (demand_ex21,)


@app.cell(hide_code=True)
def _(demand_ex21, mo, show_result):
    _expected = [15, 17, 11, 20, 23, 12, 10]
    if demand_ex21 is None:
        ex21_ok = False
        _msg = "🔲 Exercise 2.1: not attempted yet."
        _preview = ""
    elif not isinstance(demand_ex21, list):
        ex21_ok = False
        _msg = "❌ Exercise 2.1: `demand_ex21` should be a **list** of seven numbers. Collect the draws with a loop or a list comprehension."
        _preview = show_result(demand_ex21)
    elif len(demand_ex21) != 7:
        ex21_ok = False
        _msg = f"❌ Exercise 2.1: seven days expected, but you have {len(demand_ex21)}. Draw `random.randint(8, 30)` exactly seven times."
        _preview = show_result(demand_ex21)
    elif demand_ex21 == _expected:
        ex21_ok = True
        _msg = "✅ Exercise 2.1: seven days projected — and because you seeded with 4 first, anyone who runs it gets this exact week. That's a projection you can defend."
        _preview = show_result(demand_ex21)
    else:
        ex21_ok = False
        _msg = "❌ Exercise 2.1: right length, but the numbers don't match what's expected — so the seed isn't set as expected. Call `random.seed(4)` **once**, *before* the seven draws, then use `random.randint(8, 30)`."
        _preview = show_result(demand_ex21)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex21_ok else "warn")
    return (ex21_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Two steps: pin the generator with `random.seed(4)` first, then build a list of seven `random.randint(8, 30)` draws — a list comprehension over `range(7)` is the tidy way.",
            "💡 Hint 2 (the structure)": "random.seed(4)\ndemand_ex21 = [random.randint(___, ___) for _ in range(___)]   — fill the low bound, high bound, and how many days.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.2 (core, fix the bug) — the photocopy projection

    Tobi also tried to project seven days. His code runs (no red error), but
    every single day comes out **identical**. That's not a projection, that's a
    photocopy, and the investor noticed immediately.

    Here's exactly what Tobi wrote:

    ```python
    tobi_demand = []
    for day in range(7):
        random.seed(9)
        tobi_demand.append(random.randint(8, 30))
    # tobi_demand → [22, 22, 22, 22, 22, 22, 22]
    ```

    Write a corrected version into `fixed_ex22`: a list of seven demand values
    (still `random.seed(9)`, still `random.randint(8, 30)`) that **actually
    vary** from day to day.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — Tobi's seven-day projection, fixed so the days actually vary
    fixed_ex22 = None
    return (fixed_ex22,)


@app.cell(hide_code=True)
def _(fixed_ex22, mo, show_result):
    _expected = [22, 27, 19, 16, 12, 13, 29]
    if fixed_ex22 is None:
        ex22_ok = False
        _msg = "🔲 Exercise 2.2: not attempted yet."
        _preview = ""
    elif not isinstance(fixed_ex22, list):
        ex22_ok = False
        _msg = "❌ Exercise 2.2: `fixed_ex22` should be a **list** of seven numbers."
        _preview = show_result(fixed_ex22)
    elif len(fixed_ex22) != 7:
        ex22_ok = False
        _msg = f"❌ Exercise 2.2: seven days expected, but you have {len(fixed_ex22)}."
        _preview = show_result(fixed_ex22)
    elif len(set(fixed_ex22)) == 1:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: still a photocopy — all seven days are identical. Something is resetting the generator to the same starting point before every single draw. Where does that reset belong so it happens only once?"
        _preview = show_result(fixed_ex22)
    elif fixed_ex22 == _expected:
        ex22_ok = True
        _msg = "✅ Exercise 2.2: seven *different* days — a real projection. Seeding pins where the sequence *starts*; do it once and the numbers flow, do it every step and they freeze."
        _preview = show_result(fixed_ex22)
    else:
        ex22_ok = False
        _msg = "❌ Exercise 2.2: the days vary now, but they're not the expected sequence. Keep `random.seed(9)` and `random.randint(8, 30)` — check *how many times* the seed is set."
        _preview = show_result(fixed_ex22)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex22_ok else "warn")
    return (ex22_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Seeding resets the generator to a fixed starting point. Tobi resets it on every pass of the loop, so every draw starts from the same place and gives the same number. You want the sequence to *keep going*, not restart.",
            "💡 Hint 2 (the structure)": "random.seed(9)\nfixed_ex22 = [random.randint(8, 30) for _ in range(___)]   — fill how many days, and note where `seed` sits: once, above the draws, not inside them.",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 2.3 (core) — the flyer raffle

    To pick which neighborhoods get flyers, you draw zones at random, **with
    repetition**, because a popular zone can be picked more than once. The zones:

    ```python
    flyer_zones = ["Nord", "Sued", "Hafen", "Altstadt"]
    ```

    `random.seed(12)` **once**, then make **4** picks with `random.choice(...)`
    (one call per pick) and collect them, in order, into `raffle_ex23`.
    """
    )
    return


@app.cell
def _():
    flyer_zones = ["Nord", "Sued", "Hafen", "Altstadt"]
    return (flyer_zones,)


@app.cell
def _():
    # YOUR CODE BELOW — seed with 12, then 4 × random.choice(flyer_zones) into a list
    raffle_ex23 = None
    return (raffle_ex23,)


@app.cell(hide_code=True)
def _(mo, raffle_ex23, show_result):
    _expected = ["Altstadt", "Hafen", "Hafen", "Sued"]
    if raffle_ex23 is None:
        ex23_ok = False
        _msg = "🔲 Exercise 2.3: not attempted yet."
        _preview = ""
    elif not isinstance(raffle_ex23, list):
        ex23_ok = False
        _msg = "❌ Exercise 2.3: `raffle_ex23` should be a **list** of four zone names."
        _preview = show_result(raffle_ex23)
    elif len(raffle_ex23) != 4:
        ex23_ok = False
        _msg = f"❌ Exercise 2.3: four picks expected, but you have {len(raffle_ex23)}. Call `random.choice(...)` four times."
        _preview = show_result(raffle_ex23)
    elif raffle_ex23 == _expected:
        ex23_ok = True
        _msg = "✅ Exercise 2.3: four zones drawn — and Hafen came up twice, which is fine: `random.choice` can pick the same item again. Seeded with 12, so it's reproducible."
        _preview = show_result(raffle_ex23)
    elif len(set(raffle_ex23)) == 4 and set(raffle_ex23) == {"Nord", "Sued", "Hafen", "Altstadt"}:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: that draws without repetition (sample/shuffle) — the raffle can pick the same zone twice; call `random.choice` once per pick."
        _preview = show_result(raffle_ex23)
    else:
        ex23_ok = False
        _msg = "❌ Exercise 2.3: right length, different draws — so the seed isn't set as expected. `random.seed(12)` **once** before the four `random.choice(flyer_zones)` picks."
        _preview = show_result(raffle_ex23)
    mo.callout(mo.md(_msg + _preview), kind="success" if ex23_ok else "warn")
    return (ex23_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Seed once with 12, then build a list of four `random.choice(flyer_zones)` calls — each call returns one zone, and repeats are allowed.",
            "💡 Hint 2 (the structure)": "random.seed(12)\nraffle_ex23 = [random.choice(___) for _ in range(___)]   — fill the list to draw from and the number of picks.",
        }
    )
    return


# ─────────────────────────────────────────────────────────────────────────
# BOSS EXERCISE — the projection memo
# ─────────────────────────────────────────────────────────────────────────
@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 📈 Boss exercise (core) — the projection memo

    Time to write the line the investor actually asked for: *"On an average day
    next week, how many orders should we expect?"* You'll answer it by combining
    both modules from today: simulate the week with `random`, then summarize it
    with `statistics`.

    Do all of this:

    1. `random.seed(2)` **once**.
    2. Simulate **5 days** with `random.randint(10, 26)`.
    3. Store the **average** of those five days (via `statistics.mean`) in
       `boss_ex40`.

    That single number is your projection memo.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — seed 2, simulate 5 × random.randint(10, 26),
    # then store their statistics.mean in boss_ex40
    boss_ex40 = None
    return (boss_ex40,)


@app.cell(hide_code=True)
def _(boss_ex40, mo, show_result):
    if boss_ex40 is None:
        ex40_ok = False
        _msg = "🔲 Boss exercise: not attempted yet."
    elif not isinstance(boss_ex40, (int, float)):
        ex40_ok = False
        _msg = "❌ Boss exercise: the projection should be a single **number** — the average of the five simulated days."
    elif round(boss_ex40, 2) == 14.2:
        ex40_ok = True
        _msg = (
            "✅ Boss exercise: **14.2** orders a day on average. Seeded so it's "
            "reproducible, averaged so it's honest — a memo the investor can trust. 📈"
        )
    else:
        ex40_ok = False
        _msg = (
            "❌ Boss exercise: not the expected projection. Seed with 2 **once**, "
            "draw five `random.randint(10, 26)` values, then take `statistics.mean` "
            "of that list."
        )
    mo.callout(mo.md(_msg + show_result(boss_ex40)), kind="success" if ex40_ok else "warn")
    return (ex40_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "Three moves: seed, simulate, summarize. Build a list of five `random.randint(10, 26)` draws (after seeding once), then feed that whole list to `statistics.mean(...)`.",
            "💡 Hint 2 (the structure)": "random.seed(2)\n_days = [random.randint(10, 26) for _ in range(5)]\nboss_ex40 = statistics.mean(___)   — put the list of days in the blank.",
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
    ### Exercise (trace — predict first) — which way does ceil go?

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
        _msg = "🔲 Pick a prediction above first — commit before you peek!"
    elif trace_floor.value == "-2":
        _msg = (
            "✅ Correct: **-2**. `ceil` goes UP, not away from zero. On the number "
            "line -2 sits above -2.5, so the ceiling lands on -2. (`math.floor(-2.5)`, "
            "the deck's question, goes the other way, down to -3.)"
        )
    else:
        _msg = (
            "❌ Not quite — it's **-2**. `ceil` always rounds *up* (toward "
            "positive infinity), not away from zero. -2 is above -2.5, so that's where "
            "it lands. (Ungraded — the point is the prediction.)"
        )
    mo.callout(mo.md(_msg), kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Quiz (core, MCQ) — why seed at all?

    You seeded every simulation today. **Why** does seeding a simulation matter?
    Assign the letter (as text) to `answer_ex50`:

    - **a)** it makes the results reproducible — same seed, same sequence
    - **b)** it makes the random numbers generate faster
    - **c)** it makes the numbers more evenly spread out
    - **d)** the numpy library refuses to draw without a seed
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
    elif str(answer_ex50).strip().lower() == "a":
        ex50_ok = True
        _msg = (
            "✅ Quiz: **a**. A seed pins the *starting point* of the sequence, so "
            "the same seed replays the same numbers. That's what let the investor "
            "re-run your projection and see exactly what you saw."
        )
    else:
        ex50_ok = False
        _msg = (
            "❌ Quiz: not quite. Seeding doesn't change speed or spread, and numpy "
            "draws happily without one — think about what let your projection come "
            "out the same way twice in a row."
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
    ex40_ok,
    ex50_ok,
    mo,
):
    # Progress cell — the 7 core exercises plus the quiz (the trace doesn't count).
    _checks = [ex11_ok, ex12_ok, ex13_ok, ex21_ok, ex22_ok, ex23_ok, ex40_ok, ex50_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _investor = (
        "The investor closes her clipboard, satisfied."
        if _done == _total
        else "The investor is still tapping her pen, waiting for the numbers."
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
    ## Before you leave 📦

    1. Check the progress box above — all **eight** green? If not, reopen the
       hints, reread the worked examples, and try again. `math`, `statistics` and
       `random` are tools you'll reach for constantly, and seeding is the habit
       that turns "some random numbers" into "a result someone can verify".
    2. **Download your work**: menu → Download → *Download Python code*.
       Reloading this exact tab (Cmd/Ctrl+R) keeps your work, but closing the tab
       and reopening the link starts you fresh. The download is the only
       guaranteed copy.
    3. Next episode: the investor liked the numbers. Now she wants a **deck**.
       You'll turn a week of orders into the metrics that go on a slide: totals,
       per-zone breakdowns, the best day, which zone is strongest. **Episode 7:
       the numbers deck.**
    """
    )
    return


if __name__ == "__main__":
    app.run()
