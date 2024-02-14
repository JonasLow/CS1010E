def occurrence(s1, s2):
    count = 0
    length2 = len(s2)
    i = 0
    while (i + length2) <= len(s1):
        if s1[i:(i + length2)] == s2:
            count += 1
            i += length2
        else:
            i += 1
    return count

print(occurrence('101100', '10'))
print(occurrence('101010', '10'))
print(occurrence('101010', '101'))
print(occurrence('1111', '11'))
