# What if we have a variable, and what we want to do next depends on the value
# of that variable? That's why we have if statements
x = 3
if (x > 1):
	print('x is larger than 1')

# NOTE: be careful with indentation

# NOTE: our boolean expression x > 1 produced a boolean value. We must always
# pass a boolean value to our if() statement. If the boolean value is True, the
# code will be executed. Otherwise it won't

# What if we want to do a different thing if the condition is not fulfilled? We
# can use if and else
if (x > 4):
	print('x is larger than 4')
else:
	print('x is less than or equal to 4')

# We can use if, elif (else if) and else to do something more sophisticated
if (x > 4):
	print('x is greater than 4')
elif (x > 3):
	print('x is greater than 3')
elif (x > 2):
	print('x is greater than 2')
else:
	print('x is less than or equal to 2')

# NOTE: once one of the conditions is satisfied, the other conditions will not 
# be checked. If x > 4 is true, x > 3 is also true, but x > 3 wouldn't be 
# checked

# Example: random numbers
# CONCEPT: importing libraries
# Some sophisticated functions cannot be used unless we import them. This is
# how we import a library
import random
# There's a function in the library random called random. This is how we use
# the function
print(random.random())
print(random.random())
print(random.random())
# As you might have guessed, it produced random numbers between 0 and 1

# Here's how we might use if statements when working with random numbers:
y = random.random()
if (y > 0.5):
	print('y is closer to 1')
else:
	print('y is closer to 0')
