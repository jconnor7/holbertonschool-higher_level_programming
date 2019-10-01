#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in my_list:
        try:
            if i <= x:
                print(i, end="")
                counter += 1
        except IndexError:
            break
    print()
    return counter
