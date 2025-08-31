# TODO: Fix the bug in the following function.
def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total + num
    return total

# Test case
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Should print: 12, but it's not working correctly

# Bonus challenge: Add error handling to make this function more robust