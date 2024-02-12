# Project: 0x12. JavaScript - Warm up

## Resources

#### Read or watch:

* [Writing JavaScript Code](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
* [Variables](https://intranet.alxswe.com/rltoken/zgOWmcpVLZFEmFlmuwayyg)
* [Data Types](https://intranet.alxswe.com/rltoken/VPd6JWaLrwOBzjAeXNAEqg)
* [Operators](https://intranet.alxswe.com/rltoken/3HLjEesLsmyWfRUWnxgUGg)
* [Operator Precedence](https://intranet.alxswe.com/rltoken/PHtcJJk30gBNmlFQ9R4RVg)
* [Controlling Program Flow](https://intranet.alxswe.com/rltoken/tsreKcNh_KmTmLPHsfvJRw)
* [Functions](https://intranet.alxswe.com/rltoken/e3EfHIxICdIncGBwwIDbXQ)
* [Objects and Arrays](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
* [Intrinsic Objects](https://intranet.alxswe.com/rltoken/jg7IbvJpV2oLIKgqOAQH1g)
* [Module patterns](https://intranet.alxswe.com/rltoken/g-MgvO09Ur02RhM63gVyXw)
* [var, let and const](https://intranet.alxswe.com/rltoken/gJi61GeJTRX0g-M0Rx-0Iw)
* [JavaScript Tutorial](https://intranet.alxswe.com/rltoken/Y8hkOcy5jO22lQGyF6_NiA)
* [Modern JS](https://intranet.alxswe.com/rltoken/NZawtiBjWUpiojnrtVywNw)
## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between <code>var</code>, <code>const</code> and <code>let</code>
* What are all the data types available in JavaScript
* How to use the <code>if</code>, <code>if ... else</code> statements
* How to use comments
* How to affect values to variables
* How to use <code>while</code> and <code>for</code> loops
* How to use <code>break</code> and <code>continue</code> statements
* What is a function and how do you use functions
* What does a function that does not use any <code>return</code> statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

### Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant (version 16.x.x). 
* Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc

## Tasks
### 0. First constant, first print
### Write a script that prints “JavaScript is amazing”:
* You must create a constant variable called myVar with the value “JavaScript is amazing”
* You must use console.log(...) to print all output
* You are not allowed to use var

### 1. 3 languages
### Write a script that prints 3 lines:
* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use console.log(...) to print all output
* You are not allowed to use var
### 2. Arguments
### Write a script that prints a message depending of the number of arguments passed:
* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use console.log(...) to print all output
* You are not allowed to use var
### Reference: process.argv
### 3. Value of my argument
### Write a script that prints the first argument passed to it:
* If no arguments are passed to the script, print “No argument”
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use length
### 4. Create a sentence
### Write a script that prints two arguments passed to it, in the following format: “ is ”
* You must use console.log(...) to print all output
* You are not allowed to use var
### 5. An Integer
### Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
* If the argument can’t be converted to an integer, print “Not a number”
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use try/catch
### 6. Loop to languages
### Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use console.log(...) to print all output
* You are not allowed to use var
* You are not allowed to use any if/else statement
* You can use only one console.log
* You must use a loop (while, for, etc.)
### 7. I love C
### Write a script that prints x times “C is fun”
* Where x is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use console.log(...) to print all output
* You are not allowed to use var
* You can use only two console.log
* You must use a loop (while, for, etc.)
### 8. Square
### Write a script that prints a square
* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character X to print the square
* You must use console.log(...) to print all output
* You are not allowed to use var
* You must use a loop (while, for, etc.)
### 9. Add
### Write a script that prints the addition of 2 integers
* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: function add(a, b)
* You must use console.log(...) to print all output
* You are not allowed to use var
### 10. Factorial
### Write a script that computes and prints a factorial
* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of NaN is 1
* You must do it recursively
* You must use a function
* You must use console.log(...) to print all output
* You are not allowed to use var
### 11. Second biggest!
### Write a script that searches the second biggest integer in the list of arguments.
* You can assume all arguments can be converted to integer
* If no argument passed, print 0
* If the number of arguments is 1, print 0
* You must use console.log(...) to print all output
* You are not allowed to use var
### 12. Object
### Update this script to replace the value 12 with 89:
* You are not allowed to use var
### 13. Add file
### Write a function that returns the addition of 2 integers.
* The function must be visible from outside
* The name of the function must be add
* You are not allowed to use var
### 14. Const or not const
### Write a file that modifies the value of myVar to 333
### 15. Call me Moby
### Write a function that executes x times a function.
* The function must be visible from outside
* Prototype: function (x, theFunction)
* You are not allowed to use var
### 16. Add me maybe
### Write a function that increments and calls a function.
* The function must be visible from outside
* Prototype: function (number, theFunction)
* You are not allowed to use var
### 17. Increment object
### Update this script by adding a new function incr that increments the integer value.
* You are not allowed to use var

| Task | File |
| ---- | ---- |
| 0. First constant, first print | [0-javascript_is_amazing.js](./0-javascript_is_amazing.js) |
| 1. 3 languages | [1-multi_languages.js](./1-multi_languages.js) |
| 2. Arguments | [2-arguments.js](./2-arguments.js) |
| 3. Value of my argument | [3-value_argument.js](./3-value_argument.js) |
| 4. Create a sentence | [4-concat.js](./4-concat.js) |
| 5. An Integer | [5-to_integer.js](./5-to_integer.js) |
| 6. Loop to languages | [6-multi_languages_loop.js](./6-multi_languages_loop.js) |
| 7. I love C | [7-multi_c.js](./7-multi_c.js) |
| 8. Square | [8-square.js](./8-square.js) |
| 9. Add | [9-add.js](./9-add.js) |
| 10. Factorial | [10-factorial.js](./10-factorial.js) |
| 11. Second biggest! | [11-second_biggest.js](./11-second_biggest.js) |
| 12. Object | [12-object.js](./12-object.js) |
| 13. Add file | [13-add.js](./13-add.js) |
| 14. Const or not const | [100-let_me_const.js](./100-let_me_const.js) |
| 15. Call me Moby | [101-call_me_moby.js](./101-call_me_moby.js) |
| 16. Add me maybe | [102-add_me_maybe.js](./102-add_me_maybe.js) |
| 17. Increment object | [103-object_fct.js](./103-object_fct.js) |

# Author: Mekonen Abera

