#!/usr/bin/python3
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1 for i in range(10): print(magic_string())
    return "BestSchool" * magic_string.n
