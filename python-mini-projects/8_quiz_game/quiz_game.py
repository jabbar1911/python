#!/usr/bin/env python3
"""Quiz Game"""

import random

questions = [
    {"q": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Madrid"], "ans": 2},
    {"q": "Which planet is Red?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "ans": 1},
    {"q": "Who wrote Romeo and Juliet?", "options": ["Dickens", "Austen", "Shakespeare", "Twain"], "ans": 2},
]

def main():
    print("=" * 60)
    print("QUIZ GAME".center(60))
    print("=" * 60)

    score = 0
    q_list = random.sample(questions, min(5, len(questions)))

    for i, q in enumerate(q_list, 1):
        print(f"\nQ{i}: {q['q']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"  {j}. {opt}")

        try:
            ans = int(input("\nYour answer (1-4): ")) - 1
            if ans == q['ans']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Answer: {q['options'][q['ans']]}")
        except:
            print("Invalid!")

    print(f"\nScore: {score}/{len(q_list)}")

if __name__ == "__main__":
    main()
