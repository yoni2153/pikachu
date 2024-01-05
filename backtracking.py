def print_board(board):
    for row in board:
        print(row)


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # checking the 2x2 grid
    # this makes it so if you are in the last or second column (index 3) it will become index 2
    new_row = 3*(row//3)
    new_col = 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[new_row + i][new_col + j] == num:
                return False

    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve(board):
    empty_location = find_empty(board)

    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


puzzle = [
    [0, 0, 0, 1, 0, 2, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 8, 0, 0, 0, 9, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [2, 0, 0, 0, 8, 0, 0, 0, 1],
    [0, 0, 9, 0, 0, 0, 8, 0, 5],
    [0, 7, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 3, 0, 4, 0, 0, 0],
]

if solve(puzzle):
    print_board(puzzle)
