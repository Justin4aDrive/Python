#only works for puzzles that are solvable
from pprint import pprint

#proceeds by next row, then colum to find cell that is empty
def locate_next_unknown(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None #all cells are populated

def is_correct(puzzle, guess, row, col):
    row_sum = puzzle[row]
    if guess in row_sum:
        return False
    col_sum = []
    for i in range(9):
        col_sum.append(puzzle[i][col])
    col_sum = [puzzle[i][col] for i in range (9)]
    if guess in col_sum:
        return False
#index 3x3 square with location
    row_begin = (row // 3) * 3
    col_begin = (col // 3) * 3

    for r in range(row_begin, row_begin + 3):
        for c in range(col_begin, col_begin + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def complete_sudoku(puzzle):
    row, col = locate_next_unknown(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_correct(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if complete_sudoku(puzzle):
                return True
        puzzle[row][col] = -1 #try again
    return False  #unsolvable

if __name__ == '__main__':
    test_board = [
        [-1, 9, -1,   -1, -1, 2,   -1, 7, -1],
        [-1, -1, -1,   -1, -1, 3,   -1, -1, 6],
        [-1, -1, 1,    9, 6, -1,   -1, 8, -1],

        [4, -1, -1,   -1, -1, -1,   -1, 1, -1],
        [-1, -1, -1,   -1, -1, 6,   -1, -1, -1],
        [-1, 3, -1,    7, 5, -1,   -1, -1, 8],

        [-1, -1, -1,   2, -1, -1,   -1, -1, -1],
        [-1, 7, -1,    8, 9, -1,   -1, -1, 5],
        [-1, -1, 3,   -1, -1, -1,   7, -1, -1]
    ]
    print(complete_sudoku(test_board))
    pprint(test_board)