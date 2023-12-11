#!/usr/bin/python3
"""
Rewritten class for handling JSON and CSV files.
"""

import json
import csv


class Base:
    """Base class for handling JSON and CSV files."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base object."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        string = "[]"
        if list_dictionaries is not None:
            string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_string = cls.to_json_string([obj.to_dictionary()
                                                  for obj in list_objs])
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        empty_list = []
        if json_string is not None:
            empty_list = json.loads(json_string)
        return empty_list

    @classmethod
    def create(cls, **dictionary):
        """Create an object based on a dictionary."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            obj = Rectangle(1, 1)
        elif cls is Square:
            obj = Square(1)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file."""
        import os.path
        filename = cls.__name__ + '.json'
        obj_list = []
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                obj_list = [cls.create(**dictionary) for dictionary in
                            cls.from_json_string(json_string)]
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file."""
        filename = cls.__name__ + '.csv'
        csv_todict = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            dwriter = csv.DictWriter(file, csv_todict[0].keys())
            dwriter.writeheader()
            dwriter.writerows(csv_todict)

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file."""
        obj_list = []
        filename = cls.__name__ + '.csv'
        with open(filename, mode="r", encoding="utf-8") as file:
            dreader = csv.DictReader(file)
            for row in dreader:
                temp_dict = {}
                for key, value in dict(row).items():
                    temp_dict[key] = int(value)
                obj_list.append(cls.create(**temp_dict))
        return obj_list
