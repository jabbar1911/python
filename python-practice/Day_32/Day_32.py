print("✅ Day 32 – Scope, Recursion, and Problem-Solving in Python\n")
print("-"*40 + "\n")

# ------------------------
# Variable Scope Example
# ------------------------
print("Variable Scope Example:")

global_var = 100

def outer_function():
    outer_var = 50
    def inner_function():
        nonlocal outer_var
        outer_var += 10
        print(f"Inner function (nonlocal) outer_var: {outer_var}")  # Output: 60
    inner_function()
    print(f"Outer function outer_var: {outer_var}")                 # Output: 60

outer_function()
print(f"Global variable: {global_var}")                              # Output: 100

print("\n" + "-"*40 + "\n")

# ------------------------
# Factorial – 3 Ways
# ------------------------
print("Factorial Examples:")

# Using for loop
def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Using while loop
def factorial_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

# Using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

num = int(input("Enter a number to calculate factorial: "))
print(f"Factorial of {num} (for loop): {factorial_for(num)}")
print(f"Factorial of {num} (while loop): {factorial_while(num)}")
print(f"Factorial of {num} (recursion): {factorial_recursive(num)}")

print("\n" + "-"*40 + "\n")

# ------------------------
# Fibonacci Series
# ------------------------
print("Fibonacci Series Example:")
fib_terms = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
print("Fibonacci sequence:", end=" ")
for _ in range(fib_terms):
    print(a, end=" ")
    a, b = b, a + b
print("\n" + "-"*40 + "\n")

# ------------------------
# Railway Ticket System
# ------------------------
print("Railway Ticket System Simulation:")

def ticket_price(age, gender):
    base_price = 100
    if age < 5:
        price = 0
    elif age <= 18:
        price = base_price * 0.5
    elif age >= 60:
        price = base_price * 0.6
    else:
        price = base_price

    # Additional discount for females
    if gender.lower() == 'female':
        price *= 0.9

    return round(price, 2)

passenger_age = int(input("Enter passenger age: "))
passenger_gender = input("Enter passenger gender (male/female): ")
final_price = ticket_price(passenger_age, passenger_gender)
print(f"Ticket Price for {passenger_age} year old {passenger_gender}: {final_price}")

print("\n" + "-"*40 + "\n")
