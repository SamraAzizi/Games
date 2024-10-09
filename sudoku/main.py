
def fint_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None
def solve_sudoku(puzzle):
    
    #1 choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        

