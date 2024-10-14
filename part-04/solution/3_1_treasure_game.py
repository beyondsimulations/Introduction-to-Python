# a) TODO: Take a look at the code below and the instructions and add the missing code to make the game work.
# - The game should be played on a 3x3 grid.
# - The treasure is located at position (3, 3).
# - There is an obstacle at position (2, 2).
# - The player starts at position (1, 1).
# - The player can move up, down, left, or right.
# - The player cannot move outside the boundaries of the grid.
# - If the player hits the obstacle, the game is over.
# - If the player finds the treasure, the game is won.
# - Continuously prompt the player to enter a move (up, down, left, right).

grid_size = 3 # Size of the grid
treasure = (3,3) # Tuple for the treasure
obstacle = (2,2) # Tuple for the obstacle

# Player's starting position in a dictionary
player_position = {"x": 1, "y": 1}

# Function to move the player
def move_player(direction):
    if direction == "up" and player_position["y"] > 1:
        player_position["y"] -= 1
    elif direction == "down" and player_position["y"] < grid_size:
        player_position["y"] += 1
    elif direction == "left" and player_position["x"] > 1:
        player_position["x"] -= 1
    elif direction == "right" and player_position["x"] < grid_size:
        player_position["x"] += 1
    else:
        print("Invalid move. Try again.")

# Function to check the player's position
def check_position():
    pos = (player_position["x"], player_position["y"])
    if pos == treasure:
        print("You found the treasure and won!")
        return False
    elif pos == obstacle:
        print("You hit an obstacle. Game over!")
        return False
    else:
        return True

# Main game loop
def play_game():
    print("Welcome to the Mini Treasure Hunt Game!")
    while True:
        print(f"Current position: {player_position}")
        move = input("Enter move (up, down, left, right): ").strip().lower()
        move_player(move)
        if check_position() == False:
            break

# Start the game
play_game()
