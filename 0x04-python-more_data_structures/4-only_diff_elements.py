#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set_1
    set_3.append(set_2)
    return set(set_3)
