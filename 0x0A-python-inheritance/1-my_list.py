#!/usr/bin/python3
"""The Mylist inherits from the list class"""

class MyList(list):
    """The class that inherits from the list"""
    def print_sorted(self):
        """This prints the sorted list"""
        print(sorted(self))
