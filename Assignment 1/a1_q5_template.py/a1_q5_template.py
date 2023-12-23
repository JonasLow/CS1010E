def perfect_number(n):
    i = n
    j = 1
    while i > 0:
         i -= j
         j += 1
    
    if i == 0:
         return True
    else:
         return False

print(perfect_number(6))
print(perfect_number(8))
print(perfect_number(21))
