d = {'first':27, 'second':16, 'third':8}

def increase_by_one(d):
    for val in d:
        d[val] += 1
    return d

print(increase_by_one(d))
