#!/usr/bin/python3
"""
Module for Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass representing a rectangle.
    Inherits from BaseGeometry for basic geometry functionality.
    """
    def __init__(self, width, height):
        '''
        Constructor.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Method which returns area of rectangle.
        Returns:
            The area of the rectangle.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        String representation method.
        Returns:
            A string representation of the rectangle.
        '''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

