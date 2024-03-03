def num_divisor_list(n):
    lst = [0]
    for i in range(1, n + 1):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        lst.append(divisor)
    return lst

print(num_divisor_list(6))
print(num_divisor_list(10))
