#!/usr/bin/python3
"""Defines function to insert to file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        
        search_string (str): The string to search for within the file.
        filename (str): The name of file.
        new_string (str): String to insert.
    """
    output = ""
    with open(filename) as templ:
        for line in templ:
            output += line
            if search_string in line:
                output += new_string
    with open(filename, "w") as word:
        word.write(output)
