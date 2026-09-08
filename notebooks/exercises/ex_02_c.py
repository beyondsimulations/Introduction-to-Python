# notebooks/exercises/ex_02_c.py
import marimo

app = marimo.App(width="medium")


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
    mo.md(
        r"""
    # Quick exercise: de-shout the menu (10 min)

    Tobi typed a new menu item IN ALL CAPS, WITH EXCLAMATION MARKS, and
    stray spaces. Chain string methods on `raw_item` below to turn it into
    exactly `"Falafel Wrap"` and store the result in `item_exc`.

    Useful methods: `.strip()`, `.rstrip("!")`, `.title()`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "💾 **Saving your work:** this notebook runs in your browser. Press "
            "**Cmd/Ctrl+S** to save, and always save **before** menu → Download → "
            "*Download Python code*. Without a save first, the download is an empty file."
        ),
        kind="info",
    )
    return


@app.cell
def _():
    # Given: do not change this
    raw_item = "  FALAFEL WRAP!!!  "
    return (raw_item,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    item_exc = None
    return (item_exc,)


@app.cell(hide_code=True)
def _(item_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if item_exc is None:
        _ok = False
        _msg = "🔲 Not attempted yet. Assign it to `item_exc` (a `print` alone doesn't count) and run the cell."
    elif item_exc == "Falafel Wrap":
        _ok = True
        _msg = "✅ Correct! Tobi's shouting is gone."
    else:
        _ok = False
        _msg = "❌ Not quite. Watch the order: strip spaces first, then the !!!, then Title Case."
    mo.callout(mo.md(_msg + show_result(item_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
