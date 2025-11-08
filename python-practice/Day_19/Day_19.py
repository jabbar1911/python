# ✅ Day 19 – Conditions with Collections in Python


print("\n--- Presence Check in List ---")
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is available")  # Output: Banana is available
else:
    print("Banana is not available")

    
    

print("\n--- Empty vs Non-Empty Tuple ---")
numbers = ()
if numbers:
    print("Tuple has elements")
else:
    print("Tuple is empty")  # Output: Tuple is empty

    

    

print("\n--- Set Membership Check ---")
vowels = {"a", "e", "i", "o", "u"}
letter = "e"
if letter in vowels:
    print(f"{letter} is a vowel")  # Output: e is a vowel
else:
    print(f"{letter} is not a vowel")






    

    

print("\n--- Dictionary Key & Value Check ---")
student = {"name": "John", "score": 85}
if "score" in student and student["score"] > 80:
    print("Student passed with distinction")  # Output: Student passed with distinction
else:
    print("Student did not get distinction")

print("\n--- Nested if with Collections ---")
users = {"admin": "active", "guest": "inactive", "editor": "active"}
check_user = "admin"

if check_user in users:
    if users[check_user] == "active":
        print(f"{check_user} has access")  # Output: admin has access
    else:
        print(f"{check_user} does not have access")
else:
    print("User not found")
