print("✅ Day 35 – Advanced List Operations & Problem-Solving\n")
print("-"*40 + "\n")
# ------------------------
# User Input
# ------------------------
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Original list: {numbers}\n")

print("-"*40 + "\n")

# ------------------------
# Runner-Up Score: Pythonic Way
# ------------------------
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) > 1:
    runner_up = unique_numbers[-2]
    print(f"Runner-up score (Pythonic way): {runner_up}\n")
else:
    print("Not enough unique numbers for runner-up.\n")

print("-"*40 + "\n")

# ------------------------
# Runner-Up Score: Manual Way (without set or sort)
# ------------------------
max_num = float('-inf')
runner_up_manual = float('-inf')

for num in numbers:
    if num > max_num:
        runner_up_manual = max_num
        max_num = num
    elif max_num > num > runner_up_manual:
        runner_up_manual = num

if runner_up_manual != float('-inf'):
    print(f"Runner-up score (Manual way): {runner_up_manual}\n")
else:
    print("Not enough distinct numbers for manual runner-up calculation.\n")

print("-"*40 + "\n")

# ------------------------
# Nested List Comprehension Example
# ------------------------
combinations = [(x, y) for x in numbers for y in numbers if x != y]
print(f"All unique combinations (x != y) using list comprehension: {combinations}\n")

print("-"*40 + "\n")
