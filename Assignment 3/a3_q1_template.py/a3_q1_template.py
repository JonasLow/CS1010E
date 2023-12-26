def gibonacci_R(m):
    # You can only use recursion without using any reptition statments
    # You may not use iterative constructs to solve this
    # Assumption: m >= 0
    if m == 2:
        return 1
    elif m < 2:
        return 0
    else:
        return gibonacci_R(m - 1) + gibonacci_R(m - 3)

def gibonacci_I(n):
    # You may not use recursive functions to solve this
    # Assumption: n >= 0
    newbaby = 0
    baby = 1
    young = 0
    adult = 0
    i = 0
    while i < n:
        newbaby = adult
        adult += young
        young = baby
        baby = newbaby
        i += 1
        
    return adult

'''
# FUNCTION FOR MAXIMUM CALCULATION
from time import *

start_time = time()
gibonacci_R(54)
end_time = time()
print(f"Execution time: {end_time - start_time}s")


start_time = time()
gibonacci_I(3.5 * 10 ** 6)
end_time = time()
print(f"Execution time: {end_time - start_time}s")

# REFLECTION FOR MAXIMUM
The maximum number of recursions that can be done in 1 minute is 54 (50.84s)
The maximum number of iterations that can be done in 1 minute is roughly 3.5 * 10 ** 6 (61.73s)
If we were to compare 55 recursions (75.71s) and 4 * 10 ** 6 iterations (75.24s), it is evident that the amount of time taken to 
execute the recursion fuction is significantly greater than that of the iteration function
While the function is easily computed using a recursive function, but it is faster to use an iteration instead
This is also related to the time complexity of the function.
The iteration function has an order of O(n) while the recursive function has an order of O(2 ** n)
'''
