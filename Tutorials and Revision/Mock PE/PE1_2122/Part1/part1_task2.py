def RLD_R(s):
    if len(s) == 2:
        return s[0] * int(s[1])
    else:
        return s[0] * int(s[1]) + RLD_R(s[2:])

print(RLD_R('H3e2l3o1W1o3r4l2d1'))
print(RLD_R('A9H3E2M1'))
