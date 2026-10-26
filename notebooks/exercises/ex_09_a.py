# notebooks/exercises/ex_09_a.py
import marimo

app = marimo.App(width="medium", app_title="ex_09_a")


@app.cell(hide_code=True)
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
    mo.md(
        r"""
    # Quick exercise: the title is a claim (5-10 min)
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
    mo.md(
        r"""
    Episode 9: Tobi's first slide is a bar chart titled *Orders per
    day*. The investor looks at it for two seconds: "So? What should I
    see?" A title that **describes** the chart leaves the work to her.
    A title that **states the point** does it for her, and a number in
    it is the proof.

    Chart cells open with `plt.figure()` and end with `plt.gca()`, never
    `plt.show()`.

    **Predict** first: in the demo title below, which part is the claim
    and which part is the proof?
    """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def _(plt):
    # Worked example (read + run this)
    _demo_weeks = ["Week 1", "Week 2", "Week 3"]
    _demo_signups = [20, 35, 60]
    plt.figure()  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.bar(_demo_weeks, _demo_signups)
    plt.ylabel("Signups")  # what the axis measures
    plt.title("Demo: signups tripled in three weeks (20 to 60)")  # the claim, then the proof
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    `days_exa` and `orders_exa` below are this week's orders, Monday to
    Sunday. Write the title the investor needs: it names the **busiest
    day** and **how many orders** it had. Then draw the bar chart with
    your title on top.

    The chart itself isn't graded. The check below reads `title_exa`,
    the text on top of your chart.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    days_exa = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return (days_exa,)


@app.cell
def _():
    # Given: do not change this
    orders_exa = [31, 28, 35, 40, 38, 52, 47]
    return (orders_exa,)


@app.cell
def _(days_exa, orders_exa):
    # YOUR CODE BELOW: the title as a string: the busiest day and its number of orders
    title_exa = None
    return (title_exa,)


@app.cell
def _(days_exa, orders_exa, plt, title_exa):
    plt.figure()
    # YOUR CODE BELOW: bars of orders_exa per day, title_exa on top (ungraded)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo, show_result, title_exa):
    # Reactive check. Re-runs when you run the cell above.
    _result = None
    if title_exa is None:
        _ok = False
        _msg = "Not attempted: Assign it to `title_exa` (a `print` alone doesn't count) and run the cell."
    elif not isinstance(title_exa, str):
        _ok = False
        _result = f"title_exa={title_exa!r}"
        _msg = "Wrong: A title is text. Put it in quotes, or build it with an f-string."
    else:
        _v = title_exa.lower()
        _result = title_exa
        _day = "sat" in _v
        _count = "52" in _v
        if _day and _count:
            _ok = True
            _msg = "Correct: Exercise 9.a: claim and proof in one line. The investor knows what to look for before she looks."
        elif ("sun" in _v or "47" in _v) and not _day:
            _ok = False
            _msg = "Wrong: Sunday, with 47 orders, comes second. Look for the tallest bar."
        elif _day:
            _ok = False
            _msg = "Wrong: The day is right. Now the proof: how many orders? A number turns 'busy' into a claim she can check."
        elif _count:
            _ok = False
            _msg = "Wrong: 52 is the right number. Say which DAY it belongs to."
        else:
            _ok = False
            _msg = "Wrong: That describes the chart. The title needs two things: the busiest day and its number of orders."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "The busiest day is the tallest bar. `max(orders_exa)` gives its number of orders, and the position of that number in `orders_exa` gives its day in `days_exa`. An f-string can carry both into one title.",
            "Hint 2 (the structure)": "```python\n_most = max(___)\n_day = days_exa[orders_exa.index(___)]\ntitle_exa = f\"{___} is our busiest day: {___} orders\"\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** Tobi's agent made three more drafts of the same
    week. One is **ugly**, one is **bad**, and one is **wrong**: some
    number in it is not in `orders_exa`. Which one is wrong? Put its
    letter in `wrong_exa`.
    """
    )
    return


@app.cell(hide_code=True)
def _(days_exa, orders_exa, plt):
    # Tobi's three drafts (given)
    plt.figure(figsize=(12, 3.2))
    plt.subplot(1, 3, 1)
    _alphabetical = sorted(zip(days_exa, orders_exa))
    plt.bar([_d for _d, _n in _alphabetical], [_n for _d, _n in _alphabetical])
    plt.title("A")
    plt.subplot(1, 3, 2)
    plt.bar(days_exa, [31, 28, 35, 40, 38, 25, 47])
    plt.title("B")
    plt.subplot(1, 3, 3)
    plt.bar(
        days_exa,
        orders_exa,
        color=["#ff00ff", "#00ff00", "#ffff00", "#00ffff", "#ff8800", "#0000ff", "#ff0000"],
        edgecolor="black",
        linewidth=3,
    )
    plt.grid(True, color="black", linewidth=1.5)
    plt.title("C")
    plt.tight_layout()
    plt.gca()
    return


@app.cell
def _():
    # YOUR CODE BELOW: the letter of the WRONG chart, as a string
    wrong_exa = None
    return (wrong_exa,)


@app.cell(hide_code=True)
def _(mo, show_result, wrong_exa):
    # Reactive check. Re-runs when you run the cell above.
    _result = None
    if wrong_exa is None:
        _ok = False
        _msg = "Not attempted: Assign it to `wrong_exa` (a `print` alone doesn't count) and run the cell."
    elif not isinstance(wrong_exa, str):
        _ok = False
        _result = f"wrong_exa={wrong_exa!r}"
        _msg = "Wrong: The answer is one letter in quotes, like `\"A\"`."
    else:
        _v = wrong_exa.strip().upper()
        _result = f"wrong_exa={wrong_exa!r}"
        if _v == "B":
            _ok = True
            _msg = "Correct: Exercise 9.a stretch: B shows Saturday at 25, but the data says 52. A is bad (days in A-to-Z order), C is ugly (loud), and both still show the right numbers."
        elif _v == "A":
            _ok = False
            _msg = "Wrong: A puts the days in alphabetical order. That's confusing, so A is bad, but every bar has the right height."
        elif _v == "C":
            _ok = False
            _msg = "Wrong: C is loud, so it's ugly, but every bar has the right height."
        else:
            _ok = False
            _msg = "Wrong: Pick one of the three letters A, B or C."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Ugly and bad charts still show the right numbers. Read each chart's bars and compare them with `orders_exa`, day by day.",
            "Hint 2 (the structure)": "```python\nwrong_exa = \"___\"\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to hand in. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
