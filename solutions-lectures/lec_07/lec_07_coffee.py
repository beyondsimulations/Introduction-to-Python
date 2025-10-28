# Daily sales for 3 products over 4 days (Monday-Thursday)

import numpy as np

# Create 10% discount using broadcasting
friday_discount = 0.9  # 10% discount means multiply by 0.9
prices = np.array(
    [[3], [2], [5]]
)  # Prices for coffee, pastries, sandwiches (column vector)
friday_prices = prices * friday_discount
print("Friday discounted prices:\n", friday_prices)
