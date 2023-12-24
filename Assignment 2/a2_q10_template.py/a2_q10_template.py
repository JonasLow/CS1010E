def resistors(seq, R):
    # Not allowed to modify the input sequence
    # len(seq) >= 2
    # seq[i] contains only positive integers sorted in ASCENDING order
    i = 0
    n = 0
    while i < len(seq):
        if (n != i and seq[n] + seq[i] == R):
            return True
        elif n < (len(seq) - 1):
            n += 1
        else:
            n = 0
            i += 1

    return False

print(resistors((1, 3, 4), 4))
print(resistors((1, 3, 5, 7), 5))
        