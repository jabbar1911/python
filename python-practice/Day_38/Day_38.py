import math
import random

print("✅ Day 38 – Exploring Python's Math and Random Modules\n")
print("-"*40 + "\n")

# ------------------------
# Math Module Examples
# ------------------------
num = float(input("Enter a number for math operations: "))

print(f"\nSquare root of {num}: {math.sqrt(num)}")
print(f"Factorial of {int(num)}: {math.factorial(int(num))}")
print(f"Ceiling value of {num}: {math.ceil(num)}")
print(f"Floor value of {num}: {math.floor(num)}")

# GCD of two numbers
a = int(input("\nEnter first integer for GCD: "))
b = int(input("Enter second integer for GCD: "))
print(f"GCD of {a} and {b}: {math.gcd(a, b)}")
print("\n" + "-"*40 + "\n")

# ------------------------
# Random Module Examples
# ------------------------
print("Random Module Examples:")

rand_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {rand_int}")

rand_float = random.uniform(1.0, 10.0)
print(f"Random float between 1.0 and 10.0: {rand_float:.2f}")

rand_range = random.randrange(0, 50, 5)
print(f"Random number between 0-50 with step 5: {rand_range}")

print("\n" + "-"*40 + "\n")
