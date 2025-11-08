# Day 3: Variables & Data Types in Python 🐍

# Variable Declaration
name = "Python"
age = 30
height = 5.9
is_active = True

# Display Types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Active:", is_active, "| Type:", type(is_active))

# Dynamic Typing
value = 10        # int
print("Initial:", value, type(value))
value = "Ten"     # str
print("After reassignment:", value, type(value))

# Implicit Type Conversion
x = 10
y = 2.5
z = x + y
print("Result (implicit conversion):", z, "| Type:", type(z))

# Explicit Type Conversion
s = "100"
num = int(s)
print("Converted string to int:", num, "| Type:", type(num))

# Invalid Conversion (will raise error if uncommented)
# invalid = int("hello")  # Uncomment to test error

# Boolean Type Check
print("bool(0):", bool(0))         # False
print("bool(1):", bool(1))         # True
print("bool(''):", bool(''))       # False
print("bool('Python'):", bool('Python'))  # True
