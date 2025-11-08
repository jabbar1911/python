print("✅ Day 30 – Making Python Functions More Powerful\n")
print("-"*40 + "\n")
# Function with default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Testing default argument
greet()              # Output: Hello, Guest!
greet("Alice")       # Output: Hello, Alice!

print("\n" + "-"*40 + "\n")

# Function returning multiple values
def calculator(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return sum_val, diff_val, prod_val

x, y, z = calculator(10, 5)
print(f"Sum: {x}, Difference: {y}, Product: {z}")  # Output: Sum: 15, Difference: 5, Product: 50

print("\n" + "-"*40 + "\n")

# Menu-driven function
def menu_calculator():
    print("1. Add\n2. Subtract\n3. Multiply")
    choice = int(input("Choose operation: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if choice == 1:
        print(f"Result: {a + b}")
    elif choice == 2:
        print(f"Result: {a - b}")
    elif choice == 3:
        print(f"Result: {a * b}")
    else:
        print("Invalid choice!")

menu_calculator()

print("\n" + "-"*40 + "\n")

# Function using *args
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3,4: {sum_all(1,2,3,4)}")       # Output: 10
nums_list = [5,6,7]
print(f"Sum of list [5,6,7]: {sum_all(*nums_list)}") # Output: 18

print("\n" + "-"*40 + "\n")
