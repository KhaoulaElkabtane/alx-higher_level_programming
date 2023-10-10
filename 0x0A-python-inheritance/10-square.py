#!/usr/bin/python3
"""
Module for Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass representing a square.
    Inherits from Rectangle to reuse its functionality.
    """
    def __init__(self, size):
        """
        Constructor.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Method for area of square.
        Returns:
            The area of the square.
        """
        return self.__size ** 2

