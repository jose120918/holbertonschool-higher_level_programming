#!/usr/bin/python3
"""writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """ method OBJ -> txt"""
    with open(filename, 'w+') as fil:
        json.dump(my_obj, fil)
