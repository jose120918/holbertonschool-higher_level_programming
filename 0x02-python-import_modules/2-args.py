#!/usr/bin/python3
import sys

argumentos = sys.argv
tamaño = len(argumentos) - 1

if tamaño > 1:
    print(len(sys.argv), "arguments:")
    if __name__ == '__main__':
        for iterador, argumento in enumerate(sys.argv):
            print("{}: {}".format((iterador + 1), argumento))

elif tamaño == 0:
        print("{} arguments.".format(tamaño))

else:
        print("{} argument:".format(tamaño))
        print("{}: {}".format(tamaño, arg[1]))
