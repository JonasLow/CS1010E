from turtle import *
from a1_q8_template import draw_reg_poly

def draw_flower(length, sides, petals):
    rotation = 360 / petals
    for i in range(petals):
        lt(rotation)
        draw_reg_poly(length, sides)

draw_flower(100, 8, 10)