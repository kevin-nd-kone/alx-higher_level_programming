#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        newList = my_list[:x]
        l = 0
        for i in newList:
            l += 1
        print(''.join(str(i) for i in newList))
        return l
    except:
        print()

