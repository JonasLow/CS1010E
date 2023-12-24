from math import *

def deviation(tpl):
    avg = sum(tpl) / len(tpl)
    numerator = 0
    for number in tpl:
        numerator += (number - avg) ** 2
    return sqrt(numerator / len(tpl))
