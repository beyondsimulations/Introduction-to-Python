import random

def number_guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    tries = 3

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {tries} tries to guess it.\n")

    while tries > 0:
        # Get player's guess
        try:
            guess = int(input(f"Enter your guess ({tries} tries left): "))
            
            # Check if guess is in valid range
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10!")
                continue

            # Check if guess is correct
            if guess == secret_number:
                print(f"\nCongratulations! You guessed it! The number was {secret_number}!")
                return
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            tries -= 1

        except ValueError:
            print("Please enter a valid number!")
            continue

    print(f"\nGame Over! The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()