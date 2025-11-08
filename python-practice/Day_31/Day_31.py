print("✅ Day 31 – Mastering Flexible Functions with *args & **kwargs\n")
print("-"*40 + "\n")

# String unpacking example
print("String unpacking example:")
print(*"Python")   # Output: P y t h o n
print("\n" + "-"*40 + "\n")

# Function using *args
def sum_numbers(*args):
    total = sum(args)
    print(f"Sum of {args}: {total}")   # Output depends on input

sum_numbers(1, 2, 3, 4)                # Output: Sum of (1,2,3,4): 10
sum_numbers(10, 20)                     # Output: Sum of (10,20): 30

print("\n" + "-"*40 + "\n")

# Function using **kwargs
def print_order_details(**kwargs):
    print("Order Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")        # Prints each key-value pair

print_order_details(topping="Cheese", drink="Coke", dessert="Ice Cream")

print("\n" + "-"*40 + "\n")

# Real-world simulation: Zomato order
def zomato_order(*items, **extras):
    print("Main Items Ordered:", items)          # Tuple of items
    print("Extras Added:")
    for k, v in extras.items():
        print(f"{k}: {v}")
    print("Enjoy your meal!")

zomato_order("Pizza", "Burger", topping="Cheese", drink="Coke", dessert="Ice Cream")

print("\n" + "-"*40 + "\n")
