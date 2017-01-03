# DATA TYPE: string
# We use three variables, e f and g
e = 'Hello world'
f = 'Hello'
g = "world"
print(e)
print(f)
print(g)

# Strings can be concatenated using the + operator
print(f + g)
print(e + f)

# NOTE: we cannot use any of the other mathematical operators with strings!

# NOTE: don't confuse strings with numerical data
h = 1
i = '1'
print(h)
print(i)
print(type(h))
print(type(i))

# EXPLANATION: even though print() shows the same output, remember that print
# is merely a function the helps us see what value the variable contains. '1'
# is fundamentally different than 1. You cannot do mathematical operations with
# the string '1'

# This would produce an error:
# print(1 + '1')

# MORE DETAILS ABOUT STRINGS: special characters
# What if we want our strings to contain something other than alphanumeric
# characters? Examples are linebreaks (\n) and tabs (\t)
j = 'Hello \n my name is \n Bob'
k = 'Hello my \t name \t is Bob'
print(j)
print(k)

# MORE DETAILS ABOUT STRINGS: substrings
m = 'You sure can do a lot with strings'
print(m)
print(m[5])
print(m[5:10])
print(m[:10])
print(m[5:])

# Examples of other string operations
print(e.upper())
print(e.lower())
print(len(e))
print(m.count('u'))

# Other kinds of numerical data can be converted to strings
x = 'Today I woke up at '
y = 10
# This would fail:
# print(x + y)
# This will work:
print(x + str(y))
