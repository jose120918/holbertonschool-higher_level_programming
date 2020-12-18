#!/usr/bin/python3
def max_integer(my_list=[]):
    iterador = 0
    maximo = 0
    num_elementos = len(my_list)
    if num_elementos == 0:
        return None
    for cont in my_list:
        if my_list[iterador] > maximo:
            maximo = my_list[iterador]
        iterador = iterador + 1
