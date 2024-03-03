def RLD_I(string):
    i = 0
    word = ""
    while i < len(string) - 1:
        word += string[i] * int(string[i + 1])
        i += 2
    return word

print(RLD_I('H3e2l3o1W1o3r4l2d1'))
print(RLD_I('A9H3E2M1'))
