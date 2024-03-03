SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_row(board):
    counter = [0, 0, 0, 0]
    for i in range(len(board)):
        check = [1, 2, 3, 4]
        for j in range(4):
            if board[i][j] == 0:
                counter[i] += 1
            else:
                check.remove(board[i][j])
        if len(check) == 1:
            for k in range(4):
                if board[i][k] == 0:
                    board[i][k] = check[0]    
    for n in range(len(counter)):
        if counter[n] == 1:
            return True
    return False
    
print(fill_row(board1), fill_row(board2), fill_row(board3))
