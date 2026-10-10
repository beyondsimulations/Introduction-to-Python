# Lab 08: The Data Room
# Programming with Python, Episode 8
#
# The investor slid a USB stick across the table: every order of the last
# two weeks. Tobi exported it from the ordering system into orders_messy.csv.
# Nobody has looked at it yet.
#
# HOW TO RUN THIS LAB
#   1. Put this file and orders_messy.csv into your python-labs folder.
#   2. In Zed, open the python-labs folder, then the terminal (Ctrl+`).
#   3. Type:  uv run python lab_08_dataroom.py
#
# HOW THE LAB WORKS
#   - The lab is not graded. The checks are there so you know where you
#     stand.
#   - Work from top to bottom. Every task ends in a few checks (the assert
#     lines). The script stops at the first check that fails and says what
#     is wrong, so your first run ends with "Task 1: not attempted yet."
#     Solve the task, save the file and run it again.
#   - Write your code under the lines that say YOUR CODE BELOW. Leave the
#     rest as it is.
#   - The checks test the form of your answers, for example that a dict has
#     four zones or that a share lies between 0 and 100. They do not know
#     the right numbers, so a wrong number can pass every check.
#   - You may use Mistral Vibe. Ask it for one task at a time, read what it
#     wrote, and test it on a case where you know the answer.
#   - When every check passes, the script prints a block that starts with
#     SHOW THIS IN CLASS. Show it to your lecturer, who tells you whether
#     your numbers are right. You may leave either way.

# %% Load the data (given, do not change)
import numbers
from pathlib import Path

import pandas as pd

assert Path("orders_messy.csv").exists(), (
    "orders_messy.csv is not in the folder you are running from. "
    "Put it next to this script in python-labs and run the script there."
)
orders = pd.read_csv("orders_messy.csv")
pd.set_option("display.width", 120)  # print all columns side by side
pd.set_option("display.max_columns", None)  # and never hide one behind "..."


def is_number(value):
    """Used by the checks: True for one number, False for a table or a text."""
    return isinstance(value, numbers.Real) and not isinstance(value, bool)


# %% Task 1: a first look
# Before you count anything, look at what Tobi gave you. The three lines
# below print the first rows, the list of columns and a summary of the
# numeric columns. Read all three before you go on.
print(orders.head())
orders.info()
print(orders.describe().round(2))

# In the middle output, "Non-Null Count" is the number of rows that have a
# value in that column.
#
# Two things you can read from that output:
#   raw_rows      how many rows the file has
#   unrated_rows  how many of those rows have no rating
# YOUR CODE BELOW
raw_rows = None
unrated_rows = None

# Checks (do not change)
assert raw_rows is not None and unrated_rows is not None, "Task 1: not attempted yet."
assert is_number(raw_rows) and is_number(unrated_rows), (
    "Task 1: raw_rows and unrated_rows should each be one whole number."
)
assert raw_rows == len(orders), (
    f"Task 1: the file does not have {raw_rows} rows. Read the output again."
)
assert raw_rows - unrated_rows == orders["rating"].count(), (
    f"Task 1: {unrated_rows} rows without a rating does not fit the output above."
)
print("Task 1 passed:", raw_rows, "rows,", unrated_rows, "of them without a rating")

# %% Task 2: how many orders?
# The investor: "My own system shows fewer orders for these two weeks than
# your file has rows."
#
# Find out why. Then build:
#   clean        a DataFrame with every order in it exactly once
#   order_count  how many orders that is
# YOUR CODE BELOW
clean = None
order_count = None

# Checks (do not change)
assert clean is not None and order_count is not None, "Task 2: not attempted yet."
assert isinstance(clean, pd.DataFrame), "Task 2: clean should be a DataFrame."
assert list(clean.columns) == list(orders.columns), (
    "Task 2: clean should have the same columns as orders, in the same order."
)
assert clean["order_id"].is_unique, (
    "Task 2: at least one order is still in clean more than once."
)
assert clean["order_id"].nunique() >= 0.9 * orders["order_id"].nunique(), (
    "Task 2: clean has lost orders. More than one in ten order ids from the file is missing."
)
assert is_number(order_count) and order_count == len(clean), (
    "Task 2: order_count should be the number of rows in clean."
)
print("Task 2 passed:", order_count, "orders")

# %% Task 3: Tobi's Hafen number
# Tobi wrote the line below before anybody had looked at the file. It runs
# and it prints a number. The investor reads it and shakes her head: "Hafen
# is missing orders. That zone brought in more than this."
#
# Tobi's code (given, do not change):
tobi_hafen = float(orders[orders["zone"] == "Hafen"]["total_eur"].sum())
print("Tobi's Hafen revenue:", round(tobi_hafen, 2))

