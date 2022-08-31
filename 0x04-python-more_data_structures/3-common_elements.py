#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for elt in set_1:
        for d in set_2:
            if elt == d:
                common_set.add(elt)
    return common_set

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
