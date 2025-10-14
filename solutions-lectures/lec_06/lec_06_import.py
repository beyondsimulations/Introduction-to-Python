# Import the `math` module.
# Define a function named `calculate_area` that takes the radius `r` as an argument.
# Inside the function, use the `math.pi` constant to get the value of π.
# Calculate the area in the function and return it.

# Your code here
import math


def calculate_area(r: float):
    return math.pi * r**2


print(calculate_area(5))
assert calculate_area(5) == 78.53981633974483
