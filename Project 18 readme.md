# Rock, Paper, Scissors Game 🎮

A simple Python implementation of the classic "Rock, Paper, Scissors" game. Challenge the computer and see if you can outsmart it!

## How It Works

The game randomly selects one of the three options (`Rock`, `Paper`, or `Scissors`) for the computer. The player then inputs their choice, and the game determines the winner based on the standard rules of "Rock, Paper, Scissors":

- **Rock** beats Scissors (smashes them).
- **Scissors** beats Paper (cuts it).
- **Paper** beats Rock (covers it).

If both the player and the computer select the same option, the game ends in a tie.

## Features

- **Interactive Gameplay**: The player enters their choice, and the game provides real-time feedback.
- **Randomized Computer Choices**: Ensures fair play by randomly selecting the computer's move.

## Getting Started

### Prerequisites
- Python 3.x installed on your computer.

### Running the Game

1. Copy the code below into a Python file (e.g., `rock_paper_scissors.py`):
    ```python
    from random import randint

    t = ["Rock", "Paper", "Scissors"]

    computer = t[randint(0, 2)]

    player = False

    while player == False:
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cuts", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose!", computer, "smashes", player)
            else:
                print("You win!", player, "cuts", computer)
        else:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")

        # Reset the player variable for a new round
        player = False
        computer = t[randint(0, 2)]
    ```

2. Run the script:
    ```bash
    python rock_paper_scissors.py
    ```

3. Play the game by entering `Rock`, `Paper`, or `Scissors` when prompted.

## Example Gameplay

```plaintext
Rock, Paper, Scissors? Rock
You win! Rock smashes Scissors
Rock, Paper, Scissors? Paper
You lose! Scissors cuts Paper
Rock, Paper, Scissors? Scissors
Tie!
```

## Improvements to Explore
- Add more rounds and keep score.
- Implement error handling for invalid inputs.
- Enhance gameplay with graphical interfaces or animations.
- Introduce additional choices (e.g., "Lizard" and "Spock" from the extended version of the game).

## License

This project is licensed under the MIT License. Feel free to use and modify it as you like!

---

Enjoy the game! 😊
