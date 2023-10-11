#!/usr/bin/python3
"""Defines a class My list."""


class MyList(list):
    """A subclass of list."""
    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
