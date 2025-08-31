# Generate a random integer between 1 and 10 using randint().
# Ask the user to guess the number with input().
# Print whether the guess was correct.
# Give a hint if the guess was too high or too low.
# Repeat the game until the user guesses the number.

import random

def guess_number():
    secret_number = random.randint(1, 10)
    while True:
        guess = int(input("Guess the number between 1 and 10: "))
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guess_number()