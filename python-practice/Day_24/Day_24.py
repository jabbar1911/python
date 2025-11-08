# ✅ Day 24 – Building Patterns with Nested Loops

print("\n--- 5x5 Square Pattern ---")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

    
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


print("\n--- Multiplication Table up to 10 ---")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3}", end=" ")
    print()

    
# Output: 1 2 3 ... 10 (formatted table of 10x10)


print("\n--- Right-Angled Triangle Pattern ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

    
# Output:
# *
# **
# ***
# ****
# *****












print("\n--- Descending Triangle Pattern ---")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *****
# ****
# ***
# **
# *
