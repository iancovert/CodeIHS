# Day 4

Today we'll discuss data structures. We'll go over why we need them, discuss how we choose a data structure for a given problem, and implement a couple of data structures together.

## Data Structures

Data structures are, intuitively, any way of manipulating data efficiently on a computer. We discuss which data structures are best suited to various tasks by analyzing their speed (read *runtime*) and implementation. We will talk about three data structures today: 

- Stacks
- Linked Lists
- Trees

### Stacks
A stack is a data structure for when we only care about the most recent thing we put into the data structure. As such they must be able to efficiently add something, and then remove that thing. More precisely stacks implement what is called the First-in-Last-out principle, meaning if you put A, B, and C into a stack, then request three objects, you will first get C, then B, then A, at which point the stack is empty.

Example stack functions (notice that Python lists make it easy to implement these functions, but this isn't true in all programming languages):

```python
class Stack:
	def __init__(self):
		self.stack = []
	def push(self, item):
		"""
		Adds :item: to the top of the stack
		"""
		self.stack.append(item)
		
	def pop(self):
		"""
		Returns the item at the top of the stack and
		removes it from the stack
		"""
		return self.stack.pop()
```

### Linked List
A linked list is a data structure (admittedly more useful in languages other than python) which expands dynamically so that you can always add items to the front and end. 

In essense a linked list is an object which wraps a chain of nodes. Each node contains a pointer to a value (the item we want to store in the list) and a pointer to the *next* node in the chain.

We call the first object in the linked list the *head* and the last object the *tail*.

Here are some descriptions for how you would implement some of the functions for a linked list:

```python
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	def addToHead(self, item):
		# replace the head with the new node, if
		# a node was already the head, set the new head's next to
		# be equal to the old head
		# (if there's no head and no tail they become the same item)
		...
	def addToTail(self, item):
		# If there is a tail, make a new node for this item and make
		# it the new tail, then set the old tail's next to the new
		# tail node.
		# (if there's no head and no tail they become the same item)
		...
	def popFromHead(self, item):
		# Set the new head to be the current head's next
		# If the new head is None that means the list is empty, so
		# we should also set the tail to be None
		...
	def popFromTail(self, item):
		# Go through the linked list to find the node right before
		# the tail, set the tail to this node, clear the next of it,
		# and return the value of the old tail.
		...

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	def setNext(self, nextnode):
		self.next = nextnode
```

### Binary Trees
Binary Trees are a data structure which allows for much faster lookup. Essentially the idea is that instead of going linearly through a list to find the object in question you can instead search in log<sub>2</sub>(N) time. The construction is as follows:

```python
class Tree:
	def __init__(self):
		self.head = None
	def add(self, item):
		treenode = TreeNode(item)
		if self.head is None:
			self.head = treenode
		else:
			self.head.add(treenode)
	# Probably some remove/find stuff as well
	
class TreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
	
	def addToTree(self, treenode):
		if treenode.value <= self.value:
			# If the value you're adding is less than
			# this one: then put on the left
			if self.left is None:
				self.left = treenode
			else:
				self.left.addToTree(treenode)
		else:
			# Otherwise put it on the right
			if self.right is None:
				self.right = treenode
			else:
				self.right.addToTree(treenode)
```
The data is structured such that at a given tree node with value *x* we know that all values less than *x* are on the left of the tree node, and all values greater than *x* are on the right. 

Let's consider the number of comparisons necessary to find if a value *y* is in a tree of size N. At each *level* of the tree the number of nodes **doubles** (each node has a left and right *child*), thus the total number of nodes in a tree of *height* *h* (meaning number of levels) is equal to approximately 2<sup>h</sup>, therefore with N objects in the tree we know that the minimum height can be calculated by N = 2<sup>h</sup> and thus h = log<sub>2</sub>(N). So if we wanted to find if the item *y* exists in the tree we would need to check one comparison per level (to know if we need to go to the left or the right), and since there are about log<sub>2</sub>(N) levels, that means that determining if an item is in the tree takes log<sub>2</sub>(N) comparisons. This is much faster than in a list, where we would need to check if each element is equal to *y* and would therefore take N comparisons (once per element in the list). 

To see how much faster let's pretend we were searching through 1,000,000 elements. In a list that would mean a full million comparisons. In a balanced binary tree as we saw above it would take log<sub>2</sub>(1,000,000) ~ 20 comparisons. If we increased it to 1,000,000,000 it would take a billion comparisions in the list, but only log<sub>2</sub>(1,000,000) ~ 30 in the tree.

Notice these calculations are always for balanced binary trees, if you insert objects in the wrong order (like sorted order!) you can end up in a case where each inserted item is a *child* on one side of its *parent*, thus each parent only has one child and the tree looks a lot more like a linked list. Thus instead of taking log<sub>2</sub>(N) comparisons it will take N comparisons.