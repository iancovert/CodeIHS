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

- Class definitions require a constructor (the __init__() function)
- Important distinction between a class and an instance
- Created using the keyword **class**
- When referring to properties of the object, use keyword self
- Pointers: strings, ints, floats are different than all other objects in python. You've been using pointers when working with arrays without even realizing it. The assignment operator `=` makes a variable point to a new memory location, other operations either change data at an old location, or put data into a new one.

## Run time

#### Definition

An algorithm's run time is the number of computational steps it takes to reach a result. For example, for a search algorithm, the run time would be the number of computational steps until the target is located, or until it is certain that the target is not in the list.

#### Run time as a function of input size

The convention is to consider run time to be a function of the number of elements in a list. We might say, for example, that a search algorithm requires f(n) = 3 * n computational steps.

#### Best case, worst case or average case?

Algorithms don't always have a fixed run time, even given an input of fixed size. For a list of size n = 100, a search algorithm could complete after 3 steps, or after 300 steps. So how do we report run time? **Engineers are in the business of giving guarantees, so we resort to the worst case run time.**

#### Big-Oh notation

The number of computation steps required by an algorithm in the worst case is going to be some function f(n), but we do not directly report f(n) directly. The function f(n) can be hard to determine exactly, and the details generally aren't necessary. Instead, we report the Big-Oh run time, which is a simplification of f(n). The following are some examples of how we might transform certain functions to their Big-Oh run times.

- f(n) = 3n = O(n)
- f(n) = 6n<sup>2</sup> + 5n = O(n<sup>2</sup>)
- f(n) = 2<sup>n</sup> + n + 5 = O(2<sup>n</sup>)
- f(n) = log n + 100 = O(log n)
- f(n) = 10 = O(1)

The general rule is we **omit constant coefficients**, and we ignore everything except the **most dominant term**.

## Search algorithms

For simplicity, consider the scenario where we have a list containing a sequence of n ints. The methods we describe can be generalized to other data types (including strings and objects).

### Sequential search

What's the first thing you would try when searching for an int in a list of ints? Look at the one at a time! That's the logic behind sequential search. 

#### Definition of pseudocode

When we want to show some code, but care more about the logic behind it than the syntax, we sometimes want to write something closer to English. Pseudocode is a loosely defined halfway point between code and natural language. It does not follow the same syntax rules as Python or any other programming language.

#### Pseudocode for sequential search

    for each element in list:
	    if element is target:
		    return true
    return false

#### Running time

In the worst case, every element of the list will be checked. The worst case run time is O(n).

### Binary search

Imagine now that our list contains elements in sorted order. We can take advantage of the fact that elements are in order to perform our search more efficiently.

First, let's get some intuition for how this algorithm works. Think of how you search for a word in the dictionary. 

When there's a word you want to find in the dictionary, what do you do? Open a page (perhaps in the middle, perhaps at random), and then depending on whether the word you're looking for appears before or after the words on the page you opened to, you open another page either to the left or to the right of the original page. You can do this over and over until you hone in on the correct page that contains the word you were looking for.

In the scenario where we have a list of ints, we can do the same thing. 

#### Pseudocode for binary search

    min = 0 # The elements at min - 1, min - 2, ... are infeasible
    max = n # The elements at max, max + 1, ... are infeasible
    while (min != max):
	    mid = floor( (min + max) / 2)
	    if (list[mid] < target):
		    min = mid + 1
	    elif (list[mid] > target):
		    max = mid
	    else:
		    return mid
    return not found

#### Running time

Consider a scenario where the target element is not in the list. The algorithm terminates when the region where the element might reside becomes just a single element (only then can the algorithm be sure that the target is not in the list).

Let's call the *feasible region* the region of the list where the element might reside. Initially, the whole list is the feasible region. After checking the midpoint, either the left half or the right half (minus the middle element) becomes the feasible region. Etc.

To see how many iterations it takes for the feasible region to become just one element, let's look at an example. 

Consider a list with 31 elements. Before the first iteration, the feasible region contains 31 elements. After one iteration, it contains 15. After two iterations, it contains 7. After three iterations, it contains 3. After four iterations, it contains 1. After five iterations, the algorithm concludes that the target is not in the list. 

So for a list with 31 elements, it takes 5 iterations for the algorithm to terminate. Basically, this is log<sub>2</sub>(31). 

