import tkinter as tk
import random

class MemoryGame:
    def __init__(self, master, size=4):
        self.master = master
        self.size = size
        self.symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        self.board = self.initialize_board()
        self.revealed = set()
        self.buttons = [[None] * size for _ in range(size)]
        self.create_board()
        self.first_click = None

    def initialize_board(self):
        num_pairs = self.size * self.size // 2
        pairs = random.sample(self.symbols, num_pairs) * 2
        random.shuffle(pairs)
        random.shuffle(pairs)
        board = [[None] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                board[i][j] = (pairs.pop(), random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple']))
        return board

    def create_board(self):
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.master, text='', width=4, height=2,
                                   command=lambda row=i, col=j: self.reveal(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    