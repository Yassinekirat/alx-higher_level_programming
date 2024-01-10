#!/usr/bin/python3
"""inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Search and update"""
    text = ""
    with open(filename, "r") as txt:
        for line in txt:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
