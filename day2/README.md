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

## Objects

Wouldn't it be nice if we could define our own data types? We would be able to make things that are more complicated than just a number or a True/False value. That's what objects are for.

Think of an object as a real life thing, like a bank account. A bank account has **information associated with it**: an owner, an account number, and an account balance. It also has **routines associated with it**: depositing and withdrawing. 

Objects in Python are similar. They are things that have data and routines associated with them. More concretely, they are like containers that hold variables and functions.

### Example object

    class Computer:
        def __init__(self, owner):
            self.owner = owner
            self.ison = False

        def toggle_power(self):
            if self.ison:
                self.ison = False
            else:
                self.ison = True

        def print_owner(self):
            print(self.owner)

### Notes on objects

- Class definitions require a constructor (the __init__() function)
- Important distinction between a class and an instance
- Created using the keyword **class**
- When referring to properties of the object, use keyword self
- Pointers: strings, ints, floats are different than all other objects in python. You've been using pointers when working with arrays without even realizing it

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

## Part 2

Now we're going to practice making objects. We're going to make an object that's like a shopping cart. Our shopping cart will be very simple, and will allow you to put items in and take items out. In addition to keeping track of the items in the basket, the class will also record each item's price, and the total price of the items in the cart.

Guidelines:

- Make a class called Cart
- The class should have three attributes: items (a list), prices (a list), and total (a float)
- Write a function called addItem() that adds an item to the cart. The new item should be added to the list of items, its price should be added to the list of prices, and the total amount should be increased
- Write a function called removeItem() that removes an item from the cart. The item should be removed from the list of items, its price should be removed from the list of prices, and the total amount should be decreased
- Write a function called summary() that prints the items in the cart, as well as the total amount

Here's how we might test our new class:

    cart = Cart()
    cart.addItem('apples', 3)
    cart.addItem('pasta', 2)
    cart.addItem('crackers', 4)
    cart.addItem('oranges', 3)
    cart.removeItem('apples')
    cart.summary()

We would want to see the following output:

    The shopping cart contains:
    pasta
    crackers
    oranges
    Total: 9