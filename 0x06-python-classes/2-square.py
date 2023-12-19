#!/usr/bin/python3
"""Square class definition for representing a square."""


class Square:
    """constructor size of a square"""
    def __init__(self, size):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
