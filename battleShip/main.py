
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
    

def create_ships():
    for ship in range(5):
        ship_row, ship_colunm = randint(0,7), randint(0,7)
        while board[ship_row][ship_colunm] == 'X':
            ship_row, ship_colunm = randint(0,7), randint(0,7)

def get_ship_location():
    pass


def count_hit_ships():
    pass

create_ships()
turns = 10
##while turns > 0 
