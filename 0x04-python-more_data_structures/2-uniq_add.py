#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    tab = []
    for num in my_list:
        if num not in tab:
            tab.append(num)
    for elt in tab:
        sum += elt
    return sum


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
