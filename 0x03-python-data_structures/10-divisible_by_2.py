#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for elt in my_list:
        if elt % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list