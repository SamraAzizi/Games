class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = "white"

    def create_board(self):
        board = []
        for i in range(8):
            row = [None] * 8
            board.append(row)
        # Set up initial pieces
        for i in range(8):
            board[1][i] = "wp"
            board[6][i] = "bp"
        board[0] = ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
        board[7] = ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"]
        return board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(piece) if piece else "--" for piece in row))

    def move_piece(self, start_pos, end_pos):
        x1, y1 = start_pos
        x2, y2 = end_pos
        piece = self.board[x1][y1]
        if piece is None:
            print("No piece at starting position.")
            return False
        if piece.startswith("w") and self.current_player != "white":
            print("It's black's turn.")
            return False
        if piece.startswith("b") and self.current_player != "black":
            print("It's white's turn.")
            return False
        # Implement actual movement and rules here
        self.board[x2][y2] = piece
        self.board[x1][y1] = None
        self.current_player = "black" if self.current_player == "white" else "white"
        return True


def main():
    game = ChessGame()
    while True:
        game.print_board()
        start_pos = input("Enter starting position (e.g., 'a2'): ")
        end_pos = input("Enter ending position (e.g., 'a4'): ")
        start_col, start_row = ord(start_pos[0]) - ord('a'), int(start_pos[1]) - 1
        end_col, end_row = ord(end_pos[0]) - ord('a'), int(end_pos[1]) - 1
        if game.move_piece((start_row, start_col), (end_row, end_col)):
            print(f"Moved {start_pos} to {end_pos}")
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()
