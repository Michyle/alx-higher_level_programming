#!/usr/bin/python3
"""Defines Write_file module"""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
