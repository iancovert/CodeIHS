# Day 1

For the first lesson, we show you how to write your first program, and we introduce you to the important data types in Python. 

## Basic introduction

We begin by showing you how to write a very simple program. Even without knowing Python, you'll be able to guess what the program does. 

Our goal here is to introduce you to the novel concept of writing code. We'll answer several questions you may have been wondering about. What is a program? Where do I write a program? Is a file containing a program a special kind of file? What does it mean to run a program? Will my program produce an output that's visible to the user?

### Demonstrations

- Writing a program in a text editor and running it in the terminal
- Using the interpreter
- Using our preferred Python integrated development environment (IDE), PyCharm

### Useful terminal commands

- pwd: present working directory
- ls: list files in current directory
- ls -al: list all files with additional details
- python3: open python interpreter
- python3 script.py: run python program called script

## Data types

We introduce variables, and the intuitive idea of value assignment. We also introduce several data types, which are the kinds of content variables can hold. We also discuss some of the operations associated with each data type. 

### Data types introduced

- ints and floats (numerical data)
- booleans
- strings
- lists

### Mathematical operators for ints and floats

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Remainder (%)

### Comparison operators for ints and floats

- Less than (<)
- Less than or equal (<=)
- Greater than (>)
- Greater than or equal (>=)
- Equal (==)
- Not equal (!=)

### Logical operators for boolean variables

- and (combines two operands)
- or (combines two operands)
- not (negates a single operand)

### Notes on strings

- Can be created using 'single quotes' or "double quotes"
- Not to be confused with numerical data types, even strings such as '3'
- Strings can be concatenated using + operator
- To concatenate an int or float, convert to string using str()
- Substrings can be obtained using [] operator
- There are many other string operations

### Lists

- Contain a sequence of elements, possibly of different data types
- They're zero indexed
- Elements are accessed using [] operator
- There are many other list operations

## Easy, useful tool for your lab

Use input() to get user input.

## Lab 1

In this lab, you'll write a program that generates a short paragraph about the user.

The program must ask for user input, and make use of several of the data types and operations discussed in class today.

Follow these steps:

- Collect four pieces of user input: the user's name, number of brothers, number of sisters, and city of origin
- If applicable, convert those inputs to a reasonable data type
- Calculate the number of siblings
- Calculate the percentage of brothers and the percentage of sisters (rounded to the nearest integer)
- Calculate the number of vowels in the name of the user's city of origin (hint: convert the city name to lowercase first)
- Calculate the percentage of vowels in the name of the user's city of origin (rounded to the nearest integer)

Finally, print the output using these lines exactly:

    print('Hello, my name is ' + name)
    print('My name is ' + str(name_length) + ' letters long')
    print('I have ' + str(siblings) + ' siblings (' + str(perc_sisters) + ' % sisters and ' + str(perc_brothers) + ' % brothers)')
    print("I'm from " + city_from)
    print("My city's name contains " + str(city_vowels) + ' vowels')
    print("That's " + str(percentage_vowels) + ' % vowels')