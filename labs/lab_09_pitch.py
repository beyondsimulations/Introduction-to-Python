# Lab 09: The Pitch Deck
# Programming with Python, Episode 9
#
# Friday is the pitch, and the investor has asked for one thing: "Bring me
# charts I can't argue with." Tobi has already built a deck: two slides and
# one argument for a new rider. You build the deck she gets to see: six
# charts from the same orders_messy.csv as last week.
#
# HOW TO RUN THIS LAB
#   1. Put this file into your python-labs folder. orders_messy.csv is
#      still there from last week.
#   2. In Zed, open the python-labs folder, then the terminal (Ctrl+`).
#   3. Type:  uv run python lab_09_pitch.py
#
# HOW THE LAB WORKS
#   - The lab is not graded. The checks are there so you know where you
#     stand.
#   - As in Lab 08: work from top to bottom and write your code under the
#     lines that say YOUR CODE BELOW. Every task ends in a few checks (the
#     assert lines). The script stops at the first check that fails and
#     says what is wrong. Solve the task, save the file and run it again.
#   - A script has no cell that could show a chart, so every chart goes
#     into a picture file. Task 2 shows how.
#   - No task names the kind of chart. Pick the kind that fits the
#     question: line, bar, histogram or scatter.
#   - Every chart needs a title and a label on both axes.
#   - The checks test the form of a chart, for example that it has a title
#     or that its bars add up to your own numbers. They cannot see whether
#     a chart tells the truth.
#   - You may use Mistral Vibe. Ask it for one task at a time, read what it
#     wrote, and look at the picture it made.
#   - When every check passes, the script puts your six charts side by
#     side into pitch_deck.png and prints a block that starts with SHOW
#     THIS IN CLASS. Show both to your lecturer for feedback. You may
#     leave either way.

# %% Load the data (given, do not change)
import numbers
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # charts go into picture files, no window opens
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

assert Path("orders_messy.csv").exists(), (
    "orders_messy.csv is not in the folder you are running from. "
    "Put it next to this script in python-labs and run the script there."
)
orders = pd.read_csv("orders_messy.csv")
pd.set_option("display.width", 120)  # print all columns side by side
pd.set_option("display.max_columns", None)  # and never hide one behind "..."
run_started = time.time()


def is_number(value):
    """Used by the checks: True for one number, False for a table or a text."""
    return isinstance(value, numbers.Real) and not isinstance(value, bool)


def check_chart(task, chart, file_name):
    """Used by the checks: the form that every chart in this lab must have."""
    assert isinstance(chart, plt.Axes), (
        f"Task {task}: store the chart itself, the thing that plt.gca() gives you."
    )
    assert chart.has_data(), (
        f"Task {task}: the chart you stored is empty. Store it before you close the canvas."
    )
    assert chart.get_title().strip(), f"Task {task}: the chart has no title."
    assert chart.get_xlabel().strip() and chart.get_ylabel().strip(), (
        f"Task {task}: both axes need a label that says what they show."
    )
    assert Path(file_name).exists(), f"Task {task}: there is no file {file_name} in this folder."
    assert Path(file_name).stat().st_mtime > run_started - 2, (
        f"Task {task}: {file_name} is left over from an earlier run. This run did not save it."
    )
    assert not plt.get_fignums(), (
        f"Task {task}: a canvas is still open. Close it once the picture is saved, "
        "or the next chart is drawn on top of this one."
    )


def drawn(chart):
    """Used by the checks: what a chart shows, as a list of (kind, y values).

    kind is "line", "points" (no line joins them) or "bars".
    """
    found = []
    for line in chart.lines:
        joined = line.get_linestyle() not in ("None", "", " ")
        heights = pd.to_numeric(pd.Series(list(line.get_ydata())), errors="coerce")
        found.append(("line" if joined else "points", heights.to_numpy(dtype=float)))
    for cloud in chart.collections:
        points = np.ma.filled(np.ma.asarray(cloud.get_offsets(), dtype=float), np.nan)
        found.append(("points", points[:, 1]))
    bars = [bar.get_height() for bar in chart.patches if hasattr(bar, "get_height")]
    if bars:
        found.append(("bars", np.array(bars, dtype=float)))
    return found


# %% Task 1: clean again
# The lines above have read orders_messy.csv into orders. Tobi has not touched
# the file since last week, so everything that was wrong with it still is.
#
#   clean        a DataFrame with every order in it exactly once and with
#                exactly four zone names
#   order_count  how many orders that is
# YOUR CODE BELOW
clean = None
order_count = None

