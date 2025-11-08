#!/usr/bin/env python3
"""BMI Calculator - Calculate Body Mass Index"""

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=" * 50)
    print("BMI CALCULATOR".center(50))
    print("=" * 50)

    try:
        weight = float(input("\nEnter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        if weight <= 0 or height <= 0:
            print("\n❌ Error: Weight and height must be positive!")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print("\n" + "=" * 50)
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("=" * 50)
    except ValueError:
        print("\n❌ Error: Please enter valid numbers!")

if __name__ == "__main__":
    main()
