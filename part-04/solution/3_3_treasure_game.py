# c) TODO: Add a feature to allow for multiple obstacles on the grid.
# - The game master should be able to set the number of obstacles in the grid and their positions.
# - Print the position of the obstacles and the treasure after the game has been finished.
# - Try to make the printout as nice as possible.

# Game master setup
print("Welcome, Game Master! Let's set up the game.")
grid_size = int(input("Enter the size of the grid (eg. 3 = 3x3): "))
treasure_x = int(input("Enter the treasure coordinate for x (eg. 3): "))
treasure_y = int(input("Enter the treasure coordinate for y (eg. 3): "))
treasure = (treasure_x, treasure_y)

num_obstacles = int(input("Enter the number of obstacles: "))
obstacles = []
for i in range(num_obstacles):
    obstacle_x = int(input(f"Enter obstacle {i+1} coordinate for x: "))
    obstacle_y = int(input(f"Enter obstacle {i+1} coordinate for y: "))
    obstacles.append((obstacle_x, obstacle_y))

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
        return False
    elif pos in obstacles:
        print("You hit an obstacle. Game over!")
        return False
    else:
        return True

# Main game loop
def play_game():
    print("\nWelcome to the Mini Treasure Hunt Game!")
    print(f"Grid size: {grid_size}x{grid_size}")
    print(f"Treasure location: {treasure}")
    print("Obstacle locations:")
    for i, obstacle in enumerate(obstacles, 1):
        print(f"  Obstacle {i}: {obstacle}")
    print(f"Starting position: (1, 1)")
    
    while True:
        print(f"Current position: ({player_position['x']}, {player_position['y']})")
        move = input("Enter move (up, down, left, right): ").strip().lower()
        move_player(move)
        if not check_position():
            break
    
    print("\nGame Over!")
    print(f"Final position: ({player_position['x']}, {player_position['y']})")
    print(f"Treasure location: {treasure}")
    print("Obstacle locations:")
    for i, obstacle in enumerate(obstacles, 1):
        print(f"  Obstacle {i}: {obstacle}")

# Start the game
play_game()