#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']
#lets use it
locked_instance = LockedClass()
locked_instance.first_name = "John"
    print(locked_instance.first_name) 