# Checks (do not change)
assert clean is not None and order_count is not None, "Task 1: not attempted yet."
assert isinstance(clean, pd.DataFrame), "Task 1: clean should be a DataFrame."
assert list(clean.columns) == list(orders.columns), (
    "Task 1: clean should have the same columns as orders, in the same order."
)
assert clean["order_id"].is_unique, (
    "Task 1: at least one order is still in clean more than once."
)
assert clean["order_id"].nunique() >= 0.9 * orders["order_id"].nunique(), (
    "Task 1: clean has lost orders. More than one in ten order ids from the file is missing."
)
assert clean["zone"].nunique() == 4, (
    f"Task 1: clean has {clean['zone'].nunique()} different zone names. "
    "The company delivers to 4 zones."
)
assert is_number(order_count) and order_count == len(clean), (
    "Task 1: order_count should be the number of rows in clean."
)
print("Task 1 passed:", order_count, "orders")

# %% Task 2: the two weeks at a glance
# The deck opens with the question every investor asks first: how much
# revenue came in, day by day?
#
# This is your first chart in a script. Start it with plt.figure(), a fresh
# canvas as in the lecture, draw it, and end it with these three lines:
#     daily_chart = plt.gca()     # keeps the chart for the checks
#     plt.savefig("daily.png")    # writes the picture into python-labs
#     plt.close()                 # closes the canvas, so that the next
#                                 # chart starts on a fresh one
# Every chart in this lab ends like this, with its own two names. To look
# at the picture, click daily.png in Zed's project panel, the file list on
# the left.
#
#   daily.png    the revenue of each day, from clean, days 1 to 14 in order
#   daily_chart  the chart
#   best_day     the number of the day with the highest revenue
# YOUR CODE BELOW
daily_chart = None
best_day = None

# Checks (do not change)
assert daily_chart is not None, "Task 2: not attempted yet."
check_chart(2, daily_chart, "daily.png")
assert len(daily_chart.lines) == 1, (
    f"Task 2: daily.png should show exactly one line, the revenue per day. "
    f"Yours shows {len(daily_chart.lines)}."
)
day_values = list(daily_chart.lines[0].get_xdata())
assert day_values == sorted(clean["day"].unique()), (
    f"Task 2: the line needs one point per day, at the days 1 to 14. "
    f"Yours has {len(day_values)} points and starts at x = {day_values[0]}."
)
day_revenues = drawn(daily_chart)[0][1]
assert abs(day_revenues.sum() - clean["total_eur"].sum()) < 0.05, (
    "Task 2: the points of your line do not add up to the revenue of all orders in clean."
)
assert best_day is not None, "Task 2: best_day is still None."
assert is_number(best_day) and best_day == day_values[int(day_revenues.argmax())], (
    "Task 2: best_day is not the day at which your own line is highest."
)
print("Task 2 passed: daily.png, best day", best_day)

# %% Task 3: the zones
# Last week's table becomes a picture: which zone brings in the most
# revenue? The investor should see the answer without reading a number, so
# the zone with the highest revenue stands on the left.
#
#   zones.png    the revenue of each zone, from clean, highest first
#   zones_chart  the chart
#   top_zone     the name of the zone with the highest revenue
# YOUR CODE BELOW
zones_chart = None
top_zone = None

# Checks (do not change)
assert zones_chart is not None, "Task 3: not attempted yet."
check_chart(3, zones_chart, "zones.png")
zone_bars = [heights for kind, heights in drawn(zones_chart) if kind == "bars"]
assert zone_bars and len(zone_bars[0]) == clean["zone"].nunique(), (
    f"Task 3: zones.png should show one bar per zone, {clean['zone'].nunique()} bars in all."
)
assert zone_bars[0].max() > 1, (
    "Task 3: the bars lie on their side. Let them stand, with the zones on the x-axis."
)
assert abs(zone_bars[0].sum() - clean["total_eur"].sum()) < 0.05, (
    "Task 3: the bars do not add up to the revenue of all orders in clean."
)
assert list(zone_bars[0]) == sorted(zone_bars[0], reverse=True), (
    "Task 3: the bars are not sorted with the highest first."
)
assert top_zone is not None, "Task 3: top_zone is still None."
first_bar = zones_chart.patches[0]
first_middle = first_bar.get_x() + first_bar.get_width() / 2
under_first = [
    label.get_text()
    for label in zones_chart.get_xticklabels()
    if abs(label.get_position()[0] - first_middle) < 0.01
]
first_label = under_first[0] if under_first else ""
assert top_zone == first_label, (
    f"Task 3: top_zone is {top_zone!r}, but the label under your first bar reads {first_label!r}."
)
print("Task 3 passed: zones.png, top zone", top_zone)

