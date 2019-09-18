def divisible_by_2(my_list=[]):
    newlist = []
    for num in my_list:
        newlist.append(True) if num % 2 == 0 else newlist.append(False)
    return (newlist)
