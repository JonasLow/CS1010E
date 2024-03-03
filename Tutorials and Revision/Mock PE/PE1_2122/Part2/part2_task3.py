def num_divisor_list(n):
    lst = [0]
    for i in range(1, n + 1):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        lst.append(divisor)
    return lst

def how_many_prime(x):
    lst = num_divisor_list(x)
    count = 0
    for number in lst:
        if number == 2:
            count += 1
    return count

print(how_many_prime(25))
print(how_many_prime(100))
print(how_many_prime(1000))
