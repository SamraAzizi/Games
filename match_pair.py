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

    def reveal(self, row, col):
        if (row, col) not in self.revealed:
            symbol, color = self.board[row][col]
            self.buttons[row][col]['text'] = symbol
            self.buttons[row][col]['bg'] = color
            self.revealed.add((row, col))
            if self.first_click is None:
                self.first_click = (row, col)
            else:
                self.master.after(1000, self.check_match)

    def check_match(self):
        row1, col1 = self.first_click
        row2, col2 = next(iter(self.revealed - {(row1, col1)}))
        if self.board[row1][col1][0] == self.board[row2][col2][0]:
            self.buttons[row1][col1]['state'] = 'disabled'
            self.buttons[row2][col2]['state'] = 'disabled'
            self.revealed.clear()
            if all(all(cell['state'] == 'disabled' for cell in row) for row in self.buttons):
                tk.messagebox.showinfo("Game Over", "Congratulations! You won!")
        else:
            self.buttons[row1][col1]['text'] = ''
            self.buttons[row1][col1]['bg'] = 'SystemButtonFace'
            self.buttons[row2][col2]['text'] = ''
            self.buttons[row2][col2]['bg'] = 'SystemButtonFace'
            self.revealed.clear()
        self.first_click = None

def main():
    root = tk.Tk()
    root.title("Memory Game")
    size = 4  # Change the size of the board as desired
    game = MemoryGame(root, size=size)
    root.mainloop()

if __name__ == "__main__":
    main()


