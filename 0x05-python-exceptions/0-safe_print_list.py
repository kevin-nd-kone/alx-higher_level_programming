#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        newList = my_list[:x]
        v = 0
        for i in newList: v +=1
        print(''.join(str(i) for i in newList))
        return v
    except:
        print()


my_list = [1,2,3,4,5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

