#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A BaseGeometry class with an area method that raises an exception
    and an integer_validator method for validating integer values.
    """
    def area(self):
        """
        Method to compute this area.
        Raises:
            Exception: Always, as area() is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Method for validating the value.
        Args:
            name (str): The name associated with the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

