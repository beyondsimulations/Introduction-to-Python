# notebooks/exercises/ex_02_e.py
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
    # Quick exercise: de-shout the menu (5–10 min)

    Tobi typed a new menu item IN ALL CAPS, WITH EXCLAMATION MARKS, and
    stray spaces. Chain string methods on `raw_item` below to turn it into
    exactly `"Falafel Wrap"` and store the result in `item_exe`.

    Useful methods: `.strip()`, `.rstrip("!")`, `.title()`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Saving your work:** this notebook runs in your browser. Press"
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
    item_exe = None
    return (item_exe,)


@app.cell(hide_code=True)
def _(item_exe, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if item_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `item_exe` (a `print` alone doesn't count) and run the cell."
    elif item_exe == "Falafel Wrap":
        _ok = True
        _msg = "Correct — Tobi's shouting is gone."
    else:
        _ok = False
        _msg = "Wrong — watch the order: strip spaces first, then the !!!, then Title Case."
    mo.callout(mo.md(_msg + show_result(item_exe)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** Tobi tried the same trick on the daily special:

    ```python
    raw_special.rstrip("!").strip().title()
    ```

    and got `Miso Ramen!!`. The `!!` survived. Work out why, then chain the
    methods in an order that works and store `"Miso Ramen"` in `special_exe`.
    """
    )
    return


@app.cell
def _():
    # Given: do not change this
    raw_special = "  MISO RAMEN!!  "
    return (raw_special,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    special_exe = None
    return (special_exe,)


@app.cell(hide_code=True)
def _(mo, show_result, special_exe):
    # Reactive check. Re-runs when you run the cell above.
    if special_exe is None:
        _ok = False
        _msg = "Not attempted — assign it to `special_exe` (a `print` alone doesn't count) and run the cell."
    elif special_exe == "Miso Ramen":
        _ok = True
        _msg = "Correct — `.rstrip(\"!\")` only sees the **end** of the string, and in Tobi's order the end was still spaces. Strip the spaces first."
    elif special_exe == "Miso Ramen!!":
        _ok = False
        _msg = "Wrong — that is still Tobi's order. When `.rstrip(\"!\")` runs, the string still ends in spaces, so there is no `!` at the end to remove."
    else:
        _ok = False
        _msg = "Wrong — aim for exactly `Miso Ramen`: outer spaces first, then the `!!`, then Title Case."
    mo.callout(mo.md(_msg + show_result(special_exe)), kind="success" if _ok else "warn")
    return

@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
