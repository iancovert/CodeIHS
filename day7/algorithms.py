# Sequential search
# If the item is contained in the list, the index is returned
# Else, -1 is returned
def sequential_search(my_list, item):
	for index in range(len(my_list)):
		if (my_list[index] == item):
			return index
	return -1

# Selection sort
# Sorts in ascending order
def selection_sort(my_list):
	for i in range(len(my_list)):
		minIndex = i
		for j in range(i, len(my_list)):
			if my_list[j] < my_list[minIndex]:
				minIndex = j
		temp = my_list[i]
		my_list[i] = my_list[minIndex]
		my_list[minIndex] = temp

# Test the functions
the_list = [2, 4, 6, 9, 7, 3]

print(sequential_search(the_list, 6))
print(sequential_search(the_list, 10))

print(the_list)
selection_sort(the_list)
print(the_list)