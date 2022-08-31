#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elt in my_list:
        if elt == search:
            new_list.append(replace)
        else:
            new_list.append(elt)
    return new_list
