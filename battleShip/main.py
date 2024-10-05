
#legends
# x for placing ship and hit battleship
# ' ' for available space
#'_' for missed shot

from random import randint



hiden_board = [[' '] * 8 for x in range[8]]
guess_board = [[' '] * 8 for x in range[8]]

letters_to_numbers = {'a' :0, 'b' : 1, 'c' : 2, 'd' :3, 'e' : 4, 'f':5, 'g' : 6, 'h' : 7}

def print_board(board):

    print(' A B C D E F G H')
    print(' ==================')

    row_num = 1
    for row in board:
        print("%d|%s|" %(row_num,"|".join(row)))
        row_num += 1
    

def create_ships(board):
    for ship in range(5):
        ship_row, ship_colunm = randint(0,7), randint(0,7)
        while board[ship_row][ship_colunm] == 'X':
            ship_row, ship_colunm = randint(0,7), randint(0,7)
        board[ship_row][ship_colunm] = 'X'

def get_ship_location():
    row = input('Please enter a ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('please enter a ship_row 1-8')
    column = input('please enter a ship column A-H').upper()
    while column not in 'ABCDEFGH':
        print('please enter a valid column')
        column = input('please enter a ship column A-H').upper()
        



def count_hit_ships():
    pass

create_ships()
turns = 10
##while turns > 0 
