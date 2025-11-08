# ✅ Day 28 – Building Real-World Python Mini-Projects
# ----------------- ATM Simulation -----------------
print("ATM Simulation\n")
# Sample user data
correct_pin = "1234"
balance = 5000
# ATM Loop
while True:
    pin = input("Enter your 4-digit PIN (or 'quit' to exit): ")
    if pin.lower() == "quit":
        print("Exiting ATM. Thank you!")
        break
    elif pin != correct_pin:
        print("Incorrect PIN! Try again.")
        print("\n" + "-"*30 + "\n")
        continue
    print("PIN accepted. Welcome!\n")
    while True:
        print("1. Balance Inquiry\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance is: ₹{balance}")
        elif choice == "2":
            amount = int(input("Enter deposit amount: ₹"))
            balance += amount
            print(f"₹{amount} deposited. New balance: ₹{balance}")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount (multiples of 100/500): ₹"))
            if amount > balance:
                print("Insufficient funds!")
            elif amount % 100 != 0 and amount % 500 != 0:
                print("Enter amount in multiples of 100 or 500.")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn. \nNew balance: ₹{balance}")
        elif choice == "4":
            print("Exiting account. Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.")
        print("\n" + "-"*30 + "\n")



print("\n" + "-"*30 + "\n")

# ----------------- BMI Calculator -----------------
print("BMI Calculator\n")

# User input
weight = float(input("Enter your weight in kg: "))
height_ft = int(input("Enter your height - feet: "))
height_in = int(input("Enter your height - inches: "))

# Convert height to meters
height_m = (height_ft * 12 + height_in) * 0.0254

# BMI calculation
bmi = weight / (height_m ** 2)
bmi = round(bmi, 2)

# BMI Classification
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi} ({category})")
print("\n" + "-"*30 + "\n")
