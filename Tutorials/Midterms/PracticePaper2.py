# Question 1
print(7**2 == 49)

# Question 2
print(('cba' >= 'cc') == False)

# Question 3
s = {1, 1, 2, 2, 3, 3}
print(len(s) == 3)

# Question 4
lt = [10, 20, [300, [4000, 5000], 400, 500], 30, 40]
print((lt[2][1][0]) == 4000)

# Question 5
def f(a, b):
    b = g(b, b)
    return(b)
def g(a, b):
    return 3*a + b
print(f(1, 2) == 8) 

# Question 6
s = '12345'
def f(s1, s2):
    return int(s1) // int(s2)
print(f(s[:2], s[-1]) == 2)

# Question 7
def f(n):
    c = 0
    while n > 0:
        c = c + 1
        n = n // 10
    return c
print(f(12345) == 5) 

# Question 8
d = {1: 2, 3: 4, 5: 6}
def f(n):
    for val in d.values():
        if val == n:
            return True
    return False
print(f(5) == False)

# Question 9
def f(val):
    lst = [1, 7, 3, 7, -1, 9]
    idx = -1
    while idx >= -len(lst):
        if lst[idx] == val:
            break
        idx = idx - 1
    return idx
print(f(7) == -3) 

# Question 10
def f(m):
    k = m - 1
    while m > 0 and k < 10:
        k = k * 2
        m = m - 1
    return k
print(f(3) == 16) 

# Question 11
t1 = (1, 3, 2, 4, 0)
t2 = (0, 2, 1, 3)
res = 0
for i in range(len(t2)):
    res = res*10 + t1[t2[i]]
print(res == 1234) 

# Question 12
lst = [1, 2, 3, 4, 5]
j = 0
for i in range(1000):
    j = (j+2) % 5
print(lst[j] == 1) 

# Question 13
print('-7//2' == '-7//2')

# Question 14
'''
if day <= 5:
    if time < 9:
        print('Sleep!')
    elif time < 18:
        print('School!')
    else:
        print('Revision!')
else:
    if time < 10:
        print('Sleep!')
    else:
        print('Have fun!')
'''
# Answer: day = 5, time = 9

# Question 15
print(('1' + '2' * 3) == '1222')

# Question 16
def f(lst, k):
    return [x for x in lst if x % k != 0]
print(f([3, 2, 0, 5, 6, 2], 3) == [2, 5, 2]) 

# Question 17 (*)
def f(tpl):
    for i in range(len(tpl)):
        if tpl[i] < tpl[i+1]:
            return False
    return True 

# Answer: f((5, 3, 1)) will result in a runtime error

# Question 18
# Answer: D (True (+) True (+) False)

# Question 19
def f(n):
    ans = 0
    for x in range(n):
        for y in range(n, 0, -1):
            ans = ans + n
    return ans

# Answer: n * n * n

# Question 20
# Answer: 2 * (randint(0, p - 1)//2) + 1

# Question 21
def print_pyramid(k):
    for i in range(k//2+1):
        s = ''
        for j in range(2 * i - 1, k + 1):
            s = s + str(j) + '*'
        print(s) 

# Question 22 (X)
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

def f(lst1, lst2):
    lst1[1] = 7
    lst1, lst2 = lst2, lst1

f(lst1, lst2)
print(lst1 == [1, 7, 5]) 
    
# Question 23
'''
def max_occurrence(s):
    occurrence = [0] * 10
    for ch in s:
        occurrence[int(ch)] = occurrence[int(ch)] + 1
    return max(occurrence) 

def max_occurrence(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] = d[ch] + 1
        else:
            d[ch] = 1
    res = 0
    for val in d.values():
        if res < val:
            res = val
    return res 

def max_occurrence(s):
    max_occur = 0
    for i in range(0, len(s)):
        occur = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                occur = occur + 1
        max_occur = max(max_occur, occur)
    return max_occur 
'''
# Answer: D (all are acceptable functions)
