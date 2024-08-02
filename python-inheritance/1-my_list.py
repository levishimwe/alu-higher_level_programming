#!/usr/bin/python3
"""  New class """


class MyList(list):
    """ Mylist class that inherist from list """

    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))   
