
# Tic Tac Toe:

# Players take turns marking spaces on a 3x3 grid with their respective symbols (X or O).
# The first player to get three of their symbols in a row, column, or diagonal wins.
# If all spaces are filled without a winner, the game ends in a draw.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row = int(input("Player {} - Enter row (1, 2, 3): ".format(players[current_player]))) - 1
        col = int(input("Player {} - Enter column (1, 2, 3): ".format(players[current_player]))) - 1

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print("Player {} wins!".format(players[current_player]))
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2


if __name__ == "__main__":
    tic_tac_toe()
