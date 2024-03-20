# Chess Game README

## Introduction
This Python script implements a basic version of the classic board game Chess. Chess is a two-player strategy game played on an 8x8 grid, where each player controls an army of pieces including pawns, rooks, knights, bishops, a queen, and a king. The objective of the game is to checkmate the opponent's king, putting it in a position where it is threatened with capture and cannot escape.

## Features
- **Board Representation**: The game uses a 2D array to represent the chessboard, with each piece identified by its symbol.
- **Turn-based Gameplay**: Players take turns moving their pieces, with the white player going first.
- **Basic Movement Rules**: The script includes a basic implementation of piece movement rules, allowing pieces to move to empty squares or capture opponent pieces.
- **Prompts for Moves**: Players are prompted to input their moves in algebraic notation (e.g., 'a2' to 'a4').

## How to Play
1. **Game Initialization**: Run the script to start the game. The initial chessboard with pieces in their starting positions will be displayed.
2. **Move Input**: Enter the starting position and the ending position of the piece you want to move when prompted. Follow the algebraic notation format.
3. **Turn Progression**: The game alternates between white and black players, allowing each to make their moves in turn.
4. **Checkmate**: The game continues until one player achieves checkmate, where the opponent's king is threatened and cannot escape capture, or until the players agree to a draw.

## Execution
To play the game, run the script in your Python environment with the command:
```bash
python chess.py
