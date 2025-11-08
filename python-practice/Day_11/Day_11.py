# Day 11: String Formatting & Collections Basics in Python 🧩🐍

# 1. String Formatting

name = "Shaik"
course = "Python Full Stack"
marks = 95

# Using .format()
print("Name: {} | Course: {} | Marks: {}".format(name, course, marks))

# Using f-strings (Recommended in Python 3.6+)
print(f"Name: {name} | Course: {course} | Marks: {marks}")

# Using % formatting
print("Name: %s | Course: %s | Marks: %d" % (name, course, marks))

# 2. Formatting Methods
text = "Python"

print("zfill (length 10):", text.zfill(10))      # '0000Python'
print("Right Justify:", text.rjust(10, '*'))     # '****Python'
print("Left Justify:", text.ljust(10, '-'))      # 'Python----'
print("Center:", text.center(12, '='))           # '===Python==='

# 3. Case-insensitive Comparison
a = "PYTHON"
b = "python"
print("Equal (case-insensitive):", a.casefold() == b.casefold())

# 4. partition()
line = "Email: user@example.com"
print("Partitioned Line:", line.partition(":"))  # ('Email', ':', ' user@example.com')

# 5. Intro to Collections (Preview)
# Python's main collection types: list, tuple, set, dict

# Example of each
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
my_dict = {"name": "Shaik", "course": "Python"}

print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)
