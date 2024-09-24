# Number guessing game - Task c)

player1 = input("Enter the name of the first player: ")
player2 = input("Enter the name of the second player: ")

play_again = "yes"
while play_again.lower() == "yes":
    game_master = player1
    player = player2

    # Choose difficulty level
    print("\nDifficulty levels:")
    print("1. Easy (1-10, 5 guesses)")
    print("2. Medium (1-20, 10 guesses)")
    print("3. Hard (1-30, 15 guesses)")
    difficulty = input(f"{game_master}, choose a difficulty level (1/2/3): ")

    if difficulty == "1":
        max_number = 10
        max_guesses = 5
    elif difficulty == "2":
        max_number = 20
        max_guesses = 10
    else:
        max_number = 30
        max_guesses = 15

    while True:
        secret_number = int(input(f"{game_master}, enter the secret number between 1 and {max_number}: "))
        if secret_number < 1 or secret_number > max_number:
            print("Please enter a valid number.")
        else:
            break
            
    print("\n" * 25)

    guesses = 0
    correct = False

    while not correct and guesses < max_guesses:
        guess = int(input(f"{player}, guess the number between 1 and {max_number} (Guesses left: {max_guesses - guesses}): "))
        guesses += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            correct = True

    if correct:
        print(f"Congratulations, {player}! You guessed the number in {guesses} guesses.")
    else:
        print(f"Sorry, {player}. You've run out of guesses. The secret number was {secret_number}.")

    play_again = input("Do you want to play again? (yes/no): ")
    
    if play_again.lower() == "yes":
        temporary_player = player1
        player1 = player2
        player2 = temporary_player
        print(f"\nNew game! {player1} is now the game master, and {player2} is the guesser.")

print("Thanks for playing!")