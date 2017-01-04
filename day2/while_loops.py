# CONTROL FLOW TOOL: while loops
# While loops will execute repeatedly, but not necessarily a fixed number of
# times. They're more flexible: they continue iterating until some condition
# is fulfilled
x = 0
while (x < 5):
	x = x + 1
print(x)

# NOTE: while loops require a boolean value inside the while()

# Example: continue generating random numbers until one is close to 6
from random import random
y = False
while (y == False):
	z = round(random() * 6)
	if (z == 6):
		y = True

# Example: continue flipping a coin until you see 3 heads
total_flips = 0
heads = 0
while (heads < 3):
	flip = round(random())
	total_flips = total_flips + 1
	if (flip == 1):
		heads = heads + 1
print(total_flips)

# NOTE: every for loop can be transformed into a while loop. While loops are
# more flexible (though not necessarily more convenient to write)
a = [5, 8, 3, 7, 3, 8, 4, 2, 5, 7, 3]
for i in range(len(a)):
	print(a[i])

# Equivalently, using a while loop:
i = 0
while (i < len(a)):
	print(a[i])
	i = i + 1

# NOTE: be very careful to avoid infinite loops
''' If we ran these lines of code, it would just run forever

i = 0
while (i < len(a)):
	print(a[i])

'''