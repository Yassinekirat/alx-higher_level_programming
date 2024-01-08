#!/usr/bin/python3
"""add_attribute function"""

def add_attribute(obj, name, value):
    """add attribute"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
