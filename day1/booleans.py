# DATA TYPE: boolean
# Whereas ints, floats and strings can take on many different values,
# boolean variables can only take on two values: True or False
x = True
y = False
print(x)
print(y)

# Booleans can be combined in expressions, called boolean expressions. The
# operators we use are called logical operators. The main ones are 'and', 
# 'or' and 'not'
print(x or y)
print(x and y)
print(not x)
print(not y)
print(x and x and y)
print((x and y) or ((y or y) and (x or y)))

# If you ever forget what each operator does, look at a truth table. Truth
# tables show what the operator does with each possible combination of inputs

# When do booleans come up?

# An important use case is when comparing numbers. In addition to mathematical
# operators, we can make expressions by combining numbers with comparison
# operators. They are < <= > >= == and !=
a = 1
b = 1
c = 2
print(a < b)
print(a <= b)
print(c > b)
print(c <= b)
print(a == b)
print(a != b)
print(a != c)

# NOTE: be careful not to mix up == with =. The single equals sign is for
# assigning values, and double equals is for testing equality

# Another example: testing if a number is in the range [5, 10]
e = 7
f = 11
print(e >= 5 and e <= 10)
print(f >= 5 and f <= 10)

# Another example: testing if a number is outside the range [10, 20]
g = 9
h = 15
print(g < 10 or g > 20)
print(h < 10 or h > 20)
