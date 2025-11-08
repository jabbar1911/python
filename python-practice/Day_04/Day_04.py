# Day 4: Operators & Type Conversion in Python 🐍

# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# Assignment Operators
x = 5
x += 3
print("After x += 3:", x)
x *= 2
print("After x *= 2:", x)

# Comparison Operators
print("Is a > b?", a > b)
print("Is a == b?", a == b)

# Logical Operators
print("True and False:", True and False)
print("True or False:", True or False)
print("Not True:", not True)

# Bitwise Operators
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Identity Operators
print("a is b:", a is b)
print("a is not b:", a is not b)

# Implicit Type Conversion
result = a + 5.5
print("Implicit Conversion (int + float):", result)

# Explicit Type Conversion
s = "100"
n = int(s)
print("Explicit Conversion (string to int):", n)
