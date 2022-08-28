#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    p_list = my_list.copy()
    if idx < 0:
        return p_list
    elif idx > len(my_list) - 1:
        return p_list
    else:
        p_list[idx] = element
        return p_list
