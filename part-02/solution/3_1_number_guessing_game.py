# Number guessing game implementation - Task a)

# Ask for the names of the game master and the player
game_master = input("Enter the name of the game master: ")
player = input("Enter the name of the player: ")

# Ask the game master for the secret number
while True:
    secret_number = int(input(f"{game_master}, enter the secret number between 1 and 20: "))
    if secret_number < 1 or secret_number > 20:
        print("Please enter a valid number.")
    else:
        break
    
print("\n" * 25)  # Add 25 new lines to hide the secret number

# Initialize variables
guesses = 0
correct = False

# Main game loop
while not correct:
    # Ask the player for a guess
    guess = int(input(f"{player}, guess the number between 1 and 20: "))
    guesses += 1
    
    # Compare the guess to the secret number
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        correct = True

# Print congratulatory message
print(f"Congratulations, {player}! You guessed the number in {guesses} guesses.")