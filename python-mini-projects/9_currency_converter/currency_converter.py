#!/usr/bin/env python3
"""Currency Converter - Proper ₹ and $ Symbols"""

class Converter:
    def __init__(self):
        self.inr_to_usd = 0.012      # Example rate
        self.usd_to_inr = 83.00      # Example rate

    def inr2usd(self, amt):
        return amt * self.inr_to_usd

    def usd2inr(self, amt):
        return amt * self.usd_to_inr

def main():
    print("=" * 60)
    print("CURRENCY CONVERTER".center(60))
    print("=" * 60)

    c = Converter()

    while True:
        print("\n1. INR → USD")
        print("2. USD → INR")
        print("3. Exit")

        ch = input("\nChoice: ").strip()

        if ch == '1':
            try:
                amt = float(input("\nEnter Amount (₹): "))
                r = c.inr2usd(amt)
                print(f"\n₹{amt:,.2f}  =  ${r:,.2f}")
            except:
                print("⚠ Invalid amount!")

        elif ch == '2':
            try:
                amt = float(input("\nEnter Amount ($): "))
                r = c.usd2inr(amt)
                print(f"\n${amt:,.2f}  =  ₹{r:,.2f}")
            except:
                print("⚠ Invalid amount!")

        elif ch == '3':
            print("\n👋 Goodbye!\n")
            break

        else:
            print("⚠ Invalid choice! Select 1, 2, or 3.")

if __name__ == "__main__":
    main()
