# Start with the following values
price = 100
discount_percent = 15
tax_rate = 0.08

# Your task:
# 1. Apply the discount to the price (price reduced by discount_percent)
discounted_price = price * (1 - discount_percent/100)

# 2. Add tax to the discounted price
price_with_tax = discounted_price * (1 + tax_rate)

# 3. Round the final price to 2 decimal places
final_price = round(price_with_tax, 2)

print(f'The final price is {final_price}.')
