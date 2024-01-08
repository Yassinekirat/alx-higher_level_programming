#!/usr/bin/python3
"""Class"""


class BaseGeometry:
    """A basic geometry class."""

    def area(self):
        """Raises an error message."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validate input as an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
