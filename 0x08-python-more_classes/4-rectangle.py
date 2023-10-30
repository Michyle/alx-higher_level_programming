#!/usr/bin/python3
"""Module 4-rectangle"""

class Rectangle:
    """Defines the rectangle class"""

    def __init__(self, width=0, height=0):
        """This initializes the rectangle props in the constructor"""
        self.width = width
        self.height = height

    def __str__(self):
        """This returns an informal string reprsention of a rectangle"""
        Return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.seter
    def height(self, value):
        """This sets the height of a Rectangel instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the perimeter of a rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return
        return 2 * (self.__width + self.__height)
