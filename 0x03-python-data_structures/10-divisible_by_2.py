#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for cont in my_list:
        if cont % 2:
            new_list[cont] = True
        else:
            new_list[cont] = False
    return new_list
