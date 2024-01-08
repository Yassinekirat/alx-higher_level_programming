#!/usr/bin/python3
"""Mylist class"""


class MyList(list):
    """sorted list"""

    def print_sorted(self):
        print(sorted(list(self)))
