def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1

    average = total / count
    return average


# Test cases
test_lists = [[1, 2, 3, 4, 5], [10, 20, 30], []]

for i, test_list in enumerate(test_lists):
    print(f"Test case {i + 1}:")
    result = calculate_average(test_list)
    print(f"Average: {result}\n")
