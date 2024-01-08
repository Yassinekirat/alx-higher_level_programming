#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """initialisation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
