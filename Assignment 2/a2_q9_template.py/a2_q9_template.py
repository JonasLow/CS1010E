def merge(tup1, tup2):
    i1 = 0  
    i2 = 0  
    new_lst = []

    while i1 < len(tup1) and i2 < len(tup2):
        if tup1[i1] < tup2[i2]:
            new_lst.append(tup1[i1])
            i1 += 1
        else:
            new_lst.append(tup2[i2])
            i2 += 1

    new_lst.extend(tup1[i1:])
    new_lst.extend(tup2[i2:])

    return tuple(new_lst)

print(merge((-1, 1, 3, 5), (-2, 4, 6, 7)))
print(merge((-1, 1, 3, 5, 8, 10), (-2, 4, 6, 7)))
print(merge((-1, 1, 3, 5), (-2, 4, 6, 7, 9, 11)))
print(merge((-1, 1, 3, 5, 5, 5, 5, 5), (-2, 4, 6, 7)))
print(merge((-1, 1, 3, 5), (-2, 4, 6, 7, 7, 7, 7, 7)))               