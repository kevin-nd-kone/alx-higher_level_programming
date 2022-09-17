#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        newList = my_list[:x]
        length = 0
        for i in newList:
            length += 1
        print(''.join(str(i) for i in newList))
        return length
    except IndexError:
        print()
