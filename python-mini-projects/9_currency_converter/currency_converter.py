#!/usr/bin/env python3
"""Currency Converter"""

class Converter:
    def __init__(self):
        self.inr_to_usd = 0.012
        self.usd_to_inr = 83.00

    def inr2usd(self, amount):
        return amount * self.inr_to_usd

    def usd2inr(self, amount):
        return amount * self.usd_to_inr

def main():
    print("=" * 60)
    print("CURRENCY CONVERTER".center(60))
    print("=" * 60)

    conv = Converter()

    while True:
        print("\n1. INR to USD")
        print("2. USD to INR")
        print("3. Exit")

        choice = input("\nChoice: ")

        if choice == '1':
            amt = float(input("Amount (INR): "))
            result = conv.inr2usd(amt)
            print(f"\n₹{amt:.2f} = ${result:.2f}")
        elif choice == '2':
            amt = float(input("Amount (USD): "))
            result = conv.usd2inr(amt)
            print(f"\n${amt:.2f} = ₹{result:.2f}")
        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
