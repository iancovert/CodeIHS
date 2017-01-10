'''
	Exercise 1: iterating through lists
	
	Write three different functions, each of which print out every element of a
	list on its own line. Hint: use for loops for two of them, and a while loop
	for one. The outputs should look exactly the same!
'''

def printList1(my_list):
	for item in my_list:
		print(item)

def printList2(my_list):
	for i in range(len(my_list)):
		print(my_list[i])

def printList3(my_list):
	i = 0
	while (i < len(my_list)):
		print(my_list[i])
		i = i + 1


list1 = [1, 3, 5, 7, 9]
list2 = ['Print', 'me', 'out', 'one', 'line', 'at', 'a', 'time']

printList1(list1)
printList1(list2)

printList2(list1)
printList2(list2)

printList3(list1)
printList3(list2)


'''
	Exercise 2: counting positive numbers

	Write a function that takes a list of numbers, and counts how many of the
	numbers are positive (greater than zero)
'''

def numPositive(my_list):
	count = 0
	for item in my_list:
		if item > 0:
			count = count + 1
	return count


list1 = [1, -1, 6, -6, -9, 9, 0, 2]
list2 = list(range(-5, 5, 1))

print(numPositive(list1))
print(numPositive(list2))


'''
	Exercise 3: how far into a list is the first negative number?

	Write a function that takes a list of numbers, and counts how far into the
	list the first negative number appears. For example, in the list 
	[3, 2, 1, 0, -1], the first negative number appears at index 4. Return the
	index at which the first negative number appears. Hint: consider using a
	while loop
'''

def firstNegative(my_list):
	i = 0
	while (i < len(my_list)):
		if my_list[i] < 0:
			return i
		else:
			i = i + 1
	# If the list contains no negative numbers, return the length of the list
	return i


list1 = [1, 1, 1, -1, 1, -1, -1]
list2 = list(range(5, -5, -1))

print(firstNegative(list1))
print(firstNegative(list2))

'''
	Exercise 4: simulating coin flips

	The function random() simulates a number between 0 and 1. round(random())
	results in a random number that is 0 half the time, and 1 half the time -
	like flipping a coin.

	Let's say that 0 is tails and 1 is heads.

	Use this tool to simulate flipping a coin, and write a function that counts
	the number of flips until you get a head. Each time you call the function,
	a new set of coin flips should be simulated. Hint: use a while loop
'''

from random import random

# Notice how each time you call the function, you get a different result
print(round(random()))
print(round(random()))
print(round(random()))


def countFlips():
	flip = 0
	count = 0
	while (flip == 0):
		flip = round(random())
		count = count + 1
	return count


print(countFlips())
print(countFlips())
print(countFlips())