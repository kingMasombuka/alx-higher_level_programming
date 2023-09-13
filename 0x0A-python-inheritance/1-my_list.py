#!/usr/bin/python3
"""Defines inherited list class MyList."""


class MyList(list):
    """Implements  printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
