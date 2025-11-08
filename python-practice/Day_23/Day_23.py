# ✅ Day 23 – Refining Logic with continue & pass

print("\n--- Skip multiples of 3 from 1 to 20 ---")
for i in range(1, 21):
    if i % 3 == 0:
        continue  # Skip this iteration if multiple of 3
    print(i, end=" ")  # Output: 1 2 4 5 7 8 10 11 13 14 16 17 19 20
print()

print("\n--- Process only positive numbers ---")
numbers = [-5, 3, -1, 7, -2, 10]
for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(num, end=" ")  # Output: 3 7 10
print()

print("\n--- Using pass as a placeholder ---")
for i in range(5):
    if i % 2 == 0:
        pass  # Placeholder for future logic
    else:
        print(f"Processing odd number: {i}")  
        # Output: Processing odd number: 1
        #         Processing odd number: 3
