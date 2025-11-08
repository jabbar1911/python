# Day 10: String Methods & Advanced Operations in Python 🧠🐍

text = "  Welcome to Python Programming! Python is fun.  "

# Basic Cleaning
cleaned = text.strip()
print("Stripped text:", cleaned)

# replace()
replaced = cleaned.replace("Python", "Java")
print("After replace():", replaced)

# split()
words = cleaned.split()
print("After split():", words)

# join()
joined = "-".join(words)
print("After join():", joined)

# find() and index()
print("First 'Python' using find():", cleaned.find("Python"))  # Returns first index or -1
print("First 'Python' using index():", cleaned.index("Python"))  # Returns index or error

# count()
print("Count of 'Python':", cleaned.count("Python"))

# startswith() and endswith()
print("Starts with 'Welcome':", cleaned.startswith("Welcome"))
print("Ends with 'fun.':", cleaned.endswith("fun."))

# Combining methods for formatting
formatted = "Name: {}\nCourse: {}".format("Shaik Abdul Jabbar", "Python Full Stack")
print("\nFormatted Output:\n" + formatted)
