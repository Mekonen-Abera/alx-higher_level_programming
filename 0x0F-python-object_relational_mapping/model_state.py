#!/usr/bin/python3
"""
Defines a state model that contains the class definition of a 
State and an instance Base = declarative_base().
"""
rom lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

"""
Inherits from Base Tips and links to the MySQL table states.
Class attribute id represents a column of an auto-generated, 
unique integer, can't be null, and is a primary key.
Class attribute name represents a column of a string with 
a maximum of 128 characters and can't be null.
"""

 __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
