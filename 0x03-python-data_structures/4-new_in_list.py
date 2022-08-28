#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    p_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return p_list
    p_list[idx] = element
    return p_list
