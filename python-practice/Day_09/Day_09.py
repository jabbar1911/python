# Day 9: Strings in Python 🧵🐍

# Writing comments in Python
# This is a single-line comment

# Multi-line comment (docstring)
"""
This script covers:
- Striding
- Encoding
- String operations
- String methods
"""

# Striding
text = "PythonProgramming"
print("Striding forward:", text[::2])     # Every second character
print("Striding backward:", text[::-1])   # Reversed string

# Encoding
char = 'A'
print("ASCII of 'A':", ord(char))         # 65
print("Character for 97:", chr(97))       # 'a'

# String Operators
s1 = "Hello"
s2 = "World"
print("Concatenation:", s1 + " " + s2)     # Hello World
print("Repetition:", s1 * 3)               # HelloHelloHello
print("'H' in s1:", 'H' in s1)             # True
print("'z' not in s2:", 'z' not in s2)     # True

# Basic String Methods
sample = "  Python123!  "
print("Uppercase:", sample.upper())
print("Lowercase:", sample.lower())
print("Stripped:", sample.strip())

# Character Type-Checking Methods
print("Is Alpha:", sample.isalpha())        # False
print("Is Digit:", sample.isdigit())        # False
print("Is Space:", sample.isspace())        # False
print("Is Alnum:", sample.isalnum())        # False

# Testing on a clean string
clean = "Python123"
print("Is Alnum (clean):", clean.isalnum()) # True
