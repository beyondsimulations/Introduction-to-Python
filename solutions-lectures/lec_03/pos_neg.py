def check_number(number):
    """
    Come up with a function that checks whether a number is positive or negative.
    It returns "positive" for positive numbers and "negative" for negative numbers.
    If the number is zero, it returns None.
    """
    if number > 0:
        return "positive"

    if number < 0:
        return "negative"

print(check_number(1))
print(check_number(-10))
print(check_number(0))
