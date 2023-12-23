import sys

def is_sum_odd(n):
    if n < 0:
        sys.exit("Please enter a non-negative integer next time!")
    else:
        sum = 0
        while n > 0:
            sum += (n % 10)
            n = n // 10

        if (sum % 2 == 1):
            return True
        else:
            return False
        