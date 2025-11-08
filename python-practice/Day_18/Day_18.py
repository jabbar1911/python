# ✅ Day 18 – elif & Nested if Practice
print("\n--- Bus Ticket Pricing ---")
age = int(input("Enter your age: "))  # Example: 15
if age < 5:
    print("Ticket Price: Free")  # Output: Free
elif age <= 18:
    print("Ticket Price: ₹20")  # Output: ₹20
elif age <= 60:
    print("Ticket Price: ₹50")  # Output: ₹50
else:
    print("Ticket Price: ₹30")  # Output: ₹30

    

print("\n--- Categorizing Numbers ---")
num = int(input("Enter a number: "))  # Example: 150
if num < 100:
    print("Small Number")  # Output: Small Number
elif num <= 500:
    print("Big Number")  # Output: Big Number
else:
    print("Other Number")  # Output: Other Number




print("\n--- Divisibility Check (Nested if) ---")
num2 = int(input("Enter a number: "))  # Example: 12
if num2 % 2 == 0:
    if num2 % 3 == 0:
        print(f"{num2} is divisible by both 2 and 3")  # Output: divisible by both
    else:
        print(f"{num2} is divisible by 2 only")  # Output: divisible by 2 only
elif num2 % 3 == 0:
    print(f"{num2} is divisible by 3 only")  # Output: divisible by 3 only
else:
    print(f"{num2} is not divisible by 2 or 3")  # Output: not divisible




    
print("\n--- Largest of Four Numbers (Nested if) ---")
a = int(input("Enter first number: "))   # Example: 10
b = int(input("Enter second number: "))  # Example: 25
c = int(input("Enter third number: "))   # Example: 7
d = int(input("Enter fourth number: "))  # Example: 15

if a > b:
    if a > c:
        if a > d:
            largest = a
        else:
            largest = d
    elif c > d:
        largest = c
    else:
        largest = d
else:
    if b > c:
        if b > d:
            largest = b
        else:
            largest = d
    elif c > d:
        largest = c
    else:
        largest = d

print("Largest Number is:", largest)  # Output: 25
