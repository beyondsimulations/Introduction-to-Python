# notebooks/exercises/ex_05_c.py
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
    # Quick exercise: the crash-proof price (5-10 min)

    A customer typed `"drei"` into the price field instead of a number, and
    the checkout went straight to a traceback in front of the whole queue.
    The crashing line:

    ```python
    order_text = "drei"
    price = float(order_text)
    ```

    Wrap `float(order_text)` in a `try`/`except ValueError` so that when the
    text isn't a number, the checkout **survives** and `price_exc` falls back
    to `0.0` instead of crashing.

    Careful: hardcoding `price_exc = 0.0` defeats the point. Your code must
    still work when the text *is* a number.
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
    order_text = "drei"
    return (order_text,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    price_exc = None
    return (price_exc,)


@app.cell(hide_code=True)
def _(mo, price_exc, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if price_exc is None:
        _ok = False
        _msg = "Not attempted: assign it to `price_exc` (a `print` alone doesn't count) and run the cell."
    elif isinstance(price_exc, float) and price_exc == 0.0:
        _ok = True
        _msg = "Correct: the checkout survives, and 0.0 flags the order for a human."
    else:
        _ok = False
        _msg = "Wrong: wrap the `float()` call in `try`/`except ValueError` and fall back to `0.0`."
    mo.callout(mo.md(_msg + show_result(price_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Done? Then:** Tobi wrote his own crash-proof version at 3 AM. It never
    crashes. It also never charges anyone. Run it, then find out **which
    exception** the bare `except:` is quietly swallowing. Assign the type's
    name as text to `hidden_exc`.

    Tip: make the `except` specific and the hidden crash reappears as a
    traceback.
    """
    )
    return


@app.cell
def _():
    # YOUR CODE BELOW: run it first, then narrow the except to see what it hides
    # TOBI'S CODE
    try:
        price_tobi = float(order_txt)
    except:
        price_tobi = 0.0
    print(price_tobi)
    return (price_tobi,)


@app.cell
def _():
    # YOUR CODE BELOW: replace None
    hidden_exc = None
    return (hidden_exc,)


@app.cell(hide_code=True)
def _(hidden_exc, mo, show_result):
    # Reactive check. Re-runs when you run the cell above.
    if hidden_exc is None:
        _ok = False
        _msg = "Not attempted: assign the name to `hidden_exc` as text (a `print` alone doesn't count) and run the cell."
    elif not isinstance(hidden_exc, str):
        _ok = False
        _msg = "Wrong: the answer is the exception's name as **text**, in quotes."
    elif hidden_exc.strip().lower().replace(" ", "") == "nameerror":
        _ok = True
        _msg = "Correct: `order_txt` is a typo of `order_text`, a `NameError`. The bare `except:` hid it, and every price silently became 0.0. Catch the specific type."
    elif hidden_exc.strip().lower().replace(" ", "") == "valueerror":
        _ok = False
        _msg = "Wrong: that's the one Tobi *meant* to catch. Change `except:` to `except ValueError:` and read the traceback that appears."
    else:
        _ok = False
        _msg = "Wrong: narrow the `except` to `ValueError` and read the last line of the traceback that shows up."
    mo.callout(mo.md(_msg + show_result(hidden_exc)), kind="success" if _ok else "warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("*Nothing to save. This was a sandbox.*")
    return


if __name__ == "__main__":
    app.run()
