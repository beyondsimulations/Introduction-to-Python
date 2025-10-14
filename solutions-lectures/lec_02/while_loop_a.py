# Implement a while-loop that prints all even numbers between 0 and 100 excluding both 0 and 100.
number = 0
# Your code here
while True:
    if number > 0 and number < 100:
        if number % 2 == 0:
            print(number)
    if number >= 100:
        break
    number += 1
