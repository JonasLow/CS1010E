def tuplify(number):
    zeros = -1
    i = number
    x = number
    tpl = ()
    while i > 0:
        zeros += 1
        i //= 10
    while zeros > -1:
        digit = (x // (10 ** zeros)) % 10
        tpl += digit,
        zeros -= 1
    return tpl

print(tuplify(102486))