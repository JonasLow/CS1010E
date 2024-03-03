# Question 1 (*)
print(int(-2.9) == -2)

# Question 2
def f(x):
    return x**2
print(f(2) == 4)

# Question 3
def f(s, ch):
    count = 0
    for val in s:
       if val == ch:
            count = count + 1
    return count
print(f('abbacadaba', 'a') == 5)

# Question 4
for i in range(2, 100):
    if i%2 == 0 and i%3 == 0:
        break
print(i == 6)

# Question 5
lst = [1, 2, 3]
del lst[1]
lst.append(4)
print(sum(lst) == 8) 

# Question 6
t1 = (1, 2, 3, 4, 5)
t2 = (6, 2, 4, 8)
def f(): 
    s = set()
    for val in t2:
        if val not in t1:
            s.add(val)
    return(len(s))
print(f() == 2)

# Question 7
def f(n, d):
    result, weight = 0, 1
    while n > 0:
        if n%10 != d:
            result = result + n%10*weight
            weight = weight * 10
        n = n // 10
    return result
print(f(123123, 2) == 1313) 

# Question 8
def f(t1, t2):
    idx_t1, idx_t2 = 0, 0
    while idx_t1 < len(t1) and idx_t2 < len(t2):
        if t1[idx_t1] > t2[idx_t2]:
            idx_t1 = idx_t1 + 1
        elif t1[idx_t1] < t2[idx_t2]:
            idx_t2 = idx_t2 + 1
        else:
            return t1[idx_t1]
    return -1

t1, t2 = (8, 7, 5, 3, 1), (10, 9, 8)
print(f(t1, t2) == 8)

# Question 9 (*)
fruit = ( (2, 'apple'), (0, 'orange'), (4, 'banana'), (-1, 'pear'), (3, 'mango'), (-2, 'kiwi') )
p = 2
while p > 0:
    p = fruit[p][0]
print(fruit[p][1] == 'kiwi') 

# Question 10
def f(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] = d[ch] + 1
        else:
            d[ch] = 1
    count = 0
    for key in d:
        if d[key] > 1:
            count = count + 1
    return count
print(f('I_did_it') == 3)

# Question 11
x = 100
for a in range(5):
    for b in range(20):
        if a%2 == 0:
            x = x + a
        else:
            x = x - a
print(x == 140) 

# Question 12
print({1, 2} == {2, 1})

# Question 13
x = 5
def f(x):
    x = 2
    return x+1
print((x, f(x)) == (5, 3))

# Question 14
# Answer: 4, 4, 3

# Question 15
# Answer: None of the above

# Question 16 (*)
x, y = 2, 1
while x < 50:
    x = x ** 2
    y = y + 1
print(y == 4)

# Question 17 (*)
def f(a, n):
    for i in range(n):
        a = a + a
    return a 

# Answer: 2 ** n * a

# Question 18
def f1(n): # assume 0 < n < 100
    total = 0
    for a in range(n+1):
        total = total + a
    return total

def f2(n): # assume 0 < n < 100
    total = 0
    while n > 0:
        total = total + n
        n = n - 1
    return total

def f3(n): # assume 0 < n < 100
    return n*(n+1)//2 

print((f1(1) != f2(1)) == False)
print((f1(2) != f3(2)) == False)
print((f2(3) != f3(3)) == False)

# Answer: D (Given the same n, all 3 functions return the same value)

# Question 19
lt = [0, 1, 2, 3, 4]
for a in range(1, 5):
    for b in range(a):
        lt[a] = lt[a] + lt[b]
print((lt) == [0, 1, 3, 7, 15]) 

#+ Question 20
def f(n):
    b, k = 0, 10
    while n > 0:
        d = n % 10
        b = b * k + d % 2
        n = n // 10
    return b

print((f(222) == 0) and (f(111) == 111) and (f(521) == 101) and (f(654) == 10))

# Question 21
def p3_p5(n):
    p3, p5 = 3, 5
    while p3 <= n or p5 <= n:
        if p3 < p5:
            print(p3)
            p3 = p3 * 3
        else:
            print(p5)
            p5 = p5 * 5

# Answer: B

# Question 22
def compute(poly, x):
    ans = 0
    for i in range(5):
        ans = (ans + poly[i]) * x
    return ans + poly[5] 

# Answer: A

# Question 23
def is_palindrome(s):
    string = '' # begin with an empty string
    for ch in s:
       string = ch + string
    return s == string            

def is_palindrome(s):
 return s == s[::-1] 

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def is_palindrome(s):
    left, right = 0, -1
    while left < len(s)//2:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

# Answer: D (All of the above are true)