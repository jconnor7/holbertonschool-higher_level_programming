#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    max_val = my_list[-1]
    return (None if not my_list else max_val)
