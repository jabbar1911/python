# ✅ Day 15 – Script Mode & User Inputs in Python

# Taking input from the user
name = input("Enter your name: ")  
# If user inputs: Jabbar
# Output: Enter your name: Jabbar

age = int(input("Enter your age: "))  
# If user inputs: 22
# Output: Enter your age: 22

course = input("Enter your course: ")  
# If user inputs: Python
# Output: Enter your course: Python

# Using .format() method
print("Hello {}, you are {} years old and learning {}.".format(name, age, course))
# Output: Hello Jabbar, you are 22 years old and learning Python.

# Using f-string (Python 3.6+)
print(f"Welcome {name}! Age: {age}, Course: {course}")
# Output: Welcome Jabbar! Age: 22, Course: Python

# Using % formatting
print("Name: %s | Age: %d | Course: %s" % (name, age, course))
# Output: Name: Jabbar | Age: 22 | Course: Python

# A small calculation
marks = float(input("Enter your marks out of 100: "))  
# If user inputs: 88.5
# Output: Enter your marks out of 100: 88.5

percentage = marks
print(f"Hi {name}, you scored {percentage}% in {course}.")
# Output: Hi Jabbar, you scored 88.5% in Python.
