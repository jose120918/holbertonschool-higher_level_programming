#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        iterador = 0
        for valor in fila:
            iterador = iterador + 1
            print("{:d}".format(valor), end="")
            if iterador != len(fila):
                print(" ", end="")
        print("")
