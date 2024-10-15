# TODO: Implement a random number guessing game.
# The game should work as follows:
# - The computer selects a random number between 1 and 10
# - The user has to guess the number and has three guesses
# - The computer tells the user whether their guess is too high, too low, or correct
# - The computer should also print how many guesses the user made before guessing the number correctly
# - It should also ask the user if they want to play again
# Your code here

#| eval: false
import random

def play_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    guesses = 0
    max_guesses = 3

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 10. You have {max_guesses} guesses.")

    while guesses < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
                return True

            if guesses < max_guesses:
                print(f"You have {max_guesses - guesses} {'guess' if max_guesses - guesses == 1 else 'guesses'} left.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"Sorry, you've run out of guesses. The number was {secret_number}.")
    return False

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

main()