# ✅ Day 22 – Exploring while Loops & The Power of break

print("\n--- User Input Until 'quit' ---")
while True:
    user_input = input("Enter something (type 'quit' to exit): ")
    if user_input.lower() == "quit":
        break  # Exits the loop when user types 'quit'
    print(f"You entered: {user_input}")  # Output: echoes entered text

print("\n--- Countdown from 10 to 1 ---")
count = 10
while count > 0:
    print(count)  # Output: 10 9 8 ... 1
    count -= 1

print("\n--- Find the first multiple of 7 in a range ---")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
current = start
while current <= end:
    if current % 7 == 0:
        print(f"First multiple of 7: {current}")  # Output: first number divisible by 7
        break  # Stop after finding the first multiple
    current += 1