# %% Task 4: what an order is worth
# The investor: "What does a typical order bring in? And how many big ones
# do you get?" One average hides the second answer. A picture of how the
# order values (total_eur) are spread shows both.
#
#   values.png    how the order values in clean are spread: which amounts
#                 are common and which are rare
#   values_chart  the chart
#   big_orders    how many orders are worth more than 25 euros
# YOUR CODE BELOW
values_chart = None
big_orders = None

# Checks (do not change)
assert values_chart is not None, "Task 4: not attempted yet."
check_chart(4, values_chart, "values.png")
value_bars = [heights for kind, heights in drawn(values_chart) if kind == "bars"]
assert value_bars and abs(value_bars[0].sum() - len(clean)) < 0.5, (
    "Task 4: values.png should count orders. Its bars together have to "
    "stand for every order in clean exactly once."
)
left_edge = min(bar.get_x() for bar in values_chart.patches)
right_edge = max(bar.get_x() + bar.get_width() for bar in values_chart.patches)
assert left_edge <= clean["total_eur"].min() + 0.01 and right_edge >= clean["total_eur"].max() - 0.01, (
    "Task 4: the x-axis of values.png should carry the order values, from "
    "the smallest order in clean to the largest."
)
assert big_orders is not None, "Task 4: big_orders is still None."
assert is_number(big_orders) and 0 <= big_orders <= len(clean), (
    "Task 4: big_orders should be one whole number, and not more than there are orders."
)
print("Task 4 passed: values.png,", big_orders, "orders above 25 euros")

# %% Task 5: Tobi's growth slide
# Tobi's first slide compares the two weeks under the title "Revenue is
# taking off". His code runs and saves the slide as tobi_growth.png. Open it.
#
# Tobi's code (given, do not change):
tobi_week1 = round(float(orders[orders["day"] <= 7]["total_eur"].sum()), 2)
tobi_week2 = round(float(orders[orders["day"] >= 8]["total_eur"].sum()), 2)
plt.figure()
plt.plot([1, 2], [tobi_week1, tobi_week2], marker="o")
plt.ylim(780, 855)
plt.xticks([1, 2])
plt.xlabel("Week")
plt.ylabel("Revenue (EUR)")
plt.title("Revenue is taking off")
plt.savefig("tobi_growth.png")
plt.close()
print("Tobi's two weeks:", tobi_week1, "and", tobi_week2)

# The investor reads the axis before she reads the line: "Why does your
# chart start at 780 euros?"
#
# Draw the slide that she cannot argue with:
#   week1, week2  the revenue of days 1 to 7 and of days 8 to 14, in euros,
#                 rounded to 2 decimals
#   growth_pct    the change from week 1 to week 2, in percent of week 1,
#                 rounded to 2 decimals
#   growth.png    the two weeks, on a y-axis that starts at 0
#   growth_chart  the chart
# YOUR CODE BELOW
week1 = None
week2 = None
growth_pct = None
growth_chart = None

# Checks (do not change)
assert growth_chart is not None, "Task 5: not attempted yet."
assert week1 is not None and week2 is not None and growth_pct is not None, (
    "Task 5: week1, week2 or growth_pct is still None."
)
assert is_number(week1) and is_number(week2) and is_number(growth_pct), (
    "Task 5: week1, week2 and growth_pct should each be one number."
)
assert abs(week1 + week2 - clean["total_eur"].sum()) < 0.2 * clean["total_eur"].sum(), (
    "Task 5: week1 and week2 together are far away from the revenue of all orders."
)
assert abs(growth_pct - (week2 - week1) / week1 * 100) < 0.01, (
    "Task 5: growth_pct does not fit your own week1 and week2."
)
check_chart(5, growth_chart, "growth.png")
assert growth_chart.get_ylim()[0] == 0, (
    f"Task 5: the y-axis of growth.png starts at {round(float(growth_chart.get_ylim()[0]), 1)}, not at 0."
)
growth_shown = [heights for kind, heights in drawn(growth_chart)]
assert len(growth_shown) == 1 and len(growth_shown[0]) == 2, (
    "Task 5: growth.png should show two values and nothing else: week 1, then week 2."
)
assert abs(growth_shown[0][0] - week1) < 0.01 and abs(growth_shown[0][1] - week2) < 0.01, (
    "Task 5: the two values in growth.png are not your week1 and week2."
)
print("Task 5 passed: growth.png,", week1, "and", week2, "|", growth_pct, "percent")

