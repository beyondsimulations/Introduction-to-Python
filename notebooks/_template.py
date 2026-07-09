# notebooks/_template.py
# TEMPLATE — copy to nb_XX_lab_<topic>.py and replace TODO-marked content.
# Rules (spec §4): one global name per cell; += counts as a definition;
# every exercise pre-defines its answer as None; suffix exercise names (_ex1);
# underscore-prefixed names are cell-private.
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


@app.cell
def _():
    import marimo as mo
    return (mo,)


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
    mo.md(f"Welcome back to **{startup_name}**! Kevin already forgot the name again.")
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
def _(mo, revenue_ex1):
    # Reactive check — re-runs automatically whenever the cell above changes.
    if revenue_ex1 is None:
        ex1_ok = False
        _msg = "🔲 Exercise 1.1: not attempted yet."
    elif revenue_ex1 == 13.50:  # TODO expected value
        ex1_ok = True
        _msg = "✅ Exercise 1.1: correct! The investor nods approvingly."
    else:
        ex1_ok = False
        _msg = "❌ Exercise 1.1: not quite — check your multiplication."
    mo.md(_msg)
    return (ex1_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "💡 Hint 1 (a nudge)": "TODO: conceptual nudge, no code.",
            "💡 Hint 2 (the structure)": "TODO: code skeleton with a blank to fill.",
        }
    )
    return


@app.cell(hide_code=True)
def _(ex1_ok, mo):
    # Progress cell — extend the list as exercises are added.
    _checks = [ex1_ok]
    _done = sum(_checks)
    _total = len(_checks)
    _kevin = "Kevin is impressed!" if _done == _total else "Kevin remains skeptical."
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

    1. Check the progress box above — all green?
    2. **Download your work**: menu → Download → Python. Reloading this exact
       tab (Cmd/Ctrl+R) keeps your work, but closing the tab and reopening the
       link starts you fresh — the download is the only guaranteed copy.
    3. Next episode: TODO teaser sentence.
    """
    )
    return


if __name__ == "__main__":
    app.run()
