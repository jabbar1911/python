from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # Abstract method, no implementation

# Concrete child classes
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class DebitCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card")

# Example usage
payments = [CreditCardPayment(), DebitCardPayment()]

for method in payments:
    method.pay(1000)  # Calls the child class implementation
