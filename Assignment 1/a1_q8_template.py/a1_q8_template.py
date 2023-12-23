from turtle import *

def draw_reg_poly(d, n):
    for i in range(n):
        fd(d)
        lt(360 / n)

draw_reg_poly(200, 6)
draw_reg_poly(150, 8)