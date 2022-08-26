#!/usr/bin/python3
from unicodedata import name
import hidden_4
if __name__ == "__main__":
    for val in dir(hidden_4):
        if "__" not in val:
            print(val)
