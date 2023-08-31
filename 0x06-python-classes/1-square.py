#!/usr/bin/python3
'''This module defines a square class
The class has a function __init__ which contains
the self paramter and a size parameter
'''


class Square:
    """Class Square defines a square object
    """

    def __init__(self, size):
        """Initialize method that stores the size of the square

        Args:
            param1 (int): size of the square
        """

        self.__size = size
