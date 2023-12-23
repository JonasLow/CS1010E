def double_char(txt):
    word = ''
    for character in txt:
        word = word + (character * 2)

    return word

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
print(double_char('CS1010E'))