# Day 7: Indexing & Slicing in Python 🐍

# Sample String and List
text = "Codegnan"
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive Indexing
print("text[0]:", text[0])        # 'C'
print("fruits[2]:", fruits[2])    # 'cherry'

# Negative Indexing
print("text[-1]:", text[-1])      # 'n'
print("fruits[-2]:", fruits[-2])  # 'date'

# Positive Slicing [start:stop]
print("text[0:4]:", text[0:4])          # 'Code'
print("fruits[1:4]:", fruits[1:4])      # ['banana', 'cherry', 'date']

# Full Slice
print("text[:]:", text[:])              # 'Codegnan'
print("fruits[:]:", fruits[:])          # Full list

# Slicing With Step
print("text[0:8:2]:", text[0:8:2])      # 'Cden'

# Real-world Example
name = "Shaik Abdul Jabbar"
print("First Name:", name[0:5])         # 'Shaik'
print("Last Name:", name[-6:])          # 'Jabbar'
