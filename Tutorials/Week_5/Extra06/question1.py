def repeat(string):
    wordbank = {}
    count = 0
    for i in range(len(string)):
        if string[i] in wordbank:
            wordbank[string[i]] += 1
        else:
            wordbank[string[i]] = 1
    for letter in wordbank:
        if wordbank[letter] > 1:
            count += 1
    return count

print(repeat('theQUICKbRoWnFoX'))