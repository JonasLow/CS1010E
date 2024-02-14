def change_value_at_index(tpl, index, value):
    i = 0
    new_tup = ()
    while i < len(tpl):
        if i == index or i == len(tpl) + index:
            new_tup += value,
        else:
            new_tup += tpl[i],
        i += 1
    return new_tup

print(change_value_at_index((1, 2, 3, 4, 5), 4, 'huh'))