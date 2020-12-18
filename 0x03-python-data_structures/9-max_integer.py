#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        maximo = my_list[0]
        for cont in my_list:
            if cont > maximo:
                maximo = cont
    else:
        return None
