#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = dict(sorted(a_dictionary.items()))
    for x, y in new_dic.items():
        print('{}: {}'.format(x, y))
