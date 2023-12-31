#!/usr/bin/python3
"""
This module has a class that inherits attr of a class list
"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """


    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
