print("✅ Day 37 – Mastering Dictionaries in Python\n")
print("-"*40 + "\n")

# ------------------------
# Creating a dictionary
# ------------------------
student = {
    "name": input("Enter student name: "),
    "age": int(input("Enter student age: ")),
    "grade": input("Enter student grade: ")
}

print("\nInitial student dictionary:")
print(student)
print("\n" + "-"*40 + "\n")

# ------------------------
# Accessing & Modifying Data
# ------------------------
# Add or update a key
student["section"] = input("Enter section to add/update: ")
# Using get method for safe access
phone = student.get("phone", "Not provided")

print("\nUpdated student dictionary:")
print(student)
print("Phone:", phone)
print("\n" + "-"*40 + "\n")

# ------------------------
# Iteration Techniques
# ------------------------
print("Iterating through dictionary keys:")
for key in student.keys():
    print(key, end=" ")
print("\n")

print("Iterating through dictionary values:")
for value in student.values():
    print(value, end=" ")
print("\n")

print("Iterating through dictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")
print("\n" + "-"*40 + "\n")
