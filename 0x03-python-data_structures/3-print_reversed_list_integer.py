#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    longitud = len(my_list) - 1

    while longitud != -1:
        print("{:d}".format(my_list[longitud]))
        longitud = longitud - 1
