print("✅ Day 33 – Recursion and Lambda Functions in Python\n")
print("-"*40 + "\n")

# ------------------------
# Fibonacci with Recursion
# ------------------------
print("Fibonacci Sequence using Recursion:")

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

fib_terms = int(input("Enter number of Fibonacci terms: "))
fib_sequence = fibonacci_recursive(fib_terms)
print(f"Fibonacci sequence ({fib_terms} terms): {fib_sequence}")

print("\n" + "-"*40 + "\n")

# ------------------------
# Lambda Functions Examples
# ------------------------
print("Lambda Function Examples:")

# Single argument lambda
square = lambda x: x**2
num = int(input("Enter a number to square: "))
print(f"Square of {num} is: {square(num)}")

# Multiple arguments lambda
multiply = lambda x, y: x * y
a = int(input("Enter first number to multiply: "))
b = int(input("Enter second number to multiply: "))
print(f"{a} * {b} = {multiply(a, b)}")

# Lambda with conditional
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
num2 = int(input("Enter a number to check even/odd: "))
print(f"{num2} is {check_even(num2)}")

# Lambda with map and filter
numbers_list = [1, 2, 3, 4, 5, 6]
squared_list = list(map(lambda x: x**2, numbers_list))
even_list = list(filter(lambda x: x % 2 == 0, numbers_list))

print(f"Original list: {numbers_list}")
print(f"Squared list using lambda & map: {squared_list}")
print(f"Even numbers using lambda & filter: {even_list}")

print("\n" + "-"*40 + "\n")
