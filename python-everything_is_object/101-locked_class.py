#!/usr/bin/python3
class LockedClass:
    __names__ = ['first_name']

locked_instance = LockedClass()
locked_instance.first_name = "John"
    print(locked_instance.first_name) 
