def print_board(board):
    for row in board:
        print(board)
        print(row)


# def possible_positions(board, num):
#     # finding the empty positions
#     empty_positions = find_empty_postions(board)
#     # num on board
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] == num:
#                 # find the possible positions
#                 new_row, new_col = 2*(i//2), 2*(j//2)
#                 blocked_grids = []
#                 for i_row in range(2):
#                     for i_col in range(2):
#                         blocked_grid = new_row + i_row, new_col + i_col
#                         blocked_grids.append(blocked_grid)

#                 blocked_row = [(i, index) for index in range(2, 4)]
#                 blocked_col = [(index, j) for index in range(2, 4)]
#                 blocked_positions = blocked_grids + blocked_row + blocked_col
#     for value in blocked_positions:
#         for row in empty_places:
#             if value in row:
#                 row.remove(value)
#             if row == []:
#                 empty_places.remove(row)
#             if len(row) == 1 and row[0] not in blocked_positions:
#                 num_row, num_col = row[0]
#                 board[num_row][num_col] = num
#     possible_positions(board, num)
#     return print_board(puzzle)


# def solve(board):
#     # for i in range(4):
#     possible_positions(board, 1)


puzzle = [
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 3, 0, 0],
    [0, 0, 4, 0]
]

# print(possible_positions(puzzle, 1))


def find_empty_postions(board):
    empty_postions = []
    for i in range(4):
        empty_postion = [(i, j) for j in range(4) if board[i][j] == 0]
        empty_postions.append(empty_postion)
    return empty_postions


def find_possible_postisions(board):
    pass


def is_valid(board, num):
    for i in range(4):
        for j in range(4):
            if board[i][j] == num:
                new_row, new_col = 2*(i//2), 2*(j//2)
                blocked_grids = []
                for i_row in range(2):
                    for i_col in range(2):
                        blocked_grid = new_row + i_row, new_col + i_col
                        blocked_grids.append(blocked_grid)
                blocked_rows = [(i, index) for index in range(2, 4)]
                blocked_cols = [(index, j) for index in range(2, 4)]

                blocked_positions = blocked_grids + blocked_rows + blocked_cols
    return blocked_positions


# print(find_empty_postions(puzzle))
print(is_valid(puzzle, 1))
print(is_valid(puzzle, 2))
