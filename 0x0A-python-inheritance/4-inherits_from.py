#!/usr/bin/python3
"""Check object's inheritance, excluding direct class"""


def inherits_from(obj, a_class):
    """Check object's inheritance, excluding direct class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
