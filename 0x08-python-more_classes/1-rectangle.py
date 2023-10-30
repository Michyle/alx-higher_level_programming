#!/usr/bin/python3
"""
This will define a Rectangle class
"""

class Rectangle:
    """A Rectangle class that is defined  by hight and width"""

    def __init__(self, width=0, height=0):
        """Initializes  Rectangle instance in the contructor."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This will retrieve the width of the Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """This retrives the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """This will set the height of a rectangle instance
        Args:
            value: The value of the height, must be a positive integer
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value
