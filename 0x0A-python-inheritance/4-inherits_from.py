#!/usr/bin/python3
"""Defines  class-checking function."""


def inherits_from(obj, a_class):
    """Checks if a an inherited instance of a class.

    Args:
        obj (any): The object check.
        a_class (type): The class type of obj to.
    Returns:
        If obj  instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
