# Project: 0x0F. Python - Object-relational mapping

## Resources

#### Read or watch:

* [Object-relational mappers](https://intranet.alxswe.com/rltoken/a8DUOWhXpNX3TEwgyT-U8A)
* [mysqlclient/MySQLdb documentation](https://intranet.alxswe.com/rltoken/JtFaKjnqxudr6Hi05Us1Lw)
* [MySQLdb tutorial](https://intranet.alxswe.com/rltoken/TdUSYFNGbXJG1WjCEoq5FA)
* [SQLAlchemy tutorial](https://intranet.alxswe.com/rltoken/YyL5hsscviNH04XGW-XpfA)
* [SQLAlchemy](https://intranet.alxswe.com/rltoken/j9azWF2Db_2rNolTxOF3SA)
* [mysqlclient/MySQLdb](https://intranet.alxswe.com/rltoken/0zLhY9KqKjn-zmdb7X598Q)
* [Introduction to SQLAlchemy](https://intranet.alxswe.com/rltoken/pw50Bl1Bj84wksxm018dwA)
* [Flask SQLAlchemy](https://intranet.alxswe.com/rltoken/B-xIdMtGvpus8vHxAIRrPg)
* [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.alxswe.com/rltoken/deIzPMrfK8Ixqm-AboFHWg)
* [Python SQLAlchemy Cheatsheet](https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q)
* [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ)
* [SQLAlchemy Tutorial](https://intranet.alxswe.com/rltoken/5G_R2NmQRFqiZb84qxYERQ)
* [Python Virtual Environments: A primer](https://intranet.alxswe.com/rltoken/OXle6kXpmD88D0WbgbTWqg)
## Learning Objectives

### General

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to <code>SELECT</code> rows in a MySQL table from a Python script
* How to <code>INSERT</code> rows in a MySQL table from a Python script 
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment
### Background Context
* In this project, you will link two amazing worlds: Databases and Python!
* In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.
* In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).
* The biggest difference is: no more SQL queries! 
* Indeed, the purpose of an ORM is to abstract the storage to the usage. 
* With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. 
* You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. 
* You will be able to change your storage easily without re-writing your entire project.
## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Your files will be executed with MySQLdb version 2.0.x
* Your files will be executed with SQLAlchemy version 1.4.x
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation 
* (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").
* MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s 
* the purpose of the module, class or method (the length of it will be verified)
* You are not allowed to use execute with sqlalchemy

## Tasks
### 0. Get all states
### Write a script that lists all states from the database hbtn_0e_0_usa:
* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
### 1. Filter states
### Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
### 2. Filter states by user input
### Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
* Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* You must use format to create the SQL query with the user input
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
### 3. SQL Injection...
### Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
* What? Empty?
* Yes, it’s an SQL injection to delete all records of a table…
* Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. 
* But this time, write one that is safe from MySQL injections!
* Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
### 4. Cities by states
### Write a script that lists all cities from the database hbtn_0e_4_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* You can use only execute() once
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
### 5. All cities by state
### Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
* Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* You can use only execute() once
* The results must be displayed as they are in the example below
* Your code should not be executed when imported
### 6. First state model
### Write a python file that contains the class definition of a State and an instance Base = declarative_base():
* State class:
     * inherits from Base Tips
     * links to the MySQL table states
     * class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
     * class attribute name that represents a column of a string with maximum 128 characters and can’t be null
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306
* WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
### 7. All states via SQLAlchemy
### Write a script that lists all State objects from the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* The results must be displayed as they are in the example below
* Your code should not be executed when imported
### 8. First state
### Write a script that prints the first State object from the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* The state you display must be the first in states.id
* You are not allowed to fetch all states from the database before displaying the result
* The results must be displayed as they are in the example below
* If the table states is empty, print Nothing followed by a new line
* Your code should not be executed when imported
### 9. Contains `a`
### Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* The results must be displayed as they are in the example below
* Your code should not be executed when imported
### 10. Get a state
### Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
* Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* You can assume you have one record with the state name to search
* Results must display the states.id
* If no state has the name you searched for, display Not found
* Your code should not be executed when imported
### 11. Add a new state
### Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Print the new states.id after creation
* Your code should not be executed when imported
### 12. Update a state
### Write a script that changes the name of a State object from the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Change the name of the State where id = 2 to New Mexico
* Your code should not be executed when imported
### 13. Delete states
### Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Your code should not be executed when imported
### 14. Cities in state
### Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
* City class:
       * inherits from Base (imported from model_state)
       * links to the MySQL table cities
       * class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
       * class attribute name that represents a column of a string of 128 characters and can’t be null
       * class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
* You must use the module SQLAlchemy
### Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
* Your code should not be executed when imported
### 15. City relationship
### Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:
* City class:
      * No change
* State class:
      * In addition to previous requirements, the class attribute cities must represent a relationship with the class City. 
      * If the State object is deleted, all linked City objects must be automatically deleted. 
      * Also, the reference from a City object to his State should be named state
* You must use the module SQLAlchemy
### Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306
* You must use the cities relationship for all State objects
* Your code should not be executed when imported
### 16. List relationship
### Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* The connection to your MySQL server must be to localhost on port 3306
* You must only use one query to the database
* You must use the cities relationship for all State objects
* Results must be sorted in ascending order by states.id and cities.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
### 17. From city
### Write a script that lists all City objects from the database hbtn_0e_101_usa
* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306
* You must use only one query to the database
* You must use the state relationship to access to the State object linked to the City object
* Results must be sorted in ascending order by cities.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported

| Task | File |
| ---- | ---- |
| 0. Get all states | [0-select_states.py](./0-select_states.py) |
| 1. Filter states | [1-filter_states.py](./1-filter_states.py) |
| 2. Filter states by user input | [2-my_filter_states.py](./2-my_filter_states.py) |
| 3. SQL Injection... | [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) |
| 4. Cities by states | [4-cities_by_state.py](./4-cities_by_state.py) |
| 5. All cities by state | [5-filter_cities.py](./5-filter_cities.py) |
| 6. First state model | [model_state.py](./model_state.py) |
| 7. All states via SQLAlchemy | [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) |
| 8. First state | [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) |
| 9. Contains `a` | [9-model_state_filter_a.py](./9-model_state_filter_a.py) |
| 10. Get a state | [10-model_state_my_get.py](./10-model_state_my_get.py) |
| 11. Add a new state | [11-model_state_insert.py](./11-model_state_insert.py) |
| 12. Update a state | [12-model_state_update_id_2.py](./12-model_state_update_id_2.py) |
| 13. Delete states | [13-model_state_delete_a.py](./13-model_state_delete_a.py) |
| 14. Cities in state | [model_city.py](./model_city.py), [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) |
| 15. City relationship | [relationship_city.py](./relationship_city.py), [relationship_state.py](./relationship_state.py), [100-relationship_states_cities.py](./100-relationship_states_cities.py) |
| 16. List relationship | [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py) |
| 17. From city | [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py) |

## Author's: Mekonen Abera, Addis Ababa, Ethiopia

