# e) TODO: Write a recursive function (a function that calls itself) to calculate the sum of digits of a positive integer.
# E.g. 1234 -> 1 + 2 + 3 + 4 = 10
# Hint: You can use a for loop to iterate over the characters in a string and convert them to integers.
# Your code here

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))  # Should output 15
