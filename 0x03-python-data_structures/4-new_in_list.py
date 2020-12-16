#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nuevalista = my_list[:] 
    if idx < 0:
	    return nuevalista
    elif idx > (len(my_list) - 1):
        return nuevalista
    else:
        nuevalista[idx] = element
        print(nuevalista)
