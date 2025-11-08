# Day 5: Logical, Identity, Membership & Bitwise Operators in Python 🐍
# Logical Operators
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)        # True (same object)
print("x is z:", x is z)        # False (different objects, same content)
print("x is not z:", x is not z)
# Membership Operators
nums = [10, 20, 30, 40]
print("20 in nums:", 20 in nums)
print("50 not in nums:", 50 not in nums)
# Bitwise Operators
p = 5   # Binary: 0101
q = 3   # Binary: 0011
print("p & q:", p & q)    # 0001 -> 1
print("p | q:", p | q)    # 0111 -> 7
print("p ^ q:", p ^ q)    # 0110 -> 6
print("~p:", ~p)          # Inverts bits -> -6
print("p << 1:", p << 1)  # Left shift -> 10
print("p >> 1:", p >> 1)  # Right shift -> 2
# Number System Conversions
n = 25
print("Decimal to Binary:", bin(n))      # 0b11001
print("Decimal to Octal:", oct(n))       # 0o31
print("Decimal to Hex:", hex(n))         # 0x19

binary_str = "11001"
print("Binary to Decimal:", int(binary_str, 2))  # 25

octal_str = "31"
print("Octal to Decimal:", int(octal_str, 8))    # 25

hex_str = "19"
print("Hex to Decimal:", int(hex_str, 16))       # 25
