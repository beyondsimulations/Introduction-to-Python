# TODO: Write the code for a small game
# The game should work as follows:
# - The computer selects a word from a list of words
# - The computer scrambles the word and shows it to the user
# - The user has to guess the word and has three guesses
# - The user gets feedback on whether their guess is correct or not
# - The computer tells the user how many guesses they used

# List of words to choose from for the game
words = ["python", "programming", "computer", "algorithm", "database"]

# Hint: Use the random.choice() function to select a word from the list and try to come up with the rest of the code yourself!

import random

# List of words to choose from for the game
words = ["python", "programming", "computer", "algorithm", "database"]

def scramble_word(word):
    chars = list(word)
    random.shuffle(chars)
    return ''.join(chars)

# Select a random word
chosen_word = random.choice(words)
scrambled_word = scramble_word(chosen_word)

print("Welcome to the Word Guessing Game!")
print(f"The scrambled word is: {scrambled_word}")

guesses = 0
max_guesses = 3
guess = ""

while guesses < max_guesses:
    guess = input(f"Guess {guesses + 1}/{max_guesses}: ").lower()
    guesses += 1

    if guess == chosen_word:
        print(f"Congratulations! You guessed the word correctly in {guesses} {'guess' if guesses == 1 else 'guesses'}!")
        break
    else:
        print("Sorry, that's not correct.")

if guesses == max_guesses and guess != chosen_word:
    print(f"Sorry, you've used all your guesses. The correct word was '{chosen_word}'.")

print(f"You used {guesses} {'guess' if guesses == 1 else 'guesses'}.")