We write the run time as O(log n).

## Sorting algorithms

We stick with the scenario where we have a list of n ints. Again, our methods can be generalized to other data types.

### Selection sort

One idea for a sorting algorithm is to find the smallest element and put it at the first spot on the left. Then, locate the second smallest element, and put it at the second spot on the left. Etc.

#### Pseudocode for selection sort

    for i in range(n):
	    min = inf
	    target = -1
	    for j in range(i, n):
		    if list[j] < min:
			    min = list[j]
			    target = j
	    # Swap elements at i and target
	    temp = list[i]
	    list[i] = list[target]
	    list[target] = temp

#### Run time

To get at the run time, consider how many times we compare two elements (line 5). In the first iteration we do n comparisons. In the second iteration we do n - 1 comparisons. In the third we do n - 2 comparisons. Etc. In total, there are (n + 1) * n / 2 comparisons. We conclude that the run time is O(n<sup>2</sup>).

### Insertion sort

We examine elements one at a time, and slide each element to its left until its neighbor on the left is smaller than it. If we do this for the elements at indices 1, 2, ... n - 1, we end up with the list in sorted order.

#### Pseudocode for insertion sort

    for i in range(1, len(l)):
	    j = i
	    val = l[i]
	    # While the neighbor to the left is smaller
	    while (j > 0 and val > l[j - 1]):
		    l[j] = l[j - 1]
		    j = j - 1
	    l[j] = val

#### Run time

In the best case, when the list begins in sorted order, the run time is O(n).

In the worst case, the performance is the same as selection sort, O(n<sup>2</sup>).

### Other sorting algorithms

There are many other sorting algorithms, including several that achieve a better running time than O(n<sup>2</sup>). In practice, we would always use one of those over insertion sort or selection sort. We won't look at alternative methods because they're more complicated, and it's not our main goal here. We just want to introduce you to two possible algorithms.

### Conclusions on searching and sorting algorithms

Algorithm design is an important part of computer science. You can take an entire class on this subject!

Searching and sorting are two tasks that programmers want to perform a lot. Particularly in situations where programmers are working with a lot of data (n = 1,000,000), it's important that these tasks are attacked with efficient algorithms.

## Data structures

#### Definition

Data structures are tools for organizing and storing data. You've already seen your first data structure: the list.

#### Why we need them

When we have many pieces of data, we need to put it in a data structure. Our choice of data structure is motivated by the kinds of routines we want to perform with our data. Perhaps we want to be able to search our data efficiently. Or perhaps we want to efficiently locate the first or last piece of data inserted into the data structure.

Different data structures are optimized for different operations. All data structures must at least support insertion and removal of data. While data structures work with just about any data type, we tend to restrict them to one data type at a time (i.e. just ints, or just bank account objects). 

## Stacks

### Description

Think of a stack of plates. You put plates into the stack by stacking them on top of each other. When you want to remove a plate, you can only remove the one at the top.

The data structure called stack is very similar. It supports two main operations: inserting and removing elements.

Each time an element is removed, it is the element that was inserted most recently. For this reason, stacks are said to follow the last-in-first-out (LIFO) principle.

### Implementation

A stack can be implemented as an object with a list as one of the underlying attributes. It requires just one class.

### Some operations and run times

- O(1) insertion
- O(1) removal
- O(1) check if empty

## Queues

### Description

A queue is like a line. People enter a line by going behind everyone else. As long as no one gives up their spot, the first person to be removed is always at the front of the line.

The data structure called queue is very similar. It supports two main operations: inserting and removing elements. 

Each time an element is removed, it is the element that was inserted first. For this reason, queues are said to follow the first-in-first-out (FIFO) principle.

### Implementation

We won't discuss queue implementations.

### Some operations and run times

- O(1) insertion
- O(1) removal
- O(1) check if empty

### Extra: P versus NP
All of the above falls into the category of P, which means polynomial time. Polynomials are expressions of the form: f(x) = x<sup>a</sup> + x<sup>b</sup> + ...

All this means is that the algorithms we have talked about are O(n<sup>b</sup>) where b is some number. But in practise there are things that grow more quickly than any power of n, some of these we call NP, one example would be O(2<sup>n</sup>). If you're interested in the ongoing and open problem of P and NP I would recommend the following video: <https://www.youtube.com/watch?v=YX40hbAHx3s>

## Lab 3

### Part 1

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