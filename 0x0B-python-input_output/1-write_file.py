#!/usr/bin/python3
"""Defines function ot write to a file."""


def write_file(filename="", text=""):
    """Write string to UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
