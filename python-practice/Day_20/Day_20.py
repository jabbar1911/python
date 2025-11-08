# ✅ Day 20 – Practicing Control Flow with if, elif & Nested if in Python

print("\n--- List: More than 5 elements & last element even ---")
# Sample Input: 1 2 3 4 5 6
lst_input = input("Enter list elements separated by space: ").split()
lst = [int(x) for x in lst_input]
if len(lst) > 5 and lst[-1] % 2 == 0:
    print("List has more than 5 elements and last element is even")  # Output: List has more than 5 elements and last element is even
else:
    print("Condition not met")  # Output if condition fails



print("\n--- List: 2nd element > 1st & divisible by 3 ---")
# Sample Input: 2 6 5 7
lst2_input = input("Enter list elements separated by space: ").split()
lst2 = [int(x) for x in lst2_input]
if len(lst2) > 3:
    if lst2[1] > lst2[0] and lst2[1] % 3 == 0:
        print("2nd element > 1st and divisible by 3")  # Output: 2nd element > 1st and divisible by 3
    else:
        print("Condition not met")  # Output if condition fails
else:
    print("List too short")  # Output if list length <= 3

    

print("\n--- Tuple: Contains 0 and next element is also 0 ---")
# Sample Input: 4 0 0 5
tpl_input = input("Enter tuple elements separated by space: ").split()
tpl = tuple(int(x) for x in tpl_input)
if 0 in tpl:
    idx = tpl.index(0)
    if idx + 1 < len(tpl) and tpl[idx + 1] == 0:
        print("Tuple contains 0 followed by another 0")  # Output: Tuple contains 0 followed by another 0
    else:
        print("No consecutive zeros found")  # Output if next element after 0 is not 0
else:
    print("Tuple has no 0")  # Output if tuple has no 0





    

print("\n--- Employee Skills Check ---")
# Sample Input: Python, SQL, Cloud, Java
skills_input = input("Enter employee skills separated by comma: ").split(",")
skills = set([s.strip() for s in skills_input])
if "Python" in skills and "SQL" in skills and "Cloud" in skills:
    print("Employee has Python, SQL, and Cloud skills")  # Output: Employee has Python, SQL, and Cloud skills
else:
    print("Employee does not have all required skills")  # Output if any skill missing

    

print("\n--- Student Subjects & Average Score Check ---")
# Sample Input: num_subjects = 5, then subjects and scores:
Math 70, Physics 65, Chemistry 60, English 75, History 80
subjects_scores = {}
num_subjects = int(input("Enter number of subjects: "))
for _ in range(num_subjects):
    sub = input("Subject name: ")
    score = int(input(f"Score for {sub}: "))
    subjects_scores[sub] = score
if len(subjects_scores) >= 5:
    avg_score = sum(subjects_scores.values()) / len(subjects_scores)
    if avg_score > 60:
        print("Student has >=5 subjects and average score > 60")  # Output: Student has >=5 subjects and average score > 60
    else:
        print("Average score <= 60")  # Output if average <= 60
else:
    print("Less than 5 subjects")  # Output if less than 5 subjects


print("\n--- Set Intersection Check ---")
# Sample Input: set1 = 1 2 3 4, set2 = 3 4 5 6
set1_input = input("Enter elements of first set separated by space: ").split()
set2_input = input("Enter elements of second set separated by space: ").split()
set1 = set([int(x) for x in set1_input])
set2 = set([int(x) for x in set2_input])
if len(set1 & set2) > 2:
    print("Sets have more than 2 intersecting elements")  # Output: Sets have more than 2 intersecting elements
else:
    print("Intersection <= 2 elements")  # Output if intersection <= 2
