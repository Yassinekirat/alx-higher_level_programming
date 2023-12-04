#!/usr/bin/python3
def element_at(my_list, idx):
    if int(idx) < 0:
        return None
    if int(idx) >= len(my_list):
        return None
    else:
        return my_list[idx]
