print("✅ Day 29 – Mastering Functions in Python\n")
print("-"*40 + "\n")

# Function to check even or odd
def is_even(number):
    return number % 2 == 0

# Testing the function with user input
num = int(input("Enter a number to check even/odd: "))
if is_even(num):
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

print("\n" + "-"*40 + "\n")

# Function with positional, keyword, and default arguments
def student_details(name, age, grade="Not Assigned", city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print(f"City: {city}")
# Sample calls
print("Student 1 Details:")
student_details("Alice", 20)  # uses default grade and city

print("\nStudent 2 Details:")
student_details(name="Bob", age=22, grade="A")  # keyword argument for grade

print("\nStudent 3 Details:")
student_details("Charlie", 19, city="New York")  # positional + default argument usage
print("\n" + "-"*40 + "\n")
# Manual sum function
def manual_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
nums_list = [10, 20, 30, 40]
print(f"Sum of {nums_list} is: {manual_sum(nums_list)}")
print("\n" + "-"*40 + "\n")
