#!/usr/bin/python3
"""Defines Student Class."""


class Student:
    """Represent student Class."""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student.

        Args:
            age (int): The age of the student.
            first_name (str): The first name of student.
            last_name (str): The last name of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary formart of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of Student.

        Args:
            json (dict): The key-value pairs to replace with.
        """
        for x, y in json.items():
            setattr(self, x, y)
