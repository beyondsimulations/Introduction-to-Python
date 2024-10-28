# Size of the grid
grid_size = 3

# Create treasure and obstacle
treasure = (3,3)
obstacle = (2,2)

# Player's starting position
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
        return "found"
    elif pos == obstacle:
        print("You hit an obstacle! Game over.")
        return "obstacle"
    else:
        return "next"

# Main game loop
def play_game():
    print("Welcome to the Mini Treasure Hunt Game!")
    while True:
        print(f"Current position: {player_position}")
        move = input("Enter move (up, down, left, right): ").strip().lower()
        move_player(move)
        if check_position() == "found" or check_position() == "obstacle":
            break

# Start the game
play_game()

