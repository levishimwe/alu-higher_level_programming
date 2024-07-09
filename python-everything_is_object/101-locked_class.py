#!/usr/bin/python3

"""Module that defines a locked class."""


class LockedClass:
    """
    A class that prevents dynamic creation of new instance attributes,
    except for 'first_name'.
    """
    __slots__ = ['first_name']
