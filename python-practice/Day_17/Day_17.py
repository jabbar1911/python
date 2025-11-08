# ✅ Day 17 – Conditional Statements Practice
print("\n--- Even or Odd Check ---")
num = int(input("Enter a number: "))  # Example: 7
if num % 2 == 0:
    print(f"{num} is Even")  # Output: 8 is Even
else:
    print(f"{num} is Odd")  # Output: 7 is Odd

print("\n--- Voting Eligibility ---")
age = int(input("Enter your age: "))  # Example: 18
if age >= 18:
    print("You are eligible to vote.")  # Output: You are eligible to vote.
else:
    print("You are not eligible to vote.")  # Output if < 18: You are not eligible to vote.
    
print("\n--- Small Calculator ---")
a = float(input("Enter first number: "))  # Example: 10
b = float(input("Enter second number: "))  # Example: 5
op = input("Enter operation (+, -, *, /): ")  # Example: *
if op == "+":
    print("Result:", a + b)  # Output: 15.0
elif op == "-":
    print("Result:", a - b)  # Output: 5.0
elif op == "*":
    print("Result:", a * b)  # Output: 50.0
elif op == "/":
    if b != 0:
        print("Result:", a / b)  # Output: 2.0
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator!")
    
print("\n--- Positive, Negative, or Zero ---")
n = float(input("Enter a number: "))  # Example: -3
if n > 0:
    print("Positive")  # Output: Positive
elif n < 0:
    print("Negative")  # Output: Negative
else:
    print("Zero")  # Output: Zero
