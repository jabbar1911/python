#!/usr/bin/env python3
"""Password Generator - Create Secure Passwords"""

import random
import string

def gen_pwd(n=12, up=True, low=True, dig=True, sp=True):
    p = ""

    if low:
        p += string.ascii_lowercase
    if up:
        p += string.ascii_uppercase
    if dig:
        p += string.digits
    if sp:
        p += string.punctuation

    if not p:
        return "Error: Choose at least one character type!"

    return ''.join(random.choice(p) for _ in range(n))

def strength(pwd):
    s = 0
    if len(pwd) >= 8:  s += 1
    if len(pwd) >= 12: s += 1
    if any(c.islower() for c in pwd): s += 1
    if any(c.isupper() for c in pwd): s += 1
    if any(c.isdigit() for c in pwd): s += 1
    if any(c in string.punctuation for c in pwd): s += 1

    if s <= 2:
        return "Weak 🔴"
    elif s <= 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"

def main():
    print("=" * 60)
    print("PASSWORD GENERATOR".center(60))
    print("=" * 60)

    while True:
        try:
            n = int(input("\nPassword length (6-128): "))
            if n < 6 or n > 128:
                print("❌ Length must be 6–128!")
                continue

            pwd = gen_pwd(n)

            print("\n" + "=" * 60)
            print(f"Password: {pwd}")
            print(f"Strength: {strength(pwd)}")
            print("=" * 60)

            ch = input("\nGenerate another? (y/n): ").lower()
            if ch != 'y':
                print("\n👋 Goodbye!\n")
                break

        except ValueError:
            print("❌ Invalid input!")

if __name__ == "__main__":
    main()
