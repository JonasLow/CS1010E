from random import *

def is_7_solved(mat1):
    loopcounter = 0
    while loopcounter < 100000:
        # check if the mat1 is a sort and solved matrix or not, you simply can subtract your input matrix from the sorted 7-puzzle:
        # [ [1,2,3,4] , [5,6,7,0] ], if the result is an all-zero matrix (e.g., summation of all elements is 0), so this is a solved 7-puzzle return true
        # otherwise, input matrix doesn’t show a sorted/solved 7-puzzle, so return false
        if (mat1 == [[1, 2, 3, 4], [5, 6, 7, 0]]):
            return True
        else:
            next_move(mat1)
            loopcounter += 1

    return False

def next_move(mat):
    ii, jj = where_is(mat)
    if ii == 0:
        a = randrange(0, 2)
        if a == 0:
            mat[jj][ii], mat[jj][ii + 1] = mat[jj][ii + 1], mat[jj][ii]
        else:
            if jj == 0:
                mat[jj][ii], mat[jj + 1][ii] = mat[jj + 1][ii], mat[jj][ii]
            else:
                mat[jj][ii], mat[jj - 1][ii] = mat[jj - 1][ii], mat[jj][ii]
    
    elif ii == 3:
        a = randrange(0, 2)
        if a == 0:
            mat[jj][ii], mat[jj][ii - 1] = mat[jj][ii - 1], mat[jj][ii]
        else:
            if jj == 0:
                mat[jj][ii], mat[jj + 1][ii] = mat[jj + 1][ii], mat[jj][ii]
            else:
                mat[jj][ii], mat[jj - 1][ii] = mat[jj - 1][ii], mat[jj][ii]
    else:
        a = randrange(0, 3)
        if a == 0:
            mat[jj][ii], mat[jj][ii - 1] = mat[jj][ii - 1], mat[jj][ii]
        elif a == 1:
            mat[jj][ii], mat[jj][ii + 1] = mat[jj][ii + 1], mat[jj][ii]
        else:
            if jj == 0:
                mat[jj][ii], mat[jj + 1][ii] = mat[jj + 1][ii], mat[jj][ii]
            else:
                mat[jj][ii], mat[jj - 1][ii] = mat[jj - 1][ii], mat[jj][ii]

    return mat

def where_is(mat):
    jj = 0
    while jj < 2:
        ii = 0
        while ii < 4:
            if mat[jj][ii] == 0:
                break
            else:
                ii += 1
        if ii < 4:
            break
        jj += 1
    if jj == 2:
        return ii, jj - 1
    else:
        return ii, jj

Mat1 = [ [1,2,3,4] , [5,6,7,0] ]
Mat2 = [ [1,2,3,4] , [5,6,0,7] ]
Mat3 = [ [1,6,2,4] , [5,3,0,7] ]
Mat4 = [ [5,1,6,4] , [0,3,2,7] ]

print(is_7_solved(Mat1))
print(is_7_solved(Mat2))
print(is_7_solved(Mat3))
print(is_7_solved(Mat4))