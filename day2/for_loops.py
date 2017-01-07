# CONCEPT: control flow
# It's okay writing out instructions one by one...
x = 'Print me five times'
print(x)
print(x)
print(x)
print(x)
print(x)

# But it wastes time and space! Is there a faster way to do it?

# CONTROL FLOW TOOL: for loops
for i in range(7):
	print('Print me seven times')

for i in range(10):
	print(i)

# NOTE: be very careful with indentation. Use one tab for each line inside
# the loop

# How does this work?
x = range(10)
print(list(x))
# Range(n) creates a list. In our for loops, i takes on the values 0, 1,
# 2, 3, ... in each iteration of the loop.

# NOTE: notice that the last value, 10, was omitted. That's because of how
# range() works

# A for loop will iterate over any kind of list, even if it's not a list of
# ints, such as a list of strings
words = ['Parlez', 'vous', 'francais', 'mon', 'ami', '?']
for word in words:
	print(word)

# If you have a list of items you want to iterate over, there are two ways
# to do it. The way above, or by using numerical indices
for i in range(len(words)):
	print(words[i])

# Another for loop example
people = ['mother', 'father', 'sister', 'brother']
numbers = [5, 4, 2, 3]
for i in range(len(people)):
	print('My ' + people[i] +  ' gave me ' + str(numbers[i]) + ' presents')

# Another example: what's the sum of the numbers 1, 2, ... 100?
total = 0
for i in range(1, 101):
	total = total + i
print(total)

# Another example: what about the numbers 100, 101, ... 200?
# The function called range() is flexible. You can define a different starting
# point than 0
total = 0
for i in range(100, 201):
	total = total + i
print(total)

# Another example: what about the numbers 1000, 1002, 1004, ... 2000?
# You can even define different step sizes
total = 0
for i in range(1000, 2001, 2):
	total = total + i
print(total)
