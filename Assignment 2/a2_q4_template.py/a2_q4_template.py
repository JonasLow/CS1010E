def square_odd_terms(tpl):
    new_list = []
    for item in tpl:
        if item % 2 == 1:
            new_list.append(item ** 2)
        else:
            new_list.append(item)

    return new_list

print(square_odd_terms((2, 3, 4, 5)))