# %% Task 6: Tobi's momentum slide
# Tobi's second slide has three points and the title "Revenue quadrupled in
# three days". His code saves it as tobi_momentum.png. Open it.
#
# Tobi's code (given, do not change):
tobi_daily = orders.groupby("day")["total_eur"].sum().round(2)
tobi_days = [6, 7, 8]
tobi_revenue = [float(tobi_daily[6]), float(tobi_daily[7]), float(tobi_daily[8])]
plt.figure()
plt.plot(tobi_days, tobi_revenue, marker="o")
plt.xticks(tobi_days)
plt.xlabel("Day")
plt.ylabel("Revenue (EUR)")
plt.title("Revenue quadrupled in three days")
plt.savefig("tobi_momentum.png")
plt.close()
print("Tobi's three days:", tobi_revenue)

# The investor: "Three days? Your file covers fourteen."
#
#   momentum.png    the revenue of all fourteen days and, on the same chart
#                   in a second color, the three days from Tobi's slide.
#                   A legend says which is which
#   momentum_chart  the chart
#   typical_day     the revenue of an average day, in euros, rounded to
#                   2 decimals
# YOUR CODE BELOW
momentum_chart = None
typical_day = None

# Checks (do not change)
assert momentum_chart is not None, "Task 6: not attempted yet."
check_chart(6, momentum_chart, "momentum.png")
day_count = clean["day"].nunique()
shown = [heights for kind, heights in drawn(momentum_chart) if kind != "bars"]
for group in momentum_chart.containers:  # every set of bars counts on its own
    bars = [bar.get_height() for bar in group if hasattr(bar, "get_height")]
    if bars:
        shown.append(np.array(bars, dtype=float))
sizes = [len(heights) for heights in shown]
assert day_count in sizes and 3 in sizes, (
    f"Task 6: momentum.png should show all {day_count} days and, drawn once more, "
    f"Tobi's 3 days. Yours draws {' and '.join(str(size) for size in sizes[:4]) or 'no'}"
    f"{' and more' if len(sizes) > 4 else ''} points."
)
assert momentum_chart.get_legend() is not None, (
    "Task 6: the chart has no legend, so nobody can tell Tobi's days from the rest."
)
assert typical_day is not None, "Task 6: typical_day is still None."
all_days = next(heights for heights in shown if len(heights) == day_count)
assert is_number(typical_day) and abs(typical_day - all_days.mean()) < 0.01, (
    f"Task 6: typical_day is not the average of the {day_count} days on your chart."
)
print("Task 6 passed: momentum.png, typical day", typical_day)

# %% Task 7: Tobi's rider argument
# Tobi wants the new rider from last week, and he wants a slide that makes
# his case to the investor. His argument: "Slow deliveries cost us stars."
#
#   stars.png    one point for every order in clean that has a rating: its
#                delivery time on the x-axis, its rating on the y-axis
#   stars_chart  the chart
#   stars_title  the title on your chart, as a string: what the picture
#                shows, in one sentence
# YOUR CODE BELOW
stars_chart = None
stars_title = None

# Checks (do not change)
assert stars_chart is not None, "Task 7: not attempted yet."
check_chart(7, stars_chart, "stars.png")
rated_count = int(clean["rating"].count())
clouds = [heights[~np.isnan(heights)] for kind, heights in drawn(stars_chart) if kind == "points"]
assert any(len(cloud) == rated_count for cloud in clouds), (
    f"Task 7: stars.png needs {rated_count} single points, one for every order "
    "in clean that has a rating, and no line that joins them."
)
star_values = next(cloud for cloud in clouds if len(cloud) == rated_count)
assert star_values.max() <= clean["rating"].max(), (
    "Task 7: the y-axis should carry the ratings, the x-axis the delivery times."
)
assert stars_title is not None, "Task 7: stars_title is still None."
assert isinstance(stars_title, str) and len(stars_title.split()) >= 3, (
    "Task 7: stars_title should be a sentence, as a string."
)
assert stars_chart.get_title() == stars_title, (
    "Task 7: stars_title is not the title on your chart."
)
print("Task 7 passed: stars.png,", repr(stars_title))

