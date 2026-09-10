# Tic-Tac-Toe

A desktop Tic-Tac-Toe game built using **Python** and the **Tkinter GUI library**, where the player competes against a computer opponent.

This project was created as a personal project while following the **Boot.dev** curriculum. After completing guided Python projects, I wanted to apply what I had learned by independently building a graphical application from scratch.

## Features

* Single-player Tic-Tac-Toe against a computer opponent
* Player uses **X** and the computer uses **O**
* Interactive 3×3 game board built with Tkinter
* Computer selects an available square automatically
* Prevents the player from selecting an occupied square
* Automatically detects winning combinations
* Detects when the game ends in a draw
* Game Over screen displaying the result
* Option to play again after a game finishes
* Option to quit the application

## Technologies Used

* **Python**
* **Tkinter**
* **Git**
* **Linux CLI**

## What I Learned

Building this project helped me practise and develop my understanding of:

* Creating desktop graphical user interfaces with Tkinter
* Event-driven programming
* Handling button click events
* Managing application and game state
* Working with nested lists to represent a game board
* Implementing game logic and win detection
* Using Python functions to organise program behaviour
* Working with multiple Tkinter windows using `Toplevel`
* Generating random computer moves
* Debugging Python applications
* Using Git for version control

## How the Game Works

The game starts from a main menu where the user can either start a new game or quit the application.

Once the game begins:

1. The player selects a square on the 3×3 board.
2. The player's move is represented by **X**.
3. The computer then automatically selects an available square and places an **O**.
4. After each move, the program checks whether either player has won.
5. A player wins by getting three symbols in:

   * A row
   * A column
   * The main diagonal
   * The opposite diagonal
6. If all nine squares are occupied without a winner, the game ends in a draw.
7. The Game Over window allows the user to either **Play Again** or **Quit**.

## How to Run

### Prerequisites

Make sure **Python 3** is installed on your computer.

Check your Python version using:

```bash
python3 --version
```

Tkinter is included with many Python installations. On some Linux distributions, it may need to be installed separately.

For Ubuntu/Debian:

```bash
sudo apt install python3-tk
```

### Clone the Repository

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd tic-tac-toe
```

Run the application:

```bash
python3 main.py
```

## Project Structure

```text
tic-tac-toe/
├── main.py
└── README.md
```

The application is currently contained within a single Python file. `main.py` contains the Tkinter interface, game logic, computer opponent, win detection, and game restart functionality.

## Game Logic

The game board is represented internally using a 3×3 nested list. Each position stores either:

* `"X"` for the player
* `"O"` for the computer
* An empty string for an available square

After each move, the program checks all rows, columns, and diagonals to determine whether a player has won.

The computer opponent currently chooses its moves randomly from the available squares.

## Future Improvements

Some improvements I would like to explore include:

* Implementing a smarter computer opponent
* Adding multiple AI difficulty levels
* Using the **Minimax algorithm** for an unbeatable AI
* Adding score tracking across multiple games
* Allowing players to choose X or O
* Adding a two-player mode
* Improving the graphical interface and styling
* Adding player name customisation

## About the Project

This was an independent personal project created as part of my continued learning through **Boot.dev**.

My previous Boot.dev projects provided guided experience with Python, and I created this project independently to apply those skills to a new problem. The project gave me experience designing program logic from scratch, building a GUI with Tkinter, managing game state, and implementing an automated computer opponent.
