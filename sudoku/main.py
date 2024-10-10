def find_next_empty(puzzle):
    # Finds the next empty spot in the puzzle (denoted by -1)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c  # row, col
    return None, None  # if no empty spaces left

def is_valid(puzzle, guess, row, col):
    # Check if the guess is valid in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check if the guess is valid in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check if the guess is valid in the 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If it passes all checks, it's a valid guess
    return True

def solve_sudoku(puzzle):
    # Find the next empty spot in the puzzle
    row, col = find_next_empty(puzzle)

    if row is None:
        return True  # puzzle is solved

    # If there is an empty spot, we try guesses from 1 to 9
    for guess in range(1, 10):
        # Check if it's a valid guess
        if is_valid(puzzle, guess, row, col):
            # Place the guess on the puzzle
            puzzle[row][col] = guess

            # Recursively call the solver
            if solve_sudoku(puzzle):
                return True

        # If the guess doesn't lead to a solution, reset the guess
        puzzle[row][col] = -1

    return False  # If no valid guesses work, backtrack

# Example usage
if __name__ == "__main__":
    sudoku_puzzle = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]

    if solve_sudoku(sudoku_puzzle):
        for row in sudoku_puzzle:
            print(row)
    else:
        print("No solution exists")
