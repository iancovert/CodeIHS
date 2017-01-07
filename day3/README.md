# Day 3

First we will talk about creating custom objects to handle the algorithms and data structures we will see in the rest of the class. Then we will discuss algorithms for searching and sorting, and finally transition into data structures.

We examine possible sorting and searching algorithms to emphasize an important insight for all new programmers: whereas you may have some intuition for how to perform tasks like searching or sorting, particularly with a small number of objects, in the world of code these tasks require algorithms. Algorithms require precise logic. When comparing candidate algorithms, we prefer the one that is fastest.

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

- Class definitions require a constructor (the **\_\_init\_\_()** function)
- Important distinction between a class and an instance
- Created using the keyword **class**
- When referring to properties of the object, use keyword **self**
- Pointers: strings, ints, floats are different than all other objects in python. You've been using pointers when working with arrays without even realizing it. The assignment operator `=` makes a variable point to a new memory location, other operations either change data at an old location, or put data into a new one.

## Lab 3

We're going to practice making objects. We'll make an object that's like a shopping cart. Our shopping cart will be very simple, and will allow you to put items in and take items out. In addition to keeping track of the items in the basket, the class will also record each item's price, and the total price of the items in the cart.

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
