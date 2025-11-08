print("✅ Day 36 – Python Generators & Advanced List Operations\n")
print("-"*40 + "\n")

# ------------------------
# Generator Example
# ------------------------
def number_generator(limit):
    for i in range(1, limit + 1):
        yield i

n = int(input("Enter a limit for generator: "))
gen = number_generator(n)

print("\nGenerated numbers using yield (one at a time):")
for val in gen:
    print(val, end=" ")

print("\n")
print("-"*40 + "\n")

# ------------------------
# List Operations Example
# ------------------------
commands = int(input("Enter number of commands: "))
lst = []

print("\nAvailable commands:")
print("insert i e | print | remove e | append e | sort | pop | reverse\n")

for _ in range(commands):
    user_input = input("Enter command: ").split()
    cmd = user_input[0]

    if cmd == "insert":
        i, e = int(user_input[1]), int(user_input[2])
        lst.insert(i, e)
    elif cmd == "print":
        print(lst)
    elif cmd == "remove":
        e = int(user_input[1])
        if e in lst:
            lst.remove(e)
    elif cmd == "append":
        e = int(user_input[1])
        lst.append(e)
    elif cmd == "sort":
        lst.sort()
    elif cmd == "pop":
        if lst:
            lst.pop()
    elif cmd == "reverse":
        lst.reverse()

print("\nFinal List:", lst)
print("\n" + "-"*40 + "\n")
