#!/usr/bin/python3

def print_last_digit(number):
    num = 0
    if(number < 0):
        num = number * (-1)
        last = (num % 10)*(-1)
    else:
        last = number % 10
    return last


print(print_last_digit(-98))
