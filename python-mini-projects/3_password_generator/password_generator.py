#!/usr/bin/env python3
"""Password Generator - Create Secure Passwords"""

import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, 
                     use_digits=True, use_special=True):
    char_pool = ""

    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        return "Error: Select at least one character type!"

    return ''.join(random.choice(char_pool) for _ in range(length))

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score <= 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"

def main():
    print("=" * 60)
    print("PASSWORD GENERATOR".center(60))
    print("=" * 60)

    while True:
        try:
            length = int(input("\nPassword length (6-128): "))
            if length < 6 or length > 128:
                print("❌ Length must be 6-128!")
                continue

            password = generate_password(length)

            print("\n" + "=" * 60)
            print(f"Password: {password}")
            print(f"Strength: {check_strength(password)}")
            print("=" * 60)

            another = input("\nGenerate another? (y/n): ").lower()
            if another != 'y':
                print("\n👋 Goodbye!\n")
                break
        except ValueError:
            print("❌ Invalid input!")

if __name__ == "__main__":
    main()
