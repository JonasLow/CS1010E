from turtle import *

def draw_reg_poly(d, n):
    for i in range(n):
        fd(d)
        lt(360 / n)
