"""
Solution for Anagram Scramble Game
Tutorial 5 - Handling Errors
"""

import random


def load_words(filename):
    """
    Load words from a file (one word per line).

    Returns a list of words (converted to lowercase and stripped).
    Handle FileNotFoundError - print error message and return empty list.
    """
    try:
        with open(filename, "r") as file:
            words = [line.strip().lower() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


def scramble_word(word):
    """
    Scramble the letters of a word randomly.

    Convert to list, use random.shuffle(), convert back to string.
    Make sure the scrambled word is different from the original.
    """
    scrambled = list(word)

    # Keep shuffling until we get a different word
    # (important for short words that might shuffle to same order)
    while True:
        random.shuffle(scrambled)
        scrambled_word = "".join(scrambled)
        if scrambled_word != word:
            break

    return scrambled_word


def validate_guess(guess, original_word):
    """
    Validate that a guess is acceptable.

    - Raise ValueError if guess is empty or contains only spaces
    - Raise ValueError if guess contains numbers or special characters
    - Raise ValueError if guess length doesn't match original word
    - Return True if guess matches original word (case-insensitive), False otherwise
    """
    # Check for empty input
    if not guess or guess.strip() == "":
        raise ValueError("Input cannot be empty")

    # Check if input contains only letters
    if not guess.isalpha():
        raise ValueError("Input must contain only letters")

    # Check if length matches
    if len(guess) != len(original_word):
        raise ValueError(
            f"Word must be {len(original_word)} letters long, you entered {len(guess)}"
        )

    # Check if guess is correct (case-insensitive)
    return guess.lower() == original_word.lower()


def play_anagram_game():
    """
    Main game function that orchestrates the entire game.
    """
    print("=" * 50)
    print("Welcome to Anagram Scramble!")
    print("=" * 50)
    print()

    # Load words from file
    words = load_words("solutions-tutorials/tut_05/words.txt")

    # Check if words were loaded successfully
    if not words:
        print("Cannot start game without word list.")
        return

    print(f"Loaded {len(words)} words!")
    print()

    # Randomly select a word
    original_word = random.choice(words)

    # Scramble the word
    scrambled = scramble_word(original_word)

    # Game settings
    max_tries = 5
    tries_left = max_tries

    print(f"Unscramble this word: {scrambled.upper()}")
    print(f"The word has {len(original_word)} letters.")
    print(f"You have {max_tries} tries. Type 'quit' to give up.")
    print()

    # Main game loop
    while tries_left > 0:
        print(f"Tries left: {tries_left}")
        guess = input("Your guess: ").strip()
        print()

        # Handle quit command
        if guess.lower() == "quit":
            print("Thanks for playing!")
            print(f"The word was: {original_word.upper()}")
            return

        # Validate and check the guess
        try:
            is_correct = validate_guess(guess, original_word)

            if is_correct:
                print("Congratulations! You got it right!")
                print(f"The word was: {original_word.upper()}")
                print(f"You solved it with {tries_left} tries remaining!")
                return
            else:
                tries_left -= 1
                if tries_left > 0:
                    print("❌ Not quite! Try again.")
                    print()

        except ValueError as e:
            print(f"Invalid input: {e}")
            print("This doesn't count as a try. Please enter a valid guess.")
            print()

    # Out of tries
    print("Game Over! You're out of tries.")
    print(f"The word was: {original_word.upper()}")


# Test the game
if __name__ == "__main__":
    play_anagram_game()
