#!/usr/bin/python3
"""My integer class"""


class MyInt(int):
    """Subclass of int with inverted equality."""

    def __eq__(self, other):
        """Override the == operator to invert its behavior."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the != operator to invert its behavior."""
        return not super().__ne__(other)
