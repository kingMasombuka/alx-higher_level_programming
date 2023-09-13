#!/usr/bin/python3
"""Defines a Python function that conert to json."""


def class_to_json(obj):
    """Return the dictionary formart of a simple data structure."""
    return obj.__dict__
