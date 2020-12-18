#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list
    iterador = -1
    for cont in my_list:
        iterador += 1
        if cont % 2:
            new_list[iterador] = True
        else:
            new_list[iterador] = False
    return new_list
