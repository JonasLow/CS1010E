def is_sorted(tup):
    for i in range(len(tup) - 1):
        if tup[i + 1] < tup[i]:
            return False
    return True
