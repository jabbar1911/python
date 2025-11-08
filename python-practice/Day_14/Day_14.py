# ✅ Day 14 of 120 – Python Dictionaries (Advanced) 🧠📚🐍
student = {
    "name": "Jabbar",
    "age": 22,
    "course": "Python Full Stack",
    "skills": ["Python", "HTML", "CSS"]}
print("Original Dictionary:", student)
# {'name': 'Jabbar', 'age': 22, 'course': 'Python Full Stack', 'skills': ['Python', 'HTML', 'CSS']}
# Accessing elements
print("Name:", student["name"])  # Name: Jabbar
print("Skills:", student.get("skills"))  # Skills: ['Python', 'HTML', 'CSS']
# Adding new key-value pair
student["city"] = "Vijayawada"
print("After Adding City:", student["city"])  # Vijayawada
# Updating value
student["age"] = 23
print("Updated Age:", student["age"])  # 23
# Using update() to add multiple items
student.update({"gender": "Male", "graduated": False})
print("After update():", student)
# {'name': ..., 'gender': 'Male', 'graduated': False, ...}
# Removing items
student.pop("course")
print("After pop('course'):", student)  # 'course' key removed
del student["skills"]
print("After del skills:", student)  # 'skills' key removed
# popitem() removes last inserted item
last_item = student.popitem()
print("Popped Last Item:", last_item)  # ('graduated', False) or similar
print("After popitem():", student)
# Dictionary keys(), values(), items()
print("Keys:", list(student.keys()))  # ['name', 'age', 'city', 'gender']
print("Values:", list(student.values()))  # ['Jabbar', 23, 'Vijayawada', 'Male']
print("Items:", list(student.items()))  
# [('name', 'Jabbar'), ('age', 23), ('city', 'Vijayawada'), ('gender', 'Male')]
# Copying dictionary
student_copy = student.copy()
print("Copied Dictionary:", student_copy)
# Clearing dictionary
student.clear()
print("After clear():", student)  # {}
