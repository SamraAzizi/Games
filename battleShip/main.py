

hiden_board = [[' '] * 8 for x in range[8]]
guess_board = [[' '] * 8 for x in range[8]]

letters_to_numbers = {'a' :0, 'b' : 1, 'c' : 2, 'd' :3, 'e' : 4, 'f':5, 'g' : 6, 'h' : 7}

def print_board(board):

    print(' A B C D E F G H')
    print(' ==================')

    row_num = 1
    for row in board:
        print("%d|%s|" %(row_num))
    

def create_ships():
    pass

def get_ship_location():
    pass


def count_hit_ships():
    pass

create_ships()
turns = 10
##while turns > 0 
