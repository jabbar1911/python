#!/usr/bin/env python3
"""Number Guessing Game"""

import random
import math

class Game:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret = random.randint(min_num, max_num)
        self.attempts = 0
        self.max_attempts = math.ceil(math.log2(max_num - min_num + 1)) + 3

    def guess(self, guess):
        self.attempts += 1

        if guess == self.secret:
            return True, f"🎉 Correct in {self.attempts} attempts!"
        elif guess < self.secret:
            return False, "📈 Too low!"
        else:
            return False, "📉 Too high!"

def main():
    print("=" * 60)
    print("NUMBER GUESSING GAME".center(60))
    print("=" * 60)

    print("\nDifficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    choice = input("\nChoice (1-3): ")

    if choice == '1':
        game = Game(1, 50)
    elif choice == '2':
        game = Game(1, 100)
    elif choice == '3':
        game = Game(1, 500)
    else:
        print("Invalid choice!")
        return

    print(f"\nGuess between {game.min_num}-{game.max_num}")
    print(f"Attempts: {game.max_attempts}\n")

    while game.attempts < game.max_attempts:
        try:
            guess = int(input("Your guess: "))
            correct, message = game.guess(guess)
            print(message)

            if correct:
                break
        except ValueError:
            print("❌ Invalid number!")

    if game.attempts >= game.max_attempts:
        print(f"\n😞 Game Over! Number was {game.secret}")

if __name__ == "__main__":
    main()
