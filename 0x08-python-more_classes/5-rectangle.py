#!/usr/bin/python3
""" a class Rectangle that defines a rectangle"""

class Rectangle:
    """REctangle class deff"""
    def __init__(self, width=0, heigt=0):
        """intializes a rectangle instance"""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns string representation of rectangle (#).
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")

        @property
        def width(self):
            """Gets the with of the rectangle instance"""
            return self._width
        
        @width.setter
        def width(Self, value):
            """sets the width of the rectangle instance"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >=0")
            self.__width = value

        @property
        def height(self):
            """Geth the height of the rectangle instance"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of a Rectangle instance"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """Calculates the area of a Rectangle instance"""
            return self.__width * self.__height

        def perimeter(self):
            """calcs the perimeter of the rectangle instance"""
            if self.__height == 0 or self.__width == 0:
                return 0
            return 2 * (self.__width + self.__height)
