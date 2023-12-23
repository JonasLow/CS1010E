def invert_number(n):
    number = 0
    x = n
    while x > 0:
        number = number * 10
        number += (x % 10)
        x = x // 10
    
    return number
