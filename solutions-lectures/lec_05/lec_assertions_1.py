# Implement a function that takes a list of integers and returns the sum of the numbers.
# 1. Use assertions to check if the input is a list
# 2. Use assertions to check if the list contains only integers.
# 3. If the list contains only integers, return the sum of the numbers

# Your code here
def sum_of_numbers(numbers):
    # 1. Assert input is a list
    assert isinstance(numbers, list), "Input must be a list"
    # 2. Assert the list contains only integers
    for x in numbers:
        assert isinstance(x, int), "All elements must be integers"
    # 3. Return the sum
    return sum(numbers)


# Test cases
print(sum_of_numbers([1, 2, 3, 4, 5]))  # Should print: 15
print(sum_of_numbers([1, 2.0, 3, 4, 5]))  # Should print: AssertionError
