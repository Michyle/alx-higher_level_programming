#!/usr/bin/python3

"""Defines the save_to_json_file module"""
import json

def save_to_json_file(my_obj, filename):
    """
    This writes an object to a text file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
