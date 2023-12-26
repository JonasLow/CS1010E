from random import *

def monte_carlo_pi(n):
    m = 0
    for i in range(n):
        x = random()
        y = random()
        radius = (x ** 2 + y ** 2) ** 0.5
        if radius <= 1:
            m += 1
    return (m / n * 4)
