# Everything about lists in Python (Data Structure of the Language)

# A list is a collection of data represented by a vector. In Python, they can store all data types

nums = [1, 3, 5, 7, 11, 0]
names = ['Angel', 'Maria', 'Julio', 'Reniher']
booleans = [True, False, True, True]
floats = [1.0, 22.21, 21,1, 10.0]
mixed = ['Angel', True, 21, 'P', 30.00]

# Printing a list

print(f"The nums list is: {nums}")
print(f"The names list is: {names}")
print(f"The booleans list is: {booleans}")
print(f"The floats list is: {floats}")
print(f"The mixed list is: {mixed}\n")

# Lists support Indexing and Slicing

# Print the first and last element of the list

print(f"The first element of the nums list is defined by [0]: {nums[0]}")
print(f"The last element of the nums list is defined by [-1]: {nums[-1]}\n")

print(f"The elements from second to the last in the nums list is defined by [1:]: {nums[1:]} ")
print(f"The elements from start to finish (2 iterations) in the nums list is defined by [::2]: {nums[::2]}\n")

# It's possible to change the value of a stored element is the index is known

change_first_name = 'Messi'
names[0] = change_first_name
print(f"Changing the value of the first name in the names list: {names}")

# Lists can be dynamically operated thanks to the usage of Methods, Functions and Loops

# Add an element at the end of the list with append() method
 
nums.append(45)
print(f"Added a new element at the end of the nums list with the append() method: {nums}\n")

# Create a new list dinamically with the append() method and a for loop

new_nums = []
for i in range(0, int(input("Ingrese el numero de elementos de la lista: "))):
    element = int(input(f"Ingrese el nuevo elemento (nro: {i}): "))
    new_nums.append(element)

print(f"The new list created dinamically with append() is: {new_nums}\n")

# Creating a list dinamically with lambda function and list comprehension

new_element = lambda i: int(input(f"Ingrese el elemento (nro {i}): "))
new_nums_v2 = [new_element(i) for i in range(0, int(input("Ingrese el numero de elementos de la lista: ")))]
print(f"The new version of nums created with lambda and list comprehension is: {new_nums_v2}\n")

# Adding an element on a given index with the insert() method, if the index is greater than the lenght of the list
# the element is inserted at the end

nums.insert(8, 145)
print(f"A new element has been added at index 5 in the nums list: {nums}")

# Finding the number of elements of a list with len() function

print(f"The number of elements of the nums list with len() is: {len(nums)}")
print(f"The number of elements of the names list with len() is: {len(names)}")
print(f"The number of elements of the mixed list with len() is: {len(mixed)}\n")

# Remove an element from the list with pop() method

removed_element = nums.pop()
print(f"The pop() method removes the last element of the lists and is stored on a variable, in the nums list it was: {removed_element}")

removed_element = nums.pop(0)
print(f"Also, it can remove them element of a given index, this time it will remove nums[0], the first elemtn which was: {removed_element}")
print(f"Now the nums list is: {nums}\n")

# Remove the first ocurrence of an element in the list with remove() method, if the element is not on the list
# a TraceBack will be received so keep it in mind

nums.remove(7)
print(f"The first ocurrence of 7 was removed from the nums list with remove(): {nums}\n")

# Delete the whole list with clear() method

print(f"The names list was: {names}")
names.clear()
print(f"Now the names list has been deleted with clear(): {names}\n")

# Find the position in the list of a certain element with index(), if it is not on the list it will return a TraceBack

position = nums.index(5)
print(f"The position of the element 5 in the nums list is: {position}\n")

# Count the number of occurences of a element in the list with count(), if the element is not on the list then it returns 0

occurrences = booleans.count(True)
print(f"The number of times True appears in the booleans list is: {occurrences}\n")

# Sort a list with sort() method, this change is permanently

new_list = [new_element(i) for i in range(0, 4)]
print(f"The new list is: {new_list}")
new_list.sort()
print(f"The new list sorted with the sort() methods is: {new_list}\n")

# Reverse a list with the reverse() method

new_list.reverse()
print(f"The new list reversed with reverse() is: {new_list}\n")

# Sort a list or an iterable with the sorted() function which returns a list with everything sorted and
# changes are not permanently unless saved in the original variable

new_list = sorted(new_list)
print(f"The list sorted with sorted() function is: {new_list}\n")

# Copy an existing list with the copy() method

new_list_copy = new_list.copy()
print(f"The copy made of the new list with copy() is: {new_list_copy}\n")
