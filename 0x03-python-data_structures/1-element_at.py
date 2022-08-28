#!/usr/bin/python3
def element_at(my_list, idx):
    if len(my_list) < idx or idx < 0:
        return None
    return my_list[idx]


my_list = [1, 2, 3, 4, 5]
idx = 10
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
