# TODO: Fix the bug in the following function.
def sum_even_numbers(numbers):
    total = 0
    try:
        for num in numbers:
            if num % 2 == 0:  # Fixed: Changed '=' to '=='
                total += num  # Fixed: Changed '+' to '+='
    except TypeError:
        print("Error: Input must be a list of numbers")
        return None
    return total

# Test case
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Should print: 12

# Additional test cases
print(sum_even_numbers([]))  # Should print: 0
print(sum_even_numbers([1, 3, 5]))  # Should print: 0
print(sum_even_numbers(["a", "b", "c"]))  # Should print an error message and return None