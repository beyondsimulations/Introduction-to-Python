# a) Temperature Converter
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is {celsius:.2f}°C")

# b) Circle Area Calculator
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f}")

# c) Simple Interest Calculator
principal = 1946
rate = 0.05
years = 3
interest = principal * rate * years
print(f"The interest after {years} years is EUR {interest:.2f}")

# d) Time Duration Calculator
total_seconds = 298471
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds is {minutes} minutes and {seconds} seconds")

# e) Compound Growth
initial_amount = 23842
growth_rate = 0.08
years = 3
final_amount = initial_amount * (1 + growth_rate) ** years
print(f"The final amount after {years} years is EUR {final_amount:.2f}")