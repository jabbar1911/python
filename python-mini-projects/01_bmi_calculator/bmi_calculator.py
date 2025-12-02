#!/usr/bin/env python3
"""BMI Calculator - Calculate Body Mass Index"""

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=" * 50)
    print("BMI CALCULATOR".center(50))
    print("=" * 50)

    try:
        weight = float(input("\nEnter weight (kg): "))
        height_cm = float(input("Enter height (cm): "))

        if weight <= 0 or height_cm <= 0:
            print("\n❌ Error: Weight & height must be positive!")
            return

        bmi = calculate_bmi(weight, height_cm)
        category = get_bmi_category(bmi)

        print("\n" + "=" * 50)
        print(f"Your BMI : {bmi:.2f}")
        print(f"Category : {category}")
        print("=" * 50)

    except ValueError:
        print("\n❌ Error: Enter valid numbers!")

if __name__ == "__main__":
    main()
