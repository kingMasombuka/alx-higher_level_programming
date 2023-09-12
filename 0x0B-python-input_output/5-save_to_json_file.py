#!/usr/bin/python3
"""Defines JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writeobject to text file using JSON formart."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
