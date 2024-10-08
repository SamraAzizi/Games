# BattleShip Game
=====================

## Introduction
This is a simple implementation of the classic Battleship game in Python. The game is played on an 8x8 grid, where the player has to guess the locations of 5 hidden battleships.

## Gameplay
* The game starts with a welcome message and an empty 8x8 grid.
* The player is prompted to enter a row and column to guess the location of a battleship.
* If the guessed location is a hit, the game marks it with 'X' on the grid. If it's a miss, it's marked with '-'.
* The player has 10 turns to guess all the battleship locations.
* After each turn, the game displays the updated grid and the number of turns remaining.
* If the player guesses all the battleship locations before running out of turns, they win the game. Otherwise, the game ends with a "Game Over" message.

## Code Structure
### Functions
* `print_board(board)`: prints the current state of the game board.
* `create_ships(board)`: randomly places 5 battleships on the hidden board.
* `get_ship_location()`: prompts the user to enter a row and column to guess a battleship location.
* `count_hit_ships(board)`: counts the number of hit battleships on the board.

### Variables
* `hidden_board`: a 2D list representing the hidden board with the battleship locations.
* `guess_board`: a 2D list representing the player's guess board.
* `letters_to_numbers`: a dictionary mapping column letters (A-H) to numbers (0-7).
* `turns`: the number of turns remaining for the player.

## Running the Game
To play the game, simply run the Python script. The game will start automatically, and you can follow the prompts to play.