#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = my_list[x-1]
    newList = my_list[:x]
    length = 0
    value = ""
    if my_list[x-1]:
        for elt in newList:
            try:
                if elt / 1 == elt:
                    value += str(elt)
                    length += 1
            except TypeError:
                pass
    print("{:d}".format(int(value)))
    return length
