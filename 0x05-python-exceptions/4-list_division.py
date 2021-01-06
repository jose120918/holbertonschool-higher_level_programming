#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    longitud = []
    for i in range(list_length):
        result = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except ZeroDivisionError:
            print("division by 0")
            continue
        except TypeError:
            print("wrong type")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            longitud.append(result)
    return longitud
