#!/usr/bin/python3
"""Función leer archivos"""


def write_file(filename="", text=""):
    """Funcion basica para leer texto en UTF8"""
    with open(filename, 'w', encoding='utf8') as filetext:
        filetext.write(text)
        return len(text)
