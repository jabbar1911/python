from functools import reduce
print("✅ Day 34 – Functional Programming with map(), filter(), and reduce()\n")
print("-"*40 + "\n")

# ------------------------
# User Input
# ------------------------
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Original list: {numbers}\n")

print("-"*40 + "\n")

# ------------------------
# Filter: Get even numbers
# ------------------------
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers using filter(): {even_numbers}\n")

print("-"*40 + "\n")

# ------------------------
# Map: Get squares
# ------------------------
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squares using map(): {squared_numbers}\n")

print("-"*40 + "\n")

# ------------------------
# Reduce: Sum of all numbers
# ------------------------
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers using reduce(): {sum_numbers}\n")

print("-"*40 + "\n")

# ------------------------
# Additional Example: Map + Conditional Label
# ------------------------
labels = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))
print(f"Labels using map() + lambda: {labels}\n")

print("-"*40 + "\n")
