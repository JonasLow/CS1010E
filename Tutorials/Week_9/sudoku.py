from fillrow import fill_row
from fillcol import fill_col
from fillsection import fill_section

board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_board(board):
    fillable = True  # indicate if a board is still fillable
    while fillable:  # if still fillable, you shall continue filling it
        if fill_row(board) or fill_col(board) or fill_section(board):
            fill_row(board)
            fill_col(board)
            fill_section(board)
        else:
            fillable = False
    return board  # if no longer fillable, shall return the board

print(fill_board(board1), fill_board(board2), fill_board(board3))
