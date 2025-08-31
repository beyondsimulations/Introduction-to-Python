# Create a receipt for a coffee shop purchase
# Use the following information:
item1 = "Cappuccino"
price1 = 3.50
item2 = "Blueberry Muffin"
price2 = 2.25
item3 = "Bottled Water"
price3 = 1.50

# a) Calculate the subtotal
subtotal = price1 + price2 + price3

# b) Calculate the tax
tax_rate = 0.08
tax = subtotal * tax_rate

# c) Calculate the total
total = subtotal + tax

# d) Print the receipt

print("===== Coffee Shop Receipt =====")
print(f"{item1:<20}${price1:.2f}")
print(f"{item2:<20}${price2:.2f}")
print(f"{item3:<20}${price3:.2f}")
print("---------------------------")
print(f"{'Subtotal':<20}${subtotal:.2f}")
print(f"{'Tax (8%)':<20}${tax:.2f}")
print("---------------------------")
print(f"{'Total':<20}${total:.2f}")
print("========= Thank You! =========")
