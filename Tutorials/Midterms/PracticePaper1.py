# Question 1
print(int(2.9) == 2)

# Question 2 (X)
s1 = {1, 5, 3}
s2 = {2, 1}
print(len(s1 - s2) == 2)

# Question 3
s = 'abcde'
print((s[::-2] == 'eca') == True)

# Question 4
count = 0
for i in range(1, 8):
    if i == 5:
        break
    count = count + 1
print(count == 4)

# Question 5
a, b = 1, 2
while b < 10000:
    a = a - 2
    b = b + 2
print((a + b) == 3)

# Question 6
def f(n):
    return n * 3

n = 1
for i in range(3):
    n = f(n)
print(n == 27)

# Question 7
lst = [1, 2, 3]
def f():
    return lst[1:]

lst = f()
print(lst[0] == 2)

# Question 8 (*)
def make_list(n, limit):
    lst = []
    for i in range(1, n + 1):
        lst.append(limit // i)
    return lst

lst = make_list(5, 60)
print(lst[3] == 15)

# Question 9 (*)
def f(val):
    tup = (3 , 11, -6, 21)
    idx = len(tup) - 1
    while idx >= 0 and tup[idx] != val:
        idx = idx - 1
    return idx

print(f(0) == -1)

# Question 10
d = {
    5: 'good',
    'wind': [1, 2, 3],
    1.5: {'1': 6.5, (3, 4): (1, 5)}
}

print((d[1.5][(3, 4)][1]) == 5)

# Question 11
def f(s1, s2):
    count = 0
    for ch in s1:
        if ch not in s2:
            count = count + 1
    for ch in s2:
        if ch not in s1:
            count = count + 1
    return count
print(f('CS1010E', 'IS2101') == 4) 

# Question 12 (*)
def f(t, target):
    m, n = 0, len(t)-1
    while m < n:
        if t[m] + t[n] < target:
            n = n -1
        elif t[m] + t[n] > target:
            m = m + 1
        else:
            return True
    return False
print(f((1, 2, 3, 6, 7), 6) == False) 

# Question 13
# b = (1, 2, 3) + (4) will raise a Typeerror

# Question 14
y = 1000
if y > 0:
    x = 1
if y > 100:
    x = 2
elif y > 1000:
    x = 3
else:
    x = 4
print(x == 2)

# Question 15
def f(num):
    while num > 0:
        if num % 10 % 2 == 1:
            return True
        num = num // 10
    return False 

print(f(2804) == False)

# Question 16
'''
def f(n):
    while n > 0:
        print('Line', n)
        n = n - 1
for i in range(1, 5):
    f(i) 
'''
# Answer: 10 lines

# Question 17
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

lst = [22, 33, 44, 55]
swap(lst, 1, 2)
print(lst == [22, 44, 33, 55]) 

# Question 18 (X)
def f(x, y):
    i, m = 1, x
    while m % y != 0:
        i = i + 1
        m = i * x
    return m

# Question 19
'''
total = 0

for i in range(m, n):
    total = total + 1

print(total)
'''

# Answer: total + n - m

# Question 20
def convert(s):
    s1 = '' # begin with empty string
    for ch in s:
        if 'a' < ch < 'z':
            s1 = s1 + ch
        else:
            s1 = s1 + '*'
    return s1
print(convert('cs1010e is fun!') == 'cs****e*is*fun*') 

# Question 21
def check_colour(n):
    next_white, step = 1, 2
    while next_white < n:
        next_white = next_white + step
        step = step + 1

    if next_white == n:
        return 'White'
    else:
        return 'Black'

# Question 22
def is_subset(s1, s2):
    for val in s1:
        if val not in s2:
            return False
    return True 

# Question 23 (X)
def survivor(lst, k):
    pos = -1
    while len(lst) > 1:
        pos = (pos + k) % len(lst) 
        del lst[pos]
        pos = pos - 1
    return lst
print(survivor(['c', 'd', 'e', 'f', 'g', 'j'], 3))