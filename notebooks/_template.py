# notebooks/_template.py
# TEMPLATE — copy to nb_XX_lab_<topic>.py and replace TODO-marked content.
# Rules (spec §4): one global name per cell; += counts as a definition;
# every exercise pre-defines its answer as None; suffix exercise names (_ex1);
# underscore-prefixed names are cell-private.
# - exercise letters in ex_XX_<letter>.py map 1:1 to lecture block order (a=block 1)
# - never a possible infinite loop (freezes the WASM tab); Tobi's bugs always terminate
# - check literals must survive round(x, 2) exactly; avoid .xx5 boundaries
import marimo

app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Notebook X.Y — TODO Title
    **Estimated time: TODO min · Core exercises: TODO**

    TODO: Story cold-open. 2–4 sentences, sitcom tone.
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


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _():
    # Helper — renders a student's current answer as a "Your result" preview so
    # they SEE their output (e.g. a receipt's alignment), not just /. Strings
    # render in a fenced block (multi-line formatting shows); everything else
    # inline. Append `show_result(answer)` to any check cell's message.
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
    startup_name_input
    return (startup_name_input,)


@app.cell(hide_code=True)
def _(mo, startup_name_input):
    startup_name = startup_name_input.value.strip() or "Nameless Bites GmbH"
    mo.md(f"Welcome back to **{startup_name}**! Tobi already forgot the name again.")
    return (startup_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Section 1 — TODO concept name

    TODO: teach the concept in 3–6 sentences, then show a worked example below.
    """
    )
    return


@app.cell
def _():
    # Worked example (students read + run this)
    example_price = 4.50
    example_total = example_price * 3
    print(f"Three portions cost {example_total:.2f} EUR")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise 1.1 (core) — TODO one-line task

    TODO: task description referencing the story.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW — replace None
    revenue_ex1 = None
    return (revenue_ex1,)


@app.cell(hide_code=True)
def _(mo, revenue_ex1, show_result):
    # Reactive check — Re-runs when you run the cell above.
    if revenue_ex1 is None:
        ex1_ok = False
        _msg = "Not attempted — Exercise 1.1. Assign it to `revenue_ex1` (a `print` alone doesn't count) and run the cell."
    elif revenue_ex1 == 13.50:  # TODO expected value
        ex1_ok = True
        _msg = "Correct — Exercise 1.1: correct! The investor nods approvingly."
    else:
        ex1_ok = False
        _msg = "Wrong — Exercise 1.1: not quite — check your multiplication."
    # show_result echoes the student's current answer below the /Wrong — message.
    mo.md(_msg + show_result(revenue_ex1))
    return (ex1_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Hint 1 (a nudge)": "TODO: conceptual nudge, no code.",
            "Hint 2 (the structure)": "TODO: code skeleton with blanks, e.g. `revenue_ex1 = round(___ * ___, 2)` — NEVER the full pasteable answer (that lives in the post-session solution notebook).",
        }
    )
    return


@app.cell(hide_code=True)
def _(ex1_ok, mo):
    # Progress cell — extend the list as exercises are added.
    _checks = [ex1_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _tobi = "Tobi is impressed!" if _done == _total else "Tobi remains skeptical."
    mo.callout(
        mo.md(f"**Core exercises: {_done}/{_total} correct** — {_tobi}"),
        kind="success" if _done == _total else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Before you leave

    1. Check the progress box above — all green?
    2. **Download your work**: **Cmd/Ctrl+S**, then menu → Download → Python. Reloading this exact
       tab (Cmd/Ctrl+R) keeps your work, but closing the tab and reopening the
       link starts you fresh. The download is the only guaranteed copy.
    3. Next episode: TODO teaser sentence.
    """
    )
    return


if __name__ == "__main__":
    app.run()
