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

    def place_mines(self):
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.mines.add((row, col))

    def calculate_numbers(self):
        for row, col in self.mines:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < self.rows and 0 <= j < self.cols:
                        self.board[i][j] += 1

    def click(self, row, col):
        if self.game_over:
            return

        button = self.buttons[row][col]
        button.grid_forget()

        if (row, col) in self.mines:
            self.game_over = True
            for r, c in self.mines:
                self.buttons[r][c].config(text='*', bg='red')
            return

       