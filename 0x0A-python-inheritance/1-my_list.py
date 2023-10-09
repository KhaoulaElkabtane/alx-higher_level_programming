#!/usr/bin/python3
""" Defines a class My list"""

class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Initializes a new instance of My list"""
        super().__init__()
    def print_sorted(self):
        """ Prints the elements of the list in ascending order."""
        print(sorted(self))
