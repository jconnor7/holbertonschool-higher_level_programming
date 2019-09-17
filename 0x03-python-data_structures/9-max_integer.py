#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    max_val = my_list[-1]
    return (max_val if my_list is not [] else None)
