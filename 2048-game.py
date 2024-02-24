import tkinter as tk
import random
import numpy as np

# Define colors and fonts
COLORS = {
    'background': "#92877d",
    'empty_cell': "#9e948a",
    'text': "#8f8886",
    'tiles': {
        2: "#eee4da",
        4: "#ede0c8",
        8: "#f2b179",
        16: "#f59563",
        32: "#f67c5f",
        64: "#f65e3b",
        128: "#edcf72",
        256: "#edcc61",
        512: "#edc850",
        1024: "#edc53f",
        2048: "#edc22e",
    }
}
FONT = ("Verdana", 40, "bold")

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('2048')
        self.game_size = 4
        self.cells = []
        self.matrix = np.zeros((self.game_size, self.game_size), dtype=int)
        self.init_ui()
        self.start_game()

    def init_ui(self):
        self.background = tk.Frame(self, bg=COLORS['background'], width=400, height=400)
        self.background.grid()

        for i in range(self.game_size):
            row = []
            for j in range(self.game_size):
                cell_frame = tk.Frame(
                    self.background,
                    bg=COLORS['empty_cell'],
                    width=100,
                    height=100)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.background, bg=COLORS['empty_cell'], fg=COLORS['text'], font=FONT)
                cell_number.grid(row=i, column=j)
                cell_data = {'frame': cell_frame, 'number': cell_number}
                row.append(cell_data)
            self.cells.append(row)

        self.bind("<Key>", self.key_down)

    def start_game(self):
        self.matrix = np.zeros((self.game_size, self.game_size), dtype=int)
        self.add_new_tile()
        self.add_new_tile()
        self.update_ui()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.game_size) for j in range(self.game_size) if self.matrix[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.matrix[i][j] = random.choice([2, 4])

    def compress(self, grid):
        new_grid = np.zeros((self.game_size, self.game_size), dtype=int)
        for i in range(self.game_size):
            position = 0
            for j in range(self.game_size):
                if grid[i][j] != 0:
                    new_grid[i][position] = grid[i][j]
                    position += 1
        return new_grid

    def merge(self, grid):
        for i in range(self.game_size):
            for j in range(self.game_size - 1):
                if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                    grid[i][j] *= 2
                    grid[i][j + 1] = 0
        return grid

    def reverse(self, grid):
        new_grid = []
        for i in range(self.game_size):
            new_grid.append([])
            for j in range(self.game_size):
                new_grid[i].append(grid[i][self.game_size - j - 1])
        return new_grid

    def transpose(self, grid):
        return np.transpose(grid)

    def move_left(self, grid):
        grid = self.compress(grid)
        grid = self.merge(grid)
        grid = self.compress(grid)
        return grid

    def move_right(self, grid):
        grid = self.reverse(grid)
        grid = self.move_left(grid)
        grid = self.reverse(grid)
        return grid

    def move_up(self, grid):
        grid = self.transpose(grid)
        grid = self.move_left(grid)
        grid = self.transpose(grid)
        return grid

    def move_down(self, grid):
        grid = self.transpose(grid)
        grid = self.move_right(grid)
        grid = self.transpose(grid)
        return grid

    def key_down(self, event):
        key = event.keysym
        moved = False

        if key == 'Left':
            self.matrix, moved = self.move_left(self.matrix), True
        elif key == 'Right':
            self.matrix, moved = self.move_right(self.matrix), True
        elif key == 'Up':
            self.matrix, moved = self.move_up(self.matrix), True
        elif key == 'Down':
            self.matrix, moved = self.move_down(self.matrix), True

        if moved:
            self.add_new_tile()
            self.update_ui()
            if self.check_game_over():
                print("Game Over!")

    def update_ui(self):
        for i in range(self.game_size):
            for j in range(self.game_size):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]['number'].config(text="", bg=COLORS['empty_cell'])
                else:
                    self.cells[i][j]['number'].config(text=str(cell_value), bg=COLORS['tiles'][cell_value])

    def check_game_over(self):
        if any(0 in row for row in self.matrix):
            return False
        for i in range(self.game_size):
            for j in range(self.game_size-1):
                if self.matrix[i][j] == self.matrix[i][j+1] or self.matrix[j][i] == self.matrix[j+1][i]:
                    return False
        return True

if __name__ == "__main__":
    game = Game()
    game.mainloop()
