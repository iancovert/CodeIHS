# Day 2

Today we introduce control flow, functions and objects. We also discuss the concept of scope.

## Control flow

The simplest scripts contain a sequence of instructions, written one line at a time, and each line gets executed one after the other. But sometimes we may want to skip several lines of code; sometimes we'll want to repeat several lines of code a fixed number of times.

Control flow is the concept of telling the computer which line to execute next. The tools we discuss in this section will enable us to make much more powerful programs.

### Control flow tools

- If statements (execute code only under certain conditions)
- For loops (iterate a fixed number of times, or iterate through a list of items)
- While loops (continue executing until a condition is satisfied)

### Notes on control flow tools 
- If statements and while loops both rely on **boolean expressions** (see day 1 notes)
- For loops rely instead on a **list**, and each iteration corresponds to an element in the list.
- Be careful with indentation. Always use the tab key to maintain alignment.

## Functions

Several lines of code can be encapsulated and made into a routine, called a function. A function can be **called**, and all the code that defines the function will be executed. The function can be called with arguments, which change how it runs each time.

Consider a routine that takes a number, and determines if the number is prime. Wouldn't it be nice if we had a function called prime, so we could write  prime(17) and have the function return True? Functions are very useful for this kind of thing.

### Example functions:

    def square(arg):
        ''' Do something '''
        val = arg * arg
        ''' Return a value '''
        return val
    
    x = square(5)
    # x now has the value 25
    
    def hello():
        ''' The function does not need to take an argument '''
        print('Hello world')
        ''' The function does not need to return a value '''
    
    hello()
    # The program would now print Hello World

### Notes on functions

- Created using the keyword **def**
- Can take multiple arguments, and arguments can have names of your choice
- Last line often uses keyword return to pass a value to the caller of the function
- Be careful with indentation



# Lab 2

## Part 1

First, we're going to practice writing functions. Write a function called prime, that determines if a number is prime.

Hints:

- How many arguments should the function take?
- What kind of value should it return?
- How can you figure out if a number is prime? By checking all its possible factors!
- Use the remainder operator from last class (%)

Here's how we might want to use our function:

    numbers = [4, 5, 7, 13, 99]
    for num in numbers:
        result = prime(num)
        print(result)

The program should print:

    False
    True
    True
    True
    False