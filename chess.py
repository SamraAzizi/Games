import tkinter as tk

class ChessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.geometry("400x400")
        
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.draw_board()
        
        self.selected_piece = None

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                square = tk.Canvas(self, width=50, height=50, bg=color, borderwidth=0, highlightthickness=0)
                square.grid(row=row, column=col)
                square.bind("<Button-1>", lambda event, r=row, c=col: self.on_square_click(r, c))

    def on_square_click(self, row, col):
        piece = self.board[row][col]
        if piece != ' ':
            if self.selected_piece:
                self.move_piece(self.selected_piece, (row, col))
                self.selected_piece = None
        else:
            if self.selected_piece:
                self.move_piece(self.selected_piece, (row, col))
                self.selected_piece = None
            else:
                print("No piece selected.")
        
    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]
        if piece == ' ':
            print("No piece to move.")
            return
        self.board[start_row][start_col] = ' '
        self.board[end_row][end_col] = piece
        print(f"Moved {piece} from ({start_row}, {start_col}) to ({end_row}, {end_col})")
        self.draw_pieces()

    def draw_pieces(self):
        for widget in self.winfo_children():
            widget.destroy()
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                square = tk.Canvas(self, width=50, height=50, bg=color, borderwidth=0, highlightthickness=0)
                square.grid(row=row, column=col)
                piece = self.board[row][col]
                if piece != ' ':
                    img = tk.PhotoImage(file=f"{piece}.png")
                    square.create_image(25, 25, image=img)
                    square.image = img
                square.bind("<Button-1>", lambda event, r=row, c=col: self.on_square_click(r, c))

if __name__ == "__main__":
    game = ChessGame()
    # Initial board setup (for testing)
    game.board[0][0] = 'wr'
    game.board[0][1] = 'wn'
    game.board[0][2] = 'wb'
    game.board[0][3] = 'wq'
    game.board[0][4] = 'wk'
    game.board[0][5] = 'wb'
    game.board[0][6] = 'wn'
    game.board[0][7] = 'wr'
    for i in range(8):
        game.board[1][i] = 'wp'
        game.board[6][i] = 'bp'
    game.board[7][0] = 'br'
    game.board[7][1] = 'bn'
    game.board[7][2] = 'bb'
    game.board[7][3] = 'bq'
    game.board[7][4] = 'bk'
    game.board[7][5] = 'bb'
    game.board[7][6] = 'bn'
    game.board[7][7] = 'br'
    game.draw_pieces()
    game.mainloop()
