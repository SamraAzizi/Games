import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, num_mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0] * cols for _ in range(rows)]
        self.mines = set()
        self.buttons = [[None] * cols for _ in range(rows)]
        self.game_over = False

        self.init_board()
        self.place_mines()
        self.calculate_numbers()

        self.create_widgets()

    def init_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button = tk.Button(self.master, width=2, height=1, font=('Helvetica', 14), command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
