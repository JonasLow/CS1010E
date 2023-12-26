def str_sorter(string):
    unique = []
    return_str = ""
    
    for char in string:
        if char not in unique:
            unique.append(char)

    unique.sort()

    for stuff in unique:
        if stuff != " ":
            return_str += stuff

    return return_str
