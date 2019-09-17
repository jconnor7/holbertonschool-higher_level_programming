#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        cpmy_list = my_list.copy()
        if idx < 0:
            return cpmy_list
        elif idx > (len(my_list)-1):
            return cpmy_list
        else:
            cpmy_list[idx] = element
            return(cpmy_list)
