def num_divisor_list(n):
    lst = [0]
    for i in range(1, n + 1):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        lst.append(divisor)
    return lst

def list_of_max_divisor(x):
    lst = num_divisor_list(x)
    lst1 = []
    for k in range(1, len(lst)):
        if lst[k] == max(lst):
            lst1.append(k)
    return lst1

print(list_of_max_divisor(10))
print(list_of_max_divisor(25))
print(list_of_max_divisor(98))
