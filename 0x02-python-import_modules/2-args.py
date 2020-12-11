#!/usr/bin/python3
import sys

argumentos = sys.argv
tamaño = len(argumentos) - 1


if tamaño > 1:
    print((tamaño), "arguments:")
    if __name__ == '__main__':
        for x in range(1, tamaño + 1):
            print("{}: {}".format(x, argumentos[x]))

elif tamaño == 0:
        print("{} arguments.".format(tamaño))

else:
        print("{} argument:".format(tamaño))
        print("{}: {}".format(tamaño, argumentos[1]))