# Find out what Tobi's line misses. Repair clean itself, so that it knows
# exactly four zones. Then compute:
#   hafen_revenue  the revenue of all Hafen orders in clean, in euros,
#                  rounded to 2 decimals
# YOUR CODE BELOW
hafen_revenue = None

# Checks (do not change)
assert hafen_revenue is not None, "Task 3: not attempted yet."
assert clean["zone"].nunique() == 4, (
    f"Task 3: clean has {clean['zone'].nunique()} different zone names. "
    "The company delivers to 4 zones."
)
assert len(clean) == order_count, (
    "Task 3: clean changed its size after Task 2. If rows have to go, "
    "remove them in Task 2, where clean is built."
)
assert is_number(hafen_revenue), "Task 3: hafen_revenue should be one number."
assert hafen_revenue > tobi_hafen, (
    "Task 3: hafen_revenue is not larger than Tobi's number, "
    "so Hafen is still missing orders."
)
assert abs(hafen_revenue - clean[clean["zone"] == "Hafen"]["total_eur"].sum()) < 0.01, (
    "Task 3: hafen_revenue does not match the Hafen rows of clean."
)
print("Task 3 passed: Hafen revenue", hafen_revenue)

# %% Task 4: revenue per zone
# The investor asks per zone: which zone brings in the most revenue?
#
#   revenue_by_zone  a dict, zone name -> revenue in euros, rounded to 2 decimals
#   top_share        the share of all revenue that comes from the zone with
#                    the highest revenue, in percent, rounded to 2 decimals
# YOUR CODE BELOW
revenue_by_zone = None
top_share = None

# Checks (do not change)
assert revenue_by_zone is not None and top_share is not None, "Task 4: not attempted yet."
assert isinstance(revenue_by_zone, dict), (
    f"Task 4: revenue_by_zone should be a dict, not a {type(revenue_by_zone).__name__}."
)
assert set(revenue_by_zone) == set(clean["zone"]), (
    "Task 4: the keys of revenue_by_zone should be the zone names in clean."
)
assert all(is_number(v) and v > 0 for v in revenue_by_zone.values()), (
    "Task 4: every value in revenue_by_zone should be a positive number."
)
assert abs(sum(revenue_by_zone.values()) - clean["total_eur"].sum()) < 0.05, (
    "Task 4: the zone revenues do not add up to the total revenue in clean."
)
assert is_number(top_share), "Task 4: top_share should be one number."
assert 25 <= top_share <= 100, (
    f"Task 4: a top_share of {top_share} percent cannot be right. "
    "With four zones the top zone holds at least 25 percent."
)
print("Task 4 passed:", revenue_by_zone, "| top share", top_share, "percent")

# %% Task 5: critical deliveries
# As in Episode 7, a delivery that takes more than 50 minutes is critical.
# Work on a copy, so that clean stays as it is.
#
#   timed                   a copy of clean with one more column, critical:
#                           True where the delivery was critical, else False
#   critical_count          how many deliveries were critical
#   critical_share_by_zone  a dict, zone name -> percent of that zone's
#                           deliveries that were critical, rounded to 1 decimal
# YOUR CODE BELOW
timed = None
critical_count = None
critical_share_by_zone = None

# Checks (do not change)
assert timed is not None and critical_count is not None, "Task 5: not attempted yet."
assert critical_share_by_zone is not None, "Task 5: critical_share_by_zone is still None."
assert isinstance(timed, pd.DataFrame) and "critical" in timed.columns, (
    "Task 5: timed should be a DataFrame with a column named critical."
)
assert "critical" not in clean.columns, (
    "Task 5: clean has a critical column now, so timed is not a copy."
)
assert len(timed) == len(clean), "Task 5: timed should have as many rows as clean."
assert timed["critical"].dtype == bool, (
    "Task 5: the critical column should hold only True and False."
)
assert timed.loc[timed["critical"], "delivery_min"].min() > 50, (
    "Task 5: a delivery of 50 minutes or less is marked as critical."
)
assert timed.loc[~timed["critical"], "delivery_min"].max() <= 50, (
    "Task 5: a delivery of more than 50 minutes is not marked as critical."
)
assert is_number(critical_count) and critical_count == timed["critical"].sum(), (
    "Task 5: critical_count does not match the critical column of timed."
)
assert isinstance(critical_share_by_zone, dict), (
    "Task 5: critical_share_by_zone should be a dict."
)
assert set(critical_share_by_zone) == set(clean["zone"]), (
    "Task 5: the keys of critical_share_by_zone should be the zone names in clean."
)
assert all(is_number(v) and 0 <= v <= 100 for v in critical_share_by_zone.values()), (
    "Task 5: every share should be a number between 0 and 100."
)
assert max(critical_share_by_zone.values()) > 1, (
    "Task 5: the shares look like fractions. They should be in percent."
)
orders_per_zone = clean["zone"].value_counts()
implied = sum(share / 100 * orders_per_zone[zone] for zone, share in critical_share_by_zone.items())
assert abs(implied - critical_count) < 0.5, (
    "Task 5: the shares do not fit critical_count. Each share compares a "
    "zone's critical deliveries with all deliveries of that same zone."
)
print("Task 5 passed:", critical_count, "critical |", critical_share_by_zone)

