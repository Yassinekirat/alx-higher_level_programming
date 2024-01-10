#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle"""
    list_new = []
    if n <= 0:
        return ([])
    list_new = [[1]]
    for i in range(n - 1):
        tmp = [0] + list_new[-1] + [0]
        row = []
        for j in range(len(list_new[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        list_new.append(row)
    return (list_new)
