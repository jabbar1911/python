# Day 6: Bitwise Operations & Number System Conversions in Python 🐍
# Number System Conversions
num = 42
print("Decimal to Binary:", bin(num))   # 0b101010
print("Decimal to Octal:", oct(num))    # 0o52
print("Decimal to Hex:", hex(num))      # 0x2a

binary = "101010"
octal = "52"
hexa = "2a"
print("Binary to Decimal:", int(binary, 2))   # 42
print("Octal to Decimal:", int(octal, 8))     # 42
print("Hex to Decimal:", int(hexa, 16))       # 42
# Bitwise Operators
a = 12   # 1100
b = 5    # 0101
print("a & b:", a & b)      # 0100 = 4
print("a | b:", a | b)      # 1101 = 13
print("a ^ b:", a ^ b)      # 1001 = 9
print("~a:", ~a)            # -13
print("a << 1:", a << 1)    # 24
print("a >> 1:", a >> 1)    # 6

# Membership Operators
lst = ['apple', 'banana', 'cherry']
text = "Python is awesome"

print("'banana' in list:", 'banana' in lst)
print("'mango' not in list:", 'mango' not in lst)
print("'Python' in text:", 'Python' in text)
# Identity Operators
x = [10, 20]
y = x
z = [10, 20]
print("x is y:", x is y)        # True
print("x is z:", x is z)        # False
print("x is not z:", x is not z)  # True
# Logical & Bitwise Truth Table
print("\nTruth Table for Logical and Bitwise Operators:")
print("A B | A and B | A or B | A ^ B")
for A in [0, 1]:
    for B in [0, 1]:
        print(f"{A} {B} |   {A and B}     |   {A or B}    |   {A ^ B}")
