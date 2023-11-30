#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(x, y):
    if x < y:
        result = add(x, y)
        for i in range(4, 6):
            result = add(result, i)
        return result
    else:
        return sub(x, y)
