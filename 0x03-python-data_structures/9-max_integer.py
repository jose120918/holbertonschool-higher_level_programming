#!usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        maximo = my_list[0]
        for cont in my_list:
            if cont >= maximo:
                maximo = cont
        return maximo
    else:
        return None
