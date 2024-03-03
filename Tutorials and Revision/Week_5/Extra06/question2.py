def reverse_tuple(tup):
    i = 0
    j = len(tup) - 1
    new_tup = ()
    while i < len(tup):
        new_tup += tup[j],
        i += 1
        j -= 1
    return new_tup

print(reverse_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9)))
