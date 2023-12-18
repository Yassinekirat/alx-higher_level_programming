#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    if my_list is None:
        my_list = []

    for i in range(min(x, len(my_list))):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return count
