# Project: 0x0D. SQL - Introduction

# Author: Mekonen Abera

## Resources

#### Read or watch:

* [What is Database & SQL?](https://intranet.alxswe.com/rltoken/yyRKTEdRkYEVlRgZPbasjw)
* [A Basic MySQL Tutorial](https://intranet.alxswe.com/rltoken/sV2PtK5YfQsXWW1malRZ5Q)
* [Basic SQL statements: DDL and DML](https://intranet.alxswe.com/rltoken/IUKo4-UaRZSKPvXr5u9oBw)
* [Basic queries: SQL and RA](https://intranet.alxswe.com/rltoken/rXKvu2u7vg1Hj6bnX7UgMg)
* [SQL technique: functions](https://intranet.alxswe.com/rltoken/-Riv_dzSYsJyvy-LlaO6Mg)
* [SQL technique: subqueries](https://intranet.alxswe.com/rltoken/QpIXoR--8eBIaidgSWYsBQ)
* [What makes the big difference between a backtick and an apostrophe?](https://intranet.alxswe.com/rltoken/Gt0nFJPJRwW2Y0izzwbVrw)
* [MySQL Cheat Sheet](https://intranet.alxswe.com/rltoken/1oU1LwCksQLXjs6fZYezrw)
* [MySQL 8.0 SQL Statement Syntax](https://intranet.alxswe.com/rltoken/HmdmLiYBM0Q34iCYPWd9XQ)
* [installing MySQL in Ubuntu 20.04](https://intranet.alxswe.com/rltoken/IpYI9rgbwfjxOAQQgpHCmQ)
## Learning Objectives

### General

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does <code>DDL</code> and <code>DML</code> stand for
* How to <code>CREATE</code> or <code>ALTER</code> a table
* How to <code>SELECT</code> data from a table
* How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data
* What are <code>subqueries</code>
* How to use MySQL functions

### Requirements
## General
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc
## Tasks
## 0. List databases
* Write a script that lists all databases of your MySQL server.
## 1. Create a database
* Write a script that creates the database hbtn_0c_0 in your MySQL server.
* If the database hbtn_0c_0 already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements
## 2. Delete a database
### Write a script that deletes the database hbtn_0c_0 in your MySQL server.
* If the database hbtn_0c_0 doesn’t exist, your script should not fail
* You are not allowed to use the SELECT or SHOW statements
## 3. List tables
### Write a script that lists all the tables of a database in your MySQL server.
* The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)
## 4. First table
### Write a script that creates a table called first_table in the current database in your MySQL server.

* first_table description:
   * id INT
   * name VARCHAR(256)
* The database name will be passed as an argument of the mysql command
* If the table first_table already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements
## 5. Full description
### Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
* The database name will be passed as an argument of the mysql command
* You are not allowed to use the DESCRIBE or EXPLAIN statements
## 6. List all in table
### Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
* All fields should be printed
* The database name will be passed as an argument of the mysql command
## 7. First add
### Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
* New row:
* id = 89
* name = Best School
* The database name will be passed as an argument of the mysql command
## 8. Count 89
### Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
* The database name will be passed as an argument of the mysql command
## 9. Full creation
### Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
* second_table description:
    * id INT
    * name VARCHAR(256)
    * score INT
* The database name will be passed as an argument to the mysql command
* If the table second_table already exists, your script should not fail
* You are not allowed to use the SELECT and SHOW statements
* Your script should create these records:
    * id = 1, name = “John”, score = 10
    * id = 2, name = “Alex”, score = 3
    * id = 3, name = “Bob”, score = 14
    * id = 4, name = “George”, score = 8
## 10. List by best
### Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command
## 11. Select the best
### Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command
## 12. Cheating is bad
### Write a script that updates the score of Bob to 10 in the table second_table.
* You are not allowed to use Bob’s id value, only the name field
* The database name will be passed as an argument of the mysql command
## 13. Score too low
### Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
* The database name will be passed as an argument of the mysql command
## 14. Average
### Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
* The result column name should be average
* The database name will be passed as an argument of the mysql command
## 15. Number by score
### Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
* The result should display:
    * the score
    * the number of records for this score with the label number
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the mysql command
## 16. Say my name
### Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
* Don’t list rows without a name value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the mysql command
## 17. Go to UTF8
### Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
* You need to convert all of the following to UTF8:
     * Database hbtn_0c_0
     * Table first_table
     * Field name in first_table
## 18. Temperatures #0
### Import in hbtn_0c_0 database this table dump: download
* Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
## 19. Temperatures #1
### Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
* Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
## 20. Temperatures #2
### Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
* Write a script that displays the max temperature of each state (ordered by State name).

| Task | File |
| ---- | ---- |
| 0. List databases | [0-list_databases.sql](./0-list_databases.sql) |
| 1. Create a database | [1-create_database_if_missing.sql](./1-create_database_if_missing.sql) |
| 2. Delete a database | [2-remove_database.sql](./2-remove_database.sql) |
| 3. List tables | [3-list_tables.sql](./3-list_tables.sql) |
| 4. First table | [4-first_table.sql](./4-first_table.sql) |
| 5. Full description | [5-full_table.sql](./5-full_table.sql) |
| 6. List all in table | [6-list_values.sql](./6-list_values.sql) |
| 7. First add | [7-insert_value.sql](./7-insert_value.sql) |
| 8. Count 89 | [8-count_89.sql](./8-count_89.sql) |
| 9. Full creation | [9-full_creation.sql](./9-full_creation.sql) |
| 10. List by best | [10-top_score.sql](./10-top_score.sql) |
| 11. Select the best | [11-best_score.sql](./11-best_score.sql) |
| 12. Cheating is bad | [12-no_cheating.sql](./12-no_cheating.sql) |
| 13. Score too low | [13-change_class.sql](./13-change_class.sql) |
| 14. Average | [14-average.sql](./14-average.sql) |
| 15. Number by score | [15-groups.sql](./15-groups.sql) |
| 16. Say my name | [16-no_link.sql](./16-no_link.sql) |
| 17. Go to UTF8 | [100-move_to_utf8.sql](./100-move_to_utf8.sql) |
| 18. Temperatures #0 | [101-avg_temperatures.sql](./101-avg_temperatures.sql) |
| 19. Temperatures #1 | [102-top_city.sql](./102-top_city.sql) |
| 20. Temperatures #2 | [103-max_state.sql](./103-max_state.sql) |

