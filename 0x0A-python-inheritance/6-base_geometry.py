#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A BaseGeometry class with an area method that raises an exception.
    """
    def area(self):
        """
        Method to compute this area.
        Raises:
            Exception: Always, as area() is not implemented.
        """
        raise Exception('area() is not implemented')

