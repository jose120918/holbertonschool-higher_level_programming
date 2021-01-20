#!/usr/bin/python3
"""Función escribir al final de archivos"""


def append_write(filename="", text=""):
    """Funcion basica para escribir al final del archivo"""
    with open(filename, 'a+', encoding='utf8') as filetext:
        filetext.write(text)
        return len(text)
