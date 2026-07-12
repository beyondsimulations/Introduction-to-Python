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
DISHES = {"Bao Box": 8.40, "Falafel Wrap": 7.60, "Pad Thai": 10.20, "Miso Ramen": 11.90}


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
# revenue total: 1571.6
# mean order: 19.64
# zone totals: {'Altstadt': 408.4, 'Hafen': 354.2, 'Nord': 378.9, 'Sued': 430.1}
# orders per zone: {'Nord': 22, 'Altstadt': 20, 'Hafen': 19, 'Sued': 19}
# best day (revenue): 3
# max delivery: 58
# count total_eur > 20: 43
