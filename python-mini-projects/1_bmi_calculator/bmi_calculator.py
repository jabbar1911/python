#!/usr/bin/env python3
"""BMI Calculator - Calculate Body Mass Index"""

def calculate_bmi(w, h):
    return w / (h ** 2)

def get_bmi_category(b):
    if b < 18.5:
        return "Underweight"
    elif b < 25:
        return "Normal weight"
    elif b < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=" * 50)
    print("BMI CALCULATOR".center(50))
    print("=" * 50)

    try:
        w = float(input("\nEnter weight (kg): "))
        h = float(input("Enter height (m): "))

        if w <= 0 or h <= 0:
            print("\n❌ Error: Weight & height must be positive!")
            return

        bmi = calculate_bmi(w, h)
        cat = get_bmi_category(bmi)

        print("\n" + "=" * 50)
        print(f"Your BMI : {bmi:.2f}")
        print(f"Category : {cat}")
        print("=" * 50)

    except ValueError:
        print("\n❌ Error: Enter valid numbers!")

if __name__ == "__main__":
    main()
