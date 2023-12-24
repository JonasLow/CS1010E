def merge(tup1, tup2):
    # tup1 and tup2 each contain distinct integers in ascending order
    # integers in tup1 are different from those in tup2
    prev1 = tup1[0]
    prev2 = tup2[0]
    new_lst = []
    i = 1
    while i < max(len(tup1), len(tup2)):
        if i < len(tup1):
            if (tup1[i] < prev2 and tup1[i] < prev1):
                new_lst.append(tup1[i])
            elif prev1 < prev2:
                new_lst.append(prev1)
                prev1 = tup1[i]
            else:
                new_lst.append(prev2)
                prev2 = prev1
                prev1 = tup1[i]
        
        if i < len(tup2):
            if (tup2[i] < prev1 and tup2[i] < prev2):
                new_lst.append(tup2[i])
            elif prev2 < prev1:
                new_lst.append(prev2)
                prev2 = tup2[i]
            else: 
                new_lst.append(prev1)
                prev1 = prev2
                prev2 = tup2[i]
        
        i += 1
        if i == max(len(tup1), len(tup2)):
            if prev1 > prev2:
                new_lst.append(prev2)
                new_lst.append(prev1)
            else:
                new_lst.append(prev1)
                new_lst.append(prev2)
    
    return tuple(new_lst)

print(merge((-1, 1, 3, 5), (-2, 4, 6, 7)))
print(merge((-1, 1, 3, 5, 8, 10), (-2, 4, 6, 7)))
print(merge((-1, 1, 3, 5), (-2, 4, 6, 7, 9, 11)))
print(merge((-1, 1, 3, 5, 5, 5, 5, 5), (-2, 4, 6, 7)))
print(merge((-1, 1, 3, 5), (-2, 4, 6, 7, 7, 7, 7, 7)))               