def make_out_word(s, word):
    if len(s) != 4:
        return("Please input exactly for characters for the first parameter.")
    else:
        return_string = ""
        return_string += s[:2]
        return_string += word
        return_string += s[2:]

        return return_string

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))
