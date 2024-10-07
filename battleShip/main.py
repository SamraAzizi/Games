from random import randint

# Legends
# 'X' for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot

hidden_board = [[' '] * 8 for _ in range(8)]
guess_board = [[' '] * 8 for _ in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('  A B C D E F G H')
    print('  ==================')
    row_num = 1
    for row in board:
        print(f"{row_num}|{'|'.join(row)}|")
        row_num += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input('Please enter a ship row (1-8): ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row (1-8): ')
    column = input('Please enter a ship column (A-H): ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column (A-H): ').upper()
    
    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(hidden_board)

turns = 10
print('Welcome to BattleShip!')
print_board(guess_board)

while turns > 0:
    print(f'\nYou have {turns} turns remaining.')
    row, column = get_ship_location()
    
    if guess_board[row][column] == '-':
        print('You have already guessed that location.')
    elif hidden_board[row][column] == 'X':
        print('Congratulations! You have hit a battleship!')
        guess_board[row][column] = 'X'
    else:
        print('Sorry, you missed.')
        guess_board[row][column] = '-'
    
    print_board(guess_board)
    turns -= 1
    
if count_hit_ships(guess_board) == 5:
        print('Congratulations! You have sunk all the battleships!')
        break
    
    if turns == 0:
        print('Game Over!')
        print('Here was the hidden board:')
        print_board(hidden_board)
