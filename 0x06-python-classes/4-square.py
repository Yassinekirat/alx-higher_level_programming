#!/usr/bin/python3
"""Square class definition for representing a square."""


class Square:
    """constructor size of a square"""
    def __init__(self, size):
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)

    @property
    def size(self):
        """property"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
