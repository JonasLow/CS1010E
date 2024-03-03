SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_section(board):
    counter = [0, 0, 0, 0]
    n = [[0, 0], [0, 2], [2, 0], [2, 2]]
    for m in range(len(n)):
        check = [1, 2, 3, 4]
        x, y = -1, -1
        i = n[m][0]
        while i < n[m][0] + 2:
            j = n[m][1]
            while j < n[m][1] + 2:
                if board[i][j] == 0:
                    counter[m] += 1
                    x, y = i, j
                else:
                    check.remove(board[i][j])
                j += 1
            i += 1
        if len(check) == 1 and x != -1:
            board[x][y] = check[0]        
    for n in range(len(counter)):
        if counter[n] == 1:
            return True
    return False
    
print(fill_section(board1), fill_section(board2), fill_section(board3))
