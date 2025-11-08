# ✅ Day 27 – The Elegance of Python List Comprehensions

# Traditional loop to generate even numbers from 1 to 50
evens = []
for i in range(1, 51):
    if i % 2 == 0:
        evens.append(i)
print("Even numbers using loop:", evens)
print("\n" + "-"*30 + "\n")

# List comprehension for the same task
evens_comp = [i for i in range(1, 51) if i % 2 == 0]
print("Even numbers using list comprehension:", evens_comp)
print("\n" + "-"*30 + "\n")

# Transforming strings: lowercase to title case
names = ["alice", "bob", "charlie", "diana"]
title_names = [name.title() for name in names]
print("Title-cased names:", title_names)
print("\n" + "-"*30 + "\n")

# Applying inline transformations: cubes of numbers
numbers = [1, 2, 3, 4, 5]
cubes = [n**3 for n in numbers]
print("Cubes of numbers:", cubes)
print("\n" + "-"*30 + "\n")

# Conditional expressions: label numbers as Even or Odd
numbers2 = [10, 15, 22, 33, 40]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers2]
print("Even/Odd labels:", labels)
print("\n" + "-"*30 + "\n")

# Nested list comprehension: create pairs from two lists
list1 = [1, 2, 3]
list2 = ['a', 'b']
pairs = [(x, y) for x in list1 for y in list2]
print("Pairs from two lists:", pairs)
print("\n" + "-"*30 + "\n")
