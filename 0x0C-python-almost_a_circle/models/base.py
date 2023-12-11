#!/usr/bin/python3
"""
Defines and create a base model class.
"""
import json
import csv
import turtle

class Base:
    """
    Represents the base model class attributes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the instance with an optional id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        file_name = f"{cls.__name__}.json"

        with open(file_name, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the deserialized list of dictionaries from a JSON string.
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes set based on the input dictionary.
        """
        if dictionary:
            dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances instantiated from a JSON file.
        """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                list_instances = [cls.create(**d) for d in list_dicts]
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV serialization of a list of objects to a file.
        """
        file_name = f"{cls.__name__}.csv"

        with open(file_name, "w") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                field_names = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances instantiated from a CSV file.
        """
        file_name = f"{cls.__name__}.csv"

        try:
            with open(file_name, "r") as csvfile:
                fieldnames = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)

                new_list_dict = [dict((key, int(value)) for key, value in d.items()) for d in list_dicts]

                list_of_instances = [cls.create(**d) for d in new_list_dict]

                return list_of_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares using the turtle module.
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#3399FF")
        turt.pensize(4)
        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#FFFF00")

        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

if __name__ == "__main__":
    pass
