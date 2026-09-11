# notebooks/exercises/ex_04_a.py
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
    # Quick exercise: the courier route (5–10 min)

    Tobi planned tonight's route as a list of stops, in order:

    ```python
    route = ["Mensa", "Library", "Dorm A", "Gym", "Dorm B"]
    ```

    The courier has already delivered the first **two** stops. Store the
    stops still to come in `remaining_exa`, as one **slice** of `route`.
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


@app.cell
def _():
    # Given: do not change this
    route = ["Mensa", "Library", "Dorm A", "Gym", "Dorm B"]
    return (route,)


@app.cell
def _(route):
    # YOUR CODE BELOW: replace None
    remaining_exa = None
    return (remaining_exa,)


@app.cell(hide_code=True)
def _(mo, remaining_exa, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if remaining_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `remaining_exa` (a `print` alone doesn't count) and run the cell."
    elif remaining_exa == ["Dorm A", "Gym", "Dorm B"]:
        _ok = True
        _msg = "Correct — three stops to go, starting at index 2."
    elif remaining_exa == ["Library", "Dorm A", "Gym", "Dorm B"]:
        _ok = False
        _msg = "Wrong — the Library was stop number two, and it's done. Python counts from 0: the third stop lives at index 2."
    elif remaining_exa == ["Dorm A", "Gym"]:
        _ok = False
        _msg = "Wrong — the `stop` index is excluded, so the last stop fell off. Leave the right side of the slice empty to run to the end."
    elif isinstance(remaining_exa, str):
        _ok = False
        _msg = "Wrong — that's a single stop, not a list. A slice needs a colon: `route[start:stop]`."
    else:
        _ok = False
        _msg = "Wrong — the slice should start at index 2 and run to the end of `route`."
    mo.callout(mo.md(_msg + show_result(remaining_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** the Mensa and the last dorm are the two hubs where the
    courier picks up and hands over the bag. Store only the stops **between**
    them, first and last dropped, in `middle_exa`. One slice, no `len()`:
    count the end from the end.
    """
    )
    return


@app.cell
def _(route):
    # YOUR CODE BELOW: replace None
    middle_exa = None
    return (middle_exa,)


@app.cell(hide_code=True)
def _(middle_exa, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if middle_exa is None:
        _ok = False
        _msg = "Not attempted — assign it to `middle_exa` (a `print` alone doesn't count) and run the cell."
    elif middle_exa == ["Library", "Dorm A", "Gym"]:
        _ok = True
        _msg = "Correct — `route[1:-1]`: start after the first, stop before the last."
    elif middle_exa == ["Library", "Dorm A", "Gym", "Dorm B"]:
        _ok = False
        _msg = "Wrong — the last dorm is still in. A negative `stop` of `-1` stops right before the final item."
    elif middle_exa == ["Library", "Dorm A"]:
        _ok = False
        _msg = "Wrong — one stop too few. The `stop` index is excluded, so `-1` already drops the last item; `-2` drops two."
    else:
        _ok = False
        _msg = "Wrong — start at index 1 and stop at `-1`."
    mo.callout(mo.md(_msg + show_result(middle_exa)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
