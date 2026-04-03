# Number Guessing Game

A command-line guessing game where the computer picks a random number between 1 and 100 and you try to guess it.

## How to Play

1. Run the game:
   ```bash
   python3 Number_guessing_game.py
   ```
2. Enter your name.
3. Choose a difficulty level:
   - **Easy** — 10 guesses
   - **Medium** — 7 guesses
   - **Hard** — 5 guesses
4. Type your guesses. The game tells you **"Too High"** or **"Too Low"** after each wrong guess.
5. After 3 wrong guesses, you get a **hint** (even/odd, divisible by 3/5/7).
6. Win by guessing correctly, or lose when you run out of attempts.

## Features

- Random number generation using `random.randint()`
- Three difficulty levels with different guess limits
- Remaining guess counter after each attempt
- Hints after 3 wrong guesses
- High score saving to `leaderboard.txt`

## Files

| File | Description |
|------|-------------|
| `Number_guessing_game.py` | Main game (menu-based with functions) |
| `leaderboard.txt` | Auto-generated file storing high scores |

## Requirements

- Python 3.14.3.

## Contributing

1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request on GitHub.

### Ideas for Contributions

- Add a timer to track how fast players guess the number
- Add more hint types (e.g., range narrowing, prime/not prime)
- Add multiplayer support (take turns guessing)
- Improve leaderboard with date/time stamps

## Contact

Belvah Shanyisa
belvah@gmail.com
GitHub: [Belvah](https://github.com/Belvah)


