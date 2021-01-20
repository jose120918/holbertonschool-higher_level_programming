#!/usr/bin/python3
"""Función escribir en archivos"""


def write_file(filename="", text=""):
    """Funcion basica para sobreeescribir texto en UTF8"""
    with open(filename, 'w', encoding='utf8') as filetext:
        filetext.write(text)
        return len(text)
