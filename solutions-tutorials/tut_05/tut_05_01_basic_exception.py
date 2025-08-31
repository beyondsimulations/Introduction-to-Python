# TODO: Write a function that takes three numbers as input. It adds the first two numbers 
# and then divides the result by the third number. 
# Use a try-except block to handle the ZeroDivisionError.
def safe_divide(add_1, add_2, div):
    try:
        result = (add_1 + add_2) / div
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"

# Test cases
print(safe_divide(5, 5, 2))  # Should print: 5.0
print(safe_divide(10, 0, 0))  # Should print: "Error: Division by zero"