#!/usr/bin/python3
"""Define class."""


class Student:
    """Get dictionary."""
    def __init__(self, first_name, last_name, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary"""
        if attrs and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr, None)
                for attr in attrs if hasattr(self, attr)
            }
        return {key: getattr(self, key) for key in sorted(self.__dict__)
                if hasattr(self, key)}

    def reload_from_json(self, json):
        """Reload from json."""
        for key, value in json.items():
            setattr(self, key, getattr(self, key, value))
