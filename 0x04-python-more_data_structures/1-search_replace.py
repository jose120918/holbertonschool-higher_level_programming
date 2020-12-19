#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    nueva_lista = my_list[:]
    for elemento in my_list:
        if search == elemento:
            nueva_lista[i] = replace
        i += 1
    return nueva_lista
