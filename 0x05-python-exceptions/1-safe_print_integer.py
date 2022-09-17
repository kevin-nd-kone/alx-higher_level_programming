#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if(value / 1):
            return True
    except (TypeError, ValueError):
        return False
