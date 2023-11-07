#!/usr/bin/python3
"""Defines the to_son_string module"""

import json

def to_json_string(my_obj):
    """
    This returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
