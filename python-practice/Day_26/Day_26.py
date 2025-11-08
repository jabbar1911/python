# ✅ Day 26 – HackerRank Challenges & Python Lists

# 1️⃣ sWAP cASE – Convert each letter to opposite case
text = input("Enter text: ")  # Example input: HelloWorld
swap_text = text.swapcase()
print("Swap case:", swap_text)  # Output: hELLOwORLD
print("\n" + "-"*30 + "\n")

# 2️⃣ What's Your Name? – String formatting
first_name = input("Enter first name: ")  # Example input: John
last_name = input("Enter last name: ")    # Example input: Doe
full_name = f"Hello {first_name} {last_name}!"
print(full_name)  # Output: Hello John Doe!
print("\n" + "-"*30 + "\n")

# 3️⃣ String Validators – Check character types
sample = input("Enter a string: ")  # Example input: Hello123
print("Has alphanumeric:", any(c.isalnum() for c in sample))  # Output: True
print("Has alphabetic:", any(c.isalpha() for c in sample))    # Output: True
print("Has digits:", any(c.isdigit() for c in sample))         # Output: True
print("Has lowercase:", any(c.islower() for c in sample))      # Output: True
print("Has uppercase:", any(c.isupper() for c in sample))      # Output: True
print("\n" + "-"*30 + "\n")


















# 4️⃣ Python Lists – Practice methods
my_list = [10, 20, 30]
print("Original list:", my_list)  # Output: [10, 20, 30]
print("\n" + "-"*30 + "\n")

# append()
my_list.append(40)
print("After append:", my_list)  # Output: [10, 20, 30, 40]
print("\n" + "-"*30 + "\n")

# extend()
my_list.extend([50, 60])
print("After extend:", my_list)  # Output: [10, 20, 30, 40, 50, 60]
print("\n" + "-"*30 + "\n")

# insert()
my_list.insert(1, 15)
print("After insert:", my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
print("\n" + "-"*30 + "\n")

# remove()
my_list.remove(30)
print("After remove:", my_list)  # Output: [10, 15, 20, 40, 50, 60]
print("\n" + "-"*30 + "\n")

# pop()
popped = my_list.pop()
print("Popped item:", popped)    # Output: 60
print("After pop:", my_list)     # Output: [10, 15, 20, 40, 50]
print("\n" + "-"*30 + "\n")

# reverse()
my_list.reverse()
print("Reversed list:", my_list) # Output: [50, 40, 20, 15, 10]
print("\n" + "-"*30 + "\n")


# sort()
my_list.sort()
print("Sorted list:", my_list)   # Output: [10, 15, 20, 40, 50]
print("\n" + "-"*30 + "\n")

# copy() vs reference
copy_list = my_list.copy()
copy_list.append(100)
print("Original list:", my_list) # Output: [10, 15, 20, 40, 50]
print("Copied list:", copy_list) # Output: [10, 15, 20, 40, 50, 100]
print("\n" + "-"*30 + "\n")
