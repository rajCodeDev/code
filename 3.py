import random

def start_game():
    print("Welcome to Takashi Castle!")
    print("Navigate through the obstacles to reach the finish line.")

    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's begin.")

    obstacle_count = 5
    obstacles_passed = 0

    while obstacles_passed < obstacle_count:
        input("Press Enter to face the next obstacle...")
        result = face_obstacle()
        if result:
            obstacles_passed += 1
            print("You passed the obstacle!")
        else:
            print("Oops! Game Over.")
            break

    if obstacles_passed == obstacle_count:
        print("Congratulations! You have reached the finish line!")
    print("Game over.")

def face_obstacle():
    obstacles = ["Rolling Barrels", "Muddy Pits", "Swinging Pendulums", "Jumping Stones", "Wall Climb"]
    obstacle = random.choice(obstacles)

    print(f"You are facing: {obstacle}")

    # Simulate the outcome of facing the obstacle
    success = random.choice([True, False])
    return success

# Start the game
start_game()
