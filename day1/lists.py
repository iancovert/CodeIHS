# CONCEPT: a list is a container that holds multiple variables
x = [1, 2, 3, 9, 8, 7]
# We access elements of the list using the [] operator
# NOTE: lists are zero-indexed (the first element has index 0)
print(x[0])
print(x[1])
print(x[5])
print(x[4])
# We can access a sequence of elements (similarly to how we obtained
# substrings). Look closely at which elements are returned
print(x[1:4])
print(x[:4])
print(x[1:])

# We can change values in an array
print(x[0])
x[0] = 10
print(x[0])

# We can find the number of elements in an array
x_length = len(x)
print(x_length)

# Instead of viewing one element at a time, we can print the whole list
print(x)

# We can also make lists containing strings
y = ['The', 'weather', 'is', 'nice']
print(y[0] + y[1] + y[2] + y[3])

# It's okay to mix data types in a list
z = [1, 2.0, '3']
print(z[0])
print(z[1])
print(z[2])

# Lists have other operations associated with them
a = []

# Appending
a.append(1)
a.append(2)
a.append(3)
print(a)

# Inserting at a specified index
a.insert(0, 0)
print(a)

# Remove element at an index
a.pop(1)
print(a)

# Counting the number of appearances of an element in the list
b = [1, 1, 1, 2, 1, 1, 1, 3, 4, 1, 5, 1]
print(b.count(1))
