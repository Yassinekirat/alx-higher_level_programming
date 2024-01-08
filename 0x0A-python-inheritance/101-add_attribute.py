#!/usr/bin/python3
"""add_attribute function"""

def add_attribute(obj, name, value):
    """Add new attribute."""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
