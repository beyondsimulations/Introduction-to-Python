# Number guessing game - Task b)

# Initial player names
player1 = input("Enter the name of the first player: ")
player2 = input("Enter the name of the second player: ")

play_again = "yes"
while play_again.lower() == "yes":
    # Set roles for this round
    game_master = player1
    player = player2

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

    # Ask if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    
    if play_again.lower() == "yes":
        # Switch roles
        temporary_player = player1
        player1 = player2
        player2 = temporary_player
        print(f"\nNew game! {player1} is now the game master, and {player2} is the guesser.")

print("Thanks for playing!")