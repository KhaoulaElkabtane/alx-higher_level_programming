#!/user/bin/python3
"""Definies a Rectangle class."""

class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return("")

        r = []
        for i in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
            return ("".join(r))
