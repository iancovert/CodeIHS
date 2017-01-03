# CONCEPT: data types
# Variables can take different kinds of values. We'll start by looking at ints,
# and floats

# DATA TYPE: int
# We use two variables, a and b
a = 2
b = 3
print(a)
print(b)

# CONCEPT: operators and operands
# We use operators (like +) to combine operands (like 1 and 2). For example,
# the expression 1 + 2 produces a result
# Each data type has several operations associated with it

# We show how to use several mathematical operators (+ - * / // % **) to combine 
# ints
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(b ** a)

# Remark: sometimes the result is an int. Sometimes it's a float

# DATA TYPE: float
# We use two variables, c and d
c = 10.0
d = 3.5
print(c)
print(d)

# We use the same operators (+ - * / // % **)
print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(c // d)
print(c % d)
print(c ** d)

# Floats don't contain an infinite number of decimals. They have a fixed 
# precision
print(1 / 3)

# QUESTION: what's the difference between ints and floats?
# You've probably notices that ints and floats behave very similarly. They have
# all the same operators, so is there a difference? Yes, but the difference is
# under the hood: it has to do with how your computer stores ints and floats.
# Ints are simpler and easier to store. Floats are more complex. Because of 
# this difference, we prefer to use ints when possible
print(type(1))
print(type(1.))

# QUESTION: can you combine ints and floats? Yes, no problem!
print(3 * 4.0)
print(2 / 2.5)

# REMARK: the result of the operation will be a float

# Order of operations
e = 1 + 2 * 3
print(e)
f = (1 + 2) * 3
print(f)
g = 2 / 3 * 2
print(g)

# Rule of thumb: use parentheses wherever needed. It makes your code more
# readable, and you can be sure that it's right