#!/usr/bin/python3
"""Función leer archivos"""


def append_write(filename="", text=""):
    """Funcion basica para leer texto en UTF8"""
    with open(filename, 'a+', encoding='utf8') as filetext:
        filetext.write(text)
        return len(text)
