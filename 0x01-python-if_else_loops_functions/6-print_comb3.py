#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            end_str = ', ' if not (i == 8 and j == 9) else ''
            print("{}{}".format(i, j), end=end_str)
print()
