class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner         # Public attribute
        self.__balance = balance   # Private attribute
        self.__pin = pin           # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Public method to withdraw money with PIN verification
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Incorrect PIN! Access denied.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    # Public method to check balance safely
    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            print("Incorrect PIN! Cannot view balance.")
            return None

# Example usage
acc = BankAccount("Alice", 5000, 1234)

acc.deposit(1500)            # Deposited 1500. New balance: 6500
acc.withdraw(2000, 1234)     # Withdrawn 2000. New balance: 4500
print(acc.get_balance(1234)) # 4500

# Trying to access private attribute directly
#print(acc.__balance)         # AttributeError
