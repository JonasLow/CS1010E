tup = ( ('C', 3), ('1', 4) , ('E', -1), ('S', 1), ('0', 7), ('0', 2), ('M', 8), ('1', 5), ('A', 1) )

def decode(i_tup, s_idx):
    i = s_idx
    string = ''
    while True:
        if i == -1:
            break
        else:
            string += i_tup[i][0]
            i = i_tup[i][1]
    return string

print(decode(tup, 0))
print(decode(tup, 6))
