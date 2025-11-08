# ✅ Day 13 of 120 – Tuples, Sets & Dictionaries in Python 🧠📚🐍
# --- Tuple Methods ---
my_tuple = (10, 20, 30, 20, 40)  # Tuple: (10, 20, 30, 20, 40)
print("Tuple:", my_tuple)  # Tuple: (10, 20, 30, 20, 40)
print("Count of 20:", my_tuple.count(20))  # Count of 20: 2
print("Index of 30:", my_tuple.index(30))  # Index of 30: 2
print("Length:", len(my_tuple))  # Length: 5
print("Min:", min(my_tuple))  # Min: 10
print("Max:", max(my_tuple))  # Max: 40
print("Sum:", sum(my_tuple))  # Sum: 120
print("Sorted:", sorted(my_tuple))  # Sorted: [10, 20, 20, 30, 40]
# --- Set Methods ---
my_set = {1, 2, 3}  # Initial Set: {1, 2, 3}
print("\nInitial Set:", my_set)  # Output order may vary
my_set.add(4)
my_set.update([5, 6])
print("After add & update:", my_set)  # {1, 2, 3, 4, 5, 6}
my_set.remove(2)
my_set.discard(10)
print("After remove & discard:", my_set)  # {1, 3, 4, 5, 6}
popped = my_set.pop()
print("After pop():", my_set, " (Popped:", popped, ")")  # One item removed (random)
copy_set = my_set.copy()
my_set.clear()
print("Copy of Set:", copy_set)  # Remaining items before clear
print("Cleared Set:", my_set)  # Cleared Set: set()
# --- Set Operations ---
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("\nUnion:", set_a.union(set_b))  # Union: {1, 2, 3, 4, 5}
print("Intersection:", set_a.intersection(set_b))  # Intersection: {3}
print("Symmetric Difference:", set_a.symmetric_difference(set_b))  # {1, 2, 4, 5}
print("Is subset?", set_a.issubset(set_b))  # False
print("Is superset?", set_a.issuperset(set_b))  # False
print("Is disjoint?", set_a.isdisjoint(set_b))  # False
# --- Dictionary ---
student = {"name": "Jabbar","course": "Python", "duration": "120 days"}
print("\nDictionary:", student)  # {'name': 'Jabbar', 'course': 'Python', 'duration': '120 days'}
print("Accessing course:", student["course"])  # Python
