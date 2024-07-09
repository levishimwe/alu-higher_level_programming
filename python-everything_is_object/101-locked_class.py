#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']
locked_obj = LockedClass()
locked_obj.first_name = "John"  # This works
    print(locked_obj.first_name)  # Outputs: John

try:
    locked_obj.last_name = "Doe"  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")
