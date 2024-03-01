def extract_parentheses_I(st):
    new_str = ""
    i = 0
    while i < len(st):
        if st[i] == "(" or st[i] == ")":
            new_str += st[i]
        i += 1
    return new_str

def extract_parentheses_R(st):
    if len(st) == 1 and (st[0] == ")" or st[0] == "("):
        return st[0]
    elif st[0] == ")" or st[0] == "(":
        return st[0] + extract_parentheses_R(st[1:])
    else:
        return extract_parentheses_R(st[1:])



print(extract_parentheses_I('(1+2)*(3+(4-5))'))
print(extract_parentheses_I('(1+2)*(3+(4-5)))'))