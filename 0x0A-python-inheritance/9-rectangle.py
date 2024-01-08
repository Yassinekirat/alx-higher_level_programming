#!/usr/bin/python3
"""Class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits form another class"""

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string describing the rectangle: [Rectangle] <width>/<height>"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
