# Day 3

We'll discuss classes and objects in Python. A *class* can be thought of as a blueprint, or description, of a thing. An *object* is an instance of that thing.  For example, there can be a car class, and then there can be multiple instances of that class: Pierre's car, Sumner's car, etc.

## Objects

Wouldn't it be nice if we could define our own data types? We would be able to make things that are more complicated than just a number or a True/False value. That's what objects are for.

Think of an object as a real life thing, like a bank account. A bank account has **information associated with it**, such as the owner, the account number, and the account balance. It also has **routines associated with it**, such as depositing and withdrawing money. 

Objects in Python are similar. They are things that have data and routines associated with them. They are a bit like containers that hold variables and functions.

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

- Class definitions require a constructor, which is the **\_\_init\_\_()** function
- There's a distinction between a class and an object (a blueprint versus an instance of that thing)
- Created using the keyword **class**
- When referring to properties of the class, use keyword **self**

### Notes on pointers

Strings, ints, floats are different than all other objects in python. You've been using pointers when working with lists without even realizing it. The assignment operator `=` makes a variable point to a new memory location, other operations either change data at an old location, or put data into a new one.

## Lab 3

We're going to practice making objects. We'll make an object that's like a shopping cart. Our shopping cart will be very simple, and will allow you to put items in and take items out. In addition to keeping track of the items in the basket, the class will also record each item's price, and the total price of the items in the cart.

Guidelines:

- Make a class called Cart.
- The class should have three attributes: items (a list), prices (a list), and total (a float).
- Write a function called **addItem()** that adds an item to the cart. The new item should be added to the list of items, its price should be added to the list of prices, and the total amount should be increased.
- Write a function called **removeItem()** that removes an item from the cart. The item should be removed from the list of items, its price should be removed from the list of prices, and the total amount should be decreased.
- Write a function called **summary()** that prints the items in the cart, as well as the total amount.

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
