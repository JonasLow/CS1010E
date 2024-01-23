def perfect_number(n):
    if n == 1:
         return False
    i = n
    j = 1
    while i > 0:
         i -= j
         j += 1
    
    if i == 0:
         return True
    else:
         return False
