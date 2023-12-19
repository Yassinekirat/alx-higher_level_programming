#!/usr/bin/python3
"""Square class definition for representing a square."""


class Square:
    """constructor size of a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """property"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method for position."""
        if not (
        isinstance(value, tuple) and
        len(value) == 2 and
        all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
