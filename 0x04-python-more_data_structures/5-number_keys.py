#!/usr/bin/python3
def number_keys(a_dictionary):
    keys_tab = []
    for k,v in a_dictionary.items():
        keys_tab.append(k)
    return len(keys_tab)
