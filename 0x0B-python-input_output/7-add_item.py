#!/usr/bin/env python3
import sys
import json
from typing import List

def save_to_json_file(my_obj: List, filename: str) -> None:
    """Saves an object to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename: str) -> List:
    """Loads an object from a JSON file."""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == '__main__':
    args = sys.argv[1:]
    filename = 'add_item.json'
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)
