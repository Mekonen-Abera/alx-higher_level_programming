#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("You Cannot create new instance attribute")
