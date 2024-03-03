def transpose(m):
    matrix = []
    for r in range(len(m[0])):
        new_row = []
        for c in range(len(m)):
            new_row += [m[c][r]]
        matrix += [new_row]
    return matrix

print(transpose([[1, 2], [3, 4], [5, 6]]))