# %% Task 6: Tobi's rating
# Tobi asked his agent to "clean up the missing ratings" and got the line
# below. It runs. The investor reads the result and laughs: "Your average
# rating is lower than the worst rating any customer ever gave you?"
#
# Tobi's code (given, do not change):
tobi_rating = round(float(clean["rating"].fillna(0).mean()), 2)
print("Tobi's average rating:", tobi_rating)

# Find out why Tobi's number is so low. Then compute:
#   avg_rating  the average of the ratings that customers gave,
#               rounded to 2 decimals
# YOUR CODE BELOW
avg_rating = None

# Checks (do not change)
assert avg_rating is not None, "Task 6: not attempted yet."
assert is_number(avg_rating), "Task 6: avg_rating should be one number."
assert clean["rating"].min() <= avg_rating <= clean["rating"].max(), (
    f"Task 6: an average of {avg_rating} is not between the lowest and the "
    "highest rating a customer gave."
)
print("Task 6 passed: average rating", avg_rating)

# %% Task 7: the zone report
# The company can pay for one more rider. The investor wants a table she can
# read in ten seconds, and your decision.
#
#   zone_report     a DataFrame with one row per zone, sorted by revenue with
#                   the highest first, and exactly these columns:
#                     zone            the zone name
#                     orders          how many orders
#                     revenue         in euros, rounded to 2 decimals
#                     avg_order       revenue per order, rounded to 2 decimals
#                     critical_share  percent of the zone's deliveries that
#                                     were critical, rounded to 1 decimal
#   recommendation  one sentence, as a string: which zone gets the new
#                   rider, and why. There is no single right answer here.
#                   Argue from your table.
# YOUR CODE BELOW
zone_report = None
recommendation = None

# Checks (do not change)
assert zone_report is not None and recommendation is not None, "Task 7: not attempted yet."
assert isinstance(zone_report, pd.DataFrame), "Task 7: zone_report should be a DataFrame."
assert list(zone_report.columns) == ["zone", "orders", "revenue", "avg_order", "critical_share"], (
    "Task 7: zone_report should have exactly the columns zone, orders, revenue, "
    f"avg_order, critical_share. Yours has: {list(zone_report.columns)}"
)
assert set(zone_report["zone"]) == set(clean["zone"]) and len(zone_report) == 4, (
    "Task 7: zone_report should have one row for each of the four zones."
)
assert zone_report["orders"].sum() == order_count == len(clean), (
    "Task 7: the orders column does not add up to order_count. If clean "
    "changed after Task 2, make that change in Task 2 instead."
)
assert abs(zone_report["revenue"].sum() - sum(revenue_by_zone.values())) < 0.05, (
    "Task 7: the revenue column does not add up to the total in revenue_by_zone."
)
assert list(zone_report["revenue"]) == sorted(zone_report["revenue"], reverse=True), (
    "Task 7: zone_report is not sorted by revenue with the highest first."
)
assert (zone_report["avg_order"] - zone_report["revenue"] / zone_report["orders"]).abs().max() < 0.01, (
    "Task 7: avg_order should be revenue divided by orders, row by row."
)
assert zone_report["critical_share"].between(0, 100).all(), (
    "Task 7: every critical_share should be between 0 and 100."
)
assert isinstance(recommendation, str) and len(recommendation.split()) >= 8, (
    "Task 7: recommendation should be a full sentence of at least 8 words, as a string."
)
assert any(zone in recommendation for zone in revenue_by_zone), (
    "Task 7: recommendation should name the zone that gets the rider."
)

# %% Show this in class
print()
print("=" * 60)
print("SHOW THIS IN CLASS: Lab 08, The Data Room")
print("=" * 60)
print("Orders after cleaning:", order_count)
print("Revenue per zone:     ", revenue_by_zone)
print("Top zone's share:     ", top_share, "percent")
print("Critical deliveries:  ", critical_count)
print("Average rating:       ", avg_rating)
print()
print(zone_report.to_string(index=False))
print()
print("Recommendation:", recommendation)
print("=" * 60)
print("Every check passed. The checks only test the form of your answers.")
print("Before you show this: would the investor believe each number?")
