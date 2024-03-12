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
