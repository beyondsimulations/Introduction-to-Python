"""Generate the canonical Part-II dataset (notebooks/public/orders.csv).

Deterministic (seeded): re-running must reproduce the committed file exactly.
Labs nb_08/nb_09 hard-code check values computed FROM this file — never edit
the CSV by hand and never change the seed without updating every dependent
check (see the freshness ledger in the Plan 3 document).
"""
import csv
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "notebooks" / "public" / "orders.csv"
ZONES = ["Nord", "Sued", "Hafen", "Altstadt"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DISHES = {"Bao Box": 7.80, "Falafel Wrap": 6.90, "Pad Thai": 8.90, "Miso Ramen": 11.50}  # menu prices from Episodes 1-4


def main() -> None:
    random.seed(2026)
    rows = []
    order_id = 1001
    for day in range(1, 15):  # two weeks of trading
        for _ in range(random.randint(4, 8)):
            dish = random.choice(list(DISHES))
            items = random.randint(1, 3)
            rows.append(
                {
                    "order_id": order_id,
                    "day": day,
                    "weekday": WEEKDAYS[(day - 1) % 7],
                    "zone": random.choice(ZONES),
                    "dish": dish,
                    "items": items,
                    "total_eur": round(items * DISHES[dish], 2),
                    "delivery_min": random.randint(12, 58),
                    "rating": round(random.uniform(3.0, 5.0), 1),
                }
            )
            order_id += 1
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} orders -> {OUT}")


if __name__ == "__main__":
    main()

# ledger:
# rows: 80
# revenue total: 1443.3
# mean order: 18.04
# zone totals: {'Altstadt': 376.2, 'Hafen': 325.3, 'Nord': 345.9, 'Sued': 395.9}
# orders per zone: {'Nord': 22, 'Altstadt': 20, 'Hafen': 19, 'Sued': 19}
# best day (revenue): 3 (146.8)
# max delivery: 58
# count total_eur > 20: 35
# count total_eur > 25: 13
# week1 / week2: 731.1 / 712.2  -> growth -2.59 %

# Lab ledgers (moved out of the notebook headers, which ship with the WASM export):
# --- from notebooks/nb_08_lab_dataroom.py ---
# ledger (all values computed FROM notebooks/public/orders.csv, cross-checked
# against helpers/make_orders_csv.py):
#   rows len(orders)                                            = 80
#   columns orders.shape[1]                                     = 9
#   revenue orders["total_eur"].sum()                          = 1443.3
#   Nord count len(orders[zone=="Nord"])                       = 22
#   Sued & items>=2 count                                      = 15
#   Hafen revenue orders[zone=="Hafen"]["total_eur"].sum()     = 325.3
#   max eur_per_item (Miso Ramen unit price)                   = 11.5
#   groupby zone total_eur .sum() = {'Altstadt': 376.2,
#       'Hafen': 325.3, 'Nord': 345.9, 'Sued': 395.9}
#   groupby zone total_eur .mean() = {'Altstadt': 18.81,
#       'Hafen': 17.12, 'Nord': 15.72, 'Sued': 20.84}  -> idxmax = "Sued"
#   trace: orders[orders["items"]==3].shape = (27, 9)
# --- from notebooks/nb_09_lab_pitch.py ---
# ledger (all values computed FROM notebooks/public/orders.csv, cross-checked
# against helpers/make_orders_csv.py; NOTE: (total_eur > 25).sum() is 13; no order
# sits between 23.4 and 26.7, so > 25 and >= 26 agree):
#   daily = orders.groupby("day")["total_eur"].sum()
#       daily.idxmax()                                = 3   (peak day, 146.8 €)
#       daily.idxmin()                                = 6   (trough day, 49.2 €)
#       len(daily)                                    = 14  (two weeks of days)
#   orders.groupby("zone")["total_eur"].sum().round(2).to_dict()
#       = {'Altstadt': 376.2, 'Hafen': 325.3, 'Nord': 345.9, 'Sued': 395.9}
#   (orders["total_eur"] > 25).sum()                  = 13  (the tail)
#   (orders["total_eur"] > 20).sum()                  = 35  (nearly half, NOT a tail)
#   orders["delivery_min"].max()                      = 58
#   corr(delivery_min, total_eur)                     = -0.03  (no relationship)
#   week1 = orders[orders["day"] <= 7]["total_eur"].sum()  = 731.1
#   week2 = orders[orders["day"] >= 8]["total_eur"].sum()  = 712.2
#       (week2 - week1) / week1 * 100                 = -2.59  (a small dip)
#   orders["total_eur"].sum()                         = 1443.3
#   groupby zone total .idxmax() (highest TOTAL)      = "Sued"
#   len(orders)                                       = 80
