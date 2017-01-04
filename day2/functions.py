# A simple function that prints something, and returns nothing
def hello():
	print('Hello world')

hello()

# A function that always returns the value 5
def five():
	return 5

# When calling it, assign the return value to a variable
x = five()
print(x)

# A function that takes an argument, and simply returns the argument
def useless(n):
	return n

y = useless('This function just returns the argument you pass to it')
print(y)

# A function that takes the argument, does something with it, and returns
# a value
def square(n):
	val = n * n
	return(val)

z = square(5)
print(z)

# A function that takes a list of numbers (floats or ints) and calculates and 
# returns the average
def average(num_list):
	total = 0
	for num in num_list:
		total += num
	return total / len(num_list)

a = average([1, 2, 3, 4, 5, 11, 23, 56, 78])
print(a)

# A function that reverses the order of elements in a list. Note that the list
# is not returned. Nothing is returned. What does that tell us about how lists
# work in Python?
def reverse_list(my_list):
	n = len(my_list)
	for i in range(n // 2):
		temp = my_list[i]
		my_list[i] = my_list[n - i - 1]
		my_list[n - i - 1] = temp
	# Don't return a value

b = [1, 2, 3, 4, 5]
print(b)
reverse_list(b)
print(b)