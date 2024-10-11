# Sudoku Game

This is a simple implementation of a Sudoku game in Python. The game allows users to play a game of Sudoku by inputting numbers into a 9x9 grid.

## Gameplay

1. The game starts with a partially filled Sudoku board.
2. The user is prompted to enter a row, column, and number to place on the board.
3. The game checks if the move is valid (i.e., the number does not already exist in the same row, column, or 3x3 box).
4. If the move is valid, the number is placed on the board and the updated board is displayed.
5. If the move is invalid, the user is prompted to try again.
6. The game continues until the user has filled in the entire board correctly.

## Code Structure

The code is organized into several functions:

* `print_board(board)`: prints the current state of the Sudoku board.
* `find_empty(board)`: finds an empty spot on the board and returns its coordinates.
* `valid(board, num, pos)`: checks if a move is valid (i.e., the number does not already exist in the same row, column, or 3x3 box).
* `solve(board)`: solves the Sudoku board using backtracking (not used in the game, but included for completeness).
* `play_game()`: starts the game and handles user input.

