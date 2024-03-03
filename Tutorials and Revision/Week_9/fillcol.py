SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_col(board):
    counter = [0, 0, 0, 0]
    j = 0
    while j < len(board):
        check = [1, 2, 3, 4]
        x, y = -1, -1
        for i in range(len(board)):
            if board[i][j] == 0:
                counter[j] += 1
                x, y = i, j
            else:
                check.remove(board[i][j])
        if len(check) == 1 and x != -1:
            board[x][y] = check[0]
        j += 1
    for n in range(len(counter)):
        if counter[n] == 1:
            return True
    return False
    
print(fill_col(board1), fill_col(board2), fill_col(board3))
