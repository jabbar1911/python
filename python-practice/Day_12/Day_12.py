# ✅ Day 12 of 120 – Working with Lists in Python 📋🐍

# Creating a list with mixed data types
my_list = [10, "Python", 3.14, True]

# append(): adds an element at the end
my_list.append("Codegnan")
print("After append:", my_list)

# extend(): adds elements from another list
my_list.extend([20, 30])
print("After extend:", my_list)

# insert(): inserts an element at a specific position
my_list.insert(1, "Inserted")
print("After insert:", my_list)

# remove(): removes the first matching element
my_list.remove("Python")
print("After remove:", my_list)

# pop(): removes and returns the last item (or item at given index)
popped = my_list.pop()
print("Popped item:", popped)
print("After pop:", my_list)

# clear(): removes all items from the list
cleared_list = my_list.copy()
cleared_list.clear()
print("After clear:", cleared_list)

# copy(): returns a shallow copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# index(): returns the index of the first matching element
print("Index of 10:", my_list.index(10))

# reverse(): reverses the list in place
my_list.reverse()
print("Reversed list:", my_list)

# sort(): sorts a separate numerical list
numbers = [5, 1, 8, 3, 2]
numbers.sort()
print("Sorted numbers:", numbers)

# min() and max(): find the smallest and largest values
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
