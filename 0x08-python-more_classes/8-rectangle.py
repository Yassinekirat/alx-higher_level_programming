#!/usr/bin/python3
""" class that defines a rectangle."""


class Rectangle:
    """class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """property setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area"""
        return self.width * self.height

    def perimeter(self):
        """ Return the perimetre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """Return the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if i == self.height - 1:
                break
            string += "\n"

        return string

    def __repr__(self) -> str:
        """representation method"""
        ghlid = f"Rectangle({self.width}, {self.height})"
        return ghlid

    def __del__(self):
        """shinra tensei"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """check the rectangle with the bigger or equal area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
