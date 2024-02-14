def untuplify(tpl):
    sum = 0
    for val in tpl:
        sum = sum * 10 + val
    return sum

print(untuplify((1, 0, 2, 4, 8, 6)))