#!/usr/bin/python3
"""
    Nothing to import
"""


def say_my_name(first_name, last_name=""):
    """
        Print user name
    """
    if first_name == "" and last_name == "":
        return None
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
