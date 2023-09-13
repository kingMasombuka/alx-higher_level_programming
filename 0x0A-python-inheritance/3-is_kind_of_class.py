#!/usr/bin/python3
"""Defines class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check an object is  instance or inherited instance of a class.

    Args:
        a_class (type): The class to match the type of obj to.
        obj (any): The object to check.
    Returns:
        If obj an instance or  instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
