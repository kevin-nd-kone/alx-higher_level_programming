#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    tab = []
    for num in my_list:
        if num in tab:
            tab.append(num)
    for elt in tab:
        sum += elt
    return sum
