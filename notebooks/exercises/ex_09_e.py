# notebooks/exercises/ex_09_e.py
import marimo

app = marimo.App(width="medium", app_title="ex_09_e")


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
    # Quick exercise: put the deck in order (5-10 min)
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
    Episode 9: Tobi has four slides for his rider ask, and he dropped
    them on the way in. A pitch tells its story in four steps:

    1. **Opening**: where we stand
    2. **Challenge**: the problem
    3. **Action**: what we did about it
    4. **Resolution**: the result, and what we ask for

    **Predict** first: read the four titles below. Which slide could
    only come first?
    """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell(hide_code=True)
def _(plt):
    # Tobi's four slides (given), in the order he picked them up
    _red, _grey = "darkred", "lightgrey"
    _zones = ["Nord", "Altstadt", "Hafen", "Sued"]
    _weeks = [1, 2, 3, 4, 5, 6]
    plt.figure(figsize=(12, 6))  # starts a fresh figure so this chart doesn't draw on top of the last one
    plt.subplot(2, 2, 1)
    plt.plot(_weeks, [48, 39, 34, 32, 31, 31], color=_red, linewidth=3)
    plt.ylim(0, 55)
    plt.ylabel("Minutes")
    plt.title("A  A second Hafen rider: 48 down to 31 minutes", loc="left")
    plt.subplot(2, 2, 2)
    plt.plot(_weeks, [30, 34, 39, 45, 50, 57], color=_red, linewidth=3)
    plt.ylim(0, 60)
    plt.ylabel("Orders")
    plt.title("B  Hafen orders: 30 to 57 a week", loc="left")
    plt.subplot(2, 2, 3)
    plt.bar(_zones, [40, 55, 30, 38], color=[_red, _grey, _grey, _grey])
    plt.ylabel("Orders")
    plt.title("C  Four zones, 163 orders a week", loc="left")
    plt.subplot(2, 2, 4)
    plt.bar(_zones, [32, 35, 48, 30], color=[_grey, _grey, _red, _grey])
    plt.ylabel("Minutes")
    plt.title("D  Hafen: 48 minutes, the slowest zone", loc="left")
    plt.tight_layout()
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Put the four letters in story order, opening first:
    `order_exe`, a list like `["A", "B", "C", "D"]`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the four slide letters in story order, as a list
    order_exe = None
    return (order_exe,)


@app.cell(hide_code=True)
def _(mo, order_exe, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _expected = ["C", "D", "A", "B"]
    _roles = {
        0: "The opening is where we stand: the slide that only describes the business as it is.",
        1: "Second comes the problem, the thing that is wrong before anyone acted.",
        2: "Third comes what was done about the problem.",
        3: "Last comes the result, the slide that the ask hangs on.",
    }
    _result = None
    if order_exe is None:
        _ok = False
        _msg = "Not attempted: Assign it to `order_exe` (a `print` alone doesn't count) and run the cell."
    elif isinstance(order_exe, str):
        _ok = False
        _result = f"order_exe={order_exe!r}"
        _msg = "Wrong: That's one string. Make it a list of four letters, like `[\"A\", \"B\", \"C\", \"D\"]`."
    elif not isinstance(order_exe, (list, tuple)) or len(order_exe) != 4:
        _ok = False
        _result = f"order_exe={order_exe!r}"
        _msg = "Wrong: `order_exe` should be a list of exactly four letters."
    else:
        _v = [str(_letter).strip().upper() for _letter in order_exe]
        _result = f"order_exe={order_exe!r}"
        if sorted(_v) != ["A", "B", "C", "D"]:
            _ok = False
            _msg = "Wrong: Use each of the letters A, B, C and D exactly once."
        elif _v == _expected:
            _ok = True
            _msg = "Correct: Exercise 9.e: where we stand (C), the problem (D), what we did (A), the result (B). Now the ask, one more rider, follows from the story."
        elif _v[0] == "B":
            _ok = False
            _msg = "Wrong: That opens with the result. In a pitch, the room needs the problem before the result means anything."
        else:
            _ok = False
            _first_off = next(_i for _i in range(4) if _v[_i] != _expected[_i])
            _msg = f"Wrong: Slide {_first_off + 1} of your order is off. " + _roles[_first_off]
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "Read only the titles. One describes the business without any problem in it. One names a problem. One says what was changed. One shows what the change brought.",
            "Hint 2 (the structure)": "```python\norder_exe = [\"___\", \"___\", \"___\", \"___\"]\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** keep colors fixed across a deck. Dark red means Hafen
    on three of Tobi's slides, but on one slide it marks a different
    zone, and the room will read that slide wrong. Which one? Put its
    letter in `odd_exe`.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: the letter of the slide where dark red does not mean Hafen, as a string
    odd_exe = None
    return (odd_exe,)


@app.cell(hide_code=True)
def _(mo, odd_exe, show_result):
    # Reactive check. Re-runs when you run the cell above.
    _result = None
    if odd_exe is None:
        _ok = False
        _msg = "Not attempted: Assign it to `odd_exe` (a `print` alone doesn't count) and run the cell."
    elif not isinstance(odd_exe, str):
        _ok = False
        _result = f"odd_exe={odd_exe!r}"
        _msg = "Wrong: The answer is one letter in quotes, like `\"A\"`."
    else:
        _v = odd_exe.strip().upper()
        _result = f"odd_exe={odd_exe!r}"
        if _v == "C":
            _ok = True
            _msg = "Correct: Exercise 9.e stretch: on C, dark red marks Nord. Right after it, D shows Hafen in dark red, and the room thinks Nord is the slow zone."
        elif _v in ("A", "B", "D"):
            _ok = False
            _msg = f"Wrong: On {_v}, dark red is Hafen, as on the other slides. Look for the slide where dark red sits on a different zone."
        else:
            _ok = False
            _msg = "Wrong: Pick one of the four letters A, B, C or D."
    mo.callout(mo.md(_msg + show_result(_result)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "On A and B, the dark red line is Hafen's (the titles say so). On the bar slides, read the label under the dark red bar.",
            "Hint 2 (the structure)": "```python\nodd_exe = \"___\"\n```",
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to hand in. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
