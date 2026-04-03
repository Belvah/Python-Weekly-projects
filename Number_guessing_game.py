import random
import os

LEADERBOARD_FILE = "leaderboard.txt"


def load_leaderboard():
    scores = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    scores.append((parts[0], parts[1], int(parts[2])))
    return scores


def save_score(username, difficulty, attempts):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{username},{difficulty},{attempts}\n")


def show_leaderboard():
    scores = load_leaderboard()
    if not scores:
        print("\nOoops!No scores yet. Be the first!\n")
        return
    scores.sort(key=lambda x: x[2])
    print("\n===== LEADERBOARD =====")
    print(f"{'Rank':<6}{'Name':<15}{'Difficulty':<12}{'Attempts':<10}")
    print("-" * 43)
    for i, (name, diff, attempts) in enumerate(scores[:10], 1):
        print(f"{i:<6}{name:<15}{diff:<12}{attempts:<10}")
    print("=" * 43 + "\n")


def get_hint(secret):
    hints = []
    if secret % 2 == 0:
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")
    for d in [3, 5, 7]:
        if secret % d == 0:
            hints.append(f"The number is divisible by {d}.")
            break
    return " ".join(hints)


# Ask for username
username = input("Enter your name: ").strip() or "Player"

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Choose difficulty level
print("Choose difficulty:")
print("  1. Easy   (10 tries)")
print("  2. Medium  (7 tries)")
print("  3. Hard    (5 tries)")

while True:
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        max_guesses = 10
        difficulty = "Easy"
        break
    elif choice == "2":
        max_guesses = 7
        difficulty = "Medium"
        break
    elif choice == "3":
        max_guesses = 5
        difficulty = "Hard"
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print(f"\nDifficulty: {difficulty}")
print(f"I'm thinking of a number between 1 and 100.")
print(f"You have {max_guesses} guesses. Best of luck!\n")

for attempt in range(1, max_guesses + 1):
    remaining = max_guesses - attempt
    guess = input(f"Guess #{attempt}: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < 1 or guess > 100:
        print("That's out of range! Pick a number between 1 and 100.")
        continue

    if guess == secret_number:
        print(f"\nCorrect! You got it in {attempt} guess(es)!")
        save_score(username, difficulty, attempt)
        break
    elif guess < secret_number:
        print(f"Too Low! ({remaining} guess{'es' if remaining != 1 else ''} left)")
    else:
        print(f"Too High! ({remaining} guess{'es' if remaining != 1 else ''} left)")

    # Give a hint after 3 wrong tries
    if attempt == 3:
        print(f"Hint: {get_hint(secret_number)}")
else:
    print(f"\nOut of guesses! The number was {secret_number}.")

# Show leaderboard option
view = input("\nView leaderboard? (y/n): ").strip().lower()
if view == "y":
    show_leaderboard()