# %% Task 8: the pitch summary
# One page goes with the deck: the numbers behind the charts, and one
# sentence for the investor.
#
#   pitch     a dict with exactly these keys. Take every value from the
#             tasks above, do not type a number in by hand:
#               "orders"       how many orders
#               "revenue"      the revenue of all orders in clean, in
#                              euros, rounded to 2 decimals
#               "top_zone"     the zone with the highest revenue
#               "growth_pct"   the change from week 1 to week 2 in percent
#               "typical_day"  the revenue of an average day
#   headline  one sentence, as a string: what the investor should take
#             away from your six charts
# YOUR CODE BELOW
pitch = None
headline = None

# Checks (do not change)
assert pitch is not None and headline is not None, "Task 8: not attempted yet."
assert isinstance(pitch, dict), f"Task 8: pitch should be a dict, not a {type(pitch).__name__}."
assert set(pitch) == {"orders", "revenue", "top_zone", "growth_pct", "typical_day"}, (
    "Task 8: pitch should have exactly the keys orders, revenue, top_zone, "
    f"growth_pct, typical_day. Yours has: {sorted(pitch)}"
)
assert pitch["orders"] == order_count == len(clean), (
    "Task 8: the orders in pitch, order_count and the rows of clean do not "
    "agree. If clean changed after Task 1, make that change in Task 1 instead."
)
assert is_number(pitch["revenue"]) and abs(pitch["revenue"] - clean["total_eur"].sum()) < 0.01, (
    "Task 8: the revenue in pitch is not the revenue of all orders in clean."
)
assert pitch["top_zone"] == top_zone, "Task 8: the top_zone in pitch is not your top_zone from Task 3."
assert pitch["growth_pct"] == growth_pct, (
    "Task 8: the growth_pct in pitch is not your growth_pct from Task 5."
)
assert pitch["typical_day"] == typical_day, (
    "Task 8: the typical_day in pitch is not your typical_day from Task 6."
)
assert isinstance(headline, str) and len(headline.split()) >= 8, (
    "Task 8: headline should be a full sentence of at least 8 words, as a string."
)
print("Task 8 passed:", pitch)

# %% Task 9 (optional): your own question
# Done early? Ask the data one question that no task has asked, and answer
# it with a chart. If you skip this task, leave the three names at None.
#
#   own_question  your question, as a string
#   own.png       the chart that answers it
#   own_chart     the chart
#   own_answer    the answer in one sentence, as a string
# YOUR CODE BELOW
own_question = None
own_chart = None
own_answer = None

# Checks (do not change)
if own_question is None and own_chart is None and own_answer is None:
    print("Task 9 skipped. It is optional.")
else:
    assert isinstance(own_question, str) and own_question.strip().endswith("?"), (
        "Task 9: own_question should be a question, as a string."
    )
    check_chart(9, own_chart, "own.png")
    assert isinstance(own_answer, str) and len(own_answer.split()) >= 5, (
        "Task 9: own_answer should be a full sentence of at least 5 words, as a string."
    )
    print("Task 9 passed:", own_question, "|", own_answer)

# %% Show this in class (given, do not change)
deck_files = ["daily.png", "zones.png", "values.png", "growth.png", "momentum.png", "stars.png"]
deck, slides = plt.subplots(2, 3, figsize=(15, 7.5))
for slide, file_name in zip(slides.flat, deck_files):
    slide.imshow(plt.imread(file_name))
    slide.axis("off")
deck.tight_layout()
deck.savefig("pitch_deck.png", dpi=120)
plt.close()

print()
print("=" * 60)
print("SHOW THIS IN CLASS: Lab 09, The Pitch Deck")
print("=" * 60)
print("Orders after cleaning:", order_count)
print("Best day:             ", best_day)
print("Top zone:             ", top_zone)
print("Orders above 25 euros:", big_orders)
print("Week 1 and week 2:    ", week1, "and", week2)
print("Growth:               ", growth_pct, "percent")
print("Typical day:          ", typical_day)
print("Title of stars.png:   ", stars_title)
print()
print("Pitch:", pitch)
print("Headline:", headline)
if own_question is not None:
    print("Own question:", own_question, "|", own_answer)
print("=" * 60)
print("Every check passed. Your six charts are side by side in pitch_deck.png.")
print("The checks only test the form of your charts and numbers.")
print("Before you show the deck: would the investor believe each chart?")
