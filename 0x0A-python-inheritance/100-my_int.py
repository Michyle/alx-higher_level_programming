#!/usr/bin/python3
"""class MyInt that inherits from int."""

class MyInt(int):
    """MyInt class body"""

    def ___eq__(self, value):
        """Overrides == opeartor with !="""
        reeturn self.real != value

    def __ne__(self, value):
        """Override != operator with ==."""
        return self.real == value
