#!/usr/bin/python3
"""Función leer archivos"""


def read_file(filename=""):
    """Funcion basica para leer texto en UTF8"""
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end="")
