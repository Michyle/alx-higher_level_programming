#!/usr/bin/python3
"""
This defines a rectangle class
"""

class Rectangle:
    """The Rectangle class Body"""

    def __ init__(self, width=0, height=0):
        """This initializes a Rectangle props in contructor."""

    self.width = width
    self.height = height

    def __str__(self):
        """This returns an informal string representation"""
        if self.__height == 0 or self.__width == 0:
            return ''
        record_str = ''
        for i in range(self._height):
            for j in range(self._width):
                record_str += '#'
            record_str += '\n'
        return record_str[:-1]

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
            """This retrives the height of the Rectangle instance"""
            return self.__height

        @height.setter
        def height(self, value):
            """This sets the hight of a rectangle instance"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value

        def area(self):
            """This Calculates the are of a Rectangle instance"""
            return self.__width * self.__height

        def perimeter(self):
            """This calculates and returns the perimeter of a rectangle"""
            if self.__height == 0 or self.__width == 0:
                return 0
            return 2 * (self.__width + self.__height)
