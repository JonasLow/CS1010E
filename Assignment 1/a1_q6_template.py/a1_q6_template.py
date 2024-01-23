def find_winners(factor, must_have, n):
    winners = 0
    i = 1
    while (factor * i) < n+1:
        if contain_digit(factor * i, must_have):
            winners += 1
        i += 1

    return winners

def contain_digit(number, digit):
    x = number
    while x > 0:
        if (x % 10 == digit):
            return True
        else:
            x = x // 10
    
    return False


print(find_winners(3, 5, 100))
print(find_winners(9, 1, 15))
print(find_winners(7, 7, 200))