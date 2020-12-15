#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list):
        item = my_list[idx]
        return item
    elif idx > len(my_list):
        mayor = "None"
        return mayor
    else:
        menor = "None"
        return negativo