#!/usr/bin/env python3
"""Number Guessing Game"""

import random
import math

class Game:
    def __init__(self, lo=1, hi=100):
        self.lo = lo
        self.hi = hi
        self.num = random.randint(lo, hi)
        self.try_count = 0
        self.max_try = math.ceil(math.log2(hi - lo + 1)) + 3

    def check(self, g):
        self.try_count += 1
        if g == self.num:
            return True, f"🎉 Correct in {self.try_count} attempts!"
        if g < self.num:
            return False, "📈 Too low!"
        return False, "📉 Too high!"

def main():
    print("=" * 60)
    print("NUMBER GUESSING GAME".center(60))
    print("=" * 60)

    print("\nDifficulty:")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-500)")

    ch = input("\nChoice (1-3): ")

    if ch == '1':
        game = Game(1, 50)
    elif ch == '2':
        game = Game(1, 100)
    elif ch == '3':
        game = Game(1, 500)
    else:
        print("❌ Invalid choice!")
        return

    print(f"\nGuess between {game.lo}-{game.hi}")
    print(f"Attempts allowed: {game.max_try}\n")

    while game.try_count < game.max_try:
        try:
            g = int(input("Your guess: "))
            ok, msg = game.check(g)
            print(msg)

            if ok:
                break
        except ValueError:
            print("❌ Enter a valid number!")

    if game.try_count >= game.max_try:
        print(f"\n😞 Game Over! The number was {game.num}")

if __name__ == "__main__":
    main()
