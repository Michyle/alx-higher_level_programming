#!/usr/bin/python3
"""Load from josn"""
import json

def load_from_json_file(filename):
    """load from the json file"""
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file_loaded)
